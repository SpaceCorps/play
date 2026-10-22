<!-- wiki-i18n source: fca6f67d57774324 -->
<!-- wiki-i18n title: Skylab -->
# Skylab

Le Skylab est votre installation orbitale personnelle. Il construit et améliore des modules qui produisent des crédits et du Thulium, extraient du minerai, forgent les plaques dont l’Assemblage fait les meilleurs lasers et, à partir du niveau 10 du Noyau, recherchent les technologies dont l’Assemblage a besoin. Il travaille pour vous même quand vous êtes hors ligne.

Au niveau 10 du Noyau, le Skylab grandit aussi : un **pont** relie le Noyau à un second Noyau doté de six emplacements de module de plus, et trois modules supplémentaires s’y branchent : l’**Imprimante à munitions** et l’**Usine à roquettes**, qui fabriquent munitions et roquettes à partir de rien, et la **Baie à minerai**, qui verse dans l’Entrepôt de ressources le minerai que vous transportez (voir [Le pont et le Noyau 2](#the-bridge-and-core-2) et [Baie à minerai](#ore-bay)).

Au niveau 15 du Noyau, le Skylab grandit encore et apprend à voler : un **second pont** relie le Noyau à un troisième Noyau, le **Noyau 3**, doté de quatre emplacements de plus, et les quatre modules de l’**Expédition** les prennent : le **Module Moteurs**, le **Module Défense**, le **Module Radar** et la **Baie des trophées**. Avec des moteurs, des lasers et des munitions de votre Imprimante à munitions, le Skylab parcourt une **carte de l’univers** qui lui est propre, chasse les aliens des cellules qu’il atteint pendant que vous êtes absent et ramène le butin à la maison (voir [Le second pont et le Noyau 3](#the-second-bridge-and-core-3) et [Expéditions](#expeditions)).

> [!NOTE]
> **Ce qui a changé dans la 0.4.10.** Chaque module du Skylab a désormais sa propre table de production, de prix et de durées, niveau par niveau. Vous avez gardé vos niveaux : rien n’a été facturé et rien n’a été remboursé pour la différence. Ce que vos fermes et vos collecteurs avaient dans leurs réservoirs à l’arrivée de la mise à jour a été versé **une seule fois, au taux de l’ancienne version** : les crédits et le Thulium sont allés sur votre compte, le minerai dans votre Entrepôt de ressources, et les réservoirs sont repartis de zéro.
>
> Deux règles sont nouvelles. **Solaire ne produit que 25 % de son énergie pendant son amélioration**, si bien que, pour la plupart des stations, toutes les fermes et tous les collecteurs s’arrêtent jusqu’à la fin de l’amélioration (voir [Module Solaire](#solar-module) et [Planifier une amélioration de Solaire](#timing-a-solar-upgrade)). **L’Entrepôt de ressources a sa propre limite pour chaque minerai** : un jour de production du collecteur au niveau 1, quatre jours au niveau 20.

> [!NOTE]
> **Ce qui a changé dans la 0.4.15.** L’étape du Noyau du niveau 9 au niveau 10 coûte désormais **2 000 Thulium** de plus, et quand elle est terminée, un **pont** et un second Noyau, le **Noyau 2**, apparaissent avec six nouveaux emplacements de module. Solaire déménage sur le Noyau 2. Deux nouveaux modules s’y branchent : l’**Imprimante à munitions** et l’**Usine à roquettes**. Solaire produit aussi plus d’énergie à partir du niveau 7, pour qu’une station complète reste couverte. Rien de ce que vous avez construit n’est perdu : un Noyau déjà au niveau 10 ou plus a le pont tout de suite et ne paie rien.

> [!NOTE]
> **Ce qui a changé dans la 0.4.21.** L’étape du Noyau du niveau 14 au niveau 15 coûte désormais **4 000 Thulium** de plus, et quand elle est terminée, un second **pont** et le **Noyau 3** apparaissent avec quatre nouveaux emplacements. Solaire déménage sur le Noyau 3 et produit plus d’énergie à partir du niveau 15, de sorte qu’une station complète reste couverte. Quatre nouveaux modules prennent les emplacements : le **Module Moteurs**, le **Module Défense**, le **Module Radar** et la **Baie des trophées**, et avec eux votre Skylab vole sur la **carte de l’univers**, chasse tout seul et ramène son butin à la maison (voir [Expéditions](#expeditions)). Chaque module a désormais un **poids**, et le poids de la station et de ses moteurs décide de la vitesse à laquelle elle vole (voir [Poids et vitesse](#weight-and-speed)). La **Baie à minerai** verse trois fois plus de minerai par heure et garde trois fois plus de quota. Rien de ce que vous avez construit n’est perdu : un Noyau déjà au niveau 15 ou plus a le Noyau 3 tout de suite et ne paie rien.

![The Skylab of a Core 20 with the second bridge: Core 3 carries the Engine, Defense and Radar Modules and the Trophies Bay](../../img/wiki-img/shots/skylab-core3.jpg)
![The Rocket Factory's sheet: the rocket it makes, the room to carry and its storage](../../img/wiki-img/shots/skylab-factory.jpg)
![The Ore Bay's sheet: the ores it moves and banks for you and how much it holds](../../img/wiki-img/shots/skylab-orebay.jpg)
![The Ammo Printer's Build sheet: its price in Credits, Thulium and Ship Fragments](../../img/wiki-img/shots/skylab-printer-build.jpg)
![The Ammo Printer's sheet: its mode, rate, storage and what the next level gives](../../img/wiki-img/shots/skylab-printer.jpg)
![The Skylab station fully grown, seen from the side as the page opens: three Cores in a row with their bridges, every module with its name tag, the Labels switch at the bottom left](../../img/wiki-img/shots/skylab-station.jpg)
![The Resource Storage card of the Skylab](../../img/wiki-img/shots/skylab-storage.jpg)
![The Skylab table of modules: level, production, storage, power and status of every module, from the Core to the Trophies Bay](../../img/wiki-img/shots/skylab-table.jpg)
![The Skylab hunting in a cell of the Universe map: its hull and kills, the cell, the Defense and Engine Modules and the Trophies Bay filling, and Recall](../../img/wiki-img/shots/skylab-trip.jpg)
![The Trophies Bay's sheet: its level and the capacity the trophies of a trip are kept in](../../img/wiki-img/shots/skylab-trophies.jpg)
![The Universe map: 150 hexagonal cells, the ports, the cells you know and the cells the Radar can still scan, marked with a question mark](../../img/wiki-img/shots/skylab-universe.jpg)

## En une minute {#in-one-minute}

- Construisez **Solaire** d’abord : sans son énergie, rien ne tourne dans le Skylab. La Ferme à crédits ne coûte rien à construire, et la Ferme à Thulium coûte 5 000 crédits et 500 Thulium.
- Les fermes et les collecteurs remplissent un **réservoir** (72 heures de production) pendant votre absence. **Récupérer** le verse sur votre compte (crédits, Thulium) ou dans votre Entrepôt de ressources (minerai).
- La **Ferme à Thulium** est votre principale source de Thulium : 40 par heure au niveau 1, 1 280 au niveau 20. La Ferme à crédits produit 2 250 crédits par heure au niveau 1 et 225 000 au niveau 20.
- Le **Noyau** donne le rythme : aucun module ne le dépasse, et sa propre montée prend environ 16 jours et demi.
- Au **niveau 10 du Noyau**, un **pont** construit le **Noyau 2**, avec six emplacements de module de plus, et l’**Imprimante à munitions**, l’**Usine à roquettes** et la **Baie à minerai** s’y branchent. L’étape vers le niveau 10 coûte 2 000 Thulium de plus.
- Au **niveau 15 du Noyau**, un second pont construit le **Noyau 3**, et le **Module Moteurs**, le **Module Défense**, le **Module Radar** et la **Baie des trophées** prennent ses emplacements : avec eux, le Skylab vole sur la carte de l’univers et chasse tout seul. L’étape vers le niveau 15 coûte 4 000 Thulium de plus. [Voir Expéditions](#expeditions).
- **Solaire ne produit que 25 % de son énergie pendant son amélioration**, vos fermes et vos collecteurs s’arrêtent donc jusqu’à sa fin. [Planifiez-la](#timing-a-solar-upgrade).

## Vue d’ensemble {#overview}

Le Skylab suit sa propre horloge, à part de votre vaisseau : les modules produisent et forgent pendant que vous êtes absent. À vous de construire, d’améliorer, de garder l’énergie en équilibre et de récupérer. La page a quatre vues de la même station : **Station** (la station en 3D, avec une pastille au-dessus de chaque module ; cliquez sur l’une pour ouvrir sa fiche, ou appuyez sur **1** à **9**), **Liste** (une carte par module), **Tableau** (les chiffres de tous les modules dans un tableau) et **Recherche** (l’écran propre du Centre de recherche, voir [Recherche](/wiki/03-Mechanics/Research.md)). Si vous survolez **Construire** ou **Améliorer**, vous voyez ce que le niveau suivant change, ce qu’il coûte et combien de temps il prend. Le bouton **Univers** de l’en-tête de la page ouvre la carte de l’Expédition (voir [Expéditions](#expeditions)).

Seize modules forment la station :

| Module | Produit ou fait | Constructible à partir de |
| :--- | :--- | :--- |
| **Noyau** | Fixe le niveau maximal de tous les autres modules | Toujours présent |
| **Solaire** | Produit de l’énergie | N’importe quel niveau du Noyau |
| **Ferme à crédits** | Produit des [crédits](/wiki/01-General/Getting-Started.md) | N’importe quel niveau du Noyau |
| **Ferme à Thulium** | Produit du [Thulium](/wiki/01-General/Getting-Started.md) | N’importe quel niveau du Noyau |
| **Collecteur de Velkonite** | Extrait du minerai de Velkonite | Noyau au niveau 5 |
| **Collecteur d’Orvium** | Extrait du minerai d’Orvium | Noyau au niveau 5 |
| **Entrepôt de ressources** | Stocke le minerai | Noyau au niveau 5 |
| **Fonderie** | Forge le minerai en plaques | Noyau au niveau 5 |
| **Centre de recherche** | Transforme des ressources en science et recherche des [technologies](/wiki/03-Mechanics/Research.md) | Noyau au niveau 10 |
| **Imprimante à munitions** | Imprime des munitions x2, x3 ou x4 à partir de rien | Noyau au niveau 10, sur le Noyau 2 |
| **Usine à roquettes** | Construit des roquettes de la boutique à partir de rien | Noyau au niveau 10, sur le Noyau 2 |
| **Baie à minerai** | Verse dans l’Entrepôt de ressources le Velkonite et l’Orvium que vous transportez | Noyau au niveau 10, sur le Noyau 2 |
| **Module Moteurs** | Abrite les moteurs qui font voler le Skylab | Noyau au niveau 15, sur le Noyau 3 |
| **Module Défense** | Abrite les lasers et le chargeur qui combattent en expédition | Noyau au niveau 15, sur le Noyau 3 |
| **Module Radar** | Scanne le brouillard de la carte de l’univers | Noyau au niveau 15, sur le Noyau 3 |
| **Baie des trophées** | Garde ce que rapportent les expéditions | Noyau au niveau 15, sur le Noyau 3 |

Les deux **ponts**, le **Noyau 2** et le **Noyau 3** ne sont pas des modules : le premier pont et le Noyau 2 apparaissent quand le Noyau atteint le niveau 10, le second pont et le Noyau 3 au niveau 15, et aucun des deux Noyaux n’a de niveau propre (voir [Le pont et le Noyau 2](#the-bridge-and-core-2) et [Le second pont et le Noyau 3](#the-second-bridge-and-core-3)).

**Des missions dédiées.** Dix [missions Station](/wiki/03-Mechanics/Quests.md#station-missions) dans Mission Control vous guident à travers le Skylab : construire Solaire, une Ferme à crédits et une Ferme à Thulium, monter le Noyau et Solaire, récupérer vos 50 000 premiers crédits et ouvrir la chaîne d’approvisionnement, et elles rapportent un peu à chaque étape. La première est ouverte dès le niveau 1.

## La station à chaque niveau {#the-station-at-every-level}

Voici la vue Station du Skylab à chaque niveau de 1 à 20, toutes sous le même angle, avec tous les modules au même niveau. La vue fait tenir toute la station dans l’image : l’échelle n’est donc pas la même partout, elle fait un saut quand la forme grandit. La station grandit par étapes : sa forme change aux **niveaux 1, 5, 10, 15 et 20**, et entre-temps chaque niveau allume **une lampe de plus** sur le collier de chaque module (le nombre de lampes allumées est le niveau, et l’anneau de vingt lampes du Noyau se remplit de la même façon).

Ces images montrent le **premier Noyau** et ce qui y est accroché, avec Solaire à côté, comme la station était avant les ponts. La station se poursuit au-delà, et les images ne montrent pas cette partie : à partir du niveau 10, un pont, le Noyau 2 et l’Imprimante à munitions, l’Usine à roquettes et la Baie à minerai se trouvent au-delà, et Solaire passe à l’autre bout (voir [Le pont et le Noyau 2](#the-bridge-and-core-2)) ; à partir du niveau 15, un second pont, le Noyau 3 et les quatre modules de l’Expédition se trouvent encore au-delà (voir [Le second pont et le Noyau 3](#the-second-bridge-and-core-3)). La vue Station de la page montre la station entière.

**Niveaux 1 à 4.** Les quatre premiers modules autour du Noyau : Solaire, la Ferme à crédits, la Ferme à Thulium et la baie d’amarrage qui accueille votre vaisseau. La chaîne d’approvisionnement ne peut pas encore être construite.

![Niveau 1](../../img/skylab/wiki/level-01.jpg)
![Niveau 2](../../img/skylab/wiki/level-02.jpg)
![Niveau 3](../../img/skylab/wiki/level-03.jpg)
![Niveau 4](../../img/skylab/wiki/level-04.jpg)

**Niveaux 5 à 9.** Avec le Noyau au niveau 5, la chaîne d’approvisionnement peut être construite : les deux collecteurs sur leurs structures au-dessus de la station, l’Entrepôt de ressources au port nord-est du Noyau et la Fonderie à son port nord-ouest (ils sont montrés ici construits).

![Niveau 5](../../img/skylab/wiki/level-05.jpg)
![Niveau 6](../../img/skylab/wiki/level-06.jpg)
![Niveau 7](../../img/skylab/wiki/level-07.jpg)
![Niveau 8](../../img/skylab/wiki/level-08.jpg)
![Niveau 9](../../img/skylab/wiki/level-09.jpg)

**Niveaux 10 à 14.** Le Noyau porte son anneau, les fermes et les collecteurs prennent leur forme plus grande et la Ferme à Thulium reçoit son propre anneau.

![Niveau 10](../../img/skylab/wiki/level-10.jpg)
![Niveau 11](../../img/skylab/wiki/level-11.jpg)
![Niveau 12](../../img/skylab/wiki/level-12.jpg)
![Niveau 13](../../img/skylab/wiki/level-13.jpg)
![Niveau 14](../../img/skylab/wiki/level-14.jpg)

**Niveaux 15 à 19.** Les fermes se remplissent de caisses et de cristaux, la baie d’amarrage éclaire son approche et le panneau Solaire se dote de son sommet. Au niveau 15, la station grandit aussi au-delà de l’image, d’un second pont et du Noyau 3.

![Niveau 15](../../img/skylab/wiki/level-15.jpg)
![Niveau 16](../../img/skylab/wiki/level-16.jpg)
![Niveau 17](../../img/skylab/wiki/level-17.jpg)
![Niveau 18](../../img/skylab/wiki/level-18.jpg)
![Niveau 19](../../img/skylab/wiki/level-19.jpg)

**Niveau 20.** Le sommet de l’échelle : la couronne sur le Noyau et les tours achevées des fermes et de la chaîne d’approvisionnement.

![Niveau 20](../../img/skylab/wiki/level-20.jpg)

**Les cartes des neuf modules.** La vue Liste de la même station au niveau 20 : les quatre modules de la première version, le Collecteur de Velkonite, le Collecteur d’Orvium, l’Entrepôt de ressources et la Fonderie venus avec la chaîne d’approvisionnement, et le Centre de recherche. Chaque carte montre le niveau du module, sa production, son énergie et son interrupteur. Toutes les cartes affichent le niveau 20, sauf celle du Centre de recherche : il a les niveaux 1 à 10, donc sa carte affiche le niveau 10, son maximum. Les cartes de l’Imprimante à munitions, de l’Usine à roquettes et de la Baie à minerai sont dans la même vue et sont décrites [plus bas](#the-bridge-and-core-2), tout comme les quatre cartes des modules de l’Expédition, dans [Le second pont et le Noyau 3](#the-second-bridge-and-core-3).

![La vue Liste au niveau 20 : les cartes du Noyau, de Solaire, de la Ferme à crédits, de la Ferme à Thulium, du Collecteur de Velkonite, du Collecteur d’Orvium, de l’Entrepôt de ressources, de la Fonderie et du Centre de recherche](../../img/skylab/wiki/modules.jpg)

## Les quatre premiers modules {#the-first-four-modules}

### Module Noyau {#core-module}

Le cœur de votre Skylab. Le niveau du Noyau fixe le niveau maximal de tous les autres modules : aucun module ne peut être amélioré au-delà de votre Noyau. Le Noyau monte jusqu’au niveau 20 et, à partir du **niveau 5**, il ouvre la chaîne d’approvisionnement ci-dessous. Ses améliorations coûtent des crédits, l’étape vers le **niveau 10** coûte **2 000 Thulium** de plus et construit le pont et le Noyau 2 (voir [Le pont et le Noyau 2](#the-bridge-and-core-2)), et l’étape vers le **niveau 15** coûte **4 000 Thulium** de plus et construit un second pont et le Noyau 3 (voir [Le second pont et le Noyau 3](#the-second-bridge-and-core-3)). En tout, il faut 112 326 crédits jusqu’au niveau 10 et 6 647 504 jusqu’au niveau 20, plus ces 6 000 Thulium, et environ 16,5 jours (voir [Durées d’amélioration](#upgrade-times)).

### Module Solaire {#solar-module}

L’énergie est le sang du Skylab. Le module Solaire produit l’énergie qu’utilisent tous les autres modules.

- **Importance** : si votre consommation d’énergie dépasse votre production, vos fermes et vos collecteurs s’arrêtent.
- **Énergie produite** : un module Solaire au niveau N produit de quoi alimenter **chaque autre module au niveau N**, avec environ un dixième de plus : 255 au niveau 1, 965 au niveau 7, 18 575 au niveau 20. Solaire de niveau 7 alimente une station entière au niveau 7 (voir Gestion de l’énergie pour chaque niveau).
- **Prix** : construire Solaire coûte **500 crédits et 50 Thulium**. Ses améliorations coûtent la même chose et durent aussi longtemps que celles de la Fonderie : de 8 000 crédits et 25 Thulium pour le niveau 2 (5 minutes) à 9 000 000 de crédits et 10 000 Thulium pour le niveau 20 (24 heures).
- **Amélioration** : pendant son amélioration, Solaire ne produit que **25 %** de l’énergie de son niveau actuel, puis celle du nouveau niveau dès que l’amélioration se termine. Une station qui consomme davantage s’arrête : toutes les fermes et tous les collecteurs cessent de produire, et la Fonderie ne lance aucun nouveau lot jusqu’à la fin de l’amélioration. C’est le cas de presque toutes les stations : elle ne tourne pendant l’amélioration que si tous les autres modules sont au moins cinq niveaux en dessous de Solaire (six niveaux à partir du niveau 10 de Solaire). Planifiez une amélioration de Solaire comme une panne de vos fermes (voir Construction et amélioration).
- **Place** : Solaire se trouve à l’autre bout de la station : sur le Noyau 2 à partir du niveau 10 du Noyau et sur le Noyau 3 à partir du niveau 15 (voir [Le pont et le Noyau 2](#the-bridge-and-core-2) et [Le second pont et le Noyau 3](#the-second-bridge-and-core-3)).

### Ferme à crédits et Ferme à Thulium {#credit-farm-and-thulium-farm}

- **Ferme à crédits** : produit des crédits au fil du temps : **2 250 par heure au niveau 1, 225 000 au niveau 20** (niveau 5 : 11 250 ; niveau 10 : 33 750 ; niveau 15 : 76 500). Elle ne coûte rien à construire.
- **Ferme à Thulium** : produit du Thulium au fil du temps : **40 par heure au niveau 1, 1 280 au niveau 20** (niveau 5 : 144 ; niveau 10 : 360 ; niveau 15 : 760). La construire coûte 5 000 crédits et 500 Thulium.
- Les deux ont besoin d’énergie, et chacune conserve 72 heures de sa production jusqu’à ce que vous la récupériez.

## La chaîne d’approvisionnement {#the-supply-chain}

Quatre modules transforment le temps passé loin du clavier en plaques pour vos meilleurs lasers. Le minerai vient **uniquement** des collecteurs (tous les matériaux et toutes les monnaies sont sur la page [Ressources](/wiki/06-Items/Resources.md)) : les aliens n’en lâchent pas et la boutique n’en vend pas. (Une [excavatrice géante](/wiki/03-Mechanics/Giant-Excavator.md) dépose aussi un peu de Velkonite et d’Orvium dans des caisses, mais ce minerai va dans votre cargaison, et seule la [Baie à minerai](#ore-bay) le verse dans l’Entrepôt de ressources, où la Fonderie et le Centre de recherche le prennent.)

1. Un **collecteur** extrait du minerai, une quantité donnée par heure, dans son propre réservoir (de quoi stocker 72 heures).
2. **Récupérer** déplace le minerai du réservoir vers l’**Entrepôt de ressources**, la banque, où chaque minerai est gardé à part.
3. La **Fonderie** prend dans la banque le minerai dont elle a besoin au début d’un lot, et fabrique des plaques, 10 secondes par plaque, un lot à la fois.
4. **Récupérer les plaques** déplace les plaques terminées dans votre inventaire (votre vaisseau doit être amarré). L’[Assemblage](/wiki/06-Items/Lasers.md) les transforme en Quantum Laser III, en Starfire-III ou en Helios Beam, et, une de chaque avec 5 Dark Matter, en Dark Matter Plate, que demandent [la Forge](/wiki/06-Items/Forge.md) et le dernier palier de chaque chaîne d’amélioration.

### Collecteur de Velkonite et Collecteur d’Orvium {#velkonite-collector-and-orvium-collector}

- **Minerai** : le Collecteur de Velkonite extrait **10 Velkonite par heure** au niveau 1 et le Collecteur d’Orvium **10 Orvium par heure**, et chaque niveau a sa propre cadence : jusqu’à 80 Velkonite et 40 Orvium par heure au niveau 20 (niveau 5 : 18 et 14 par heure ; niveau 10 : 32 et 24).
- **Réservoir** : chacun contient 72 heures de son minerai et cesse d’extraire quand il est plein.
- **Récupérer** : déplace le minerai dans l’Entrepôt de ressources, dans la limite de la place disponible. Sans entrepôt construit, ou si la banque de ce minerai est pleine, il n’y a nulle part où le mettre et le bouton en indique la raison. Le reste demeure dans le réservoir.
- **Énergie** : 20 (Velkonite) et 30 (Orvium) au niveau 1, soit 15 % de plus par niveau.

### Entrepôt de ressources {#resource-storage}

- **Banque** : garde la Velkonite et l’Orvium séparés, et en contient une quantité différente de chacun : **240 de chaque au niveau 1**, jusqu’à 7 680 de Velkonite et 3 840 d’Orvium au niveau 20 (niveau 5 : 720 et 560 ; niveau 10 : 1 920 et 1 440).
- **Limite** : un jour de production de son collecteur au niveau 1, jusqu’à quatre jours au niveau 20. Le réservoir d’un collecteur contient trois jours : à partir du niveau 13, la banque contient donc au moins un réservoir plein.
- **Au-dessus de la limite** : si une banque contient plus que sa limite (le versement de la mise à jour 0.4.10 a pu la laisser ainsi), rien n’est retiré, mais Récupérer n’ajoute plus de ce minerai tant que vous n’en avez pas utilisé un peu.
- Le minerai y entre en le récupérant d’un collecteur, ou depuis votre inventaire par la [Baie à minerai](#ore-bay), et n’en sort que vers la Fonderie et le Centre de recherche. Il ne revient jamais dans votre inventaire.
- **Le minerai en réserve est conservé** lors de la réinitialisation de saison.
- **Énergie** : 10 au niveau 1, soit 10 % de plus par niveau. Il ne peut pas être éteint.

### Fonderie {#forgery}

- **Plaques** : la Fonderie fabrique une **Velkonite Reinforced Plate** à partir de Velkonite et une **Orvium Reinforced Plate** à partir d’Orvium : **40 Velkonite** ou **80 Orvium** par plaque au niveau 1, en baissant à chaque niveau jusqu’à 30 et 60 au niveau 20 (jamais moins de 75 %).
- **Lots** : un seul lot d’un seul type de plaque à la fois, **10 plaques au niveau 1** et 5 de plus pour chaque niveau supérieur. Le minerai quitte l’Entrepôt de ressources dès que le lot commence, et chaque plaque prend **10 secondes**. Les plaques sont fabriquées l’une après l’autre, y compris pendant votre absence.
- **Récupérer les plaques** : déplace les plaques terminées dans votre inventaire tant que votre **vaisseau est amarré**, et le reste du lot continue. Un nouveau lot peut commencer une fois la Fonderie vide.
- Un lot en cours se termine même si vous éteignez la Fonderie ou l’améliorez. Un **nouveau** lot exige que la Fonderie soit allumée, pas en cours d’amélioration, et que l’énergie du Skylab soit à l’équilibre.
- **Énergie** : 30 au niveau 1, soit 15 % de plus par niveau.
- **Non vendable** : les plaques que fabrique la Fonderie ne peuvent pas être vendues aux [Enchères](/wiki/03-Mechanics/Auction.md#marketable-items), sinon elles seraient la plus grosse marchandise de son Marché. Elles servent toujours de matériau à l’Assemblage et à la Forge.

### Les construire {#building-them}

Les deux collecteurs coûtent chacun **10 Ship Fragments, 20 000 crédits et 500 Thulium**, l’Entrepôt de ressources **10 Ship Fragments, 5 000 crédits et 250 Thulium** et la Fonderie **10 Ship Fragments, 5 000 crédits et 500 Thulium** ; les quatre exigent le Noyau au niveau 5.

- Les Ship Fragments sont prélevés dans votre inventaire (pas dans la cache de transport) et votre vaisseau doit être amarré. La fiche de construction montre ce que vous avez face à ce qu’il faut, et ce qui vous manque.
- Ils consomment de l’énergie. Avant la construction, la fiche montre votre bilan énergétique actuel et après : **construire peut mettre une station en déficit** quand son Solaire est en retard sur les autres modules, et un seul déficit arrête toutes les fermes et tous les collecteurs. Éteignez un module, ou améliorez d’abord Solaire.
- Les deux collecteurs sont suspendus à des structures au-dessus de la station, l’Entrepôt de ressources se trouve au port nord-est du Noyau et la Fonderie à son port nord-ouest.

## Le Centre de recherche {#the-research-centre}

Le neuvième module transforme des ressources en science et recherche les technologies dont l’Assemblage a besoin avant de fabriquer quoi que ce soit de nouveau. Il se construit à partir du niveau 10 du Noyau, a les niveaux 1 à 10, consomme de l’énergie et ne peut pas être éteint. Ses chiffres, ce qu’il brûle comme carburant, le boost et tout l’arbre des technologies sont sur la page [Recherche](/wiki/03-Mechanics/Research.md). Les technologies les plus hautes demandent aussi de la Dark Matter, que vous ajoutez au Centre : [Dark Matter et Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md) dit comment l’obtenir. Les niveaux du Module Moteurs, du Module Défense et du Module Radar sont aussi des technologies, recherchées ici (voir [Recherche](/wiki/03-Mechanics/Research.md#module-technologies)).

## Le pont et le Noyau 2 {#the-bridge-and-core-2}

L’amélioration du Noyau au **niveau 10** construit un **pont** et un second Noyau. Le pont s’amarre au port nord du Noyau, là où se trouvait Solaire, et le relie à l’autre bout au **Noyau 2**.

- **Coût** : l’étape du niveau 9 au niveau 10 coûte **2 000 Thulium** en plus de ses 38 443 crédits, et dure autant qu’avant, 1 h 20 min. Le pont et le Noyau 2 ne coûtent rien de plus et ne prennent aucun temps propre. Une amélioration déjà en cours garde le prix auquel elle a été lancée, et un Noyau au niveau 10 ou plus ne paie rien.
- **Le Noyau 2 n’a pas de niveau** : il n’y a rien à améliorer ni à payer. Il offre à votre station **six emplacements de module de plus**, et la carte du Noyau indique combien sont libres.
- **Solaire déménage** : Solaire quitte le port nord du Noyau, que le pont occupe désormais, pour le port nord du Noyau 2, à l’autre bout de la station. Son niveau, son énergie et une amélioration en cours ne changent pas.
- **Une règle, pas une construction** : la place de chaque module découle du seul niveau du Noyau. Le pont apparaît à l’instant où l’amélioration du Noyau vers le niveau 10 se termine (un son discret et un message vous le disent), et un Skylab dont le Noyau est déjà au niveau 10 ou plus l’a au prochain coup d’œil. Aucun module n’est perdu ni supprimé, et seul Solaire change de place.
- **Emplacements** : l’**Imprimante à munitions** prend l’emplacement nord-est du Noyau 2, l’**Usine à roquettes** l’emplacement nord-ouest et la **Baie à minerai** sa structure est ; les trois autres restent libres pour les modules à venir. Les trois ne se construisent que lorsque le Noyau 2 existe : avant cela, le bouton de construction affiche « Nécessite Noyau 2 ».
- **Niveaux** : un module du Noyau 2 suit le niveau du Noyau comme tout autre module : aucun ne le dépasse, donc le Noyau 2 ajoute des emplacements, pas des niveaux.

### Imprimante à munitions {#ammo-printer}

L’Imprimante à munitions imprime des munitions laser à partir de rien, un type à la fois : ni minerai ni crédits, seulement de l’énergie. Elle a les niveaux 1 à 20.

- **Production** : **x2** (Advanced Plasma) **100 par heure au niveau 1, 2 000 au niveau 20** (100 de plus à chaque niveau) ; **x3** (Ultra Core) la moitié, de 50 à 1 000 ; **x4** (Experimental Fusion Core) un quart, de 25 à 500.
- **Mode** : vous choisissez x2, x3 ou x4 sur sa carte ou sa fiche. Un changement garde les heures déjà stockées et les compte ensuite au taux du nouveau mode.
- **Stock** : un jour, 24 heures de production au niveau et dans le type en cours (2 400 x2 au niveau 1, 48 000 au niveau 20). Le temps hors ligne compte, et un stock plein s’arrête simplement.
- **Récupérer** : déplace les unités entières dans votre inventaire tant que votre **vaisseau est amarré**. Les munitions n’ont pas de limite de transport, et la fraction d’une unité reste et continue de compter.
- **Énergie** : 40 au niveau 1, soit 20 % de plus par niveau. Lors d’une panne, elle s’arrête comme les fermes et les collecteurs, et ce qu’elle contient reste et peut être récupéré.
- **Construction** : 20 000 crédits, 500 Thulium et 10 Ship Fragments (pris dans votre inventaire, vaisseau amarré), sur le Noyau 2 uniquement. Ses améliorations coûtent de 21 000 crédits et 140 Thulium à 5 600 000 crédits et 11 000 Thulium, et durent autant que celles de la Fonderie, de 5 minutes à 24 heures et 5 j 13 h en tout (voir les tableaux plus bas).
- **Non vendable** : ce qu’elle imprime ne peut pas être vendu aux [Enchères](/wiki/03-Mechanics/Auction.md#marketable-items).

### Usine à roquettes {#rocket-factory}

L’Usine à roquettes construit des roquettes de la boutique à partir de rien, un type à la fois. Elle a les niveaux 1 à 20.

- **Ce qu’elle fabrique** : une seule des douze roquettes de la boutique, celle que vous choisissez : Lancet, Rivet, Scatter ou Ember, gammes I, II et III. Le N.U.K.E. et le N.I.K.E. ne sont jamais fabriqués.
- **Production** : gamme III **0,5 par heure au niveau 1, 10 au niveau 20** (0,5 de plus à chaque niveau), gamme II 1,25 fois cela et gamme I le double. Seules les roquettes entières comptent : la fraction d’une roquette reste et continue de compter.
- **Stock** : un jour, 24 heures de production au niveau et avec la roquette en cours (240 de gamme III au niveau 20). Le temps hors ligne compte, un stock plein s’arrête simplement, et un changement de roquette garde les heures déjà stockées.
- **Récupérer** : déplace les roquettes dans votre inventaire tant que votre **vaisseau est amarré**, autant que vous pouvez en transporter : au plus 5 000 de gamme I, 2 000 de gamme II et 500 de gamme III, la limite de la boutique elle-même. Ce qui ne rentre pas reste dans l’usine.
- **Énergie** : 24 au niveau 1, soit 15 % de plus par niveau. Lors d’une panne, elle s’arrête comme l’imprimante.
- **Construction** : 20 000 crédits, 500 Thulium et 15 Ship Fragments (pris dans votre inventaire, vaisseau amarré), sur le Noyau 2 uniquement. Ses améliorations coûtent le quart de celles de l’imprimante, de 5 300 crédits et 35 Thulium à 1 400 000 crédits et 2 800 Thulium, et durent autant : 5 j 13 h en tout.
- **Non vendable** : ce qu’elle construit ne peut pas être vendu aux [Enchères](/wiki/03-Mechanics/Auction.md#marketable-items).

### Baie à minerai {#ore-bay}

La Baie à minerai verse dans l’Entrepôt de ressources le minerai que vous transportez. Une [excavatrice géante](/wiki/03-Mechanics/Giant-Excavator.md) dépose du Velkonite et de l’Orvium dans des caisses qui vont dans votre cargaison, où aucun module ne s’en sert ; la Baie à minerai est le chemin d’ici jusqu’à la réserve, où la Fonderie et le Centre de recherche le prennent. Elle a les niveaux 1 à 20.

- **Ce qu’elle transfère** : le **Velkonite et l’Orvium**, les deux minerais que garde l’Entrepôt de ressources. La Cataclysite et le Quorvium sont un carburant que le Centre de recherche et la [Forge](/wiki/06-Items/Forge.md) prennent directement dans votre inventaire, et le Thulium va sur votre compte quand vous le ramassez.
- **Dans un seul sens** : de votre inventaire vers l’Entrepôt de ressources, jamais en sens inverse. Seul le minerai libre de votre inventaire est transféré, jamais celui du Cache de transport.
- **Comment** : votre **vaisseau doit être amarré**. Un transfert est instantané : sur la fiche de la Baie à minerai, choisissez le minerai, saisissez une quantité ou appuyez sur Max, puis sur **Transférer**. La fiche montre ce que vous transportez et ce que la réserve contient par rapport à sa capacité.
- **Quota** : le niveau fixe la quantité de minerai transférée par heure, **30 au niveau 1, 960 au niveau 20**, et elle en garde jusqu’à une journée (720 au niveau 1, 23 040 au niveau 20). Une Baie neuve commence avec une journée pleine, et une amélioration garde ce qui était stocké. Un transfert est coupé au minerai que vous transportez, à la place qu’il reste dans l’Entrepôt de ressources et au quota, et la fiche dit lequel. Une journée de quota vaut environ trois fois ce que l’Entrepôt de ressources contient d’un minerai au même niveau : c’est donc surtout la place qui arrête un transfert, et le quota ne compte que si vous faites passer le minerai par l’entrepôt encore et encore dans la même journée.
- **Énergie** : 15 au niveau 1, avec 10 % de plus par niveau (92 au niveau 20). Elle peut être éteinte. Lors d’une panne, tant qu’elle est éteinte et pendant son amélioration, elle ne transfère rien.
- **Construction** : 5 000 crédits, 250 Thulium et 10 Ship Fragments (pris dans votre inventaire, vaisseau amarré), sur le Noyau 2 seulement. Ses améliorations coûtent ce que coûtent celles de l’Entrepôt de ressources et prennent autant de temps (voir les tableaux plus bas).
- **Pas un moyen d’avoir plus de minerai** : elle transfère du minerai que vous avez déjà. Une série de l’excavatrice est plafonnée à la source, et la capacité de l’Entrepôt de ressources borne la réserve.

## Le second pont et le Noyau 3 {#the-second-bridge-and-core-3}

L’amélioration du Noyau au **niveau 15** construit un **second pont** et un troisième Noyau, et les quatre modules de l’Expédition y prennent leurs emplacements. Le pont II s’amarre au port nord du Noyau 2, là où se trouvait Solaire, et le relie à l’autre bout de la station au **Noyau 3** : le schéma du niveau 10, une fois de plus.

- **Coût** : l’étape du niveau 14 au niveau 15 coûte **4 000 Thulium** en plus de ses crédits, et dure autant qu’avant, 14 h. Le pont II et le Noyau 3 ne coûtent rien de plus et ne prennent aucun temps propre. Une amélioration déjà en cours garde le prix auquel elle a été lancée, et un Noyau au niveau 15 ou plus ne paie rien.
- **Le Noyau 3 n’a pas de niveau** : il n’y a rien à améliorer ni à payer. Il offre à votre station **quatre emplacements de module de plus**, et la carte du Noyau indique combien sont libres.
- **Solaire déménage encore** : Solaire quitte le port nord du Noyau 2, que le pont II occupe désormais, pour le port nord du Noyau 3, à l’autre bout de la station. Son niveau, son énergie et une amélioration en cours ne changent pas.
- **Une règle, pas une construction** : la place de chaque module découle du seul niveau du Noyau. Le Noyau 3 apparaît à l’instant où l’amélioration du Noyau vers le niveau 15 se termine, et un Skylab dont le Noyau est déjà au niveau 15 ou plus l’a au prochain coup d’œil. Aucun module n’est perdu, et seul Solaire change de place.
- **Emplacements** : le **Module Défense** prend l’emplacement nord-est du Noyau 3, le **Module Radar** l’emplacement nord-ouest, la **Baie des trophées** sa structure est et le **Module Moteurs** sa structure ouest. Ses deux ports sud font face aux modules du Noyau 2 et restent vides. Les quatre ne se construisent que lorsque le Noyau 3 existe : avant cela, le bouton de construction est verrouillé et indique qu’il faut le Noyau au niveau 15.
- **Niveaux** : un module du Noyau 3 suit le niveau du Noyau comme tout autre : aucun ne le dépasse. Les modules Moteurs et Défense s’arrêtent au niveau 5, le module Radar au niveau 3 et la Baie des trophées au niveau 20.
- **Ce qu’une construction demande** : en plus des crédits et du Thulium, des **Ship Fragments** et, pour les modules Moteurs, Défense et Radar, des **Dark Matter Plates** de votre inventaire (pas de la cache de transport), prises vaisseau amarré, ainsi que la **technologie** du niveau, recherchée au Centre de recherche. Une étape qui demande des plaques les demande de la même façon.

**Les technologies.** Chaque niveau des modules Moteurs, Défense et Radar est une technologie de la famille Skylab dans la vue Recherche, recherchée à la suite et nécessaire avant de pouvoir construire ce niveau ou y monter. Les trois modules partagent les durées (le module Radar s’arrête au niveau 3) :

| Niveau | Durée de recherche | Dark Matter |
| :--- | ---: | ---: |
| 1 | 3 h | 0 |
| 2 | 10 h | 5 |
| 3 | 1 d | 10 |
| 4 | 2 d | 15 |
| 5 | 3 d | 20 |

Les technologies des trois modules demandent 115 Dark Matter et 14 j 15 h de recherche au rythme normal (voir [Recherche](/wiki/03-Mechanics/Research.md#module-technologies)).

### Module Moteurs {#engine-module}

Le Module Moteurs abrite les moteurs qui font voler votre Skylab. Il a les niveaux 1 à 5, et chaque niveau accueille un moteur de plus. Les moteurs que vous montez et le poids de toute la station décident de sa vitesse (voir [Poids et vitesse](#weight-and-speed)).

- **Ce qui se monte** : des objets [Engine](/wiki/06-Items/Propulsion.md) avec leurs propulseurs dedans, pris dans votre inventaire : un Engine I, II ou III. Un Adaptive Core ne convient pas : son bonus de vitesse est l’affaire d’un vaisseau. Un moteur garde ses propulseurs et ses bonus de la Forge quand vous le retirez.
- **Comment** : votre **vaisseau doit être amarré** et le Skylab ne doit pas être en route. La carte Moteurs de la fenêtre Univers liste vos moteurs libres : glissez-en un sur un emplacement libre ou cliquez dessus, et cliquez sur un moteur monté pour le retirer. La carte montre aussi la poussée, le poids, la vitesse et la durée d’un saut.
- **Un voyage exige** : le module construit, allumé, pas en amélioration et contenant au moins un moteur.
- **Recherche** : chaque niveau demande sa propre technologie, Module Moteurs I à V (voir le tableau plus haut).
- **Énergie** : 60 au niveau 1, soit 25 % de plus par niveau. Il peut être éteint, mais pas pendant que le Skylab est en route.
- **Construction** : 375 000 crédits, 1 500 Thulium, 20 Ship Fragments et 1 Dark Matter Plate, sur le Noyau 3 uniquement.
- **Amélioration** : le module est hors ligne pendant qu’il s’améliore. L’amélioration du Module Moteurs attend la fin d’un voyage, car la vitesse d’un voyage est fixée au départ.

| Niveau | Moteurs | Crédits | Thulium | Plaques | Durée |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 1 (la construction) | 1 | 375 000 | 1 500 | 1 | – |
| 2 | 2 | 825 000 | 3 300 | 2 | 2 h |
| 3 | 3 | 1 825 000 | 7 300 | 3 | 6 h |
| 4 | 4 | 4 000 000 | 16 000 | 5 | 1 d |
| 5 | 5 | 8 750 000 | 35 000 | 8 | 2 d |

Les plaques sont des Dark Matter Plates, et la durée est celle de l’amélioration vers le niveau. En tout, les cinq niveaux coûtent 15 775 000 crédits, 63 100 Thulium, 19 plaques et 3 j 8 h d’amélioration.

### Module Défense {#defense-module}

Le Module Défense combat pour votre Skylab. Il abrite les lasers qui tirent sur les aliens des cellules où vole votre Skylab et le chargeur dont ils tirent. Il a les niveaux 1 à 5, et son niveau décide du nombre de lasers qu’il abrite, du nombre de munitions, de ce qu’il peut gagner par heure et du danger des cellules où il peut entrer.

- **Ce qui se monte** : des objets [Laser](/wiki/06-Items/Lasers.md) avec leurs amplificateurs dedans, pris dans votre inventaire : un Quantum Laser I, II ou III, un Starfire-III ou un Helios Beam. Tous les lasers tirent ensemble, une munition chacun par seconde. Les amplificateurs comptent comme sur un vaisseau (dégâts, chance de critique et dégâts critiques) ; un Penetration Amp n’apporte rien ici.
- **Le chargeur** contient des munitions des types de l’Imprimante à munitions et se remplit **uniquement depuis l’Imprimante à munitions**, jamais depuis votre inventaire (voir [Montage et munitions](#fits-and-ammunition)).
- **La porte** : une cellule de difficulté 3, par exemple, ne peut être franchie que par un Skylab dont le Module Défense est au niveau 3 ou plus. Un Skylab sans Module Défense ne peut traverser que l’espace vide et son port.
- **Le budget d’éliminations** est le maximum que le Skylab peut gagner par heure : 108 points de prime au niveau 1 et 630 au niveau 5 (voir [Ce que rapporte un voyage](#what-a-trip-pays)).
- **La coque** grandit avec le niveau (voir [La coque, la destruction et la réparation](#the-hull-and-repair)).
- **Recherche** : chaque niveau demande sa propre technologie, Module Défense I à V (voir le tableau plus haut).
- **Énergie** : 80 au niveau 1, soit 25 % de plus par niveau. Il peut être éteint, mais pas pendant que le Skylab est en route. Un module éteint, en amélioration ou sans énergie est inactif : le Skylab ne combat rien et passe sans combattre.
- **Construction** : 500 000 crédits, 2 000 Thulium, 25 Ship Fragments et 1 Dark Matter Plate, sur le Noyau 3 uniquement.

| Niveau | Lasers | Chargeur (munitions) | Budget d’éliminations (points par heure) | Difficulté maximale |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 1 | 1 300 | 108 | 1 |
| 2 | 2 | 3 600 | 293 | 2 |
| 3 | 3 | 14 000 | 476 | 3 |
| 4 | 4 | 23 000 | 548 | 4 |
| 5 | 5 | 35 000 | 630 | 5 |

| Niveau | Crédits | Thulium | Plaques | Durée |
| :--- | ---: | ---: | ---: | ---: |
| 1 (la construction) | 500 000 | 2 000 | 1 | – |
| 2 | 1 150 000 | 4 600 | 2 | 3 h |
| 3 | 2 750 000 | 11 000 | 4 | 9 h |
| 4 | 6 000 000 | 24 000 | 7 | 1 d 12 h |
| 5 | 14 000 000 | 56 000 | 12 | 3 d |

En tout, les cinq niveaux coûtent 24 400 000 crédits, 97 600 Thulium, 26 plaques et 5 j d’amélioration.

### Module Radar {#radar-module}

Le Module Radar lève le brouillard de la carte de l’univers (voir [Brouillard et scan](#fog-and-scanning)). Il a les niveaux 1 à 3, et un niveau plus élevé scanne une cellule plus vite.

- **Ce qu’il fait** : il scanne **une cellule à la fois**, parmi les cellules voisines d’une cellule que vous connaissez, et garde une **file de trois** : la première est scannée, les autres attendent. Quand un scan est terminé, vous connaissez la cellule, et votre Skylab peut y voler.
- **Durée** : 90 minutes par cellule au niveau 1, 40 au niveau 2 et 15 au niveau 3. Un scan suit l’horloge du serveur, même quand vous êtes absent et pendant que le Skylab vole. Il s’arrête, et le temps n’est pas rattrapé, tant que le module est éteint, en amélioration ou sans énergie et tant que le Skylab est détruit. Un scan coûte du temps et rien d’autre.
- **Tout cartographier** : pour cartographier une à une les 131 cellules que vous ne connaissez pas au départ, il faut 8 j 4 h au niveau 1, 3 j 15 h au niveau 2 et 1 j 9 h au niveau 3.
- **Recherche** : chaque niveau demande sa propre technologie, Module Radar I à III (voir le tableau plus haut).
- **Énergie** : 40 au niveau 1, soit 30 % de plus par niveau. Il peut être éteint, mais pas pendant que le Skylab est en route.
- **Construction** : 250 000 crédits, 1 000 Thulium et 15 Ship Fragments, sur le Noyau 3 uniquement.

| Niveau | Durée du scan | Crédits | Thulium | Plaques | Durée |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 1 (la construction) | 90 min | 250 000 | 1 000 | 0 | – |
| 2 | 40 min | 750 000 | 3 000 | 1 | 4 h |
| 3 | 15 min | 2 250 000 | 9 000 | 3 | 1 d |

En tout, les trois niveaux coûtent 3 250 000 crédits, 13 000 Thulium, 4 plaques et 1 j 4 h d’amélioration.

### Baie des trophées {#trophies-bay}

La Baie des trophées garde ce que rapportent les éliminations de votre Skylab jusqu’à ce que vous le récupériez. Elle a les niveaux 1 à 20 et ne demande aucune technologie.

- **Ce qu’elle contient** : crédits, Thulium, expérience, honneur et le butin des éliminations.
- **La capacité** se compte en **points de prime** : une élimination ajoute la prime de son alien, les crédits divisés par 200 plus le Thulium, quoi qu’il laisse tomber (les chiffres d’Alpha dans tous les mondes). Elle contient 650 points au niveau 1 et 45 000 au niveau 20.
- **Pleine** : une baie pleine fait **cesser le feu** au Skylab : rien n’est éliminé, payé ni compté et aucune munition n’est dépensée jusqu’à ce que vous récupériez (la coque continue de se régénérer). Un message, une notification, une pastille ambre **Baie pleine** dans la barre de la station, un avis sur la page du Skylab et l’info-bulle de la ligne Skylab de la barre latérale l’indiquent.
- **Récupérer** dans la fenêtre Univers, vaisseau amarré : les crédits et le Thulium vont sur votre compte, l’expérience et l’honneur à votre pilote et le butin dans votre inventaire. Deux récupérations simultanées ne paient qu’une fois.
- **Le butin** est tiré pour chaque élimination d’après ce que laisse l’alien, jamais de Dark Matter, d’Ancient Control Units, de N.I.K.E. ni de N.U.K.E. Il est **non vendable** : il ne peut pas être vendu aux [Enchères](/wiki/03-Mechanics/Auction.md#marketable-items).
- **Énergie** : 20 au niveau 1, soit 10 % de plus par niveau. Elle peut être éteinte, mais pas pendant que le Skylab est en route.
- **Construction** : 100 000 crédits, 400 Thulium et 10 Ship Fragments, sur le Noyau 3 uniquement. Ses améliorations coûtent de 117 500 crédits et 470 Thulium (15 minutes) à 2 325 000 crédits et 9 300 Thulium (1 j 13 h) : 14 722 500 crédits et 58 890 Thulium en tout, et 6 j 8 h.

| Niveau | Capacité (points) | Crédits | Thulium | Durée |
| :--- | ---: | ---: | ---: | ---: |
| 1 (la construction) | 650 | 100 000 | 400 | – |
| 2 | 810 | 117 500 | 470 | 15 min |
| 5 | 1 600 | 195 000 | 780 | 34 min |
| 10 | 4 800 | 450 000 | 1 800 | 2 h 18 min |
| 15 | 15 000 | 1 025 000 | 4 100 | 9 h 14 min |
| 20 | 45 000 | 2 325 000 | 9 300 | 1 d 13 h |

Le temps que met une baie à se remplir quand le Skylab gagne tout le budget d’éliminations de son niveau de défense (une baie plus petite se remplit plus vite, un budget plus petit plus lentement) :

| Niveau de défense | Baie niveau 1 | Baie niveau 5 | Baie niveau 10 | Baie niveau 15 | Baie niveau 20 |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 1 | 6 h 1 min | 14 h 49 min | 1 d 20 h | 5 d 19 h | 17 d 9 h |
| 2 | 2 h 13 min | 5 h 28 min | 16 h 23 min | 2 d 3 h | 6 d 10 h |
| 3 | 1 h 22 min | 3 h 22 min | 10 h 5 min | 1 d 8 h | 3 d 22 h |
| 4 | 1 h 11 min | 2 h 55 min | 8 h 46 min | 1 d 3 h | 3 d 10 h |
| 5 | 1 h 2 min | 2 h 32 min | 7 h 37 min | 23 h 49 min | 2 d 23 h |

## Poids et vitesse {#weight-and-speed}

Chaque module pèse quelque chose, en **unités de masse (MU)**, et une station plus lourde vole plus lentement. Un module pèse plus à chaque niveau, un module non construit ne pèse rien et un module en amélioration pèse le niveau qu’il a. Les moteurs et les lasers que vous montez ne comptent pas : le poids du module les couvre.

| Module | Niveau 1 | Niveau 5 | Niveau 10 | Niveau 15 | Niveau maximal |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Noyau | 100 | 148 | 208 | 268 | 328 |
| Solaire | 60 | 84 | 114 | 144 | 174 |
| Ferme à crédits | 60 | 84 | 114 | 144 | 174 |
| Ferme à Thulium | 80 | 118 | 166 | 214 | 262 |
| Collecteur de Velkonite | 70 | 92 | 120 | 148 | 176 |
| Collecteur d’Orvium | 70 | 92 | 120 | 148 | 176 |
| Entrepôt de ressources | 70 | 92 | 120 | 148 | 176 |
| Fonderie | 80 | 112 | 152 | 192 | 232 |
| Centre de recherche | 60 | 89 | 125 | – | 125 |
| Imprimante à munitions | 60 | 84 | 114 | 144 | 174 |
| Usine à roquettes | 60 | 84 | 114 | 144 | 174 |
| Baie à minerai | 40 | 53 | 69 | 85 | 101 |
| Module Moteurs | 80 | 144 | – | – | 144 |
| Module Défense | 100 | 180 | – | – | 180 |
| Module Radar | 30 | – | – | – | 39 |
| Baie des trophées | 50 | 60 | 73 | 85 | 98 |
| **La station entière : tous les modules présents à ce niveau du Noyau, à ce niveau** | 300 | 824 | 1 537 | 2 353 | 2 734 |

Le niveau maximal est 20, sauf pour le Centre de recherche (10), les modules Moteurs et Défense (5) et le module Radar (3). La station entière pèse 2 353 MU au niveau 15 du Noyau et 2 734 MU au niveau 20.

- **La poussée** est le calcul des moteurs des vaisseaux, sans vitesse de base : un moteur apporte sa vitesse de base plus la vitesse fixe de ses propulseurs, multipliée par leurs multiplicateurs ; les moteurs sont classés du meilleur au moins bon, les quatre premiers comptent pour 100 % et le cinquième pour 85 % (le module en abrite cinq au plus) ; et les quatre meilleurs bonus de vitesse s’y ajoutent. Une station sans moteur n’a pas de poussée.
- **La vitesse** vaut 60 fois la poussée divisée par le poids de la station, en unités par seconde, et un saut entre deux cellules voisines fait 15 000 unités. Sous l’énergie, la page du Skylab affiche la ligne « Poids 2 353 MU, vitesse 7,8 unités/s, un saut 32 min ».
- **Fixée au départ** : la vitesse d’un voyage est calculée à son départ, d’après le poids et la poussée de cet instant. Une amélioration qui se termine en route, ou un moteur que vous changez pendant que le Skylab est stationné, compte pour le voyage suivant.

Ce que font les moteurs pour une station dont tous les modules sont au niveau 15 (le Module Moteurs au niveau qui abrite les moteurs) :

| Moteurs montés | Poids (MU) | Poussée | Vitesse (unités par seconde) | Un saut | À travers la carte (14 sauts) |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 1 Engine I (Module Moteurs niveau 1) | 2 289 | 2,0 | 0,05 | 3 j 6 h | 45 j 11 h |
| 3 Engine II, chacun avec 2 Impulse Thruster II (niveau 3) | 2 321 | 73,6 | 1,90 | 2 h 11 min | 1 j 7 h |
| 5 Engine III, chacun avec 3 Impulse Thruster IV (niveau 5) | 2 353 | 305,5 | 7,79 | 32 min | 7 h 29 min |

Au niveau 20 du Noyau, la station pèse 16 % de plus, et les meilleurs moteurs mettent 37 minutes par saut et 8 h 42 min pour traverser la carte.

## Expéditions {#expeditions}

Une **expédition** est un voyage de votre Skylab à travers la **carte de l’univers**. Il vole jusqu’à une cellule, y chasse les aliens avec les lasers de son Module Défense et remplit la Baie des trophées avec ce que rapportent les éliminations. Tout suit l’horloge du serveur, donc cela continue quand vous êtes déconnecté, et aucun joueur ne peut attaquer le Skylab : seul le danger de la cellule lui fait mal (voir [La coque, la destruction et la réparation](#the-hull-and-repair)). Vous planifiez un voyage dans la fenêtre **Univers**, qu’ouvre le bouton Univers de l’en-tête de la page du Skylab.

Ce qu’il faut : un Noyau au niveau 15, une corporation (son port est le port d’attache de votre Skylab) et un monde ; pour un voyage, un Module Moteurs avec un moteur monté ; pour gagner quelque chose, un Module Défense avec un laser et des munitions de votre Imprimante à munitions, et une Baie des trophées où les garder. Tout le reste continue pendant que le Skylab est absent : les fermes, les collecteurs, la Fonderie, l’Imprimante, l’Usine, la Baie à minerai et le Centre de recherche suivent leurs propres horloges, et votre vaisseau peut être piloté comme d’habitude.

### La carte de l’univers {#the-universe-map}

La carte est la **couche propre** du Skylab, pas les secteurs du jeu ni une vue de ceux-ci : ses cellules ne sont pas des cartes du jeu, les portails n’y figurent pas, rien n’y est piloté en temps réel et ses aliens ne sont qu’un nombre et un danger. Elle touche le reste du jeu par ce qu’elle rapporte : crédits, Thulium, expérience, honneur, butin et éliminations pour les missions.

- **Le champ** : 15 colonnes et 10 lignes de cellules hexagonales, **150 en tout**. Une cellule a un code, la lettre de la colonne et le numéro de la ligne (A1 à O10), et, une fois que vous la connaissez, un nom et un type.
- **Ports** : chaque corporation a un **port**, une cellule de difficulté 0 : celui de Mars est H3, celui de Terra D8 et celui de Galactic L8. Votre Skylab démarre dans le port de votre corporation et y revient après une réinitialisation. On n’y chasse rien et rien n’y attaque le Skylab.
- **La difficulté** va de 1 à 5 et croît avec la distance au port le plus proche : les six cellules voisines d’un port sont toujours de difficulté 1, et chaque saut de plus en ajoute une, jusqu’à 5. Environ un cinquième des cellules est d’un cran plus facile que ne le dit leur distance et un quart d’un cran plus difficile, et quelques-unes sont de l’**espace vide**, difficulté 0.
- **Types** : un **nid** contient tous les aliens de sa difficulté et une **dérive**, la plupart des cellules, trois cinquièmes d’entre eux. L’espace vide ne contient rien ni personne, et un Skylab peut le traverser sans aucun Module Défense.
- **Une carte par monde** : tous les pilotes d’un monde voient la même carte, chaque monde a la sienne, et chaque saison (la réinitialisation) en fait une nouvelle.

Les aliens d’un nid, par difficulté (une dérive en contient trois cinquièmes, arrondis) :

| Difficulté | Aliens |
| :--- | :--- |
| 1 | 30 [Seekers](/wiki/04-Aliens/Seeker.md) |
| 2 | 20 Seekers et 10 [Phantasms](/wiki/04-Aliens/Phantasm.md) |
| 3 | 20 Phantasms, 10 [Bulwarks](/wiki/04-Aliens/Bulwark.md) et 5 [Goombahs](/wiki/04-Aliens/Goombah.md) |
| 4 | 20 Bulwarks, 10 Goombahs et 5 [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| 5 | 6 [Slumbering Voids](/wiki/03-Mechanics/Dormant-Swamp.md), 3 [Dormant Pulses](/wiki/05-Swarms/Dormant-Swarm.md) et 1 Dormant Force |

### Brouillard et scan {#fog-and-scanning}

Vous ne voyez que les cellules que vous connaissez.

- **Au début d’une saison**, vous connaissez votre port et les deux anneaux de cellules autour de lui : **19 cellules**, les mêmes pour toute corporation.
- **Une cellule devient connue** quand votre Skylab la traverse ou s’y arrête, et quand le radar finit de la scanner.
- **Une cellule que vous ne connaissez pas** ne montre rien d’elle-même : ni son type, ni sa difficulté, ni son nom, ni ses aliens. Une cellule voisine d’une cellule connue est marquée d’un **?** et peut être scannée ; toute autre cellule inconnue est sombre.
- **Une cellule connue** montre dans son panneau son code, son type, sa difficulté, son nom et ses aliens.
- **On ne vole** que vers des cellules connues.
- **Scanner** : choisissez une cellule **?** et appuyez sur **Scanner cette cellule**. Le radar scanne une cellule à la fois et garde une file de trois ; on peut retirer une cellule de la file, et **Tout annuler** la vide. La durée d’un scan est indiquée au [Module Radar](#radar-module).

### Le voyage {#the-trip}

Cliquez sur une cellule connue de la carte : le panneau de la cellule montre l’**aperçu** du voyage, que le serveur planifie avec votre Skylab tel qu’il est maintenant, et **Partir** y envoie le Skylab. Il vole un saut à la fois à la vitesse de ses moteurs, arrive dans la cellule et **y chasse jusqu’à ce que vous donniez un autre ordre**. **Rappeler** le renvoie à son port par le plus court chemin connu.

- **L’itinéraire** compte le moins de sauts possible sur des cellules que vous connaissez et dont la difficulté est permise par le niveau de votre Module Défense. Parmi les itinéraires de même longueur, on en choisit un, toujours le même.
- **L’horloge** est celle du serveur : l’arrivée est fixée quand le Skylab part, et un voyage continue quand vous êtes déconnecté. Un nouvel ordre donné en route prend effet à la cellule suivante : le saut en cours est terminé.
- **Ce qui bloque un ordre** : pas de Module Moteurs, ou un module éteint ou en amélioration ; pas de moteur monté ; pas assez d’énergie ; un Skylab détruit ; la cellule où il se trouve déjà ; une cellule que vous ne connaissez pas ; une cellule trop difficile pour votre Module Défense ; aucun itinéraire connu.
- **En route**, les quatre modules de l’Expédition ne peuvent pas être allumés ni éteints, le Module Moteurs ne peut pas être amélioré et rien ne peut être monté ni retiré. En chemin, il rencontre les aliens des cellules qu’il traverse à la moitié du rythme qu’il aurait s’il y restait.
- **Messages** : un message vous dit quand le Skylab arrive, quand il est détruit ou réparé et quand sa baie est pleine, et les quatre s’accompagnent d’un son discret qui leur est propre.

Ce que dit l’aperçu, dans l’ordre de ses lignes (chaque chiffre est celui du serveur, pour l’équipement que votre Skylab a maintenant) :

| Ligne | Ce qu’elle dit |
| :--- | :--- |
| **Trajet** | les sauts et la durée du voyage |
| **Arrivée** | le moment où il arriverait, selon votre horloge |
| **En chemin** | environ combien d’aliens il rencontre dans les cellules qu’il traverse |
| **Éliminations par heure** | ce que le séjour élimine par heure, et quelle limite s’applique : les aliens de passage, le budget d’éliminations, les dégâts de vos lasers ou vos munitions |
| **Primes par heure** | ce que valent ces éliminations, en points de prime |
| **Vos dégâts** | ce que font vos lasers par seconde avec la meilleure munition du chargeur |
| **La cellule exige** | les dégâts à partir desquels la régénération de la coque tient tout juste la cellule au rythme qu’elle rapporte : en dessous, la coque baisse |
| **Coque** | Tient, ou Détruit après un certain temps |
| **Munitions** | combien de temps durent les munitions du chargeur, ou qu’elles suffisent pour tout le séjour |
| **Baie des trophées** | au bout de combien de temps elle est pleine, ou qu’elle ne se remplit pas à ce rythme |

Au-dessus des lignes, un **avertissement** signale quand le voyage ne rapporterait rien : rien à combattre dans la cellule, aucun laser monté, un chargeur vide que rien n’alimente, aucune Baie des trophées ou un Module Défense inactif.

### Ce que rapporte un voyage {#what-a-trip-pays}

Une élimination rapporte ce que rapporte son alien dans votre monde : ses crédits, son Thulium, son expérience et son honneur multipliés par la paie du monde (1, 2 et 3 en Alpha, Beta et Gamma), et son butin. Rien ne s’y ajoute : ni booster, ni premium, ni bonus de formation, ni boost de clan, ni expérience pour vos drones.

Les éliminations par heure sont la plus petite de trois limites : les aliens de passage, le **budget d’éliminations** du niveau de votre Module Défense, et ce que vos lasers et vos munitions peuvent faire. Le budget garde un Skylab sans surveillance comme un complément des fermes et non comme un second emploi : 108, 293, 476, 548 et 630 points de prime par heure aux niveaux de défense 1 à 5, où un point vaut 1 Thulium ou 200 crédits. **Une cellule paie selon son palier** : un Skylab touche le plus bas entre le budget de son niveau de défense et celui de la difficulté de la cellule, donc un Skylab de Défense 5 dans une cellule de difficulté 1 y gagne ce que gagne un Skylab de Défense 1.

Ce que rapporte au plus un jour dans une cellule (Alpha ; Beta et Gamma paient 1,6 et 2 fois plus) :

| Difficulté | Points de prime par heure | Éliminations par jour | Thulium par jour | Crédits par jour |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 108 | 288 | 1 152 | 288 000 |
| 2 | 293 | 469 | 3 124 | 780 911 |
| 3 | 476 | 224 | 5 524 | 1 181 375 |
| 4 | 548 | 86 | 5 503 | 1 528 510 |
| 5 | 630 | 32 | 5 255 | 1 972 329 |

Un jour dans une cellule vaut environ deux heures de chasse à la main dans cette cellule (3,4 heures en difficulté 4). À partir de la difficulté 3, c’est environ 30 % de ce que fait en Thulium une Ferme à Thulium au niveau 15 du Noyau (18 240 par jour) et 0,6 à 1,1 fois ce que fait en crédits une Ferme à crédits de ce niveau (1 836 000 par jour). Une dérive de difficulté 2 contient moins d’aliens que son budget n’en paie et rapporte un peu moins.

Le **butin** d’une élimination est tiré d’après ce que laisse son alien : Ship Fragments, minerais, Reinforced Hull Plates et Power Cores, et, à partir de la difficulté 5, des munitions Ultra Core et Experimental Fusion Core.

### La coque, la destruction et la réparation {#the-hull-and-repair}

Le Skylab a une **coque**, une réserve de points de vie, qui **se régénère de 5 % d’elle-même par heure**, même sous le feu. Les aliens qu’il combat l’abîment, en proportion de leur nombre, de leur force et de la durée du combat : l’aperçu dit si la coque tient et, sinon, au bout de combien de temps le Skylab est détruit. Elle est de 4 000 000 au niveau 15 du Noyau avec le Module Défense au niveau 1, de 12 % de plus pour chaque niveau du Noyau au-delà de 15 et de plus avec un niveau de défense plus élevé. Un Skylab sans Module Défense a la coque du niveau 1 et ne combat rien.

| Niveau de défense | Noyau niveau 15 | Noyau niveau 20 |
| :--- | ---: | ---: |
| 1 | 4 000 000 | 7 049 367 |
| 2 | 4 800 000 | 8 459 240 |
| 3 | 6 000 000 | 10 574 050 |
| 4 | 8 800 000 | 15 508 607 |
| 5 | 11 200 000 | 19 738 227 |

- **Détruit** : quand la coque est épuisée, le Skylab est détruit là où il se trouvait, à cet instant, et le voyage est terminé. Ce que contenait la Baie des trophées y reste. Tous les producteurs de la station s’arrêtent à partir de cet instant : les fermes, les collecteurs, l’Imprimante, l’Usine et la Baie à minerai ne produisent rien, la Fonderie ne lance aucun nouveau lot et le Centre de recherche aucune nouvelle recherche (un lot ou une recherche déjà en cours continue), et les scans du radar sont à l’arrêt.
- **Réparation** : appuyez sur **Réparer** dans la fenêtre Univers. Elle est gratuite et dure **60 secondes** ; ensuite la coque est entière et le Skylab est de retour dans la cellule où son voyage a commencé. La production reprend à la fin de la réparation. Rien n’est perdu, sauf le temps.
- **Messages** : la page du Skylab affiche un avis et une pastille sur la barre de la station tant que le Skylab est détruit ou en réparation, et l’info-bulle de la ligne Skylab de la barre latérale l’indique aussi.

### Montage et munitions {#fits-and-ammunition}

**Montage.** Les moteurs vont dans le Module Moteurs et les lasers dans le Module Défense, un par emplacement, pris parmi les objets libres de votre inventaire : pas sur un vaisseau, pas dans la cache de transport. Monter et retirer demandent votre **vaisseau amarré** et le Skylab **pas en route** ; un Skylab stationné peut être rééquipé, et les nouveaux taux comptent à partir de cet instant. Un objet monté garde ses bonus de la Forge et ce qu’il contient (propulseurs, amplificateurs) et est **réservé** : il ne peut pas être mis sur un vaisseau, supprimé, mis aux Enchères, placé dans la cache de transport ni utilisé par la Forge et l’Assemblage tant que vous ne l’avez pas retiré, et le Hangar, la fiche de vente des Enchères et l’Assemblage l’affichent grisé.

**Munitions.** Le chargeur contient des munitions des types que fabrique l’Imprimante à munitions et tire d’abord le **multiplicateur le plus haut**, une munition par laser et par seconde. Il se remplit **uniquement depuis l’Imprimante à munitions**, jamais depuis votre inventaire :

- **Alimenter depuis l’Imprimante à munitions** activé : ce que fabrique l’Imprimante va d’abord dans le chargeur, dans la limite de la place ; seul le reste attend dans la trémie de l’Imprimante que vous le récupériez.
- **Alimentation** désactivée : ce que fabrique l’Imprimante attend dans sa trémie, et **Charger** déplace dans le chargeur ce que contient la trémie, vaisseau amarré, dans la limite de la place.
- On ne décharge pas : les munitions sont tirées ou gardées.

Un Skylab sans lasers, sans munitions ou sans Baie des trophées ne combat rien, et rien ne lui fait de mal non plus.

### Éliminations et missions {#expedition-kills}

Les éliminations d’une expédition ne font avancer une **étape d’élimination de vos missions** que si l’étape **ne nomme aucun secteur**, jusqu’à **250 éliminations par jour** (UTC) et seulement celles de l’alien que l’étape nomme. Une cellule n’est pas un secteur : une étape qui en nomme un (`x-1` à `x-4`, `DS-x` ou `x-4` d’une autre corporation) ne les compte donc jamais, pas même dans une cellule de même difficulté. En pratique, ce sont les grandes chasses de la ligne des Défis dont les aliens vivent dans une cellule, et aucune des missions des niveaux 1 à 8. Une mission avec une limite de temps, ou une étape avec une limite de coque, ne les compte pas non plus. Seules les étapes d’élimination comptent : les objets, les visites et les séjours exigent votre présence. La carte du Skylab dans la fenêtre Univers affiche « Éliminations d’expédition aujourd’hui : N sur 250 ».

Les éliminations ne rapportent aucun point de réinitialisation et ne comptent pour aucune ligne de clan, aucune statistique d’éliminations ni aucun point de classement (voir [Missions](/wiki/03-Mechanics/Quests.md#where-it-counts)).

### Votre clan le voit {#clan-skylabs}

Les pilotes de votre clan voient où sont les Skylabs des autres : la colonne **Skylab** de la liste des membres donne la cellule (« Amarré à H3 », « H3, vers K7 dans 3 h 12 min », « Stationné à K7 », « Détruit à H3 »), et la fenêtre Univers les dessine comme de petits losanges dorés, avec le nom du pilote quand vous en pointez un. Seul le clan le voit, une occultation ne cache pas un Skylab et il n’y a aucun interrupteur pour le cacher. Une destruction ne se montre au clan que lorsque son pilote a de nouveau regardé le Skylab ou lui a donné un ordre (voir [Clans](/wiki/03-Mechanics/Clans.md#where-your-clan-mates-are)).

## Mécaniques {#mechanics}

### Construction et amélioration {#building-and-upgrading}

- **Construction** : chaque module se construit séparément. Un module est au niveau 1 dès sa construction, et l’améliorer augmente sa production (ou l’énergie qu’il produit) et son stockage, mais aussi ce qu’il consomme en énergie.
- **Durée et coût** : les améliorations coûtent des crédits et du Thulium et prennent du temps, et chaque module a son propre prix et son propre temps pour chaque niveau (survolez **Améliorer** pour voir le suivant ; les totaux sont plus bas). Le prix est payé au lancement de l’amélioration. Le coût ne dépend pas de la durée. Les modules Moteurs, Défense et Radar prennent en plus des Dark Matter Plates et demandent la technologie du niveau (voir [Le second pont et le Noyau 3](#the-second-bridge-and-core-3)).
- **Minuteurs** : une amélioration tourne sur l’horloge du serveur, elle se termine donc pendant votre absence, des jours plus tard s’il le faut. Lancez-la, déconnectez-vous, revenez : le module est à son nouveau niveau quand vous ouvrez la page Skylab.
- **Durées d’amélioration** : les premiers niveaux sont rapides et les derniers prennent jusqu’à 37 heures, ceux du Noyau jusqu’à 6 jours (voir les tableaux plus bas). Chaque module a son propre minuteur, vous pouvez donc en améliorer plusieurs à la fois.
- **Pause de production** : pendant son amélioration, un module est hors ligne : il ne produit rien et ne consomme pas d’énergie. Solaire fait exception : il continue de produire un quart de son énergie (voir plus bas).
- **Solaire ne produit que 25 % de son énergie pendant son amélioration** : Solaire produit toute l’énergie du Skylab et, pendant son amélioration (24 heures pour le dernier niveau), il produit un quart de l’énergie de son niveau **actuel** ; celle du nouveau niveau prend le relais dès que l’amélioration se termine. Une station complète consomme environ 90 % de ce que Solaire produit à son propre niveau : un quart de cela ne porte donc qu’une station située cinq à six niveaux en dessous de Solaire. Sinon, toutes les fermes et tous les collecteurs s’arrêtent pendant toute l’amélioration, ce que vous avez en réserve reste et peut être récupéré, et la Fonderie ne lance aucun nouveau lot. Un module en cours d’amélioration ou éteint ne consomme pas d’énergie : monter les fermes en même temps que Solaire ne coûte donc rien de plus, et éteindre des modules fait de la place pour les autres ; la Ferme à Thulium consomme de loin le plus d’énergie.

### Ce que ça coûte {#what-it-costs}

Le prix de toute la montée, la construction plus chaque amélioration, jusqu’au niveau 10 et jusqu’au niveau 20. Le Noyau est toujours là et ses étapes coûtent des crédits, avec 2 000 Thulium de plus à l’étape vers le niveau 10 et 4 000 de plus à l’étape vers le niveau 15 ; le Centre de recherche a les niveaux 1 à 10 et ses chiffres sont sur la page [Recherche](/wiki/03-Mechanics/Research.md). L’Imprimante à munitions, l’Usine à roquettes et la Baie à minerai se construisent sur le Noyau 2, donc seulement quand le Noyau est au niveau 10, et leur niveau 1 est la construction. Les quatre modules de l’Expédition se construisent sur le Noyau 3, donc seulement quand le Noyau est au niveau 15, et les modules Moteurs, Défense et Radar s’arrêtent aux niveaux 5, 5 et 3 : leurs deux chiffres sont toute la montée.

| Module | Crédits jusqu’au niveau 10 | Thulium jusqu’au niveau 10 | Crédits jusqu’au niveau 20 | Thulium jusqu’au niveau 20 |
| :--- | ---: | ---: | ---: | ---: |
| Noyau | 112 326 | 2 000 | 6 647 504 | 6 000 |
| Solaire | 1 219 500 | 1 600 | 35 039 500 | 36 850 |
| Ferme à crédits | 840 000 | 109 | 26 240 000 | 2 399 |
| Ferme à Thulium | 1 154 000 | 4 190 | 32 254 000 | 67 890 |
| Collecteur de Velkonite | 696 000 | 6 950 | 20 996 000 | 78 950 |
| Collecteur d’Orvium | 696 000 | 6 950 | 20 996 000 | 78 950 |
| Entrepôt de ressources | 619 500 | 359 | 18 169 500 | 2 649 |
| Fonderie | 1 224 000 | 2 050 | 35 044 000 | 37 300 |
| Imprimante à munitions | 1 411 000 | 5 140 | 22 031 000 | 47 940 |
| Usine à roquettes | 377 300 | 1 674 | 5 547 300 | 12 494 |
| Baie à minerai | 619 500 | 359 | 18 169 500 | 2 649 |
| Module Moteurs | 15 775 000 | 63 100 | 15 775 000 | 63 100 |
| Module Défense | 24 400 000 | 97 600 | 24 400 000 | 97 600 |
| Module Radar | 3 250 000 | 13 000 | 3 250 000 | 13 000 |
| Baie des trophées | 2 372 500 | 9 490 | 14 722 500 | 58 890 |

Les premières étapes sont bon marché et les dernières chères : l’étape de la Ferme à crédits du niveau 1 au niveau 2 coûte 5 000 crédits et 1 Thulium, celle du niveau 19 au niveau 20 coûte 7 000 000 de crédits et 550 Thulium. Celles de la Ferme à Thulium coûtent 7 000 crédits et 45 Thulium, puis 8 500 000 crédits et 16 000 Thulium. Les améliorations de Solaire coûtent à chaque niveau la même chose que celles de la Fonderie, et les deux collecteurs coûtent autant l’un que l’autre.

Les quatre modules de l’Expédition demandent plus que des crédits et du Thulium : des Ship Fragments pour construire, des Dark Matter Plates et une technologie pour chaque niveau des trois premiers :

| Module | Ship Fragments pour construire | Plaques en tout | Recherche : Dark Matter | Recherche : durée |
| :--- | ---: | ---: | ---: | ---: |
| Module Moteurs | 20 | 19 | 50 | 6 d 13 h |
| Module Défense | 25 | 26 | 50 | 6 d 13 h |
| Module Radar | 15 | 4 | 15 | 1 d 13 h |
| Baie des trophées | 10 | 0 | 0 | – |

Les quatre ensemble : 232 590 Thulium, 58 147 500 crédits, 49 plaques, 115 Dark Matter et 14 j 15 h de recherche. Les plaques sont des Dark Matter Plates, et ce que coûte une plaque est sur [Dark Matter et Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md#how-to-get-a-plate).

### Durées d’amélioration {#upgrade-times}

<!-- upgrade-times:start -->
<!-- Generated from server/Resources/SkylabConfig.json by the test skylab::duration_tests::the_wiki_page_is_the_config (run it with SKYLAB_WIKI_WRITE=1 to rewrite this part). -->

**Durées d’amélioration**, par module (l’amélioration à partir du niveau de la première colonne) :

| Niveau | Noyau | Solaire | Ferme à crédits | Ferme à Thulium | Entrepôt de ressources | Collecteur de Velkonite | Collecteur d’Orvium | Fonderie | Centre de recherche |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 à 2 | 72 s | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 78 s |
| 2 à 3 | 86 s | 15 min | 10 min | 15 min | 10 min | 15 min | 15 min | 15 min | 101 s |
| 3 à 4 | 104 s | 30 min | 15 min | 30 min | 15 min | 20 min | 20 min | 30 min | 132 s |
| 4 à 5 | 124 s | 45 min | 20 min | 45 min | 20 min | 30 min | 30 min | 45 min | 171 s |
| 5 à 6 | 149 s | 1 h | 30 min | 1 h | 30 min | 45 min | 45 min | 1 h | 223 s |
| 6 à 7 | 20 min | 1 h 15 min | 45 min | 1 h 30 min | 45 min | 50 min | 50 min | 1 h 15 min | 20 min |
| 7 à 8 | 30 min | 1 h 30 min | 1 h | 2 h | 1 h | 1 h | 1 h | 1 h 30 min | 30 min |
| 8 à 9 | 50 min | 2 h | 1 h 20 min | 3 h | 1 h 20 min | 1 h 15 min | 1 h 15 min | 2 h | 50 min |
| 9 à 10 | 1 h 20 min | 3 h | 1 h 40 min | 4 h | 1 h 40 min | 1 h 30 min | 1 h 30 min | 3 h | 1 h 20 min |
| 10 à 11 | 2 h 15 min | 4 h | 2 h | 5 h | 2 h | 2 h | 2 h | 4 h | – |
| 11 à 12 | 3 h 30 min | 5 h | 2 h 30 min | 6 h | 2 h 30 min | 3 h | 3 h | 5 h | – |
| 12 à 13 | 5 h 30 min | 6 h | 3 h | 8 h | 3 h | 4 h | 4 h | 6 h | – |
| 13 à 14 | 9 h | 8 h | 3 h 30 min | 10 h | 3 h 30 min | 6 h | 6 h | 8 h | – |
| 14 à 15 | 14 h | 10 h | 4 h | 11 h | 4 h | 8 h | 8 h | 10 h | – |
| 15 à 16 | 1 j | 12 h | 5 h | 12 h | 5 h | 10 h | 10 h | 12 h | – |
| 16 à 17 | 1 j 12 h | 16 h | 6 h | 14 h | 6 h | 12 h | 12 h | 16 h | – |
| 17 à 18 | 2 j 12 h | 18 h | 8 h | 18 h | 8 h | 16 h | 18 h | 18 h | – |
| 18 à 19 | 4 j | 20 h | 10 h | 1 j | 10 h | 20 h | 1 j | 20 h | – |
| 19 à 20 | 6 j | 1 j | 12 h | 1 j 12 h | 12 h | 1 j | 1 j 12 h | 1 j | – |
| **Total** | 16 j 13 h | 5 j 13 h | 2 j 14 h | 6 j 13 h | 2 j 14 h | 4 j 16 h | 5 j 10 h | 5 j 13 h | 3 h 12 min |
<!-- upgrade-times:end -->

<!-- upgrade-times-expedition:start -->
<!-- Generated from server/Resources/SkylabConfig.json by the test skylab::duration_tests::the_wiki_page_is_the_config (run it with SKYLAB_WIKI_WRITE=1 to rewrite this part). -->

**Durées d’amélioration** des quatre modules de l’Expédition (l’amélioration à partir du niveau de la première colonne ; un tiret est au-delà du niveau maximal du module) :

| Niveau | Module Moteurs | Module Défense | Module Radar | Baie des trophées |
| :--- | ---: | ---: | ---: | ---: |
| 1 à 2 | 2 h | 3 h | 4 h | 15 min |
| 2 à 3 | 6 h | 9 h | 1 j | 19 min |
| 3 à 4 | 1 j | 1 j 12 h | – | 26 min |
| 4 à 5 | 2 j | 3 j | – | 34 min |
| 5 à 6 | – | – | – | 45 min |
| 6 à 7 | – | – | – | 1 h |
| 7 à 8 | – | – | – | 1 h 19 min |
| 8 à 9 | – | – | – | 1 h 44 min |
| 9 à 10 | – | – | – | 2 h 18 min |
| 10 à 11 | – | – | – | 3 h 2 min |
| 11 à 12 | – | – | – | 4 h |
| 12 à 13 | – | – | – | 5 h 17 min |
| 13 à 14 | – | – | – | 6 h 59 min |
| 14 à 15 | – | – | – | 9 h 14 min |
| 15 à 16 | – | – | – | 12 h 11 min |
| 16 à 17 | – | – | – | 16 h 5 min |
| 17 à 18 | – | – | – | 21 h 14 min |
| 18 à 19 | – | – | – | 1 j 4 h |
| 19 à 20 | – | – | – | 1 j 13 h |
| **Total** | 3 j 8 h | 5 j | 1 j 4 h | 6 j 8 h |
<!-- upgrade-times-expedition:end -->

Une amélioration déjà en cours quand les durées changent garde l’heure de fin qu’on lui a donnée. Le Noyau seul demande environ **16,5 jours** d’amélioration d’affilée pour aller du niveau 1 au niveau 20. Aucun module ne dépasse le niveau du Noyau, donc la dernière étape de tout autre module (12 à 37 heures) ne peut commencer qu’une fois le Noyau au niveau 20 : avec tous les minuteurs occupés et les crédits et le Thulium prêts, toute la station demande environ **18 jours**.

### Gestion de l’énergie {#power-management}

Votre Skylab dispose d’un budget d’énergie limité.

- **Bilan** : gardez la production de Solaire au-dessus de l’énergie consommée par tous les autres modules. La page Skylab affiche le bilan, et vous prévient avant qu’une construction le fasse passer sous zéro.
- **Solaire suit le rythme** : un module Solaire de niveau N produit l’énergie de **tous les autres modules au niveau N** (le Noyau, les deux fermes, l’Entrepôt de ressources, les deux collecteurs et la Fonderie, et à partir du niveau 10 le Centre de recherche et la Baie à minerai) et environ un dixième de plus, donc une station dont tous les modules sont au niveau 7 a besoin de Solaire 7 et l’a couverte. Solaire un niveau plus bas ne suffit pas pour une station complète (la dernière colonne), donc Solaire doit continuer à suivre le reste. Le Noyau consomme peu, il peut donc avoir de l’avance : Solaire 5 et plus couvre une station complète à son niveau avec le Noyau à n’importe quel niveau. Le tableau ci-dessous compte aussi l’Imprimante à munitions à partir du niveau 7, l’Usine à roquettes et la Baie à minerai à partir du niveau 10, et les modules Moteurs, Défense et Radar et la Baie des trophées à partir du niveau 11 (ils se construisent à partir du niveau 15 du Noyau et comptent quatre niveaux plus tôt, parce que le Noyau peut devancer Solaire), chacun au plus à son propre niveau maximal.
- **État actif** : vous pouvez allumer et éteindre les fermes, les collecteurs et la Fonderie pour gérer l’énergie. Le Noyau, Solaire, l’Entrepôt de ressources et le Centre de recherche fonctionnent toujours. L’Imprimante à munitions, l’Usine à roquettes et la Baie à minerai peuvent aussi être allumées et éteintes, tout comme les quatre modules de l’Expédition (pas pendant qu’un voyage est en cours).
- **Panne** : si la consommation d’énergie dépasse la production, toutes les fermes et tous les collecteurs cessent de produire jusqu’au retour de l’équilibre. Ce qu’ils contiennent déjà reste, et vous pouvez toujours le récupérer. La Fonderie ne lance aucun nouveau lot et le Centre de recherche aucune nouvelle recherche (une recherche déjà en cours continue). L’Imprimante à munitions, l’Usine à roquettes et la Baie à minerai s’arrêtent comme les fermes et les collecteurs. Le Module Défense ne combat rien, les scans du radar sont à l’arrêt et aucun voyage ne peut partir (un voyage en cours continue).
- **Amélioration de Solaire** : pendant son amélioration, Solaire ne produit qu’un quart de son énergie ; si vos autres modules ne sont pas très en dessous, la station est donc en déficit, et les fermes et les collecteurs s’arrêtent jusqu’à la fin de l’amélioration (voir [Module Solaire](#solar-module)).

L’énergie de Solaire à chaque niveau, face à ce que les autres modules consomment au même niveau (chaque module à ce niveau, le Noyau compris, et le Centre de recherche et la Baie à minerai à partir du niveau 10, et les quatre modules de l’Expédition à partir du niveau 11) :

<!-- skylab-power:start -->
<!-- Generated from server/Resources/SkylabConfig.json by docs/design/skylab-power-model.py --doc (--check fails while this part is behind). -->

| Niveau | Solaire produit | Les autres modules consomment | Excédent | Avec Solaire un niveau en dessous |
| :--- | ---: | ---: | ---: | :--- |
| 1 | 255 | 230 | 25 | – |
| 2 | 310 | 278 | 32 | 255 : il manque 23 |
| 3 | 375 | 337 | 38 | 310 : il manque 27 |
| 4 | 455 | 410 | 45 | 375 : il manque 35 |
| 5 | 555 | 501 | 54 | 455 : il manque 46 |
| 6 | 680 | 615 | 65 | 555 : il manque 60 |
| 7 | 965 | 875 | 90 | 680 : il manque 195 |
| 8 | 1 185 | 1 076 | 109 | 965 : il manque 111 |
| 9 | 1 460 | 1 327 | 133 | 1 185 : il manque 142 |
| 10 | 2 035 | 1 849 | 186 | 1 460 : il manque 389 |
| 11 | 2 995 | 2 721 | 274 | 2 035 : il manque 686 |
| 12 | 3 565 | 3 241 | 324 | 2 995 : il manque 246 |
| 13 | 4 285 | 3 893 | 392 | 3 565 : il manque 328 |
| 14 | 5 185 | 4 713 | 472 | 4 285 : il manque 428 |
| 15 | 6 325 | 5 748 | 577 | 5 185 : il manque 563 |
| 16 | 7 765 | 7 055 | 710 | 6 325 : il manque 730 |
| 17 | 9 585 | 8 711 | 874 | 7 765 : il manque 946 |
| 18 | 11 895 | 10 812 | 1 083 | 9 585 : il manque 1 227 |
| 19 | 14 835 | 13 483 | 1 352 | 11 895 : il manque 1 588 |
| 20 | 18 575 | 16 885 | 1 690 | 14 835 : il manque 2 050 |
<!-- skylab-power:end -->

Le tableau compte chaque module au même niveau. La Ferme à Thulium en consomme en haut plus des deux tiers (11 695 au niveau 20, contre 16 885 pour les quinze), donc une station dont cette ferme est bien en avance sur le reste a besoin de plus de Solaire que son Noyau ne le laisse penser.

### Récupération {#collecting}

Chaque ferme et chaque collecteur a un réservoir pour environ 72 heures de sa production. La récupération se fait à la main.

- **Capacité** : une fois son réservoir plein, un module cesse de produire jusqu’à ce que vous récupériez.
- **Fermes** : les crédits et le Thulium récupérés vont directement sur votre compte.
- **Collecteurs** : le minerai va dans l’Entrepôt de ressources, dans la limite de la place disponible.
- **Fonderie** : les plaques vont dans votre inventaire, quand votre vaisseau est amarré.
- **Imprimante à munitions et Usine à roquettes** : les munitions et les roquettes vont dans votre inventaire, quand votre vaisseau est amarré. Chacune ne garde que 24 heures de production (voir [Imprimante à munitions](#ammo-printer) et [Usine à roquettes](#rocket-factory)).
- **Baie à minerai** : rien à récupérer. Elle verse le minerai de votre inventaire dans l’Entrepôt de ressources quand vous appuyez sur **Transférer**, vaisseau amarré, jusqu’à son quota (voir [Baie à minerai](#ore-bay)).
- **Baie des trophées** : récupérée dans la fenêtre Univers, vaisseau amarré : les crédits et le Thulium vont sur votre compte, l’expérience et l’honneur à votre pilote et le butin dans votre inventaire. Elle garde ce qu’elle contient jusqu’à ce que vous la récupériez, mais une baie pleine fait cesser le feu au Skylab (voir [Baie des trophées](#trophies-bay)).
- **Tout récupérer** prend tout d’un coup, y compris les modules éteints ou en amélioration, mais pas la Baie des trophées, que vous récupérez dans la fenêtre Univers.
- Un badge **(!)** signale un réservoir plein que vous pouvez vider, et des plaques qui attendent dans la Fonderie, sur la page Skylab et sur la ligne Skylab de la barre latérale.

### La réinitialisation {#the-wipe}

Le Skylab n’est jamais réinitialisé : les modules gardent leurs niveaux, l’Entrepôt de ressources garde son minerai et le Centre de recherche garde ses technologies, son réservoir de science, la Dark Matter qu’il contient et une recherche en cours. Les plaques de votre inventaire sont des objets comme les autres, elles suivent donc les [règles de la réinitialisation](/wiki/03-Mechanics/Wipe-Timeline.md). L’Imprimante à munitions et l’Usine à roquettes gardent leurs niveaux, ce qu’elles sont réglées pour fabriquer et ce qu’elles contiennent, et la Baie à minerai garde son niveau et son quota. Les quatre modules de l’Expédition gardent aussi leurs niveaux, avec leurs technologies, et le chargeur et le réglage de l’alimentation de même. Le minerai de votre inventaire est réinitialisé comme n’importe quel objet : versez-le d’abord dans l’Entrepôt de ressources.

Une **expédition** est soldée jusqu’à la réinitialisation : un voyage en cours est terminé, la Baie des trophées verse ses crédits, son Thulium, son expérience et son honneur et est vidée (son butin est supprimé comme tout objet libre), et le Skylab commence la nouvelle saison à la maison, dans le port de votre corporation, avec une nouvelle carte de l’univers, les 19 cellules de départ connues et la file du radar vide. Les moteurs et les lasers montés dans les modules Moteurs et Défense sont des objets libres comme les autres : retirez-les et mettez-les dans la cache de transport pour les garder.

## Planifier votre Skylab {#planning-your-skylab}

Le Skylab met des semaines à grandir : un peu de planification paie donc. Les chiffres sont ceux des tableaux ci-dessus.

### Que monter en premier {#what-to-upgrade-first}

1. **Solaire, puis la Ferme à crédits.** Solaire coûte 500 crédits et 50 Thulium et rien ne tourne sans lui ; la Ferme à crédits ne coûte rien. Les dix [missions Station](/wiki/03-Mechanics/Quests.md#station-missions) vous guident dans ces premières étapes et vous versent 52 000 crédits et 610 Thulium pour elles, en base : votre monde, vos boosters et les bonus de votre clan la multiplient.
2. **Ensuite la Ferme à Thulium : c’est votre principale source de Thulium.** Au niveau 10, elle produit 360 Thulium par heure, 8 640 par jour, environ autant que rapportent 43 victimes d’un [Crystalys](/wiki/04-Aliens/Crystalys.md) en Alpha (200 chacune). La montée jusqu’au niveau 10 coûte 1 154 000 crédits et 4 190 Thulium, construction comprise. Au niveau 15, la ferme produit 18 240 par jour, et 30 720 au niveau 20. Son réservoir contient 72 heures : revenez donc au moins tous les trois jours. Ce que le Thulium permet d’acheter est sur la page [Ressources](/wiki/06-Items/Resources.md#thulium).
3. **La Ferme à crédits est le revenu régulier d’appoint.** Au niveau 10, elle produit 33 750 crédits par heure, 810 000 par jour, pour 840 000 crédits et 109 Thulium. Les niveaux élevés se rentabilisent en quelques jours : l’étape du niveau 9 au niveau 10 coûte 300 000 crédits pour 4 500 de plus par heure, soit 67 heures. Montez-la quand il vous reste des crédits.
4. **Gardez le Noyau occupé.** Rien ne dépasse le Noyau, et le Noyau seul demande environ 16 jours et demi pour atteindre le niveau 20. Il n’y a pas de file d’attente : lancez donc son étape suivante chaque fois que vous revenez.
5. **Construisez la chaîne d’approvisionnement d’un bloc.** Les collecteurs, l’Entrepôt de ressources et la Fonderie s’ouvrent au niveau 5 du Noyau. Un collecteur ne peut mettre du minerai en banque que dans un Entrepôt de ressources, et la banque contient un jour de production de son collecteur au niveau 1 et quatre jours au niveau 20 : montez donc l’Entrepôt avec les collecteurs, sinon le minerai attend dans leurs réservoirs.
6. **Gardez 2 000 Thulium prêts pour le niveau 10 du Noyau.** L’étape du Noyau du niveau 9 au niveau 10 les demande, et elle construit le pont et le Noyau 2, où se construisent l’[Imprimante à munitions](#ammo-printer), l’[Usine à roquettes](#rocket-factory) et la [Baie à minerai](#ore-bay).
7. **Ayez 4 000 Thulium prêts pour le niveau 15 du Noyau.** L’étape du Noyau du niveau 14 au niveau 15 les demande, et elle construit le second pont et le Noyau 3, où se construisent les quatre modules de l’Expédition. Les modules eux-mêmes demandent bien plus, 232 590 Thulium et 49 Dark Matter Plates en tout (voir [Ce que ça coûte](#what-it-costs)) : commencez par le Module Moteurs et le Module Défense au niveau 1.
8. **Construisez l’Expédition dans cet ordre.** Un moteur dans le Module Moteurs, un laser dans le Module Défense avec une Imprimante à munitions pour l’alimenter, et la Baie des trophées pour garder ce que rapportent les éliminations : un voyage ne rapporte rien tant que les trois ne sont pas là. Le Module Radar peut attendre : avec Défense 1, votre Skylab atteint au moins les six cellules voisines de son port, et les 19 cellules que vous connaissez au départ comptent des cellules jusqu’à la difficulté 3.

### Planifier une amélioration de Solaire {#timing-a-solar-upgrade}

Pendant qu’une amélioration de Solaire est en cours, il produit un quart de son énergie, et une station consomme presque toujours plus que cela. Les fermes et les collecteurs s’arrêtent alors pendant toute l’amélioration : ce qu’ils contiennent reste, mais ce qu’ils auraient produit est perdu. Le tableau donne, pour chaque étape de Solaire, sa durée, la plus grande station qui la traverse encore (tous les modules au même niveau, le Noyau et la chaîne d’approvisionnement compris ; une station plus petite supporte un peu plus) et ce qu’une Ferme à crédits et une Ferme à Thulium de ce niveau auraient produit pendant ce temps. Par exemple, Solaire du niveau 10 au niveau 11 prend 4 heures, et des fermes de niveau 10 y auraient produit 135 000 crédits et 1 440 Thulium. Le tableau compte aussi l’Imprimante à munitions à partir du niveau 7, l’Usine à roquettes et la Baie à minerai à partir du niveau 10 et les quatre modules de l’Expédition à partir du niveau 15.

| Amélioration de Solaire | Durée | Station qui continue de tourner, jusqu’au niveau | La Ferme à crédits produit pendant ce temps | La Ferme à Thulium produit pendant ce temps |
| :--- | ---: | ---: | ---: | ---: |
| 1 à 2 | 5 min | aucune | 188 | 3 |
| 2 à 3 | 15 min | aucune | 1 125 | 16 |
| 3 à 4 | 30 min | aucune | 3 375 | 44 |
| 4 à 5 | 45 min | aucune | 6 750 | 84 |
| 5 à 6 | 1 h | aucune | 11 250 | 144 |
| 6 à 7 | 1 h 15 min | aucune | 19 688 | 230 |
| 7 à 8 | 1 h 30 min | 1 | 30 375 | 336 |
| 8 à 9 | 2 h | 2 | 49 500 | 528 |
| 9 à 10 | 3 h | 3 | 87 750 | 912 |
| 10 à 11 | 4 h | 5 | 135 000 | 1 440 |
| 11 à 12 | 5 h | 6 | 202 500 | 2 200 |
| 12 à 13 | 6 h | 7 | 297 000 | 3 120 |
| 13 à 14 | 8 h | 7 | 468 000 | 4 800 |
| 14 à 15 | 10 h | 8 | 675 000 | 6 800 |
| 15 à 16 | 12 h | 9 | 918 000 | 9 120 |
| 16 à 17 | 16 h | 10 | 1 440 000 | 14 080 |
| 17 à 18 | 18 h | 11 | 1 944 000 | 18 000 |
| 18 à 19 | 20 h | 12 | 2 610 000 | 22 400 |
| 19 à 20 | 1 j | 13 | 3 780 000 | 28 800 |

- **Montez les fermes en même temps que Solaire.** Un module en amélioration ne produit rien et ne consomme pas d’énergie de toute façon : le temps qu’une ferme passe en amélioration pendant la pause ne coûte donc rien de plus.
- **Gardez les autres modules bas si vous ne pouvez pas vous offrir une pause.** Une station ne tourne pendant une amélioration de Solaire que si tous ses autres modules sont au moins cinq niveaux en dessous de Solaire (six à partir du niveau 10 de Solaire), et une station complète demande un peu plus, comme le montre le tableau.
- **Éteignez ce dont vous pouvez vous passer.** Un module éteint ne consomme pas d’énergie : éteindre la Ferme à Thulium, la plus gourmande (80 au niveau 1, et 30 % de plus à chaque niveau), fait donc de la place pour les autres.
