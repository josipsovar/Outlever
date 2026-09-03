# Internal Linking Tool

Adds relevant internal links to an article, given a list of candidate
destination URLs (pages you want to link to). It fetches each candidate
page's title/meta description for context, then asks Claude to weave in
markdown hyperlinks using only anchor text that already exists in the
article — never rewriting prose, never linking headings, never using
generic anchors like "click here."

## Setup

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-...
```

## Usage

```bash
python internal_linking.py article.md urls.txt -o article_linked.md
```

- `article.md` — the article, markdown or plain text.
- `urls.txt` — one candidate destination URL per line (blank lines and
  lines starting with `#` are ignored).
- `-m/--max-links` — maximum links to add (default: 15).
- `-o/--output` — output file; omit to print to stdout.

The tool only links to URLs you provide in `urls.txt` — it does not crawl
or discover pages on its own.
