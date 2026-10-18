<!-- wiki-i18n source: 574007c029169684 -->
<!-- wiki-i18n title: Boucliers -->
# Boucliers et défense {#shields-defense}

Les modules défensifs fournissent de la capacité de bouclier, absorbent les dégâts et rechargent vos défenses.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Arbre d’objets {#item-tree}

Ce que fabrique l’Assemblage exige d’abord sa technologie ; pointez un objet pour voir combien de temps sa recherche prend. L’arbre des technologies, le carburant et le boost : [Recherche](/wiki/03-Mechanics/Research.md).

```tree
Light Shield Core | shield, shoddy | buy 20000 Credits | /wiki/06-Items/Shields.md#shield-cores
Basic Shield Core | shield, common | buy 2000 Thulium | /wiki/06-Items/Shields.md#shield-cores
Heavy Shield Core | shield, rare | craft 4000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 12 Reinforced Hull Plate, 2 Power Core, 1 Ancient Control Unit, 30 Cataclysite, 4 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cores
Adaptive Core I | hybrid-generator, shoddy | buy 100000 Credits | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core II | hybrid-generator, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Adaptive Core I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core III | hybrid-generator, rare | craft 4000 Thulium, 90 s | research 10800 s, 10800 science | 1 Adaptive Core II, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Absorption Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell II | shield-cell, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 50 Ship Fragment, 8 Reinforced Hull Plate, 20 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 50 Ship Fragment, 8 Reinforced Hull Plate, 20 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 50 Ship Fragment, 10 Reinforced Hull Plate, 2 Power Core, 25 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 50 Ship Fragment, 10 Reinforced Hull Plate, 2 Power Core, 25 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 5000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 12 Reinforced Hull Plate, 2 Power Core, 1 Ancient Control Unit, 30 Cataclysite, 4 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 5000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 12 Reinforced Hull Plate, 2 Power Core, 1 Ancient Control Unit, 30 Cataclysite, 4 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells

Light Shield Core -> Basic Shield Core => Heavy Shield Core
Adaptive Core I => Adaptive Core II => Adaptive Core III
Absorption Shield Cell I => Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell I => Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```
<!-- item-tree:end -->

## Boucliers (Shield Cores) {#shield-cores}

Équipez des boucliers pour générer des barrières défensives actives, dans les emplacements de générateur de votre vaisseau ou sur vos [drones](/wiki/03-Mechanics/Drones.md) (l’emplacement d’un drone compte comme un emplacement principal). Notez que les boucliers lourds pèsent sur votre vitesse. Un bouclier placé dans un **emplacement de compétence** vous donne à la place le **Shield Surge** de la colonne Effet spécial, une réparation du bouclier sur dix secondes, et n’ajoute aucun bouclier propre (voir [Compétences](/wiki/03-Mechanics/Abilities.md)).

| Nom | Rareté | Capacité | Vitesse de recharge | Absorption | Bouclier (%) | Vitesse (%) | Empl. cellule | Effet spécial | Coût |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Light Shield Core** | Médiocre | 10 000 | 333/s | 45 % | +5 % | -1 % | 1 | Shield Surge I | 20 000 crédits |
| **Basic Shield Core** | Commun | 15 000 | 500/s | 48 % | +10 % | -3 % | 2 | Shield Surge II | 2 000 Thulium |
| **Heavy Shield Core** | Rare | 25 000 | 833/s | 50 % | +20 % | -5 % | 3 | Shield Surge III | À fabriquer |

Le **Heavy Shield Core** se fabrique à l’[Assemblage](/wiki/06-Items/Overview.md#upgrading-modules) à partir d’un Basic Shield Core, avec 4 000 Thulium, 30 Cataclysite, 12 Reinforced Hull Plates, 2 Power Cores, 1 Ancient Control Unit et 4 Dark Matter Plates ([Dark Matter et Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)). Il garde le rang d’enchantement et les bonus du bouclier qu’il consomme ([Améliorations de modules](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Retirez d’abord le Basic Shield Core de votre vaisseau (et sortez-en les cellules) : un bouclier installé ou qui contient des cellules n’est pas consommé.

L’**absorption** est la part de chaque tir que prennent vos boucliers ; la coque encaisse le reste. Un bouclier seul donne **45 à 50 %**, et ses cellules ajoutent le reste : le meilleur bouclier avec les meilleures cellules (un Heavy Shield Core avec trois Absorption Shield Cell IV) donne **80 %**, le maximum qu’un vaisseau possède d’emblée. Trois bonus permanents s’y ajoutent : le Shield Absorbance Boost de la Boutique de saison (+0,1 point par niveau, 100 niveaux, 25 points de réinitialisation chacun), les bonus d’absorption de la Forge et la recherche Pilote Field Theory (+2, +3 ou +5 points). Les sources actuelles de points de réinitialisation (1 105 au total à leur plafond, conservés d’une réinitialisation à l’autre ; d’autres sources sont prévues) achètent 44 de ces 100 niveaux (+4,4 points), ce qui, avec un ensemble Éternel entièrement forgé, donne environ **95 %**, et environ **99 %** avec Field Theory III. La stat n’est cependant pas plafonnée à 100 % : la *pénétration de bouclier* d’un attaquant en est retranchée, si bien que ce qu’un vaisseau a au-dessus de 100 % est sa marge face à la pénétration. Voir [Mécaniques des boucliers](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-).

---

## Générateurs hybrides (cœurs adaptatifs) {#hybrid-generators-adaptive-cores-}

Les cœurs adaptatifs font office de générateurs hybrides, combinant les capacités de bouclier et de vitesse. Ils acceptent à la fois des propulseurs et des cellules de bouclier dans leurs emplacements (un module par emplacement, de l’un ou l’autre type). Leur bonus de bouclier et leur bonus de vitesse comptent comme ceux d’un bouclier ou d’un moteur (les quatre meilleurs, multipliés par la part de l’emplacement). Ils n’ont pas d’absorption : ils ne changent pas l’absorption de votre vaisseau, et les cellules qu’ils contiennent n’ajoutent que de la capacité et de la recharge. Seuls les boucliers encaissent une part d’un tir, les cellules d’un cœur adaptatif demandent donc aussi un bouclier sur le vaisseau.

| Nom | Rareté | Bonus de bouclier (%) | Bonus de vitesse (%) | Emplacements | Effet spécial | Coût |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **Adaptive Core I** | Médiocre | +4 % | +2,4 % | 1 | — | 100 000 crédits |
| **Adaptive Core II** | Commun | +6,4 % | +3,2 % | 2 | — | À fabriquer |
| **Adaptive Core III** | Rare | +8 % | +4 % | 3 | — | À fabriquer |

L’**Adaptive Core II** se fabrique à l’[Assemblage](/wiki/06-Items/Overview.md#upgrading-modules) à partir d’un Adaptive Core I, avec 2 000 Thulium, 60 Ship Fragments, 1 Power Core et 4 Velkonite Reinforced Plates. L’**Adaptive Core III** s’y fabrique à partir d’un Adaptive Core II, avec 4 000 Thulium, 110 Ship Fragments, 5 Power Cores, 1 Ancient Control Unit et 4 Dark Matter Plates ([Dark Matter et Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)). Chacun garde le rang d’enchantement et les bonus du cœur qu’il consomme ([Améliorations de modules](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Retirez d’abord de votre vaisseau le cœur à consommer (et sortez-en les propulseurs et les cellules) : un cœur installé ou qui contient des modules n’est pas consommé.

---

## Cellules de bouclier {#shield-cells}

Les cellules de bouclier s’installent dans des boucliers ou des cœurs adaptatifs (autant que le nombre d’emplacements du bouclier ou du cœur) pour le renforcer. Dans un bouclier, elles augmentent aussi son absorption, en points, et avec elle la part de chaque tir que prennent vos boucliers. Il y a deux familles de quatre paliers : les **Capacity Shield Cells** apportent le plus de bouclier et de recharge, les **Absorption Shield Cells** le plus d’absorption (à chaque palier, deux fois plus d’absorption et deux fois moins de bouclier et de recharge que la Capacity du même palier). La Capacity aide un vaisseau dont le bouclier décide du combat, l’Absorption un vaisseau dont c’est la coque. Pour un bouclier dont tous les emplacements sont remplis par une même cellule : un Light Shield Core (1 emplacement) atteint de 47 à 55 %, un Basic Shield Core (2 emplacements) de 52 à 68 % et un Heavy Shield Core (3 emplacements) de 56 à 80 %, des cellules Capacity de palier I aux cellules Absorption de palier IV. Retirer le bouclier, ou le consommer comme donneur d’une fusion de la [Forge](/wiki/06-Items/Forge.md), rend ses cellules à l’inventaire.

| Nom | Rareté | Boost de capacité | Boost de recharge | Boost d’absorption | Coût |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Capacity Shield Cell I** | Médiocre | +3 000 | +250/s | +2 % | 30 000 crédits |
| **Capacity Shield Cell II** | Commun | +6 000 | +500/s | +3 % | À fabriquer |
| **Capacity Shield Cell III** | Rare | +9 000 | +750/s | +4 % | À fabriquer |
| **Capacity Shield Cell IV** | Épique | +12 000 | +1 000/s | +5 % | À fabriquer |
| **Absorption Shield Cell I** | Médiocre | +1 500 | +125/s | +4 % | 30 000 crédits |
| **Absorption Shield Cell II** | Commun | +3 000 | +250/s | +6 % | À fabriquer |
| **Absorption Shield Cell III** | Rare | +4 500 | +375/s | +8 % | À fabriquer |
| **Absorption Shield Cell IV** | Épique | +6 000 | +500/s | +10 % | À fabriquer |

Le palier I de chaque famille se vend 30 000 crédits. Les paliers II à IV se fabriquent à l’[Assemblage](/wiki/06-Items/Overview.md#upgrading-modules), chacun à partir de la cellule de la même famille un palier en dessous (une Capacity Shield Cell II à partir d’une Capacity Shield Cell I, une III à partir d’une II, une IV à partir d’une III), avec du Thulium, du butin et des plaques : 4 Velkonite Reinforced Plates de votre Skylab pour le palier II ou III, et 4 Dark Matter Plates et une Ancient Control Unit pour le palier IV. Une cellule ne change jamais de famille : vous choisissez Capacity ou Absorption en achetant le palier I. La nouvelle cellule garde le rang d’enchantement et les bonus de la cellule qu’elle consomme ([Améliorations de modules](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Les cellules ne vont pas dans un [emplacement de compétence](/wiki/03-Mechanics/Abilities.md) ; elles se placent dans des boucliers et des cœurs adaptatifs.
