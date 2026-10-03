<!-- wiki-i18n source: b04277deb1c5225f -->
<!-- wiki-i18n title: Propulsion -->
# Propulsion et vitesse {#propulsion-speed}

Les systèmes de propulsion déterminent la vitesse de déplacement et la maniabilité de votre vaisseau.

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

Les propulseurs s’installent dans des moteurs ou des cœurs adaptatifs pour augmenter leur vitesse. Il y a deux familles de quatre paliers : les **Impulse Thrusters** apportent le plus de vitesse fixe et multiplient un peu la vitesse du moteur dans lequel ils sont installés, les **Momentum Thrusters** moins de vitesse fixe, mais ils la multiplient davantage. Un moteur (ou cœur adaptatif) muni de propulseurs produit **sa propre vitesse de base plus les boosts de vitesse fixes des propulseurs, le tout multiplié par les multiplicateurs de vitesse des propulseurs, multipliés entre eux** ([comment la vitesse est calculée](/wiki/03-Mechanics/Speed.md)) : un Engine III avec trois Momentum Thruster IV produit (6 + 3 x 12) x 1,14 x 1,14 x 1,14 = 62,2, avec trois Impulse Thruster IV (6 + 3 x 17) x 1,02 x 1,02 x 1,02 = 60,5, et un Adaptive Core II avec deux Impulse Thruster IV produit (0 + 2 x 17) x 1,02 x 1,02 = 35,4 (31,2 avec deux Momentum Thruster IV).

| Nom | Rareté | Boost de vitesse fixe | Multiplicateur de vitesse | Coût |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Médiocre | +5 | 1,02x | 20 000 crédits |
| **Impulse Thruster II** | Commun | +10 | 1,02x | À fabriquer |
| **Impulse Thruster III** | Rare | +15 | 1,03x | À fabriquer |
| **Impulse Thruster IV** | Épique | +17 | 1,02x | À fabriquer |
| **Momentum Thruster I** | Médiocre | +4 | 1,08x | 20 000 crédits |
| **Momentum Thruster II** | Commun | +8 | 1,10x | À fabriquer |
| **Momentum Thruster III** | Rare | +11 | 1,13x | À fabriquer |
| **Momentum Thruster IV** | Épique | +12 | 1,14x | À fabriquer |

La famille la plus rapide dépend de l’endroit où elle est montée. Les Impulse Thrusters produisent davantage dans un cœur adaptatif et dans un moteur qui en contient un ou deux ; les Momentum Thrusters du même palier produisent davantage dans un Engine III dont les trois emplacements sont remplis (62,2 contre 60,5 au palier IV, et un Impulse Thruster IV avec deux Momentum Thruster IV, 62,3, est le meilleur Engine III possible).

Le bonus de multiplicateur de vitesse d’un propulseur, issu de la [Forge](/wiki/06-Items/Forge.md), fait croître la part au-dessus de 1 (un bonus de +15 % sur 1,14x donne 1,161x), et la Forge ne tire aucun bonus sur un multiplicateur de 1,05x ou moins : sur le 1,02x ou 1,03x d’un Impulse Thruster, il vaudrait un millième. Un Impulse Thruster porte un bonus (sa vitesse fixe), un Momentum Thruster deux.

Le palier I de chaque famille se vend 20 000 crédits. Les paliers II à IV se fabriquent à l’[Assemblage](/wiki/06-Items/Overview.md#upgrading-modules), chacun à partir du propulseur de la même famille un palier en dessous (un Impulse Thruster II à partir d’un Impulse Thruster I, un III à partir d’un II, un IV à partir d’un III), avec du Thulium, du butin et des Velkonite Reinforced Plates de votre Skylab (2, 4 et 6 plaques). Un propulseur ne change jamais de famille : vous choisissez Impulse ou Momentum en achetant le palier I. Chacun garde le rang d’enchantement du propulseur qu’il consomme, et ses bonus sont tirés de nouveau ([Améliorations de modules](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Les propulseurs ne vont pas dans un [emplacement de compétence](/wiki/03-Mechanics/Abilities.md) ; ils se placent dans des moteurs et des cœurs adaptatifs.

### Distancer les aliens {#outrunning-aliens}

Les aliens volent à 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) et 230 (Crystalys). Un Ostirion avec un Engine II et deux propulseurs vole à 223,1 avec des Impulse Thruster I : toujours sous le Crystalys, il faut donc un propulseur fabriqué à l’Assemblage pour le distancer (234,0 avec des Impulse Thruster II, 245,5 avec des III, 249,1 avec des IV). Les Momentum Thrusters volent un peu plus bas sur ce vaisseau (222,6 avec des Momentum Thruster I ; 233,2, 242,5 et 245,8 avec des II à IV) : le palier I des deux familles reste sous un Crystalys, et chaque palier fabriqué à l’Assemblage passe au-dessus.
