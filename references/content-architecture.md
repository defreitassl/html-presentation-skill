# Content Architecture

## Narrative Matrix

Before writing HTML, form a compact narrative matrix:

| Section | Purpose | Key message | Evidence/details | Best pattern |
| --- | --- | --- | --- | --- |
| Opening | Establish context | What this presentation is about and why now | Audience, scope, stakes | Hero |
| Summary | Give the answer first | 3-5 conclusions or decisions | Facts, metrics, constraints | Summary cards |
| Body | Explain the system or plan | How it works and what matters | Flows, roles, timelines | Maps, tables, roadmaps |
| Risks | Build trust | What could fail and how to mitigate | Owners, severity, mitigations | Risk board or accordions |
| Close | Drive action | What happens next | Decisions, owners, dates | Checklist or action cards |

The matrix is thinking scaffolding. Do not expose it unless the user asks.

## Section Patterns

Choose patterns based on the source material:

- Hero: title, core promise, context, 2-4 quick tags.
- Executive summary: 3-5 cards with the most important conclusions.
- System map: actors, platforms, integrations, responsibilities.
- Process flow: ordered steps with inputs, outputs, and owner.
- Timeline or roadmap: phases, dependencies, milestones, decision gates.
- Comparison: options, tradeoffs, criteria, recommendation.
- Metrics: numbers with labels and interpretation.
- Risk board: risk, impact, mitigation, owner.
- Operating model: roles, routines, escalation, SLAs.
- FAQ or accordion: detailed explanations that should not dominate the page.
- Next steps: concrete actions, sequencing, owners, unresolved dependencies.

## Section Ordering

Prefer one of these flows:

- Decision briefing: hero, executive summary, context, options, recommendation, risks, next steps.
- Operating guide: hero, principles, journey, roles, workflows, governance, launch checklist.
- Technical overview: hero, architecture, data/control flow, components, failure modes, runbook, validation.
- Product launch: hero, audience/problem, value proposition, features, rollout, enablement, success metrics.
- Training: hero, learning goals, concept map, modules, exercises, checks, reference.

## Condensing Long Documents

When source material is verbose:

- Keep the exact meaning; compress wording.
- Move examples into expandable details if they are useful but secondary.
- Convert repeated paragraphs into a table or checklist.
- Surface unresolved decisions as visible pending items.
- Avoid turning every paragraph into a card.
- Keep the main scan path concise; put secondary detail in accordions, tabs, tables, or appendices.
- Preserve important qualifiers such as deadlines, eligibility, scope limits, dependencies, and unresolved approvals.

## Repetition And Relevance

Edit aggressively before designing.

- If the same idea appears in multiple source sections, merge it into one clear statement.
- If two sections have the same purpose, combine them.
- If a detail does not change the reader's understanding, decision, risk assessment, workflow, or next action, omit it.
- If a detail is useful but secondary, move it to an accordion, footnote-style note, appendix section, or compact table.
- Do not repeat the same metric, claim, caveat, or next step in multiple cards.
- Do not create separate sections just because the source has separate headings.

The presentation should feel curated, not transcribed.

## Text Block Limits

Avoid walls of text.

- Hero paragraph: 1-2 short sentences.
- Section lead: 1-2 sentences.
- Card body: 1-3 short sentences.
- Accordion content: 1 concise paragraph or a short list.
- Table cells: concise phrases, not full paragraphs.

If a section needs more explanation, split it into:

- summary cards plus an accordion;
- a flow plus detail panel;
- a table plus short interpretation;
- a roadmap plus risk notes;
- a main section plus appendix/reference section.

## Headings

Write headings as claims or clear labels:

- Prefer: `Entrada controlada por dados, cargos e convites.`
- Avoid: `Sobre o onboarding`

For executive decks, put the implication in the heading and the detail in body text.

Heading rules:

- H1 names the subject, product, program, report, or decision.
- H2 states the section's main point when possible.
- H3 labels individual cards, roles, risks, steps, or metrics.
- Avoid repeated generic headings such as "Overview", "Details", "Information", and "More".

## Density And Readability

- Use cards for repeated units, not for every section.
- Keep card body text to 1-3 short sentences.
- Use tables when the reader needs comparison, ownership, criteria, or structured detail.
- Use metric cards only when the number changes interpretation.
- Do not create empty decorative cards.
- Break long pages into clear bands with enough whitespace, but keep content dense enough for stakeholder review.
- Prefer fewer stronger sections over many repetitive sections.
- Every visible block should earn its space.

## Tables

Use tables for dense structured comparisons. Add horizontal scroll wrappers on mobile. Keep table headers short.

Each table should have:

- A clear reason to exist.
- Short headers.
- Row labels that can be scanned quickly.
- Mobile overflow handling.

Avoid tables for prose that would be clearer as a flow or cards.

## Language

Match the source language. If the source is Portuguese, write the presentation in Portuguese unless the user asks otherwise.
