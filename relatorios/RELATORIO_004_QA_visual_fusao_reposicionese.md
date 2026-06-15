# RELATÓRIO 004 — QA Visual, Infográficos e Plano de Fusão

Projeto: **Reposicione-se™**  
Autora: **Sol Lima**  
Data: 2026-06-15

## Veredito direto

A prévia `REPOSICIONESE_v02_PREVIEW_LIVRO_6x9_COM_INFOGRAFICOS.pdf` não pode ser considerada uma versão visual confiável.

Ela serviu para revelar o problema: a conversão automática inseriu páginas vazias ou quase vazias, não posicionou os infográficos como parte real da narrativa editorial e não respeitou a experiência de leitura esperada para um livro premium.

A versão correta não deve ser gerada por “juntar Markdown + imagens do PDF” de forma automática. O caminho certo é fazer uma fusão editorial controlada.

## Achados objetivos

| Item auditado | Evidência encontrada | Gravidade | Decisão editorial | Próxima ação |
|---|---:|---|---|---|
| Páginas do PDF original | 584 páginas | Informação-base | Manter como referência visual | Usar como fonte de artes e mapa visual |
| Páginas da prévia gerada | 639 páginas | Alta | A prévia aumentou 55 páginas | Não usar como versão final |
| Páginas vazias/quase vazias na prévia | cerca de 35 a 38 páginas detectadas | Alta | Resultado visual inaceitável | Remover quebras automáticas cegas |
| Infográficos | Não aparecem para a autora como gráficos integrados | Alta | Inserção falhou como experiência editorial | Extrair artes do PDF original e reinserir por manifesto visual |
| Letras | Pequenas em alguns trechos e inconsistentes | Média/Alta | Fonte precisa seguir padrão editorial fixo | Definir template tipográfico antes de nova exportação |
| Respiro entre títulos | Insuficiente/inconsistente | Alta | Hierarquia visual ainda não está resolvida | Criar estilos reais: parte, capítulo, subtítulo, box, comando |
| Páginas de abertura | Algumas viraram páginas brancas ou quase vazias | Alta | Respiro não pode parecer erro | Criar páginas de abertura desenhadas, não páginas vazias |
| Sumário | Já foi limpo na v02 textual, mas precisa de sumário visual | Média | Manter limpo e redesenhar | Gerar sumário editorial com hierarquia e página própria |
| Fusão entre versões | Ainda não foi feita corretamente | Alta | Precisa de método de fusão, não gambiarra | Fundir texto v02 + visual original + template premium |
| PDF como base textual | Ruim para edição | Alta | Não usar como base única | Usar Markdown/DOCX para texto e PDF original para artes |

## O que está faltando

1. Manifesto visual: lista oficial de onde cada infográfico entra.
2. Extração limpa das páginas visuais do PDF original.
3. Template editorial 6x9 real, com estilos de livro.
4. Grade de controle de páginas: texto, abertura, infográfico, checkpoint, respiro, teste.
5. Validação visual página a página antes de entregar novo PDF.
6. Skill de QA visual para bloquear entrega ruim.
7. Skill de fusão editorial para unir texto e visual sem quebrar o livro.
8. Skill de diagramação 6x9 para criar estilos consistentes.

## O que está sobrando

1. Páginas brancas automáticas sem função editorial.
2. Quebras de página cegas.
3. Tentativa de inserir imagem sem ancoragem por capítulo.
4. Prévia visual gerada antes do manifesto visual.
5. Mistura entre “respiro” e “vazio”. Respiro editorial tem intenção; página vazia é só silêncio constrangedor.

## O que está passando do ponto

1. O arquivo visual ficou maior que a fonte original.
2. A prévia tentou parecer livro antes de ter controle de layout.
3. A automação quis diagramar sem saber a função de cada página visual.
4. Algumas páginas têm pouca informação e parecem erro, não pausa estética.

## Método correto de fusão

A nova versão deve fundir três camadas:

### Camada 1 — Texto limpo

Fonte: `reposicionese_v02_limpeza_estrutura.md`

Função: base textual, hierarquia, sumário, capítulos e marcações editoriais.

### Camada 2 — Visual original

Fonte: `REPOSICIONESE_melhor versão até agora(1).pdf`

Função: recuperar capa, mapas, infográficos, páginas visuais e artes aprovadas.

### Camada 3 — Template premium

Novo arquivo a ser criado.

Função: definir formato 6x9, fonte, margens, hierarquia, boxes, checkpoints, aberturas de parte e páginas de respiro.

## Fluxo recomendado antes de gerar outro PDF

1. Criar `MAPA_DE_FUSAO_VISUAL.md`.
2. Criar `GRADE_QA_EDITORIAL.xlsx` ou tabela equivalente.
3. Definir estilos de livro:
   - corpo;
   - citação;
   - título de parte;
   - título de capítulo;
   - subtítulo;
   - box;
   - checkpoint;
   - comando;
   - página visual.
4. Extrair as páginas visuais do PDF original como imagens de alta qualidade.
5. Associar cada imagem a um ponto do manuscrito.
6. Gerar DOCX/PDF apenas depois da associação.
7. Renderizar páginas-chave e conferir automaticamente:
   - página em branco;
   - fonte pequena;
   - imagem ausente;
   - título grudado;
   - excesso de texto por página.
8. Só entregar se passar no QA visual.

## Skills adicionais necessárias

Sim. Além das skills já criadas, o projeto precisa de mais três:

1. `qa-visual-editorial-reposicionese` — bloqueia PDF com páginas vazias, fonte pequena, infográfico ausente e hierarquia ruim.
2. `fusionador-editorial-reposicionese` — funde texto limpo, visual original e template premium.
3. `diagramador-6x9-reposicionese` — define estilos, margens, respiros, tipografia e páginas de abertura.

## Decisão final

Não gerar outro PDF “bonitinho” agora.

A próxima entrega correta é:

1. um **mapa de fusão visual**;
2. uma **grade de QA**;
3. um **template editorial 6x9 aprovado**;
4. só depois uma nova prévia PDF.

Sem isso, a automação vai continuar fazendo o que automação faz quando está sem comando editorial: fingir que página em branco é minimalismo.
