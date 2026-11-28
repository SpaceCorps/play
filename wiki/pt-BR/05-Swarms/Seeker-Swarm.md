<!-- wiki-i18n source: 7c6bc3eaf70223f5 -->
<!-- wiki-i18n title: Enxame Seeker -->
# Enxame Seeker {#seeker-swarm}

O enxame Seeker é o menor dos [enxames](/wiki/05-Swarms/Swarms.md): um **Boss Seeker** e os **Seeker Slaves** que o protegem e o curam. Vive nos setores onde os pilotos novos começam a voar, por isso é o primeiro enxame que a maioria encontra. O Boss Seeker nunca começa uma luta, mas, assim que você atira nele, é muito mais perigoso do que o [Seeker](/wiki/04-Aliens/Seeker.md) em que se baseia.

## Resumo rápido {#at-a-glance}

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Onde**: Os setores `x-1` e `x-2` de cada corporação
- **Quantos**: Um em cada um desses setores, 6 em cada mundo
- **Aparece**: Do dia 4 da temporada até o reset (Beta e Gamma: do dia 1 da temporada)
- **Líder**: Boss Seeker
- **Seguidores**: Até 4 × Seeker Slave, um novo a cada 10 s
- **Os seguidores ficam a**: até 500 unidades do líder
- **Cura**: Cada Seeker Slave a até 600 unidades do líder cura o casco dele, 50 HP por segundo em Alpha
- **Líder destruído**: Os seguidores vão embora 30 s depois que o líder é destruído, a menos que estejam atacando
- **Volta**: {{guide:vitals.respawn@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} depois que o líder é destruído, no mesmo setor
- **Avisos**: Os pilotos do setor são avisados quando o líder aparece e quando é destruído. São linhas do Sistema: aparecem na aba **Sistema** do chat, com uma contagem de linhas não lidas, e não em **Global** nem em **Local**. O registro de baixas nomeia o piloto a quem o abate é creditado.

<!-- seeker-glance:end -->

## Os membros {#the-members}

- **Boss Seeker**: um Seeker bem maior, com a tonalidade do enxame e o nome por cima, com várias vezes o casco, o escudo e o dano de um Seeker (os números estão abaixo). É passivo: vagueia até um piloto acertá-lo, então para onde está e atira nesse piloto, e as naves do seu enxame que estão perto entram na luta. O alcance da arma e a velocidade são os de um Seeker, e ele nunca conserta o próprio casco. As suas [três etapas](#the-leaders-three-steps) e uma [habilidade especial](/wiki/03-Mechanics/Special-Abilities.md) podem mudar isso.
- **Seeker Slave**: um Seeker comum com a tonalidade do enxame. Os Slaves ficam perto do chefe, entram na luta quando uma nave de enxame perto deles é acertada, e cada um que está perto do chefe cura o casco dele. Um Slave conserta o próprio casco depois de um descanso, como um Seeker faz.

## Como a luta transcorre {#how-the-fight-goes}

- **Deixe-o em paz até a sua nave aguentar.** Um Boss Seeker bate mais forte do que a primeira nave de um piloto suporta: a Protos de um piloto novo, ainda sem escudo, é destruída em segundos assim que o chefe e seus Slaves estão sobre ela.
- **Fique fora do alcance.** O chefe e seus Slaves são mais lentos que uma Protos, e as armas deles alcançam menos que um Quantum Laser II (veja [Lasers e munição](/wiki/06-Items/Lasers.md)): um piloto que tem esses lasers e fica além do alcance deles não sofre dano enquanto eles atiram. Um piloto com Quantum Laser I não consegue ficar fora do alcance.
- **Os Slaves curam mais rápido do que um piloto novo sozinho acerta.** Juntos, eles curam mais do que os lasers de um piloto causam com munição x1, então leve um parceiro e munição x2. Dois pilotos com Quantum Laser II que mantêm a distância derrubam o chefe em cerca de um minuto em Alpha, e bem mais rápido com munição x2.
- **O chefe volta** depois do tempo da lista *Resumo rápido*, com a força toda, no mesmo setor, e seus Slaves chegam um depois do outro.

## As três etapas do líder {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

A luta tem três etapas ([como funcionam](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); cada uma acontece uma vez.

- **No início**: Seus Seeker Slaves o reparam ×2 mais rápido por 8 s.
- **Abaixo de dois terços**: 2 cópias dele aparecem, e o verdadeiro usa um anel.
- **Abaixo de um terço**: Foge dos pilotos por 4 s e depois se volta contra eles.

<!-- mob-ladder:end -->

## Recompensas e saque {#rewards-and-drops}

O Boss Seeker paga **exatamente dez Seekers**: dez vezes os créditos, o Thulium, a XP e a honra de um Seeker, divididos pelo dano entre os pilotos que lutaram contra ele ([como o abate de um chefe paga](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). A caixa dele contém o saque de dez Seekers e, além disso, munição e foguetes abaixo de Épico, para o piloto que mais causou dano. Os Slaves pagam pouco e não largam nada; abatê-los não é farm, porque eles voltam com o chefe.

## Os números {#the-numbers}

Os números das naves do enxame nos três mundos ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker

Base: Seeker, com 400% de casco, escudo e dano; a velocidade e o alcance são os da nave de origem.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Boss Seeker#1}} | {{guide:vitals.hull@Boss Seeker#2}} | {{guide:vitals.hull@Boss Seeker#3}} |
| Escudo | {{guide:vitals.shield@Boss Seeker#1}} | {{guide:vitals.shield@Boss Seeker#2}} | {{guide:vitals.shield@Boss Seeker#3}} |
| Dano dos lasers (uma salva por segundo) | {{guide:vitals.dps@Boss Seeker#1}} | {{guide:vitals.dps@Boss Seeker#2}} | {{guide:vitals.dps@Boss Seeker#3}} |
| Velocidade | {{guide:vitals.speed@Boss Seeker#1}} | {{guide:vitals.speed@Boss Seeker#2}} | {{guide:vitals.speed@Boss Seeker#3}} |
| Alcance dos lasers | 600 | 600 | 600 |
| Raio de agressão | só quando atacado | só quando atacado | só quando atacado |
| Créditos | {{guide:spoils.pay.credits@Boss Seeker#1}} | {{guide:spoils.pay.credits@Boss Seeker#2}} | {{guide:spoils.pay.credits@Boss Seeker#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Seeker#1}} | {{guide:spoils.pay.thulium@Boss Seeker#2}} | {{guide:spoils.pay.thulium@Boss Seeker#3}} |
| Experiência (XP) | {{guide:spoils.pay.experience@Boss Seeker#1}} | {{guide:spoils.pay.experience@Boss Seeker#2}} | {{guide:spoils.pay.experience@Boss Seeker#3}} |
| Honra | {{guide:spoils.pay.honor@Boss Seeker#1}} | {{guide:spoils.pay.honor@Boss Seeker#2}} | {{guide:spoils.pay.honor@Boss Seeker#3}} |
| Pontos PvE por abate | 5 | 5 | 5 |

**Saque**: uma caixa, para o piloto que mais causou dano.

| Item |
| :--- |
| {{guide:spoils.box@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} |

### Seeker Slave

Base: Seeker, com 100% de casco, escudo e dano; a velocidade e o alcance são os da nave de origem.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Seeker Slave#1}} | {{guide:vitals.hull@Seeker Slave#2}} | {{guide:vitals.hull@Seeker Slave#3}} |
| Escudo | {{guide:vitals.shield@Seeker Slave#1}} | {{guide:vitals.shield@Seeker Slave#2}} | {{guide:vitals.shield@Seeker Slave#3}} |
| Dano dos lasers (uma salva por segundo) | {{guide:vitals.dps@Seeker Slave#1}} | {{guide:vitals.dps@Seeker Slave#2}} | {{guide:vitals.dps@Seeker Slave#3}} |
| Velocidade | {{guide:vitals.speed@Seeker Slave#1}} | {{guide:vitals.speed@Seeker Slave#2}} | {{guide:vitals.speed@Seeker Slave#3}} |
| Alcance dos lasers | 600 | 600 | 600 |
| Raio de agressão | só quando atacado | só quando atacado | só quando atacado |
| Cura o líder, cada um, por segundo (só o casco) | 50 | 75 | 100 |
| Créditos | {{guide:spoils.pay.credits@Seeker Slave#1}} | {{guide:spoils.pay.credits@Seeker Slave#2}} | {{guide:spoils.pay.credits@Seeker Slave#3}} |
| Thulium | {{guide:spoils.pay.thulium@Seeker Slave#1}} | {{guide:spoils.pay.thulium@Seeker Slave#2}} | {{guide:spoils.pay.thulium@Seeker Slave#3}} |
| Experiência (XP) | {{guide:spoils.pay.experience@Seeker Slave#1}} | {{guide:spoils.pay.experience@Seeker Slave#2}} | {{guide:spoils.pay.experience@Seeker Slave#3}} |
| Honra | {{guide:spoils.pay.honor@Seeker Slave#1}} | {{guide:spoils.pay.honor@Seeker Slave#2}} | {{guide:spoils.pay.honor@Seeker Slave#3}} |
| Pontos PvE por abate | 1 | 1 | 1 |

**Saque**: nenhum. O abate paga só os seus créditos, Thulium, XP e honra.

<!-- seeker-members:end -->
