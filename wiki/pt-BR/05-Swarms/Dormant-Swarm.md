<!-- wiki-i18n source: fcba1b51b68a9123 -->
<!-- wiki-i18n title: Enxame Dormant -->
# Enxame Dormant {#dormant-swarm}

O enxame Dormant é uma **Dormant Force** com suas **Dormant Pulses**: um grupo de naves que nunca começam uma luta e batem muito forte depois de acordadas. Há só um nos setores de perigo de cada mundo (o [Deep Void](/wiki/03-Mechanics/Deep-Void.md#the-dormant-swarms-visit) tem uma visita própria, uma vez por dia). Ele vagueia de um setor de perigo para o seguinte e é a luta mais dura e o saque mais rico dos enxames: uma luta para um grupo grande das naves mais fortes. A partir do dia 11 da temporada ele começa no [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) de `DS-4`, volta mais cedo e paga o dobro (veja a lista *Em resumo*).

## Resumo rápido {#at-a-glance}

<!-- dormant-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Onde**: Os setores de perigo `DS-1`, `DS-2`, `DS-3`, `DS-4`, voando de um para outro
- **Quantos**: Um em cada mundo
- **Aparece**: Do dia 4 da temporada até o reset (Beta e Gamma: do dia 1 da temporada)
- **Líder**: Dormant Force
- **Seguidores**: 2 × Dormant Pulse, voando com o líder
- **Os seguidores ficam a**: até 700 unidades do líder
- **Líder destruído**: Dormant Pulse assume a liderança
- **Líder destruído**: Os seguidores vão embora 30 s depois que o líder é destruído, estejam atacando ou não
- **Deslocamento**: Fica 8 a 15 min num mapa, depois voa até o portão de outro setor de perigo. Nunca usa os portões que saem dos setores de perigo e nunca entra no anel do buraco negro
- **Volta**: {{guide:vitals.respawn@Dormant Force#1;Dormant Force#2;Dormant Force#3}} depois que o enxame inteiro é destruído, num setor de perigo aleatório
- **A partir do dia 11 da temporada**: Aparece no [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) de `DS-4` em vez de num setor de perigo aleatório, volta 30 min depois que o enxame inteiro é destruído, e cada nave paga ×2 (créditos, Thulium, XP e honra; o espólio continua o mesmo)
- **Avisos**: Os pilotos do mundo inteiro são avisados quando o enxame aparece e quando é destruído. São linhas do Sistema: aparecem na aba **Sistema** do chat, com uma contagem de linhas não lidas, e não em **Global** nem em **Local**. Um marcador o mostra nos mapas dos setores de perigo e no mapa da galáxia. O registro de baixas nomeia o piloto a quem o abate é creditado.

<!-- dormant-glance:end -->

## Os membros {#the-members}

- **Dormant Force**: uma Wraith com força total, com lasers que batem três vezes mais forte que os de um equipamento típico. Ela lidera o enxame, é passiva até ser acertada e dispara **foguetes retos** no primeiro piloto que a acertou.
- **Dormant Pulse**: uma Paragon com força total, com lasers pesados do mesmo tipo, cada um batendo duas vezes mais forte que um da Force, e foguetes próprios. Uma Pulse tem menos lasers que a Force, então a sua rajada inteira é maior que a da Force, mas não o dobro (os números estão abaixo). As Pulses voam perto da Force, e quando a Force é destruída uma delas assume a liderança.

São passivas: nunca vão atrás de um piloto. Se uma delas é acertada, as outras que estão perto entram na luta contra o primeiro piloto que a acertou.

## Como a luta transcorre {#how-the-fight-goes}

- **Encontre-o.** O mundo inteiro é avisado quando ele aparece, e um marcador o mostra nos mapas dos setores de perigo e no mapa da galáxia. Ele fica num mapa pelo tempo da lista *Resumo rápido*, depois voa até o portão de outro setor de perigo e salta; nunca usa um portão que saia dos setores de perigo e nunca entra no anel do buraco negro. Voa na velocidade da nave mais lenta e, como um piloto, não inicia nem termina um salto sob fogo. A partir do dia 11 da temporada ele aparece primeiro logo fora da zona do [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md), onde um grupo pode esperá-lo fora do alcance dos canhões do pântano, e depois sai voando por um portão de `DS-4`.
- **Não se derrota sozinho, nem com poucos.** Oito pilotos de nível 8 em Paragons com munição x2 ou x4 o destroem em cerca de um minuto em Alpha, perdendo no máximo uma nave; uma Paragon sozinha é destruída, e três ou quatro com munição x2 também. Os enxames de Beta e Gamma são mais fortes ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)), então esses mundos pedem grupos maiores.
- **Os lasers dele decidem a luta.** Juntos, podem destruir uma Paragon em menos de um minuto, e até uma com os melhores escudos em menos de dois, com foguetes ou sem: leve o seu dano rápido, com os melhores escudos que tiver.
- **Nave por nave.** Cada nave tem o seu casco e o seu pagamento, então a Force ou uma Pulse pode ser destruída primeiro. O enxame só é substituído quando é destruído por inteiro, depois do tempo da lista *Resumo rápido*.

## As três etapas do líder {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

A luta tem três etapas ([como funcionam](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); cada uma acontece uma vez.

- **No início**: Recebe 70% de cada golpe enquanto um dos seus Dormant Pulses estiver vivo.
- **Abaixo de dois terços**: Seus Dormant Pulses disparam um foguete a cada 2,5 s por 15 s.
- **Abaixo de um terço**: Enquanto todos os seus Dormant Pulses estiverem vivos, eles o reparam em 5% do casco por segundo por 6 s.

<!-- mob-ladder:end -->

## Recompensas e saque {#rewards-and-drops}

Cada nave paga por si, pelo dano causado a ela ([como o abate de um chefe paga](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)), e cada uma larga uma caixa para o piloto que mais lhe causou dano. A **caixa da Force** é o prêmio: muita munição x3 e x4, foguetes Épicos de um só tipo e, de vez em quando, um N.I.K.E. ou um N.U.K.E. As **Pulses** podem largar uma Ancient Control Unit, um Power Core ou Dark Matter. Um minuto de luta contra o enxame paga mais do que um minuto de luta contra o Crystalys, o alienígena mais bem pago. A partir do dia 11 da temporada cada nave paga o dobro (veja a lista *Em resumo*); as caixas são as mesmas.

## Os números {#the-numbers}

Os números das naves do enxame nos três mundos ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)). Os créditos, o Thulium, o XP e a honra das tabelas são o pagamento anterior ao dia 11 da temporada; a partir desse dia um abate paga o dobro.

<!-- dormant-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Dormant Force

Base: Wraith, com 100% do casco e 300% do dano dos lasers; a velocidade e o alcance são os da nave de origem. Dispara um foguete reto a cada 5 s: [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Dormant Force#1}} | {{guide:vitals.hull@Dormant Force#2}} | {{guide:vitals.hull@Dormant Force#3}} |
| Escudo | {{guide:vitals.shield@Dormant Force#1}} | {{guide:vitals.shield@Dormant Force#2}} | {{guide:vitals.shield@Dormant Force#3}} |
| Dano dos lasers (uma salva por segundo) | {{guide:vitals.dps@Dormant Force#1}} | {{guide:vitals.dps@Dormant Force#2}} | {{guide:vitals.dps@Dormant Force#3}} |
| Velocidade | {{guide:vitals.speed@Dormant Force#1}} | {{guide:vitals.speed@Dormant Force#2}} | {{guide:vitals.speed@Dormant Force#3}} |
| Alcance dos lasers | 800 | 800 | 800 |
| Raio de agressão | só quando atacado | só quando atacado | só quando atacado |
| Dano dos foguetes, no máximo | {{guide:behaviour.ability:rocket.damage@Dormant Force#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#3}} |
| Créditos | {{guide:spoils.pay.credits@Dormant Force#1}} | {{guide:spoils.pay.credits@Dormant Force#2}} | {{guide:spoils.pay.credits@Dormant Force#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Force#1}} | {{guide:spoils.pay.thulium@Dormant Force#2}} | {{guide:spoils.pay.thulium@Dormant Force#3}} |
| Experiência (XP) | {{guide:spoils.pay.experience@Dormant Force#1}} | {{guide:spoils.pay.experience@Dormant Force#2}} | {{guide:spoils.pay.experience@Dormant Force#3}} |
| Honra | {{guide:spoils.pay.honor@Dormant Force#1}} | {{guide:spoils.pay.honor@Dormant Force#2}} | {{guide:spoils.pay.honor@Dormant Force#3}} |
| Pontos PvE por abate | 25 | 25 | 25 |

**Saque**: uma caixa, para o piloto que mais causou dano.

| Item |
| :--- |
| {{guide:spoils.box@Dormant Force#1;Dormant Force#2;Dormant Force#3}} |

### Dormant Pulse

Base: Paragon, com 100% do casco e 600% do dano dos lasers; a velocidade e o alcance são os da nave de origem. Dispara um foguete reto a cada 5 s: [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Dormant Pulse#1}} | {{guide:vitals.hull@Dormant Pulse#2}} | {{guide:vitals.hull@Dormant Pulse#3}} |
| Escudo | {{guide:vitals.shield@Dormant Pulse#1}} | {{guide:vitals.shield@Dormant Pulse#2}} | {{guide:vitals.shield@Dormant Pulse#3}} |
| Dano dos lasers (uma salva por segundo) | {{guide:vitals.dps@Dormant Pulse#1}} | {{guide:vitals.dps@Dormant Pulse#2}} | {{guide:vitals.dps@Dormant Pulse#3}} |
| Velocidade | {{guide:vitals.speed@Dormant Pulse#1}} | {{guide:vitals.speed@Dormant Pulse#2}} | {{guide:vitals.speed@Dormant Pulse#3}} |
| Alcance dos lasers | 800 | 800 | 800 |
| Raio de agressão | só quando atacado | só quando atacado | só quando atacado |
| Dano dos foguetes, no máximo | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#3}} |
| Créditos | {{guide:spoils.pay.credits@Dormant Pulse#1}} | {{guide:spoils.pay.credits@Dormant Pulse#2}} | {{guide:spoils.pay.credits@Dormant Pulse#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Pulse#1}} | {{guide:spoils.pay.thulium@Dormant Pulse#2}} | {{guide:spoils.pay.thulium@Dormant Pulse#3}} |
| Experiência (XP) | {{guide:spoils.pay.experience@Dormant Pulse#1}} | {{guide:spoils.pay.experience@Dormant Pulse#2}} | {{guide:spoils.pay.experience@Dormant Pulse#3}} |
| Honra | {{guide:spoils.pay.honor@Dormant Pulse#1}} | {{guide:spoils.pay.honor@Dormant Pulse#2}} | {{guide:spoils.pay.honor@Dormant Pulse#3}} |
| Pontos PvE por abate | 11 | 11 | 11 |

**Saque**: uma caixa, para o piloto que mais causou dano.

| Item |
| :--- |
| {{guide:spoils.box@Dormant Pulse#1;Dormant Pulse#2;Dormant Pulse#3}} |

<!-- dormant-members:end -->
