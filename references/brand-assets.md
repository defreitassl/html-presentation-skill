# Brand Assets

Use this guide when the user wants the presentation to follow a company, product, event, or project identity.

## Asset Folder

Do not require users to place brand files inside the skill configuration. First scan the user's actual project/workspace for existing assets.

Workspace scan:

```bash
python3 scripts/inspect_brand_assets.py . --scan-workspace
```

The user may also provide a specific asset path. Inspect that folder before designing.

Expected files:

- Logos: `.svg`, `.png`, `.jpg`, `.jpeg`, `.webp`
- Icons: `.svg`, `.png`
- Photos or screenshots: `.png`, `.jpg`, `.jpeg`, `.webp`
- Fonts: `.woff`, `.woff2`, `.ttf`, `.otf`
- Brand notes: `.css`, `.json`, `.md`, `.txt`

Explicit folder scan:

```bash
python3 scripts/inspect_brand_assets.py path/to/assets
```

Use the output to choose colors and assets. If raster palette extraction is unavailable because Pillow is not installed, still inspect SVG/CSS colors and file names, then visually inspect images when possible.

If the scan finds no useful assets, ask one concise question:

```text
Do you have a logo, brand guide, product screenshot, or reference image I should use for the visual identity?
```

If the user does not provide assets, continue with the best style preset.

## Brand Application

Apply brand identity through:

- CSS variables: `--bg`, `--surface`, `--ink`, `--muted`, `--line`, `--primary`, `--accent`, `--success`, `--warning`, `--danger`.
- Logo in sidebar or hero when provided.
- Brand colors in progress bar, active nav state, key metrics, and section markers.
- Photos/screenshots only when they clarify the subject.
- Custom fonts only when local font files are provided or the user accepts web font dependencies.

## Color Rules

- Pick 1 primary, 1 accent, and 1 support color from the brand.
- Preserve text contrast. Do not put brand colors behind body text unless contrast is sufficient.
- If the brand palette is too light, create darker accessible variants for text and navigation.
- If the brand palette is too saturated, reserve it for accents and use neutral surfaces.

## Asset Path Rules

- Use relative paths from the generated HTML file to assets.
- Do not embed large raster images as base64.
- If the output HTML will be moved, place copied assets next to it in a sibling `assets/` folder or keep all paths documented.
- Add meaningful `alt` text for logos and content images.

## Privacy

Do not copy private brand assets into public examples. Public examples should use fictional brands or CSS-only marks. When generating a presentation inside the user's project, reference existing local assets with relative paths instead of moving them unless there is a clear reason.
