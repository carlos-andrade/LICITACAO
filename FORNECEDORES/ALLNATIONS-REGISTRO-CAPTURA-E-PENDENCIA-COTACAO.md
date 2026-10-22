# ALLNATIONS — Registro de captura e pendência de cotação

**Data do registro:** 2026-10-22  
**Fornecedor:** ALLNATIONS  
**Fonte consultada:** https://allnations.com.br/  
**Repositório do projeto:** https://github.com/carlos-andrade/LICITACAO

## 1. Resultado da captura de catálogo

A execução manual **Captura de catálogo ALLNATIONS #7** terminou com sucesso. A autenticação foi confirmada nos logs e o coletor visitou 1.000 páginas.

| Indicador | Resultado |
|---|---:|
| Páginas visitadas | 1.000 |
| Páginas HTML lidas | 1.000 |
| Produtos distintos | 869 |
| Preços capturados explicitamente | 869 |
| Produtos sem preço capturado | 0 |
| Quantidades numéricas de estoque capturadas | 0 |
| Produtos sem quantidade numérica exposta | 869 |

**Conclusão:** o workflow foi executado sem erro operacional, mas a quantidade de estoque não foi localizada nos campos HTML e dados estruturados que o coletor analisa. Isso não significa que os produtos estejam sem estoque; significa que não foi possível confirmar quantidades numéricas na captura.

## 2. Artefatos e evidências

- Workflow: https://github.com/carlos-andrade/LICITACAO/actions/workflows/captura-allnations.yml
- Execução #7 e logs: https://github.com/carlos-andrade/LICITACAO/actions/runs/39841840133
- Logs do job: https://github.com/carlos-andrade/LICITACAO/actions/runs/39841840133/job/120044621770
- Artefato da execução: https://github.com/carlos-andrade/LICITACAO/actions/runs/39841840133/artifacts/12455730131
- CSV de produtos: https://github.com/carlos-andrade/LICITACAO/blob/main/FORNECEDORES/allnations-produtos.csv
- JSON de resultados: https://github.com/carlos-andrade/LICITACAO/blob/main/FORNECEDORES/allnations-produtos.json
- Coletor atualizado para procurar quantidades explícitas em HTML e JSON embutido: https://github.com/carlos-andrade/LICITACAO/blob/main/scripts/capture_allnations_catalog.py
- Commit da ampliação da captura: https://github.com/carlos-andrade/LICITACAO/commit/fc5d1e99031aa8c641280f51f4b57dc37fa11e1d

## 3. Decisão do projeto

Foi decidido **manter a captura de quantidades como não disponível** e solicitar os preços comerciais diretamente ao fornecedor por e-mail. Não preencher quantidades por estimativa nem inferir estoque a partir de indicadores genéricos de disponibilidade.

## 4. Dados a solicitar ao fornecedor

Solicitar cotação formal contendo, para cada produto/SKU:

- SKU e descrição completa;
- preço unitário comercial para compra empresarial;
- quantidade disponível em estoque;
- condições e prazo de pagamento;
- validade da proposta;
- prazo de entrega e valor do frete;
- identificação do fornecedor e CNPJ na proposta.

## 5. Próximas ações

1. Enviar o pedido formal de cotação usando o modelo em `COTAÇÃO/EMAIL-SOLICITACAO-COTACAO-ALLNATIONS.md`.
2. Anexar ou referenciar o catálogo de 869 produtos capturados, conforme o formato adequado para o fornecedor.
3. Ao receber a resposta, arquivar o e-mail e a proposta comercial na pasta correspondente do projeto.
4. Atualizar a tabela comparativa de preços apenas com os valores confirmados na proposta, distinguindo-os dos preços capturados no site.
