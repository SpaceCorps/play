<!-- wiki-i18n source: 9b9606619f84bd51 -->
<!-- wiki-i18n title: Leilão -->
# Leilão {#auction}

O leilão é o mercado dos pilotos e, ao mesmo tempo, os lotes de cada hora do próprio jogo, numa página do menu da estação. Como a Loja, é uma página da estação: você a usa atracado, não em voo. Ela tem quatro seções. **Mercado** é o que outros pilotos têm à venda. **Lotes** são as ofertas do próprio jogo, uma por hora. **Meus anúncios** é o que você mesmo tem à venda. **Histórico** são as suas vendas, as suas compras e os lotes que você venceu, e como foi o seu comércio.

<!-- market-glance:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- Você precisa do **nível 5** para usar o leilão: para anunciar, comprar e dar lances.
- Um anúncio tem preço por lote, em créditos inteiros ou em Thulium inteiro (não os dois), e nunca abaixo do preço mínimo do item. **Não existe preço máximo.**
- Um preço em Thulium é, no mínimo, o preço mínimo em créditos dividido pela taxa (1.000), arredondado para cima, e só para os itens cujo preço mínimo chega a 1 Thulium ou mais. É só isso que a taxa faz: **1 Thulium = 1.000 créditos é uma regra para o preço mínimo, não uma taxa de câmbio.** Nada é trocado, nenhum valor é mostrado, e créditos e Thulium nunca são somados.
- 80 itens podem ser anunciados, e 79 deles também podem ter preço em Thulium.
- Um anúncio dura 24 / 72 / 168 horas, à sua escolha: as opções são as mesmas em todos os níveis.
- O **depósito** é de 1% do preço para cada 24 horas de duração do anúncio, com mínimo de 50 créditos ou 1 Thulium. Você paga ao anunciar; ele nunca é devolvido, nem se você cancelar o anúncio.
- A partir do nível 10, o depósito é de 1,5%.
- O **imposto** é de 5% do preço. Ele é descontado do que o vendedor recebe quando o anúncio é vendido.
- O depósito e o imposto são queimados: não vão para ninguém.
- A partir do dia 28 da temporada até o reset, não há depósito nem imposto.
- A partir do dia 30 da temporada, o leilão fica fechado até a nova temporada começar: nada pode ser anunciado, comprado ou disputado com lances. Você ainda pode cancelar os seus anúncios.
- Cada moeda tem o seu próprio limite do que você pode vender e do que pode comprar em 24 horas (tabela de níveis abaixo). O que você vence nos Lotes não conta.
- Entre dois pilotos, um comprando do outro, passam no máximo 8.000.000 créditos ou 40.000 Thulium em 24 horas.

<!-- market-glance:end -->

## Itens vendáveis {#marketable-items}

