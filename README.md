# HTML Presentation Skill

[Português](README.pt-BR.md) | English

Public Codex skill for creating polished, responsive, interactive HTML presentations from documents, notes, briefs, reports, outlines, or raw content.

The goal is to replace manual slide-building with a repeatable agent workflow: analyze the source, design the narrative, generate a standalone HTML presentation, add useful interactions, and validate the result.

## Install

There are only two supported install modes:

### Option 1: Local Project Install

Use this when you want the skill available only inside the current project:

```bash
tmpdir="$(mktemp -d)" && git clone https://github.com/defreitassl/html-presentation-skill.git "$tmpdir" && python3 "$tmpdir/scripts/install.py" --scope local --agents all --project .
```

This installs the skill into the current project and creates local instruction files for supported agents when applicable:

- Codex: `.codex/skills/html-presentation-skill`
- Claude Code: `CLAUDE.md`
- GitHub Copilot: `.github/copilot-instructions.md`
- Antigravity or other agents: `AGENTS.md`

### Option 2: Global Agent Install

Use this when you want the skill available globally in your agent configuration:

```bash
tmpdir="$(mktemp -d)" && git clone https://github.com/defreitassl/html-presentation-skill.git "$tmpdir" && python3 "$tmpdir/scripts/install.py" --scope global --agents codex
```

Global install currently targets Codex:

- Codex: `${CODEX_HOME:-$HOME/.codex}/skills/html-presentation-skill`

Then invoke it:

```text
Use $html-presentation-skill to transform this document into a polished interactive HTML presentation.
```

## Multi-Agent Support

The skill is native to Codex through `SKILL.md`. For Claude Code, GitHub Copilot, Antigravity, and other coding agents, use the local project install. It creates instruction bridge files that point the agent to the skill instructions.

For these agents, ask directly:

```text
Use the HTML Presentation Skill instructions in this project to create a standalone HTML presentation from this document.
```

## What It Produces

- Single-file HTML presentations by default.
- Embedded CSS and JavaScript.
- Responsive layouts.
- Navigation, progress, accordions, tabs, timelines, cards, metrics, tables, and decision sections when useful.
- Optional branded themes using logos, colors, icons, photos, and fonts already present in the user's project.
- Browser-ready output that can replace a slide deck or become a shareable internal page.

## Repository Contents

```text
SKILL.md
agents/openai.yaml
references/
assets/templates/standalone-presentation.html
install.sh
scripts/install.py
scripts/inspect_brand_assets.py
scripts/validate_presentation.py
examples/
  civic-mobility-briefing.html
  community-platform-guide.html
```

## Style Presets And Brand Assets

If you do not provide a visual direction, the skill can ask you to choose one of these presets:

- Executive briefing
- Editorial report
- Technical command center
- Community platform
- Product launch
- Training field guide
- Data dashboard
- Minimal board memo

To provide a custom brand identity, let the agent scan the current workspace or give it a specific folder path.

Workspace scan:

```bash
python3 scripts/inspect_brand_assets.py . --scan-workspace
```

Example asset location:

```text
assets/brand/
  logo.svg
  icon.png
  brand-colors.css
  product-screenshot.png
  brand-font.woff2
```

Then ask:

```text
Use $html-presentation-skill to create a presentation. First scan this workspace for existing brand or product assets. If nothing useful is found, ask me for a logo or reference image.
```

Or, if you already know the folder:

```text
Use $html-presentation-skill to create a presentation using the brand assets in assets/brand/.
```

## Validate A Presentation

```bash
python3 scripts/validate_presentation.py path/to/presentation.html
```

## Examples

- [Civic Mobility Briefing](examples/civic-mobility-briefing.html): executive briefing with sidebar navigation, dashboard-style hero, operating map, tabs, roadmap, and risk accordions.
- [Community Platform Guide](examples/community-platform-guide.html): operational guide with onboarding flow, role detail panel, channel map, governance notes, and launch checklist.

## Example Prompt

```text
Use $html-presentation-skill to create a standalone HTML presentation from this program documentation. The audience is an executive team. Keep the language in Portuguese, include a roadmap, risks, operating model, and next steps.
```

## Known Limitations

- Raster color extraction depends on Pillow. Without it, the asset scanner still reads SVG/CSS/text colors and lists image files for visual inspection.
- Multi-agent support uses local instruction bridge files; each agent may interpret project instructions differently.
- Browser-level visual validation still depends on the coding agent opening or inspecting the generated HTML.
- The generated presentation quality depends on the quality and specificity of the source material.

## License

MIT License. See [LICENSE](LICENSE).
