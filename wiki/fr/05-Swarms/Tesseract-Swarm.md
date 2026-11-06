<!-- wiki-i18n source: 554085379d2ae5df -->
<!-- wiki-i18n title: Essaim Tesseract -->
# Essaim Tesseract {#tesseract-swarm}

L’essaim Tesseract est un unique et immense vaisseau-mère, le **Tesseract**, et les **Facets** qu’il lâche tant qu’il est touché. Le Tesseract vit à un endroit fixe du [secteur dangereux](/wiki/01-General/Danger-Sectors.md) `DS-4`, n’a aucune arme à lui et ne quitte jamais son secteur. Il est fait pour un très grand groupe des pilotes les plus forts : sa coque et son bouclier dépassent de loin un Crystalys, et il se répare tout seul dès qu’on le laisse tranquille. Les secteurs dangereux sont des secteurs PvP : le combat peut donc attirer des rivaux en plus des Facets.

## D’un coup d’œil {#at-a-glance}

<!-- tesseract-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Où** : Le secteur dangereux `DS-4`
- **Combien** : Un dans chaque monde
- **Apparaît** : Du jour 4 de la saison jusqu’à la réinitialisation (Bêta et Gamma : dès le jour 1 de la saison)
- **Meneur** : Tesseract
- **Position** : À moins de 2 500 unités du point 27 000, 5 000 de la carte du secteur
- **Régénération** : 125 000 PV par seconde dans Alpha, d’abord la coque puis le bouclier, une fois 5 s écoulées sans dégâts
- **Suivants** : Jusqu’à 100 × Facet, 20 de plus toutes les 5 s tant que le meneur est touché
- **Arrivée des suivants** : Seulement si le meneur a été touché depuis moins de 5 s, à moins de 400 unités de lui
- **Chasseurs** : Chaque Facet vole par trajets à lui autour du meneur, à moins de 1 800 unités de celui-ci, et ne poursuit personne. Il tire sur le pilote le plus proche qui a touché le meneur quand ce pilote est à sa portée. Sans cible, il continue de voler autour du meneur et part 20 s après le dernier coup
- **Meneur détruit** : Les suivants partent 1 min après la destruction du meneur, qu’ils attaquent ou non
- **Revient** : 30 min après la destruction du meneur, dans le même secteur
- **Annonces** : Les pilotes du secteur sont prévenus quand le meneur apparaît et quand il est détruit. Ce sont des lignes Système : elles apparaissent dans l’onglet **Système** du chat, avec un compteur de lignes non lues, et pas dans **Global** ni **Local**. Le fil des éliminations nomme le pilote à qui l’élimination est créditée.

<!-- tesseract-glance:end -->

## Les membres {#the-members}

- **Tesseract** : un vaisseau-mère en forme de cube, bien plus grand qu’un Crystalys, en fer forgé sombre aux veines de braise lumineuses, avec son nom au-dessus. Une baie de sa paroi avant s’ouvre quand il est touché, et un cube lumineux tourne dans une cage sur son toit. Il est passif : il dérive lentement dans sa zone tant que personne ne le blesse, et dès qu’un pilote le touche, il s’immobilise et tient sa position. Il ne tire pas et ne poursuit personne ; sa défense, c’est sa taille, sa réparation et les Facets qu’il lâche.
- **Facet** : un petit vaisseau rapide du même fer sombre, aux arêtes de braise, avec une lentille lumineuse au nez et deux plaques d’aile flottantes. Il n’existe que tant que le Tesseract est touché. Il ne poursuit personne : il reste près du Tesseract, vole par petits trajets à lui vers des endroits pris au hasard tout autour, et tire sur le pilote le plus proche qui a touché le Tesseract dès que l’un d’eux est à sa portée. Il part quand on laisse le Tesseract tranquille. Il est plus rapide que n’importe quel vaisseau : fuir l’essaim ne sert à rien, mais un pilote qui reste loin du Tesseract n’est jamais pris pour cible.

## Le déroulement du combat {#how-the-fight-goes}

