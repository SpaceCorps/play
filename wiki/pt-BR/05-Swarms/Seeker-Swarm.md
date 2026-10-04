<!-- wiki-i18n source: babc7a19c6dcab42 -->
<!-- wiki-i18n title: Enxame Seeker -->
# Enxame Seeker {#seeker-swarm}

O enxame Seeker é o menor dos [enxames](/wiki/05-Swarms/Swarms.md): um **Boss Seeker** e os **Seeker Slaves** que o protegem e o curam. Vive nos setores onde os pilotos novos começam a voar, por isso é o primeiro enxame que a maioria encontra. O Boss Seeker nunca começa uma luta, mas, assim que você atira nele, é muito mais perigoso do que o [Seeker](/wiki/04-Aliens/Seeker.md) em que se baseia.

## Resumo rápido {#at-a-glance}

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Onde**: Os setores `x-1` e `x-2` de cada corporação
- **Quantos**: Um em cada um desses setores, 6 em cada mundo
- **Aparece**: Do dia 4 da temporada até o reset
- **Líder**: Boss Seeker
- **Seguidores**: Até 4 × Seeker Slave, um novo a cada 10 s
- **Os seguidores ficam a**: até 500 unidades do líder
- **Cura**: Cada Seeker Slave a até 600 unidades do líder cura o casco dele, 50 HP por segundo em Alpha
- **Líder destruído**: Os seguidores vão embora 30 s depois que o líder é destruído, a menos que estejam atacando
- **Volta**: 2 min depois que o líder é destruído, no mesmo setor
- **Avisos**: Os pilotos do setor são avisados quando o líder aparece e quando é destruído. São linhas do Sistema: aparecem na aba **Sistema** do chat, com uma contagem de linhas não lidas, e não em **Global** nem em **Local**. O registro de baixas nomeia o piloto a quem o abate é creditado.

<!-- seeker-glance:end -->

## Os membros {#the-members}

- **Boss Seeker**: um Seeker bem maior, com a tonalidade do enxame e o nome por cima, com várias vezes o casco, o escudo e o dano de um Seeker (os números estão abaixo). É passivo: vagueia até um piloto acertá-lo, então para onde está e atira nesse piloto, e as naves do seu enxame que estão perto entram na luta. O alcance da arma e a velocidade são os de um Seeker, e ele nunca conserta o próprio casco.
- **Seeker Slave**: um Seeker comum com a tonalidade do enxame. Os Slaves ficam perto do chefe, entram na luta quando uma nave de enxame perto deles é acertada, e cada um que está perto do chefe cura o casco dele. Um Slave conserta o próprio casco depois de um descanso, como um Seeker faz.

## Como a luta transcorre {#how-the-fight-goes}

- **Deixe-o em paz até a sua nave aguentar.** Um Boss Seeker bate mais forte do que a primeira nave de um piloto suporta: a Protos de um piloto novo, ainda sem escudo, é destruída em segundos assim que o chefe e seus Slaves estão sobre ela.
- **Fique fora do alcance.** O chefe e seus Slaves são mais lentos que uma Protos, e as armas deles alcançam menos que um Quantum Laser 2 (veja [Lasers e munição](/wiki/06-Items/Lasers.md)): um piloto que tem esses lasers e fica além do alcance deles não sofre dano enquanto eles atiram. Um piloto com Quantum Laser 1 não consegue ficar fora do alcance.
- **Os Slaves curam mais rápido do que um piloto novo sozinho acerta.** Juntos, eles curam mais do que os lasers de um piloto causam com munição x1, então leve um parceiro e munição x2. Dois pilotos com Quantum Laser 2 que mantêm a distância derrubam o chefe em cerca de um minuto em Alpha, e bem mais rápido com munição x2.
- **O chefe volta** depois do tempo da lista *Resumo rápido*, com a força toda, no mesmo setor, e seus Slaves chegam um depois do outro.

## Recompensas e saque {#rewards-and-drops}

O Boss Seeker paga **exatamente dez Seekers**: dez vezes os créditos, o Thulium, a XP e a honra de um Seeker, divididos pelo dano entre os pilotos que lutaram contra ele ([como o abate de um chefe paga](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). A caixa dele contém o saque de dez Seekers e, além disso, munição e foguetes abaixo de Épico, para o piloto que mais causou dano. Os Slaves pagam pouco e não largam nada; abatê-los não é farm, porque eles voltam com o chefe.

## Os números {#the-numbers}

Os números das naves do enxame nos três mundos ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker {#boss-seeker}

Base: Seeker, com 400% de casco, escudo e dano; a velocidade e o alcance são os da nave de origem.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 3.200 | 4.800 | 6.400 |
| Escudo | 3.200 | 4.800 | 6.400 |
| Dano dos lasers (uma salva por segundo) | 720 | 1.080 | 1.440 |
| Velocidade | 120 | 120 | 120 |
| Alcance dos lasers | 600 | 600 | 600 |
| Raio de agressão | só quando atacado | só quando atacado | só quando atacado |
| Créditos | 10.000 | 20.000 | 30.000 |
| Thulium | 40 | 80 | 120 |
| Experiência (XP) | 1.000 | 2.000 | 3.000 |
| Honra | 20 | 40 | 60 |
| Pontos PvE por abate | 5 | 5 | 5 |

**Saque**: uma caixa, para o piloto que mais causou dano.

| Item | Chance | Quantidade |
| :--- | ---: | ---: |
| Ship Fragment | 20% em cada uma de 10 rolagens | 1 |
| Daraxium | 50% em cada uma de 10 rolagens | 1–2 |
| Standard Battery | 100% | 200–400 |
| Advanced Plasma | 100% | 10–20 |
| Ultra Core | 100% | 2–4 |
| Um dos 8 [foguetes](/wiki/06-Items/Rockets.md) comprados com créditos, escolhido ao acaso | 100% | 2–3 |

### Seeker Slave {#seeker-slave}

Base: Seeker, com 100% de casco, escudo e dano; a velocidade e o alcance são os da nave de origem.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 800 | 1.200 | 1.600 |
| Escudo | 800 | 1.200 | 1.600 |
| Dano dos lasers (uma salva por segundo) | 180 | 270 | 360 |
| Velocidade | 120 | 120 | 120 |
| Alcance dos lasers | 600 | 600 | 600 |
| Raio de agressão | só quando atacado | só quando atacado | só quando atacado |
| Cura o líder, cada um, por segundo (só o casco) | 50 | 75 | 100 |
| Créditos | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Experiência (XP) | 12 | 24 | 36 |
| Honra | 1 | 2 | 3 |
| Pontos PvE por abate | 1 | 1 | 1 |

**Saque**: nenhum. O abate paga só os seus créditos, Thulium, XP e honra.

<!-- seeker-members:end -->
