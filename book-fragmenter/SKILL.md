---
name: book-fragmenter
description: "Fragmentador Inteligente de Livros. Use para: dividir manuscritos longos em fragmentos lógicos, criar mapas de contexto para preservação de coerência narrativa e preparar textos para edição modular."
---

# Book Fragmenter

Esta skill é responsável por receber manuscritos extensos e dividi-los em fragmentos gerenciáveis, garantindo que o contexto não seja perdido durante o processo editorial modular.

## Fluxo de Trabalho

1. **Recebimento**: Aceita o manuscrito bruto em formato de texto.
2. **Análise Estrutural**: Identifica divisões lógicas (capítulos, seções) usando o script `scripts/fragmenter.py`.
3. **Geração de Contexto**: Cria um arquivo JSON de "Mapa de Contexto" para cada fragmento, contendo metadados e resumos de transição.
4. **Preservação**: Garante que as quebras respeitem a integridade semântica.

## Recursos Disponíveis

- `scripts/fragmenter.py`: Script para automação da fragmentação.
- `references/`: Guia de boas práticas para preservação de contexto narrativo.

## Como Usar

Para fragmentar um arquivo, execute o script via shell:
```bash
python3 /home/ubuntu/skills/book-fragmenter/scripts/fragmenter.py manuscrito.txt ./fragmentos/
```
