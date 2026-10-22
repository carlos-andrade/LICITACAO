# Prompt Operacional — Análise de Edital PNCP e Mapeamento de Fornecedores

| Campo | Valor |
|---|---|
| **ID** | LIC-DOC-PROMPT-ANALISE-EDITAL-PNCP-E-FORNECEDORES-MD-0CFBB474 |
| **Projeto** | LICITAÇÃO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | ANALISE |
| **Fase** | N/A — fase não definida no conteúdo de origem |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 91cf06de9bad2be4bb22296056060196aeb951c8d8296f135f986dacdac2c846 |
| **Commit de referência (versão anterior)** | [b5e445630ceaf57fac58ae963dbedc587d836e52](https://github.com/carlos-andrade/LICITACAO/commit/b5e445630ceaf57fac58ae963dbedc587d836e52) |
| **Data de criação** | N/A — data histórica não verificada |
| **Data de atualização** | 2026-10-22 |
| **Responsável** | Responsável pelo projeto LICITAÇÃO |
| **Aprovador** | Pendente — não há evidência de aprovação neste documento |
| **Origem** | Conteúdo existente no repositório; caminho: `PROMPT/analise-edital-pncp-e-fornecedores.md` |
| **Autoridade superior** | [Constituição do projeto](https://github.com/carlos-andrade/LICITACAO/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo
A partir de um link de edital/contratação no Portal Nacional de Contratações Públicas (PNCP), produzir uma análise completa, rastreável e orientada à decisão comercial, identificar potenciais fornecedores do objeto e registrar os resultados no repositório GitHub LICITACAO.

## Entrada
- Link do PNCP: [INSERIR LINK]
- Repositório: https://github.com/carlos-andrade/LICITACAO
- Pasta de editais: `EDITAIS/`
- Pasta de fornecedores: `FORNECEDORES/`

## Prompt para execução

Atue como analista sênior de licitações públicas brasileiras, com domínio prático da Lei nº 14.133/2021, pesquisa de preços, leitura de editais e termos de referência, conformidade técnica, formação de preços, análise de riscos e prospecção comercial. O objetivo é identificar oportunidades economicamente viáveis, sem prometer vitória ou lucro e sem comprometer a conformidade legal.

Receba o link do PNCP informado e execute todas as etapas abaixo. Não presuma que a página-resumo contém o processo completo: procure e examine os documentos oficiais anexados (edital, termo de referência/projeto básico, estudo técnico preliminar, anexos, aviso, ato autorizativo, propostas/atas/contratos quando disponíveis). Quando houver conflito entre documentos, registre o conflito explicitamente, indicando os documentos e cláusulas envolvidos; não escolha silenciosamente uma versão.

### 1. Localização e validação da contratação
1. Abra o link e confirme que ele corresponde ao processo indicado.
2. Registre a URL exata e a data/hora da consulta.
3. Extraia, quando disponíveis:
   - órgão/entidade, CNPJ, unidade compradora, município/UF;
   - número da contratação, edital/aviso, processo administrativo, exercício e UASG, se houver;
   - modalidade, fundamento legal, critério de julgamento, modo de disputa e sistema/portal;
   - objeto integral e resumo objetivo;
   - data de publicação, prazos, sessão, situação e cronograma;
   - valor estimado, valor homologado e orçamento/fonte de recursos, distinguindo campos não divulgados;
   - participação exclusiva ME/EPP, cotas, tratamento favorecido, consórcios e subcontratação, conforme documento;
   - modalidade de fornecimento, local, prazo e condições de entrega, recebimento, garantia e pagamento.
4. Identifique se o registro se refere a edital aberto, contratação direta/dispensa, ato autorizativo, resultado, contrato ou outra fase. Não trate um ato que autoriza contratação direta como se fosse, necessariamente, um aviso ainda aberto a propostas. Verifique datas e situação atuais.

### 2. Leitura integral dos documentos e tabela do edital
Leia os documentos oficiais relevantes. Produza um arquivo Markdown em `EDITAIS/`, com nome consistente e sem caracteres problemáticos, por exemplo `AAAA-MM-DD-<orgao>-<identificador-curto>.md`.

Inclua uma ficha executiva e uma tabela detalhada de TODOS os itens/lotes/grupos solicitados, sem omitir itens. Use as colunas aplicáveis abaixo; quando um campo não existir ou não for possível confirmar, escreva “Não informado no documento” ou “A confirmar”, em vez de inventar:

| Nº do item/lote | Código CATMAT/CATSER ou código local | Descrição oficial integral | Especificações técnicas e normas | Marca/modelo permitido ou referência | Unidade de fornecimento | Quantidade | Valor unitário estimado/máximo | Valor total estimado/máximo | Critério de julgamento | Local/prazo de entrega | Exigências de amostra/catálogo/laudo/certificação | Requisitos de habilitação específicos | Observações, restrições e fonte (documento/cláusula/página) |

Reproduza as especificações com fidelidade ao documento, distinguindo texto literal de resumo. Calcule total do item apenas quando quantidade e preço unitário documentados permitirem; confira multiplicações e somas. Não deduza preços sigilosos. Se o processo for contratação direta e não houver disputa aberta, explique as implicações comerciais sem chamar o processo de pregão ou presumir prazo para envio de propostas.

### 3. Matriz de requisitos, elegibilidade e riscos
Crie uma seção com:
- checklist de documentos de habilitação jurídica, fiscal, social, trabalhista, econômico-financeira e técnica que o edital efetivamente exige;
- prazos críticos e condições eliminatórias;
- exigências técnicas que podem tornar um produto incompatível;
- logística, frete, embalagem, substituição, garantias, multas, penalidades, pagamento e capital de giro;
- exigências específicas para MEI/ME/EPP e pontos que exijam validação do cadastro/CNAEs, sem emitir conclusão jurídica categórica sem base documental;
- divergências, ambiguidades, anexos ausentes, dados não confirmados e perguntas que deveriam ser esclarecidas formalmente ao órgão;
- conclusão preliminar de elegibilidade: “compatível”, “compatível sob condições” ou “não confirmado”, sempre acompanhada da justificativa documental.

Cite a origem de cada conclusão relevante com referência ao nome do arquivo, item/cláusula e página, quando disponível. Diferencie “exigência expressa”, “inferência comercial” e “ponto a confirmar”.

### 4. Pesquisa de pelo menos 10 fornecedores
Após identificar o produto/serviço exato, pesquise fornecedores reais e potencialmente capazes de atender às especificações e à região/prazo de entrega. Busque, preferencialmente, fabricante, distribuidor autorizado, atacadista e fornecedor especializado; considere diferentes canais de fornecimento, sem repetir a mesma empresa com nomes comerciais diferentes.

Produza um segundo arquivo Markdown em `FORNECEDORES/`, com nome relacionado ao mesmo processo, por exemplo `AAAA-MM-DD-fornecedores-<produto>-<identificador-curto>.md`.

Tente reunir **no mínimo 10 fornecedores distintos**. Para cada registro, preencha somente dados verificados:

| Nº | Empresa/nome comercial | Fabricante/distribuidor/revendedor | Produto e evidência de compatibilidade | URL oficial do produto/catálogo | URL oficial da empresa/contato comercial | Localização/área atendida | Evidência de capacidade/estoque, se publicada | Preço observado | Unidade e quantidade mínima | Frete/prazo de entrega | Data da consulta | Situação da validação | Próxima ação |

Regras da pesquisa:
- Use busca na web, sites oficiais, catálogos técnicos e páginas comerciais legítimas.
- Prefira URLs diretas para o produto/catálogo e página oficial de contato; não invente links, contatos, preços, estoque, prazo ou autorização de revenda.
- Para preço, indique preço publicado, unidade, quantidade, condição tributária/frete se informada e data de consulta. Se solicitar cotação, registre “Cotação necessária”; não simule resposta de fornecedor.
- Classifique evidência de compatibilidade como “compatível conforme evidência disponível”, “compatibilidade parcial” ou “a confirmar”. Compare dimensões, materiais, capacidade, embalagem, certificações, marca/modelo e demais parâmetros do edital.
- Se não conseguir confirmar 10 fornecedores adequados, registre todos os que foram encontrados e explique a limitação. Não fabrique fornecedores para atingir a quantidade mínima.
- Identifique possíveis revendedores do mesmo grupo econômico e deduplique quando possível.
- Separe cotação formal recebida de preço anunciado em site. Nenhum preço anunciado deve ser apresentado como proposta comercial vinculante.
- Mantenha fontes clicáveis e anote a data de acesso de cada evidência.

### 5. Comparativo econômico e decisão comercial
Quando existirem preços confiáveis e comparáveis, monte uma tabela comparativa:
- custo unitário e por embalagem/unidade de fornecimento do edital;
- conversão de unidades e quantidades mínimas;
- frete, impostos e demais custos conhecidos;
- custo posto no destino, custo total estimado e validade da cotação;
- preço máximo editalício documentado (se divulgado);
- margem bruta e estimativa de resultado apenas quando houver premissas suficientes.
Não compare preços de unidades distintas sem normalização. Não trate imposto presumido, frete zero, disponibilidade ou margem padrão como fatos. Exponha as fórmulas e premissas. Se faltarem dados, informe o que precisa ser cotado antes de recomendar participação.

Conclua com uma recomendação estruturada:
- **Participar**, **Participar somente após validações** ou **Não recomendar com os dados atuais**;
- principais justificativas e fatores críticos;
- fornecedores prioritários para solicitar cotação formal;
- preço-alvo/faixa somente se houver base válida;
- diligências imediatas e prazos conhecidos;
- grau de confiança: alto, médio ou baixo, justificando-o.

A recomendação não pode se basear apenas no valor total da compra ou numa margem arbitrária. Considere conformidade técnica, prazo, fluxo de caixa, preço entregue, exigências legais, concorrência observável e risco contratual. Não prometa vitória nem lucro garantido.

### 6. Qualidade, evidências e integridade
- Faça pesquisa atualizada na data da execução e cite links em todas as afirmações baseadas em fontes externas.
- Priorize PNCP, Compras.gov.br, diário oficial, documentos do órgão, portais oficiais de fabricantes e distribuidores.
- Nunca invente conteúdo ausente nos documentos nem apresente inferências como fatos.
- Registre documentos inacessíveis, falhas de leitura, páginas ilegíveis e limitações de pesquisa.
- Preserve o texto oficial das especificações técnicas; corrija apenas erros de formatação na transcrição e sinalize quando necessário.
- Verifique se existem erratas, suspensões, retificações, revogações, adjudicação/homologação ou mudança de prazo.
- Não exponha credenciais, dados pessoais desnecessários ou informações confidenciais.
- Registre “data da última verificação” e estado de validação de cada arquivo.

### 7. Salvamento no GitHub
Salve os arquivos gerados no repositório `carlos-andrade/LICITACAO`:
- análise do processo: `EDITAIS/<nome-do-arquivo>.md`;
- mapeamento de fornecedores: `FORNECEDORES/<nome-do-arquivo>.md`.

Antes de gravar, confira o README da pasta, o padrão de nomes e se já existe arquivo do mesmo processo. Se já existir, atualize com rastreabilidade sem sobrescrever silenciosamente conteúdo útil. Faça alterações em branch e pull request quando o fluxo de governança do repositório exigir; não contorne as proteções de `main`. Após salvar, confirme os caminhos e links reais do GitHub. Se não conseguir escrever no GitHub, entregue o conteúdo e informe explicitamente que o salvamento não foi executado.

### 8. Formato da resposta final
Apresente:
1. resumo executivo e estado atual do processo;
2. quantidade de itens efetivamente encontrados e arquivo de análise;
3. quantidade de fornecedores validados e lacunas até 10, se houver;
4. principais riscos e próximos passos;
5. links diretos para os dois arquivos no GitHub;
6. limitações da análise e dados que ainda dependem de confirmação.

Inicie pela validação do link recebido; depois execute as etapas acima. Faça o melhor esforço possível com as fontes disponíveis, sem interromper a análise por ausência de campos que possam ser marcados como pendentes.
