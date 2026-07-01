# HTML Presentation Skill

Português | [English](README.md)

## Sobre A Skill

HTML Presentation Skill ajuda agentes de código a transformar documentos, notas, briefs, relatórios, outlines ou conteúdo bruto em apresentações HTML autônomas e bem acabadas.

Ela guia o agente por um fluxo repetível: entender o material de origem, organizar a narrativa, escolher uma direção visual, gerar um arquivo HTML responsivo com CSS e JavaScript embutidos, adicionar interações úteis e validar o resultado.

O resultado pode substituir uma apresentação de slides ou virar uma página interna compartilhável. As apresentações podem incluir navegação, barra de progresso, cards, métricas, tabelas, timelines, abas, acordeões, seções de decisão e identidade visual quando houver assets disponíveis.

**Apresentação geral**

![Preview do Artemis Program Overview](assets/previews/artemis-program-overview.png)

[Abrir exemplo HTML](examples/artemis-program-overview.html)

**Briefing executivo**

![Preview do Artemis II Executive Briefing](assets/previews/artemis-ii-executive-briefing.png)

[Abrir exemplo HTML](examples/artemis-ii-executive-briefing.html)

**Command center técnico**

![Preview do Kubernetes Command Center](assets/previews/kubernetes-command-center.png)

[Abrir exemplo HTML](examples/kubernetes-command-center.html)

**Planner interativo**

![Preview do Artemis II Mission Planner](assets/previews/artemis-ii-mission-planner.png)

[Abrir exemplo HTML](examples/artemis-ii-mission-planner.html)

**Dossiê documental**

![Preview do WHO Ambient Air Pollution Dossier](assets/previews/who-air-pollution-dossier.png)

[Abrir exemplo HTML](examples/who-air-pollution-dossier.html)

Depois de instalar, peça ao seu agente:

```text
Use a HTML Presentation Skill para transformar este documento em uma apresentação HTML interativa e bem acabada.
```

## Instalação

Requisitos: Git e Python 3.10+.

Escolha uma opção:

**Instalação local no projeto**

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

**Instalação global**

macOS/Linux:

```bash
tmpdir="$(mktemp -d)"
git clone https://github.com/defreitassl/html-presentation-skill.git "$tmpdir"
python3 "$tmpdir/scripts/install.py" --scope global --agents all
```

Windows PowerShell:

```powershell
$tmpdir = Join-Path $env:TEMP "html-presentation-skill"
Remove-Item $tmpdir -Recurse -Force -ErrorAction SilentlyContinue
git clone https://github.com/defreitassl/html-presentation-skill.git $tmpdir
py "$tmpdir\scripts\install.py" --scope global --agents all
```