Só podem ser vendidos os itens que você **ganhou**. Tudo o que você ganha leva no [Hangar](/wiki/03-Mechanics/Inventory.md#marketable-items) uma pequena etiqueta, **Vendável**: o que você pega no espaço (drops de alienígenas, enxames, Wardens e do buraco negro: [Carga](/wiki/03-Mechanics/Cargo.md)), o que uma missão paga ([Missões](/wiki/03-Mechanics/Quests.md#rewards)) e tudo o que a Montagem e a Forja fazem. O que você **comprou** na Loja, venceu num lote, comprou no Mercado, recebeu por um código de bônus, um pacote de convite ou o kit inicial, ou recebeu de volta como reembolso não é vendável e nunca pode ser vendido de novo, para que nada seja comprado só para ser revendido. As placas que a Forja do Skylab faz também não são vendáveis; as Reinforced Plates que uma missão paga são.

A etiqueta é um número de unidades, não um interruptor: uma pilha de munição pode ter tiros comprados e ganhos, e o cartão diz “Vendável (3 de 5)”. Quando você usa parte de uma pilha (atirar, criar), as unidades comuns saem primeiro, de modo que as vendáveis duram mais. Combinar duas peças na [Forja](/wiki/06-Items/Forge.md#merge) mantém a etiqueta só se as duas a tinham, e a pré-visualização avisa; uma etapa da Forja que falha devolve os materiais como unidades comuns.

O chip **Somente vendável** do Hangar mostra só o que você pode vender, e o **martelo** ao lado da lixeira de um item com etiqueta abre a folha de venda do Leilão para ele. Na Montagem, uma receita cujo resultado é vendável diz isso, e um material que falta tem um link que abre o Leilão com o nome dele na busca.

Quando o Leilão chegou (0.4.12), o equipamento que você já tinha e que a Loja não vende, e os recursos, foram marcados uma vez. Estes não foram, porque a Loja já os vendeu um dia ou porque o que você tem mistura peças compradas e ganhas: a Quantum Laser III, as Absorption Shield Cells II e III, os Impulse Thrusters II e III, as duas Reinforced Plates e a Base CPU I mais antiga de cada piloto (a do kit inicial). Os novos desses que você ganhar ou criar são marcados.

## O que pode ser vendido {#what-can-be-sold}

<!-- market-kinds:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Tipo | Itens que você pode vender | Quantidade |
| :--- | :--- | ---: |
| **Lasers** | Quantum Laser I, Quantum Laser II, Quantum Laser III, Starfire-III, Helios Beam | 5 |
| **Amplificadores de laser** | Damage Amp I, Crit Amp I, Penetration Amp I, Damage Amp II, Crit Amp II, Penetration Amp II, Damage Amp III, Crit Amp III, Penetration Amp III, Damage Amp IV, Crit Amp IV, Penetration Amp IV | 12 |
| **Escudos** | Light Shield Core, Basic Shield Core, Heavy Shield Core | 3 |
| **Motores** | Engine I, Engine II, Engine III | 3 |
| **Adaptive Cores** | Adaptive Core I, Adaptive Core II, Adaptive Core III | 3 |
| **Células de escudo** | Absorption Shield Cell I, Capacity Shield Cell I, Absorption Shield Cell II, Capacity Shield Cell II, Absorption Shield Cell III, Capacity Shield Cell III, Absorption Shield Cell IV, Capacity Shield Cell IV | 8 |
| **Propulsores** | Impulse Thruster I, Momentum Thruster I, Impulse Thruster II, Momentum Thruster II, Impulse Thruster III, Momentum Thruster III, Impulse Thruster IV, Momentum Thruster IV | 8 |
| **Munição de laser** | Standard Battery (em lotes de 100), Siphon Battery (em lotes de 10), Advanced Plasma (em lotes de 10), Ultra Core (em lotes de 10), Experimental Fusion Core | 5 |
| **Foguetes** | Ember I, Lancet I, Rivet I, Scatter I, Ember II, Lancet II, Rivet II, Scatter II, Ember III, Lancet III, Rivet III, Scatter III | 12 |
| **Extras** | Repair Drone I, Repair Drone II, Repair Drone III, EMP Charge, Repair Drone IV, Cloaking CPU S, Base CPU I, Cloaking CPU M, Auto-Repair CPU, Cloaking CPU L, Base CPU II | 11 |
| **Recursos** | Cataclysite (em lotes de 100), Ship Fragment (em lotes de 100), Daraxium (em lotes de 100), Nyxite (em lotes de 100), Quorvium (em lotes de 10), Reinforced Hull Plate (em lotes de 10), Power Core, Velkonite Reinforced Plate, Dark Matter, Orvium Reinforced Plate | 10 |

<!-- market-kinds:end -->

Naves, drones, formações de drones, boosters e assinaturas nunca podem ser vendidos, nem a Ancient Control Unit, os minérios Velkonite e Orvium, a Dark Matter Plate, a Jump CPU, as Extra Slots CPUs, a N.U.K.E. e a N.I.K.E. As Dark Matter Plates não estão no Leilão de forma alguma, nem como mercadoria nem como preço. Um item equipado, encaixado em outro item, com módulos dentro ou no [Cache de Transporte](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) não pode ser anunciado, nem uma Cloaking CPU, uma EMP Charge ou uma Base CPU que já foi usada. Munição e foguetes são vendidos da estação: pouse a nave primeiro.

## Vender {#selling}

Toque em **Vender um item** (ou no martelo do Hangar), escolha o que você ganhou (um menu de categorias reduz a lista, com as mesmas categorias do Mercado), escolha créditos ou Thulium, defina o preço de um lote e quanto tempo o anúncio dura: 1, 3 ou 7 dias. A folha mostra o preço mínimo, três chips que preenchem um preço (**Mínimo**; **Venda rápida**, um abaixo do anúncio mais barato no momento; e **Justo**, o preço da última venda) e o depósito, o imposto e o que você recebe, antes de anunciar. Abaixo do preço, **Anúncios parecidos** mostra num gráfico por quais preços o mesmo item, com o mesmo encantamento, está anunciado agora, na moeda que você escolheu: o seu preço é uma linha nele, o preço mínimo, a última venda e o preço da Loja ficam marcados, uma linha em palavras diz onde o seu preço ficaria e os três anúncios mais baratos aparecem em seguida. Uma peça é um lote de um; munição e alguns recursos são vendidos em lotes de 10 ou 100, e você vende um número inteiro de lotes. O que você anuncia sai do seu inventário e fica guardado pelo servidor até vender, você cancelar ou expirar; depois volta, com a sua etiqueta. Você pode cancelar a qualquer momento, até nos últimos dias de uma temporada. Um anúncio é uma foto do momento: para mudar um preço, cancele o anúncio e anuncie de novo (o depósito é pago outra vez).

Todo item tem um **preço mínimo** e **não existe preço máximo**: peça o que quiser. A tabela mostra o preço mínimo de alguns itens.

<!-- market-bands:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Item | Vendido em lotes de | Preço mínimo, créditos | Preço mínimo, Thulium |
| :--- | ---: | ---: | ---: |
| Quantum Laser II | 1 | 32.000 | 32 |
| Quantum Laser III | 1 | 170.000 | 170 |
| Helios Beam | 1 | 1.600.000 | 1.600 |
| Absorption Shield Cell IV | 1 | 1.100.000 | 1.100 |
| Heavy Shield Core | 1 | 870.000 | 870 |
| Impulse Thruster IV | 1 | 980.000 | 980 |
| EMP Charge | 1 | 40.000 | 40 |
| Cloaking CPU S | 1 | 400.000 | 400 |
| Ultra Core | 10 | 800 | 1 |
| Lancet I | 1 | 200 | 1 |
| Ship Fragment | 100 | 600 | 1 |
| Dark Matter | 1 | 33.000 | 33 |

<!-- market-bands:end -->

Um preço em Thulium segue uma única regra: o preço mínimo em créditos dividido pela taxa, arredondado para cima. A taxa não é um valor que o jogo dá ao Thulium. Ela só diz como se calcula o preço mínimo em Thulium, e por isso um anúncio em Thulium pode ser barato para um piloto que tem Thulium. A maioria dos vendedores vai pedir créditos. Todo item, menos o **Quorvium**, pode ter preço em Thulium, também os baratos (munição, foguetes, recursos comuns): o preço mínimo deles é então 1 Thulium, o menor passo. Só o Quorvium fica apenas em créditos, porque 1 Thulium valeria mais do que um lote dele.

Os seus **anúncios abertos** (e um anúncio que um admin deixou em espera) ocupam vagas. Ao subir de nível você ganha mais vagas, até um máximo, e pode vender e comprar mais por dia. Quanto tempo um anúncio pode durar é igual em todos os níveis.

<!-- market-limits:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Nível | Anúncios abertos | Maior duração | Por dia, créditos | Por dia, Thulium | Depósito por 24 h |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 5 | 20 | 168 h | 4.500.000 | 22.500 | 1% |
| 6 | 40 | 168 h | 6.000.000 | 30.000 | 1% |
| 7 | 70 | 168 h | 7.500.000 | 37.500 | 1% |
| 8 | 100 | 168 h | 8.500.000 | 42.500 | 1% |
| 9 | 100 | 168 h | 10.000.000 | 50.000 | 1% |
| 10 | 100 | 168 h | 15.000.000 | 75.000 | 1,5% |
| 11 | 100 | 168 h | 15.000.000 | 75.000 | 1,5% |
| 12 | 100 | 168 h | 15.000.000 | 75.000 | 1,5% |
| 13 | 100 | 168 h | 20.000.000 | 100.000 | 1,5% |
| 14 | 100 | 168 h | 20.000.000 | 100.000 | 1,5% |
| 15 | 100 | 168 h | 20.000.000 | 100.000 | 1,5% |
| 16 | 100 | 168 h | 20.000.000 | 100.000 | 1,5% |
| 17 | 100 | 168 h | 20.000.000 | 100.000 | 1,5% |
| 18 | 100 | 168 h | 20.000.000 | 100.000 | 1,5% |
| 19 | 100 | 168 h | 20.000.000 | 100.000 | 1,5% |
| 20 ou mais | 100 | 168 h | 20.000.000 | 100.000 | 1,5% |

<!-- market-limits:end -->

## Taxas {#fees}

Um anúncio custa um **depósito**, pago ao anunciar e nunca devolvido, e uma venda custa um **imposto**, descontado do que o vendedor recebe. Os dois são pagos na moeda do anúncio e **queimados**: não vão para ninguém, então ninguém lucra negociando consigo mesmo. Nos dois últimos dias de uma temporada não há depósito nem imposto.

<!-- market-fees:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Anúncio | Preço | Depósito | Imposto | O vendedor recebe |
| :--- | ---: | ---: | ---: | ---: |
| Quantum Laser III: nível 6, 24 h | 170.000 créditos | 1.700 créditos | 8.500 créditos | 161.500 créditos |
| Quantum Laser III: nível 10, 72 h | 170 Thulium | 8 Thulium | 8 Thulium | 162 Thulium |
| Helios Beam: nível 12, 168 h | 2.500.000 créditos | 262.500 créditos | 125.000 créditos | 2.375.000 créditos |
| Helios Beam: nível 12, 168 h, nos últimos dias de uma temporada | 2.500.000 créditos | 0 créditos | 0 créditos | 2.500.000 créditos |

<!-- market-fees:end -->

## Comprar {#buying}

O **Mercado** mostra o que outros pilotos vendem. Reduza a lista com os **chips de categoria** (um para cada tipo de item, com o número de anúncios que ele tem), procure pelo nome, filtre por encantamento e moeda, e ordene por preço, pelo que termina primeiro ou pelo mais novo. Escolha um anúncio para ver o que é, quem vende, quanto tempo dura e como o preço se compara com a última venda, com o menor preço no momento e com o preço da Loja. Uma pilha é comprada em lotes inteiros. Uma compra grande pede mais uma confirmação. O vendedor é pago na hora, menos o imposto; você não paga depósito nem imposto. O que você compra **não é vendável**: a página diz “Você recebe: não negociável” ao lado de **Comprar por …**, porque só pode ser vendido o que você ganha. Você não pode comprar o seu próprio anúncio. Um anúncio que é vendido enquanto você olha diz “Esse anúncio não existe mais.”

## Limites {#limits}

Cada moeda tem o seu próprio limite diário do que você pode vender e do que pode comprar, contado nas últimas 24 horas, e um limite do que passa entre dois pilotos, para que uma segunda conta não seja um jeito rápido de mover uma fortuna. Créditos e Thulium nunca são somados: quem vende por Thulium usa o seu limite de Thulium e mais nada. A folha de venda avisa quando uma venda passaria do seu limite diário de venda, e quando uma compra passaria do seu limite diário de compra, o Mercado avisa e deixa **Comprar por …** desativado. Os limites crescem com o nível, e o Premium não muda nenhum. O que você vence nos Lotes não conta.

Os foguetes de um anúncio, de um lote que você lidera e do seu porão contam todos para o máximo de um foguete que você pode levar: um anúncio não serve para levar mais do que a pilha da Loja permite.

## Meus anúncios e Histórico {#my-listings-and-history}

**Meus anúncios** mostra as suas vagas e cada anúncio com o seu estado (aberto, vendido, cancelado, expirado, devolvido ou em espera), um botão **Cancelar**, **Anunciar de novo** para um encerrado e um chip **Superado** quando outro anúncio do mesmo item pede menos. Um anúncio que expirou volta sozinho para o seu inventário. O **Histórico** começa com as suas negociações dos últimos 30 dias: as suas vendas e compras, o que você recebeu e gastou, as taxas e os impostos que pagou, o seu resultado líquido, a sua melhor venda, a sua venda média e o item que você mais negociou, mais dois gráficos de linha: os seus ganhos por dia e o seu resultado até agora (em créditos ou em Thulium, um de cada vez). Abaixo fica a lista do que você vendeu, comprou e venceu, com o imposto. O jogo guarda o livro-razão do Leilão por 90 dias.

Você é avisado quando algo é vendido: por um aviso, pelo som do Leilão e pelo novo saldo, e por um selo na entrada do Leilão enquanto a página está fechada. Uma sequência de vendas é um aviso só. O Leilão tem sons discretos só dele, um para cada coisa que você faz ou que acontece com você ali (anunciar, encerrar, uma venda, um lance, ser superado, vencer), e eles seguem o volume da interface.

## Os Lotes de cada hora {#the-hourly-lots}

Os Lotes são as ofertas do próprio jogo: munição, foguetes e EMP Charges, a cada hora, para dar lances. São um jeito de comprar munição por menos do que a Loja pede, e um ralo: o lance vencedor é queimado. Só abrem os lotes da tabela do dia abaixo (nunca munição x1 ou x4, nunca Siphon Batteries, nunca um foguete especial), na moeda da Loja. Um lote de foguetes nunca passa do máximo desse foguete que você pode levar (a pilha da Loja), então um lance que faria você passar dele é recusado: dê lances num lote de foguetes quando você levar poucos desse foguete.

<!-- market-lots:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- No início de cada hora UTC abre um novo lote, que fica aberto por 4 horas, de modo que 4 ficam abertos ao mesmo tempo.
- O lance inicial é de 40% do preço da Loja da mercadoria. Cada lance seguinte precisa superar o mais alto em pelo menos 5%, e em pelo menos 100 créditos ou 1 Thulium.
- O seu lance é pago na hora e fica retido. Se alguém cobrir, ele volta para você na hora.
- Um lance nos últimos 2 min de um lote move o fim dele para 2 min depois do lance, no máximo 5 vezes.
- O que você vence é para voar, não para negociar: nunca é vendável. O lance vencedor é queimado. Um lote em que ninguém dá lance não é vendido e não custa nada a ninguém.
- O tamanho de um lote segue os pilotos de nível 5 ou mais que olharam o leilão nos últimos 3 dias: com nenhum, é 10% do tamanho da tabela; com 30 ou mais, o tamanho completo, em passos de 500 para munição, 50 para foguetes e 1 para EMP Charges.
- Nas últimas 6 horas de uma temporada, nenhum lote é criado. O reset cancela os lotes que ainda estão abertos, e todo lance é devolvido.

<!-- market-lots:end -->

<!-- market-day:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Hora UTC | Lote | Tamanho completo | Pago em | Lance inicial no tamanho completo |
| :--- | :--- | ---: | :--- | ---: |
| 00:00 | Scatter III | 1.250 | Thulium | 2.500 Thulium |
| 01:00 | Advanced Plasma | 25.000 | Thulium | 5.000 Thulium |
| 02:00 | Lancet I | 12.500 | Créditos | 2.500.000 créditos |
| 03:00 | EMP Charge | 5 | Thulium | 1.000 Thulium |
| 04:00 | Ultra Core | 25.000 | Thulium | 10.000 Thulium |
| 05:00 | Rivet II | 5.000 | Créditos | 1.600.000 créditos |
| 06:00 | Advanced Plasma | 10.000 | Thulium | 2.000 Thulium |
| 07:00 | Advanced Plasma | 50.000 | Thulium | 10.000 Thulium |
| 08:00 | Ember I | 12.500 | Créditos | 2.500.000 créditos |
| 09:00 | Ultra Core | 50.000 | Thulium | 20.000 Thulium |
| 10:00 | Scatter II | 5.000 | Créditos | 1.600.000 créditos |
| 11:00 | EMP Charge | 5 | Thulium | 1.000 Thulium |
| 12:00 | Advanced Plasma | 50.000 | Thulium | 10.000 Thulium |
| 13:00 | Lancet III | 1.250 | Thulium | 2.500 Thulium |
| 14:00 | Ultra Core | 10.000 | Thulium | 4.000 Thulium |
| 15:00 | Advanced Plasma | 25.000 | Thulium | 5.000 Thulium |
| 16:00 | Ultra Core | 50.000 | Thulium | 20.000 Thulium |
| 17:00 | Rivet I | 12.500 | Créditos | 2.500.000 créditos |
| 18:00 | Advanced Plasma | 50.000 | Thulium | 10.000 Thulium |
| 19:00 | Ember II | 5.000 | Créditos | 1.600.000 créditos |
| 20:00 | Ultra Core | 25.000 | Thulium | 10.000 Thulium |
| 21:00 | Advanced Plasma | 25.000 | Thulium | 5.000 Thulium |
| 22:00 | Advanced Plasma | 10.000 | Thulium | 2.000 Thulium |
| 23:00 | EMP Charge | 5 | Thulium | 1.000 Thulium |

<!-- market-day:end -->

Quando poucos pilotos usam o Leilão, os lotes são pequenos, para que um punhado de pilotos não receba milhares de tiros a cada hora; eles crescem conforme mais pilotos olham.

## A temporada e o reset {#the-season-and-the-wipe}

O Leilão segue a temporada (veja a [Linha do tempo do reset](/wiki/03-Mechanics/Wipe-Timeline.md)). Nos dois últimos dias não há taxas. A partir do dia 30, quando a contagem regressiva de cinco minutos do reset começa, ele fica fechado: nada é anunciado, comprado ou disputado com lances, um lote que termina então é cancelado e o lance devolvido, e você ainda pode cancelar os seus próprios anúncios. Um anúncio nunca dura além do fim da temporada.

No reset, **todo anúncio aberto volta para o vendedor** como itens soltos, e o reset então apaga os itens soltos como quaisquer outros (só fica o que você põe no [Cache de Transporte](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-)): então venda, ou cancele e ponha no Cache o que você quer guardar. Os lotes ainda abertos são cancelados e os lances devolvidos. Créditos e Thulium não são zerados.

## O que o Leilão não dá a você {#what-the-auction-does-not-give-you}

O Leilão serve para negociar o que você ganha, e é honesto sobre os seus limites.

- **Vender drops não é grind.** Os drops brutos de alienígenas são só recursos e valem de 0,4 a 0,9 por cento do que a mesma hora de caça no nível 5 paga em abates. O que o Mercado dá a um piloto novo é o equipamento que as missões dele pagam e de que ele não precisa (uma vez), os recursos das missões de Desafio, as caixas dos chefes de enxame e o que ele cria.
- **Não há comerciante.** Ordens de compra, em que um piloto diz o que quer comprar e por quanto, não estão nesta versão. Até lá, os únicos comerciantes são o artesão, que compra materiais, cria equipamento na Montagem e o vende, e o piloto armazenador, que guarda estoque no Cache de Transporte durante o reset.
- **O equipamento da Loja não é para revenda.** O equipamento que você comprou na Loja não pode ser vendido de novo: isso inclui a Quantum Laser I e II, o Light e o Basic Shield Core, Engine I e II, o primeiro grau de células e propulsores, os amps que a Loja vende e a munição comprada. A única Quantum Laser II vendável de um piloto é a que uma missão paga uma vez.
- **As placas vêm de missões.** As Velkonite e Orvium Reinforced Plates do Mercado são as que as missões de Desafio pagam. As placas da Forja ficam de fora; senão seriam a maior mercadoria do Mercado.

Se um anúncio parecer errado, avise do jeito de sempre: os administradores do jogo podem deixar um anúncio em espera, devolvê-lo, pausar o Leilão ou banir um piloto dele, e toda ação assim é registrada.
