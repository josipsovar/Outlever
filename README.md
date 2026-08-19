# Outlever — Executive LinkedIn Content System

A reusable system for ghostwriting LinkedIn thought-leadership posts for
Outlever's client executives, using Claude Code as the drafting engine.

## How it works

1. **Set up an executive once.** Each executive gets a folder under
   `executives/<name>/` with a `profile.md` (voice, bio, topics, do's/don'ts)
   and a `sample-posts.md` (real past posts used as voice examples).
2. **Write a brief per post.** Drop a short brief in `briefs/` describing the
   angle, source material, and goal for a specific post — copy
   `briefs/_template.md` to start.
3. **Generate.** In Claude Code, run the `linkedin-post` skill (`/linkedin-post`
   or ask Claude to "draft a LinkedIn post for <executive> about <brief>").
   Claude reads the executive's profile + samples + the brief, and writes
   2–3 draft variations into `drafts/<executive>/`.
4. **Iterate.** Give feedback in chat; Claude revises the draft in place.

## Folder structure

```
executives/
  _template/           # copy this to onboard a new executive
    profile.md
    sample-posts.md
  <executive-slug>/
    profile.md
    sample-posts.md
briefs/
  _template.md          # copy this per post
drafts/
  <executive-slug>/
    YYYY-MM-DD-<slug>.md
```

## Adding a new executive

1. `cp -r executives/_template executives/<name-slug>`
2. Fill in `profile.md` — bio, voice, tone, topics, red lines.
3. Paste 3–5 real past LinkedIn posts (by or for this person) into
   `sample-posts.md`. These are the single biggest driver of voice accuracy —
   more real examples beats more description of "tone."

## Writing a brief

Copy `briefs/_template.md`, fill it in, and reference it when asking for a
draft. A good brief has: the angle/POV, source material (article, data, a
quote, a personal anecdote), the goal, and anything that must be included.
