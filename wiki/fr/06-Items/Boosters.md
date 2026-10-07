<!-- wiki-i18n source: 630505c843ae163b -->
<!-- wiki-i18n title: Boosters -->
# Boosters

<!-- wiki-search: damage amp; damage amp ii; shield wall; shield wall ii; hull plating; hull plating ii; shield regen; experience kit; honor beacon; resource magnet; loot luck -->

Les boosters apportent des modifications temporaires de stats qui renforcent les capacités de combat, de défense, de progression en niveau et de collecte de ressources de votre vaisseau.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Arbre d’objets {#item-tree}

Ce que fabrique l’Assemblage exige d’abord sa technologie ; pointez un objet pour voir combien de temps sa recherche prend. L’arbre des technologies, le carburant et le boost : [Recherche](/wiki/03-Mechanics/Research.md).

```tree
Experience Booster | booster, common | buy 8000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Honor Booster | booster, common | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Laser Damage Booster 2 | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster 2 | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster 2 | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Regen Booster | booster, rare | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster 1 | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster 1 | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Resource Magnet Booster | booster, rare | buy 18000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Laser Damage Booster 1 | booster, rare | buy 20000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Loot Luck Booster | booster, legendary | buy 30000 Thulium | /wiki/06-Items/Boosters.md#active-boosters

Shield Wall Booster 1 -> Shield Wall Booster 2
Hull Plating Booster 1 -> Hull Plating Booster 2
Laser Damage Booster 1 -> Laser Damage Booster 2
```
<!-- item-tree:end -->

## Règles de cumul {#stacking-rules}

Les boosters reposent sur un système de cumul additif :
1. **Les pourcentages de bonus s’additionnent** : si vous achetez deux boosters différents qui donnent chacun +10 % de dégâts laser, vous obtenez un bonus total de **+20 % de dégâts laser**.
2. **Les durées se cumulent de façon multiplicative** : acheter plusieurs fois le _même_ booster prolonge sa durée active. Les minuteries de boosters _différents_ tournent en parallèle.
3. **Vue des minuteries** : les boosters actifs s’affichent dans le HUD, dans la fenêtre Boosters, avec le total des bonus actifs regroupés et la prochaine expiration.

---

## Boosters actifs {#active-boosters}

Chaque booster dure **10 heures** de base et s’active dès l’achat, la réception ou la collecte. Les trois boosters **de second palier** (Laser Damage Booster 2, Shield Wall Booster 2 et Hull Plating Booster 2) ne sont pas vendus : vous recherchez leur technologie dans le Skylab ([Recherche](/wiki/03-Mechanics/Research.md)), puis vous les fabriquez à l’Assemblage, et en collecter un lance ses 10 heures aussitôt, comme à l’achat.

| Nom | Rareté | Effet de base (10 heures) | Prix (Thulium) |
| :--- | :--- | :--- | :--- |
| **Laser Damage Booster 1** | Rare | +10 % de dégâts laser | 20 000 |
| **Laser Damage Booster 2** | Rare | +10 % de dégâts laser | Assemblage : 20 000 |
| **Shield Wall Booster 1** | Rare | +25 % de capacité du bouclier (points de bouclier maximum) | 15 000 |
| **Shield Wall Booster 2** | Rare | +25 % de capacité du bouclier (points de bouclier maximum) | Assemblage : 15 000 |
| **Hull Plating Booster 1** | Rare | +10 % de points de vie maximum | 15 000 |
| **Hull Plating Booster 2** | Rare | +10 % de points de vie maximum | Assemblage : 15 000 |
| **Shield Regen Booster** | Rare | +25 % de vitesse de recharge du bouclier (points de bouclier rendus par seconde) | 10 000 |
| **Experience Booster** | Commun | +20 % de gain d’expérience | 8 000 |
| **Honor Booster** | Commun | +20 % de gain de points d’honneur | 10 000 |
| **Resource Magnet Booster** | Rare | +25 % de rendement des caisses de cargaison | 18 000 |
| **Loot Luck Booster** | Légendaire | +5 % de chance de butin rare sur les PNJ | 30 000 |

> [!NOTE]
> **Booster ou ampli ?** Ce sont deux choses différentes. Tout booster a **Booster** dans son nom, tourne sur un minuteur et n’a rien à installer : le **Laser Damage Booster 1** et le **Laser Damage Booster 2** donnent +10 % de dégâts laser pendant 10 heures, en boutique ou à l’Assemblage. Le **Damage Amp**, le **Crit Amp** et le **Penetration Amp** (paliers I à IV) sont des amplificateurs laser : des modules qu’on installe dans l’emplacement d’ampli d’un laser, sans minuteur ([Lasers et munitions](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-)). Avant 0.4.12, les boosters s’appelaient Damage Amp et Damage Amp II, Shield Wall et Shield Wall II, Hull Plating et Hull Plating II, Shield Regen, Experience Kit, Honor Beacon, Resource Magnet et Loot Luck ; ceux que vous aviez en cours ont continué sous leurs nouveaux noms.

---

## Bonus de bouclier : trois types {#shield-boosts-three-kinds}

Les boucliers ont trois stats distinctes, et chaque bonus de bouclier en augmente une seule. La fenêtre Boosters les sépare, avec une icône et un total pour chacune :

| Type | Définition | Bonus qui l’augmentent |
| :--- | :--- | :--- |
| **Capacité bouclier** | Vos points de bouclier maximum | Shield Wall Booster 1, Shield Wall Booster 2, le bonus permanent **Shield Capacity Boost** (Boutique de saison) |
| **Absorption bouclier** | La part de chaque tir que prennent vos boucliers (la coque encaisse le reste) ; elle peut dépasser 100 % | Le bonus permanent **Shield Absorbance Boost** (Boutique de saison) : +0,1 point par niveau pour 25 PR, +10 points au maximum. Aucun booster ne l’augmente |
| **Recharge bouclier** | Les points de bouclier rendus par seconde | Shield Regen Booster. Aucun bonus permanent ne l’augmente |

Les bonus d’un même type s’additionnent ; ils ne comptent jamais pour un autre type. Les bonus permanents sont décrits dans [Progression d’une saison à l’autre](/wiki/03-Mechanics/Wipe-Timeline.md) ; les stats elles-mêmes dans [Mécaniques des boucliers](/wiki/03-Mechanics/Shields.md).
