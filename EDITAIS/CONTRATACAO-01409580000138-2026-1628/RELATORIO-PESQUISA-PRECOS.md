# Verificação e pesquisa inicial — Dispensa MPGO 01409580000138-1-001628/2026

**Data da pesquisa:** 24/10/2026  
**Fonte oficial da contratação:** https://pncp.gov.br/app/editais/01409580000138/2026/1628  
**Objeto:** aquisição de medidor digital de espessura por ultrassom com datalogger, certificado de calibração rastreável à RBC/Inmetro e gel acoplante.

## 1. Situação dos anexos

A captura registrada no repositório obteve respostas binárias dos quatro endpoints de arquivos (IDs 1–4), com tamanhos de 65.704, 7.869, 8.673 e 1.241.843 bytes. Entretanto, o CSV de downloads anterior registrou falhas porque as URIs fornecidas pela API apontavam para `pncp.gov.br:10240`, uma porta interna que não estava acessível no runner.

Foi corrigido o script `scripts/capturar_edital_pncp.py` para normalizar essas URIs removendo a porta interna e mantendo o host público HTTPS. **A correção foi commitada, mas precisa ser executada novamente no GitHub Actions para confirmar que os quatro arquivos podem ser baixados, identificados e abertos.** Arquivos `.bin` antigos não devem ser tratados como documentos validados até verificar assinatura/formato e conteúdo.

Workflow: https://github.com/carlos-andrade/LICITACAO/actions/workflows/capturar-edital-pncp.yml

## 2. Itens e valores estimados capturados

| Item | Descrição resumida capturada | Quantidade | Valor unitário estimado | Total estimado |
|---|---|---:|---:|---:|
| 1 | Medidor de espessura ultrassônico com datalogger | 1 | R$ 2.380,00 | R$ 2.380,00 |
| 2 | Medidor de espessura ultrassônico com datalogger (descrição resumida da API) | 2 | R$ 90,00 | R$ 180,00 |
| **Total** |  |  |  | **R$ 2.560,00** |

A descrição resumida do item 2 parece atípica diante do objeto global, que inclui gel acoplante. É necessário conferir o Termo de Referência e o aviso antes de assumir que o item 2 seja gel. O valor de referência do órgão não é uma cotação de fornecedor.

## 3. Pesquisa pública inicial de preços

Os preços abaixo são anúncios públicos localizados na internet, não cotações formais nem confirmação de venda para esta contratação. Frete, impostos eventualmente adicionais, estoque, validade da oferta e entrega em Goiânia ainda precisam ser confirmados por escrito.

| Fornecedor / modelo | Preço anunciado | Calibração | Aderência e pendências |
|---|---:|---|---|
| TecnoFerramentas — Novotest-br GT1201 com armazenamento de dados | R$ 1.685,53 à vista, anunciado com opção de certificado RBC de R$ 42,49 e total combinado exibido de R$ 1.685,53 | Opção rastreável RBC/Inmetro | **Pendente.** Confirmar por escrito datalogger, modelo, certificado requerido, gel, estoque, frete e tributos. Fonte: https://www.tecnoferramentas.com.br/medidor-de-espessura-por-ultrassom-1003000mm-5mhz--25mhz-armazenamento-de-dados-valor-max-min-e-medio-novotestbr-gt1201-110267_0/p?idsku=210169807 |
| TecnoFerramentas — Novotest-br GM100 com certificado | R$ 1.935,44 à vista | A página informa certificado rastreável Inmetro/RBC e gel de 50 ml | **Pendente.** A página consultada não comprova datalogger. Confirmar aderência integral, frete, tributos, estoque e prazo. Fonte: https://www.tecnoferramentas.com.br/medidor-de-espessura-ultrassonico-capacidade-12-220mm-tecnoferramentas-gm100-com-certificado-de-calibracao-500797/p |
| Instrutherm — ME-260 | R$ 2.244,14 + R$ 299,00 de certificado = R$ 2.543,14, antes de frete | Certificado RBC opcional, seis pontos de calibração | **Não comparável sem esclarecimento.** A página informa prazo de entrega de até 50 dias; não evidencia datalogger. O total com certificado supera R$ 2.380,00 antes do frete. Fonte: https://www.instrutherm.com.br/medidor-de-espessura-me-260 |
| Casmet Engenharia — ME-215 | Preço não publicado | Página menciona certificado rastreável | **Pendente de cotação.** Não há preço público nem confirmação de datalogger/aderência integral. Fonte: https://casmetconsultoria.com.br/instrutherm-me-215/ |

