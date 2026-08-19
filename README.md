# Outlever — Executive LinkedIn Content System

A reusable system for ghostwriting LinkedIn thought-leadership posts for
Outlever's client executives, using Claude Code as the drafting engine.

## How it works

1. **Set up the client company once.** Each company gets a folder under
   `companies/<company-slug>/` with `overview.md`, `products-features.md`,
   `audience-personas.md`, and `voice-style.md` — the brand-level context and
   tone floor that every executive at that company writes within.
2. **Set up an executive once.** Each executive gets a folder under
   `executives/<name>/` with a `profile.md` (voice, bio, topics, do's/don'ts,
   and a link to their company) and a `sample-posts.md` (real past posts used
   as voice examples).
3. **Write a brief per post.** Drop a short brief in `briefs/` describing the
   angle, source material, and goal for a specific post — copy
   `briefs/_template.md` to start.
4. **Generate.** In Claude Code, run the `linkedin-post` skill (`/linkedin-post`
   or ask Claude to "draft a LinkedIn post for <executive> about <brief>").
   Claude reads the executive's profile + samples + their company's
   knowledge base + the brief, and writes 2–3 draft variations into
   `drafts/<executive>/`.
5. **Iterate.** Give feedback in chat; Claude revises the draft in place.

## Folder structure

```
companies/
  _template/            # copy this to onboard a new client company
    overview.md
    products-features.md
    audience-personas.md
    voice-style.md
  <company-slug>/
executives/
  _template/             # copy this to onboard a new executive
    profile.md
    sample-posts.md
  <executive-slug>/
    profile.md
    sample-posts.md
briefs/
  _template.md            # copy this per post
drafts/
  <executive-slug>/
    YYYY-MM-DD-<slug>.md
```

## Adding a new client company

1. `cp -r companies/_template companies/<company-slug>`
2. Fill in `overview.md` and `products-features.md` first — they ground
   `audience-personas.md` and `voice-style.md`, which are easier to write
   once the basics are down.

## Adding a new executive

1. `cp -r executives/_template executives/<name-slug>`
2. Fill in `profile.md` — bio, voice, tone, topics, red lines, and their
   `companies/<company-slug>/` link.
3. Paste 3–5 real past LinkedIn posts (by or for this person) into
   `sample-posts.md`. These are the single biggest driver of voice accuracy —
   more real examples beats more description of "tone."

## Writing a brief

Copy `briefs/_template.md`, fill it in, and reference it when asking for a
draft. A good brief has: the angle/POV, source material (article, data, a
quote, a personal anecdote), the goal, and anything that must be included.
