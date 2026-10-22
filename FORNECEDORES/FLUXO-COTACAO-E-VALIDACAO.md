# Fluxo de cotação e validação de fornecedores

## Objetivo
Registrar evidências comparáveis de fornecedores e impedir que preço indicativo seja tratado como cotação formal ou que menor preço seja confundido com conformidade técnica.

## Estados permitidos
- `indicative_web_price`: preço público consultado; não comprova disponibilidade, validade, frete, tributos ou atendimento integral ao edital.
- `requested`: solicitação enviada; ainda sem proposta recebida.
- `formal_received`: proposta formal recebida, aguardando análise.
- `validated`: preço, escopo, quantidade, prazo e documentação conferidos.
- `rejected`: não atende a um requisito ou condição comercial; registrar motivo.
- `expired`: prazo de validade da proposta terminou.

## Campos mínimos a coletar
1. Razão social/nome, CNPJ (quando aplicável), contato e data.
2. Fabricante, marca, código e descrição exata do produto.
3. Confirmação de PP, capacidade 180 ml, uso com líquidos quentes e frios, característica oxi-biodegradável e atoxicidade, conforme edital.
4. Evidência documental da norma técnica e selo/certificação exigidos. A divergência do edital UFRJ sobre referências normativas precisa ser esclarecida formalmente antes de marcar conformidade como validada.
5. Unidade comercial (pacote com 100), quantidade disponível e capacidade de fornecer 715 pacotes.
6. Preço unitário, total, tributos incluídos/excluídos e condições de pagamento.
7. Frete até os cinco endereços de entrega, com indicação explícita se o valor cobre todos os destinos.
8. Prazo de expedição/entrega, validade da proposta e disponibilidade dentro do prazo do edital.
9. Data de recebimento, responsável pela análise, documentos e URL/fonte.

## Regras de validação
- Não marcar `validated` se houver campo crítico sem evidência.
- Não usar preço de varejo, anúncio ou captura sem data como cotação formal.
- Não comparar preços unitários sem normalizar a unidade para pacote com 100 unidades.
- Separar preço do produto, frete, tributos incrementais, entrega local, manuseio, custo financeiro e contingência.
- Registrar motivo objetivo para rejeição; preservar a cotação original e seus documentos.
- Uma cotação válida não substitui a análise jurídica, fiscal nem a decisão formal de participar.

## Checklist — oportunidade UFRJ
- [ ] Cotação formal identificada e datada.
- [ ] Especificação técnica comprovada por ficha técnica/documento do fabricante.
- [ ] Divergência normativa esclarecida com a Administração ou por documento oficial suficiente.
- [ ] 715 pacotes disponíveis para entrega integral.
- [ ] Preço e condições de pagamento registrados.
- [ ] Frete cotado para os cinco endereços, não apenas para um CEP.
- [ ] Prazo de entrega compatível com o instrumento convocatório.
- [ ] Tratamento tributário validado para a operação específica.
- [ ] Cálculo atualizado e margem calculada sobre a receita, incluindo todos os custos.
- [ ] Validade da proposta cobre o período necessário.

## Mensagem-modelo para solicitar cotação
Solicitar ao fornecedor uma proposta formal com:
- preço por pacote com 100 unidades e preço total para 715 pacotes;
- marca, fabricante, código e ficha técnica;
- evidência documental dos requisitos técnicos do edital;
- disponibilidade para fornecimento integral;
- tributos incluídos/excluídos;
- frete detalhado para os cinco destinos indicados no edital da UFRJ;
- prazo de entrega, condições de pagamento e validade da proposta;
- identificação fiscal do fornecedor e contato responsável.

Não afirmar que o produto atende a uma norma que não esteja comprovada documentalmente. Anexar o edital e o Termo de Referência à solicitação e pedir confirmação expressa de cada requisito.

## Relação com o schema
Cada proposta efetivamente recebida deve ser registrada em um arquivo JSON individual conforme `ARQUITETURA/schemas/cotacao.schema.json`. Não criar registro de cotação fictício para representar ausência de resposta. Preços indicativos devem permanecer identificados como `indicative_web_price`.
