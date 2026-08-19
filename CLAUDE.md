# Outlever — Executive LinkedIn Content System

This repo is a ghostwriting system. Outlever's writers use it to produce
LinkedIn thought-leadership posts on behalf of client executives. Claude Code
never publishes anything — it only produces drafts for a human writer/editor
to review and post.

## Structure

- `executives/<slug>/profile.md` — voice, bio, expertise, do's/don'ts for one
  executive. `executives/<slug>/sample-posts.md` — real past posts, used as
  few-shot voice examples.
- `briefs/` — one file per post: angle, source material, goal.
- `drafts/<slug>/` — generated drafts, one file per post, named
  `YYYY-MM-DD-<slug>.md`.
- `.claude/skills/linkedin-post/` — the skill that generates drafts.

## Working conventions

- Always ground a draft in a real executive's `profile.md` and
  `sample-posts.md`. Never invent facts, statistics, or anecdotes not present
  in the brief or source material — flag gaps instead of filling them with
  something plausible-sounding.
- Match the executive's actual voice from their sample posts over generic
  "LinkedIn thought leadership" tone. If sample posts are sparse or missing,
  say so before drafting rather than guessing.
- Save every draft to `drafts/<slug>/`, don't just print it in chat — the
  writer needs a file to revise and hand off.
- Keep `executives/_template/` and `briefs/_template.md` as empty templates;
  don't fill them with real content.
