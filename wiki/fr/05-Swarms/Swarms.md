<!-- wiki-i18n source: bbd76eb145ce6188 -->
<!-- wiki-i18n title: Essaims -->
# Essaims {#swarms}

Un **essaim** est un groupe d’aliens qui parcourt une partie de la galaxie sous la conduite d’un **meneur** : un boss, bien plus fort que n’importe quel alien autour de lui, avec des **suivants** qui le protègent et, dans deux des essaims, le soignent. Il y en a trois, et chacun a son propre article :

- [Essaim Seeker](/wiki/05-Swarms/Seeker-Swarm.md) : le Boss Seeker et ses Seeker Slaves, le plus petit essaim, dans les secteurs où volent les nouveaux pilotes.
- [Essaim Pirate](/wiki/05-Swarms/Pirate-Swarm.md) : le Pirate Boss et ses Pirate Scouts, un long combat pour un groupe.
- [Essaim Dormant](/wiki/05-Swarms/Dormant-Swarm.md) : la Dormant Force et ses Dormant Pulses, l’essaim le plus fort, au butin le plus riche.

Leurs vaisseaux sont des **aliens d’espèces à part** : ils ont leurs propres noms et leurs propres compteurs d’éliminations, et aucun ne compte comme un Seeker, un Phantasm ou un autre alien. Un vaisseau d’essaim a la forme du vaisseau sur lequel il est construit, avec une teinte à lui et son nom au-dessus ; le Boss Seeker est un Seeker bien plus grand.

## Les trois essaims {#the-three-swarms}

<!-- swarms-list:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Essaim | Où | Combien | Meneur | Suivants | Revient |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**Essaim Pirate**](/wiki/05-Swarms/Pirate-Swarm.md) | Les secteurs `x-2` et `x-3` de chaque corporation | Un dans chacun de ces secteurs, 6 dans chaque monde | **Pirate Boss** | Jusqu’à 5 × Pirate Scout, un nouveau toutes les 10 s | 2 min après la destruction du meneur, dans le même secteur |
| [**Essaim Dormant**](/wiki/05-Swarms/Dormant-Swarm.md) | Les secteurs dangereux `DS-1`, `DS-2`, `DS-3`, `DS-4`, qu’il parcourt de l’un à l’autre | Un dans chaque monde | **Dormant Force** | 2 × Dormant Pulse, qui volent avec le meneur | 1 h après la destruction de tout l’essaim, dans un secteur dangereux tiré au hasard |
| [**Essaim Seeker**](/wiki/05-Swarms/Seeker-Swarm.md) | Les secteurs `x-1` et `x-2` de chaque corporation | Un dans chacun de ces secteurs, 6 dans chaque monde | **Boss Seeker** | Jusqu’à 4 × Seeker Slave, un nouveau toutes les 10 s | 2 min après la destruction du meneur, dans le même secteur |

<!-- swarms-list:end -->

## Quand et où {#when-and-where}

Les essaims commencent à apparaître au **Premier contact** et restent jusqu’à la réinitialisation (voir la [Chronologie des réinitialisations](/wiki/03-Mechanics/Wipe-Timeline.md) ; le jour est la première ligne des règles ci-dessous). **Chaque monde a ses propres essaims**, aux mêmes endroits : le Pirate Boss d’Alpha et celui de Beta sont deux vaisseaux différents, et un essaim que vous détruisez dans votre monde n’est pas détruit dans un autre. Un essaim détruit revient après le délai du tableau ci-dessus.

## Les règles de chaque essaim {#the-rules-of-every-swarm}

<!-- swarms-rules:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- Les essaims apparaissent à partir du jour 4 de la saison jusqu’à la réinitialisation.
- Quand un vaisseau d’essaim est touché, les vaisseaux de son essaim situés à moins de 1 500 unités se joignent au combat contre le premier pilote qui l’a touché.
- Un meneur apparaît à au moins 2 500 unités du bord de chaque anneau de station et de portail.
- Un pilote qui a infligé au moins 5 % des dégâts subis par un boss est payé pour son élimination.

<!-- swarms-rules:end -->

## Les mondes {#the-worlds}

Le monde met un essaim à l’échelle comme il le fait pour tout alien ([Mondes](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)) : la coque, le bouclier, la recharge du bouclier, les dégâts des lasers, les dégâts des roquettes et les soins d’un vaisseau d’essaim sont les valeurs d’Alpha multipliées par la puissance ci-dessous, et une élimination paie le gain ci-dessous. La vitesse, la portée et le butin sont les mêmes dans tous les mondes. Les articles donnent les valeurs de chaque vaisseau dans les trois mondes.

<!-- swarms-world:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Monde | Puissance | Gain |
| :--- | ---: | ---: |
| **Alpha** | ×1 | ×1 |
| **Beta** | ×1,5 | ×2 |
| **Gamma** | ×2 | ×3 |

<!-- swarms-world:end -->

## Ce que les pilotes apprennent {#what-the-pilots-are-told}

Les essaims Seeker et Pirate préviennent les pilotes de leur propre secteur quand un boss apparaît et quand il est détruit. L’essaim Dormant prévient son monde entier, et il est marqué sur les cartes des secteurs dangereux et sur la carte de la galaxie, pour que les pilotes puissent le trouver. Ce sont des lignes Système : elles apparaissent dans l’onglet **Système** du chat, avec un compteur de lignes non lues, et pas dans **Global** ni **Local**. L’élimination d’un boss a aussi une ligne dans le fil des éliminations, qui nomme le pilote à qui elle est créditée. La liste *D’un coup d’œil* de chaque article dit qui est prévenu.

