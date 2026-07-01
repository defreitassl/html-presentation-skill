# Agent Decisions

Use this reference when the user leaves implementation details unspecified. Make conservative decisions that preserve momentum and avoid unnecessary clarification.

## Defaults

- Filename: choose a descriptive kebab-case `.html` name from the subject, such as `program-briefing.html`.
- Language: match the source language. If the source mixes languages, use the language of the user's request.
- Style: choose the preset that fits audience and material when the user wants speed or does not answer.
- Template: choose the bundled template that fits the source, or use `standalone-presentation.html` when no dominant structure is clear.
- Output: create one standalone HTML file with embedded CSS and JavaScript.
- Navigation: add sidebar or top navigation when the presentation has 5 or more sections.
- Brand: scan the workspace for likely brand assets unless the user provides an explicit asset path.
- Assets: reference local assets with relative paths; do not embed large raster images as base64.
- Data: preserve provided facts, numbers, owners, dates, caveats, and pending decisions. Do not invent missing values.
- Validation: run the validator in normal mode for drafts and `--strict` for examples, public artifacts, or release-ready deliverables.

## Template Selection

- Decision, leadership, risk, recommendation, sponsor, or budget material: use `executive-briefing.html`.
- Architecture, systems, security, platform, incident, runbook, or implementation material: use `technical-command-center.html`.
- Dates, events, launch plans, cohorts, campaigns, calendars, releases, or owner/workstream coordination: use `interactive-planner.html`.
- Text-heavy, memo-like, legalistic, policy, research, or async executive reading material: use `document-dossier.html`.
- Mixed or ambiguous material: use `standalone-presentation.html`.

## Preset Selection

- Executive, board, sponsor, investor, or decision material: use `executive briefing`.
- Research, policy, strategy, or narrative-heavy reports: use `editorial report`.
- Architecture, DevOps, security, platform, or incident material: use `technical command center`.
- Community, cohort, support, volunteer, education, or member operations: use `community platform`.
- Product, GTM, launch, demo, or sales enablement: use `product launch`.
- SOP, tutorial, course, workshop, or onboarding: use `training field guide`.
- Metrics, OKRs, analytics, or monitoring: use `data dashboard`.
- Formal decision memo with little decoration: use `minimal board memo`.

## Clarification Rules

Ask one concise question only when the missing answer would materially change the artifact. Good reasons to ask include:

- The user requires a specific brand but no assets, colors, or references are available.
- The output location matters and cannot be inferred from the workspace.
- The source contains conflicting facts, dates, names, or requirements.
- The presentation is for a regulated, legal, financial, medical, or public claim where unsupported inference would be risky.

Otherwise, proceed with the best default and state the assumption briefly in the final response.

## Handling Uncertainty

- Mark unresolved decisions as `Pending` or `To confirm` near the relevant section.
- Use qualitative labels when exact values are absent.
- If examples or mock data are useful, label them clearly as illustrative.
- Do not convert ambiguous source text into stronger claims.
- Do not hide caveats in appendices when they affect decisions, scope, risk, cost, eligibility, dates, or ownership.
