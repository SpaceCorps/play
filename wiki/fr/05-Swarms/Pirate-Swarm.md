<!-- wiki-i18n source: f06b4c7b561b1789 -->
<!-- wiki-i18n title: Essaim Pirate -->
# Essaim Pirate {#pirate-swarm}

L’essaim Pirate est un **Pirate Boss** avec ses **Pirate Scouts** : un vaisseau énorme et lent qui n’attaque personne et répond par des roquettes, et une meute de vaisseaux plus rapides qui le protègent et le soignent. Il vit dans les secteurs entre la base d’une corporation et sa frontière, là où se jouent les niveaux intermédiaires du jeu, et c’est un long combat pour un groupe de pilotes, pas une élimination rapide.

## D’un coup d’œil {#at-a-glance}

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Où** : Les secteurs `x-2` et `x-3` de chaque corporation
- **Combien** : Un dans chacun de ces secteurs, 6 dans chaque monde
- **Apparaît** : Du jour 4 de la saison jusqu’à la réinitialisation
- **Meneur** : Pirate Boss
- **Suivants** : Jusqu’à 5 × Pirate Scout, un nouveau toutes les 10 s
- **Les suivants restent** : à 900 unités au plus du meneur
- **Soins** : Chaque Pirate Scout à moins de 600 unités du meneur soigne sa coque, 40 PV par seconde dans Alpha
- **Meneur détruit** : Les suivants partent 1 min après la destruction du meneur, sauf s’ils attaquent
- **Revient** : 2 min après la destruction du meneur, dans le même secteur
- **Annonces** : Le chat du secteur annonce quand le meneur apparaît et quand il est détruit. Le fil des éliminations nomme le pilote à qui l’élimination est créditée.

<!-- pirate-glance:end -->

## Les membres {#the-members}

- **Pirate Boss** : un vaisseau construit sur l’Ironclad, avec une part de sa force (les valeurs sont plus bas). Il est passif et ne tire **aucun laser** : sa seule arme est une **roquette droite** ([Roquettes](/wiki/06-Items/Rockets.md) ; laquelle dépend du secteur, voir le tableau), sur le pilote qui l’a attaqué, et il continue d’errer pendant qu’il tire. Il ne répare jamais sa coque de lui-même.
- **Pirate Scout** : un vaisseau construit sur le Kitefin, avec une part de sa force. Les Scouts attaquent tout pilote qui s’approche d’eux, restent près du boss, et chacun qui est près du boss soigne sa coque.

## Le déroulement du combat {#how-the-fight-goes}

- **Tirez sur le boss, pas sur les Scouts.** Les Scouts soignent le boss, mais ce soin est faible à côté de sa coque, et un nouveau Scout arrive aussi souvent que le dit la liste *D’un coup d’œil* : un groupe qui élimine d’abord les Scouts ne prend jamais d’avance sur eux, et seul un très grand groupe peut les éliminer tous et met pourtant plus de temps à finir le boss que celui qui les a laissés tranquilles. Les Scouts vous coûtent du temps, ils ne décident pas du combat.
- **Éloignez les Scouts.** Un Scout ne soigne que tant qu’il est à portée du boss, donc un Scout qui vous suit hors de cette portée ne soigne rien, et un Ostirion est plus rapide qu’un Scout.
- **Restez en mouvement.** La roquette du boss est droite et non guidée : un vaisseau qui reste en mouvement l’esquive, un vaisseau immobile est touché.
- **Amenez un groupe.** Trois pilotes en Ostirion avec des munitions x2 peuvent l’abattre en environ cinq minutes dans Alpha ; un Ostirion seul n’y arrive pas, un Paragon seul si. Le boss répond au premier pilote qui l’a touché, donc laissez le vaisseau le plus robuste commencer, et utilisez vos compétences (Emergency Repair, Shield Surge : [Compétences](/wiki/03-Mechanics/Abilities.md)) dans un combat aussi long. Les pilotes encore de niveau 2 ou 3 sont trop faibles pour lui, même là où ils volent : restez à l’écart jusqu’à être plus forts.
- **Le boss revient** après le délai de la liste *D’un coup d’œil*, dans le même secteur.

## Récompenses et butin {#rewards-and-drops}

Le Pirate Boss paie à la mesure du combat qu’il est : une minute de combat contre lui paie plus qu’une minute de combat contre un Goombah. Le gain est réparti selon les dégâts entre les pilotes qui l’ont combattu ([comment paie l’élimination d’un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Sa caisse est pour le pilote qui a infligé le plus de dégâts et peut contenir une **Reinforced Hull Plate**, des roquettes et des munitions. Les Scouts paient peu et ne laissent rien.

## Les valeurs {#the-numbers}

Les valeurs des vaisseaux de l’essaim dans les trois mondes ([Mondes](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss {#pirate-boss}

Base : Ironclad, avec 50 % de coque, de bouclier et de dégâts ; la vitesse et la portée sont celles du vaisseau d’origine. Tire une roquette droite toutes les 5 s : [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) dans `x-2`, [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) dans `x-3`.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | 300 000 | 450 000 | 600 000 |
| Bouclier | 50 100 | 75 150 | 100 200 |
| Dégâts des lasers (une salve par seconde) | aucun | aucun | aucun |
| Vitesse | 92 | 92 | 92 |
| Portée des lasers | – | – | – |
| Rayon d’aggro | seulement si attaqué | seulement si attaqué | seulement si attaqué |
| Dégâts des roquettes, au maximum | 2 500 (Rivet I) / 5 000 (Rivet II) | 3 750 (Rivet I) / 7 500 (Rivet II) | 5 000 (Rivet I) / 10 000 (Rivet II) |
| Crédits | 116 000 | 232 000 | 348 000 |
| Thulium | 725 | 1 450 | 2 175 |
| Expérience (XP) | 29 000 | 58 000 | 87 000 |
| Honneur | 232 | 464 | 696 |
| Points PvE par élimination | 10 | 10 | 10 |

**Butin** : une caisse, pour le pilote qui a infligé le plus de dégâts.

| Objet | Chance | Quantité |
| :--- | ---: | ---: |
| Reinforced Hull Plate | 50 % | 1 |
| L’une des 8 [roquettes](/wiki/06-Items/Rockets.md) achetées avec des crédits, tirée au hasard | 100 % | 5–10 |
| L’un de Advanced Plasma et Siphon Battery, tiré au hasard | 100 % | 500–1 000 |

### Pirate Scout {#pirate-scout}

Base : Kitefin, avec 50 % de coque, de bouclier et de dégâts ; la vitesse et la portée sont celles du vaisseau d’origine.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | 12 000 | 18 000 | 24 000 |
| Bouclier | 9 818 | 14 727 | 19 636 |
| Dégâts des lasers (une salve par seconde) | 98 | 147 | 196 |
| Vitesse | 175 | 175 | 175 |
| Portée des lasers | 700 | 700 | 700 |
| Rayon d’aggro | 700 | 700 | 700 |
| Soigne le meneur, chacun, par seconde (coque seulement) | 40 | 60 | 80 |
| Crédits | 800 | 1 600 | 2 400 |
| Thulium | 4 | 8 | 12 |
| Expérience (XP) | 100 | 200 | 300 |
| Honneur | 2 | 4 | 6 |
| Points PvE par élimination | 1 | 1 | 1 |

**Butin** : aucun. L’élimination ne paie que ses crédits, son Thulium, son XP et son honneur.

<!-- pirate-members:end -->
