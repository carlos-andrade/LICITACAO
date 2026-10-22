# Capturador de dados PNCP — LICITAÇÃO

Este utilitário recebe uma URL pública de contratação do PNCP, consulta endpoints públicos, tenta extrair metadados HTML e links da página e gera:
- tabela Markdown com metadados, itens, documentos e status de cada fonte;
- CSV com os campos normalizados dos itens;
- JSON bruto com respostas de API, metadados e diagnósticos;
- opcionalmente, download dos documentos listados pela API.

## Instalação
```bash
python -m pip install requests beautifulsoup4
```

## Exemplo
```bash
python scripts/pncp_capture.py "https://pncp.gov.br/app/editais/33663683000116/2026/548" --output-dir EDITAIS --download-docs
```

Os arquivos recebem nomes baseados no ano, sequencial e CNPJ. O script não atualiza o GitHub diretamente: ele gera artefatos locais para revisão e commit, evitando publicar automaticamente uma captura parcial ou campos errados. Se a captura for integrada a GitHub Actions futuramente, use credenciais em secrets e mantenha revisão dos resultados antes do merge.

## Fontes oficiais
- [Swagger da API pública de consulta do PNCP](https://pncp.gov.br/api/consulta/swagger-ui/index.html)
- [Manual de integração do PNCP](https://pncp.gov.br/manual/pt-br/latest/)
- [Documentação de consulta dos itens](https://pncp.gov.br/manual/pt-br/latest/contratacao/consultar_itens_de_uma_contratacao.html)
- [Documentação de consulta dos arquivos](https://pncp.gov.br/manual/pt-br/latest/contratacao/consultar_todos_documentos_de_uma_contratacao.html)

## Limitações conhecidas
- A página pode ser uma aplicação JavaScript e depender de API; metadados HTML simples não necessariamente contêm a tela exibida.
- A API ou o site podem estar indisponíveis/restringir chamadas em determinados ambientes. O relatório registra os erros.
- PDF/DOC/XLS anexados precisam de parsing separado para extração integral de tabelas/texto; PDF digitalizado pode exigir OCR.
- Campos ausentes não são inferidos. Compare o resultado com a tela e documentos oficiais antes de uso comercial.
- Use apenas conteúdo público e respeite limites operacionais dos serviços consultados.
