<!-- wiki-i18n source: d7e1133b56dbdf93 -->
<!-- wiki-i18n title: Enchères -->
# Enchères {#auction}

Les Enchères sont le marché des pilotes et, en même temps, les lots de chaque heure du jeu, sur une page du menu de la station. Comme la Boutique, c’est une page de la station : vous l’utilisez à quai, pas en vol. Elle a quatre sections. **Marché** montre ce que d’autres pilotes vendent. **Lots** sont les offres du jeu lui-même, une par heure. **Mes annonces** montre ce que vous avez vous-même en vente. **Historique** montre vos ventes, vos achats et les lots que vous avez gagnés, et comment se sont passés vos échanges.

<!-- market-glance:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- Il faut être au **niveau 5** pour utiliser les enchères : pour mettre en vente, acheter et enchérir.
- Une annonce est mise à prix par lot, en crédits entiers ou en Thulium entier (pas les deux), et jamais sous le prix minimum de l’objet. Il n’y a **pas de prix maximum**.
- Un prix en Thulium vaut au moins le prix minimum en crédits divisé par 1 000, arrondi à l’entier supérieur, et seulement pour les objets dont le prix minimum atteint 1 Thulium ou plus. C’est tout ce que fait le taux : **1 Thulium = 1 000 crédits est une règle pour le prix minimum, pas un taux de change.** Rien n’est échangé, aucune valeur n’est affichée, et les crédits et le Thulium ne sont jamais additionnés.
- 80 objets peuvent être mis en vente, et 79 d’entre eux peuvent aussi être mis à prix en Thulium.
- Une annonce dure 24 / 72 / 168 heures, au choix : les durées sont les mêmes à tous les niveaux.
- Le **dépôt** est de 1 % du prix pour chaque période de 24 heures de l’annonce, au minimum 50 crédits ou 1 Thulium. Vous le payez à la mise en vente ; il n’est jamais remboursé, même si vous annulez l’annonce.
- À partir du niveau 10, le dépôt est de 1,5 %.
- La **taxe** est de 5 % du prix. Elle est prélevée sur ce que reçoit le vendeur quand l’annonce se vend.
- Le dépôt et la taxe sont détruits : ils ne vont à personne.
- À partir du jour 28 de la saison et jusqu’à la réinitialisation, il n’y a ni dépôt ni taxe.
- À partir du jour 30 de la saison, les enchères sont fermées jusqu’au début de la nouvelle saison : rien ne peut être mis en vente, acheté ou enchéri. Vous pouvez toujours annuler vos annonces.
- Chaque monnaie a sa propre limite de ce que vous pouvez vendre et de ce que vous pouvez acheter en 24 heures (tableau des niveaux ci-dessous). Les lots gagnés ne comptent pas.
- Entre deux pilotes, l’un achetant à l’autre, il passe au plus 8 000 000 crédits ou 40 000 Thulium en 24 heures.

<!-- market-glance:end -->

## Objets vendables {#marketable-items}

