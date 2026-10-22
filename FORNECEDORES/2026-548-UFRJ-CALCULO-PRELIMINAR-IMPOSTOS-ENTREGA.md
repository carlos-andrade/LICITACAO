# UFRJ — Estimativa refinada de impostos, frete e teto de compra
Data: 22/10/2026

## Dados confirmados do edital e do usuário
- Quantidade: 715 pacotes.
- Preço de referência: R$ 8,67 por pacote.
- Receita bruta máxima se vender pelo valor de referência: R$ 6.199,05.
- Meta do usuário: lucro de pelo menos 50% da receita/preço de referência.
- Teto total de custos para preservar essa meta: aproximadamente R$ 3.099,53 (metade de R$ 6.199,05; usar R$ 3.099,52 como limite operacional conservador por arredondamento).
- Regime informado: MEI.
- Receita anual informada pelo usuário: abaixo do limite de R$ 81.000, mas o valor acumulado exato não foi fornecido.
- CEP de origem informado: 05685-000, São Paulo/SP.
- Destino: cinco pontos da UFRJ no Rio de Janeiro/RJ; o frete precisa contemplar a entrega nos cinco pontos, não apenas o transporte entre cidades.

## Impostos — cenário MEI
A Receita Federal informa que, em 2026, o DAS-MEI de comércio/indústria (contribuição INSS + ICMS) é R$ 82,05 por mês. Para serviços, o valor é diferente. Fonte oficial: https://www8.receita.fazenda.gov.br/SimplesNacional/Noticias/NoticiaCompleta.aspx?id=48dfa572-321f-423b-a014-5ed6629cb0ba

Para esta simulação, alocamos um mês de DAS de comércio (R$ 82,05) ao contrato. Isso é um rateio prudencial de custo fixo, não uma alíquota adicional sobre a venda. O DAS é devido mensalmente independentemente da receita específica desta venda, desde que o enquadramento permaneça válido.

**Ponto de controle:** confirme que a receita bruta acumulada do ano, somada aos R$ 6.199,05 deste contrato e a outras receitas ainda previstas, permanece dentro do limite aplicável ao MEI. A resposta “está abaixo do limite” não revela quanto resta de margem. Também é necessário confirmar que a ocupação/CNAE permite a atividade e que o MEI pode cumprir a habilitação e a emissão de nota fiscal exigidas na contratação pública.

## Frete — referência pública, não cotação
Uma página de transportadora publica frete fracionado São Paulo → Rio de Janeiro a partir de R$ 637,40, referindo-se a carga mínima de 30 kg ou 0,33 m³; o preço final depende de peso, cubagem, valor declarado e modalidade. Fonte: https://zurcadtransportes.com.br/quanto-custa-frete

Esse valor **não é uma cotação para esta carga** e não confirma entrega nos cinco endereços. Sem quantidade de volumes, peso total, dimensões das caixas e confirmação de entrega múltipla, o frete real não pode ser fechado. Para planejamento, simulamos R$ 637,40 (referência pública inicial), R$ 750 e R$ 1.000. Os dois últimos são hipóteses, não preços consultados.

## Cálculo do teto para compra dos produtos
Fórmula conservadora:
(R$ 3.099,52 de custo total máximo − R$ 82,05 de DAS alocado − frete) ÷ 715 pacotes.

| Cenário de frete | Frete por pacote | DAS alocado | Teto agregado para mercadoria | Teto de compra por pacote |
|---|---:|---:|---:|---:|
| Referência pública inicial: R$ 637,40 | R$ 0,89 | R$ 82,05 | R$ 2.380,07 | R$ 3,33 |
| Hipótese intermediária: R$ 750,00 | R$ 1,05 | R$ 82,05 | R$ 2.267,47 | R$ 3,17 |
| Hipótese conservadora: R$ 1.000,00 | R$ 1,40 | R$ 82,05 | R$ 2.017,47 | R$ 2,82 |

Os tetos acima ainda não reservam verba para embalagem, mão de obra, deslocamentos entre os cinco locais, taxas, custos financeiros, perdas ou outros gastos. Se houver qualquer um desses custos, subtraí-los antes de determinar o preço máximo de compra. Por prudência, não tratar o cenário de R$ 637,40 como custo de entrega garantido.

## Conclusão econômica
Para manter lucro de pelo menos 50% da receita de R$ 6.199,05, o preço de aquisição precisaria ficar em torno de R$ 2,82 a R$ 3,33 por pacote nos cenários simulados, antes de outros custos operacionais. Os preços públicos encontrados anteriormente estavam substancialmente acima disso. A operação parece inviável sem preço direto de fabricante muito abaixo do varejo e uma solução de frete consolidado de baixo custo.

## Próximos passos objetivos
1. Pedir cotação formal de frete com origem CEP 05685-000 e os cinco destinos finais no Rio, informando peso real, dimensões e número de volumes. Solicitar valor total com taxas de entrega múltipla, descarga, seguro, impostos do transporte e prazo.
2. Pedir aos fornecedores preço por pacote para 715 unidades de embalagem (71.500 copos), com entrega incluída ou separada, disponibilidade comprovada e documentação técnica compatível com o TR.
3. Confirmar com o contador: CNAE/ocupação permitida, emissão de NF para órgão público, situação cadastral e margem exata restante até o limite anual do MEI.
4. Não ofertar lance antes de validar produto, preço, frete e capacidade de entrega. Se o custo total passar de R$ 3.099,52, a meta de lucro não será atingida.
