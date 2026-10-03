<!-- wiki-i18n source: 897dab3210b8f84a -->
<!-- wiki-i18n title: Vitesse -->
# Calcul de la vitesse {#speed-calculation}

La vitesse détermine la rapidité avec laquelle votre vaisseau se déplace sur la carte spatiale : elle vous permet de poursuivre des cibles, de fuir un combat ou de traverser des zones.

## La formule de vitesse {#the-speed-formula}

La vitesse finale de votre vaisseau est calculée sur le serveur selon la formule suivante :

\[\text{Vitesse finale} = (\text{Vitesse de base du vaisseau} + \text{Vitesse totale des moteurs}) \times (1,0 + \text{Pourcentage total de bonus de vitesse})\]

### 1. Vitesse effective des moteurs {#1-effective-engine-speed}

Chaque moteur équipé génère de la vitesse, et chaque cœur adaptatif qui contient des propulseurs aussi. Si des propulseurs sont installés dans le moteur, sa vitesse est modifiée :

\[\text{Vitesse du moteur} = (\text{Vitesse de base du moteur} + \text{Bonus fixe des propulseurs}) \times \text{Multiplicateur des propulseurs}\]

- **Bonus fixe des propulseurs** : la somme de tous les ajouts fixes de vitesse des propulseurs (par ex. l’Impulse Thruster III donne `+15` de vitesse).
- **Multiplicateur des propulseurs** : le produit des multiplicateurs de vitesse de tous les propulseurs installés dans ce moteur (par ex. le Momentum Thruster III vaut `1.13`, soit `+13%`, l’Impulse Thruster III `1.03`, soit `+3%`). Il multiplie tout ce que produit le moteur : sa vitesse de base propre et les bonus fixes des propulseurs. Un cœur adaptatif n’a pas de vitesse de base propre, et les bonus fixes de ses propulseurs sont multipliés tout de même.

Un Engine III (vitesse de base 6) avec trois Momentum Thruster IV (`+12`, `1.14`) produit (6 + 3 x 12) x 1,14 x 1,14 x 1,14 = 62,2, et avec trois Impulse Thruster IV (`+17`, `1.02`) (6 + 3 x 17) x 1,02 x 1,02 x 1,02 = 60,5. Un bonus de la Forge sur le multiplicateur d’un propulseur fait croître la part au-dessus de 1 : +15 % sur `1.14` donne `1.161`.

### 2. Rendements décroissants (efficacité marginale) {#2-diminishing-returns-marginal-efficiency-}

Pour empêcher les joueurs d’empiler un nombre infini de moteurs et d’obtenir une vitesse infinie, une courbe de **rendements décroissants (efficacité marginale)** est appliquée. Tous les moteurs sont triés selon leur contribution à la vitesse et traités dans l’ordre. Les cœurs adaptatifs (hybrides) et les cœurs de bouclier sont classés de la même manière, chaque type dans un groupe à part : un vaisseau qui a à la fois des moteurs et des cœurs adaptatifs a donc ses quatre premiers rangs pour chacun des deux types :

| Rang du moteur | Multiplicateur d’efficacité |
| :---: | :--- |
| **1er à 4e** | **100 %** (1,0) |
| **5e** | **85 %** (0,85) |
| **6e** | **70 %** (0,70) |
| **7e** | **55 %** (0,55) |
| **8e et suivants** | **25 %** (0,25) |

De plus, la vitesse du moteur est multipliée par l’efficacité de son emplacement (principal : 100 %, de soutien : 75 %, auxiliaire : 50 %).

### 3. Pourcentage de bonus de vitesse et pénalités des boucliers {#3-speed-bonus-percent-shield-penalties}

Le pourcentage total de bonus de vitesse est la somme de tous les bonus de vitesse des moteurs équipés (et des hybrides), moins les pénalités des boucliers équipés :

- **Bonus de vitesse des moteurs** : les moteurs ajoutent des pourcentages de vitesse positifs (par ex. l’Engine III ajoute `+5%`).
- **Pénalité de vitesse des boucliers** : les boucliers lourds alourdissent votre vaisseau et ajoutent des pourcentages de vitesse négatifs (par ex. le Heavy Shield Core ajoute `-5%` de vitesse).
- **Pondération selon l’emplacement** : ces bonus et pénalités en pourcentage sont eux aussi pondérés par l’efficacité de l’emplacement où l’objet est équipé. Un bouclier installé sur l’un de vos drones vous ralentit comme un bouclier placé dans un emplacement principal.
- **Jamais sous zéro** : quel que soit le nombre de boucliers que vous portez, votre vitesse ne descend pas sous 0.
