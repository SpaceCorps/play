<!-- wiki-i18n source: bf987d259afc1762 -->
<!-- wiki-i18n title: Recherche -->
# Recherche {#research}

Le **Centre de recherche** est le laboratoire de votre [Skylab](/wiki/03-Mechanics/Skylab.md). Vous lui donnez des ressources, il les transforme en **science**, et la science recherche des **technologies**. Toute fabrication à l’[Assemblage](/wiki/06-Items/Overview.md#upgrading-modules) exige d’abord sa technologie : un vaisseau, un laser, un propulseur ou un CPU ne peut être fabriqué tant qu’il n’a pas été recherché.

Cette page rassemble l’arbre complet des technologies avec la durée de chacune, la science que donne chaque ressource, le boost de Thulium, la règle de la Dark Matter et les nouveaux CPU. Ses chiffres sont lus dans les données mêmes du jeu : ce sont donc toujours ceux du jeu.

![The Research view with a technology that needs Dark Matter picked: its Dark Matter row, the Add and Take back buttons, where Dark Matter comes from and the Wiki button](../../img/wiki-img/shots/research-dark-matter.jpg)
![The Research view filtered to the Defence tree: the shield and hull formations, each a technology with its Dark Matter](../../img/wiki-img/shots/research-formations.jpg)
![The Research view of the Skylab with the pointer on Impulse Thruster III: its kind and tier, what it does, its numbers, the four tiers of its family and what Assembly asks to craft it](../../img/wiki-img/shots/research-hover.jpg)

## Le Centre de recherche {#the-research-centre}

<!-- research-centre:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **S’ouvre au niveau 10 du Noyau.** Le Centre de recherche est un module de votre [Skylab](/wiki/03-Mechanics/Skylab.md), construit comme les autres : 25 Ship Fragments de votre inventaire (vaisseau posé), 25 000 crédits et 500 Thulium. Son écran est la vue **Recherche** de la page du Skylab.
- **Niveaux 1 à 10.** Un niveau plus élevé donne un réservoir plus grand et consomme plus d’énergie. Il n’accélère pas la recherche : une technologie prend le même temps à chaque niveau.
- **Le réservoir.** Le Centre garde sa science dans un réservoir qui contient 12 h de recherche au niveau 1 et 25 % de plus à chaque niveau (voir le tableau ci-dessous).
- **Du carburant à la science.** Une ressource que vous introduisez devient aussitôt de la science, comme le montre le tableau du carburant. Une recherche brûle 1 de science par seconde de sa durée de recherche ; réservoir vide, elle attend, et elle reprend quand vous alimentez le Centre.
- **Une première heure offerte.** Un nouveau Centre démarre avec 3 600 de science dans son réservoir, soit 1 h de recherche.
- **Une à la fois.** Le Centre ne recherche qu’une technologie à la fois, mais avec le bouton Mettre en file vous pouvez en placer jusqu’à 5 de plus derrière elle. Chacune démarre toute seule dès que la précédente est terminée, même en votre absence. Mettre en file ne coûte rien : une technologie prend sa Dark Matter au démarrage, et une technologie en file se retire gratuitement.
- **Pendant votre absence.** Une recherche suit l’horloge du serveur : elle continue donc après votre déconnexion, jusqu’à ce qu’elle soit terminée ou que le réservoir soit vide. Une panne ou une amélioration du Centre ne l’arrête pas.
- **Énergie.** Le Centre consomme 25 au niveau 1 et 15 % de plus à chaque niveau, et il ne peut pas être éteint.
- **La réinitialisation garde tout :** vos technologies, la science du réservoir, la Dark Matter introduite, une recherche en cours et le boost.
- **Ce que vous possédez est à vous.** Quand la recherche est arrivée dans le jeu, chaque pilote a reçu la technologie de chaque objet qu’il détenait déjà, et les technologies que ceux-ci exigeaient. Un objet qui vous parvient plus tard (un cadeau, un code, une récompense) ne débloque pas sa technologie, à une exception près : un Engine II, un Engine III, un Adaptive Core II ou un Adaptive Core III que vous donne un code, une quête, une invitation ou un administrateur débloque aussitôt sa technologie et celles qu’il exige.
- **En dessous du niveau 10 du Noyau,** vous ne pouvez pas faire de recherche, donc rien de nouveau à l’Assemblage pour l’instant. Les missions Station vous font monter le Noyau.

<!-- research-centre:end -->

**Les amplis laser et le dernier palier.** Les Damage, Crit et Penetration Amps des paliers II à IV se recherchent comme tout ce qui se fabrique. Les pilotes qui possédaient ou avaient en file des amplis à l’arrivée des gammes d’amplis ont reçu la technologie de chacun d’eux et celle des paliers en dessous. Treize technologies demandent une technologie d’un autre arbre, celle de la Dark Matter Plate, de l’arbre Ressources, parce que le dernier palier de chaque chaîne d’amélioration demande trois plates : les Damage, Crit et Penetration Amps du palier IV, les Absorption et Capacity Shield Cells du palier IV, les Impulse et Momentum Thrusters du palier IV, le Heavy Shield Core, l’Engine III, l’Adaptive Core III, le Helios Beam, l’Extra Slots CPU III et le Base CPU II. Un pilote qui a déjà recherché l’une d’elles la garde, mais il lui faut la technologie de la plate pour fabriquer ses plates. L’arbre ci-dessous ne trace aucune flèche pour elle, mais le tableau la liste et la carte en jeu la nomme ([Dark Matter et Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)).

Dans la vue **Recherche** de votre Skylab, une technologie en dit plus qu’une case des arbres ci-dessous. Pointez une technologie et une carte s’ouvre avec la durée de recherche et la science qu’elle brûle puis, dessous, ce que l’objet **est et fait** : son type et son rang dans sa famille (par exemple le troisième des quatre Impulse Thruster), sa description, ses valeurs telles que le hangar et la boutique les montrent (les dégâts, le taux critique et la portée d’un laser, la capacité, la recharge et l’absorption d’un bouclier, le boost de vitesse et le multiplicateur d’un propulseur, les dégâts, l’explosion et la portée d’une roquette, ce qu’une formation de drones apporte et ce qu’elle vous coûte), un petit tableau des rangs de sa famille, et ce que l’Assemblage demande ensuite pour le fabriquer : le temps, les crédits et le Thulium et les matériaux. Vous voyez ainsi ce que donne un rang avant de le rechercher. Cliquez sur une technologie pour la choisir : la carte à côté de l’arbre montre la même chose en entier, sous le bouton **Lancer la recherche**. Tant qu’une recherche tourne, **Mettre en file** prend la place du bouton de lancement : une technologie en file montre son numéro d’ordre dans l’arbre, et une carte de la file sous la recherche en cours les liste toutes, chacune avec une croix pour la retirer. Si la suivante ne peut pas démarrer (la Dark Matter dont elle a besoin n’est pas dans le Centre, ou le réservoir est vide), la file attend et dit pourquoi, jusqu’à ce que vous y remédiiez et appuyiez sur **Lancer la file**.

### Le réservoir à chaque niveau {#the-tank-at-every-level}

<!-- research-tank:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Niveau | Réservoir (science) | Contient de la recherche pour | … avec le boost | Énergie |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 43 200 | 12 h | 6 h | 25 |
| 2 | 54 000 | 15 h | 7,5 h | 28,7 |
| 3 | 67 500 | 18,8 h | 9,4 h | 33,1 |
| 4 | 84 375 | 23,4 h | 11,7 h | 38 |
| 5 | 105 469 | 29,3 h | 14,6 h | 43,7 |
| 6 | 131 836 | 36,6 h | 18,3 h | 50,3 |
| 7 | 164 795 | 45,8 h | 22,9 h | 57,8 |
| 8 | 205 994 | 57,2 h | 28,6 h | 66,5 |
| 9 | 257 492 | 71,5 h | 35,8 h | 76,5 |
| 10 | 321 865 | 89,4 h | 44,7 h | 87,9 |

<!-- research-tank:end -->

## Carburant {#fuel}

Vous alimentez le Centre en ressources, et chaque unité devient aussitôt de la science. Plus une unité demande de travail pour être obtenue, plus elle donne de science : les chiffres suivent la difficulté de l’obtenir, pas son étiquette de rareté. Les minerais font exception : une unité donne plus de science que les secondes qu’un collecteur met à l’extraire, si bien qu’une heure du minerai d’un collecteur à mi-parcours de ses niveaux alimente environ deux heures de recherche. Les minerais viennent de l’Entrepôt de ressources de votre [Skylab](/wiki/03-Mechanics/Skylab.md#resource-storage) ; toute autre ressource vient de votre inventaire, et votre vaisseau doit être amarré. La Velkonite Reinforced Plate, l’Orvium Reinforced Plate, la Dark Matter Plate, la Dark Matter, les crédits et le Thulium ne peuvent pas être brûlés ; la Reinforced Hull Plate, si. La Velkonite et l’Orvium que les caisses d’une excavatrice mettent dans votre inventaire arrivent dans l’Entrepôt de ressources par la [Baie à minerai](/wiki/03-Mechanics/Skylab.md#ore-bay).

<!-- research-fuel:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Ressource | Rareté | Prise dans | Science par unité | Unités pour 1 heure |
| :--- | :--- | :--- | ---: | ---: |
| [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) | Commun | Votre inventaire | 5 | 720 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | Commun | Votre inventaire | 5 | 720 |
| [Daraxium](/wiki/06-Items/Resources.md#daraxium) | Commun | Votre inventaire | 7 | 515 |
| [Nyxite](/wiki/06-Items/Resources.md#nyxite) | Commun | Votre inventaire | 7 | 515 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | Commun | Votre inventaire | 8 | 450 |
| [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) | Commun | Votre inventaire | 33 | 110 |
| [Power Core](/wiki/06-Items/Resources.md#power-core) | Peu commun | Votre inventaire | 100 | 36 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | Peu commun | Entrepôt de ressources | 210 | 18 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | Rare | Entrepôt de ressources | 321 | 12 |
| [Ancient Control Unit](/wiki/06-Items/Resources.md#ancient-control-unit) | Rare | Votre inventaire | 650 | 6 |

La dernière colonne donne le nombre d’unités qui font tourner une heure de recherche sans le boost, arrondi au supérieur ; avec le boost, il y en a 2 fois plus.

<!-- research-fuel:end -->

## Le boost de Thulium {#the-thulium-boost}

<!-- research-boost:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **5 000 Thulium** achètent un boost : le Centre recherche **2 fois plus vite pendant 24 heures**.
- Il **brûle aussi la science 2 fois plus vite** : un boost achète donc du temps et jamais du carburant : une technologie brûle la même science, avec ou sans boost.
- Un boost commence au moment où vous l’achetez et suit l’horloge, que le réservoir ait du carburant ou non ; achetez-le donc pendant qu’une recherche tourne. Le Centre le refuse quand rien n’est en cours de recherche.
- Les boosts s’additionnent : en acheter un pendant qu’un autre tourne ajoute 24 heures à sa fin, jusqu’à 72 heures d’avance. Un boost appartient à votre Centre de recherche, pas à une recherche en particulier.

Ce qu’un boost fait à la durée d’une recherche, avec le boost dès son début :

| Durée de recherche | Avec le boost | Boosts pour toute la recherche | Thulium |
| :--- | :--- | ---: | ---: |
| 30 min | 15 min | 1 | 5 000 |
| 3 h | 1 h 30 min | 1 | 5 000 |
| 6 h | 3 h | 1 | 5 000 |
| 10 h | 5 h | 1 | 5 000 |
| 1 j | 12 h | 1 | 5 000 |
| 2 j | 1 j | 1 | 5 000 |

<!-- research-boost:end -->

## Dark Matter

Les technologies du haut de l’arbre exigent aussi de la Dark Matter. Elle vient du [trou noir](/wiki/03-Mechanics/Black-Hole.md#dark-matter), où une roquette N.I.K.E. qui l’atteint en laisse un peu, et, de temps en temps, d’un Dormant Pulse de l’[Essaim Dormant](/wiki/05-Swarms/Dormant-Swarm.md).

<!-- research-dark-matter:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **10 Dark Matter** pour chacune des 16 technologies du tableau ci-dessous, en plus de la science : introduisez-la dans le Centre de recherche (depuis votre inventaire, vaisseau posé) avant de commencer, et la recherche la prend à son démarrage.
- **La règle :** un objet de rareté Épique ou supérieure dont la recherche dure 10 h ou plus. La N.I.K.E., qui sert à produire la Dark Matter, n’en a jamais besoin.
- **Les formations de drones** sont hors règle : chaque recherche de formation demande de la Dark Matter, 5, 13 ou 20 selon sa puissance, comme le montre le tableau.
- **Le blindage de coque** est lui aussi hors règle : ses deux recherches demandent plus, 25 Dark Matter pour un jour de recherche et 40 pour deux jours, comme le montre le tableau.
- **Si vous annulez une recherche,** la Dark Matter introduite pour elle revient au Centre. La progression et la science déjà brûlée, non.
- Toutes ensemble demandent 414 Dark Matter.

| Technologie | Rareté | Durée de recherche | Dark Matter |
| :--- | :--- | :--- | ---: |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | Épique | 10 h | 10 |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | Épique | 10 h | 10 |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | Épique | 10 h | 10 |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | Épique | 10 h | 10 |
| [Starfire-III](/wiki/06-Items/Lasers.md#lasers) | Mythique | 1 j | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | Mythique | 1 j | 10 |
| [Damage Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Épique | 10 h | 10 |
| [Crit Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Épique | 10 h | 10 |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | Épique | 1 j | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | Épique | 1 j | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | Mythique | 2 j | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | Mythique | 1 j | 10 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | Légendaire | 1 j | 10 |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | Épique | 1 j | 10 |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | Épique | 1 j | 10 |
| [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épique | 10 h | 5 |
| [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épique | 1 j | 13 |
| [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épique | 10 h | 5 |
| [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Mythique | 2 j | 20 |
| [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épique | 10 h | 5 |
| [Ballista Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épique | 1 j | 13 |
| [Stiletto Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Mythique | 2 j | 20 |
| [Rampart Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Mythique | 2 j | 20 |
| [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épique | 1 j | 13 |
| [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épique | 10 h | 5 |
| [Culler Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épique | 1 j | 13 |
| [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épique | 1 j | 13 |
| [Auger Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épique | 1 j | 13 |
| [Cordon Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épique | 1 j | 13 |
| [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épique | 10 h | 5 |
| [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | Épique | 1 j | 13 |
| [Penetration Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Épique | 10 h | 10 |
| [Hull Plating II](/wiki/06-Items/Hull-Plating.md#the-three-platings) | Rare | 1 j | 25 |
| [Hull Plating III](/wiki/06-Items/Hull-Plating.md#the-three-platings) | Épique | 2 j | 40 |

<!-- research-dark-matter:end -->

## L’arbre des technologies {#the-technology-tree}

Chaque case est une technologie : l’objet qu’elle vous permet de fabriquer, avec sa durée de recherche sous le nom (l’horloge) et, si elle exige de la Dark Matter, l’insigne de la Dark Matter. Une flèche va d’une technologie à celle qui en a besoin, que vous recherchez d’abord ; une case sans flèche peut être recherchée tout de suite. Pointez une case pour voir la durée de recherche, la science qu’elle brûle et ce que l’Assemblage demande ensuite pour l’objet, et cliquez dessus pour ouvrir la page de l’objet. Les arbres sont dessinés à partir des données mêmes du jeu. Deux des arbres, **Défense** et **Frappe et mobilité**, contiennent les seize [formations de drones](/wiki/03-Mechanics/Formations.md).

<!-- research-tree:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

### Propulsion et vitesse {#tree-propulsion}

```tree research
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Engine I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Adaptive Core II | hybrid-generator, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Adaptive Core I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core III | hybrid-generator, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Adaptive Core II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-

Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
Engine II => Engine III
Adaptive Core II => Adaptive Core III
```

### Boucliers et défense {#tree-shields}

```tree research
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cores

Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```

### Lasers et munitions {#tree-lasers}

```tree research
Quantum Laser III | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Quantum Laser II, 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-III | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser III, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-III, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Damage Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Crit Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Damage Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Damage Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Crit Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Crit Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Penetration Amp I, 20 Daraxium, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Penetration Amp II, 1 Power Core, 30 Nyxite, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp IV | laser-amp, epic | craft 1200 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Penetration Amp III, 1 Power Core, 30 Cataclysite, 40 Quorvium, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-

Quantum Laser III => Starfire-III => Helios Beam
Damage Amp II => Damage Amp III => Damage Amp IV
Crit Amp II => Crit Amp III => Crit Amp IV
Penetration Amp II => Penetration Amp III => Penetration Amp IV
```

### Boosters {#tree-boosters}

```tree research
Laser Damage Booster II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
```

### Drones {#tree-drones}

```tree research
Master Drone | drone, rare | craft 40000 Thulium, 60 s | research 36000 s, 36000 science | 1 Slave Drone, 100 Ship Fragment | /wiki/06-Items/Drones.md#available-drones
```

### Vaisseaux {#tree-ships}

```tree research
Paragon | ship, rare | craft 1500 Thulium, 900 s | research 21600 s, 21600 science | 120 Ship Fragment, 20 Reinforced Hull Plate, 5 Power Core | /wiki/02-Ships/Paragon.md
Ironclad | ship, epic | craft 10500 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit | /wiki/02-Ships/Ironclad.md
Storm | ship, epic | craft 15000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit | /wiki/02-Ships/Storm.md
Wraith | ship, mythical | craft 20000 Thulium, 900 s | research 172800 s, 172800 science, 10 Dark Matter | 300 Ship Fragment, 50 Reinforced Hull Plate, 15 Power Core, 3 Ancient Control Unit | /wiki/02-Ships/Wraith.md
```

### Ressources {#tree-resources}

```tree research
Dark Matter Plate | resource, mythical | craft 250 Thulium, 120 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Velkonite Reinforced Plate, 1 Orvium Reinforced Plate, 5 Dark Matter | /wiki/06-Items/Resources.md#dark-matter-plate
```

### Roquettes {#tree-rockets}

```tree research
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
```

### CPU {#tree-cpus}

```tree research
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 6 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 2 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Extras.md#base-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu

Extra Slots CPU I => Extra Slots CPU II => Extra Slots CPU III
Base CPU I => Base CPU II => Jump CPU
```

### Défense {#tree-defence}

```tree research
Testudo Formation | formation, epic | craft 7500 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Adamant Formation | formation, epic | craft 9000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Rampart Formation | formation, mythical | craft 38500 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Sanctum Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Redoubt Formation | formation, epic | craft 21000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Cordon Formation | formation, epic | craft 21500 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations

Testudo Formation => Sanctum Formation => Rampart Formation
Adamant Formation => Redoubt Formation => Cordon Formation
```

### Frappe et mobilité {#tree-strike-mobility}

```tree research
Bodkin Formation | formation, epic | craft 21000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Asterism Formation | formation, epic | craft 7000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Gemini Formation | formation, mythical | craft 38000 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Ballista Formation | formation, epic | craft 24000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Stiletto Formation | formation, mythical | craft 46000 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Shrike Formation | formation, epic | craft 8500 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Culler Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Auger Formation | formation, epic | craft 20500 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Centurion Formation | formation, epic | craft 8000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Gyre Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations

Asterism Formation => Bodkin Formation => Ballista Formation
Gemini Formation => Stiletto Formation
Centurion Formation => Shrike Formation => Culler Formation
Gyre Formation => Auger Formation
```

### Blindage de coque {#tree-hull-plating}

```tree research
Hull Plating II | hull-plating, rare | craft 2500 Thulium, 300 s | research 86400 s, 86400 science, 25 Dark Matter | 1 Hull Plating I, 150 Ship Fragment, 20 Reinforced Hull Plate, 6 Power Core, 5 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating III | hull-plating, epic | craft 4000 Thulium, 600 s | research 172800 s, 172800 science, 40 Dark Matter | 1 Hull Plating II, 300 Ship Fragment, 40 Reinforced Hull Plate, 12 Power Core, 1 Ancient Control Unit, 8 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings

Hull Plating II => Hull Plating III
```


<!-- research-tree:end -->

## Designs de vaisseaux et emplacements de blindage {#ship-technologies}

La famille Vaisseaux de la vue de recherche de votre Skylab contient deux sortes de technologies qui ne sont pas des fabrications. L’arbre ci-dessus les laisse de côté, parce que ce qu’elles ouvrent est un emplacement ou une transformation, pas un objet.

- **Emplacements de blindage.** Une technologie par [emplacement de blindage](/wiki/06-Items/Hull-Plating.md#hull-plate-slots) des quatre vaisseaux que vous fabriquez. Chacune vient après la précédente, la première après la technologie du vaisseau lui-même. Dans le jeu, les emplacements d’un vaisseau forment une seule carte avec un point par emplacement.
- **Designs de vaisseaux.** Une technologie par [design](/wiki/03-Mechanics/Ship-Designs.md). Chacune demande la technologie de son vaisseau et celle de la Dark Matter Plate.

Leurs durées, leur Dark Matter et les totaux sont sur la page [Designs de vaisseaux](/wiki/03-Mechanics/Ship-Designs.md#the-technologies).

## Toutes les technologies {#all-the-technologies}

<!-- research-technologies:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Technologie | Exige d’abord | Classe | Durée de recherche | Science | Dark Matter |
| :--- | :--- | :--- | ---: | ---: | ---: |
| [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 min | 1 800 | – |
| [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 h | 10 800 | – |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 h | 36 000 | 10 |
| [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 min | 1 800 | – |
| [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 h | 10 800 | – |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 h | 36 000 | 10 |
| [Engine III](/wiki/06-Items/Propulsion.md#engines) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Engine II](/wiki/06-Items/Propulsion.md#engines) | B | 3 h | 10 800 | – |
| [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 min | 1 800 | – |
| [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 h | 10 800 | – |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10 h | 36 000 | 10 |
| [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 min | 1 800 | – |
| [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 h | 10 800 | – |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10 h | 36 000 | 10 |
| [Heavy Shield Core](/wiki/06-Items/Shields.md#shield-cores) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | B | 3 h | 10 800 | – |
| [Quantum Laser III](/wiki/06-Items/Lasers.md#lasers) | – | B | 3 h | 10 800 | – |
| [Starfire-III](/wiki/06-Items/Lasers.md#lasers) | [Quantum Laser III](/wiki/06-Items/Lasers.md#lasers) | D | 1 j | 86 400 | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Starfire-III](/wiki/06-Items/Lasers.md#lasers) | D | 1 j | 86 400 | 10 |
| [Damage Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Damage Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10 h | 36 000 | 10 |
| [Crit Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Crit Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10 h | 36 000 | 10 |
| [Laser Damage Booster II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 h | 10 800 | – |
| [Shield Wall Booster II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 h | 10 800 | – |
| [Hull Plating Booster II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 h | 10 800 | – |
| [Master Drone](/wiki/06-Items/Drones.md#available-drones) | – | C | 10 h | 36 000 | – |
| [Paragon](/wiki/02-Ships/Paragon.md) | – | B | 6 h | 21 600 | – |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | – | D | 1 j | 86 400 | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | – | D | 1 j | 86 400 | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | – | D | 2 j | 172 800 | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | – | D | 1 j | 86 400 | 10 |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | B | 3 h | 10 800 | – |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | D | 1 j | 86 400 | 10 |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | – | A | 30 min | 1 800 | – |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | C | 10 h | 36 000 | – |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | D | 1 j | 86 400 | 10 |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | – | B | 3 h | 10 800 | – |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10 h | 36 000 | – |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | D | 1 j | 86 400 | 10 |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | – | B | 6 h | 21 600 | – |
| [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 h | 36 000 | 5 |
| [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 j | 86 400 | 13 |
| [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 h | 36 000 | 5 |
| [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | D | 2 j | 172 800 | 20 |
| [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 h | 36 000 | 5 |
| [Ballista Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 j | 86 400 | 13 |
| [Stiletto Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 2 j | 172 800 | 20 |
| [Rampart Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 2 j | 172 800 | 20 |
| [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 j | 86 400 | 13 |
| [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | C | 10 h | 36 000 | 5 |
| [Culler Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 j | 86 400 | 13 |
| [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 j | 86 400 | 13 |
| [Auger Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 j | 86 400 | 13 |
| [Cordon Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 j | 86 400 | 13 |
| [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 h | 36 000 | 5 |
| [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | D | 1 j | 86 400 | 13 |
| [Damage Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30 min | 1 800 | – |
| [Damage Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Damage Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3 h | 10 800 | – |
| [Crit Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30 min | 1 800 | – |
| [Crit Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Crit Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3 h | 10 800 | – |
| [Penetration Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30 min | 1 800 | – |
| [Penetration Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Penetration Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3 h | 10 800 | – |
| [Penetration Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Penetration Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10 h | 36 000 | 10 |
| [Hull Plating II](/wiki/06-Items/Hull-Plating.md#the-three-platings) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | D | 1 j | 86 400 | 25 |
| [Hull Plating III](/wiki/06-Items/Hull-Plating.md#the-three-platings) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Hull Plating II](/wiki/06-Items/Hull-Plating.md#the-three-platings) | D | 2 j | 172 800 | 40 |
| [Engine II](/wiki/06-Items/Propulsion.md#engines) | – | A | 30 min | 1 800 | – |
| [Adaptive Core II](/wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-) | – | A | 30 min | 1 800 | – |
| [Adaptive Core III](/wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-) | [Adaptive Core II](/wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | B | 3 h | 10 800 | – |

Les classes, par durée de recherche :

| Classe | Durée de recherche | Technologies | L’une après l’autre | Science | Dark Matter |
| :--- | :--- | ---: | ---: | ---: | ---: |
| A | 30 min | 10 | 5 h | 18 000 | 0 |
| B | 3 h à 6 h | 18 | 2 j 12 h | 216 000 | 0 |
| C | 10 h | 15 | 6 j 6 h | 540 000 | 95 |
| D | 1 j à 2 j | 22 | 27 j | 2 332 800 | 319 |
| Toutes |  | 65 | 35 j 23 h | 3 106 800 | 414 |

Recherché une technologie après l’autre, l’arbre entier prend 35 j 23 h. Avec le boost actif en permanence, il prend 17 j 23 h 30 min, soit 18 boosts et 90 000 Thulium ; la science est la même.

<!-- research-technologies:end -->

## Les CPU {#the-cpus}

Les nouveaux CPU se recherchent aussi ici, puis se fabriquent à l’Assemblage. Le même tableau et les mêmes notes figurent sur la page [Extras](/wiki/06-Items/Extras.md#research-cpus).

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | Durée de recherche | Exige d’abord | Thulium pour fabriquer | Durée de fabrication |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 min | – | 12 000 | 5 min |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10 h | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 000 | 10 min |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1 j | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75 000 | 15 min |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3 h | – | 8 000 | 5 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10 h | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | 20 000 | 10 min |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1 j | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40 000 | 15 min |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6 h | – | 15 000 | 10 min |

Aucun n’est vendu à la boutique : recherchez la technologie, puis fabriquez le CPU à l’Assemblage. Pointez un CPU dans son arbre pour voir ce que l’Assemblage demande pour le fabriquer.

### Extra Slots CPUs

- **Ce qu’ils font.** Les Extra Slots CPU I, II et III donnent à chaque vaisseau 3, 5 et 7 emplacements extras de plus, soit 6, 8 et 10 au total sur un vaisseau qui en possède 3 en propre, et 5, 7 et 9 sur un vaisseau qui en possède 2. Un CPU supérieur remplace le précédent : le II ne s’ajoute pas au I.
- **Installé, pas transporté.** Un Extra Slots CPU n’est pas un objet : quand vous le récupérez à l’Assemblage, il s’installe dans votre Skylab, pour chaque vaisseau dans les deux configurations, et ne prend aucun emplacement. Il reste après la réinitialisation.
- **Dans l’ordre.** Fabriquez-les l’un après l’autre : le II seulement quand le I est installé, le III seulement quand le II est installé ; d’ici là, l’Assemblage vous dit lequel installer d’abord. Les trois coûtent 117 000 Thulium en tout : 12 000, 30 000 et 75 000.

### Jump CPU

- **Ce qu’il fait.** Il fait sauter votre vaisseau vers n’importe quel secteur de corporation de votre monde, celui de votre propre corporation comme ceux des autres, secteurs d’origine compris (`M`, `T` et `G`, secteurs 1 à 4), pour **500 Thulium** le saut. Il n’a pas de limite d’utilisations : vous ne payez que le Thulium. Il ne mène jamais à un secteur dangereux (`DS`) ni à un secteur neutre (`N`).
- **Le saut.** Appuyez sur l’emplacement JMP, choisissez le secteur sur la carte du Système stellaire et confirmez : le vaisseau se charge pendant 5 secondes, puis arrive à une porte de ce secteur, protégé comme après n’importe quel saut de porte. Le CPU refroidit pendant 30 secondes après votre arrivée.
- **Pas en combat.** Il ne peut pas démarrer dans les 10 secondes qui suivent un tir ou un coup reçu, et un tir ou un coup pendant la charge annule le saut ; rien n’est alors payé. Vous ne pouvez pas sauter occulté.
- **Pas depuis un secteur neutre :** un pilote dans un secteur neutre, ou sans corporation, ne peut pas l’utiliser.
- Il peut quitter un secteur dangereux quand vous n’êtes pas en combat.

### Base CPUs

- **Ce qu’ils font.** Ils téléportent votre vaisseau à la base de votre corporation, dans la zone sûre autour de sa station (`M-1`, `T-1` ou `G-1`, le secteur de Mission Control), sans coût en Thulium. Vous les lancez depuis l’emplacement BSE de la barre rapide.
- **Pas en combat.** Une charge de 10 secondes, la même pour les deux. Elle ne peut pas démarrer dans les 10 secondes qui suivent un tir ou un coup reçu, ni occulté, ni quand vous êtes déjà dans la zone sûre de votre base, et un tir ou un coup pendant la charge l’annule.

| CPU | Utilisations | Recharge |
| :--- | ---: | ---: |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 10 | 10 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 25 | 5 min |

- **Épuisé, pas rechargé.** Chaque utilisation consomme l’une des utilisations du CPU, et un CPU qui n’en a plus disparaît : fabriquez-en un nouveau. Si les deux sont installés, le meilleur (II) est utilisé en premier.

### Auto-Repair CPU

- **Ce qu’il fait.** Il envoie tout seul le Repair Drone installé dans vos emplacements extras, chaque fois que vous auriez pu l’envoyer à la main : votre coque n’est pas pleine, le drone n’est pas déjà sorti et 10 secondes se sont écoulées depuis le dernier coup reçu. Il n’y a aucun seuil de coque à régler.
- Il occupe un emplacement extra à lui et ne fait rien sans un Repair Drone dans un emplacement extra de la même configuration. Il n’envoie jamais un Repair Drone placé dans un emplacement de compétence (c’est le bouton Emergency Repair).
- **Si vous arrêtez le drone à la main,** le CPU le laisse tranquille jusqu’à ce que votre coque soit de nouveau pleine, ou jusqu’à ce que vous l’envoyiez vous-même.


<!-- research-cpus:end -->
