# Relatório de verificação de integridade — captura ALLNATIONS

| Campo | Valor |
|---|---|
| **ID** | LIC-VER-ALLNATIONS-001 |
| **Projeto** | LICITAÇÃO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | RELATÓRIO DE VERIFICAÇÃO |
| **Fase** | Validação de evidência |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 39475d68b37c6b9ff11ddae24ac79f9199d174428b3a271c4edcba6b7b4316d6 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-22 |
| **Data de atualização** | 2026-10-22 |
| **Responsável** | Responsável pelo projeto LICITAÇÃO |
| **Aprovador** | Pendente — sem evidência de aprovação |
| **Origem** | Arquivo recebido nesta conversa: `allnations-catalog-capture (2).zip`; SHA-256 calculado localmente sobre os bytes do arquivo |
| **Autoridade superior** | [Constituição do projeto](https://github.com/carlos-andrade/LICITACAO/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Resultado

**O hash informado não corresponde ao arquivo ZIP recebido.**

- **SHA-256 informado:** `c44f2e0d2795379f3b1efd70f23750985b9d9e5dc788b6155af8ee5320865eba`
- **SHA-256 calculado do ZIP recebido:** `92a70e501f379e20cde2c7b0eed6904c2265d3cd54bce03e54d3cabcdd5de987`
- **Resultado da comparação:** divergente (`match = false`).

O hash foi calculado sobre o arquivo ZIP completo, não sobre os ficheiros extraídos. Os hashes dos ficheiros internos são registados abaixo para permitir verificação independente.

## 2. Ficheiros dentro do ZIP

| Ficheiro | Tamanho (bytes) | SHA-256 |
|---|---:|---|
| `allnations-produtos.csv` | 43.974 | `df72f3629d7380acf0c18b0e143821488bfe7183468531cc81eade3ec211f251` |
| `allnations-produtos.json` | 78.257 | `e90efde0951973c54498c2ffa52b1cc0eaf7f2eb3ec9ff1e2f0a962bc391c914` |

## 3. Metadados da captura

Conforme declarado no JSON incluído no arquivo:

- Fonte: `https://allnations.com.br/`
- Data de captura indicada: `2026-10-22T15:45:29+00:00`
- Páginas visitadas: 300
- Páginas HTML lidas: 290
- Produtos distintos: 103
- Produtos com preço preenchido: 0
- Erros ou restrições registados: 9

Estes metadados descrevem o conteúdo recebido; não comprovam uma execução posterior do coletor corrigido nem uma captura com limite de 1.000 páginas.

## 4. Conclusão e ação necessária

O arquivo recebido **não valida** o hash informado. Não é possível determinar apenas por esta comparação se o hash informado pertence a outra versão do ZIP, a outro arquivo, ou se houve alteração no percurso de transferência.

Para resolver a divergência, deve-se calcular novamente o SHA-256 do ZIP na origem e compará-lo com o hash calculado aqui. Se o hash da origem for o valor informado, deve ser enviado novamente o arquivo correspondente. Os preços da ALLNATIONS continuam por obter: o CSV e o JSON incluídos não contêm preços preenchidos.

## 5. Referências no repositório

- [CSV de produtos ALLNATIONS](https://github.com/carlos-andrade/LICITACAO/blob/main/FORNECEDORES/allnations-produtos.csv)
- [JSON de produtos ALLNATIONS](https://github.com/carlos-andrade/LICITACAO/blob/main/FORNECEDORES/allnations-produtos.json)
- [Script de captura](https://github.com/carlos-andrade/LICITACAO/blob/main/scripts/capture_allnations_catalog.py)
- [Workflow de captura](https://github.com/carlos-andrade/LICITACAO/actions/workflows/captura-allnations.yml)
