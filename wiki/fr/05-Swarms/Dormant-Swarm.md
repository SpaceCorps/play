<!-- wiki-i18n source: 4bfb24feda6f6bf5 -->
<!-- wiki-i18n title: Essaim Dormant -->
# Essaim Dormant {#dormant-swarm}

L’essaim Dormant est une **Dormant Force** avec ses **Dormant Pulses** : un groupe de vaisseaux qui ne commencent jamais un combat et frappent très fort une fois réveillés. Il n’y en a qu’un dans chaque monde. Il erre d’un secteur dangereux au suivant, et c’est le combat le plus dur et le butin le plus riche des essaims : un combat pour un grand groupe des vaisseaux les plus forts.

## D’un coup d’œil {#at-a-glance}

<!-- dormant-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Où** : Les secteurs dangereux `DS-1`, `DS-2`, `DS-3`, `DS-4`, qu’il parcourt de l’un à l’autre
- **Combien** : Un dans chaque monde
- **Apparaît** : Du jour 4 de la saison jusqu’à la réinitialisation
- **Meneur** : Dormant Force
- **Suivants** : 2 × Dormant Pulse, qui volent avec le meneur
- **Les suivants restent** : à 700 unités au plus du meneur
- **Meneur détruit** : Dormant Pulse prend la tête
- **Déplacements** : Reste 8 à 15 min sur une carte, puis vole vers le portail d’un autre secteur dangereux. Il ne prend jamais les portails qui sortent des secteurs dangereux et n’entre jamais dans l’anneau du trou noir
- **Revient** : 1 h après la destruction de tout l’essaim, dans un secteur dangereux tiré au hasard
- **Annonces** : Les pilotes du monde entier sont prévenus quand l’essaim apparaît et quand il est détruit. Ce sont des lignes Système : elles apparaissent dans l’onglet **Système** du chat, avec un compteur de lignes non lues, et pas dans **Global** ni **Local**. Un marqueur le montre sur les cartes des secteurs dangereux et sur la carte de la galaxie. Le fil des éliminations nomme le pilote à qui l’élimination est créditée.

<!-- dormant-glance:end -->

## Les membres {#the-members}

- **Dormant Force** : un Wraith à pleine force, avec des lasers qui frappent trois fois plus fort que ceux d’un équipement typique. Elle mène l’essaim, est passive tant qu’on ne la touche pas, et tire des **roquettes droites** sur le premier pilote qui l’a touchée.
- **Dormant Pulse** : un Paragon à pleine force, avec le même genre de lasers lourds et ses propres roquettes. Les Pulses volent près de la Force, et quand la Force est détruite, l’une d’elles prend la tête.

Ils sont passifs : ils n’attaquent jamais un pilote. Si l’un d’eux est touché, les autres proches de lui se joignent au combat contre le premier pilote qui l’a touché.

## Le déroulement du combat {#how-the-fight-goes}