Seuls les objets que vous avez **gagnés** peuvent être vendus. Tout ce que vous gagnez porte dans le [Hangar](/wiki/03-Mechanics/Inventory.md#marketable-items) une petite étiquette, **Vendable** : ce que vous ramassez dans l’espace (butin des aliens, des essaims, des Wardens et du trou noir : [Cargaison](/wiki/03-Mechanics/Cargo.md)), ce que paie une mission ([Quêtes](/wiki/03-Mechanics/Quests.md#rewards)) et tout ce que fabriquent l’Assemblage et la Forge. Ce que vous avez **acheté** en Boutique, gagné dans un lot, acheté sur le Marché, reçu avec un code bonus, un pack d’invitation ou le kit de départ, ou récupéré en remboursement n’est pas vendable et ne peut jamais être revendu, pour que rien ne soit acheté juste pour être revendu. Les plaques que fabrique la Fonderie du Skylab ne sont pas vendables non plus ; les Reinforced Plates qu’une mission paie le sont. Les munitions et les roquettes que fabriquent l’Imprimante à munitions et l’Usine à roquettes du Skylab ne sont pas vendables non plus.

L’étiquette est un nombre d’unités, pas un interrupteur : une pile de munitions peut contenir des coups achetés et gagnés, et la fiche indique « Vendable (3 sur 5) ». Quand vous utilisez une partie d’une pile (tir, fabrication), les unités ordinaires partent d’abord, si bien que les vendables durent le plus longtemps. Fusionner deux pièces dans la [Forge](/wiki/06-Items/Forge.md#merge) ne garde l’étiquette que si les deux pièces l’avaient, et l’aperçu le dit ; une étape de la Forge qui échoue rend ses matériaux sous forme d’unités ordinaires.

La pastille **Vendable uniquement** du Hangar ne montre que ce que vous pouvez vendre, et le **marteau** à côté de la corbeille d’un objet étiqueté ouvre pour lui la fiche de vente des Enchères. Dans l’Assemblage, une recette dont le résultat est vendable le dit, et un matériau qui vous manque a un lien qui ouvre les Enchères avec son nom dans la zone de recherche.

Quand les Enchères sont arrivées (0.4.12), l’équipement que vous déteniez déjà et que la Boutique ne vend pas, ainsi que les ressources, ont été étiquetés une fois. Ceux-ci ne l’ont pas été, parce que la Boutique les a vendus un temps ou parce que ce que vous détenez mêle pièces achetées et gagnées : le Quantum Laser III, les Absorption Shield Cells II et III, les Impulse Thrusters II et III, les deux Reinforced Plates et la plus ancienne Base CPU I de chaque pilote (celle du kit de départ). Les nouveaux exemplaires que vous gagnez ou fabriquez sont étiquetés.

## Ce qui peut être vendu {#what-can-be-sold}

<!-- market-kinds:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Catégorie | Objets que vous pouvez vendre | Nombre |
| :--- | :--- | ---: |
| **Lasers** | Quantum Laser I, Quantum Laser II, Quantum Laser III, Starfire-III, Helios Beam | 5 |
| **Amplis laser** | Damage Amp I, Crit Amp I, Penetration Amp I, Damage Amp II, Crit Amp II, Penetration Amp II, Damage Amp III, Crit Amp III, Penetration Amp III, Damage Amp IV, Crit Amp IV, Penetration Amp IV | 12 |
| **Boucliers** | Light Shield Core, Basic Shield Core, Heavy Shield Core | 3 |
| **Moteurs** | Engine I, Engine II, Engine III | 3 |
| **Adaptive Cores** | Adaptive Core I, Adaptive Core II, Adaptive Core III | 3 |
| **Cellules de bouclier** | Absorption Shield Cell I, Capacity Shield Cell I, Absorption Shield Cell II, Capacity Shield Cell II, Absorption Shield Cell III, Capacity Shield Cell III, Absorption Shield Cell IV, Capacity Shield Cell IV | 8 |
| **Propulseurs** | Impulse Thruster I, Momentum Thruster I, Impulse Thruster II, Momentum Thruster II, Impulse Thruster III, Momentum Thruster III, Impulse Thruster IV, Momentum Thruster IV | 8 |
| **Munitions laser** | Standard Battery (par lots de 100), Siphon Battery (par lots de 10), Advanced Plasma (par lots de 10), Ultra Core (par lots de 10), Experimental Fusion Core | 5 |
| **Roquettes** | Ember I, Lancet I, Rivet I, Scatter I, Ember II, Lancet II, Rivet II, Scatter II, Ember III, Lancet III, Rivet III, Scatter III | 12 |
| **Extras** | Repair Drone I, Repair Drone II, Repair Drone III, EMP Charge, Repair Drone IV, Cloaking CPU S, Base CPU I, Cloaking CPU M, Auto-Repair CPU, Cloaking CPU L, Base CPU II | 11 |
| **Ressources** | Cataclysite (par lots de 100), Ship Fragment (par lots de 100), Daraxium (par lots de 100), Nyxite (par lots de 100), Quorvium (par lots de 10), Reinforced Hull Plate (par lots de 10), Power Core, Velkonite Reinforced Plate, Dark Matter, Orvium Reinforced Plate | 10 |

<!-- market-kinds:end -->

Les vaisseaux, les drones, les formations de drones, les boosters et les abonnements ne peuvent jamais être vendus, pas plus que l’Ancient Control Unit, les minerais Velkonite et Orvium, la Dark Matter Plate, la Jump CPU, les Extra Slots CPU, la N.U.K.E. et la N.I.K.E. Les Dark Matter Plates ne sont pas du tout aux Enchères, ni comme marchandise ni comme prix. Un objet équipé, enchâssé dans un autre objet, contenant des modules ou placé dans le [Cache de transport](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) ne peut pas être mis en vente, pas plus qu’une Cloaking CPU, une EMP Charge ou une Base CPU déjà utilisée. Les munitions et les roquettes se vendent depuis la station : posez d’abord votre vaisseau.

## Vendre {#selling}

Appuyez sur **Vendre un objet** (ou sur le marteau dans le Hangar), choisissez ce que vous avez gagné (un menu de catégories réduit la liste, avec les mêmes catégories que le Marché), choisissez crédits ou Thulium, fixez le prix d’un lot et la durée de l’annonce : 1, 3 ou 7 jours. La fiche montre le prix minimum, trois pastilles qui remplissent un prix (**Minimum** ; **Vente rapide**, un de moins que l’annonce la moins chère du moment ; et **Équitable**, le prix de la dernière vente), puis le dépôt, la taxe et ce que vous recevez, avant de mettre en vente. Sous le prix, **Annonces similaires** montre sur un graphique à quels prix le même objet, avec le même enchantement, est en vente en ce moment, dans la monnaie que vous avez choisie : votre prix y est une ligne, le prix minimum, la dernière vente et le prix de la Boutique sont repérés, une ligne en mots dit où se situerait votre prix, et les trois annonces les moins chères sont affichées. Une pièce est un lot de un ; les munitions et certaines ressources se vendent par lots de 10 ou 100, et vous vendez un nombre entier de lots. Ce que vous mettez en vente quitte votre inventaire et est tenu par le serveur jusqu’à ce que ce soit vendu, que vous annuliez ou que l’annonce expire ; alors cela revient, avec son étiquette. Vous pouvez annuler à tout moment, même pendant les derniers jours d’une saison. Une annonce est un instantané : pour changer un prix, annulez l’annonce et remettez-la en vente (le dépôt est payé de nouveau).

Chaque objet a un **prix minimum** et il n’y a **pas de prix maximum** : demandez ce que vous voulez. Le tableau montre le prix minimum de quelques objets.

<!-- market-bands:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Objet | Vendu par lots de | Prix minimum, crédits | Prix minimum, Thulium |
| :--- | ---: | ---: | ---: |
| Quantum Laser II | 1 | 32 000 | 32 |
| Quantum Laser III | 1 | 210 000 | 210 |
| Helios Beam | 1 | 1 600 000 | 1 600 |
| Absorption Shield Cell IV | 1 | 1 100 000 | 1 100 |
| Heavy Shield Core | 1 | 870 000 | 870 |
| Impulse Thruster IV | 1 | 980 000 | 980 |
| EMP Charge | 1 | 40 000 | 40 |
| Cloaking CPU S | 1 | 400 000 | 400 |
| Ultra Core | 10 | 800 | 1 |
| Lancet I | 1 | 200 | 1 |
| Ship Fragment | 100 | 600 | 1 |
| Dark Matter | 1 | 33 000 | 33 |

<!-- market-bands:end -->

Un prix en Thulium suit une seule règle : le prix minimum en crédits divisé par le taux, arrondi à l’entier supérieur. Le taux n’est pas une valeur que le jeu donne au Thulium. Il sert seulement à calculer le prix minimum en Thulium, et à cause de lui une annonce en Thulium peut être bon marché pour un pilote qui a du Thulium. La plupart des vendeurs demanderont des crédits. Tous les objets sauf le **Quorvium** peuvent être mis à prix en Thulium, les bon marché aussi (munitions, roquettes, ressources communes) : leur prix minimum est alors de 1 Thulium, le plus petit pas. Seul le Quorvium reste en crédits uniquement, car 1 Thulium vaudrait plus qu’un lot de Quorvium.

Vos **annonces ouvertes** (et une annonce qu’un admin a suspendue) occupent des emplacements. En montant de niveau, vous avez plus d’emplacements, jusqu’à un maximum, et vous pouvez vendre et acheter davantage par jour. La durée que peut avoir une annonce est la même à tous les niveaux.

<!-- market-limits:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Niveau | Annonces ouvertes | Durée maximale | Par jour, crédits | Par jour, Thulium | Dépôt par 24 h |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 5 | 20 | 168 h | 4 500 000 | 22 500 | 1 % |
| 6 | 40 | 168 h | 6 000 000 | 30 000 | 1 % |
| 7 | 70 | 168 h | 7 500 000 | 37 500 | 1 % |
| 8 | 100 | 168 h | 8 500 000 | 42 500 | 1 % |
| 9 | 100 | 168 h | 10 000 000 | 50 000 | 1 % |
| 10 | 100 | 168 h | 15 000 000 | 75 000 | 1,5 % |
| 11 | 100 | 168 h | 15 000 000 | 75 000 | 1,5 % |
| 12 | 100 | 168 h | 15 000 000 | 75 000 | 1,5 % |
| 13 | 100 | 168 h | 20 000 000 | 100 000 | 1,5 % |
| 14 | 100 | 168 h | 20 000 000 | 100 000 | 1,5 % |
| 15 | 100 | 168 h | 20 000 000 | 100 000 | 1,5 % |
| 16 | 100 | 168 h | 20 000 000 | 100 000 | 1,5 % |
| 17 | 100 | 168 h | 20 000 000 | 100 000 | 1,5 % |
| 18 | 100 | 168 h | 20 000 000 | 100 000 | 1,5 % |
| 19 | 100 | 168 h | 20 000 000 | 100 000 | 1,5 % |
| 20 et plus | 100 | 168 h | 20 000 000 | 100 000 | 1,5 % |

<!-- market-limits:end -->

## Frais {#fees}

Une annonce coûte un **dépôt**, payé à la mise en vente et jamais remboursé, et une vente coûte une **taxe**, prélevée sur ce que reçoit le vendeur. Les deux sont payés dans la monnaie de l’annonce et **détruits** : ils ne vont à personne, donc personne ne gagne à commercer avec soi-même. Pendant les deux derniers jours d’une saison, il n’y a ni dépôt ni taxe.

<!-- market-fees:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Annonce | Prix | Dépôt | Taxe | Le vendeur reçoit |
| :--- | ---: | ---: | ---: | ---: |
| Quantum Laser III : niveau 6, 24 h | 210 000 crédits | 2 100 crédits | 10 500 crédits | 199 500 crédits |
| Quantum Laser III : niveau 10, 72 h | 210 Thulium | 10 Thulium | 10 Thulium | 200 Thulium |
| Helios Beam : niveau 12, 168 h | 2 500 000 crédits | 262 500 crédits | 125 000 crédits | 2 375 000 crédits |
| Helios Beam : niveau 12, 168 h, pendant les derniers jours d’une saison | 2 500 000 crédits | 0 crédits | 0 crédits | 2 500 000 crédits |

<!-- market-fees:end -->

## Acheter {#buying}

Le **Marché** montre ce que vendent les autres pilotes. Réduisez la liste avec les **pastilles de catégorie** (une par type d’objet, avec le nombre d’annonces qu’elle contient), cherchez par nom, filtrez par enchantement et monnaie, et triez par prix, par ce qui se termine le plus tôt ou par ce qui est le plus récent. Choisissez une annonce pour voir ce que c’est, qui la vend, combien de temps elle dure et comment son prix se situe par rapport à la dernière vente, au prix le plus bas du moment et au prix de la Boutique. Une pile s’achète par lots entiers. Un gros achat demande une dernière confirmation. Le vendeur est payé tout de suite, moins la taxe ; vous ne payez ni dépôt ni taxe. Ce que vous achetez **n’est pas vendable** : la page dit « Vous obtenez : non commercialisable » à côté de **Acheter pour …**, parce que seul ce que vous gagnez peut être vendu. Vous ne pouvez pas acheter votre propre annonce. Une annonce qui se vend pendant que vous la regardez dit « Cette annonce n’existe plus. »

## Limites {#limits}

Chaque monnaie a sa propre limite quotidienne de ce que vous pouvez vendre et de ce que vous pouvez acheter, comptée sur les dernières 24 heures, et une limite de ce qui passe entre deux pilotes, pour qu’un second compte ne soit pas un moyen rapide de déplacer une fortune. Les crédits et le Thulium ne sont jamais additionnés : qui vend en Thulium use sa limite de Thulium, et rien d’autre. La fiche de vente vous avertit quand une vente dépasserait votre limite quotidienne de vente, et quand un achat dépasserait votre limite quotidienne d’achat, le Marché vous le dit et laisse **Acheter pour …** inactif. Les limites grandissent avec le niveau, et Premium n’en change aucune. Les lots gagnés ne comptent pas.

Les roquettes d’une annonce, d’un lot que vous menez et de votre soute comptent toutes dans le maximum d’une roquette que vous pouvez emporter : une annonce ne permet pas d’emporter plus que ce qu’autorise la pile de la Boutique.

## Mes annonces et Historique {#my-listings-and-history}

**Mes annonces** montre vos emplacements et chaque annonce avec son état (ouverte, vendue, annulée, expirée, rendue ou suspendue), un bouton **Annuler**, **Remettre en vente** pour une annonce terminée et une pastille **Sous-cotée** quand une autre annonce du même objet demande moins. Une annonce arrivée à son terme revient d’elle-même dans votre inventaire. L’**Historique** s’ouvre sur vos échanges des 30 derniers jours : vos ventes et vos achats, ce que vous avez gagné et dépensé, les frais et taxes que vous avez payés, votre résultat net, votre meilleure vente, votre vente moyenne et l’objet que vous avez le plus échangé, avec deux courbes : vos gains par jour et votre résultat à ce jour (en crédits ou en Thulium, une monnaie à la fois). En dessous vient la liste de ce que vous avez vendu, acheté et gagné, avec la taxe. Le jeu garde le registre des Enchères 90 jours.

Vous êtes prévenu quand quelque chose se vend : par une notification, le son des Enchères et le nouveau solde, et par un badge sur l’entrée des Enchères tant que la page est fermée. Une série de ventes ne fait qu’une notification. Les Enchères ont leurs propres sons discrets, un pour chaque chose que vous y faites ou qui vous y arrive (mettre en vente, terminer, une vente, une enchère, être surenchéri, gagner), et ils suivent le volume de l’interface.

## Les lots de chaque heure {#the-hourly-lots}

Les Lots sont les offres du jeu lui-même : munitions, roquettes et EMP Charges, chaque heure, à enchérir. C’est un moyen d’acheter des munitions moins cher que la Boutique, et un puits : l’enchère gagnante est détruite. Seuls s’ouvrent les lots du tableau du jour ci-dessous (jamais de munitions x1 ou x4, jamais de Siphon Batteries, jamais de roquette spéciale), dans la monnaie de la Boutique. Un lot de roquettes ne dépasse jamais le maximum de cette roquette que vous pouvez emporter (la pile de la Boutique) : une enchère qui vous ferait le dépasser est refusée, alors enchérissez sur un lot de roquettes quand vous en emportez peu.

<!-- market-lots:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- Un nouveau lot s’ouvre au début de chaque heure UTC et reste ouvert 4 heures, si bien que 4 sont ouverts en même temps.
- La mise de départ est de 40 % du prix en Boutique de la marchandise. Une enchère suivante doit dépasser la meilleure d’au moins 5 %, et d’au moins 100 crédits ou 1 Thulium.
- Votre enchère est payée tout de suite et retenue. Si quelqu’un surenchérit, elle vous est rendue tout de suite.
- Une enchère dans les 2 min qui précèdent la fin d’un lot repousse sa fin à 2 min après l’enchère, au plus 5 fois.
- Ce que vous gagnez sert à voler, pas à commercer : ce n’est jamais vendable. L’enchère gagnante est détruite. Un lot sur lequel personne n’enchérit n’est pas vendu et ne coûte rien à personne.
- La taille d’un lot suit les pilotes de niveau 5 ou plus qui ont consulté les enchères ces 3 derniers jours : sans aucun, elle est de 10 % de la taille du tableau, à partir de 30 la taille complète, par paliers de 500 pour les munitions, 50 pour les roquettes et 1 pour les EMP Charges.
- Aucun lot n’est créé pendant les 6 dernières heures d’une saison. La réinitialisation annule les lots encore ouverts, et chaque enchère est rendue.

<!-- market-lots:end -->

<!-- market-day:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Heure UTC | Lot | Taille complète | Payé en | Mise de départ à taille complète |
| :--- | :--- | ---: | :--- | ---: |
| 00:00 | Scatter III | 1 250 | Thulium | 2 500 Thulium |
| 01:00 | Advanced Plasma | 25 000 | Thulium | 5 000 Thulium |
| 02:00 | Lancet I | 12 500 | Crédits | 2 500 000 crédits |
| 03:00 | EMP Charge | 5 | Thulium | 1 000 Thulium |
| 04:00 | Ultra Core | 25 000 | Thulium | 10 000 Thulium |
| 05:00 | Rivet II | 5 000 | Crédits | 1 600 000 crédits |
| 06:00 | Advanced Plasma | 10 000 | Thulium | 2 000 Thulium |
| 07:00 | Advanced Plasma | 50 000 | Thulium | 10 000 Thulium |
| 08:00 | Ember I | 12 500 | Crédits | 2 500 000 crédits |
| 09:00 | Ultra Core | 50 000 | Thulium | 20 000 Thulium |
| 10:00 | Scatter II | 5 000 | Crédits | 1 600 000 crédits |
| 11:00 | EMP Charge | 5 | Thulium | 1 000 Thulium |
| 12:00 | Advanced Plasma | 50 000 | Thulium | 10 000 Thulium |
| 13:00 | Lancet III | 1 250 | Thulium | 2 500 Thulium |
| 14:00 | Ultra Core | 10 000 | Thulium | 4 000 Thulium |
| 15:00 | Advanced Plasma | 25 000 | Thulium | 5 000 Thulium |
| 16:00 | Ultra Core | 50 000 | Thulium | 20 000 Thulium |
| 17:00 | Rivet I | 12 500 | Crédits | 2 500 000 crédits |
| 18:00 | Advanced Plasma | 50 000 | Thulium | 10 000 Thulium |
| 19:00 | Ember II | 5 000 | Crédits | 1 600 000 crédits |
| 20:00 | Ultra Core | 25 000 | Thulium | 10 000 Thulium |
| 21:00 | Advanced Plasma | 25 000 | Thulium | 5 000 Thulium |
| 22:00 | Advanced Plasma | 10 000 | Thulium | 2 000 Thulium |
| 23:00 | EMP Charge | 5 | Thulium | 1 000 Thulium |

<!-- market-day:end -->

Quand peu de pilotes utilisent les Enchères, les lots sont petits, pour qu’une poignée de pilotes ne se voie pas offrir des milliers de coups chaque heure ; ils grandissent à mesure que plus de pilotes regardent.

## La saison et la réinitialisation {#the-season-and-the-wipe}

Les Enchères suivent la saison (voir [Chronologie des réinitialisations](/wiki/03-Mechanics/Wipe-Timeline.md)). Pendant les deux derniers jours, il n’y a pas de frais. À partir du jour 30, quand le compte à rebours de cinq minutes de la réinitialisation commence, elles sont fermées : rien n’est mis en vente, acheté ou enchéri, un lot qui se termine alors est annulé et son enchère rendue, et vous pouvez toujours annuler vos propres annonces. Une annonce ne dépasse jamais la fin de la saison.

À la réinitialisation, **chaque annonce ouverte revient à son vendeur** comme objets en vrac, et la réinitialisation supprime ensuite les objets en vrac comme tous les autres (seul reste ce que vous mettez dans le [Cache de transport](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-)) : vendez donc, ou annulez et mettez au Cache ce que vous voulez garder. Les lots encore ouverts sont annulés et les enchères remboursées. Les crédits et le Thulium ne sont pas réinitialisés.

## Ce que les Enchères ne vous donnent pas {#what-the-auction-does-not-give-you}

Les Enchères servent à échanger ce que vous gagnez, et elles sont honnêtes sur leurs limites.

- **Vendre du butin n’est pas un grind.** Le butin brut des aliens n’est composé que de ressources et vaut de 0,4 à 0,9 pour cent de ce que paient en kills la même heure de chasse au niveau 5. Ce que le Marché donne à un nouveau pilote, c’est l’équipement que lui paient ses missions et dont il n’a pas besoin (une fois), les ressources des missions Défi, les caisses des boss d’essaim et ce qu’il fabrique.
- **Il n’y a pas de revendeur.** Les ordres d’achat, où un pilote dit ce qu’il veut acheter et pour combien, ne sont pas dans cette version. En attendant, les seuls marchands sont l’artisan, qui achète des matériaux, fabrique de l’équipement dans l’Assemblage et le vend, et le pilote entrepôt, qui garde son stock dans le Cache de transport à travers la réinitialisation.
- **L’équipement de la Boutique n’est pas fait pour être revendu.** L’équipement que vous avez acheté en Boutique ne peut pas être revendu : cela comprend le Quantum Laser I et II, le Light et le Basic Shield Core, Engine I et II, le premier rang de cellules et de propulseurs, les amplis que vend la Boutique et les munitions achetées. Le seul Quantum Laser II vendable d’un pilote est celui qu’une mission paie une fois.
- **Les plaques viennent des missions.** Les Velkonite et Orvium Reinforced Plates du Marché sont celles que paient les missions Défi. Les plaques de la Fonderie restent dehors, sinon elles seraient la plus grosse marchandise du Marché.

Si une annonce vous semble anormale, signalez-la de la façon habituelle : les administrateurs du jeu peuvent suspendre une annonce, la rendre, mettre les Enchères en pause ou en exclure un pilote, et chacune de ces actions est enregistrée.
