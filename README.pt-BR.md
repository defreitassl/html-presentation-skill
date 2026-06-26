# HTML Presentation Skill

Português | [English](README.md)

Skill pública para Codex que cria apresentações HTML bonitas, responsivas e interativas a partir de documentos, notas, briefs, relatórios, outlines ou conteúdo bruto.

O objetivo é substituir a criação manual de slides por um fluxo repetível com agente: analisar o material de origem, organizar a narrativa, gerar uma apresentação HTML autônoma, adicionar interações úteis e validar o resultado.

## Instalação

Existem apenas dois modos de instalação suportados:

### Opção 1: Instalação Local No Projeto

Use quando quiser que a skill fique disponível apenas dentro do projeto atual:

```bash
tmpdir="$(mktemp -d)" && git clone https://github.com/defreitassl/html-presentation-skill.git "$tmpdir" && python3 "$tmpdir/scripts/install.py" --scope local --agents all --project .
```

Isso instala a skill no projeto atual e cria arquivos locais de instrução para os agentes suportados quando aplicável:

- Codex: `.codex/skills/html-presentation-skill`
- Claude Code: `CLAUDE.md`
- GitHub Copilot: `.github/copilot-instructions.md`
- Antigravity ou outros agentes: `AGENTS.md`

### Opção 2: Instalação Global Nas Configurações Do Agente

Use quando quiser que a skill fique disponível globalmente nas configurações do agente:

```bash
tmpdir="$(mktemp -d)" && git clone https://github.com/defreitassl/html-presentation-skill.git "$tmpdir" && python3 "$tmpdir/scripts/install.py" --scope global --agents codex
```

No momento, a instalação global aponta para Codex:

- Codex: `${CODEX_HOME:-$HOME/.codex}/skills/html-presentation-skill`

Depois invoque a skill:

```text
Use $html-presentation-skill para transformar este documento em uma apresentação HTML interativa e bem acabada.
```

## Suporte Multi-Agente

A skill é nativa para Codex por causa do `SKILL.md`. Para Claude Code, GitHub Copilot, Antigravity e outros agentes de código, use a instalação local no projeto. Ela cria arquivos de instrução que apontam o agente para as instruções da skill.

Nesses agentes, peça diretamente:

```text
Use as instruções da HTML Presentation Skill neste projeto para criar uma apresentação HTML autônoma a partir deste documento.
```

## O Que Ela Gera

- Apresentações HTML em arquivo único por padrão.
- CSS e JavaScript embutidos.
- Layouts responsivos.
- Navegação, barra de progresso, acordeões, abas, timelines, cards, métricas, tabelas e seções de decisão quando forem úteis.
- Temas personalizados usando logos, cores, ícones, fotos e fontes já presentes no projeto do usuário.
- Arquivo pronto para abrir no navegador, substituir uma apresentação de slides ou virar uma página interna compartilhável.

## Conteúdo Do Repositório

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

## Estilos E Identidade Visual

Se você não informar uma direção visual, a skill pode perguntar qual preset você quer usar:

- Executive briefing
- Editorial report
- Technical command center
- Community platform
- Product launch
- Training field guide
- Data dashboard
- Minimal board memo

Para usar uma identidade visual própria, você pode deixar o agente escanear o workspace atual ou informar uma pasta específica.

Escanear o workspace:

```bash
python3 scripts/inspect_brand_assets.py . --scan-workspace
```

Exemplo de pasta de assets:

```text
assets/brand/
  logo.svg
  icon.png
  brand-colors.css
  product-screenshot.png
  brand-font.woff2
```

Depois peça:

```text
Use $html-presentation-skill para criar uma apresentação. Primeiro escaneie este workspace em busca de assets de marca ou produto. Se não encontrar nada útil, me pergunte por um logo ou imagem de referência.
```

Ou, se você já souber a pasta:

```text
Use $html-presentation-skill para criar uma apresentação usando os assets de marca em assets/brand/.
```

## Validar Uma Apresentação

```bash
python3 scripts/validate_presentation.py caminho/para/apresentacao.html
```

## Exemplos

- [Civic Mobility Briefing](examples/civic-mobility-briefing.html): briefing executivo com navegação lateral, hero em estilo dashboard, mapa operacional, abas, roadmap e acordeões de risco.
- [Community Platform Guide](examples/community-platform-guide.html): guia operacional com fluxo de onboarding, painel interativo de papéis, mapa de canais, governança e checklist de lançamento.

## Exemplo De Prompt

```text
Use $html-presentation-skill para criar uma apresentação HTML autônoma a partir desta documentação do programa. O público é uma equipe executiva. Mantenha o idioma em português e inclua roadmap, riscos, modelo operacional e próximos passos.
```

## Como Usar Bem

Forneça ao Codex o máximo possível do material de origem: documento, resumo, notas de reunião, briefing, transcrição, requisitos, links internos ou conteúdo colado na conversa.

Quando souber, informe também:

- público-alvo;
- idioma;
- tom desejado;
- nome do arquivo final;
- identidade visual ou cores;
- caminho da pasta de assets de marca, se existir;
- se a apresentação será usada ao vivo ou como leitura assíncrona.

Exemplo:

```text
Use $html-presentation-skill para transformar este relatório em uma apresentação HTML para uma reunião com a diretoria. Quero uma linguagem objetiva, seções de riscos e próximos passos, e um arquivo final chamado apresentacao-executiva.html.
```

## Limitações Conhecidas

- A extração de cores de imagens raster depende do Pillow. Sem ele, o scanner ainda lê cores de SVG/CSS/texto e lista imagens para inspeção visual.
- O suporte multi-agente usa arquivos locais de instrução; cada agente pode interpretar essas instruções de forma um pouco diferente.
- A validação visual em navegador ainda depende do agente abrir ou inspecionar o HTML gerado.
- A qualidade da apresentação gerada depende da qualidade e especificidade do material de origem.

## Licença

Licença MIT. Veja [LICENSE](LICENSE).
