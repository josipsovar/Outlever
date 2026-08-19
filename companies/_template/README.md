# Company Knowledge Base: [Company Name]

Reference material for one client company, used to ground executive
LinkedIn posts in real product/audience context. Executives who work at
this company should reference it (see `executives/<slug>/profile.md` →
`Company` field).

- `overview.md` — mission, business model, market position, key facts.
- `products-features.md` — what the company actually sells, feature by
  feature, in customer terms.
- `audience-personas.md` — who this company's LinkedIn content needs to
  reach and what lands with them.
- `voice-style.md` — company-level brand tone/formatting rules that sit
  underneath each executive's personal voice.

## Onboarding a new client company

1. `cp -r companies/_template companies/<company-slug>`
2. Fill in all four files. `overview.md` and `products-features.md` first —
   personas and voice are easier to write once those are grounded.
3. Link executives to this company: add `**Company:** <company-slug>` to
   each relevant `executives/<slug>/profile.md`.
