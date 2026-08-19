# Outlever — Executive LinkedIn Content System

This repo is a ghostwriting system. Outlever's writers use it to produce
LinkedIn thought-leadership posts on behalf of client executives. Claude Code
never publishes anything — it only produces drafts for a human writer/editor
to review and post.

## Structure

- `companies/<slug>/` — one client company's brand knowledge base:
  `overview.md`, `products-features.md`, `audience-personas.md`,
  `voice-style.md`. This is the factual/tone ground truth every executive at
  that company writes within.
- `executives/<slug>/profile.md` — voice, bio, expertise, do's/don'ts, and a
  link to their `companies/<slug>/` for one executive.
  `executives/<slug>/sample-posts.md` — real past posts, used as few-shot
  voice examples.
- `briefs/` — one file per post: angle, source material, goal.
- `drafts/<slug>/` — generated drafts, one file per post, named
  `YYYY-MM-DD-<slug>.md`.
- `.claude/skills/linkedin-post/` — the skill that generates drafts.

## Working conventions

- Always ground a draft in a real executive's `profile.md` and
  `sample-posts.md`, plus their company's knowledge base when linked. Never
  invent facts, statistics, product claims, or anecdotes not present in the
  brief, company knowledge base, or source material — flag gaps instead of
  filling them with something plausible-sounding.
- Match the executive's actual voice from their sample posts over generic
  "LinkedIn thought leadership" tone. Company `voice-style.md` sets the floor
  (never violate its red lines/compliance rules); the executive's personal
  voice sets the texture on top of it. If sample posts are sparse or
  missing, say so before drafting rather than guessing.
- Save every draft to `drafts/<slug>/`, don't just print it in chat — the
  writer needs a file to revise and hand off.
- Keep `companies/_template/`, `executives/_template/`, and
  `briefs/_template.md` as empty templates; don't fill them with real
  content.
