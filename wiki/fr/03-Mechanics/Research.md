<!-- wiki-i18n source: 55131889617bd886 -->
<!-- wiki-i18n title: Recherche -->
# Recherche {#research}

Le **Centre de recherche** est le laboratoire de votre [Skylab](/wiki/03-Mechanics/Skylab.md). Vous lui donnez des ressources, il les transforme en **science**, et la science recherche des **technologies**. Toute fabrication à l’[Assemblage](/wiki/06-Items/Overview.md#upgrading-modules) exige d’abord sa technologie : un vaisseau, un laser, un propulseur ou un CPU ne peut être fabriqué tant qu’il n’a pas été recherché.

Cette page rassemble l’arbre complet des technologies avec la durée de chacune, la science que donne chaque ressource, le boost de Thulium, la règle de la Dark Matter et les nouveaux CPU. Ses chiffres sont lus dans les données mêmes du jeu : ce sont donc toujours ceux du jeu.

## Le Centre de recherche {#the-research-centre}

<!-- research-centre:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **S’ouvre au niveau 10 du Noyau.** Le Centre de recherche est un module de votre [Skylab](/wiki/03-Mechanics/Skylab.md), construit comme les autres : 25 Ship Fragments de votre inventaire (vaisseau posé), 25 000 crédits et 500 Thulium. Son écran est la vue **Recherche** de la page du Skylab.
- **Niveaux 1 à 10.** Un niveau plus élevé donne un réservoir plus grand et consomme plus d’énergie. Il n’accélère pas la recherche : une technologie prend le même temps à chaque niveau.
- **Le réservoir.** Le Centre garde sa science dans un réservoir qui contient 12 h de recherche au niveau 1 et 25 % de plus à chaque niveau (voir le tableau ci-dessous).
- **Du carburant à la science.** Une ressource que vous introduisez devient aussitôt de la science, comme le montre le tableau du carburant. Une recherche brûle 1 de science par seconde de sa durée de recherche ; réservoir vide, elle attend, et elle reprend quand vous alimentez le Centre.
- **Une première heure offerte.** Un nouveau Centre démarre avec 3 600 de science dans son réservoir, soit 1 h de recherche.
- **Une à la fois.** Le Centre ne recherche qu’une technologie à la fois. Il n’y a pas de file d’attente.
- **Pendant votre absence.** Une recherche suit l’horloge du serveur : elle continue donc après votre déconnexion, jusqu’à ce qu’elle soit terminée ou que le réservoir soit vide. Une panne ou une amélioration du Centre ne l’arrête pas.
- **Énergie.** Le Centre consomme 25 au niveau 1 et 15 % de plus à chaque niveau, et il ne peut pas être éteint.
- **La réinitialisation garde tout :** vos technologies, la science du réservoir, la Dark Matter introduite, une recherche en cours et le boost.
- **Ce que vous possédez est à vous.** Quand la recherche est arrivée dans le jeu, chaque pilote a reçu la technologie de chaque objet qu’il détenait déjà, et les technologies que ceux-ci exigeaient. Un objet qui vous parvient plus tard (un cadeau, un code, une récompense) ne débloque pas sa technologie.
- **En dessous du niveau 10 du Noyau,** vous ne pouvez pas faire de recherche, donc rien de nouveau à l’Assemblage pour l’instant. Les missions Station vous font monter le Noyau.

<!-- research-centre:end -->

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

Vous alimentez le Centre en ressources, et chaque unité devient aussitôt de la science. Plus une unité demande de travail pour être obtenue, plus elle donne de science : les chiffres suivent la difficulté de l’obtenir, pas son étiquette de rareté, si bien qu’un Power Core (Peu commun) donne plus qu’un Orvium (Rare). Les minerais viennent de l’Entrepôt de ressources de votre [Skylab](/wiki/03-Mechanics/Skylab.md#resource-storage) ; toute autre ressource vient de votre inventaire, et votre vaisseau doit être posé. La Velkonite Reinforced Plate, la Orvium Reinforced Plate, la Dark Matter Plate, la Dark Matter, les crédits et le Thulium ne peuvent pas être brûlés ; la Reinforced Hull Plate, elle, le peut.

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
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | Peu commun | Entrepôt de ressources | 40 | 90 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | Rare | Entrepôt de ressources | 80 | 45 |
| [Power Core](/wiki/06-Items/Resources.md#power-core) | Peu commun | Votre inventaire | 100 | 36 |
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

## Dark Matter {#dark-matter}

Les technologies du haut de l’arbre exigent aussi de la Dark Matter. Elle vient du [trou noir](/wiki/03-Mechanics/Black-Hole.md#dark-matter), où une roquette N.I.K.E. qui l’atteint en laisse un peu, et, de temps en temps, d’un Dormant Pulse de l’[Essaim Dormant](/wiki/05-Swarms/Dormant-Swarm.md).

<!-- research-dark-matter:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **10 Dark Matter** pour chacune des 15 technologies du tableau ci-dessous, en plus de la science : introduisez-la dans le Centre de recherche (depuis votre inventaire, vaisseau posé) avant de commencer, et la recherche la prend à son démarrage.
- **La règle :** un objet de rareté Épique ou supérieure dont la recherche dure 10 h ou plus. La N.I.K.E., qui sert à produire la Dark Matter, n’en a jamais besoin.
- **Si vous annulez une recherche,** la Dark Matter introduite pour elle revient au Centre. La progression et la science déjà brûlée, non.
- Toutes ensemble demandent 150 Dark Matter.

| Technologie | Rareté | Durée de recherche | Dark Matter |
| :--- | :--- | :--- | ---: |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | Épique | 10 h | 10 |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | Épique | 10 h | 10 |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | Épique | 10 h | 10 |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | Épique | 10 h | 10 |
| [Starfire-3](/wiki/06-Items/Lasers.md#lasers) | Mythique | 1 j | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | Mythique | 1 j | 10 |
| [Nova Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Épique | 10 h | 10 |
| [Apex Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Épique | 10 h | 10 |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | Épique | 1 j | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | Épique | 1 j | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | Mythique | 2 j | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | Mythique | 1 j | 10 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | Légendaire | 1 j | 10 |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | Épique | 1 j | 10 |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | Épique | 1 j | 10 |

<!-- research-dark-matter:end -->

## L’arbre des technologies {#the-technology-tree}

Chaque case est une technologie : l’objet qu’elle vous permet de fabriquer, avec sa durée de recherche sous le nom (l’horloge) et, si elle exige de la Dark Matter, l’insigne de la Dark Matter. Une flèche va d’une technologie à celle qui en a besoin, que vous recherchez d’abord ; une case sans flèche peut être recherchée tout de suite. Pointez une case pour voir la durée de recherche, la science qu’elle brûle et ce que l’Assemblage demande ensuite pour l’objet, et cliquez dessus pour ouvrir la page de l’objet. Les arbres sont dessinés à partir des données mêmes du jeu.

<!-- research-tree:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

### Propulsion et vitesse {#tree-propulsion}

```tree research
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines

Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```

### Boucliers et défense {#tree-shields}

```tree research
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cores

Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```

### Lasers et munitions {#tree-lasers}

```tree research
Quantum Laser 3 | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-3 | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser 3, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-3, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Nova Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Pulse Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Apex Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Prism Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-

Quantum Laser 3 => Starfire-3 => Helios Beam
```

### Boosters {#tree-boosters}

```tree research
Damage Amp II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
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
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 20 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 8 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu

Extra Slots CPU I => Extra Slots CPU II => Extra Slots CPU III
Base CPU I => Base CPU II => Jump CPU
```


<!-- research-tree:end -->

## Toutes les technologies {#all-the-technologies}

<!-- research-technologies:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Technologie | Exige d’abord | Classe | Durée de recherche | Science | Dark Matter |
| :--- | :--- | :--- | ---: | ---: | ---: |
| [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 min | 1 800 | – |
| [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 h | 10 800 | – |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 h | 36 000 | 10 |
| [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 min | 1 800 | – |
| [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 h | 10 800 | – |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 h | 36 000 | 10 |
| [Engine III](/wiki/06-Items/Propulsion.md#engines) | – | B | 3 h | 10 800 | – |
| [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 min | 1 800 | – |
| [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 h | 10 800 | – |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | C | 10 h | 36 000 | 10 |
| [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 min | 1 800 | – |
| [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 h | 10 800 | – |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | C | 10 h | 36 000 | 10 |
| [Heavy Shield Core](/wiki/06-Items/Shields.md#shield-cores) | – | B | 3 h | 10 800 | – |
| [Quantum Laser 3](/wiki/06-Items/Lasers.md#lasers) | – | B | 3 h | 10 800 | – |
| [Starfire-3](/wiki/06-Items/Lasers.md#lasers) | [Quantum Laser 3](/wiki/06-Items/Lasers.md#lasers) | D | 1 j | 86 400 | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | [Starfire-3](/wiki/06-Items/Lasers.md#lasers) | D | 1 j | 86 400 | 10 |
| [Nova Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | C | 10 h | 36 000 | 10 |
| [Apex Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | C | 10 h | 36 000 | 10 |
| [Damage Amp II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 h | 10 800 | – |
| [Shield Wall II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 h | 10 800 | – |
| [Hull Plating II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 h | 10 800 | – |
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
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | D | 1 j | 86 400 | 10 |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | – | B | 3 h | 10 800 | – |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | C | 10 h | 36 000 | – |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | D | 1 j | 86 400 | 10 |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | – | B | 6 h | 21 600 | – |

Les classes, par durée de recherche :

| Classe | Durée de recherche | Technologies | L’une après l’autre | Science | Dark Matter |
| :--- | :--- | ---: | ---: | ---: | ---: |
| A | 30 min | 5 | 2 h 30 min | 9 000 | 0 |
| B | 3 h à 6 h | 14 | 2 j | 172 800 | 0 |
| C | 10 h | 9 | 3 j 18 h | 324 000 | 60 |
| D | 1 j à 2 j | 9 | 10 j | 864 000 | 90 |
| Toutes |  | 37 | 15 j 20 h 30 min | 1 369 800 | 150 |

Recherché une technologie après l’autre, l’arbre entier prend 15 j 20 h 30 min. Avec le boost actif en permanence, il prend 7 j 22 h 15 min, soit 8 boosts et 40 000 Thulium ; la science est la même.

<!-- research-technologies:end -->

## Les CPU {#the-cpus}

Les nouveaux CPU se recherchent aussi ici, puis se fabriquent à l’Assemblage. Le même tableau et les mêmes notes figurent sur la page [Extras](/wiki/06-Items/Extras.md#research-cpus).

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | Durée de recherche | Exige d’abord | Thulium pour fabriquer | Durée de fabrication |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 min | – | 12 000 | 5 min |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10 h | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 000 | 10 min |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1 j | [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75 000 | 15 min |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3 h | – | 8 000 | 5 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10 h | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 20 000 | 10 min |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1 j | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40 000 | 15 min |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6 h | – | 15 000 | 10 min |

Aucun n’est vendu à la boutique : recherchez la technologie, puis fabriquez le CPU à l’Assemblage. Pointez un CPU dans son arbre pour voir ce que l’Assemblage demande pour le fabriquer.

### Extra Slots CPUs {#extra-slots-cpus}

- **Ce qu’ils font.** Les Extra Slots CPU I, II et III donnent à chaque vaisseau 3, 5 et 7 emplacements extras de plus, soit 6, 8 et 10 au total avec les 3 que possède chaque vaisseau. Un CPU supérieur remplace le précédent : le II ne s’ajoute pas au I.
- **Installé, pas transporté.** Un Extra Slots CPU n’est pas un objet : quand vous le récupérez à l’Assemblage, il s’installe dans votre Skylab, pour chaque vaisseau dans les deux configurations, et ne prend aucun emplacement. Il reste après la réinitialisation.
- **Dans l’ordre.** Fabriquez-les l’un après l’autre : le II seulement quand le I est installé, le III seulement quand le II est installé ; d’ici là, l’Assemblage vous dit lequel installer d’abord. Les trois coûtent 117 000 Thulium en tout : 12 000, 30 000 et 75 000.

### Jump CPU {#jump-cpu}

- **Ce qu’il fait.** Il fait sauter votre vaisseau vers n’importe quel secteur de corporation de votre monde, celui de votre propre corporation comme ceux des autres, secteurs d’origine compris (`M`, `T` et `G`, secteurs 1 à 4), pour **500 Thulium** le saut. Il n’a pas de limite d’utilisations : vous ne payez que le Thulium. Il ne mène jamais à un secteur dangereux (`DS`) ni à un secteur neutre (`N`).
- **Le saut.** Appuyez sur l’emplacement JMP, choisissez le secteur sur la carte du Système stellaire et confirmez : le vaisseau se charge pendant 5 secondes, puis arrive à une porte de ce secteur, protégé comme après n’importe quel saut de porte. Le CPU refroidit pendant 30 secondes après votre arrivée.
- **Pas en combat.** Il ne peut pas démarrer dans les 10 secondes qui suivent un tir ou un coup reçu, et un tir ou un coup pendant la charge annule le saut ; rien n’est alors payé. Vous ne pouvez pas sauter occulté.
- **Pas depuis un secteur neutre :** un pilote dans un secteur neutre, ou sans corporation, ne peut pas l’utiliser.
- Il peut quitter un secteur dangereux quand vous n’êtes pas en combat.

### Base CPUs {#base-cpus}

- **Ce qu’ils font.** Ils téléportent votre vaisseau à la base de votre corporation, dans la zone sûre autour de sa station (`M-1`, `T-1` ou `G-1`, le secteur de Mission Control), sans coût en Thulium. Vous les lancez depuis l’emplacement BSE de la barre rapide.
- **Pas en combat.** Une charge de 10 secondes, la même pour les deux. Elle ne peut pas démarrer dans les 10 secondes qui suivent un tir ou un coup reçu, ni occulté, ni quand vous êtes déjà dans la zone sûre de votre base, et un tir ou un coup pendant la charge l’annule.

| CPU | Utilisations | Recharge |
| :--- | ---: | ---: |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 10 | 10 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 25 | 5 min |

- **Épuisé, pas rechargé.** Chaque utilisation consomme l’une des utilisations du CPU, et un CPU qui n’en a plus disparaît : fabriquez-en un nouveau. Si les deux sont installés, le meilleur (II) est utilisé en premier.

### Auto-Repair CPU {#auto-repair-cpu}

- **Ce qu’il fait.** Il envoie tout seul le Repair Drone installé dans vos emplacements extras, chaque fois que vous auriez pu l’envoyer à la main : votre coque n’est pas pleine, le drone n’est pas déjà sorti et 10 secondes se sont écoulées depuis le dernier coup reçu. Il n’y a aucun seuil de coque à régler.
- Il occupe un emplacement extra à lui et ne fait rien sans un Repair Drone dans un emplacement extra de la même configuration. Il n’envoie jamais un Repair Drone placé dans un emplacement de compétence (c’est le bouton Emergency Repair).
- **Si vous arrêtez le drone à la main,** le CPU le laisse tranquille jusqu’à ce que votre coque soit de nouveau pleine, ou jusqu’à ce que vous l’envoyiez vous-même.


<!-- research-cpus:end -->
