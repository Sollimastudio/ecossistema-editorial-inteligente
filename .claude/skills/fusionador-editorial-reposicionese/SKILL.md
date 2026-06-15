---
name: fusionador-editorial-reposicionese
description: Skill para fundir a base textual limpa, o PDF visual original e o template editorial premium do livro Reposicione-se sem perder conteudo nem quebrar o layout.
---

# Skill - Fusionador Editorial Reposicione-se

Use esta skill quando a tarefa for criar uma versao unificada do livro a partir de mais de uma fonte.

## Fontes principais

1. Texto limpo: `reposicionese_v02_limpeza_estrutura.md`
2. Visual aprovado: `REPOSICIONESE_melhor versão até agora(1).pdf`
3. Template editorial premium: arquivo de estilos a ser criado

## Missao

Unir texto, estrutura, infograficos e diagramação sem transformar o livro em colagem.

## Regras de fusao

- O texto editavel manda na estrutura.
- O PDF original manda nas artes visuais aprovadas.
- O template premium manda em fonte, margem, respiro e hierarquia.
- Nenhum infografico entra sem ID e local definido.
- Nenhum bloco visual entra apenas porque existia no PDF original.
- Nenhum trecho textual e apagado sem registro.

## Processo

1. Criar mapa de fusao visual.
2. Extrair artes do PDF original.
3. Associar cada arte a uma seção do manuscrito.
4. Criar grade de controle.
5. Gerar preview curto primeiro.
6. Rodar QA visual.
7. So depois gerar livro inteiro.

## Saida esperada

- `MAPA_DE_FUSAO_VISUAL.md`
- `GRADE_QA_EDITORIAL.md` ou planilha
- preview curto aprovado
- versao integral somente depois do preview aprovado

## Regra final

Fusao editorial nao e misturar arquivo.
E casamento com separacao de bens: cada fonte entra com sua função e nenhuma invade o papel da outra.
