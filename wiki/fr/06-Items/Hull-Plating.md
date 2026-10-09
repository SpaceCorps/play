<!-- wiki-i18n source: 2bd1925e336e25b6 -->
<!-- wiki-i18n title: Blindage de coque -->
# Blindage de coque {#hull-plating}

<!-- wiki-search: hull plate; hull plate slot; hull plate slots; plate slot; plate; armour; armor; hpl; blindage; emplacement de blindage; plaque de coque -->

L’étude de l’essaim Dormant a montré des progrès dans la technologie du blindage. Grâce à elle, les vaisseaux peuvent améliorer leur coque : le **blindage de coque** est un blindage qui se monte dans un emplacement de plaque de coque d’un vaisseau fabriqué et lui ajoute des points de coque. Ce n’est pas le Hull Plating **Booster** de la page [Boosters](/wiki/06-Items/Boosters.md), un bonus temporaire.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Arbre d’objets {#item-tree}

Ce que fabrique l’Assemblage exige d’abord sa technologie ; pointez un objet pour voir combien de temps sa recherche prend. L’arbre des technologies, le carburant et le boost : [Recherche](/wiki/03-Mechanics/Research.md).

```tree
Hull Plating I | hull-plating, uncommon | buy 5000 Thulium | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating II | hull-plating, rare | craft 2500 Thulium, 300 s | research 86400 s, 86400 science, 25 Dark Matter | 1 Hull Plating I, 150 Ship Fragment, 20 Reinforced Hull Plate, 6 Power Core, 5 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating III | hull-plating, epic | craft 4000 Thulium, 600 s | research 172800 s, 172800 science, 40 Dark Matter | 1 Hull Plating II, 300 Ship Fragment, 40 Reinforced Hull Plate, 12 Power Core, 1 Ancient Control Unit, 8 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings

Hull Plating I => Hull Plating II => Hull Plating III
```
<!-- item-tree:end -->

## Les trois blindages {#the-three-platings}

| Objet | Coque ajoutée | D’où il vient |
| :--- | ---: | :--- |
| **Hull Plating I** | 5 000 | Boutique, 5 000 Thulium |
| **Hull Plating II** | 10 000 | Assemblage, à partir d’un Hull Plating I |
| **Hull Plating III** | 15 000 | Assemblage, à partir d’un Hull Plating II |

Le Hull Plating I s’achète. **Le II et le III sont des améliorations** : l’Assemblage consomme un blindage du palier en dessous (libre dans votre inventaire) et demande du Thulium, des matériaux et des **Dark Matter Plates**, 5 pour le II et 8 pour le III, là où le dernier palier de toute autre pièce d’équipement en demande 3. Chacun a d’abord besoin de sa technologie, dans l’arbre Hull Plating de la page [Recherche](/wiki/03-Mechanics/Research.md#tree-hull-plating) : 1 jour et 25 Dark Matter pour le II, 2 jours et 40 pour le III, en plus de la technologie de la Dark Matter Plate elle-même. L’arbre ci-dessus donne les prix, les matériaux et les durées.

La [Forge](/wiki/06-Items/Forge.md) accepte tous les blindages, et une amélioration conserve le rang de forge du blindage consommé et retire son bonus au sort. Un blindage n’a qu’une seule stat, sa coque, il porte donc un seul bonus, de +2 % à +15 % selon le rang : un Hull Plating III Éternel ajoute jusqu’à 17 250. Les [Enchères](/wiki/03-Mechanics/Auction.md) acceptent les Hull Plating II et III, jamais le Hull Plating I, que vend la boutique.

## Emplacements de blindage {#hull-plate-slots}

Le blindage de coque ne se monte que dans des **emplacements de blindage**, un type d’emplacement à part qu’ont les quatre vaisseaux que vous fabriquez dans l’Assemblage, en plus de leurs emplacements de laser, de générateur, d’extra, de compétence et de drone :

| Vaisseau | Emplacements de blindage | Un jeu complet de Hull Plating III ajoute |
| :--- | ---: | ---: |
| **Paragon** | 5 | 75 000 |
| **Storm** | 7 | 105 000 |
| **Ironclad** | 15 | 225 000 |
| **Wraith** | 9 | 135 000 |

- **Tous verrouillés au départ.** Un emplacement s’ouvre quand vous le recherchez dans le Skylab : une technologie par emplacement, 1 heure et 10 Dark Matter, dans l’ordre à partir du premier. La vue [Recherche](/wiki/03-Mechanics/Research.md#ship-technologies) montre les emplacements d’un vaisseau sous la forme d’une seule carte avec un point par emplacement.
- **Un type de vaisseau, pas un seul vaisseau.** Les emplacements que vous avez ouverts pour le Paragon sont ouverts aussi sur chaque design du Paragon ([Designs de vaisseaux](/wiki/03-Mechanics/Ship-Designs.md)). Une technologie est à vous pour toujours : la réinitialisation la conserve.
- **Les deux configurations les partagent.** Les blindages appartiennent au vaisseau : changer de configuration les laisse en place, et le hangar montre les mêmes dans les deux.
- **Tout mélange.** Un emplacement accepte n’importe quel blindage de coque, et deux identiques ne posent aucun problème.
- **Votre part de coque reste la même.** Monter ou retirer un blindage conserve la part de coque que vous avez, donc un blindage ne vous soigne jamais et ne vous blesse jamais.
- **Comme tout équipement**, les blindages se montent et se retirent au hangar, ou dans sa fenêtre depuis une zone sûre, jamais sur le terrain. Un emplacement que vous n’avez pas recherché refuse un blindage.

Au hangar, la carte **Blindage de coque** montre les emplacements. Un emplacement ouvert accepte un blindage par glisser-déposer, comme tous les emplacements ; un emplacement verrouillé affiche un cadenas, et un clic ouvre la recherche du Skylab. Une tuile à côté des autres stats additionne ce que donnent les blindages montés.

## Comment la coque s’additionne {#how-the-hull-adds-up}

Un blindage ajoute sa coque à celle du vaisseau, et le hangar et la fenêtre du vaisseau affichent le nombre plus grand. La coque du vaisseau plus ses blindages passe ensuite par les mêmes multiplicateurs qu’avant : un [Hull Plating Booster](/wiki/06-Items/Boosters.md) et la [formation de drones](/wiki/03-Mechanics/Formations.md) que vous portez. Un design qui change la coque (le BUCKY en a 25 % de plus) change la coque propre du vaisseau, et les blindages s’y ajoutent.

## Hull Plating ou Hull Plating Booster ? {#hull-plating-or-booster}

Deux choses portent le même nom. Le **blindage de coque** (cette page) est une armure : une plaque qui se place dans un emplacement de blindage d’un vaisseau fabriqué et ajoute sa coque tant qu’elle est montée. Le **Hull Plating Booster** est un bonus temporaire de la page [Boosters](/wiki/06-Items/Boosters.md), +10 % de points de coque maximum pendant 10 heures sur le vaisseau que vous pilotez, et il n’y a rien à monter. Ils s’additionnent : les blindages viennent d’abord, et les 10 % du Booster sont pris sur le total.
