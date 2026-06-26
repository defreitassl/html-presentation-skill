# Workflow

## 1. Intake

Identify:

- Audience: executive, technical, public, student, internal operations, sales, or mixed.
- Goal: inform, persuade, train, align, decide, launch, report, or document.
- Presentation setting: live meeting, async reading, public page, internal reference, or kiosk.
- Required output path and filename.
- Brand constraints, assets, colors, logos, and language.
- Preferred style preset or visual direction.

If the user gives no filename, choose a descriptive kebab-case name.

If the user does not specify style, ask one concise question with preset options. If the user wants fast execution or gives no answer, choose a preset based on the audience and content.

For brand identity, prefer this order:

1. Use the explicit asset path the user provides.
2. If no path is provided, scan the workspace for likely brand, logo, image, style, screenshot, and font files.
3. If nothing useful is found, ask whether the user has a logo, reference image, brand guide, or product screenshot.
4. If the user has no assets, choose a style preset and build a tasteful CSS-only identity.

Workspace scan:

```bash
python3 scripts/inspect_brand_assets.py . --scan-workspace
```

Explicit folder scan:

```bash
python3 scripts/inspect_brand_assets.py path/to/assets
```

## 2. Source Analysis

Extract these before writing HTML:

- Main thesis.
- 5-12 major sections.
- Key facts and numbers.
- Actors, systems, roles, teams, or audiences.
- Process steps, timeline, dependencies, and risks.
- Decisions already made.
- Open questions and pending work.

For a long source, create a short internal outline first. Do not expose this outline unless useful.

## 3. Narrative Shape

Use one of these shapes:

- Executive briefing: context, systems, plan, risks, decisions, next steps.
- Product or program overview: promise, user journey, capabilities, operations, roadmap.
- Technical guide: architecture, setup, workflows, edge cases, validation.
- Training guide: objective, concepts, steps, examples, checks, reference.
- Proposal: problem, opportunity, solution, implementation, investment, ask.

## 4. HTML Build

Default to a single `.html` file with:

- Semantic landmarks: `header`, `nav`, `main`, `section`, `article`, `footer`.
- Embedded `<style>` and `<script>`.
- Responsive CSS using grid/flex, `clamp()`, and practical breakpoints.
- Sidebar or top navigation for more than 5 sections.
- IDs for every navigable section.
- Accessible button semantics for tabs, accordions, filters, and toggles.
- CSS variables derived from either the selected preset or detected brand assets.
- Relative asset paths for logos, icons, photos, and fonts.

## 5. Review Loop

After generating the file:

- Scan the HTML for placeholders and repeated generic wording.
- Verify internal links match section IDs.
- Check that each interaction has a visible state.
- Run the validation script.
- If possible, inspect the page in a browser at desktop and mobile sizes.
