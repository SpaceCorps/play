<!-- wiki-i18n source: 011fc9c31c4045f1 -->
<!-- wiki-i18n title: Skylab -->
# Skylab

Le Skylab est votre installation orbitale personnelle. Il construit et améliore des modules qui produisent des crédits et du Thulium, extraient du minerai, forgent les plaques dont l’Assemblage fait les meilleurs lasers et, à partir du niveau 10 du Noyau, recherchent les technologies dont l’Assemblage a besoin. Il travaille pour vous même quand vous êtes hors ligne.

> [!NOTE]
> **Ce qui a changé dans la 0.4.10.** Chaque module du Skylab a désormais sa propre table de production, de prix et de durées, niveau par niveau. Vous avez gardé vos niveaux : rien n’a été facturé et rien n’a été remboursé pour la différence. Ce que vos fermes et vos collecteurs avaient dans leurs réservoirs à l’arrivée de la mise à jour a été versé **une seule fois, au taux de l’ancienne version** : les crédits et le Thulium sont allés sur votre compte, le minerai dans votre Entrepôt de ressources, et les réservoirs sont repartis de zéro.
>
> Deux règles sont nouvelles. **Solaire ne produit que 25 % de son énergie pendant son amélioration**, si bien que, pour la plupart des stations, toutes les fermes et tous les collecteurs s’arrêtent jusqu’à la fin de l’amélioration (voir [Module Solaire](#solar-module) et [Planifier une amélioration de Solaire](#timing-a-solar-upgrade)). **L’Entrepôt de ressources a sa propre limite pour chaque minerai** : un jour de production du collecteur au niveau 1, quatre jours au niveau 20.

![The Skylab station fully grown](../../img/wiki-img/shots/skylab-station.jpg)
![The Resource Storage card of the Skylab](../../img/wiki-img/shots/skylab-storage.jpg)
![The Skylab table of modules: level, production, storage and power of every module, with the 0.4.10 numbers](../../img/wiki-img/shots/skylab-table.jpg)

## En une minute {#in-one-minute}

- Construisez **Solaire** d’abord : sans son énergie, rien ne tourne dans le Skylab. La Ferme à crédits ne coûte rien à construire, et la Ferme à Thulium coûte 5 000 crédits et 500 Thulium.
- Les fermes et les collecteurs remplissent un **réservoir** (72 heures de production) pendant votre absence. **Récupérer** le verse sur votre compte (crédits, Thulium) ou dans votre Entrepôt de ressources (minerai).
- La **Ferme à Thulium** est votre principale source de Thulium : 50 par heure au niveau 1, 1 600 au niveau 20. La Ferme à crédits produit 500 crédits par heure au niveau 1 et 50 000 au niveau 20.
- Le **Noyau** donne le rythme : aucun module ne le dépasse, et sa propre montée prend environ 16 jours et demi.
- **Solaire ne produit que 25 % de son énergie pendant son amélioration**, vos fermes et vos collecteurs s’arrêtent donc jusqu’à sa fin. [Planifiez-la](#timing-a-solar-upgrade).

## Vue d’ensemble {#overview}

Le Skylab tourne sur sa propre horloge, indépendamment de votre vaisseau : les modules produisent et forgent pendant votre absence. Votre rôle : construire, améliorer, garder l’énergie à l’équilibre et récupérer. La page offre quatre vues de la même station : **Station** (la station en 3D, avec une pastille au-dessus de chaque module ; cliquez sur l’une d’elles pour ouvrir sa fiche, ou appuyez sur **1** à **9**), **Liste** (une carte par module), **Tableau** (les chiffres de tous les modules dans un seul tableau) et **Recherche** (l’écran propre au Centre de recherche, voir [Recherche](/wiki/03-Mechanics/Research.md)). Survoler **Construire** ou **Améliorer** montre ce que change le niveau suivant, ce qu’il coûte et combien de temps il prend.

Neuf modules composent la station :

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

**Des missions dédiées.** Dix [missions Station](/wiki/03-Mechanics/Quests.md#station-missions) dans Mission Control vous guident à travers le Skylab : construire Solaire, une Ferme à crédits et une Ferme à Thulium, monter le Noyau et Solaire, récupérer vos 50 000 premiers crédits et ouvrir la chaîne d’approvisionnement, et elles rapportent un peu à chaque étape. La première est ouverte dès le niveau 1.

## La station à chaque niveau {#the-station-at-every-level}

Voici la vue Station du Skylab à chaque niveau de 1 à 20, toutes sous le même angle, avec tous les modules au même niveau. La vue fait tenir toute la station dans l’image : l’échelle n’est donc pas la même partout, elle fait un saut quand la forme grandit. La station grandit par étapes : sa forme change aux **niveaux 1, 5, 10, 15 et 20**, et entre-temps chaque niveau allume **une lampe de plus** sur le collier de chaque module (le nombre de lampes allumées est le niveau, et l’anneau de vingt lampes du Noyau se remplit de la même façon).

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

**Niveaux 15 à 19.** Les fermes se garnissent de caisses et de cristaux, la baie d’amarrage éclaire son approche et l’ensemble Solaire se dote d’un sommet.

![Niveau 15](../../img/skylab/wiki/level-15.jpg)
![Niveau 16](../../img/skylab/wiki/level-16.jpg)
![Niveau 17](../../img/skylab/wiki/level-17.jpg)
![Niveau 18](../../img/skylab/wiki/level-18.jpg)
![Niveau 19](../../img/skylab/wiki/level-19.jpg)

**Niveau 20.** Le sommet de l’échelle : la couronne sur le Noyau et les tours achevées des fermes et de la chaîne d’approvisionnement.

![Niveau 20](../../img/skylab/wiki/level-20.jpg)

**Les cartes des neuf modules.** La vue Liste de la même station au niveau 20 : les quatre modules de la première version, le Collecteur de Velkonite, le Collecteur d’Orvium, l’Entrepôt de ressources et la Fonderie, arrivés avec la chaîne d’approvisionnement, et le Centre de recherche. Chaque carte montre le niveau du module, sa production, son énergie et son interrupteur. Toutes les cartes affichent le niveau 20, sauf celle du Centre de recherche : il a les niveaux 1 à 10, sa carte affiche donc le niveau 10, son maximum.

![La vue Liste au niveau 20 : les cartes du Noyau, de Solaire, de la Ferme à crédits, de la Ferme à Thulium, du Collecteur de Velkonite, du Collecteur d’Orvium, de l’Entrepôt de ressources, de la Fonderie et du Centre de recherche](../../img/skylab/wiki/modules.jpg)

## Les quatre premiers modules {#the-first-four-modules}

### Module Noyau {#core-module}

Le cœur de votre Skylab. Le niveau du Noyau détermine le niveau maximal de tous les autres modules : vous ne pouvez améliorer aucun module au-delà de votre Noyau. Le Noyau monte jusqu’au niveau 20, et à partir du **niveau 5** il ouvre la chaîne d’approvisionnement décrite plus bas. Ses améliorations ne coûtent que des crédits : 112 326 en tout jusqu’au niveau 10 et 6 647 504 jusqu’au niveau 20, et elles prennent environ 16 jours et demi en tout (voir [Durées d’amélioration](#upgrade-times)).

### Module Solaire {#solar-module}

L’énergie est le sang du Skylab. Le module Solaire produit l’énergie qu’utilisent tous les autres modules.

- **Importance** : si votre consommation d’énergie dépasse votre production, vos fermes et vos collecteurs s’arrêtent.
- **Énergie produite** : un module Solaire au niveau N produit de quoi alimenter **chaque autre module au niveau N**, avec environ un dixième de plus : 255 au niveau 1, 835 au niveau 7, 16 110 au niveau 20. Solaire de niveau 7 alimente une station entière au niveau 7 (voir Gestion de l’énergie pour chaque niveau).
- **Prix** : construire Solaire coûte **500 crédits et 50 Thulium**. Ses améliorations coûtent la même chose et durent aussi longtemps que celles de la Fonderie : de 8 000 crédits et 25 Thulium pour le niveau 2 (5 minutes) à 9 000 000 de crédits et 10 000 Thulium pour le niveau 20 (24 heures).
- **Amélioration** : pendant son amélioration, Solaire ne produit que **25 %** de l’énergie de son niveau actuel, puis celle du nouveau niveau dès que l’amélioration se termine. Une station qui consomme davantage s’arrête : toutes les fermes et tous les collecteurs cessent de produire, et la Fonderie ne lance aucun nouveau lot jusqu’à la fin de l’amélioration. C’est le cas de presque toutes les stations : elle ne tourne pendant l’amélioration que si tous les autres modules sont au moins cinq niveaux en dessous de Solaire (six niveaux à partir du niveau 10 de Solaire). Planifiez une amélioration de Solaire comme une panne de vos fermes (voir Construction et amélioration).

### Ferme à crédits et Ferme à Thulium {#credit-farm-and-thulium-farm}

- **Ferme à crédits** : produit des crédits au fil du temps : **500 par heure au niveau 1, 50 000 au niveau 20** (niveau 5 : 2 500 ; niveau 10 : 7 500 ; niveau 15 : 17 000). Elle ne coûte rien à construire.
- **Ferme à Thulium** : produit du Thulium au fil du temps : **50 par heure au niveau 1, 1 600 au niveau 20** (niveau 5 : 180 ; niveau 10 : 450 ; niveau 15 : 950). La construire coûte 5 000 crédits et 500 Thulium.
- Les deux ont besoin d’énergie, et chacune conserve 72 heures de sa production jusqu’à ce que vous la récupériez.

## La chaîne d’approvisionnement {#the-supply-chain}

Quatre modules transforment le temps passé loin du clavier en plaques pour vos meilleurs lasers. Le minerai vient **uniquement** des collecteurs (tous les matériaux et toutes les monnaies sont sur la page [Ressources](/wiki/06-Items/Resources.md)) : les aliens n’en lâchent pas et la boutique n’en vend pas.

1. Un **collecteur** extrait du minerai, une quantité donnée par heure, dans son propre réservoir (de quoi stocker 72 heures).
2. **Récupérer** déplace le minerai du réservoir vers l’**Entrepôt de ressources**, la banque, où chaque minerai est gardé à part.
3. La **Fonderie** prend dans la banque le minerai dont elle a besoin au début d’un lot, et fabrique des plaques, 10 secondes par plaque, un lot à la fois.
4. **Récupérer les plaques** déplace les plaques terminées dans votre inventaire (votre vaisseau doit être amarré). L’[Assemblage](/wiki/06-Items/Lasers.md) les transforme en Quantum Laser 3, en Starfire-3 ou en Helios Beam, et, une de chaque avec 5 Dark Matter, en Dark Matter Plate, que demandent [la Forge](/wiki/06-Items/Forge.md) et le dernier palier de chaque chaîne d’amélioration.

### Collecteur de Velkonite et Collecteur d’Orvium {#velkonite-collector-and-orvium-collector}

- **Minerai** : le Collecteur de Velkonite extrait **10 Velkonite par heure** au niveau 1 et le Collecteur d’Orvium **10 Orvium par heure**, et chaque niveau a sa propre cadence : jusqu’à 80 Velkonite et 40 Orvium par heure au niveau 20 (niveau 5 : 18 et 14 par heure ; niveau 10 : 32 et 24).
- **Réservoir** : chacun contient 72 heures de son minerai et cesse d’extraire quand il est plein.
- **Récupérer** : déplace le minerai dans l’Entrepôt de ressources, dans la limite de la place disponible. Sans entrepôt construit, ou si la banque de ce minerai est pleine, il n’y a nulle part où le mettre et le bouton en indique la raison. Le reste demeure dans le réservoir.
- **Énergie** : 20 (Velkonite) et 30 (Orvium) au niveau 1, soit 15 % de plus par niveau.

### Entrepôt de ressources {#resource-storage}

- **Banque** : garde la Velkonite et l’Orvium séparés, et en contient une quantité différente de chacun : **240 de chaque au niveau 1**, jusqu’à 7 680 de Velkonite et 3 840 d’Orvium au niveau 20 (niveau 5 : 720 et 560 ; niveau 10 : 1 920 et 1 440).
- **Limite** : un jour de production de son collecteur au niveau 1, jusqu’à quatre jours au niveau 20. Le réservoir d’un collecteur contient trois jours : à partir du niveau 13, la banque contient donc au moins un réservoir plein.
- **Au-dessus de la limite** : si une banque contient plus que sa limite (le versement de la mise à jour 0.4.10 a pu la laisser ainsi), rien n’est retiré, mais Récupérer n’ajoute plus de ce minerai tant que vous n’en avez pas utilisé un peu.
- Le minerai n’y entre qu’en le récupérant d’un collecteur, et n’en sort que vers la Fonderie. Il n’entre jamais dans votre inventaire.
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

Le neuvième module transforme des ressources en science et recherche les technologies dont l’Assemblage a besoin avant de fabriquer quoi que ce soit de nouveau. Il se construit à partir du niveau 10 du Noyau, a les niveaux 1 à 10, consomme de l’énergie et ne peut pas être éteint. Ses chiffres, ce qu’il brûle comme carburant, le boost et tout l’arbre des technologies sont sur la page [Recherche](/wiki/03-Mechanics/Research.md). Les technologies les plus hautes demandent aussi de la Dark Matter, que vous ajoutez au Centre : [Dark Matter et Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md) explique comment l’obtenir.

## Mécaniques {#mechanics}

### Construction et amélioration {#building-and-upgrading}

- **Construction** : chaque module se construit séparément. Un module est au niveau 1 dès sa construction, et l’améliorer augmente sa production (ou l’énergie qu’il produit) et son stockage, mais aussi ce qu’il consomme en énergie.
- **Durée et coût** : les améliorations coûtent des crédits et du Thulium et prennent du temps, et chaque module a pour chaque niveau son propre prix et sa propre durée (survolez **Améliorer** pour voir le suivant ; les totaux sont plus bas). Le prix est payé au lancement de l’amélioration. Le coût ne dépend pas de la durée.
- **Minuteurs** : une amélioration tourne sur l’horloge du serveur, elle se termine donc pendant votre absence, des jours plus tard s’il le faut. Lancez-la, déconnectez-vous, revenez : le module est à son nouveau niveau quand vous ouvrez la page Skylab.
- **Durées d’amélioration** : les premiers niveaux sont rapides et les derniers prennent jusqu’à 36 heures, ceux du Noyau jusqu’à 6 jours (voir les tableaux ci-dessous). Chaque module a son propre minuteur : vous pouvez donc en améliorer plusieurs à la fois.
- **Pause de production** : pendant son amélioration, un module est hors ligne : il ne produit rien et ne consomme pas d’énergie. Solaire fait exception : il continue de produire un quart de son énergie (voir plus bas).
- **Solaire ne produit que 25 % de son énergie pendant son amélioration** : Solaire produit toute l’énergie du Skylab et, pendant son amélioration (24 heures pour le dernier niveau), il produit un quart de l’énergie de son niveau **actuel** ; celle du nouveau niveau prend le relais dès que l’amélioration se termine. Une station complète consomme environ 90 % de ce que Solaire produit à son propre niveau : un quart de cela ne porte donc qu’une station située cinq à six niveaux en dessous de Solaire. Sinon, toutes les fermes et tous les collecteurs s’arrêtent pendant toute l’amélioration, ce que vous avez en réserve reste et peut être récupéré, et la Fonderie ne lance aucun nouveau lot. Un module en cours d’amélioration ou éteint ne consomme pas d’énergie : monter les fermes en même temps que Solaire ne coûte donc rien de plus, et éteindre des modules fait de la place pour les autres ; la Ferme à Thulium consomme de loin le plus d’énergie.

### Ce que ça coûte {#what-it-costs}

Le prix de toute la montée, la construction plus chaque amélioration, jusqu’au niveau 10 et jusqu’au niveau 20. Le Noyau est toujours là et ses étapes ne coûtent que des crédits ; le Centre de recherche a les niveaux 1 à 10, et ses chiffres sont sur la page [Recherche](/wiki/03-Mechanics/Research.md).

| Module | Crédits jusqu’au niveau 10 | Thulium jusqu’au niveau 10 | Crédits jusqu’au niveau 20 | Thulium jusqu’au niveau 20 |
| :--- | ---: | ---: | ---: | ---: |
| Noyau | 112 326 | 0 | 6 647 504 | 0 |
| Solaire | 1 219 500 | 1 600 | 35 039 500 | 36 850 |
| Ferme à crédits | 840 000 | 109 | 26 240 000 | 2 399 |
| Ferme à Thulium | 1 154 000 | 4 190 | 32 254 000 | 67 890 |
| Collecteur de Velkonite | 696 000 | 6 950 | 20 996 000 | 78 950 |
| Collecteur d’Orvium | 696 000 | 6 950 | 20 996 000 | 78 950 |
| Entrepôt de ressources | 619 500 | 359 | 18 169 500 | 2 649 |
| Fonderie | 1 224 000 | 2 050 | 35 044 000 | 37 300 |

Les premières étapes sont bon marché et les dernières chères : l’étape de la Ferme à crédits du niveau 1 au niveau 2 coûte 5 000 crédits et 1 Thulium, celle du niveau 19 au niveau 20 coûte 7 000 000 de crédits et 550 Thulium. Celles de la Ferme à Thulium coûtent 7 000 crédits et 45 Thulium, puis 8 500 000 crédits et 16 000 Thulium. Les améliorations de Solaire coûtent à chaque niveau la même chose que celles de la Fonderie, et les deux collecteurs coûtent autant l’un que l’autre.

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

Une amélioration déjà en cours quand les durées changent garde l’heure de fin qui lui a été donnée. Le Noyau seul demande environ **16 jours et demi** d’améliorations à la suite pour passer du niveau 1 au niveau 20. Aucun module ne dépasse le niveau du Noyau : la dernière étape de chaque autre module (de 12 à 36 heures) ne peut donc commencer qu’une fois le Noyau au niveau 20. En gardant chaque minuteur occupé, et avec les crédits et le Thulium nécessaires, la station entière demande environ **18 jours**.

### Gestion de l’énergie {#power-management}

Votre Skylab dispose d’un budget d’énergie limité.

- **Bilan** : gardez la production de Solaire au-dessus de l’énergie consommée par tous les autres modules. La page Skylab affiche le bilan, et vous prévient avant qu’une construction le fasse passer sous zéro.
- **Solaire suit le rythme** : un module Solaire au niveau N produit l’énergie de **tous les autres modules au niveau N** (le Noyau, les deux fermes, l’Entrepôt de ressources, les deux collecteurs et la Fonderie, et dès le niveau 10 le Centre de recherche), avec environ un dixième de plus, si bien qu’une station dont tous les modules sont au niveau 7 a besoin de Solaire au niveau 7, qui la couvre. Solaire un niveau en dessous ne suffit pas pour une station complète (la dernière colonne) : Solaire doit donc toujours suivre les autres vers le haut. Le Noyau consomme peu, il peut donc prendre de l’avance : Solaire au niveau 5 et au-delà couvre une station complète à son niveau, quel que soit le niveau du Noyau.
- **État actif** : vous pouvez allumer ou éteindre les fermes, les collecteurs et la Fonderie pour gérer l’énergie. Le Noyau, Solaire, l’Entrepôt de ressources et le Centre de recherche fonctionnent toujours.
- **Panne** : si la consommation d’énergie dépasse la production, toutes les fermes et tous les collecteurs cessent de produire jusqu’au retour à l’équilibre. Ce qu’ils contiennent déjà reste, et vous pouvez toujours le récupérer. La Fonderie ne lance aucun nouveau lot, et le Centre de recherche ne lance aucune nouvelle recherche (une recherche en cours continue).
- **Amélioration de Solaire** : pendant son amélioration, Solaire ne produit qu’un quart de son énergie ; si vos autres modules ne sont pas très en dessous, la station est donc en déficit, et les fermes et les collecteurs s’arrêtent jusqu’à la fin de l’amélioration (voir [Module Solaire](#solar-module)).

L’énergie de Solaire à chaque niveau, face à ce que consomment les autres modules au même niveau (chaque module à ce niveau, le Noyau compris, et le Centre de recherche dès le niveau 10) :

<!-- skylab-power:start -->
<!-- Generated from server/Resources/SkylabConfig.json by docs/design/skylab-power-model.py --doc (--check fails while this part is behind). -->

| Niveau | Solaire produit | Les sept autres modules consomment | Excédent | Avec Solaire un niveau en dessous |
| :--- | ---: | ---: | ---: | :--- |
| 1 | 255 | 230 | 25 | – |
| 2 | 310 | 278 | 32 | 255 : il manque 23 |
| 3 | 375 | 337 | 38 | 310 : il manque 27 |
| 4 | 455 | 410 | 45 | 375 : il manque 35 |
| 5 | 555 | 501 | 54 | 455 : il manque 46 |
| 6 | 680 | 615 | 65 | 555 : il manque 60 |
| 7 | 835 | 756 | 79 | 680 : il manque 76 |
| 8 | 1 030 | 933 | 97 | 835 : il manque 98 |
| 9 | 1 275 | 1 155 | 120 | 1 030 : il manque 125 |
| 10 | 1 680 | 1 523 | 157 | 1 275 : il manque 248 |
| 11 | 2 065 | 1 876 | 189 | 1 680 : il manque 196 |
| 12 | 2 555 | 2 322 | 233 | 2 065 : il manque 257 |
| 13 | 3 180 | 2 888 | 292 | 2 555 : il manque 333 |
| 14 | 3 970 | 3 607 | 363 | 3 180 : il manque 427 |
| 15 | 4 975 | 4 522 | 453 | 3 970 : il manque 552 |
| 16 | 6 260 | 5 688 | 572 | 4 975 : il manque 713 |
| 17 | 7 895 | 7 176 | 719 | 6 260 : il manque 916 |
| 18 | 9 990 | 9 080 | 910 | 7 895 : il manque 1 185 |
| 19 | 12 670 | 11 517 | 1 153 | 9 990 : il manque 1 527 |
| 20 | 16 110 | 14 642 | 1 468 | 12 670 : il manque 1 972 |
<!-- skylab-power:end -->

Le tableau compte chaque module au même niveau. La Ferme à Thulium en consomme les quatre cinquièmes au sommet (11 695 au niveau 20, contre 14 642 pour les huit), si bien qu’une station dont cette ferme est très en avance sur le reste a besoin de plus de Solaire que ne le suggère son Noyau.

### Récupération {#collecting}

Chaque ferme et chaque collecteur a un réservoir pour environ 72 heures de sa production. La récupération se fait à la main.

- **Capacité** : une fois son réservoir plein, un module cesse de produire jusqu’à ce que vous récupériez.
- **Fermes** : les crédits et le Thulium récupérés vont directement sur votre compte.
- **Collecteurs** : le minerai va dans l’Entrepôt de ressources, dans la limite de la place disponible.
- **Fonderie** : les plaques vont dans votre inventaire, quand votre vaisseau est amarré.
- **Tout récupérer** prend tout d’un coup, modules éteints et en cours d’amélioration compris.
- Un badge **(!)** signale un réservoir plein que vous pouvez vider, et des plaques qui attendent dans la Fonderie, sur la page Skylab et sur la ligne Skylab de la barre latérale.

### La réinitialisation {#the-wipe}

Le Skylab n’est jamais réinitialisé : les modules gardent leurs niveaux, l’Entrepôt de ressources garde son minerai et le Centre de recherche garde ses technologies, son réservoir de science, la Dark Matter qu’il contient et une recherche en cours. Les plaques de votre inventaire sont des objets comme les autres : elles suivent donc les [règles de réinitialisation](/wiki/03-Mechanics/Wipe-Timeline.md).

## Planifier votre Skylab {#planning-your-skylab}

Le Skylab met des semaines à grandir : un peu de planification paie donc. Les chiffres sont ceux des tableaux ci-dessus.

### Que monter en premier {#what-to-upgrade-first}

1. **Solaire, puis la Ferme à crédits.** Solaire coûte 500 crédits et 50 Thulium et rien ne tourne sans lui ; la Ferme à crédits ne coûte rien. Les dix [missions Station](/wiki/03-Mechanics/Quests.md#station-missions) vous guident dans ces premières étapes et vous versent 52 000 crédits et 610 Thulium pour elles, en base : votre monde, vos boosters et les bonus de votre clan la multiplient.
2. **Ensuite la Ferme à Thulium : c’est votre principale source de Thulium.** Au niveau 10, elle produit 450 Thulium par heure, 10 800 par jour, autant que rapportent 54 victimes d’un [Crystalys](/wiki/04-Aliens/Crystalys.md) en Alpha (200 chacune). La montée jusqu’au niveau 10 coûte 1 154 000 crédits et 4 190 Thulium, construction comprise. Au niveau 15, la ferme produit 22 800 par jour, et 38 400 au niveau 20. Son réservoir contient 72 heures : revenez donc au moins tous les trois jours. Ce que le Thulium permet d’acheter est sur la page [Ressources](/wiki/06-Items/Resources.md#thulium).
3. **La Ferme à crédits est le revenu régulier d’appoint.** Au niveau 10, elle produit 7 500 crédits par heure, 180 000 par jour, pour 840 000 crédits et 109 Thulium. Les niveaux élevés se rentabilisent lentement : l’étape du niveau 9 au niveau 10 coûte 300 000 crédits pour 1 000 de plus par heure, soit 300 heures. Montez-la quand il vous reste des crédits.
4. **Gardez le Noyau occupé.** Rien ne dépasse le Noyau, et le Noyau seul demande environ 16 jours et demi pour atteindre le niveau 20. Il n’y a pas de file d’attente : lancez donc son étape suivante chaque fois que vous revenez.
5. **Construisez la chaîne d’approvisionnement d’un bloc.** Les collecteurs, l’Entrepôt de ressources et la Fonderie s’ouvrent au niveau 5 du Noyau. Un collecteur ne peut mettre du minerai en banque que dans un Entrepôt de ressources, et la banque contient un jour de production de son collecteur au niveau 1 et quatre jours au niveau 20 : montez donc l’Entrepôt avec les collecteurs, sinon le minerai attend dans leurs réservoirs.

### Planifier une amélioration de Solaire {#timing-a-solar-upgrade}

Pendant son amélioration, Solaire produit un quart de son énergie, et une station consomme presque toujours davantage. Les fermes et les collecteurs s’arrêtent alors pendant toute l’amélioration : ce qu’ils contiennent reste, mais ce qu’ils auraient produit est perdu. Le tableau donne, pour chaque étape de Solaire, sa durée, la plus grande station qui tourne encore pendant celle-ci (tous les modules au même niveau, Noyau et chaîne d’approvisionnement compris ; une station plus petite tient un peu plus longtemps) et ce qu’une Ferme à crédits et une Ferme à Thulium de ce niveau auraient produit pendant ce temps. Par exemple, Solaire du niveau 10 au niveau 11 prend 4 heures, et des fermes de niveau 10 auraient produit 30 000 crédits et 1 800 Thulium pendant ce temps.

| Amélioration de Solaire | Durée | Station qui continue de tourner, jusqu’au niveau | La Ferme à crédits produit pendant ce temps | La Ferme à Thulium produit pendant ce temps |
| :--- | ---: | ---: | ---: | ---: |
| 1 à 2 | 5 min | aucune | 42 | 4 |
| 2 à 3 | 15 min | aucune | 250 | 20 |
| 3 à 4 | 30 min | aucune | 750 | 55 |
| 4 à 5 | 45 min | aucune | 1 500 | 105 |
| 5 à 6 | 1 h | aucune | 2 500 | 180 |
| 6 à 7 | 1 h 15 min | aucune | 4 375 | 288 |
| 7 à 8 | 1 h 30 min | aucune | 6 750 | 420 |
| 8 à 9 | 2 h | 1 | 11 000 | 660 |
| 9 à 10 | 3 h | 2 | 19 500 | 1 140 |
| 10 à 11 | 4 h | 4 | 30 000 | 1 800 |
| 11 à 12 | 5 h | 5 | 45 000 | 2 750 |
| 12 à 13 | 6 h | 6 | 66 000 | 3 900 |
| 13 à 14 | 8 h | 7 | 104 000 | 6 000 |
| 14 à 15 | 10 h | 8 | 150 000 | 8 500 |
| 15 à 16 | 12 h | 9 | 204 000 | 11 400 |
| 16 à 17 | 16 h | 10 | 320 000 | 17 600 |
| 17 à 18 | 18 h | 11 | 432 000 | 22 500 |
| 18 à 19 | 20 h | 12 | 580 000 | 28 000 |
| 19 à 20 | 1 j | 13 | 840 000 | 36 000 |

- **Montez les fermes en même temps que Solaire.** Un module en amélioration ne produit rien et ne consomme pas d’énergie de toute façon : le temps qu’une ferme passe en amélioration pendant la pause ne coûte donc rien de plus.
- **Gardez les autres modules bas si vous ne pouvez pas vous offrir une pause.** Une station ne tourne pendant une amélioration de Solaire que si tous ses autres modules sont au moins cinq niveaux en dessous de Solaire (six à partir du niveau 10 de Solaire), et une station complète demande un peu plus, comme le montre le tableau.
- **Éteignez ce dont vous pouvez vous passer.** Un module éteint ne consomme pas d’énergie : éteindre la Ferme à Thulium, la plus gourmande (80 au niveau 1, et 30 % de plus à chaque niveau), fait donc de la place pour les autres.
