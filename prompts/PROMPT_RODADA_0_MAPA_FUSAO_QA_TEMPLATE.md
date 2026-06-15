# Prompt Profissional — Rodada 0: Mapa de Fusão Visual, Grade QA e Template 6x9

Use este prompt para executar a próxima etapa editorial do projeto **Reposicione-se™**, antes de editar texto fino ou gerar novo PDF completo.

---

Você atuará como **diretor editorial premium, arquiteto de diagramação 6x9, curador visual e auditor de qualidade editorial** da obra **Reposicione-se™**, de **Sol Lima**.

Sua tarefa agora NÃO é reescrever capítulos.
Sua tarefa agora NÃO é gerar o livro inteiro em PDF.
Sua tarefa agora NÃO é empurrar imagem dentro do arquivo sem critério.

Sua missão é executar a **Rodada 0 — Preparação do Mapa de Fusão**, criando três arquivos-base obrigatórios:

1. `mapa-visual/MAPA_DE_FUSAO_VISUAL.md`
2. `relatorios/GRADE_QA_EDITORIAL.md`
3. `templates/TEMPLATE_6X9_REPOSICIONESE.md`

## Objetivo da Rodada 0

Criar o controle editorial que vai permitir fundir:

- o texto limpo da v02;
- as imagens didáticas geradas;
- o PDF visual anterior como referência;
- o futuro template 6x9;
- e o QA visual.

Antes de gerar qualquer nova prévia, você deve saber exatamente:

- qual imagem entra;
- onde entra;
- por que entra;
- em qual tamanho entra;
- se ocupa página inteira;
- que texto vem antes;
- que texto vem depois;
- se é abertura, infográfico, checkpoint, página de respiro ou página simbólica.

Sem isso, não gere PDF.

## Fontes oficiais

Use como fontes-base:

### Texto limpo

`manuscrito/reposicionese_v02_limpeza_estrutura.md`

Função:

- estrutura textual;
- partes;
- capítulos;
- sumário limpo;
- blocos realocados;
- base para edição fina.

### Plano operacional

`PLANO_OPERACIONAL_V03_EDICAO_POR_PARTES.md`

Função:

- define as rodadas;
- define ordem por partes;
- define como cada bloco será editado.

### Tabela visual

`mapa-visual/TABELA_DE_IMAGENS_DIDATICAS_REPOSICIONESE.md`

Função:

- lista de imagens didáticas;
- prioridades;
- função visual;
- destino editorial;
- status.

### Relatório de QA visual

`relatorios/RELATORIO_004_QA_visual_fusao_reposicionese.md`

Função:

- registra falhas da prévia anterior;
- define o que deve ser bloqueado;
- impede repetição do erro.

### Skills obrigatórias

Leia e aplique as skills:

- `.claude/skills/editor-reposicionese/SKILL.md`
- `.claude/skills/infografico-reposicionese/SKILL.md`
- `.claude/skills/qa-visual-editorial-reposicionese/SKILL.md`
- `.claude/skills/fusionador-editorial-reposicionese/SKILL.md`
- `.claude/skills/diagramador-6x9-reposicionese/SKILL.md`

## Arquivo 1 — MAPA_DE_FUSAO_VISUAL.md

Crie um mapa visual que amarre cada imagem a uma posição editorial.

O arquivo deve conter uma tabela com estas colunas:

| ID | Imagem | Arquivo/Status | Função | Onde entra no manuscrito | Rodada | Tipo de inserção | Página inteira? | Texto antes | Texto depois | Observações |

### Tipos de inserção permitidos

- Capa
- Abertura de parte
- Infográfico central
- Página âncora
- Página de respiro didático
- Checkpoint
- Página simbólica
- Guia rápido
- Apêndice / bônus

### Regra

Nenhuma imagem pode ficar solta.
Toda imagem precisa ter:

- ID;
- função;
- posição;
- tipo de inserção;
- justificativa curta;
- decisão sobre página inteira ou não.

## Arquivo 2 — GRADE_QA_EDITORIAL.md

