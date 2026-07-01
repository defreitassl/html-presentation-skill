# Template Selection

Use this reference before creating a new HTML presentation when the user has not provided a specific layout.

## Ask Or Decide

When the task allows a quick clarification, ask one concise question:

```text
Which template should I use: general presentation, executive briefing, technical command center, interactive planner, or document dossier?
```

If the user wants speed, does not answer, or the content clearly implies a template, decide automatically and continue.

## Available Templates

| Template | File | Best for | Built-in patterns |
| --- | --- | --- | --- |
| General presentation | `assets/templates/standalone-presentation.html` | Mixed content, flexible reports, broad briefs | Sidebar, hero, summary cards, operating map, timeline, evidence table, accordions |
| Executive briefing | `assets/templates/executive-briefing.html` | Board, sponsor, leadership, decisions, policy, investments | Decision hero, KPI strip, recommendation cards, roadmap, scenario matrix, risk accordions, decision register |
| Technical command center | `assets/templates/technical-command-center.html` | Architecture, security, DevOps, platform, incident, implementation plans | System console hero, status cards, dependency map, incident timeline, tabbed runbook, validation matrix |
| Interactive planner | `assets/templates/interactive-planner.html` | Programs, launches, events, training cohorts, editorial calendars, roadmaps | Calendar controls, milestone roadmap, workstream filters, capacity board, owner table, launch checklist |
| Document dossier | `assets/templates/document-dossier.html` | Executive memos, policy notes, narrative reports, legalistic or text-heavy documents | Document cover, table of contents, paragraphs, pull quote, margin notes, evidence table, appendix accordions |

## Selection Rules

- Choose `executive-briefing.html` when the source includes decisions, recommendations, risks, budget, sponsors, governance, or leadership audience.
- Choose `technical-command-center.html` when the source includes systems, environments, services, security, architecture, incidents, dependencies, runbooks, or validation.
- Choose `interactive-planner.html` when the source includes dates, events, phases, launch plans, cohorts, campaigns, workshops, releases, calendars, or owner/workstream coordination.
- Choose `document-dossier.html` when the source is text-heavy, memo-like, policy-oriented, legalistic, or intended for async executive reading.
- Choose `standalone-presentation.html` when the source is mixed, ambiguous, or needs a balanced presentation without a dominant workflow metaphor.

## Adaptation Rules

- Treat templates as scaffolding, not fixed output. Remove sections that do not serve the source.
- Replace every placeholder with source-grounded content.
- Add new sections only when the source requires them.
- Keep interactions purposeful: tabs for mutually exclusive views, filters for repeated workstreams, accordions for secondary detail, calendar controls for date-based planning.
- If a template provides a pattern but the source lacks real data for it, convert the pattern into a simpler summary instead of inventing dates, owners, numbers, or dependencies.
- Read `references/component-library.md` when you need optional components beyond the chosen template.
