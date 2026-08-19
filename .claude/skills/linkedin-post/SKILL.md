---
name: linkedin-post
description: Draft a LinkedIn thought-leadership post ghostwritten for one of Outlever's client executives, matching their voice from profile.md and sample-posts.md. Use when asked to write, draft, or generate a LinkedIn post for a named executive, or to revise an existing draft in drafts/.
---

# LinkedIn Post Drafting

You are ghostwriting a LinkedIn post for a specific executive client of
Outlever. The output is a draft for a human writer/editor to review — never
claim it will be posted automatically, and never invent facts.

## 1. Identify the executive and brief

- Executive: look for `executives/<slug>/`. If the name given doesn't match
  an existing folder, ask which executive or offer to scaffold a new one
  from `executives/_template/` (see README.md).
- Brief: use the brief file in `briefs/` if one is referenced; otherwise use
  whatever topic/angle/source material the user gives inline. If there's no
  real source material or angle at all (just a bare topic), ask for at least
  one concrete anecdote, data point, or opinion to ground the post in —
  don't fabricate one.

## 2. Read voice and company inputs

- Read `executives/<slug>/profile.md` in full (voice, tone, do's/don'ts, red
  lines, standing facts, and the `Company knowledge base` link).
- Read `executives/<slug>/sample-posts.md`. If it has no real posts pasted in
  (still just the template header), tell the user voice-matching will be
  weaker without examples and proceed on `profile.md` alone.
- If the profile links a `companies/<company-slug>/`, read `overview.md`,
  `products-features.md`, `audience-personas.md`, and `voice-style.md` there.
  Use these for factual grounding (product claims, positioning, personas to
  target) and as the tone floor underneath the executive's personal voice —
  see the precedence note at the top of `voice-style.md`. If no company is
  linked or the folder is still the empty template, proceed on the
  executive's profile alone.

## 3. Draft

Write 2–3 distinct variations (different hooks/angles on the same brief), each following:

- **Hook (first 1–2 lines):** must stand alone before LinkedIn's "see more"
  cutoff (~210 characters). Specific and concrete, not a generic truism.
- **Body:** short paragraphs, generous line breaks, one throughline. Ground
  claims in the concrete example/data from the brief — no vague platitudes.
- **Takeaway:** the point the executive is actually making, not just a
  topic recap.
- **Close:** optional soft question or CTA only if it fits the executive's
  voice per their profile — never a generic "Thoughts?" unless that's
  actually how they write.
- **Length:** default 900–1500 characters unless the brief or profile says
  otherwise.
- **Hashtags/emoji:** only if the profile explicitly allows them; default to
  none.
- Respect every item in the executive's Don'ts/red lines section exactly.

Match sentence rhythm and first-person habits from `sample-posts.md` — prefer
copying observed patterns over inventing new ones.

## 4. Save and present

- Save to `drafts/<slug>/YYYY-MM-DD-<slug-of-topic>.md`, one file containing
  all variations clearly labeled ("Variation A / B / C").
- In chat, show the drafts and briefly note which brief/source material each
  variation leans on, plus any gaps you had to ask about instead of guessing.

## 5. Revisions

If asked to revise, edit the same draft file in place rather than creating a
new one, unless the user asks for a fresh direction.