Crie uma grade de controle para avaliar cada rodada antes de gerar PDF.

O arquivo deve conter uma tabela com estas colunas:

| Critério | O que verificar | Gravidade | Como reprova | Como aprova | Rodadas aplicáveis |

Inclua, no mínimo, estes critérios:

1. página em branco sem função;
2. imagem prometida ausente;
3. texto pequeno dentro da imagem;
4. título grudado no texto;
5. capítulo sem respiro;
6. sumário contaminado;
7. infográfico ilegível no celular;
8. imagem sem função editorial;
9. excesso de texto por página;
10. bloco visual duplicado;
11. aumento de páginas sem justificativa;
12. quebra ruim de capítulo;
13. box ou checkpoint sem padrão;
14. página de abertura parecendo erro;
15. conteúdo de teste interrompendo leitura.

Ao final, crie uma seção:

`## Decisão de QA`

Com três possíveis status:

- **Aprovado** — pode ir para preview;
- **Aprovado com ressalvas** — precisa ajuste pequeno;
- **Reprovado** — não entregar para autora.

## Arquivo 3 — TEMPLATE_6X9_REPOSICIONESE.md

Crie o template editorial base para os próximos previews.

O arquivo deve conter:

### 1. Formato

- formato 6 x 9 polegadas;
- orientação vertical;
- uso para livro digital e boneco editorial impresso;
- páginas de imagem inteira em proporção vertical.

### 2. Tipografia recomendada

Defina:

- fonte do corpo;
- tamanho do corpo;
- entrelinha;
- fonte/tamanho de H1;
- fonte/tamanho de H2;
- fonte/tamanho de H3;
- estilo de citação;
- estilo de box;
- estilo de checkpoint;
- estilo de comando.

### 3. Margens

Defina margens confortáveis para leitura:

- superior;
- inferior;
- interna;
- externa.

Inclua observação de que o arquivo final para impressão pode exigir sangria e ajuste técnico posterior.

### 4. Hierarquia visual

Crie regras para:

- capa interna;
- sumário;
- abertura de parte;
- abertura de capítulo;
- subtítulos;
- interlúdios;
- boxes;
- checkpoints;
- comandos;
- imagens de página inteira;
- apêndices.

### 5. Páginas de imagem inteira

Defina que as imagens didáticas principais devem ocupar página inteira, com:

- margem visual segura;
- nenhuma imagem espremida em meia página quando houver texto interno;
- conferência de legibilidade no celular;
- não inserir imagem se o texto da arte ficar pequeno.

### 6. Regras de respiro

Diferencie:

- página de respiro real;
- página de abertura;
- página vazia por erro.

Regra final:

Página vazia sem intenção é erro, não elegância.

## Proibição importante

Não gere PDF completo nesta etapa.
Não gere DOCX completo nesta etapa.
Não edite capítulos ainda.
Não apague texto.
Não faça corte literário.

Esta rodada é de **preparação, mapa, controle e template**.

## Entrega esperada

Ao final, entregue:

1. confirmação dos três arquivos criados;
2. resumo do mapa de fusão;
3. lista das imagens que entram na Rodada 1;
4. lista das imagens que entram na Rodada 2;
5. riscos ainda pendentes antes de gerar preview curto.

## Próxima etapa depois da Rodada 0

Após estes arquivos estarem prontos, iniciar:

`Rodada 1 — Pré-livro e navegação`

Com entrega curta contendo:

- capa interna;
- guia de leitura;
- mapa da travessia;
- mapa mental;
- legenda do método;
- checkpoint;
- sumário limpo;
- nota de lente autoral;
- nota de proteção;
- este livro e o anterior.

E somente depois gerar um **preview curto**, aprovado no QA visual.

## Tom editorial

Firme, organizado, premium e prático.

Sem bajulação.
Sem gambiarra.
Sem gerar PDF só para parecer que avançou.

A Rodada 0 é a trena, o prumo e a planta da casa.
Livro premium não nasce no improviso.
Nasce quando cada página sabe por que existe.