## Combattre un essaim {#fighting-a-swarm}

- **Les meneurs ne commencent jamais un combat.** Un meneur erre jusqu’à ce qu’un pilote le touche, puis il riposte, et les vaisseaux de son essaim proches de lui se joignent au combat contre le premier pilote qui l’a touché (la distance est donnée dans les règles ci-dessus). Les Pirate Scouts font exception : ils attaquent tout pilote qui s’approche. Un meneur ne répare jamais sa coque de lui-même, donc les dégâts que vous lui avez infligés restent sur lui, sauf si ses suivants le soignent ; son bouclier se recharge comme celui de tout alien.
- **Les vaisseaux d’essaim ne combattent que les pilotes.** Ils ne tirent pas sur les aliens et les aliens ne tirent pas sur eux, et les [pilotes de corporation](/wiki/03-Mechanics/Company-Pilots.md) les ignorent : ils ne chassent pas un vaisseau d’essaim et ne viennent pas vous aider contre l’un d’eux.
- **Roquettes.** Le Pirate Boss, la Dormant Force et les Pulses tirent des roquettes **droites**, des [roquettes Rivet](/wiki/06-Items/Rockets.md), sur le pilote qui les a attaqués. Un vaisseau qui reste en mouvement les esquive, un vaisseau immobile est touché.
- **L’ampleur des combats.** L’essaim Seeker est fait pour deux pilotes, l’essaim Pirate pour un petit groupe, l’essaim Dormant pour un grand groupe des vaisseaux les plus forts ; les mondes plus élevés demandent plus de pilotes, comme pour tout alien.

## Quoi emporter {#what-to-bring}

- **Un groupe.** Volez en [groupe](/wiki/03-Mechanics/Groups.md) : les essaims sont équilibrés pour des groupes, un pilote isolé de bas niveau est détruit vite, et seuls les vaisseaux les plus forts peuvent vaincre seuls un Pirate Boss. Personne ne vainc seul l’essaim Dormant. Un essaim combat le premier pilote qui l’a touché ([Qui un alien combat](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)), donc laissez le vaisseau le plus robuste du groupe commencer.
- **De meilleures munitions.** Emportez des munitions x2 ou mieux (voir [Lasers et munitions](/wiki/06-Items/Lasers.md)). Les soins des suivants d’un essaim peuvent dépasser ce qu’un petit groupe inflige avec des munitions x1.
- **Des boucliers et des réparations** pour un long combat : les compétences de votre vaisseau ([Compétences](/wiki/03-Mechanics/Abilities.md)) comptent surtout dans le combat contre les pirates, qui dure des minutes.
- **De la place pour bouger.** Restez hors de portée d’une arme que vous surpassez en portée, et gardez le mouvement face à une roquette.

## Comment paie l’élimination d’un boss {#how-a-boss-kill-pays}

Un alien ordinaire paie le pilote qui l’a touché en premier ([Combat](/wiki/03-Mechanics/Combat.md#kill-rewards-first-hit-claims)). Le meneur d’un essaim, et chaque Dormant Pulse, paient plutôt **selon les dégâts infligés** :

- **Le gain est réparti selon les dégâts.** Tout pilote qui a infligé au moins la part indiquée dans les règles ci-dessus est payé, en proportion des dégâts infligés : les crédits, le Thulium, l’XP et l’honneur de l’élimination sont répartis entre eux. Un pilote sous cette part ne reçoit rien.
- **La caisse de cargaison va au pilote qui a infligé le plus de dégâts.** Elle est à lui (et à son clan) pendant 30 secondes, comme pour tout alien, puis n’importe qui peut la prendre ([Cargaison](/wiki/03-Mechanics/Cargo.md)). Chaque vaisseau Dormant a son propre décompte de dégâts et sa propre caisse.
- **Les suivants paient comme d’habitude** : les Pirate Scouts et les Seeker Slaves paient le pilote qui les a touchés en premier, et leur gain est faible à côté de celui d’un boss.
- **Le gain d’un boss est fait pour battre les aliens qui l’entourent.** Une minute de combat contre un Pirate Boss paie plus qu’une minute de combat contre un Goombah, et l’essaim Dormant paie plus encore ; le Boss Seeker paie exactement dix Seekers.

Chaque élimination est comptée sous le nom propre du vaisseau dans vos statistiques d’éliminations et ajoute des points PvE à votre classement :

<!-- swarms-points:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Vaisseau d’essaim | Essaim | Points PvE par élimination |
| :--- | :--- | ---: |
| **Pirate Boss** | Essaim Pirate | 10 |
| **Pirate Scout** | Essaim Pirate | 1 |
| **Dormant Force** | Essaim Dormant | 25 |
| **Dormant Pulse** | Essaim Dormant | 10 |
| **Boss Seeker** | Essaim Seeker | 5 |
| **Seeker Slave** | Essaim Seeker | 1 |

<!-- swarms-points:end -->

Une élimination d’essaim ne compte pas comme celle d’un autre alien : un Boss Seeker ou un Seeker Slave n’est pas un Seeker pour une mission qui demande des Seekers, et les paliers des points de réinitialisation ([Chronologie des réinitialisations](/wiki/03-Mechanics/Wipe-Timeline.md#earning-wipe-points)) sont ceux des cinq aliens seulement.
