# HTML Presentation Skill

Português | [English](README.md)

## Sobre A Skill

HTML Presentation Skill ajuda agentes de código a transformar documentos, notas, briefs, relatórios, outlines ou conteúdo bruto em apresentações HTML autônomas e bem acabadas.

Ela guia o agente por um fluxo repetível: entender o material de origem, organizar a narrativa, escolher uma direção visual, gerar um arquivo HTML responsivo com CSS e JavaScript embutidos, adicionar interações úteis e validar o resultado.

O resultado pode substituir uma apresentação de slides ou virar uma página interna compartilhável. As apresentações podem incluir navegação, barra de progresso, cards, métricas, tabelas, timelines, abas, acordeões, seções de decisão e identidade visual quando houver assets disponíveis.

![Preview do Civic Mobility Briefing](assets/previews/civic-mobility-briefing.png)

![Preview do Community Platform Guide](assets/previews/community-platform-guide.png)

Depois de instalar, peça ao seu agente:

```text
Use a HTML Presentation Skill para transformar este documento em uma apresentação HTML interativa e bem acabada.
```

## Instalação

Requisitos: Git e Python 3.10+.

Existem duas opções de instalação:

- **Opção 1: Instalação Local No Projeto**: recomendada para a maioria dos usuários. A skill é instalada dentro de um projeto e pode atender Codex, Claude Code, GitHub Copilot e Antigravity/agentes genéricos.
- **Opção 2: Instalação Global Para Codex**: instala a skill na pasta global do Codex para uso em vários projetos.

**Opção 1: Instalação Local No Projeto**

Execute a partir do projeto onde o agente de código vai trabalhar.

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

Se `py` não estiver disponível no Windows, use `python`.

Alvos locais de agente:

| Agente | Valor de instalação | Arquivos criados ou atualizados |
| --- | --- | --- |
| Codex | `codex` | `.codex/skills/html-presentation-skill` |
| Claude Code | `claude` | `.codex/skills/html-presentation-skill`, `CLAUDE.md` |
| GitHub Copilot | `copilot` | `.codex/skills/html-presentation-skill`, `.github/copilot-instructions.md` |
| Antigravity / agentes genéricos | `antigravity` | `.codex/skills/html-presentation-skill`, `AGENTS.md` |
| Todos os agentes suportados | `all` | Todos os arquivos acima |

Para instalar para apenas um agente, substitua `all`:

```bash
python3 scripts/install.py --scope local --agents codex --project .
python3 scripts/install.py --scope local --agents claude --project .
python3 scripts/install.py --scope local --agents copilot --project .
python3 scripts/install.py --scope local --agents antigravity --project .
```

Quando estiver executando a partir de um clone deste repositório, pré-visualize ou atualize uma instalação:

```bash
python3 scripts/install.py --scope local --agents all --project . --dry-run
python3 scripts/install.py --scope local --agents all --project . --force
```

**Opção 2: Instalação Global Para Codex**

Use quando quiser que o Codex encontre a skill a partir de qualquer projeto. A instalação global atualmente atende apenas Codex.

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

Destino global do Codex:

```text
${CODEX_HOME:-$HOME/.codex}/skills/html-presentation-skill
```
