# GRADE QA EDITORIAL — REPOSICIONE-SE™

Projeto: **Reposicione-se™**  
Rodada: **0 — Controle de Qualidade Visual e Editorial**

## Objetivo

Esta grade existe para impedir que qualquer preview seja entregue com páginas vazias, fonte pequena, imagens sumidas, infográficos ilegíveis ou hierarquia visual quebrada.

A regra é simples: se não passa no QA, não vai para a autora como preview.

## Tabela de controle

| Critério | O que verificar | Gravidade | Como reprova | Como aprova | Rodadas aplicáveis |
|---|---|---|---|---|---|
| Página em branco sem função | Ver se há página vazia ou quase vazia | Alta | Página branca sem título, sem arte, sem intenção | Página tem abertura, arte, respiro textual ou função clara | Todas |
| Imagem prometida ausente | Conferir se cada imagem do mapa apareceu no preview | Alta | Mapa diz que entra, mas a imagem não aparece | Imagem está no local previsto e com tamanho correto | Todas |
| Texto pequeno dentro da imagem | Ver legibilidade em celular | Alta | Texto da imagem ilegível ou exige zoom exagerado | Texto legível em tela de celular | Todas |
| Título grudado no texto | Conferir espaço antes/depois de títulos | Média/Alta | Título aparece colado no parágrafo anterior ou seguinte | Título tem respiro visual confortável | Todas |
| Capítulo sem respiro | Conferir se abertura de capítulo respira | Média | Capítulo começa esmagado em página cheia | Capítulo começa com hierarquia clara | Todas |
| Sumário contaminado | Ver se o sumário tem apenas títulos | Alta | Parágrafo explicativo aparece dentro do sumário | Sumário contém apenas partes, capítulos, interlúdios e apêndices | Rodada 1 |
| Infográfico ilegível no celular | Testar leitura reduzida | Alta | Caixas, ícones ou texto ficam pequenos demais | Infográfico funciona em página inteira e mobile | Todas com imagens |
| Imagem sem função editorial | Conferir se a imagem tem motivo | Média | Imagem decorativa sem conexão com trecho | Imagem fixa método, guia leitura ou cria pausa necessária | Todas |
| Excesso de texto por página | Ver densidade visual | Média | Página parece bloco de apostila sem pausa | Texto tem parágrafos, boxes ou imagem de apoio | Todas |
| Bloco visual duplicado | Conferir repetição de imagem | Média | A mesma imagem aparece sem função repetida | Repetição só ocorre como eco planejado | Todas |
| Aumento de páginas sem justificativa | Comparar previsão e saída | Alta | Preview aumenta por páginas vazias/erros | Aumento é justificado por imagens e aberturas | Todas |
| Quebra ruim de capítulo | Ver fim/início de capítulo | Média | Capítulo quebra deixando título órfão ou página torta | Quebra favorece leitura e hierarquia | Todas |
| Box ou checkpoint sem padrão | Conferir elementos especiais | Média | Cada box aparece de um jeito diferente | Boxes e checkpoints seguem modelo fixo | Todas |
| Página de abertura parecendo erro | Ver se abertura é intencional | Alta | Página com pouca coisa e sem design parece falha | Página tem título, símbolo, arte ou frase de abertura | Todas |
| Conteúdo de teste interrompendo leitura | Ver fluxo dos testes | Alta | Teste longo quebra narrativa principal | Teste resumido no livro e completo em caderno/apêndice | Rodadas 3 e 8 |
| Imagem com erro de ortografia | Conferir texto dentro da arte | Alta | Acento errado, palavra inventada ou frase truncada | Arte revisada e aprovada antes de entrar no PDF | Todas com imagens |
| Imagem cortada pela margem | Conferir sangria visual | Alta | Título, ícone ou borda fica cortado | Imagem respeita margem segura | Todas com imagens |
| Página de imagem espremida | Conferir proporção | Média/Alta | Infográfico com texto entra em meia página | Infográfico textual ocupa página inteira | Todas com imagens |
| Rodapé/cabeçalho invasivo | Conferir se elementos automáticos competem | Baixa/Média | Número de página sobre imagem ou borda | Rodapé discreto e fora da arte principal | Todas |
| Alternância visual cansativa | Conferir sequência de páginas pretas/creme | Média | Muitas páginas escuras seguidas pesam | Alternância planejada entre texto claro e visual escuro | Todas |

## Decisão de QA

### Aprovado

Pode ir para preview da autora.

Condições:

- nenhuma falha alta aberta;
- imagens principais presentes;
- leitura confortável;
- sumário limpo;
- sem páginas vazias sem função.

### Aprovado com ressalvas

Pode ir para revisão interna, mas não para versão final.

Condições:

- falhas pequenas de espaçamento;
- um ou dois ajustes visuais simples;
- nenhuma imagem essencial ausente.

### Reprovado

Não entregar para a autora como preview aprovado.

Condições:

- página vazia sem função;
- imagem prometida ausente;
- infográfico ilegível;
- sumário contaminado;
- fonte pequena;
- aumento de páginas sem justificativa;
- elementos visuais parecendo erro.

## Procedimento de QA por rodada

1. Conferir mapa de fusão da rodada.
2. Conferir se todas as imagens previstas aparecem.
3. Renderizar páginas-chave.
4. Verificar legibilidade no celular.
5. Marcar falhas por gravidade.
6. Corrigir antes de gerar novo arquivo.
7. Só entregar se o status for Aprovado ou Aprovado com ressalvas.

## Regra final

Respiro editorial tem intenção.

Página vazia sem intenção é só erro com autoestima alta.
