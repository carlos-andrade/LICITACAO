# Modelo de Dados v1 — Guia de implementação

| Campo | Valor |
|---|---|
| **ID** | LIC-GUIA-DADOS-001 |
| **Projeto** | LICITAÇÃO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | GUIA_TECNICO |
| **Fase** | Modelagem de dados |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | 0752d3cfaa8515178a514d5418dc9699665ad01cfed6ff85a667094d26fe6566 |
| **Commit de referência (versão anterior)** | [afe4a46ea2cf5e4ee55b49b7358221e57881f739](https://github.com/carlos-andrade/LICITACAO/commit/afe4a46ea2cf5e4ee55b49b7358221e57881f739) |
| **Data de criação** | 2026-10-22 — primeira evidência disponível no repositório |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Responsável pelo projeto LICITAÇÃO |
| **Aprovador** | Pendente de aprovação documental |
| **Origem** | Conteúdo anterior e histórico Git |
| **Autoridade superior** | [Constituição do projeto](https://github.com/carlos-andrade/LICITACAO/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

Este guia complementa a arquitetura central. Os schemas e exemplos são a primeira versão do contrato de dados do Sistema LICITAÇÃO.

## Arquivos
- [Arquitetura central](../ARQUITETURA-CENTRAL-SISTEMA-LICITACAO.md)
- [Schema de oportunidade](schemas/oportunidade.schema.json)
- [Schema de item](schemas/item.schema.json)
- [Schema de documento](schemas/documento.schema.json)
- [Schema de cotação](schemas/cotacao.schema.json)
- [Schema de cenário econômico](schemas/cenario-economico.schema.json)
- [Schema de decisão](schemas/decisao.schema.json)
- [Exemplo UFRJ — oportunidade](exemplos/ufrj-2026-548-oportunidade.json)
- [Exemplo UFRJ — item](exemplos/ufrj-2026-548-item-1.json)
- [Validador local](../scripts/validate_schemas.py)
- [Fluxo de cotação e validação de fornecedores](../FORNECEDORES/FLUXO-COTACAO-E-VALIDACAO.md)

## Identificadores e relações
- `oportunidade.id` é a chave interna estável.
- `item.opportunity_id`, `documento.opportunity_id`, `cotacao.opportunity_id`, `cenario_economico.opportunity_id` e `decisao.opportunity_id` referenciam essa chave.
- `item.id` é referenciado por cotações e cenários econômicos.
- IDs externos do PNCP são armazenados separadamente e nunca substituem o ID interno.
- Os schemas validam formato; a aplicação deverá validar referências cruzadas e regras de negócio.

## Convenções
- Dinheiro em BRL; na implementação de cálculo, usar Decimal ou tipo decimal no banco.
- Datas ISO 8601, preservando fuso quando conhecido.
- Não preencher lacunas com suposições silenciosas.
- Preço de página pública deve ser classificado como preço indicativo, não cotação formal.
- Estados de validação refletem evidência disponível, não apenas a presença do campo.
- Toda alteração incompatível de contrato de dados exige revisão de versão.

## Validação
Com Python 3 e pacote `jsonschema`:
```bash
python -m pip install jsonschema
python scripts/validate_schemas.py
```

O validador está versionado, mas precisa ser executado num checkout do repositório antes de afirmar que todos os arquivos passaram nos testes. Os próximos testes devem cobrir também cálculos do motor econômico, referências cruzadas, campos obrigatórios por estado e dados pendentes.
