---
name: html-presentation-skill
description: Create polished, responsive, interactive HTML presentations from documents, notes, briefs, reports, outlines, transcripts, or raw content. Use when Codex needs to turn source material into a standalone HTML presentation that can replace slides, with strong information architecture, visual hierarchy, navigation, embedded CSS/JS, and browser-ready validation.
---

# HTML Presentation Skill

## Core Workflow

Build a standalone HTML presentation from source material.

1. Inspect the source content and identify audience, purpose, key decisions, constraints, risks, and level of detail.
2. Identify the desired visual direction, brand assets, color constraints, and preferred style preset.
3. Build a narrative matrix before writing HTML: sections, section purpose, key message, evidence/details, and best visual pattern.
4. Choose section patterns that match the content: hero, executive summary, roadmap, comparison, process flow, metrics, table, FAQ, dashboard, embedded document, or decision checklist.
5. Design a visual system with CSS variables, layout rhythm, typography scale, component rules, and responsive behavior.
6. Generate one browser-ready `.html` file with embedded CSS and JavaScript unless the user requests a framework.
7. Add useful interaction only where it improves scanning, comparison, exploration, or comprehension.
8. Validate the file before handing it off.

Read `references/workflow.md` for the full execution sequence.

## Output Standard

Create an artifact that can replace a slide deck:

- Single HTML file by default.
- Responsive layout for desktop and mobile.
- Clear navigation for long presentations.
- Strong first screen with title, context, and main promise.
- Section rhythm that alternates dense content with visual summaries.
- At least one custom visual composition that reflects the domain, such as a dashboard preview, process map, role map, score panel, document viewer, or system diagram.
- Readable body text, stable spacing, and no layout shifts caused by hover states, buttons, labels, cards, or dynamic content.
- Embedded CSS and minimal JavaScript.
- No placeholder copy, lorem ipsum, unused controls, broken anchors, generic decorative filler, unsupported claims, or fake data presented as real.
- No repeated content, redundant sections, oversized text blocks, or low-value details that make the presentation harder to scan.

Use `assets/templates/standalone-presentation.html` as a starting point when creating a new file from scratch.

## Style And Brand Intake

When the user has not specified a visual direction, ask one concise style question before building if the task allows it. Offer a few presets instead of asking open-ended design questions. If the user wants speed or does not answer, choose the best preset for the content and audience.

Use these preset families:

- Executive briefing
- Editorial report
- Technical command center
- Community platform
- Product launch
- Training field guide
- Data dashboard
- Minimal board memo

For branded presentations, first scan the user's workspace for existing brand or product assets. Use a user-provided path when given. Do not require users to copy assets into the skill folder.

```bash
python3 scripts/inspect_brand_assets.py . --scan-workspace
```

If no useful assets or colors are found, ask whether the user has a logo, screenshot, product image, brand guide, or reference image to use. Continue with an appropriate preset if they do not.

Read `references/style-presets.md` for preset selection.
Read `references/brand-assets.md` for brand asset handling.

## Quality Bar

Do not ship a generic page. Before finalizing, check that the presentation has:

- A coherent narrative arc from context to conclusion.
- Section headings that communicate meaning, not labels only.
- Visual hierarchy that lets a reader scan the page in under 60 seconds.
- Enough density to be useful in a real meeting, without dumping raw document text.
- Interactions that reveal or organize content, not decorative motion.
- Mobile layouts with no overlapping text, clipped controls, or unreadable tables.
- Tight editing: repeated ideas are merged, irrelevant details are removed, and long sections are split into cards, tables, flows, accordions, or summary/detail layers.

## Content Architecture

Start with structure, not styling.

- Preserve facts, constraints, risks, numbers, names, and decisions from the source.
- Group related details into sections that a stakeholder can scan quickly.
- Turn long paragraphs into cards, tables, timelines, accordions, or decision lists.
- Put caveats and pending decisions near the relevant section instead of hiding them at the end.
- Use concise headings that describe the point of each section.
- Remove duplication aggressively. If the source repeats an idea, present it once in the strongest location.
- Exclude details that do not affect understanding, decisions, risks, workflow, or next steps.
- Never place a large wall of text in one section; split or compress it.

Read `references/content-architecture.md` when the source is long, messy, legalistic, technical, or multi-audience.

## Visual And Interaction Patterns

Favor purposeful presentation patterns:

- Use side navigation, scroll progress, tabs, accordions, filters, timelines, metrics, and embedded viewers when they make the content easier to understand.
- Use restrained color systems with clear contrast.
- Avoid landing-page filler, decorative blobs, oversized cards for every section, and one-note color palettes.
- Do not put important text into images.

Read `references/visual-patterns.md` before designing the visual system.
Read `references/interaction-patterns.md` before adding JavaScript interactions.
Read `references/presentation-pattern-library.md` when choosing reusable section layouts for a realistic presentation.

## Validation

Before final response:

1. Run the presentation through `scripts/validate_presentation.py`.
2. If a dev server or browser validation is appropriate, open the page and inspect desktop and mobile layouts.
3. Fix critical warnings: missing title, missing viewport, broken internal anchors, empty buttons, unresolved placeholders, horizontal overflow risks, or missing navigation in long documents.

Use:

```bash
python3 scripts/validate_presentation.py path/to/presentation.html
```

Read `references/validation-checklist.md` for manual review criteria.
