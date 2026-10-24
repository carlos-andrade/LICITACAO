# Capturador de catálogo público — ALLNATIONS

| Campo | Valor |
|---|---|
| **ID** | LIC-SCRIPT-ALLNATIONS-CAPTURA-001 |
| **Projeto** | LICITAÇÃO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | DOCUMENTAÇÃO DE SCRIPT |
| **Fase** | Captura experimental / validação |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 44f990d2f251717f079b7d294888ff23670241c4f390d3f90faf7a67b9d68747 |
| **Commit de referência (versão anterior)** | N/A — novo documento |
| **Data de criação** | 2026-10-22 |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Responsável pelo projeto LICITAÇÃO |
| **Aprovador** | Pendente — sem evidência de aprovação |
| **Origem** | Implementação para o domínio público allnations.com.br |
| **Autoridade superior** | [Constituição do projeto](https://github.com/carlos-andrade/LICITACAO/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo

Tentar capturar produtos publicamente acessíveis no domínio https://allnations.com.br/ e exportar um CSV tabular e um JSON de auditoria. O script extrai apenas campos que a página exponha em metadados JSON-LD de tipo `Product`/`ProductGroup` ou metadados Open Graph de produto.

## Instalação

```bash
python -m pip install requests beautifulsoup4
```

## Execução

Na raiz do repositório:

```bash
python scripts/capture_allnations_catalog.py
```

Limitar ou ajustar a velocidade:

```bash
python scripts/capture_allnations_catalog.py --max-pages 1000 --delay 1.0
```

O script gera:

- `FORNECEDORES/allnations-produtos.csv`: tabela para abrir em Excel/LibreOffice;
- `FORNECEDORES/allnations-produtos.json`: dados capturados, diagnóstico, erros e restrições.

É possível escolher caminhos com `--output` e `--json-output`.

## Colunas produzidas

| Coluna | Significado |
|---|---|
| `capturado_em_utc` | Momento de captura em UTC |
| `nome` | Nome público do produto |
| `marca` | Marca, se encontrada |
| `modelo` | Modelo/MPN, se encontrado |
| `sku` | SKU/identificador, se encontrado |
| `gtin` | Código GTIN/EAN, se encontrado |
| `categoria` | Categoria ou caminho de breadcrumbs, se legível |
| `preco` | Preço exposto publicamente, quando disponível |
| `moeda` | Moeda publicada, se fornecida |
| `disponibilidade` | Disponibilidade publicada, quando disponível |
| `url_produto` | URL de origem para auditoria |
| `origem_dado` | Tipo de metadado em que o registo foi encontrado |
| `status_captura` | Qualidade aproximada da captura |
| `observacoes` | Limitações e alertas de interpretação |

## Limites, responsabilidade e interpretação

- O coletor foi atualizado para normalizar links legados com barras invertidas, canonicalizar o host, remover parâmetros comuns de rastreamento, evitar rotas de conta/pedido/checkout e descobrir URLs em sitemaps públicos quando permitidos. A execução deve ser repetida para validar a melhoria; estes ajustes não garantem a captura integral do catálogo.
- Por padrão, o script verifica `robots.txt` e respeita as regras legíveis para o identificador do coletor e para `*`. Se não conseguir ler o ficheiro de regras, termina conservadoramente.
- Não contorna login, CAPTCHA, autenticação, bloqueios HTTP, limites 401/403/429 ou controles de acesso. Não usar `--ignore-robots` sem autorização explícita do proprietário.
- Um catálogo B2B pode exigir conta. Nesse caso, o script não irá descobrir produtos restritos e não tenta contornar autenticação.
- A captura percorre links alcançáveis a partir do ponto inicial com limite de páginas e atraso configuráveis. URLs não ligadas, feeds/APIs não referenciados e páginas carregadas apenas por fluxos privados podem faltar.
- O resultado não deve ser descrito como catálogo completo sem conferir paginação, sitemap, categorias, totais e cobertura do site. O limite padrão do workflow foi aumentado para 1.000 páginas; confirme a duração e os limites do servidor. Ausência no CSV não significa que o fornecedor não venda o item.
- Preços, disponibilidade, SKU e marca só são preenchidos quando constam do HTML público capturado. Nenhum valor é estimado ou fabricado.
- Antes de usar os dados em licitações, revalidar preço, impostos, frete, prazo, garantia, validade e disponibilidade junto ao fornecedor.
