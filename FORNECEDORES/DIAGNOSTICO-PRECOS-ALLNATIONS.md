# Diagnóstico — preços ausentes na captura ALLNATIONS

| Campo | Valor |
|---|---|
| **ID** | LIC-DIAG-ALLNATIONS-PRECO-001 |
| **Projeto** | LICITAÇÃO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | DIAGNÓSTICO TÉCNICO |
| **Fase** | Investigação da captura |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | fc6d6eaf9064d1444def3620cfe2a95e8c04292ffb373d0bd4057a9c5d130f60 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-22 |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Responsável pelo projeto LICITAÇÃO |
| **Aprovador** | Pendente — sem evidência de aprovação |
| **Origem** | Inspeção do coletor versionado, JSON/CSV recebidos e página pública de produto ALLNATIONS |
| **Autoridade superior** | [Constituição do projeto](https://github.com/carlos-andrade/LICITACAO/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Resumo executivo

A evidência aponta para duas causas distintas:

1. **Causa provável principal — preço não exposto na página pública anónima.** A página pública de produto inspecionada apresenta nome, fabricante, SKU, disponibilidade e botão “Comprar”, mas não apresenta um preço no texto acessível. O cabeçalho do site apresenta “Entrar”, “CADASTRE-SE” e “REVENDEDOR, ENTRE OU CADASTRE-SE”. Isto é compatível com preço dependente de sessão/cadastro de revendedor, embora a inspeção anónima, por si só, não prove todos os requisitos comerciais do fornecedor.
2. **Limitação do coletor — extração de preço estreita.** O script só procura preço em `offers.price`, `offers.lowPrice` ou `offers.highPrice` do JSON-LD, e em `meta[property="product:price:amount"]`, `meta[itemprop="price"]` ou `[itemprop="price"]`. Não procura texto de preço nos seletores visuais específicos do tema da loja, nem inspeciona respostas de APIs usadas pelo frontend.

A segunda limitação pode fazer perder preços públicos apresentados apenas no HTML visível. Contudo, não resolve o caso em que o fornecedor não envia o preço a visitantes anónimos.

## 2. Evidências

### 2.1 Página pública de produto

Página consultada: [Drone DJI Neo Fly More Combo — All Nations](https://allnations.com.br/drone-dji-neo-fly-more-combo-sem-tela-br-dji051).

O conteúdo público acessível apresenta:
- título e fabricante;
- SKU `0116301-01`;
- disponibilidade “Em estoque”;
- botão “Comprar”;
- sem preço legível no conteúdo da página consultada.

A página inicial também apresenta os acessos “Entrar”, “CADASTRE-SE” e “REVENDEDOR, ENTRE OU CADASTRE-SE”: [All Nations](https://allnations.com.br/).

Esta evidência sustenta a hipótese de restrição comercial, mas não confirma se o preço é disponibilizado após login, cadastro aprovado, integração comercial ou pedido de cotação.

### 2.2 Dados capturados

No ZIP inspecionado, o JSON informa 103 produtos distintos, 290 páginas HTML lidas e zero preços preenchidos. Os campos `preco` estão vazios nos registos. Os dados são da captura anterior, com limite de 300 páginas; não comprovam uma execução posterior do coletor corrigido.

### 2.3 Limitação de implementação

No ficheiro [`scripts/capture_allnations_catalog.py`](https://github.com/carlos-andrade/LICITACAO/blob/main/scripts/capture_allnations_catalog.py), a função `price_from_product` lê apenas `offers` do JSON-LD. A função `product_row` tenta depois três seletores genéricos de metadados HTML. Não existe uma etapa que:
- procure o preço visível nos seletores próprios da página de produto;
- examine dados JSON embutidos usados pelo frontend;
- registe um diagnóstico por produto que distinga “sem preço no HTML”, “preço protegido” e “falha de extração”.

## 3. Conclusão

**Não há evidência de que o script esteja a omitir um preço público presente na página de produto inspecionada; o preço não aparece no conteúdo público acessível.** A causa mais provável é o modelo de acesso comercial da ALLNATIONS, possivelmente combinado com a cobertura incompleta dos seletores de extração.

Não se deve contornar login, CAPTCHA, controlos de acesso ou regras do site. Para obter preço comercial, a via segura é confirmar com a ALLNATIONS o acesso de revendedor, exportação de catálogo ou API autorizada.

## 4. Plano de resolução

1. Testar o coletor em várias páginas de produto públicas e registar se o HTML recebido contém algum campo de preço.
2. Melhorar a extração de preço visível do HTML e dos dados estruturados, sem inferir ou fabricar valores.
3. Adicionar um diagnóstico por produto: `PRECO_PUBLICO_ENCONTRADO`, `SEM_PRECO_NO_HTML_PUBLICO`, `POSSIVEL_RESTRICAO_COMERCIAL` ou `FALHA_DE_EXTRACAO`.
4. Se continuar sem preços, solicitar à ALLNATIONS acesso de revendedor, tabela comercial, feed de catálogo ou documentação de API autorizada.
5. Só marcar a recolha de preços como concluída quando houver valores observados, URL de origem e data/hora de captura.

## 5. Critério de aceitação

A captura de preços só será considerada resolvida quando o CSV/JSON incluir valores não vazios, moeda, URL da página de origem e timestamp, com os valores rastreáveis à fonte. O preço não deve ser inferido a partir de lojas terceiras nem de produtos semelhantes.
