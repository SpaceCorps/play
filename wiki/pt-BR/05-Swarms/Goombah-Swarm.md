<!-- wiki-i18n source: 7859e3f6a7efac1e -->
<!-- wiki-i18n title: Enxame Goombah -->
# Enxame Goombah {#goombah-swarm}

O enxame Goombah é um **Boss Goombah** com seus **Goombah Guards**: um [Goombah](/wiki/04-Aliens/Goombah.md) gigantesco que nunca começa uma luta, e outros menores que ficam perto dele e o curam. Vive nos mesmos setores que o [enxame Phantasm](/wiki/05-Swarms/Phantasm-Swarm.md), `x-3` e `x-4`, e é uma luta para um grupo dos pilotos mais fortes dos setores das corporações.

## Resumo rápido {#at-a-glance}

<!-- goombah-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Onde**: Os setores `x-3` e `x-4` de cada corporação
- **Quantos**: Um em cada um desses setores, 6 em cada mundo
- **Aparece**: Do dia 4 da temporada até o reset (Beta e Gamma: do dia 1 da temporada)
- **Líder**: Boss Goombah
- **Seguidores**: Até 4 × Goombah Guard, um novo a cada 10 s
- **Os seguidores ficam a**: até 500 unidades do líder
- **Cura**: Cada Goombah Guard a até 600 unidades do líder cura o casco dele, 110 HP por segundo em Alpha
- **Líder destruído**: Os seguidores vão embora 30 s depois que o líder é destruído, a menos que estejam atacando
- **Volta**: 5 min depois que o líder é destruído, no mesmo setor
- **Avisos**: Os pilotos do setor são avisados quando o líder aparece e quando é destruído. São linhas do Sistema: aparecem na aba **Sistema** do chat, com uma contagem de linhas não lidas, e não em **Global** nem em **Local**. O registro de baixas nomeia o piloto a quem o abate é creditado.

<!-- goombah-glance:end -->

## Os membros {#the-members}

- **Boss Goombah**: um Goombah maior, com a tonalidade do enxame e o nome por cima, com casco, escudo e salva de laser próprios (os números estão abaixo). É passivo: vagueia até um piloto acertá-lo, então vai atrás desse piloto e atira nele, e as naves do seu enxame que estão perto entram na luta. O alcance da arma e a velocidade são os de um Goombah, e ele nunca conserta o próprio casco.
- **Goombah Guard**: um Goombah menor com a tonalidade do enxame. Os Guards ficam perto do chefe, entram na luta quando uma nave de enxame perto deles é acertada, e cada um que está perto do chefe cura o casco dele. Um Guard conserta o próprio casco depois de um descanso, como um Goombah faz.

## Como a luta transcorre {#how-the-fight-goes}

- **Leve um grupo das naves mais fortes.** Três pilotos de nível 8 com munição x2 o destroem em cerca de 75 segundos em Alpha, perdendo no máximo uma nave; dois deles precisam de munição x4, e pilotos de níveis mais baixos não causam dano suficiente para vencer.
- **Atire no chefe, não nos Guards.** Um Guard cai em segundos, mas um novo chega na frequência que a lista *Resumo rápido* diz, e o que os Guards curam é uma parte pequena do que um grupo causa: deixá-los em paz custa um pouco de tempo, caçá-los custa mais.
- **Beta e Gamma são mais duros.** Os enxames desses mundos são mais fortes ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)), então pedem mais pilotos ou munição melhor.
- **Fique de olho no setor.** `x-4` é um setor PvP em Alpha, e `x-3` e `x-4` são em Beta e Gamma ([Mundos](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): um rival pode entrar na luta ou esperar a caixa. Deixe uma nave do grupo de vigia.
- **O chefe volta** depois do tempo da lista *Resumo rápido*, com a força toda, no mesmo setor, e seus Guards chegam um depois do outro.

## Recompensas e saque {#rewards-and-drops}

O Boss Goombah paga pela luta que ele é: um minuto de luta contra ele paga mais do que um minuto contra um Goombah, o alienígena mais bem pago desses setores. O pagamento é dividido pelo dano entre os pilotos que lutaram contra ele ([como o abate de um chefe paga](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). A caixa dele é do piloto que mais causou dano e contém o saque de um Goombah várias vezes (Cataclysite, Quorvium, Power Cores, Reinforced Hull Plates e Ship Fragments), com munição e foguetes. Os Guards pagam pouco e não largam nada; abatê-los não é farm, porque eles voltam com o chefe.

## Os números {#the-numbers}

Os números das naves do enxame nos três mundos ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- goombah-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Goombah

Base: Goombah, com 400% do casco e 100% do dano dos lasers; a velocidade e o alcance são os da nave de origem.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 128.000 | 192.000 | 256.000 |
| Escudo | 192.000 | 288.000 | 384.000 |
| Dano dos lasers (uma salva por segundo) | 3.000 | 4.500 | 6.000 |
| Velocidade | 180 | 180 | 180 |
| Alcance dos lasers | 800 | 800 | 800 |
| Raio de agressão | só quando atacado | só quando atacado | só quando atacado |
| Créditos | 120.000 | 240.000 | 360.000 |
| Thulium | 600 | 1.200 | 1.800 |
| Experiência (XP) | 24.000 | 48.000 | 72.000 |
| Honra | 192 | 384 | 576 |
| Pontos PvE por abate | 14 | 14 | 14 |

**Saque**: uma caixa, para o piloto que mais causou dano.

| Item | Chance | Quantidade |
| :--- | ---: | ---: |
| Ship Fragment | 100% em cada uma de 8 rolagens | 3 |
| Reinforced Hull Plate | 60% em cada uma de 8 rolagens | 1 |
| Power Core | 25% em cada uma de 8 rolagens | 1 |
| Cataclysite | 100% em cada uma de 8 rolagens | 4 |
| Quorvium | 100% em cada uma de 8 rolagens | 2–4 |
| Advanced Plasma | 100% | 100–200 |
| Ultra Core | 100% | 100–200 |
| Um dos 8 [foguetes](/wiki/06-Items/Rockets.md) comprados com créditos, escolhido ao acaso | 100% | 6–10 |

### Goombah Guard

Base: Goombah, com 20% de casco, escudo e dano; a velocidade e o alcance são os da nave de origem.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 6.400 | 9.600 | 12.800 |
| Escudo | 9.600 | 14.400 | 19.200 |
| Dano dos lasers (uma salva por segundo) | 600 | 900 | 1.200 |
| Velocidade | 180 | 180 | 180 |
| Alcance dos lasers | 800 | 800 | 800 |
| Raio de agressão | só quando atacado | só quando atacado | só quando atacado |
| Cura o líder, cada um, por segundo (só o casco) | 110 | 165 | 220 |
| Créditos | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Experiência (XP) | 12 | 24 | 36 |
| Honra | 1 | 2 | 3 |
| Pontos PvE por abate | 3 | 3 | 3 |

**Saque**: nenhum. O abate paga só os seus créditos, Thulium, XP e honra.

<!-- goombah-members:end -->
