<!-- wiki-i18n source: 969bfa836749a15e -->
<!-- wiki-i18n title: Propulsion -->
# Propulsion et vitesse {#propulsion-speed}

Les systèmes de propulsion déterminent la vitesse de déplacement et la maniabilité de votre vaisseau.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Arbre d’objets {#item-tree}

Ce que fabrique l’Assemblage exige d’abord sa technologie ; pointez un objet pour voir combien de temps sa recherche prend. L’arbre des technologies, le carburant et le boost : [Recherche](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | buy 2000 Thulium | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I -> Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Moteurs {#engines}

Les moteurs sont la principale source de poussée de votre vaisseau. Un moteur placé dans un **emplacement de compétence** vous donne à la place l’**Afterburner** de la colonne Effet spécial, un regain de vitesse de dix secondes (plus long avec davantage de moteurs), et n’ajoute aucune poussée propre (voir [Compétences](/wiki/03-Mechanics/Abilities.md)).

| Nom | Rareté | Vitesse de base | Bonus de vitesse (%) | Bonus de bouclier (%) | Emplacements | Effet spécial | Coût |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Médiocre | +2 | +2 % | -2 % | 1 | Afterburner I | 20 000 crédits |
| **Engine II** | Commun | +4 | +4 % | -8 % | 2 | Afterburner II | 2 000 Thulium |
| **Engine III** | Rare | +6 | +5 % | -15 % | 3 | Afterburner III | À fabriquer |

L’**Engine III** se fabrique à l’[Assemblage](/wiki/06-Items/Overview.md#upgrading-modules) à partir d’un Engine II, avec 2 000 Thulium, 60 Ship Fragments, 3 Power Cores et 6 Velkonite Reinforced Plates de votre Skylab. Il garde le rang d’enchantement du moteur qu’il consomme, et ses bonus sont tirés de nouveau ([Améliorations de modules](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Retirez d’abord l’Engine II de votre vaisseau (et sortez-en les propulseurs) : un moteur installé ou qui contient des propulseurs n’est pas consommé.

Le bonus de bouclier des moteurs figure dans les données de l’objet, mais le jeu ne l’a jamais appliqué : les moteurs n’affaiblissent pas vos boucliers, et les cartes d’objet l’omettent.

---

## Propulseurs {#thrusters}

Les propulseurs s’installent dans des moteurs ou des cœurs adaptatifs pour augmenter leur vitesse. Il y a deux familles de quatre paliers : les **Impulse Thrusters** apportent le plus de vitesse fixe et multiplient un peu la vitesse du moteur dans lequel ils sont installés, les **Momentum Thrusters** moins de vitesse fixe, mais ils la multiplient davantage. Un moteur (ou cœur adaptatif) muni de propulseurs produit **sa propre vitesse de base plus les boosts de vitesse fixes des propulseurs, le tout multiplié par les multiplicateurs de vitesse des propulseurs, multipliés entre eux** ([comment la vitesse est calculée](/wiki/03-Mechanics/Speed.md)) : un Engine III avec trois Momentum Thruster IV produit (6 + 3 x 12) x 1,11 x 1,11 x 1,11 = 57,4, avec trois Impulse Thruster IV (6 + 3 x 17) x 1,02 x 1,02 x 1,02 = 60,5, et un Adaptive Core II avec deux Impulse Thruster IV produit (0 + 2 x 17) x 1,02 x 1,02 = 35,4 (29,6 avec deux Momentum Thruster IV).

| Nom | Rareté | Boost de vitesse fixe | Multiplicateur de vitesse | Coût |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Médiocre | +5 | 1,02x | 20 000 crédits |
| **Impulse Thruster II** | Commun | +10 | 1,02x | À fabriquer |
| **Impulse Thruster III** | Rare | +15 | 1,03x | À fabriquer |
| **Impulse Thruster IV** | Épique | +17 | 1,02x | À fabriquer |
| **Momentum Thruster I** | Médiocre | +4 | 1,06x | 20 000 crédits |
| **Momentum Thruster II** | Commun | +8 | 1,07x | À fabriquer |
| **Momentum Thruster III** | Rare | +11 | 1,09x | À fabriquer |
| **Momentum Thruster IV** | Épique | +12 | 1,11x | À fabriquer |

À chaque palier, un Impulse Thruster produit davantage que le Momentum Thruster du même palier, dans un cœur adaptatif comme dans un moteur qui en contient un, deux ou trois (60,5 contre 57,4 avec trois propulseurs de palier IV dans un Engine III, et trois Impulse Thruster IV sont le meilleur Engine III possible). Ce qu’un Momentum Thruster a de plus, c’est un second bonus (ci-dessous).

Le bonus de multiplicateur de vitesse d’un propulseur, issu de la [Forge](/wiki/06-Items/Forge.md), fait croître la part au-dessus de 1 (un bonus de +15 % sur 1,11x donne 1,1265x), et la Forge ne tire aucun bonus sur un multiplicateur de 1,05x ou moins : sur le 1,02x ou 1,03x d’un Impulse Thruster, il vaudrait un millième. Un Impulse Thruster porte un bonus (sa vitesse fixe), un Momentum Thruster deux.

Le palier I de chaque famille se vend 20 000 crédits. Les paliers II à IV se fabriquent à l’[Assemblage](/wiki/06-Items/Overview.md#upgrading-modules), chacun à partir du propulseur de la même famille un palier en dessous (un Impulse Thruster II à partir d’un Impulse Thruster I, un III à partir d’un II, un IV à partir d’un III), avec du Thulium, du butin et des Velkonite Reinforced Plates de votre Skylab (2, 4 et 6 plaques). Un propulseur ne change jamais de famille : vous choisissez Impulse ou Momentum en achetant le palier I. Chacun garde le rang d’enchantement du propulseur qu’il consomme, et ses bonus sont tirés de nouveau ([Améliorations de modules](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Les propulseurs ne vont pas dans un [emplacement de compétence](/wiki/03-Mechanics/Abilities.md) ; ils se placent dans des moteurs et des cœurs adaptatifs.

### Distancer les aliens {#outrunning-aliens}

Les aliens volent à 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) et 230 (Crystalys). Un Ostirion avec un Engine II et deux propulseurs vole à 223,1 avec des Impulse Thruster I : toujours sous le Crystalys, il faut donc un propulseur fabriqué à l’Assemblage pour le distancer (234,0 avec des Impulse Thruster II, 245,5 avec des III, 249,1 avec des IV). Les Momentum Thrusters volent un peu plus bas sur ce vaisseau (222,0 avec des Momentum Thruster I ; 231,8, 240,1 et 243,9 avec des II à IV) : le palier I des deux familles reste sous un Crystalys, et chaque palier fabriqué à l’Assemblage passe au-dessus.
