# Presentation Pattern Library

Use these patterns to make generated presentations feel like complete presentation products instead of static documents.

## Long-Form Presentation Shell

Use for executive briefings, implementation plans, operating guides, and large documentation summaries.

- Sticky sidebar on desktop with compact brand block and anchor navigation.
- Full-width content sections with constrained inner content.
- Progress bar fixed to the top.
- Active navigation state based on scroll position.
- Mobile navigation becomes a compact grid or horizontal band.

## First-Viewport Hero

Use a first screen that acts like the opening slide:

- Dark or strongly branded background.
- Eyebrow label for context.
- Large title.
- One concise paragraph with the promise of the presentation.
- 3-4 small tags or metrics.
- Optional visual panel showing a dashboard, document viewer, map, console, or process preview.

Keep at least a hint of the next section visible on common desktop and mobile viewports.

## Executive Summary Grid

Use 3-5 cards for the most important takeaways.

Each card should have:

- Short claim heading.
- 1-2 sentences of explanation.
- Optional metric, status, owner, or decision label.

Do not use summary cards for every paragraph.

## Operating Map

Use when the source includes platforms, teams, channels, processes, or support flows.

Recommended structure:

- Left column: inputs or user groups.
- Center: hub, system, community, service, or program.
- Right column: outputs, outcomes, or operating routines.
- Supporting cards below for ownership, dependencies, and risks.

## Roadmap

Use for implementation sequences and launch plans.

Recommended structure:

- Alternating or vertical timeline.
- Phase number, title, description, and dependency.
- Clear labels for blocker, critical, important, or optional items.
- Avoid exact dates unless provided by the source.

## Interactive Detail Panel

Use when several items share the same explanation format.

Pattern:

- A grid/list of buttons or cards.
- A detail panel updates based on selected item.
- The default active item is visible.
- Button state uses `aria-pressed` or `aria-selected`.

Good for channels, platforms, roles, risks, modules, categories, and project types.

## Accordions For Secondary Detail

Use accordions for explanations that are important but too long for the main scan path.

Good for:

- FAQ.
- Validation criteria.
- Risks and mitigations.
- Policy details.
- Operational notes.

Avoid hiding the main conclusion inside an accordion.

## Data Table Band

Use tables for dense structured content such as tracks, schedules, requirements, responsibilities, comparison criteria, or scoring rubrics.

Wrap tables in a scroll container:

```css
.table-wrap { overflow-x: auto; }
table { min-width: 720px; }
```

Include a short interpretation before or after the table so the table has a clear reason to exist. Keep wide comparison tables out of the main mobile scan path unless the wrapper is present.

## Closing Section

End with practical closure:

- Next steps.
- Decision needed.
- Validation checklist.
- Owners or dependencies.
- Download/open links when relevant.
