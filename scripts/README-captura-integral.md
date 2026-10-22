# Capturador integral PNCP

Este script tenta reunir em uma execução:
- detalhes e endpoints comuns da contratação;
- itens;
- arquivos/documentos;
- atas de registro de preço;
- contratos e empenhos;
- histórico;
- HTML e texto renderizados;
- links e respostas JSON observados no tráfego de rede do navegador.

## Instalação

```bash
python -m pip install requests beautifulsoup4 playwright
python -m playwright install chromium
```

## Execução para o processo de exemplo

```bash
python scripts/pncp_capture_integral.py "https://pncp.gov.br/app/editais/33663683000116/2026/548" --output-dir EDITAIS --download-files
```

Gera:
- `AAAA-SEQ-CNPJ-captura-integral.json`: respostas de API, HTML/texto, frames, links, respostas de rede e diagnósticos;
- `AAAA-SEQ-CNPJ-todos-campos.csv`: cada campo encontrado nas respostas JSON, com endpoint e caminho do campo;
- `AAAA-SEQ-CNPJ-captura-integral.md`: resumo de diagnóstico e cobertura das cinco seções;
- opcionalmente, diretório `*_arquivos/` com os links identificados que puderem ser baixados.

## O que significa “tudo”

O script combina endpoints comuns da API e uma sessão real de Chromium via Playwright. A interface do PNCP pode mudar e os endpoints de atas/contratos/empenhos/histórico podem depender de outras rotas ou paginação. Por isso o JSON bruto e os diagnósticos são parte essencial da captura: resposta HTTP com erro não significa que a seção esteja vazia. Confira os parâmetros de paginação e os totais retornados antes de considerar uma lista completa.

O download de um PDF ou arquivo Office não extrai seu conteúdo interno. Para obter tabelas e texto desses anexos, rode uma etapa de parsing/OCR separada. Não trate a ausência de campos como prova de ausência da informação.

Fontes oficiais: [API de Consulta PNCP](https://pncp.gov.br/api/consulta/swagger-ui/index.html) · [Manual PNCP](https://pncp.gov.br/manual/pt-br/latest/).
