# HTML Presentation Skill

[Português](README.pt-BR.md) | English

## About The Skill

HTML Presentation Skill helps coding agents turn documents, notes, briefs, reports, outlines, or raw content into polished standalone HTML presentations.

It guides the agent through a repeatable workflow: understand the source material, shape the narrative, choose a visual direction, generate a responsive HTML file with embedded CSS and JavaScript, add useful interactions, and validate the result.

The output is designed to replace a slide deck or become a shareable internal page. Presentations can include navigation, progress indicators, cards, metrics, tables, timelines, tabs, accordions, decision sections, and branded visuals when assets are available.

![Civic Mobility Briefing preview](assets/previews/civic-mobility-briefing.png)

![Community Platform Guide preview](assets/previews/community-platform-guide.png)

After installing, ask your agent:

```text
Use the HTML Presentation Skill to transform this document into a polished interactive HTML presentation.
```

## Install

Requirements: Git and Python 3.10+.

There are two install options:

- **Option 1: Local Project Install**: recommended for most users. The skill is installed inside one project and can support Codex, Claude Code, GitHub Copilot, and Antigravity/generic agents.
- **Option 2: Global Codex Install**: installs the skill into the Codex home folder so Codex can use it across projects.

**Option 1: Local Project Install**

Run this from the project where the coding agent will work.

macOS/Linux:

```bash
tmpdir="$(mktemp -d)"
git clone https://github.com/defreitassl/html-presentation-skill.git "$tmpdir"
python3 "$tmpdir/scripts/install.py" --scope local --agents all --project .
```

Windows PowerShell:

```powershell
$tmpdir = Join-Path $env:TEMP "html-presentation-skill"
Remove-Item $tmpdir -Recurse -Force -ErrorAction SilentlyContinue
git clone https://github.com/defreitassl/html-presentation-skill.git $tmpdir
py "$tmpdir\scripts\install.py" --scope local --agents all --project .
```

If `py` is not available on Windows, use `python`.

Local agent targets:

| Agent | Install value | Files created or updated |
| --- | --- | --- |
| Codex | `codex` | `.codex/skills/html-presentation-skill` |
| Claude Code | `claude` | `.codex/skills/html-presentation-skill`, `CLAUDE.md` |
| GitHub Copilot | `copilot` | `.codex/skills/html-presentation-skill`, `.github/copilot-instructions.md` |
| Antigravity / generic agents | `antigravity` | `.codex/skills/html-presentation-skill`, `AGENTS.md` |
| All supported agents | `all` | All files above |

To install for only one agent, replace `all`:

```bash
python3 scripts/install.py --scope local --agents codex --project .
python3 scripts/install.py --scope local --agents claude --project .
python3 scripts/install.py --scope local --agents copilot --project .
python3 scripts/install.py --scope local --agents antigravity --project .
```

When running from a cloned copy of this repository, preview or update an install:

```bash
python3 scripts/install.py --scope local --agents all --project . --dry-run
python3 scripts/install.py --scope local --agents all --project . --force
```

**Option 2: Global Codex Install**

Use this when you want Codex to find the skill from any project. Global install currently targets Codex only.

macOS/Linux:

```bash
tmpdir="$(mktemp -d)"
git clone https://github.com/defreitassl/html-presentation-skill.git "$tmpdir"
python3 "$tmpdir/scripts/install.py" --scope global --agents codex
```

Windows PowerShell:

```powershell
$tmpdir = Join-Path $env:TEMP "html-presentation-skill"
Remove-Item $tmpdir -Recurse -Force -ErrorAction SilentlyContinue
git clone https://github.com/defreitassl/html-presentation-skill.git $tmpdir
py "$tmpdir\scripts\install.py" --scope global --agents codex
```

Global Codex target:

```text
${CODEX_HOME:-$HOME/.codex}/skills/html-presentation-skill
```
