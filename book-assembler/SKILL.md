---
name: book-assembler
description: "Montador Final de Livros. Use para: reunir fragmentos editados, integrar infográficos, realizar revisão de fluidez e exportar o manuscrito finalizado."
---

# Book Assembler

Esta é a skill final do ecossistema, responsável por consolidar todo o trabalho de edição e design em um manuscrito coeso e pronto para publicação.

## Funcionalidades

1. **Recomposição**: Une os fragmentos editados na ordem correta.
2. **Integração Visual**: Insere as propostas de infográficos nos locais sugeridos.
3. **Revisão de Fluidez**: Analisa transições e consistência tonal.
4. **Exportação**: Gera arquivos em formatos padrão (Markdown, PDF, e-book).

## Fluxo de Trabalho

1. **Input**: Recebe a pasta de fragmentos editados e os arquivos de proposta de infográfico.
2. **Processamento**: Executa o script `scripts/assembler.py`.
3. **Finalização**: Aplica formatação final e gera o sumário.

## Recursos Disponíveis

- `scripts/assembler.py`: Script para montagem automática do livro.
- `templates/`: Modelos de formatação para diferentes tipos de publicação.
