#!/usr/bin/env python3
"""Insert relevant internal links into an article.

Given an article and a list of candidate destination URLs (pages you want
internal links to), this fetches each URL's title/meta description for
context and asks Claude to weave in markdown hyperlinks — using only anchor
text that already exists in the article — following a fixed set of
internal-linking rules (no generic anchors, no edited prose, no linked
headings, etc).

Usage:
    export ANTHROPIC_API_KEY=sk-...
    python internal_linking.py article.md urls.txt -o article_linked.md

`urls.txt` is one candidate destination URL per line (blank lines and lines
starting with # are ignored).
"""

import argparse
import re
import sys
import urllib.request
from html.parser import HTMLParser

import anthropic

MODEL = "claude-sonnet-5"

RULES = """INTERNAL LINKING RULES:
- Only link to the candidate destination pages listed below. Never link anywhere else.
- Do not modify, rewrite, remove, or add visible article text.
- Only add markdown hyperlinks to phrases that already exist in the article.
- Never add links to headings or titles.
- Do not replace or modify existing hyperlinks.
- Use descriptive, contextually relevant anchor text drawn from the article itself.
- Keep anchor text concise, normally 2-4 words.
- Do not use generic anchors such as "click here," "learn more," or "read more."
- Link only when the destination page is genuinely relevant to the surrounding sentence.
- Avoid forcing links simply to reach the maximum number.
- Do not link the same destination repeatedly unless there is a strong contextual reason.
- Avoid placing multiple internal links excessively close together.
- Prefer links that help readers explore a closely related topic.
- Preserve the article exactly aside from the added hyperlinks."""


class _MetaParser(HTMLParser):
    """Pulls <title> and the meta description out of an HTML page."""

    def __init__(self):
        super().__init__()
        self.title = ""
        self.description = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            attrs_d = dict(attrs)
            name = (attrs_d.get("name") or attrs_d.get("property") or "").lower()
            if name in ("description", "og:description") and not self.description:
                self.description = (attrs_d.get("content") or "").strip()

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def fetch_page_info(url: str, timeout: float = 10.0) -> dict:
    """Best-effort fetch of a page's title + meta description for context."""
    req = urllib.request.Request(url, headers={"User-Agent": "internal-linking-tool/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            html = resp.read(200_000).decode("utf-8", errors="ignore")
    except Exception as exc:
        print(f"warning: could not fetch {url}: {exc}", file=sys.stderr)
        return {"url": url, "title": "", "description": ""}

    parser = _MetaParser()
    parser.feed(html)
    return {
        "url": url,
        "title": re.sub(r"\s+", " ", parser.title).strip(),
        "description": re.sub(r"\s+", " ", parser.description).strip(),
    }


def build_prompt(article: str, pages: list, max_links: int) -> str:
    page_lines = "\n".join(
        f"- {p['url']}"
        + (f' — "{p["title"]}"' if p["title"] else "")
        + (f": {p['description']}" if p["description"] else "")
        for p in pages
    )
    return f"""Your only task is to add relevant internal links to the article below.

{RULES}

CANDIDATE DESTINATION PAGES (link ONLY to these URLs, never any other page):
{page_lines}

Maximum number of links to add: {max_links}

ARTICLE:
{article}

Return the complete article, unchanged except for the added markdown \
hyperlinks. Do not wrap it in a code block and do not add any commentary."""


def add_internal_links(article: str, urls: list, max_links: int) -> str:
    pages = [fetch_page_info(url) for url in urls]
    client = anthropic.Anthropic()
    response = client.messages.create(
        model=MODEL,
        max_tokens=8000,
        messages=[{"role": "user", "content": build_prompt(article, pages, max_links)}],
    )
    return "".join(block.text for block in response.content if block.type == "text")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("article", help="Path to the article file (markdown or plain text)")
    parser.add_argument("urls", help="Path to a text file with one candidate destination URL per line")
    parser.add_argument("-m", "--max-links", type=int, default=15, help="Maximum internal links to add (default: 15)")
    parser.add_argument("-o", "--output", help="Where to write the linked article (default: stdout)")
    args = parser.parse_args()

    with open(args.article, encoding="utf-8") as f:
        article = f.read()

    with open(args.urls, encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    if not urls:
        sys.exit("no candidate URLs found in " + args.urls)

    result = add_internal_links(article, urls, args.max_links)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"wrote {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()
