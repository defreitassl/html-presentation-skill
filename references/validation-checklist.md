# Validation Checklist

## Automated

Run:

```bash
python3 scripts/validate_presentation.py path/to/file.html
```

Fix errors before final response. Review warnings and fix the ones that affect quality.

For examples, public artifacts, and final deliverables that should be release-ready, run:

```bash
python3 scripts/validate_presentation.py path/to/file.html --strict
```

For bundled templates that intentionally contain `{{PLACEHOLDER}}` markers, run:

```bash
python3 scripts/validate_presentation.py assets/templates/standalone-presentation.html --allow-template
```

## Manual

Check:

- The page opens directly in a browser.
- The title and first screen clearly identify the presentation.
- Navigation links all land on real sections.
- Mobile layout does not overlap or clip important text.
- Buttons and controls have visible hover/focus/active states.
- ARIA references such as `aria-controls` point to real element IDs.
- Tables scroll horizontally on small screens.
- No section feels like filler.
- The final section gives useful next steps or closure.
- The first viewport is strong but not empty spectacle.
- Each major section has a clear purpose and distinct visual rhythm.
- Cards, metrics, tables, timelines, and accordions are used for the right kind of information.
- The presentation can be scanned quickly without reading every paragraph.
- Any visual metaphor or CSS illustration clarifies the subject.

## Content

Verify:

- Source facts, numbers, names, and constraints were preserved.
- Open decisions remain visible.
- No unsupported claims were introduced.
- Dense source material was condensed without changing meaning.
- Fictional/example data is clearly marked as fictional.
- Generated summaries do not invent owners, dates, metrics, or outcomes that were not implied by the source.
- Repeated ideas from the source were merged instead of copied into multiple sections.
- Irrelevant details were omitted or moved into secondary detail.
- No section contains a large uninterrupted block of text.
- Each section has a clear reason to exist.

## Visual Quality

Verify:

- CSS variables define a coherent theme.
- Text contrast is readable.
- Font sizes are appropriate for their containers.
- Layout dimensions are stable.
- Mobile grids collapse cleanly.
- No nested-card look dominates the page.
- No generic decorative blobs, meaningless illustrations, or placeholder visuals remain.

## Brand

When using brand assets, verify:

- Logo/image paths resolve from the generated HTML location.
- Brand colors are used consistently through CSS variables.
- Text contrast remains readable.
- Private brand files are not copied into public example folders.
- Large raster images are not embedded as base64.
