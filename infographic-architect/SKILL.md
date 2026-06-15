---
name: infographic-architect
description: "Arquiteto de Infográficos. Use para: analisar densidade informacional, propor elementos visuais estratégicos e gerar conceitos de infográficos para livros."
---

# Infographic Architect

Esta skill analisa fragmentos de texto para identificar oportunidades de melhoria na compreensão do leitor através de elementos visuais.

## Funcionalidades

1. **Análise de Densidade**: Identifica seções complexas ou abstratas que necessitam de suporte visual.
2. **Proposição de Design**: Sugere tipos de infográficos (linhas do tempo, fluxogramas, comparativos).
3. **Geração de Conceito**: Descreve os dados e rótulos necessários para a criação do infográfico.

## Fluxo de Trabalho

1. **Input**: Recebe o fragmento editado pela `book-editor-pro`.
2. **Análise**: Executa o script `scripts/infographic_generator.py` para detectar padrões.
3. **Output**: Gera uma proposta detalhada com a localização ideal para inserção no texto.

## Recursos Disponíveis

- `scripts/infographic_generator.py`: Ferramenta de análise de texto para sugestões visuais.
- `references/visual_patterns.md`: Catálogo de tipos de infográficos e quando usá-los.