- **Venez en très grand groupe et frappez ensemble.** La coque et le bouclier du Tesseract forment une réserve de millions de points ; le combat est long même pour un grand groupe de vaisseaux puissants, et le paiement est réparti selon les dégâts : chaque pilote présent compte.
- **Ne le laissez jamais tranquille.** Quand personne ne l’a blessé pendant le temps indiqué dans la liste *D’un coup d’œil*, il répare sa coque puis son bouclier à cette vitesse ; une pause de quelques secondes peut défaire une longue minute de travail. Un Tesseract entièrement réparé oublie qui l’a blessé : le paiement et la caisse suivent les dégâts du combat qui le détruit.
- **Chaque coup appelle les Facets.** Tant que le Tesseract est touché, un groupe de Facets arrive près de lui toutes les quelques secondes, jusqu’au plafond de la liste *D’un coup d’œil*. Tant que personne ne le touche, aucun ne vient, et ceux qui sont déjà là attendent puis partent.
- **Les Facets volent tout autour du Tesseract et tirent sur ceux qui sont à leur portée.** Ils ne traquent ni celui qui inflige le plus de dégâts ni aucun pilote en particulier : chaque Facet vole par petits trajets à lui vers des endroits pris au hasard dans un large anneau autour du Tesseract, dans toutes les directions, et dès qu’un pilote qui a touché le Tesseract est à sa portée, il tire sur le plus proche d’entre eux. Un groupe qui reste serré est à portée de moins de Facets à la fois, et se partage leur tir, contrairement à un groupe réparti tout autour du Tesseract. Un Facet a peu de coque et de bouclier, et en abattre un ne paie rien, mais cela retire une salve aux pilotes qui sont près de lui. Un pilote qui n’a pas touché le Tesseract n’est pas leur cible.
- **Un pilote qui reste assez loin est laissé tranquille.** Les Facets ne s’éloignent jamais du Tesseract au-delà de la distance de la liste *D’un coup d’œil* ; un pilote qui reste au-delà de cette distance et de la portée du laser d’un Facet n’est pas pris pour cible, quels que soient les dégâts qu’il a infligés. Un Facet sans personne sur qui tirer continue de voler autour du Tesseract et part quand on laisse le Tesseract tranquille.
- **Beta et Gamma sont plus durs.** Les essaims de ces mondes sont plus forts ([Mondes](/wiki/05-Swarms/Swarms.md#the-worlds)), de même que la réparation du Tesseract et la salve de chaque Facet.
- **Les secteurs dangereux sont PvP.** Un rival peut attaquer le groupe en plein combat et attendre la caisse : elle est au pilote qui a infligé le plus de dégâts (et à son clan) pendant 30 secondes, puis à n’importe qui ([Cargaison](/wiki/03-Mechanics/Cargo.md)). Ne venez pas seul.
- **Le Tesseract revient** après le temps de la liste *D’un coup d’œil*, à pleine force, à son emplacement.

## Récompenses et butin {#rewards-and-drops}

Le Tesseract paie pour le combat qu’il est : autant que de nombreux Crystalys réunis, et davantage, pour les dégâts qu’il encaisse, qu’un Crystalys, l’alien le mieux payé. Le paiement est réparti selon les dégâts entre les pilotes qui l’ont combattu ([comment paie l’élimination d’un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Sa caisse revient au pilote qui a infligé le plus de dégâts et contient des Power Cores et des Ancient Control Units, et de temps en temps de la Dark Matter. Les plaques de coque n’y sont pas : chaque pilote que l’élimination paie reçoit sa propre [caisse privée](/wiki/03-Mechanics/Cargo.md#private-boxes) de plaques, que lui seul voit et peut prendre, pendant 10 minutes. Elle est tirée pour sa part des dégâts, comme le butin d’un [Clan Warden](/wiki/03-Mechanics/Clans.md#warden-pay-and-loot) : celui qui a infligé un cinquième des dégâts reçoit environ un cinquième des quantités du tableau, et dans un groupe chaque pilote reçoit sa part de celle du groupe, comme le paiement est partagé. Les Facets ne paient rien, ne laissent rien et ne rapportent aucun point PvE : les tuer n’est pas une façon de farmer.

## Les valeurs {#the-numbers}

Les valeurs des vaisseaux de l’essaim dans les trois mondes ([Mondes](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- tesseract-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Tesseract

Base : Crystalys, avec 625 % de sa coque ; sans arme, avec un bouclier et une vitesse qui lui sont propres.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | 1 600 000 | 2 400 000 | 3 200 000 |
| Bouclier | 1 200 000 | 1 800 000 | 2 400 000 |
| Dégâts des lasers (une salve par seconde) | aucun | aucun | aucun |
| Vitesse | 30 | 30 | 30 |
| Portée des lasers | – | – | – |
| Rayon d’aggro | seulement si attaqué | seulement si attaqué | seulement si attaqué |
| Répare, par seconde, après 5 s sans dégâts (coque, puis bouclier) | 125 000 | 187 500 | 250 000 |
| Crédits | 900 000 | 1 800 000 | 2 700 000 |
| Thulium | 2 400 | 4 800 | 7 200 |
| Expérience (XP) | 144 000 | 288 000 | 432 000 |
| Honneur | 624 | 1 248 | 1 872 |
| Points PvE par élimination | 42 | 42 | 42 |

**Butin** : une caisse, pour le pilote qui a infligé le plus de dégâts.

| Objet | Chance | Quantité |
| :--- | ---: | ---: |
| Power Core | 70 % | 1–2 |
| Ancient Control Unit | 35 % | 1 |
| Dark Matter | 2,5 % | 1 |

**Butin pour chaque pilote que l’élimination paie** : une caisse de plus pour chacun, rien que pour lui, avec sa part de ces quantités.

| Objet | Chance | Quantité |
| :--- | ---: | ---: |
| Reinforced Hull Plate | 100 % | 1–2 |
| Velkonite Reinforced Plate | 60 % | 3–6 |
| Orvium Reinforced Plate | 40 % | 1–2 |

### Facet

Base : Seeker, avec 2 500 % de sa coque et 309 % de ses dégâts laser ; le bouclier, la vitesse et la portée lui sont propres.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | 20 000 | 30 000 | 40 000 |
| Bouclier | 16 000 | 24 000 | 32 000 |
| Dégâts des lasers (une salve par seconde) | 556 | 834 | 1 112 |
| Vitesse | 750 | 750 | 750 |
| Portée des lasers | 600 | 600 | 600 |
| Rayon d’aggro | seulement si attaqué | seulement si attaqué | seulement si attaqué |
| Crédits | 0 | 0 | 0 |
| Thulium | 0 | 0 | 0 |
| Expérience (XP) | 0 | 0 | 0 |
| Honneur | 0 | 0 | 0 |
| Points PvE par élimination | 0 | 0 | 0 |

**Butin** : aucun. L’élimination ne paie rien.

<!-- tesseract-members:end -->
