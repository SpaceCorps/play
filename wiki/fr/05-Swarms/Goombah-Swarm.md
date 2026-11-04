<!-- wiki-i18n source: 7859e3f6a7efac1e -->
<!-- wiki-i18n title: Essaim Goombah -->
# Essaim Goombah {#goombah-swarm}

L’essaim Goombah est un **Boss Goombah** avec ses **Goombah Guards** : un [Goombah](/wiki/04-Aliens/Goombah.md) gigantesque qui ne commence jamais un combat, et de plus petits qui restent près de lui et le soignent. Il vit dans les mêmes secteurs que l’[essaim Phantasm](/wiki/05-Swarms/Phantasm-Swarm.md), `x-3` et `x-4`, et c’est un combat pour un groupe des pilotes les plus forts des secteurs des corporations.

## D’un coup d’œil {#at-a-glance}

<!-- goombah-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Où** : Les secteurs `x-3` et `x-4` de chaque corporation
- **Combien** : Un dans chacun de ces secteurs, 6 dans chaque monde
- **Apparaît** : Du jour 4 de la saison jusqu’à la réinitialisation
- **Meneur** : Boss Goombah
- **Suivants** : Jusqu’à 4 × Goombah Guard, un nouveau toutes les 10 s
- **Les suivants restent** : à 500 unités au plus du meneur
- **Soins** : Chaque Goombah Guard à moins de 600 unités du meneur soigne sa coque, 110 PV par seconde dans Alpha
- **Meneur détruit** : Les suivants partent 30 s après la destruction du meneur, sauf s’ils attaquent
- **Revient** : 5 min après la destruction du meneur, dans le même secteur
- **Annonces** : Les pilotes du secteur sont prévenus quand le meneur apparaît et quand il est détruit. Ce sont des lignes Système : elles apparaissent dans l’onglet **Système** du chat, avec un compteur de lignes non lues, et pas dans **Global** ni **Local**. Le fil des éliminations nomme le pilote à qui l’élimination est créditée.

<!-- goombah-glance:end -->

## Les membres {#the-members}

- **Boss Goombah**: un Goombah plus grand, à la teinte de l’essaim et avec son nom au-dessus, avec une coque, un bouclier et une salve laser qui lui sont propres (les valeurs sont plus bas). Il est passif : il erre jusqu’à ce qu’un pilote le touche, puis poursuit ce pilote et tire sur lui, et les vaisseaux de son essaim proches se joignent au combat. La portée de son arme et sa vitesse sont celles d’un Goombah, et il ne répare jamais sa coque tout seul.
- **Goombah Guard**: un Goombah plus petit à la teinte de l’essaim. Les Guards restent près du boss, se joignent au combat quand un vaisseau d’essaim proche est touché, et chacun qui est près du boss soigne sa coque. Un Guard répare sa propre coque après un repos, comme un Goombah.

## Le déroulement du combat {#how-the-fight-goes}

