<!-- wiki-i18n source: f725fcc3af1d7832 -->
<!-- wiki-i18n title: Extras -->
# Extras

Les extras sont les gadgets installés dans les **emplacements extras** d’un vaisseau (deux sur le Protos, le Kitefin, l’Ostirion et le Nomad, les vaisseaux avec lesquels vous commencez ou que vous achetez, et trois sur le Paragon, l’Ironclad, le Wraith et le Storm, les vaisseaux que vous fabriquez, par configuration, et 3, 5 ou 7 de plus avec les Extra Slots CPU). Vous en activez un depuis le sélecteur d’extras de la barre rapide, ou depuis un emplacement de la barre rapide où vous l’avez placé. Ils ne fonctionnent que dans la configuration que vous pilotez : installé dans l’autre configuration, un extra attend que vous changiez de configuration.

| Extra | Effet | Utilisations | Prix |
| :---- | :----------- | :--- | :---- |
| **Repair Drone I à IV** | Répare votre coque de 1,5 %, 2,25 %, 3,5 % et 5 % du maximum par seconde | illimitées | 5 000 / 15 000 / 35 000 crédits, 2 000 Thulium |
| **Cloaking CPU S** | Cache votre vaisseau | 10 | 5 000 Thulium |
| **Cloaking CPU M** | Cache votre vaisseau | 25 | 11 250 Thulium |
| **Cloaking CPU L** | Cache votre vaisseau | 50 | 20 000 Thulium |
| **P.E.T. Station I à III** | Sur ON, elle laisse 2, 3 ou 5 [P.E.T.s](/wiki/03-Mechanics/Pets.md#the-station) arrimés apporter des boosts à votre vaisseau, gagner de l’expérience et travailler ; sur OFF, ils ne font rien de tout cela | ON / OFF | Assemblage, après sa recherche (l’arbre des objets ci-dessous) |
| **Auto-Rocket CPU** | Sur ON, elle tire toute seule votre roquette active sur la cible d’un combat | ON / OFF | Assemblage, après sa recherche (l’arbre des objets ci-dessous) |

Les Cloaking CPU ne se vendent qu’à la boutique. Ils ne peuvent pas être fusionnés, et aucune récompense ni aucun butin ne les donne. L’**EMP Charge** n’est plus un extra : depuis la 0.4.21, c’est un consommable, porté en pile comme une roquette et monté dans aucun emplacement, donc elle n’occupe aucun de vos emplacements extras (voir [Roquettes](/wiki/06-Items/Rockets.md#emp-charge)). Les deux **Energetic Wall** ne sont plus des extras non plus : depuis la 0.4.22, ce sont aussi des consommables, portés en pile et montés dans aucun emplacement (voir [Energetic Wall](#energetic-wall)).

Le **kit de départ** d’un nouveau pilote installe déjà deux extras dans les deux emplacements extras du Protos : un **Base CPU I** (10 utilisations, une téléportation vers la base de votre corporation) et un **Repair Drone I**. Faites-les glisser depuis le sélecteur d’extras de la barre rapide vers un emplacement pour les utiliser. Seuls les nouveaux pilotes reçoivent le kit : un pilote engagé avant la 0.4.10 ne l’a pas.

Huit autres CPU ne sont pas vendus : l’Assemblage les fabrique une fois que le Centre de recherche du Skylab les a recherchés (voir [Recherche](/wiki/03-Mechanics/Research.md)). Ce sont les Extra Slots CPU I, II et III, le Jump CPU, les Base CPU I et II, l’Auto-Repair CPU et l’Auto-Rocket CPU, et [la dernière section](#research-cpus) dit ce que fait chacun. Comme le Cloaking CPU, le Jump CPU et les Base CPU sont faits pour un moment calme : aucun des trois ne démarre dans les 10 secondes qui suivent un tir de votre part ou un coup reçu. Les deux CPU warp, le Jump CPU et les Base CPU, sont aussi refusés tant que vous transportez un objet de mission (« Vous ne pouvez pas utiliser de CPU warp en transportant un objet de mission. ») : voir [Objets de mission](/wiki/03-Mechanics/Quests.md#quest-items).

Chaque extra porte une étiquette courte sur son emplacement de la barre rapide : **REP** pour un Repair Drone, **CLK** pour un Cloaking CPU et **ARP**, **ARL**, **BSE** et **JMP** pour l’Auto-Repair CPU, l’Auto-Rocket CPU, les Base CPU et le Jump CPU. Les consommables ont les leurs : **EMP** et **WAL** (pour une Energetic Wall). Les trois objets **P.E.T. Station** sont des extras comme les autres, avec l’étiquette **PET** : équipez-en un, et son emplacement passe la Station sur **ON** ou **OFF** (une seconde entre deux appuis) et montre lequel. Sur ON, les [P.E.T.s](/wiki/03-Mechanics/Pets.md) arrimés comptent ; sur OFF, non. L’**Auto-Rocket CPU** se commute de la même façon, sur ON ou OFF. Pointez un emplacement pour lire ce que fait un appui en ce moment, ou pourquoi il n’en fait rien.

![The Extras picker of the hotbar: the Repair Drone, the Auto-Repair, Cloaking, Base and Jump CPUs and the P.E.T. Station you have fitted (REP, ARP, CLK, BSE, JMP, PET): click one to use it, or drag it onto a slot](../../img/wiki-img/shots/cpu-hotbar.jpg)
![The Consumables picker of the hotbar: the EMP Charge and the Energetic Wall I and II (EMP, WAL), with how many of each you hold: click one to use it, or drag it onto a slot](../../img/wiki-img/shots/emp-hotbar.jpg)
![The hotbar with extras on its slots: a Repair Drone, a Cloaking CPU with its uses left, the P.E.T. Station that says ON, the EMP Charge and the Energetic Wall I and II with the number of each you carry](../../img/wiki-img/shots/hotbar-slots.jpg)
![The Repair Drone of an extra slot docked to its ship and its wingmen](../../img/wiki-img/shots/repair-drones-extra.jpg)
![The Shop's Consumables category: the EMP Charge and the Energetic Wall I with their prices in Thulium, and the Energetic Wall II, which only Assembly makes](../../img/wiki-img/shots/shop-consumables.jpg)

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Arbre d’objets {#item-tree}

Ce que fabrique l’Assemblage exige d’abord sa technologie ; pointez un objet pour voir combien de temps sa recherche prend. L’arbre des technologies, le carburant et le boost : [Recherche](/wiki/03-Mechanics/Research.md).

```tree
P.E.T. Station I | extra, common | craft 100000 Credits, 2000 Thulium, 300 s | research 10800 s, 10800 science | 25 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md
Cloaking CPU S | extra, common | buy 5000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Repair Drone I | extra, common | buy 5000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone II | extra, common | buy 15000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone III | extra, common | buy 35000 Credits | /wiki/06-Items/Extras.md#repair-drones
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
P.E.T. Station II | extra, uncommon | craft 300000 Credits, 4000 Thulium, 600 s | research 36000 s, 36000 science | 1 P.E.T. Station I, 35 Ship Fragment, 6 Reinforced Hull Plate, 2 Power Core, 4 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md
Cloaking CPU M | extra, uncommon | buy 11250 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 2 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Extras.md#base-cpus
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu
P.E.T. Station III | extra, rare | craft 1100000 Credits, 12000 Thulium, 900 s | research 86400 s, 86400 science | 1 P.E.T. Station II, 60 Ship Fragment, 6 Reinforced Hull Plate, 4 Power Core, 2 Ancient Control Unit, 4 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md
Auto-Rocket CPU | extra, rare | craft 20000 Thulium, 900 s | research 36000 s, 36000 science | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 1 Ancient Control Unit, 8 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-rocket-cpu
Repair Drone IV | extra, rare | buy 2000 Thulium | /wiki/06-Items/Extras.md#repair-drones
Cloaking CPU L | extra, rare | buy 20000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 6 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu

P.E.T. Station I => P.E.T. Station II => P.E.T. Station III
Cloaking CPU S -> Cloaking CPU M -> Cloaking CPU L
Repair Drone I -> Repair Drone II -> Repair Drone III -> Repair Drone IV
Extra Slots CPU I -> Extra Slots CPU II -> Extra Slots CPU III
Base CPU I -> Base CPU II
```
<!-- item-tree:end -->

## Repair Drones

Activez un Repair Drone (REP) et il répare la coque jusqu’à ce qu’elle soit pleine. Il ne démarre qu’après 10 secondes sans coup reçu, et chaque coup reçu l’éteint. Si plusieurs sont installés, c’est le meilleur qui travaille. Un [Auto-Repair CPU](#auto-repair-cpu) le réactive à votre place. Les taux figurent dans [Combat](/wiki/03-Mechanics/Combat.md). Pendant qu’il répare, de petits drones de réparation sortent du vaisseau, tournent autour et arrosent la coque de faisceaux, un pour un Repair Drone I, deux pour un II, trois pour un III ou un IV, et les pilotes proches les voient ; ils retournent s’arrimer quand la réparation s’arrête.

## Cloaking CPU

Appuyez sur l’emplacement CLK pour vous occulter. **Un appui consomme une utilisation**, quel que soit le pack, et vous voyez les utilisations restantes sur l’emplacement et dans le hangar. Une occultation **n’a pas de limite de durée** : elle reste active jusqu’à ce que vous la coupiez ou que quelque chose la rompe.

- **Qui ne peut pas vous voir.** Les pilotes des autres corporations et les aliens ne voient pas du tout votre vaisseau : il n’est ni à leur écran ni dans leur liste de cibles, et personne ne peut le verrouiller. Les pilotes de corporation des autres corporations l’ignorent aussi.
- **Le point radar.** Tous les autres pilotes de la carte, à l’exception de votre corporation, voient sur la mini-carte un simple **point rouge** là où vous êtes, et savent ainsi que quelqu’un d’occulté rôde. Le point n’a ni nom, ni vaisseau, ni corporation, ni ID, et on ne peut ni cliquer dessus ni le cibler ; le survol indique seulement « Quelque chose est occulté ici ». Il est rond, à l’intérieur d’un anneau (les vaisseaux sont des carrés sur la mini-carte), et l’anneau respire lentement, ou reste immobile si vous avez activé Réduire les animations. Le serveur le rafraîchit environ deux fois par seconde et votre jeu le déplace en douceur entre-temps. Il indique que quelqu’un est là, et où, mais pas qui : un pilote qui vous a vu vous occulter peut suivre le point, et **l’explosion d’une roquette** visée dessus vous trouve quand même.
- **Qui peut vous voir.** Vous voyez votre propre vaisseau, estompé, avec un contour. Les pilotes de votre corporation vous voient comme un pâle fantôme ; les membres de votre clan issus d’autres corporations, non, car un clan accepte tous ceux qui postulent. Personne ne peut cibler le fantôme, pas même votre corporation.
- **Vous ne pouvez pas vous occulter** dans une zone sûre, pendant que le CPU se recharge, ni dans les **10 secondes** qui suivent un coup reçu ou un tir.
- **Ce qui la rompt.** Appuyer de nouveau sur l’emplacement, votre première salve ou roquette (elle touche, et vous êtes vu), l’entrée dans une zone sûre, le CPU qui quitte la configuration que vous pilotez, une **EMP déclenchée à moins de 1 500 unités** de vous, quel qu’en soit l’auteur (celle de votre propre corporation aussi, mais pas celle d’un membre de votre groupe), et l’explosion de zone d’une roquette qui vous touche. Le temps ne la rompt pas, la récupération d’une cargaison non plus (une caisse que vous prenez disparaît pour tout le monde, qui apprend ainsi que quelque chose se trouvait à portée de cet endroit, sans savoir qui), les compétences non plus, et la radiation du trou noir blesse un vaisseau occulté sans rompre son occultation. Se déconnecter ou mourir la rompt, car un vaisseau que personne ne pilote n’est pas occulté.
- **Recharge.** Quand une occultation prend fin, quelle qu’en soit la cause, le CPU se recharge pendant **60 secondes**. La recharge vous appartient, pas au vaisseau : elle se poursuit si vous sautez par un portail, vous déconnectez ou mourez. Chaque appui consomme toujours une utilisation.
- Les **aliens** qui vous poursuivaient vous perdent. Vos revendications d’éliminations sont levées quand vous vous occultez.
- **Roquettes.** Personne ne peut verrouiller une roquette guidée sur vous, et une roquette droite à cible unique vous traverse. Une **explosion de zone** blesse toujours un vaisseau qu’elle couvre et rompt son occultation, et l’endroit où se trouve le vaisseau est montré aux pilotes qui peuvent le voir avant que le nombre de dégâts n’apparaisse. Lancer une roquette est un tir : cela rompt votre propre occultation comme une salve (le CPU se recharge alors les 60 secondes indiquées plus haut) et, occulté ou non, vous empêche de vous occulter pendant les 10 secondes qui suivent.
- Le **trou noir** engloutit un vaisseau occulté comme n’importe quel autre, et toute la carte en est informée.
- **Ce que vous voyez.** Votre vaisseau devient translucide, avec un contour violet en pointillés, ses drones s’estompant avec lui, et une pastille en haut de l’écran indique « Occulté » avec les utilisations restantes (pas de secondes : il n’y a pas de minuterie). L’emplacement CLK affiche les utilisations restantes ; pendant que vous êtes occulté, il brille en violet et indique ON, et quand l’occultation prend fin, quelle qu’en soit la cause, il s’assombrit et décompte les 60 secondes de recharge. Un appui que le serveur refuse (recharge, zone sûre, coup reçu ou tir dans les 10 dernières secondes) fait clignoter l’emplacement en rouge, et un message vous en donne la raison. Un allié apparaît comme un pâle fantôme, avec une marque de fantôme devant son nom, et un pilote qui s’occulte près de vous disparaît dans une ondulation. Faites glisser CLK depuis les Extras de la barre rapide sur un emplacement pour l’utiliser, comme REP.
- Les **utilisations** sont enregistrées avec le CPU. Se déconnecter, mourir ou relancer le jeu n’en rend aucune, et une activation que vous annulez est tout de même dépensée. Quand la dernière utilisation d’un pack disparaît, il est épuisé et son emplacement est réapprovisionné à partir d’un exemplaire de rechange du même CPU de votre inventaire, si vous en possédez un.
- **Plusieurs CPU** dans une même configuration ne s’additionnent pas. Celui qui a le moins d’utilisations restantes est utilisé en premier.

Les S, M et L fonctionnent de la même façon : les packs plus gros ne sont que moins chers par utilisation (500, 450 et 400 Thulium).

## Energetic Wall

Appuyez sur l’emplacement WAL et une **paroi de plasma** se dresse **à votre curseur**, en travers de la ligne qui va de votre vaisseau jusqu’à lui : une bande de 360 unités de long (environ trois modèles de vaisseau et demi) et de 10 unités de large. Son milieu est à **450 unités** au plus du milieu du vaisseau : un curseur plus éloigné la met à 450 unités sur la ligne, un curseur à moins de 120 unités la repousse à 120. Tant que l’emplacement est prêt, une ligne pointillée discrète et un contour fantôme montrent où elle se dressera. Si le jeu ne sait pas où est votre curseur, elle se dresse à 220 unités devant le milieu du vaisseau, en travers de son cap. Une Energetic Wall est un **consommable**, comme l’[EMP Charge](/wiki/06-Items/Rockets.md#emp-charge) : une pile dans votre inventaire qui n’occupe **aucun emplacement** d’aucun vaisseau (jusqu’à la 0.4.22, c’était un extra). Glissez-la depuis les Consommables de la barre rapide sur un emplacement pour l’utiliser ; les deux niveaux sont deux entrées, un emplacement en tient donc un seul. Elle sert à se cacher derrière et à barrer un couloir, pas à s’y tenir.

- **Ce qu’elle arrête.** Tout tir qui la croise frappe la paroi à la place, quel que soit celui qui l’a tiré et de quel côté : une salve de laser, une roquette, la salve d’un alien. Ce qui se tient derrière ne subit rien et les points de vie de la paroi encaissent les dégâts. Le souffle d’une roquette qui explose sur la paroi touche les vaisseaux du côté proche et non ceux qui sont derrière. Vos propres tirs aussi : vous ne pouvez pas tirer à travers votre propre paroi. La N.I.K.E. et les tourelles du Dormant Swamp passent par-dessus, comme par-dessus les astéroïdes.
- **Ce qu’elle brûle.** Tout vaisseau dont la coque touche la bande subit **2 500 de dégâts par seconde**, bouclier d’abord, le vôtre aussi, ainsi que les aliens et les pilotes de corporation. Un vaisseau dans une zone sûre ou sous la protection d’une réapparition ne brûle pas, et deux bandes sur un même vaisseau ne s’additionnent pas.
- **Combien de temps elle tient.** Une paroi de niveau 1 a **30 000 points de vie**, une de niveau 2 **90 000**. Une paroi en perd d’elle-même un soixantième chaque seconde, si bien qu’une paroi sur laquelle personne ne tire disparaît après **60 secondes**. Les tirs raccourcissent ce délai : un Wraith avec douze Helios Beam en munitions x4 abat une paroi de niveau 1 en 3,5 secondes environ.
- **Une seule à la fois, une paroi par appui.** Une nouvelle paroi prend la place de l’ancienne. Après un appui, l’objet se recharge pendant **90 secondes** ; l’attente est la vôtre, pas celle du vaisseau : mourir ou se déconnecter ne la raccourcit pas. Un appui consomme **une paroi du niveau que tient son emplacement**, et seulement quand la paroi se dresse : un appui que le jeu refuse (voir plus bas) ne consomme rien et ne lance aucune attente. S’il n’en reste plus de ce niveau, il dit « Il ne vous reste aucune Energetic Wall. », et l’autre niveau n’est jamais consommé à sa place.
- **Où non.** Pas tant qu’une zone sûre ou une réapparition vous protège, pas là où la bande toucherait une zone sûre ou une porte, pas en étant occulté et pas là où le milieu de la bande tomberait hors de la carte. Le jeu dit de quel cas il s’agit.
- **Éliminations.** Un vaisseau que la paroi détruit meurt de radiation, et l’élimination revient au dernier pilote ennemi qui l’a touché dans les 15 secondes, s’il y en a eu un. Celui qui a posé la paroi n’est crédité de rien qu’il n’ait tiré lui-même. Un alien que la paroi détruit ne rapporte rien : ni récompense ni butin.
- **Les aliens ne la contournent pas.** Ils la traversent et brûlent, ou restent de leur côté et tirent sur la paroi.
- **Ce que vous voyez.** Une bande de lumière blanc-bleu avec des traits brillants qui courent le long d’elle et un poteau de lumière à chaque bout, qui s’embrase là où un tir porte et vacille quand elle est presque épuisée. Une paroi de niveau 2 brille en jaune à la place, avec un cœur plus épais et plus lumineux et une lueur plus forte, mais sa bande fait les mêmes 10 unités de large que celle du niveau 1. Une fine barre de vie à côté d’elle se raccourcit et passe à l’ambre puis au rouge ; votre emplacement montre la vie restante de votre paroi en arc et l’attente en ombre. Une paroi posée s’embrase, une paroi abattue s’effondre en étincelles, et une paroi dont le temps est écoulé s’efface. Sur votre emplacement, un nombre compte aussi les parois de son niveau qu’il vous reste.
- **Comment l’obtenir et la porter.** L’Energetic Wall I se vend à la boutique pour **250 Thulium** la paroi, et vous en portez jusqu’à **20** dans une même pile (ce que vous avez mis en vente aux [Enchères](/wiki/03-Mechanics/Auction.md) compte). L’Energetic Wall II se fabrique à l’Assemblage, **une paroi par fabrication**, pour **600 Thulium**, 5 Ship Fragments et un Power Core, une fois qu’elle a été recherchée au Centre de recherche (6 heures à vitesse normale : [Recherche](/wiki/03-Mechanics/Research.md)) ; vous en portez jusqu’à **10**. Contrairement aux douze roquettes, dont 1 000 de chaque sont conservées d’office, les parois que vous portez sont perdues avec la saison si vous ne les mettez pas dans la cache de transport, et celles de la cache ne peuvent pas servir. Une Energetic Wall II fabriquée par vous peut être vendue aux Enchères ; une Energetic Wall I, que la boutique vend, jamais.

## CPU du Centre de recherche {#research-cpus}

Deux des CPU demandent des Dark Matter Plates, comme le dernier palier de chaque chaîne d’amélioration : l’**Extra Slots CPU III** en demande 4 (avec en plus 2 Ancient Control Units et 6 Orvium Reinforced Plates) et le **Base CPU II** 4 (avec en plus une Ancient Control Unit et 2 Orvium Reinforced Plates) ; recherchez donc d’abord la Dark Matter Plate ([Dark Matter et Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)).

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
| [Energetic Wall II](/wiki/06-Items/Extras.md#energetic-wall) | 6 h | – | 600 | 2 min |
| [Auto-Rocket CPU](/wiki/06-Items/Extras.md#auto-rocket-cpu) | 10 h | – | 20 000 | 15 min |

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

### Auto-Rocket CPU

- **Ce qu’il fait.** Tant qu’il est sur ON et que vous êtes au combat (vos lasers visent un alien ou un pilote ennemi), il tire tout seul votre roquette active, la dernière que vous avez tirée, sur cette cible, chaque fois qu’un appui sur la touche Tirer roquette fonctionnerait : le minuteur des roquettes est prêt et il vous en reste une. Le serveur vérifie chaque tir comme il vérifie les vôtres.
- **L’interrupteur.** Équipez-le dans un emplacement Extras et appuyez sur son emplacement ARL pour le passer sur ON ou OFF. Il démarre sur OFF et reste comme vous l’avez laissé, y compris quand vous vous reconnectez. L’emplacement indique ON ou OFF et brille quand le CPU tire.
- **Ce qu’il ne fait jamais.** Il ne choisit jamais de cible, ne tire jamais sur des astéroïdes, ni depuis une zone sûre, ni sous occultation, et ne tire jamais une N.U.K.E. ni une N.I.K.E. Une roquette que vous tirez vous-même fonctionne toujours. Sans touche, clic ni mouvement de souris pendant 3 minutes, il attend que vous fassiez quelque chose.
- **Plus de roquettes.** Il vous le dit une fois et tire de nouveau dès que vous en avez.


<!-- research-cpus:end -->