### Intervalo de preços

Não há ainda intervalo mínimo/máximo confiável para fornecedores tecnicamente aderentes. Os dois preços da TecnoFerramentas correspondem a modelos diferentes e a aderência ao requisito de datalogger ainda não foi demonstrada para ambos. O ME-260 da Instrutherm não deve ser usado como comparável integral sem confirmar datalogger e demais exigências. A Casmet não publica preço.

**Faixa bruta observada de anúncios de equipamento:** R$ 1.685,53 a R$ 2.543,14 com certificado no caso Instrutherm, antes de custos de entrega e tributos não informados. Essa faixa é apenas indicativa e mistura modelos de aderência técnica incompleta; não é uma faixa validada de cotações.

## 4. Aplicação da política financeira interna

Para o valor total estimado de R$ 2.560,00:
- teto de custos operacionais (60%): **R$ 1.536,00**;
- meta de lucro (20%): **R$ 512,00**;
- reserva protegida (20%): **R$ 512,00**.

Mesmo o menor anúncio localizado para equipamento (R$ 1.685,53) ultrapassa o teto interno de custos operacionais de R$ 1.536,00 antes de frete, tributos e custos de entrega, caso seja imputado integralmente a este contrato. Isso **não sustenta recomendação de participação no momento**. É preciso confirmar o que compõe o item 2 e conseguir preço formal que satisfaça a especificação, a política financeira e o custo total.

## 5. Fornecedores: quantidade e validação

Foram identificados três fornecedores/lojas como possíveis contatos (TecnoFerramentas, Instrutherm e Casmet), mas somente duas páginas apresentaram preços públicos úteis; uma delas é de modelo cuja aderência não está confirmada. Não foi possível comprovar dez fornecedores distintos com produtos tecnicamente equivalentes e preço público. Não serão inventados fornecedores, preços, CNPJs ou cotações para preencher uma meta numérica.

## 6. Próximas verificações necessárias

1. Executar novamente o workflow de captura após a correção das URLs.
2. Abrir os quatro anexos e validar nome, extensão, conteúdo e requisitos do Termo de Referência.
3. Confirmar a descrição correta do item 2 e as quantidades.
4. Solicitar cotações formais aos fornecedores identificados, com CNPJ, modelo, datalogger, certificado RBC/Inmetro, gel, frete, impostos, prazo, estoque, validade e preço total entregue em Goiânia.
5. Só calcular mínimo/máximo após normalizar especificações e excluir anúncios não comparáveis.
6. Aplicar a política CDC e a política financeira do repositório antes de recomendar participação.

## Fontes

- PNCP oficial: https://pncp.gov.br/app/editais/01409580000138/2026/1628
- TecnoFerramentas GT1201: https://www.tecnoferramentas.com.br/medidor-de-espessura-por-ultrassom-1003000mm-5mhz--25mhz-armazenamento-de-dados-valor-max-min-e-medio-novotestbr-gt1201-110267_0/p?idsku=210169807
- TecnoFerramentas GM100: https://www.tecnoferramentas.com.br/medidor-de-espessura-ultrassonico-capacidade-12-220mm-tecnoferramentas-gm100-com-certificado-de-calibracao-500797/p
- Instrutherm ME-260: https://www.instrutherm.com.br/medidor-de-espessura-me-260
- Casmet ME-215: https://casmetconsultoria.com.br/instrutherm-me-215/
