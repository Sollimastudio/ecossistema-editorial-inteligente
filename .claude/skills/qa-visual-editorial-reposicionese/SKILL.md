---
name: qa-visual-editorial-reposicionese
description: Skill de controle de qualidade visual para bloquear entregas do Reposicione-se com paginas vazias, fonte pequena, graficos ausentes, hierarquia ruim ou layout quebrado.
---

# Skill - QA Visual Editorial Reposicione-se

Use esta skill antes de entregar qualquer PDF, DOCX ou preview visual do livro Reposicione-se.

## Missao

Impedir que uma versao visual ruim seja entregue como se estivesse pronta.

## Verificacoes obrigatorias

1. Conferir se ha paginas vazias ou quase vazias.
2. Conferir se as paginas visuais prometidas aparecem de fato.
3. Conferir se infograficos estao legiveis no celular.
4. Conferir se titulos, subtitulos e corpo possuem hierarquia clara.
5. Conferir se a fonte do corpo esta confortavel.
6. Conferir se paginas de abertura parecem intencionais, nao erro.
7. Conferir se o sumario esta limpo.
8. Conferir se imagens nao foram inseridas como paginas duplicadas sem funcao.
9. Conferir se o PDF gerado nao aumentou paginas sem motivo.
10. Conferir se cada grafico tem funcao editorial.

## Bloqueios automaticos

Bloqueie a entrega se:

- houver paginas vazias sem intencao;
- houver promessas de infografico sem imagem visivel;
- a fonte estiver pequena demais;
- o arquivo tiver mais paginas que a fonte sem justificativa;
- a hierarquia visual estiver confusa;
- houver texto grudado em titulo;
- o preview parecer tecnico, nao editorial.

## Saida esperada

Antes de qualquer entrega, gerar:

- resumo de problemas;
- tabela de QA;
- paginas criticas;
- decisao: aprovado, aprovado com ressalvas ou reprovado.

## Regra final

Respiro editorial nao e pagina em branco.
Pagina em branco sem intencao e erro fantasiado de minimalismo.
