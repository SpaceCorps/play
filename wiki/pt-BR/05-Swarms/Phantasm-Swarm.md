<!-- wiki-i18n source: 2eff9c368449da99 -->
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
- **Volta**: {{guide:vitals.respawn@Boss Phantasm#1;Boss Phantasm#2;Boss Phantasm#3}} depois que o líder é destruído, no mesmo setor
- **Avisos**: Os pilotos do setor são avisados quando o líder aparece e quando é destruído. São linhas do Sistema: aparecem na aba **Sistema** do chat, com uma contagem de linhas não lidas, e não em **Global** nem em **Local**. O registro de baixas nomeia o piloto a quem o abate é creditado.

<!-- phantasm-glance:end -->

## Os membros {#the-members}

- **Boss Phantasm**: um Phantasm maior, com a tonalidade do enxame e o nome por cima, com casco, escudo e salva de laser próprios (os números estão abaixo). É passivo: vagueia até um piloto acertá-lo, então vai atrás desse piloto e atira nele, e as naves do seu enxame que estão perto entram na luta. O alcance da arma e a velocidade são os de um Phantasm, e ele nunca conserta o próprio casco. As suas [três etapas](#the-leaders-three-steps) e uma [habilidade especial](/wiki/03-Mechanics/Special-Abilities.md) podem mudar isso.
- **Phantasm Guard**: um Phantasm menor com a tonalidade do enxame. Os Guards ficam perto do chefe, entram na luta quando uma nave de enxame perto deles é acertada, e cada um que está perto do chefe cura o casco dele. Um Guard conserta o próprio casco depois de um descanso, como um Phantasm faz.

## Como a luta transcorre {#how-the-fight-goes}

- **Leve um grupo.** Três pilotos de nível 4–5 com munição x2 o destroem em cerca de um minuto e meio em Alpha, perdendo no máximo uma nave; um piloto desse nível sozinho é destruído, e dois vencem por pouco, e só enquanto os acertos são divididos. Naves melhores e munição x4 o deixam bem mais rápido.
- **Atire no chefe, não nos Guards.** Um Guard cai em segundos, mas um novo chega na frequência que a lista *Resumo rápido* diz, e o que os Guards curam é uma parte pequena do que um grupo causa: deixá-los em paz custa um pouco de tempo, caçá-los custa mais.
- **Beta e Gamma são mais duros.** Os enxames desses mundos são mais fortes ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)), então pedem mais pilotos ou munição melhor.
- **Fique de olho no setor.** `x-4` é um setor PvP em Alpha, e `x-3` e `x-4` são em Beta e Gamma ([Mundos](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): um rival pode entrar na luta ou esperar a caixa. Deixe uma nave do grupo de vigia.
- **O chefe volta** depois do tempo da lista *Resumo rápido*, com a força toda, no mesmo setor, e seus Guards chegam um depois do outro.

## As três etapas do líder {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

A luta tem três etapas ([como funcionam](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); cada uma acontece uma vez.

- **No início**: Cada um dos seus Phantasm Guards ergue uma camada de escudo de 10% do próprio casco.
- **Abaixo de dois terços**: 3 cópias dele aparecem, e o verdadeiro usa um anel.
- **Abaixo de um terço**: Salta cerca de 2.500 unidades para longe dos pilotos, e seus Phantasm Guards voltam inteiros ao redor dele.

<!-- mob-ladder:end -->

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
| Casco | {{guide:vitals.hull@Boss Phantasm#1}} | {{guide:vitals.hull@Boss Phantasm#2}} | {{guide:vitals.hull@Boss Phantasm#3}} |
| Escudo | {{guide:vitals.shield@Boss Phantasm#1}} | {{guide:vitals.shield@Boss Phantasm#2}} | {{guide:vitals.shield@Boss Phantasm#3}} |
| Dano dos lasers (uma salva por segundo) | {{guide:vitals.dps@Boss Phantasm#1}} | {{guide:vitals.dps@Boss Phantasm#2}} | {{guide:vitals.dps@Boss Phantasm#3}} |
| Velocidade | {{guide:vitals.speed@Boss Phantasm#1}} | {{guide:vitals.speed@Boss Phantasm#2}} | {{guide:vitals.speed@Boss Phantasm#3}} |
| Alcance dos lasers | 700 | 700 | 700 |
| Raio de agressão | só quando atacado | só quando atacado | só quando atacado |
| Créditos | {{guide:spoils.pay.credits@Boss Phantasm#1}} | {{guide:spoils.pay.credits@Boss Phantasm#2}} | {{guide:spoils.pay.credits@Boss Phantasm#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Phantasm#1}} | {{guide:spoils.pay.thulium@Boss Phantasm#2}} | {{guide:spoils.pay.thulium@Boss Phantasm#3}} |
| Experiência (XP) | {{guide:spoils.pay.experience@Boss Phantasm#1}} | {{guide:spoils.pay.experience@Boss Phantasm#2}} | {{guide:spoils.pay.experience@Boss Phantasm#3}} |
| Honra | {{guide:spoils.pay.honor@Boss Phantasm#1}} | {{guide:spoils.pay.honor@Boss Phantasm#2}} | {{guide:spoils.pay.honor@Boss Phantasm#3}} |
| Pontos PvE por abate | 8 | 8 | 8 |

**Saque**: uma caixa, para o piloto que mais causou dano.

| Item |
| :--- |
| {{guide:spoils.box@Boss Phantasm#1;Boss Phantasm#2;Boss Phantasm#3}} |

### Phantasm Guard

Base: Phantasm, com 50% de casco, escudo e dano; a velocidade e o alcance são os da nave de origem.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Phantasm Guard#1}} | {{guide:vitals.hull@Phantasm Guard#2}} | {{guide:vitals.hull@Phantasm Guard#3}} |
| Escudo | {{guide:vitals.shield@Phantasm Guard#1}} | {{guide:vitals.shield@Phantasm Guard#2}} | {{guide:vitals.shield@Phantasm Guard#3}} |
| Dano dos lasers (uma salva por segundo) | {{guide:vitals.dps@Phantasm Guard#1}} | {{guide:vitals.dps@Phantasm Guard#2}} | {{guide:vitals.dps@Phantasm Guard#3}} |
| Velocidade | {{guide:vitals.speed@Phantasm Guard#1}} | {{guide:vitals.speed@Phantasm Guard#2}} | {{guide:vitals.speed@Phantasm Guard#3}} |
| Alcance dos lasers | 700 | 700 | 700 |
| Raio de agressão | só quando atacado | só quando atacado | só quando atacado |
| Cura o líder, cada um, por segundo (só o casco) | 30 | 45 | 60 |
| Créditos | {{guide:spoils.pay.credits@Phantasm Guard#1}} | {{guide:spoils.pay.credits@Phantasm Guard#2}} | {{guide:spoils.pay.credits@Phantasm Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Phantasm Guard#1}} | {{guide:spoils.pay.thulium@Phantasm Guard#2}} | {{guide:spoils.pay.thulium@Phantasm Guard#3}} |
| Experiência (XP) | {{guide:spoils.pay.experience@Phantasm Guard#1}} | {{guide:spoils.pay.experience@Phantasm Guard#2}} | {{guide:spoils.pay.experience@Phantasm Guard#3}} |
| Honra | {{guide:spoils.pay.honor@Phantasm Guard#1}} | {{guide:spoils.pay.honor@Phantasm Guard#2}} | {{guide:spoils.pay.honor@Phantasm Guard#3}} |
| Pontos PvE por abate | 1 | 1 | 1 |

**Saque**: nenhum. O abate paga só os seus créditos, Thulium, XP e honra.

<!-- phantasm-members:end -->
