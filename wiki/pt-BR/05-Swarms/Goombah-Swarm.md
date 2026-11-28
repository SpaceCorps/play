<!-- wiki-i18n source: 38ffa8ba7cbf5000 -->
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
- **Volta**: {{guide:vitals.respawn@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} depois que o líder é destruído, no mesmo setor
- **Avisos**: Os pilotos do setor são avisados quando o líder aparece e quando é destruído. São linhas do Sistema: aparecem na aba **Sistema** do chat, com uma contagem de linhas não lidas, e não em **Global** nem em **Local**. O registro de baixas nomeia o piloto a quem o abate é creditado.

<!-- goombah-glance:end -->

## Os membros {#the-members}

- **Boss Goombah**: um Goombah maior, com a tonalidade do enxame e o nome por cima, com casco, escudo e salva de laser próprios (os números estão abaixo). É passivo: vagueia até um piloto acertá-lo, então vai atrás desse piloto e atira nele, e as naves do seu enxame que estão perto entram na luta. O alcance da arma e a velocidade são os de um Goombah, e ele nunca conserta o próprio casco. As suas [três etapas](#the-leaders-three-steps) e uma [habilidade especial](/wiki/03-Mechanics/Special-Abilities.md) podem mudar isso.
- **Goombah Guard**: um Goombah menor com a tonalidade do enxame. Os Guards ficam perto do chefe, entram na luta quando uma nave de enxame perto deles é acertada, e cada um que está perto do chefe cura o casco dele. Um Guard conserta o próprio casco depois de um descanso, como um Goombah faz.

## Como a luta transcorre {#how-the-fight-goes}

- **Leve um grupo das naves mais fortes.** Três pilotos de nível 8 com munição x2 o destroem em cerca de 75 segundos em Alpha, perdendo no máximo uma nave; dois deles precisam de munição x4, e pilotos de níveis mais baixos não causam dano suficiente para vencer.
- **Atire no chefe, não nos Guards.** Um Guard cai em segundos, mas um novo chega na frequência que a lista *Resumo rápido* diz, e o que os Guards curam é uma parte pequena do que um grupo causa: deixá-los em paz custa um pouco de tempo, caçá-los custa mais.
- **Beta e Gamma são mais duros.** Os enxames desses mundos são mais fortes ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)), então pedem mais pilotos ou munição melhor.
- **Fique de olho no setor.** `x-4` é um setor PvP em Alpha, e `x-3` e `x-4` são em Beta e Gamma ([Mundos](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): um rival pode entrar na luta ou esperar a caixa. Deixe uma nave do grupo de vigia.
- **O chefe volta** depois do tempo da lista *Resumo rápido*, com a força toda, no mesmo setor, e seus Guards chegam um depois do outro.

## As três etapas do líder {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

A luta tem três etapas ([como funcionam](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); cada uma acontece uma vez.

- **No início**: Recebe 50% de cada golpe por 6 s.
- **Abaixo de dois terços**: O dano dele é multiplicado por ×1,5 e a velocidade por ×1,25 por 10 s.
- **Abaixo de um terço**: Recupera 25% do casco e do escudo (uma rajada de dano o interrompe), e seus Goombah Guards o reparam ×2 mais rápido nesse tempo.

<!-- mob-ladder:end -->

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
| Casco | {{guide:vitals.hull@Boss Goombah#1}} | {{guide:vitals.hull@Boss Goombah#2}} | {{guide:vitals.hull@Boss Goombah#3}} |
| Escudo | {{guide:vitals.shield@Boss Goombah#1}} | {{guide:vitals.shield@Boss Goombah#2}} | {{guide:vitals.shield@Boss Goombah#3}} |
| Dano dos lasers (uma salva por segundo) | {{guide:vitals.dps@Boss Goombah#1}} | {{guide:vitals.dps@Boss Goombah#2}} | {{guide:vitals.dps@Boss Goombah#3}} |
| Velocidade | {{guide:vitals.speed@Boss Goombah#1}} | {{guide:vitals.speed@Boss Goombah#2}} | {{guide:vitals.speed@Boss Goombah#3}} |
| Alcance dos lasers | 800 | 800 | 800 |
| Raio de agressão | só quando atacado | só quando atacado | só quando atacado |
| Créditos | {{guide:spoils.pay.credits@Boss Goombah#1}} | {{guide:spoils.pay.credits@Boss Goombah#2}} | {{guide:spoils.pay.credits@Boss Goombah#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Goombah#1}} | {{guide:spoils.pay.thulium@Boss Goombah#2}} | {{guide:spoils.pay.thulium@Boss Goombah#3}} |
| Experiência (XP) | {{guide:spoils.pay.experience@Boss Goombah#1}} | {{guide:spoils.pay.experience@Boss Goombah#2}} | {{guide:spoils.pay.experience@Boss Goombah#3}} |
| Honra | {{guide:spoils.pay.honor@Boss Goombah#1}} | {{guide:spoils.pay.honor@Boss Goombah#2}} | {{guide:spoils.pay.honor@Boss Goombah#3}} |
| Pontos PvE por abate | 14 | 14 | 14 |

**Saque**: uma caixa, para o piloto que mais causou dano.

| Item |
| :--- |
| {{guide:spoils.box@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} |

### Goombah Guard

Base: Goombah, com 20% de casco, escudo e dano; a velocidade e o alcance são os da nave de origem.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Goombah Guard#1}} | {{guide:vitals.hull@Goombah Guard#2}} | {{guide:vitals.hull@Goombah Guard#3}} |
| Escudo | {{guide:vitals.shield@Goombah Guard#1}} | {{guide:vitals.shield@Goombah Guard#2}} | {{guide:vitals.shield@Goombah Guard#3}} |
| Dano dos lasers (uma salva por segundo) | {{guide:vitals.dps@Goombah Guard#1}} | {{guide:vitals.dps@Goombah Guard#2}} | {{guide:vitals.dps@Goombah Guard#3}} |
| Velocidade | {{guide:vitals.speed@Goombah Guard#1}} | {{guide:vitals.speed@Goombah Guard#2}} | {{guide:vitals.speed@Goombah Guard#3}} |
| Alcance dos lasers | 800 | 800 | 800 |
| Raio de agressão | só quando atacado | só quando atacado | só quando atacado |
| Cura o líder, cada um, por segundo (só o casco) | 110 | 165 | 220 |
| Créditos | {{guide:spoils.pay.credits@Goombah Guard#1}} | {{guide:spoils.pay.credits@Goombah Guard#2}} | {{guide:spoils.pay.credits@Goombah Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Goombah Guard#1}} | {{guide:spoils.pay.thulium@Goombah Guard#2}} | {{guide:spoils.pay.thulium@Goombah Guard#3}} |
| Experiência (XP) | {{guide:spoils.pay.experience@Goombah Guard#1}} | {{guide:spoils.pay.experience@Goombah Guard#2}} | {{guide:spoils.pay.experience@Goombah Guard#3}} |
| Honra | {{guide:spoils.pay.honor@Goombah Guard#1}} | {{guide:spoils.pay.honor@Goombah Guard#2}} | {{guide:spoils.pay.honor@Goombah Guard#3}} |
| Pontos PvE por abate | 3 | 3 | 3 |

**Saque**: nenhum. O abate paga só os seus créditos, Thulium, XP e honra.

<!-- goombah-members:end -->
