# Calculadora de viabilidade — Sistema LICITAÇÃO

| Campo | Valor |
|---|---|
| **ID** | LIC-DOC-SCRIPTS-README-CALCULADORA-VIABILIDADE-MD-D2311248 |
| **Projeto** | LICITAÇÃO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | N/A — fase não definida no conteúdo de origem |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | fca35070dcf881011f9e4f6ea40a5c12d36d408540213c47ada963f7fee1ea61 |
| **Commit de referência (versão anterior)** | [b5e445630ceaf57fac58ae963dbedc587d836e52](https://github.com/carlos-andrade/LICITACAO/commit/b5e445630ceaf57fac58ae963dbedc587d836e52) |
| **Data de criação** | N/A — data histórica não verificada |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Responsável pelo projeto LICITAÇÃO |
| **Aprovador** | Pendente — não há evidência de aprovação neste documento |
| **Origem** | Conteúdo existente no repositório; caminho: `scripts/README-calculadora-viabilidade.md` |
| **Autoridade superior** | [Constituição do projeto](https://github.com/carlos-andrade/LICITACAO/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

Arquivo: `scripts/calculadora_viabilidade.py`

## Objetivo
Calcular receita, custo de aquisição, imposto incremental informado, DAS alocado, frete, despesas adicionais, lucro, margem sobre receita, markup sobre custo e teto máximo de compra para uma meta de margem.

Usa `Decimal` para evitar erros comuns de ponto flutuante. O resultado inclui pendências e bloqueia a liberação para participação quando não há confirmação dos pontos críticos.

## Exemplo de uso
Executar a partir da raiz do repositório:

```bash
python scripts/calculadora_viabilidade.py \
  --opportunity-id PNCP-UFRJ-2026-548 \
  --item-id PNCP-UFRJ-2026-548-ITEM-1 \
  --scenario-name "UFRJ base preliminar" \
  --quantity 715 \
  --sale-price 8.67 \
  --acquisition-price 3.00 \
  --das-allocated 82.05 \
  --freight 637.40 \
  --target-margin 0.50 \
  --assumption "Frete é hipótese pública preliminar, não cotação" \
  --pending-cost "Entrega nos cinco endereços não cotada" \
  --output /tmp/ufrj-cenario.json
```

O exemplo é ilustrativo. Não implica que R$ 3,00 seja um preço de aquisição encontrado ou viável, nem que R$ 637,40 seja o frete real. O programa não presume alíquota fiscal: `--tax-rate` só deve receber um valor validado para a operação.

## Confirmações que afetam o status
Os flags abaixo só devem ser usados quando houver evidência real:
- `--tax-confirmed`: tratamento fiscal validado.
- `--freight-confirmed`: cotação válida cobre a carga e todos os destinos.
- `--technical-compliance-confirmed`: documentação confirma a especificação do edital.
- `--supplier-capacity-confirmed`: fornecedor confirmou quantidade e prazo.

Sem essas confirmações, o cenário permanece como estimativa e a recomendação é `PARTICIPATION_NOT_CLEARED`.

## Fórmulas
- Receita = quantidade × preço de venda unitário.
- Aquisição = quantidade × custo unitário de aquisição.
- Custo total = aquisição + imposto incremental + DAS alocado + frete + despesas adicionais.
- Lucro = receita − custo total.
- Margem sobre receita = lucro ÷ receita.
- Markup sobre custo = lucro ÷ custo total.
- Teto de aquisição = orçamento máximo de custos compatível com a meta − custos não relacionados à aquisição.

O teto monetário é arredondado para baixo a centavos antes do cálculo do teto de aquisição. O preço unitário máximo também é arredondado para baixo a centavos: assim, comprar todas as unidades pelo preço unitário exibido não ultrapassa o teto total. O preço médio matemático pode ser, portanto, ligeiramente superior ao preço unitário operacional permitido.

## Testes
```bash
python -m unittest discover -s scripts/tests -v
```

Para validar schemas e exemplos:
```bash
python -m pip install jsonschema
python scripts/validate_schemas.py
```

Os testes devem ser executados em um checkout atualizado antes de considerar a ferramenta validada em produção.
