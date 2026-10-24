# Modelo de Dados v1 — Sistema LICITAÇÃO

| Campo | Valor |
|---|---|
| **ID** | LIC-DOC-ARQUITETURA-SCHEMAS-README-MD-8B255086 |
| **Projeto** | LICITAÇÃO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | README |
| **Fase** | N/A — fase não definida no conteúdo de origem |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | e84e0e5f462f2c745bb7ff1db352502ad7c0a8757494e427b1cbdf6877438860 |
| **Commit de referência (versão anterior)** | [b5e445630ceaf57fac58ae963dbedc587d836e52](https://github.com/carlos-andrade/LICITACAO/commit/b5e445630ceaf57fac58ae963dbedc587d836e52) |
| **Data de criação** | N/A — data histórica não verificada |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Responsável pelo projeto LICITAÇÃO |
| **Aprovador** | Pendente — não há evidência de aprovação neste documento |
| **Origem** | Conteúdo existente no repositório; caminho: `ARQUITETURA/schemas/README.md` |
| **Autoridade superior** | [Constituição do projeto](https://github.com/carlos-andrade/LICITACAO/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

Esta pasta contém schemas JSON Schema Draft 2020-12 para normalizar os registros do sistema.

## Schemas
- `oportunidade.schema.json`: oportunidade e metadados do processo.
- `item.schema.json`: item, quantidade, unidade, preço de referência e requisitos.
- `documento.schema.json`: documentos de origem e estado de captura/validação.
- `cotacao.schema.json`: cotação de fornecedor, disponibilidade, frete e evidências.
- `cenario-economico.schema.json`: receita, aquisição, tributos, logística, custo total, lucro e margens.
- `decisao.schema.json`: decisão humana, riscos, pendências e aprovação.

## Regras de modelagem
1. Identificadores internos devem ser estáveis e não substituir os IDs externos da fonte.
2. Campos ausentes não devem ser preenchidos por inferência. Use `null` quando permitido e registre pendências em notas/listas próprias.
3. Datas e horas devem ser ISO 8601 com fuso horário sempre que conhecido.
4. Valores monetários usam BRL; cálculos em produção devem usar decimal exato (não ponto flutuante binário).
5. `indicative_web_price` não é cotação formal. A existência de preço público não comprova estoque, capacidade de entrega nem conformidade técnica.
6. Os schemas validam a forma dos dados; não garantem que os dados sejam verdadeiros ou que a regra de negócio tenha sido cumprida.
7. Toda análise econômica deve separar margem sobre receita de markup sobre custo.
8. Requisitos técnicos e fiscais críticos precisam de validação humana e evidência documental.

## Validação local
Com Python 3 e `jsonschema` instalado:

```bash
python -m pip install jsonschema
python scripts/validate_schemas.py
```

O script deve ser executado a partir da raiz do repositório. Ele valida a sintaxe dos schemas, os exemplos em `ARQUITETURA/exemplos/` e regras aritméticas explícitas para cenários econômicos.
