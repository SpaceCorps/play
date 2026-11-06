<!-- wiki-i18n source: c21ae6d189180cd7 -->
<!-- wiki-i18n title: Enxame Phantasm -->
# Enxame Phantasm {#phantasm-swarm}

O enxame Phantasm é um **Boss Phantasm** com seus **Phantasm Guards**: um [Phantasm](/wiki/04-Aliens/Phantasm.md) enorme que nunca começa uma luta, e outros menores que ficam perto dele e o curam. Vive nos setores externos das corporações, `x-3` e `x-4`, e é uma luta para um grupo de pilotos de nível médio.

## Resumo rápido {#at-a-glance}

<!-- phantasm-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Onde**: Os setores `x-3` e `x-4` de cada corporação
- **Quantos**: Um em cada um desses setores, 6 em cada mundo
- **Aparece**: Do dia 4 da temporada até o reset (Beta e Gamma: do dia 1 da temporada)
- **Líder**: Boss Phantasm
- **Seguidores**: Até 4 × Phantasm Guard, um novo a cada 10 s
- **Os seguidores ficam a**: até 500 unidades do líder
- **Cura**: Cada Phantasm Guard a até 600 unidades do líder cura o casco dele, 30 HP por segundo em Alpha
- **Líder destruído**: Os seguidores vão embora 30 s depois que o líder é destruído, a menos que estejam atacando
- **Volta**: 2 min depois que o líder é destruído, no mesmo setor
- **Avisos**: Os pilotos do setor são avisados quando o líder aparece e quando é destruído. São linhas do Sistema: aparecem na aba **Sistema** do chat, com uma contagem de linhas não lidas, e não em **Global** nem em **Local**. O registro de baixas nomeia o piloto a quem o abate é creditado.

<!-- phantasm-glance:end -->

## Os membros {#the-members}

- **Boss Phantasm**: um Phantasm maior, com a tonalidade do enxame e o nome por cima, com casco, escudo e salva de laser próprios (os números estão abaixo). É passivo: vagueia até um piloto acertá-lo, então vai atrás desse piloto e atira nele, e as naves do seu enxame que estão perto entram na luta. O alcance da arma e a velocidade são os de um Phantasm, e ele nunca conserta o próprio casco.
- **Phantasm Guard**: um Phantasm menor com a tonalidade do enxame. Os Guards ficam perto do chefe, entram na luta quando uma nave de enxame perto deles é acertada, e cada um que está perto do chefe cura o casco dele. Um Guard conserta o próprio casco depois de um descanso, como um Phantasm faz.

## Como a luta transcorre {#how-the-fight-goes}

- **Leve um grupo.** Três pilotos de nível 4–5 com munição x2 o destroem em cerca de um minuto e meio em Alpha, perdendo no máximo uma nave; um piloto desse nível sozinho é destruído, e dois também. Naves melhores e munição x4 o deixam bem mais rápido.
- **Atire no chefe, não nos Guards.** Um Guard cai em segundos, mas um novo chega na frequência que a lista *Resumo rápido* diz, e o que os Guards curam é uma parte pequena do que um grupo causa: deixá-los em paz custa um pouco de tempo, caçá-los custa mais.
- **Beta e Gamma são mais duros.** Os enxames desses mundos são mais fortes ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)), então pedem mais pilotos ou munição melhor.
- **Fique de olho no setor.** `x-4` é um setor PvP em Alpha, e `x-3` e `x-4` são em Beta e Gamma ([Mundos](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): um rival pode entrar na luta ou esperar a caixa. Deixe uma nave do grupo de vigia.
- **O chefe volta** depois do tempo da lista *Resumo rápido*, com a força toda, no mesmo setor, e seus Guards chegam um depois do outro.

## Recompensas e saque {#rewards-and-drops}

O Boss Phantasm paga pela luta que ele é: um minuto de luta contra ele paga mais do que um minuto contra um Goombah, o alienígena mais bem pago desses setores. O pagamento é dividido pelo dano entre os pilotos que lutaram contra ele ([como o abate de um chefe paga](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). A caixa dele é do piloto que mais causou dano e contém o saque de um Phantasm muitas vezes (Ship Fragments, Daraxium e Nyxite), com munição e foguetes. Os Guards pagam pouco e não largam nada; abatê-los não é farm, porque eles voltam com o chefe.

## Os números {#the-numbers}

Os números das naves do enxame nos três mundos ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- phantasm-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Phantasm

Base: Phantasm, com 2.000% do casco e 300% do dano dos lasers; a velocidade e o alcance são os da nave de origem.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 40.000 | 60.000 | 80.000 |
| Escudo | 64.000 | 96.000 | 128.000 |
| Dano dos lasers (uma salva por segundo) | 1.050 | 1.575 | 2.100 |
| Velocidade | 160 | 160 | 160 |
| Alcance dos lasers | 700 | 700 | 700 |
| Raio de agressão | só quando atacado | só quando atacado | só quando atacado |
| Créditos | 39.000 | 78.000 | 117.000 |
| Thulium | 195 | 390 | 585 |
| Experiência (XP) | 7.800 | 15.600 | 23.400 |
| Honra | 62 | 124 | 186 |
| Pontos PvE por abate | 8 | 8 | 8 |

**Saque**: uma caixa, para o piloto que mais causou dano.

| Item | Chance | Quantidade |
| :--- | ---: | ---: |
| Ship Fragment | 100% em cada uma de 13 rolagens | 1 |
| Daraxium | 60% em cada uma de 13 rolagens | 1–2 |
| Nyxite | 60% em cada uma de 13 rolagens | 1–2 |
| Standard Battery | 100% | 600–1.200 |
| Advanced Plasma | 100% | 60–100 |
| Ultra Core | 100% | 10–20 |
| Um dos 8 [foguetes](/wiki/06-Items/Rockets.md) comprados com créditos, escolhido ao acaso | 100% | 4–6 |

### Phantasm Guard

Base: Phantasm, com 50% de casco, escudo e dano; a velocidade e o alcance são os da nave de origem.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 1.000 | 1.500 | 2.000 |
| Escudo | 1.600 | 2.400 | 3.200 |
| Dano dos lasers (uma salva por segundo) | 175 | 263 | 350 |
| Velocidade | 160 | 160 | 160 |
| Alcance dos lasers | 700 | 700 | 700 |
| Raio de agressão | só quando atacado | só quando atacado | só quando atacado |
| Cura o líder, cada um, por segundo (só o casco) | 30 | 45 | 60 |
| Créditos | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Experiência (XP) | 12 | 24 | 36 |
| Honra | 1 | 2 | 3 |
| Pontos PvE por abate | 1 | 1 | 1 |

**Saque**: nenhum. O abate paga só os seus créditos, Thulium, XP e honra.

<!-- phantasm-members:end -->
