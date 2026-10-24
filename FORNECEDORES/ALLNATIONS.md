# ALLNATIONS — Ficha de fornecedor

| Campo | Valor |
|---|---|
| **ID** | LIC-FORN-ALLNATIONS-001 |
| **Projeto** | LICITAÇÃO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | FICHA DE FORNECEDOR |
| **Fase** | Cadastro inicial / validação |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | ccc8cfaa385df73e046daeda71de6e5b654facb015ddb17efa7fe7fd1913b972 |
| **Commit de referência (versão anterior)** | N/A — nova ficha |
| **Data de criação** | 2026-10-22 |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Responsável pelo projeto LICITAÇÃO |
| **Aprovador** | Pendente — sem evidência de aprovação |
| **Origem** | Cadastro criado para registo do fornecedor; fontes públicas indicadas abaixo |
| **Autoridade superior** | [Constituição do projeto](https://github.com/carlos-andrade/LICITACAO/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Identificação

- **Nome informado:** ALLNATIONS / All Nations.
- **Razão social encontrada em fonte pública:** ALL NATIONS COMERCIO EXTERIOR S.A.
- **Nome fantasia divulgado:** ALL NATIONS / Grupo All Nations.
- **Área de atuação divulgada:** distribuição e comércio atacadista de tecnologia, equipamentos e suprimentos de informática.
- **CNPJ:** há múltiplas inscrições de filiais associadas à razão social. Confirmar qual CNPJ deve ser utilizado para cotação, faturamento e cadastro antes de selecionar uma unidade.
- **Estado cadastral:** não consolidado para uma unidade específica nesta ficha.

## 2. Contato institucional publicado

- **Site institucional:** [Grupo All Nations](https://grupoallnations.com.br/)
- **Telefone divulgado:** (21) 3523-8000.
- **E-mail geral divulgado:** contato@grupoallnations.com.br.

Confirmar os canais no site institucional antes de enviar solicitação de cotação. Não foram registados preços, condições comerciais ou propostas nesta ficha.

## 3. Fontes consultadas

1. [Site institucional — Grupo All Nations](https://grupoallnations.com.br/) — apresentação da empresa, linhas de serviço e contacto institucional.
2. [Portal da Transparência — Pessoa Jurídica, CNPJ 00.070.112/0005-42](https://portaldatransparencia.gov.br/pessoa-juridica/00070112000542) — fonte pública para uma filial; não usar como identificação definitiva de todas as filiais.
3. [Consulta pública — ALL NATIONS COMERCIO EXTERIOR S.A., CNPJ 00.070.112/0017-86](https://casadosdados.com.br/solucao/cnpj/all-nations-comercio-exterior-sa-00070112001786) — fonte secundária para dados cadastrais de uma filial; confirmar os dados na Receita Federal.

**Data de consulta das fontes:** 2026-10-22.

## 4. Captura de catálogo e produtos publicamente acessíveis

**Fonte-alvo:** [https://allnations.com.br/](https://allnations.com.br/)  
**Situação da captura ao publicar esta ficha:** **PENDENTE DE EXECUÇÃO NO AMBIENTE DO REPOSITÓRIO**. O domínio não pôde ser lido diretamente pela ferramenta de pesquisa desta sessão. Portanto, não há produtos ou preços confirmados nesta tabela inicial. A tabela será preenchida pelo script apenas com dados que o site torne publicamente capturáveis; nenhum produto será inventado.

O coletor está em [`scripts/capture_allnations_catalog.py`](https://github.com/carlos-andrade/LICITACAO/blob/main/scripts/capture_allnations_catalog.py), com instruções em [`scripts/README-allnations-captura.md`](https://github.com/carlos-andrade/LICITACAO/blob/main/scripts/README-allnations-captura.md).

### Tabela de produtos capturados

| Nº | Produto | Marca | Modelo | SKU | GTIN/EAN | Categoria | Preço | Moeda | Disponibilidade | URL de origem | Estado |
|---:|---|---|---|---|---|---|---:|---|---|---|---|
| — | **Nenhum produto confirmado ainda** | — | — | — | — | — | — | — | — | [Site All Nations](https://allnations.com.br/) | PENDENTE — executar coletor e validar cobertura |

### Campos e rastreabilidade

O CSV gerado contém nome, marca, modelo, SKU, GTIN, categoria, preço e moeda quando publicados, disponibilidade, URL de origem, data de captura, origem do dado e observações. O JSON associado regista totais de páginas, restrições e erros encontrados.

**Importante:** o catálogo pode ser B2B e exigir autenticação. O coletor não contorna login, CAPTCHA, bloqueios ou regras do `robots.txt`. A ausência de produto no resultado não prova que o fornecedor não o comercialize. Antes de usar um produto em uma licitação, confirmar diretamente com o fornecedor preço, impostos, frete, prazo, garantia, validade e disponibilidade.

### Execução na raiz do repositório

```bash
python -m pip install requests beautifulsoup4
python scripts/capture_allnations_catalog.py --max-pages 300 --delay 1.0
```

Os ficheiros serão gravados por padrão em `FORNECEDORES/allnations-produtos.csv` e `FORNECEDORES/allnations-produtos.json`. Após a execução, importar os resultados para esta tabela depois de verificar duplicatas, cobertura de URLs e campos obrigatórios. Não colar a tabela bruta sem validar resultados.

## 5. Pendências de validação

- Executar o coletor numa máquina com acesso ao site e confirmar as regras de `robots.txt`.
- Conferir número de páginas visitadas, produtos capturados, erros e categorias não alcançadas.
- Confirmar a filial/CNPJ exato que emitirá proposta e nota fiscal.
- Validar situação cadastral diretamente na Receita Federal.
- Confirmar preços, marcas, disponibilidade, frete, impostos, prazos e condições de pagamento diretamente com o fornecedor.
- Vincular a ficha aos editais/processos relevantes quando houver relação documentada.

## 6. Histórico

- 2026-10-22 — criada ficha inicial; dados de preços e condições comerciais permanecem não informados.
- 2026-10-22 — adicionado coletor de catálogo público, documentação de execução e tabela inicial sem produtos não verificados.