- **Trouvez-le.** Le monde entier est prévenu quand il apparaît, et un marqueur le montre sur les cartes des secteurs dangereux et sur la carte de la galaxie. Il reste sur une carte le temps indiqué dans la liste *D’un coup d’œil*, puis vole vers la porte d’un autre secteur dangereux et saute ; il ne prend jamais une porte qui sort des secteurs dangereux et n’entre jamais dans l’anneau du trou noir. Il vole à la vitesse de son vaisseau le plus lent et, comme un pilote, ne commence ni ne termine un saut sous le feu.
- **On ne le bat pas seul, ni à quelques-uns.** Huit pilotes de niveau 8 en Paragon avec des munitions x2 ou x4 le détruisent en environ une minute dans Alpha, en perdant au plus un vaisseau ; un Paragon seul est détruit, et trois avec des munitions x2 aussi. Les essaims de Beta et de Gamma sont plus forts ([Mondes](/wiki/05-Swarms/Swarms.md#the-worlds)), ces mondes demandent donc de plus grands groupes.
- **Ses lasers décident du combat.** Ensemble, ils peuvent détruire un Paragon en moins d’une minute, et même un Paragon aux meilleurs boucliers en moins de deux, roquettes ou non : amenez vos dégâts vite, avec les meilleurs boucliers que vous ayez.
- **Vaisseau par vaisseau.** Chaque vaisseau a sa propre coque et son propre gain, la Force ou une Pulse peut donc être détruite en premier. L’essaim n’est remplacé que lorsqu’il est entièrement détruit, après le délai de la liste *D’un coup d’œil*.

## Récompenses et butin {#rewards-and-drops}

Chaque vaisseau paie pour lui-même, selon les dégâts qu’il a subis ([comment paie l’élimination d’un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)), et chacun laisse une caisse pour le pilote qui lui a infligé le plus de dégâts. La **caisse de la Force** est le gros lot : énormément de munitions x3 et x4, des roquettes Épiques d’une seule sorte et, de temps en temps, un N.I.K.E. ou un N.U.K.E. Les **Pulses** peuvent laisser une Ancient Control Unit, un Power Core ou de la Dark Matter. Une minute de combat contre l’essaim paie plus qu’une minute de combat contre le Crystalys, l’alien le mieux payé.

## Les valeurs {#the-numbers}

Les valeurs des vaisseaux de l’essaim dans les trois mondes ([Mondes](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- dormant-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Dormant Force

Base : Wraith, avec 100 % de coque, de bouclier et de dégâts ; la vitesse et la portée sont celles du vaisseau d’origine. Tire une roquette droite toutes les 5 s : [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | 324 000 | 486 000 | 648 000 |
| Bouclier | 83 400 | 125 100 | 166 800 |
| Dégâts des lasers (une salve par seconde) | 2 880 | 4 320 | 5 760 |
| Vitesse | 220 | 220 | 220 |
| Portée des lasers | 800 | 800 | 800 |
| Rayon d’aggro | seulement si attaqué | seulement si attaqué | seulement si attaqué |
| Dégâts des roquettes, au maximum | 7 500 | 11 250 | 15 000 |
| Crédits | 200 000 | 400 000 | 600 000 |
| Thulium | 535 | 1 070 | 1 605 |
| Expérience (XP) | 32 100 | 64 200 | 96 300 |
| Honneur | 139 | 278 | 417 |
| Points PvE par élimination | 25 | 25 | 25 |

**Butin** : une caisse, pour le pilote qui a infligé le plus de dégâts.

| Objet | Chance | Quantité |
| :--- | ---: | ---: |
| Ultra Core et Experimental Fusion Core, répartis à parts égales | 100 % | 2 000–3 000 en tout |
| L’une des 4 [roquettes](/wiki/06-Items/Rockets.md) Épiques, tirée au hasard | 100 % | 30–50 |
| L’un de [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) et [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets), tiré au hasard | 50 % | 1 |

### Dormant Pulse

Base : Paragon, avec 100 % de coque, de bouclier et de dégâts ; la vitesse et la portée sont celles du vaisseau d’origine. Tire une roquette droite toutes les 5 s : [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | 128 000 | 192 000 | 256 000 |
| Bouclier | 64 570 | 96 855 | 129 140 |
| Dégâts des lasers (une salve par seconde) | 1 920 | 2 880 | 3 840 |
| Vitesse | 210 | 210 | 210 |
| Portée des lasers | 800 | 800 | 800 |
| Rayon d’aggro | seulement si attaqué | seulement si attaqué | seulement si attaqué |
| Dégâts des roquettes, au maximum | 5 000 | 7 500 | 10 000 |
| Crédits | 95 000 | 190 000 | 285 000 |
| Thulium | 255 | 510 | 765 |
| Expérience (XP) | 15 200 | 30 400 | 45 600 |
| Honneur | 66 | 132 | 198 |
| Points PvE par élimination | 11 | 11 | 11 |

**Butin** : une caisse, pour le pilote qui a infligé le plus de dégâts.

| Objet | Chance | Quantité |
| :--- | ---: | ---: |
| Ancient Control Unit | 20 % | 1 |
| Power Core | 20 % | 1 |
| Dark Matter | 20 % | 1–5 |

<!-- dormant-members:end -->
