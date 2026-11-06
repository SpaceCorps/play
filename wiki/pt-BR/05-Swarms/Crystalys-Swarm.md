<!-- wiki-i18n source: 5f873edc2b653495 -->
<!-- wiki-i18n title: Enxame Crystalys -->
# Enxame Crystalys {#crystalys-swarm}

O enxame Crystalys é um **Boss Crystalys** com seus **Crystalys Guards**: o mais resistente dos alienígenas, o [Crystalys](/wiki/04-Aliens/Crystalys.md), crescido, com guardas que ficam perto dele e o curam. Vive nos [setores de perigo](/wiki/01-General/Danger-Sectors.md) `DS-1`, `DS-2` e `DS-3`, um em cada, e nunca sai do seu setor. Os setores de perigo são setores PvP, então a luta é para um grupo grande dos pilotos mais fortes, e o chefe não é o único perigo ali.

## Resumo rápido {#at-a-glance}

<!-- crystalys-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Onde**: Os setores de perigo `DS-1`, `DS-2`, `DS-3`
- **Quantos**: Um em cada um desses setores, 3 em cada mundo
- **Aparece**: Do dia 4 da temporada até o reset (Beta e Gamma: do dia 1 da temporada)
- **Líder**: Boss Crystalys
- **Seguidores**: Até 3 × Crystalys Guard, um novo a cada 10 s
- **Os seguidores ficam a**: até 500 unidades do líder
- **Cura**: Cada Crystalys Guard a até 600 unidades do líder cura o casco dele, 250 HP por segundo em Alpha
- **Líder destruído**: Os seguidores vão embora 30 s depois que o líder é destruído, a menos que estejam atacando
- **Volta**: 30 min depois que o líder é destruído, no mesmo setor
- **Avisos**: Os pilotos do setor são avisados quando o líder aparece e quando é destruído. São linhas do Sistema: aparecem na aba **Sistema** do chat, com uma contagem de linhas não lidas, e não em **Global** nem em **Local**. O registro de baixas nomeia o piloto a quem o abate é creditado.

<!-- crystalys-glance:end -->

## Os membros {#the-members}

- **Boss Crystalys**: um Crystalys maior, com a tonalidade do enxame e o nome por cima, com casco, escudo e salva de laser próprios (os números estão abaixo). É passivo: vagueia até um piloto acertá-lo, então vai atrás desse piloto e atira nele, e as naves do seu enxame que estão perto entram na luta. O alcance da arma e a velocidade são os de um Crystalys, e ele nunca conserta o próprio casco.
- **Crystalys Guard**: um Crystalys menor com a tonalidade do enxame. Os Guards ficam perto do chefe, entram na luta quando uma nave de enxame perto deles é acertada, e cada um que está perto do chefe cura o casco dele. Um Guard conserta o próprio casco depois de um descanso, como um Crystalys faz.

## Como a luta transcorre {#how-the-fight-goes}

- **Leve um grupo grande.** Em Alpha, seis pilotos de nível 8 em Paragons com munição x2 bastam se o fogo dele se distribuir entre eles, nove se for todo em um piloto; com munição x4 são cinco e seis. Mais pilotos terminam a luta mais cedo e perdem menos naves, e um piloto sozinho é destruído.
- **Atire no chefe, não nos Guards.** Um Guard cai em segundos, mas um novo chega na frequência que a lista *Resumo rápido* diz, e o que os Guards curam é uma parte pequena do que um grupo causa: deixá-los em paz custa um pouco de tempo, caçá-los custa mais.
- **Beta e Gamma são mais duros.** Os enxames desses mundos são mais fortes ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)), então pedem mais pilotos ou munição melhor.
- **Os setores de perigo são PvP.** Um rival pode atacar o grupo no meio da luta e esperar a caixa: ela é do piloto que mais causou dano (e do clã dele) por 30 segundos, e depois de qualquer um ([Carga](/wiki/03-Mechanics/Cargo.md)). Não vá sozinho.
- **O chefe volta** depois do tempo da lista *Resumo rápido*, com a força toda, no mesmo setor, e seus Guards chegam um depois do outro.

## Recompensas e saque {#rewards-and-drops}

O Boss Crystalys paga pela luta que ele é: um minuto de luta contra ele paga mais do que um minuto contra um Crystalys, o alienígena mais bem pago. O pagamento é dividido pelo dano entre os pilotos que lutaram contra ele ([como o abate de um chefe paga](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). A caixa dele é do piloto que mais causou dano e contém Cataclysite e Quorvium, de vez em quando um Power Core, uma Ancient Control Unit ou Dark Matter, munição x3 e x4 e foguetes Épicos. Os Guards pagam pouco e não largam nada; abatê-los não é farm, porque eles voltam com o chefe.

## Os números {#the-numbers}

Os números das naves do enxame nos três mundos ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- crystalys-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Crystalys

Base: Crystalys, com 350% do casco e 100% do dano dos lasers; a velocidade e o alcance são os da nave de origem.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 896.000 | 1.344.000 | 1.792.000 |
| Escudo | 560.000 | 840.000 | 1.120.000 |
| Dano dos lasers (uma salva por segundo) | 10.000 | 15.000 | 20.000 |
| Velocidade | 230 | 230 | 230 |
| Alcance dos lasers | 900 | 900 | 900 |
| Raio de agressão | só quando atacado | só quando atacado | só quando atacado |
| Créditos | 393.750 | 787.500 | 1.181.250 |
| Thulium | 1.050 | 2.100 | 3.150 |
| Experiência (XP) | 63.000 | 126.000 | 189.000 |
| Honra | 273 | 546 | 819 |
| Pontos PvE por abate | 30 | 30 | 30 |

**Saque**: uma caixa, para o piloto que mais causou dano.

| Item | Chance | Quantidade |
| :--- | ---: | ---: |
| Cataclysite | 100% em cada uma de 2 rolagens | 8 |
| Quorvium | 100% em cada uma de 2 rolagens | 6–10 |
| Power Core | 30% | 1 |
| Ancient Control Unit | 15% | 1 |
| Dark Matter | 4% | 1 |
| Ultra Core e Experimental Fusion Core, divididos igualmente | 100% | 600–1.000 no total |
| Um dos 4 [foguetes](/wiki/06-Items/Rockets.md) Épicos, escolhido ao acaso | 100% | 8–15 |

### Crystalys Guard

Base: Crystalys, com 15% de casco, escudo e dano; a velocidade e o alcance são os da nave de origem.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 38.400 | 57.600 | 76.800 |
| Escudo | 24.000 | 36.000 | 48.000 |
| Dano dos lasers (uma salva por segundo) | 1.500 | 2.250 | 3.000 |
| Velocidade | 230 | 230 | 230 |
| Alcance dos lasers | 900 | 900 | 900 |
| Raio de agressão | só quando atacado | só quando atacado | só quando atacado |
| Cura o líder, cada um, por segundo (só o casco) | 250 | 375 | 500 |
| Créditos | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Experiência (XP) | 12 | 24 | 36 |
| Honra | 1 | 2 | 3 |
| Pontos PvE por abate | 6 | 6 | 6 |

**Saque**: nenhum. O abate paga só os seus créditos, Thulium, XP e honra.

<!-- crystalys-members:end -->