- **Venez avec un groupe des vaisseaux les plus forts.** Trois pilotes de niveau 8 avec des munitions x2 le détruisent en environ 75 secondes dans Alpha, en perdant au plus un vaisseau ; deux d’entre eux ont besoin de munitions x4, et des pilotes de niveau inférieur n’infligent pas assez de dégâts pour gagner.
- **Tirez sur le boss, pas sur les Guards.** Un Guard tombe en quelques secondes, mais un nouveau arrive aussi souvent que la liste *D’un coup d’œil* l’indique, et ce que les Guards soignent est une petite part de ce qu’inflige un groupe : les laisser tranquilles coûte un peu de temps, leur donner la chasse en coûte davantage.
- **Beta et Gamma sont plus durs.** Les essaims de ces mondes sont plus forts ([Mondes](/wiki/05-Swarms/Swarms.md#the-worlds)), ils demandent donc plus de pilotes ou de meilleures munitions.
- **Surveillez le secteur.** `x-4` est un secteur PvP dans Alpha, et `x-3` et `x-4` le sont dans Beta et Gamma ([Mondes](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)) : un rival peut se joindre au combat ou attendre la caisse. Gardez un vaisseau du groupe en veille.
- **Le boss revient** après le délai de la liste *D’un coup d’œil*, en pleine force, dans le même secteur, et ses Guards arrivent l’un après l’autre.

## Récompenses et butin {#rewards-and-drops}

Le Boss Goombah paie pour le combat qu’il est : une minute à le combattre paie plus qu’une minute à combattre un Goombah, l’alien le mieux payé de ces secteurs. Le paiement est réparti selon les dégâts entre les pilotes qui l’ont combattu ([comment paie l’élimination d’un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Sa caisse revient au pilote qui a infligé le plus de dégâts et contient le butin propre d’un Goombah plusieurs fois (Cataclysite, Quorvium, Power Cores, Reinforced Hull Plates et Ship Fragments), avec des munitions et des roquettes. Les Guards paient peu et ne laissent rien ; les tuer n’est pas une façon de farmer, car ils reviennent avec le boss.

## Les valeurs {#the-numbers}

Les valeurs des vaisseaux de l’essaim dans les trois mondes ([Mondes](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- goombah-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Goombah

Base : Goombah, avec 400 % de sa coque et 100 % de ses dégâts laser ; la vitesse et la portée sont celles du vaisseau d’origine.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | 128 000 | 192 000 | 256 000 |
| Bouclier | 192 000 | 288 000 | 384 000 |
| Dégâts des lasers (une salve par seconde) | 3 000 | 4 500 | 6 000 |
| Vitesse | 180 | 180 | 180 |
| Portée des lasers | 800 | 800 | 800 |
| Rayon d’aggro | seulement si attaqué | seulement si attaqué | seulement si attaqué |
| Crédits | 120 000 | 240 000 | 360 000 |
| Thulium | 600 | 1 200 | 1 800 |
| Expérience (XP) | 24 000 | 48 000 | 72 000 |
| Honneur | 192 | 384 | 576 |
| Points PvE par élimination | 14 | 14 | 14 |

**Butin** : une caisse, pour le pilote qui a infligé le plus de dégâts.

| Objet | Chance | Quantité |
| :--- | ---: | ---: |
| Ship Fragment | 100 % à chacun des 8 tirages | 3 |
| Reinforced Hull Plate | 60 % à chacun des 8 tirages | 1 |
| Power Core | 25 % à chacun des 8 tirages | 1 |
| Cataclysite | 100 % à chacun des 8 tirages | 4 |
| Quorvium | 100 % à chacun des 8 tirages | 2–4 |
| Advanced Plasma | 100 % | 100–200 |
| Ultra Core | 100 % | 100–200 |
| L’une des 8 [roquettes](/wiki/06-Items/Rockets.md) achetées avec des crédits, tirée au hasard | 100 % | 6–10 |

### Goombah Guard

Base : Goombah, avec 20 % de coque, de bouclier et de dégâts ; la vitesse et la portée sont celles du vaisseau d’origine.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | 6 400 | 9 600 | 12 800 |
| Bouclier | 9 600 | 14 400 | 19 200 |
| Dégâts des lasers (une salve par seconde) | 600 | 900 | 1 200 |
| Vitesse | 180 | 180 | 180 |
| Portée des lasers | 800 | 800 | 800 |
| Rayon d’aggro | seulement si attaqué | seulement si attaqué | seulement si attaqué |
| Soigne le meneur, chacun, par seconde (coque seulement) | 110 | 165 | 220 |
| Crédits | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Expérience (XP) | 12 | 24 | 36 |
| Honneur | 1 | 2 | 3 |
| Points PvE par élimination | 3 | 3 | 3 |

**Butin** : aucun. L’élimination ne paie que ses crédits, son Thulium, son XP et son honneur.

<!-- goombah-members:end -->
