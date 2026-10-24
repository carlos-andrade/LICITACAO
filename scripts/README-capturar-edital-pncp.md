# Captura reutilizável de editais PNCP

| Campo | Valor |
|---|---|
| **ID** | LIC-DOC-SCRIPTS-README-CAPTURAR-EDITAL-PNCP-MD-7C4C13D0 |
| **Projeto** | LICITAÇÃO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | N/A — fase não definida no conteúdo de origem |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | f538ce6aa45d543b39bfc627b70dbf164a4eebf19ca93f3deaaac73e6163fb12 |
| **Commit de referência (versão anterior)** | [1750a00407fd2cb8ce285b8efe039c32882969c5](https://github.com/carlos-andrade/LICITACAO/commit/1750a00407fd2cb8ce285b8efe039c32882969c5) |
| **Data de criação** | N/A — data histórica não verificada |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Responsável pelo projeto LICITAÇÃO |
| **Aprovador** | Pendente — não há evidência de aprovação neste documento |
| **Origem** | Conteúdo existente no repositório; caminho: `scripts/README-capturar-edital-pncp.md` |
| **Autoridade superior** | [Constituição do projeto](https://github.com/carlos-andrade/LICITACAO/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

Script: `scripts/capturar_edital_pncp.py`

## Execução

```bash
python -m pip install requests openpyxl
python scripts/capturar_edital_pncp.py --url "https://pncp.gov.br/app/editais/01409580000138/2026/1628" --download-files
```

A saída será gravada em `EDITAIS/CONTRATACAO-01409580000138-2026-1628/`. Para outro edital, basta trocar a URL.

## Arquivos produzidos

- `captura-bruta.json`: respostas e metadados de origem, diagnóstico HTTP, links e resultados de download.
- `todos-os-campos.csv`: campos retornados pela API, preservados em formato tabular.
- `itens.csv`: normalização inicial dos itens retornados pela API.
- `arquivos.csv` e `downloads.csv`: URLs de documentos e situação de cada tentativa de download.
- `arquivos_originais/`: anexos baixados quando a API expõe URLs acessíveis.
- `captura-pncp.xlsx`: planilha com os campos brutos, se `openpyxl` estiver instalado.
- `pesquisa-fornecedores-template.csv`: dez espaços de pesquisa por item; espaços vazios não representam fornecedores reais nem cotações.

## Limites e regras de qualidade

1. O script consulta endpoints de detalhe, itens, arquivos, histórico e outras seções opcionais. O PNCP pode mover endpoints, exigir outros parâmetros ou alterar o esquema; por isso, a execução registra falhas HTTP e não interpreta endpoint 404 como prova de inexistência.
2. A API pode retornar apenas uma página, campos com nomes diferentes ou URLs de arquivo que exijam tratamento adicional. Conferir `diagnostico_http`, paginação, anexos e a página oficial antes de declarar captura completa.
3. O script não inventa fornecedores nem recolhe preços de lojas de forma universal. Para pesquisar preços reais, cada linha precisa de fonte rastreável, data/hora, especificação equivalente, preço, frete, tributos, estoque, prazo e validade da oferta. A quantidade-alvo é dez fornecedores verificáveis por item, quando disponíveis; caso contrário, registrar quantos foram encontrados e a limitação.
4. Preço anunciado não é garantia de estoque nem prova automática de obrigação de venda nas condições do edital. Solicitar confirmação/cotação formal para decisão comercial.
5. Aplicar a regra financeira do projeto: custo operacional completo máximo de 60% do preço contratual; lucro-alvo 20%; reserva 20%. Frete, tributos, calibração, acessórios, taxas, financiamento e entrega são custos, não valores presumidos como zero.
6. Não guardar tokens, senhas ou credenciais no repositório. Antes de publicar arquivos, verificar se os anexos contêm dados pessoais ou informação confidencial.

## Fonte oficial

[Portal Nacional de Contratações Públicas](https://pncp.gov.br/).

## Controle de conformidade de fornecedores (CDC)

A pesquisa comercial deve observar a [política de conformidade de fornecedores](../docs/POLITICA-CONFORMIDADE-FORNECEDORES-CDC.md), com referência ao CDC e ao Decreto nº 7.962/2013 conforme aplicabilidade. Antes de considerar uma oferta válida, registar a fonte e data, a especificação, o preço anunciado, frete e demais despesas, preço total entregue, disponibilidade, prazo e validade.

- Não negociar com fornecedor quando houver evidência confiável de incumprimento de obrigação legal aplicável, publicidade enganosa ou omissão material.
- Se houver dúvida ou faltar evidência, classificar como PENDENTE e não usar a oferta como cotação aprovada.
- O preço anunciado não comprova, por si só, estoque, custo final entregue ou obrigação incondicional de venda.
- Não criar nomes ou preços para preencher a meta de dez fornecedores. Reportar apenas fornecedores encontrados e verificáveis.

