# Visual Patterns

## Design Goals

Make the presentation feel intentional, not like a generic generated page.

- Use a small color system: background, surface, ink, muted, line, primary, accent, success/warning/danger when needed.
- Use consistent radius, spacing, and shadow scale.
- Use high contrast for body text.
- Use stable layout dimensions for cards, controls, timelines, boards, and embedded viewers.
- Keep cards for repeated items, modals, or framed tools. Do not wrap every page section in a card.
- Define CSS variables at `:root` and build the entire theme from them.
- Use real layout structure instead of decorative wrappers.

## Visual System Requirements

Every presentation should define:

- Color tokens: `--bg`, `--surface`, `--surface-2`, `--ink`, `--muted`, `--line`, `--primary`, `--accent`, and optional status colors.
- Typography scale: hero title, section heading, card heading, body, small labels.
- Spacing scale: section padding, grid gap, card padding, compact controls.
- Radius and shadow scale.
- Component states: default, hover, active, focus-visible, disabled if applicable.
- Responsive breakpoints for sidebar, grids, tables, and hero visuals.

## Recommended Layouts

- Long presentation: sticky sidebar plus full-width sections.
- Executive report: dark or branded hero, section bands, metrics, tables, roadmap.
- Training guide: top progress, step navigation, examples, accordions, checklists.
- Technical system overview: architecture board, process lanes, risk table, validation checklist.

## Presentation Identity

Each generated presentation should have a distinct identity system:

- Choose a domain-specific visual metaphor: control room, editorial dossier, field manual, command center, atlas, lab notebook, operations board, civic dashboard, launch room, or workshop manual.
- Define typography, spacing, color, and component rhythm from that metaphor.
- Use at least one custom visual composition made with HTML/CSS, such as a dashboard preview, channel map, roadmap, score panel, document viewer, or system map.
- Keep the presentation usable and dense enough for real stakeholder review.
- Repeat the identity subtly through section markers, cards, controls, and visual diagrams.

## First View

The first viewport should immediately show:

- Presentation title.
- Who or what it is about.
- Why it matters.
- Visual signal of the domain or system.
- At least a hint of the next content on common desktop and mobile sizes.

Avoid hero sections that feel like marketing splash screens when the task is a working presentation. The hero should start the presentation, not delay it.

## Layout Rules

- Prefer full-width section bands with constrained inner content.
- Use sticky sidebar or top navigation for long presentations.
- Keep fixed-format UI elements stable with explicit `min-height`, grid tracks, or aspect ratios.
- Ensure hover/active states do not resize cards, buttons, timeline nodes, or nav items.
- Use `overflow-x: auto` wrappers for tables and wide diagrams.
- Keep mobile layouts single-column where needed, with controls still easy to tap.
- Do not put cards inside cards.
- Do not use viewport-width font sizes; use `clamp()` with rem/px boundaries if scaling is needed.

## Typography

- Use readable system fonts unless a brand font is available.
- Pair a more expressive display face with a readable body face only when it matches the tone.
- Do not use negative letter spacing.
- Keep button and card text sized to fit.
- Avoid all-caps body text; reserve uppercase for short labels.

## Avoid

- Lorem ipsum or placeholder UI.
- Decorative gradient blobs, bokeh, or meaningless abstract SVGs.
- One-color themes dominated by purple, beige, dark blue, or brown.
- Overly large type inside compact UI.
- Negative letter spacing.
- Text over busy images without contrast treatment.
- Repeated cards with identical rhythm for the entire page.
- Tiny nav-only branding where the subject is unclear.
- Generic icons or emoji as the main visual system.
- Visual assets that are dark, blurred, cropped, or impossible to inspect when the subject matters.

## Assets

Use provided logos and images when available. If no assets exist, build tasteful CSS visuals that represent the content: dashboards, timelines, process maps, channel maps, terminal windows, document viewers, or scoreboards.

When brand assets exist, do not default to a generic palette. Extract or inspect the brand colors, then adapt them into an accessible presentation system. Keep brand color usage strongest in the hero, sidebar, progress bar, active controls, section markers, and key metrics.
