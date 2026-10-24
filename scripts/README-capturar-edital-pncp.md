# Captura reutilizável de editais PNCP

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
