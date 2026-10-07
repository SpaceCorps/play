<!-- wiki-i18n source: 240bad7b031a48fe -->
<!-- wiki-i18n title: Trou noir -->
# Le trou noir {#the-black-hole}

<!-- wiki-search: black hole -->

Au centre exact du Secteur dangereux 4 (`DS-4`, le cœur de la zone PvP), un trou noir est suspendu dans l’obscurité. Il est le même dans chaque monde (Alpha, Beta et Gamma), chaque jour de la saison, Protocole de paix compris. Il prend tout ce qui s’approche trop près, et ne rend qu’une chose : de la [Dark Matter](#dark-matter), contre une roquette N.I.K.E. tirée dedans. Le chemin complet, de la recherche à la plate, est dans [Dark Matter et Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md).

![A Wraith approaches the black hole from 3,500 units: the radiation and pull rings lie around it like a gravity well](../../img/wiki-img/shots/black-hole-approach.jpg)
![Looking down on the black hole from 1,300 units: the shadow, the photon ring and the spiral of the accretion disk, with the starfield bent around it](../../img/wiki-img/shots/black-hole-closeup.jpg)

## Les anneaux {#the-rings}

Les distances se mesurent depuis le centre du secteur, en unités de carte. Le secteur mesure 32 000 sur 18 000 unités.

| Anneau | Distance | Ce qui se passe |
| :--- | ---: | :--- |
| **Radiation** | 4 000 | Votre vaisseau subit des dégâts chaque seconde, une part de ses PV maximum totaux. Plus vous êtes près, plus ils sont élevés. |
| **Attraction** | 3 000 | Le trou noir attire votre vaisseau vers le centre, d’autant plus fort que vous êtes près. Un vaisseau qui ne vole pas est emporté. |
| **Point de non-retour** | environ 1 000 à 2 600 | Là où l’attraction égale la vitesse de votre vaisseau. En deçà, même à pleine puissance, vous êtes aspiré. Il dépend de votre vitesse. |
| **Horizon des événements** | 300 | Tout vaisseau qui l’atteint est détruit sur-le-champ, quels que soient sa coque et son bouclier. |

Les portails du Secteur dangereux 4 et les couloirs qui les relient passent tous bien à l’écart de la radiation : vous ne la croisez donc jamais par accident en traversant le secteur.

## Radiation

Les dégâts sont un **pourcentage des PV maximum totaux de votre vaisseau** (coque plus bouclier) chaque seconde : à une distance donnée, toutes les classes de vaisseau tiennent donc exactement aussi longtemps. Un Protos et un Wraith à 2 000 unités consument tous deux un vaisseau plein en 50 secondes.

| Distance | Dégâts par seconde | Un vaisseau plein tient |
| ---: | ---: | ---: |
| 4 000 | 0,3 % | 333 s |
| 3 500 | 0,55 % | 182 s |
| 3 000 | 0,8 % | 125 s |
| 2 000 | 2 % | 50 s |
| 1 200 | 5 % | 20 s |
| 700 | 11 % | 9 s |
| 300 | 24 % | 4 s |

Entre deux lignes, les dégâts augmentent de façon linéaire. En points de vie par seconde, pour les vaisseaux en équipement de série :

| Vaisseau | PV max totaux | À 3 500 | À 3 000 | À 2 000 | À 1 200 | À 700 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Protos | 30 000 | 165 | 240 | 600 | 1 500 | 3 300 |
| Kitefin | 46 000 | 253 | 368 | 920 | 2 300 | 5 060 |
| Ostirion | 82 500 | 454 | 660 | 1 650 | 4 125 | 9 075 |
| Nomad | 130 500 | 718 | 1 044 | 2 610 | 6 525 | 14 355 |
| Paragon | 162 500 | 894 | 1 300 | 3 250 | 8 125 | 17 875 |
| Storm | 198 000 | 1 089 | 1 584 | 3 960 | 9 900 | 21 780 |
| Wraith | 372 000 | 2 046 | 2 976 | 7 440 | 18 600 | 40 920 |
| Ironclad | 673 200 | 3 703 | 5 386 | 13 464 | 33 660 | 74 052 |

- Le **bouclier encaisse en premier**, puis la coque. Ce n’est pas un coup : l’absorption du bouclier n’entre pas en jeu, et on ne peut pas l’esquiver.
- La radiation compte comme des **dégâts subis** : votre bouclier ne se recharge pas, un Repair Drone s’arrête (« Réparations interrompues : radiation. ») et ne peut pas être lancé, et une zone sûre ne vous protégerait qu’une fois 5 secondes écoulées depuis la dernière dose.
- Les boosters et les améliorations changent la taille de votre total, pas le temps que vous tenez : les dégâts en sont une part.
- Rien ne rend un vaisseau immunisé. La radiation n’est pas un coup, donc rien ne l’absorbe ; mais les compétences continuent d’agir dedans : un Shield Surge continue de restaurer votre bouclier et un Emergency Repair de réparer votre coque pendant leurs dix secondes (ce ne sont pas les réparations naturelles que la dose interrompt). L’occultation ne cache pas le vaisseau à la radiation.

## L’attraction {#the-pull}

En deçà de 3 000 unités, le trou noir attire chaque vaisseau vers le centre, et l’attraction ne fait que croître à mesure que vous approchez. Elle commence en douceur à la limite et se fait déjà sentir 200 unités plus loin :

| Distance | Attraction (unités par seconde) | Un vaisseau qui ne vole pas est emporté |
| ---: | ---: | :--- |
| 3 000 | 0 | pas encore |
| 2 800 | 25 | de 25 unités en une seconde |
| 2 300 | 60 | de 60 unités en une seconde |
| 1 800 | 120 | de 120 unités en une seconde |
| 1 300 | 220 | de 220 unités en une seconde |
| 1 000 | 262 | de 262 unités en une seconde, et ça augmente |
| 900 | 289 | de 289 unités en une seconde, et ça augmente vite |
| 700 | 496 | jusqu’à l’horizon en une seconde environ |
| 300 | 2 829 | l’horizon des événements |

De 3 000 à 925 unités, l’attraction augmente de façon linéaire entre deux lignes ; en deçà de 925, elle suit une courbe plus raide (les trois dernières lignes sont dessus). C’est un courant : il déplace votre vaisseau, et vos moteurs luttent contre lui.

- **Un vaisseau qui ne vole pas ne peut pas rester immobile.** Si vous vous arrêtez (vous atteignez l’endroit où vous avez cliqué, ou vous n’avez jamais donné d’ordre), le trou noir emporte votre vaisseau vers le centre, et votre ordre avec lui : votre vaisseau continue donc de tomber, quelle que soit la vitesse dont ses moteurs seraient capables. Pour tenir une position, il faut continuer d’y voler : maintenez la souris dessus, et votre vaisseau tient là où sa vitesse dépasse l’attraction, en cédant un peu entre deux ordres. Deux vaisseaux qui s’arrêtent pour échanger des tirs dans l’attraction sont tous deux aspirés.
- **Un vaisseau qui vole subit un vent contraire.** En vous éloignant tout droit du centre, la vitesse de votre vaisseau est réduite de l’attraction là où vous êtes : à une vitesse de 155, vous avancez de 130 unités par seconde à 2 800, de 95 à 2 300 et de 35 à 1 800, et à 1 500 (une attraction de 180) vous n’avancez plus du tout.

Votre **point de non-retour** est la distance où l’attraction égale votre vitesse. Un vaisseau de vitesse 150 l’a à 1 650 unités ; plus vous êtes rapide, plus il se trouve profond :

| Vaisseau (équipement de série) | Vitesse | Point de non-retour |
| :--- | ---: | ---: |
| Ironclad | 99 | 1 974 |
| Protos | 165 | 1 577 |
| Kitefin | 184 | 1 480 |
| Ostirion | 208 | 1 362 |
| Nomad | 211 | 1 347 |
| Paragon | 222 | 1 287 |
| Wraith | 233 | 1 208 |
| Storm | 263 | 995 |

Un vaisseau plus rapide que 272 unités par seconde (un équipement de course, ou un Wraith de série avec un Afterburner actif) a son point de non-retour là où il a toujours été : à une vitesse de 300, il est à 885 ; à 432, il est à 747.

Misez sur la vitesse et vous pourrez repartir de plus profond ; chargez-vous de boucliers lourds et vous ne le pourrez pas (un Ironclad, le vaisseau le plus lent, avec un Heavy Shield Core dans chacun de ses 14 emplacements vole à 39,1, avec son point de non-retour à environ 2 600). Seule une pointe de vitesse ramène un vaisseau qui se trouve juste en deçà de son point de non-retour : un [Afterburner](/wiki/03-Mechanics/Abilities.md) actif compte, et repousse le point de non-retour plus profond tant qu’il dure (dix secondes avec un moteur, quinze avec deux, vingt avec trois ; l’Afterburner III fait passer celui d’un Protos de série de 1 577 à 989 et celui d’un Wraith de série de 1 208 à 801). Rien ne peut repartir d’en deçà d’environ 390 unités, pas même un vaisseau conçu pour la vitesse, avec chaque statistique de vitesse enchantée au maximum et la plus forte pointe de vitesse active (un Afterburner III enchanté jusqu’au plafond, x1,69) ; un vaisseau non enchanté conçu pour la vitesse (des Engine III avec un Impulse Thruster IV et deux Momentum Thruster IV, des Adaptive Core II avec deux Impulse Thruster IV), avec un Afterburner III, repart au mieux d’au-delà de 427.

La chute depuis le point de non-retour commence lentement : un vaisseau quelques unités en deçà, à pleine puissance, est aspiré en vingt secondes ou plus, puis de plus en plus vite. L’attraction n’est pas du vol : elle ne compte pour aucune distance parcourue.

## L’horizon des événements {#the-event-horizon}

Un vaisseau qui arrive à 300 unités du centre est détruit. Un vaisseau dont la coque s’épuise sous la radiation en chemin est détruit par la radiation. Dans les deux cas :

- C’est une destruction ordinaire : vous choisissez où revenir (voir [Destruction et réapparition](/wiki/01-General/Getting-Started.md)), avec au plus 10 000 de coque et un bouclier vide (voir cette page), et elle coûte ce que coûte toujours une destruction. « Sur place » ne vous remet jamais dans l’anneau : cette option vous déplace au point le plus proche hors de celui-ci (4 500 unités du centre) et vous le signale.
- **Ni épave, ni caisse, ni butin**, et aucun honneur perdu.
- Votre destruction est créditée comme une élimination PvP au **dernier pilote ennemi qui a touché votre vaisseau dans les 15 secondes précédant sa destruction** : un pilote d’une autre corporation (là et quand le PvP est permis), aussi petit qu’ait été le coup. Cela lui vaut une élimination dans ses statistiques et des points de classement PvP selon votre type de vaisseau, rien de plus. Un seul tir suffit, et si personne d’une autre corporation ne vous a touché pendant ces 15 secondes, personne ne gagne rien.
- Les membres de votre corporation qui ont touché votre vaisseau pendant ces 15 secondes perdent quand même l’honneur du tir allié, quelle que soit la cause de la destruction.
- Les aliens et les pilotes de corporation ne s’en approchent jamais. Si l’un d’eux finit quand même à l’intérieur, il disparaît sans butin, sans récompense et sans revendication.

## Ce que vous voyez et entendez {#what-you-see-and-hear}

La vue est petite (environ 1 900 sur 1 150 unités à l’écran au zoom par défaut, 4 400 sur 2 650 en dézoomant au maximum) : l’image du trou noir lui-même n’apparaît donc qu’à environ trois mille unités de lui (3 600 en dézoomant au maximum). De plus loin, rien à l’écran ne le signale (regardez la mini-carte ou la carte du Système stellaire, ci-dessous) ; l’alerte de l’interface est faite pour quand vous êtes proche :

- **De loin.** Si vous inclinez la caméra pour regarder à travers le plan, le trou noir est dessiné là où il se trouve à l’écran, depuis n’importe quel point du secteur, dès qu’il est dans le cadre : un disque noir cerclé d’un anneau dans une lueur d’accrétion, mis à l’échelle pour rester bien visible (environ 2 % de la hauteur de la vue depuis le coin le plus éloigné, qui est à environ 18 000 unités), et il devient sa propre image à mesure que vous approchez. Rien n’y bouge de soi-même. Quand le trou noir est hors de la vue, aucun marqueur ne le signale à l’écran.
- **Des anneaux sur le plan de vol.** Une bande violette s’illumine jusqu’à un bord net à la limite de la radiation (4 000 unités), et une bande ambre plus fine marque la limite de l’attraction (3 000). Dans l’attraction, une **ligne rouge** montre *votre propre* point de non-retour. Elle suit votre vitesse : elle se déplace quand votre vaisseau accélère ou ralentit.
- **La jauge**, au-dessus de la barre rapide, apparaît à mille unités de la limite et reste tant que vous brûlez. Elle montre la radiation en pourcentage des PV totaux de votre vaisseau par seconde, le temps que la radiation seule mettrait à consumer ce qui reste (« Mortel dans 31 s », en rouge sous dix), une barre de ces PV, l’attraction là où vous êtes face à votre vitesse, et la distance qui vous sépare encore de votre point de non-retour, ou une alerte clignotante une fois que vous l’avez dépassé. Survolez une ligne pour savoir ce qu’elle signifie ; le (i) ouvre une fiche.
- **Les bords de l’écran** luisent en violet, virent au rouge à mesure que la dose augmente, et pulsent une fois par seconde.
- **La mini-carte** dessine le trou noir avec ses anneaux en ellipses (la carte s’étire avec sa fenêtre), et son info-bulle indique les rayons. La carte stellaire marque le secteur d’un petit trou noir.
- **Un compteur de radiation** crépite plus vite à mesure que la dose monte, par-dessus le combat. Une alerte à deux tons retentit quand vous franchissez la limite et de nouveau à votre point de non-retour, et un grondement sourd se fait entendre à partir d’environ 6 500 unités, plus grave à mesure que vous approchez.
- **L’image :** à partir de la qualité graphique **Moyenne** (avec le post-traitement activé), le trou est dessiné en suivant la lumière autour de lui, rayon par rayon : une ombre noire cerclée d’un fin anneau de photons blanc, et le disque d’accrétion tel que sa lumière vous parviendrait. Avec la caméra haute, c’est un anneau brillant autour du noir ; inclinez la caméra vers le bas et la face lointaine du disque se courbe au-dessus du trou et sa face inférieure en dessous, la face proche passant devant. Le ciel derrière le trou se courbe aussi, avec modération : les étoiles, la nébuleuse, les planètes et les astéroïdes sont repoussés vers l’extérieur autour de l’ombre et leurs lignes s’incurvent autour d’elle. Les vaisseaux sont dessinés par-dessus le trou et ne sont plus noircis par lui : une coque entre vous et le trou reste devant. La qualité Moyenne suit la lumière sur moins de tours, dessine moins d’images du disque et omet l’éclaircissement du côté qui se tourne vers vous, que les qualités Élevée et Ultra ajoutent. La qualité graphique **Faible**, et une image sans post-traitement, gardent l’ancienne image : un disque noir à l’anneau brillant et un disque d’accrétion de trois couches tournant en sens contraires, sans courbure du ciel. Une carte graphique qui ne peut pas construire la nouvelle image revient elle aussi à l’ancienne image, avec la légère courbure des étoiles qu’elle avait. À toutes les qualités s’ajoutent des traînées de matière qui tombent en suivant l’attraction (elles tombent à la vitesse même de l’attraction : un vaisseau qui ne vole pas est emporté au même rythme qu’elles, et celui qui s’en éloigne contre l’attraction les voit défiler). Un vaisseau emporté par l’attraction n’a pas de flamme de moteur et ne laisse pas de sillage ; celui qui s’en éloigne contre elle brûle à pleine vitesse à travers le courant, et son sillage file vers le trou. Le tremblement de la caméra croît avec l’attraction, en parts de la vitesse de votre vaisseau, atteint son niveau réglé à votre point de non-retour et continue d’augmenter jusqu’à l’horizon. Un vaisseau que le trou consume projette des étincelles violettes ; celui qu’il avale est attiré vers le centre et étiré en un mince filet. Le ciel du secteur est celui, violet sombre et vert, de `DS-3`.
- **Les débris :** des rochers et des morceaux de coques détruites tournent autour du trou noir et y tombent en spirale, de la limite de son attraction jusqu’à l’horizon : lentement d’abord, puis de plus en plus vite, en tournoyant autour de lui et en culbutant d’autant plus vite qu’ils approchent. Ils luisent en orange dans la lumière du disque, sont étirés en aiguilles quand ils se disloquent, et disparaissent avant d’atteindre l’horizon. Quelques gros rochers se trouvent parmi eux, et certains dérivent au-dessus du plan de vol, si bien que les vaisseaux passent dessous. Ce n’est que du décor : rien ne les touche et ils ne touchent rien, et ils n’apparaissent qu’à environ quatre mille unités du trou noir, en s’estompant vers 6 500. La lumière du disque tombe aussi sur votre vaisseau quand il est proche.
- **Quand vous mourez**, l’écran qui s’affiche en donne la raison : « Englouti par le trou noir » ou « Consumé par la radiation », et le Journal de jeu en garde la ligne.

Des paramètres aident là où le trou est lourd ou fatigant pour les yeux : **Réduire les animations** arrête le disque et les traînées, fige les débris, et arrête la pulsation des bords de l’écran, et **Réduire les tremblements de l’écran** arrête le tremblement de la caméra près du trou ; la qualité graphique **Faible** garde l’ancienne image, sans la lentille à tracé de rayons, et dessine moins de traînées (40, contre 100 en Moyenne et 200 au-dessus) et moins de débris (30, contre 80 en Moyenne et 160 au-dessus), fait briller l’anneau plus fort pour compenser, et dessine la vue lointaine avec une lueur de moins. Une **qualité des particules** plus basse éclaircit les débris comme elle éclaircit les rochers en arrière-plan.

## Rester à l’écart {#staying-out}

- Le serveur vous guide : un ordre de déplacement qui ferait traverser à votre vaisseau l’anneau de radiation (4 200 unités du centre, un peu plus large que la radiation elle-même) est exécuté en le **contournant**, le long de son bord. Les ordres qui se terminent dans l’anneau sont exécutés tels quels : y entrer est votre choix. Les trajets à travers le secteur sont jusqu’à un cinquième plus longs, les couloirs entre les portails pas du tout.
- L’onglet **Système** du chat vous avertit quand vous franchissez la limite de la radiation, celle de l’attraction et votre propre point de non-retour, et de nouveau quand vous en êtes sorti. Ces lignes ne sont ni dans **Global** ni dans **Local**.
- Si vous quittez le jeu dans la radiation, hors de l’attraction, vous revenez sur le bord extérieur de l’anneau, à l’arrêt, avec la coque que vous aviez. Si vous le quittez **dans l’attraction** (3 000 unités), vous revenez exactement là où vous l’avez quitté, avec la coque que vous aviez, et la chute continue : se déconnecter ne permet pas de sortir du trou noir.
- Une version plus ancienne du jeu n’affiche pas le trou noir. Elle reçoit quand même les avertissements et le guidage, et peut toujours entrer dans l’anneau sur ordre.

Les drones volent avec leur vaisseau. Aucune cargaison n’est jamais déposée dans l’anneau : une caisse qui y tomberait est placée sur son bord. Les caisses de Dark Matter sont la seule exception.

## Récolter la Dark Matter {#dark-matter}

Nouveau avec la Dark Matter ? [Dark Matter et Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md) donne le chemin complet, de la recherche à la plate. Cette section est le côté du trou noir.

Le trou rend de la **Dark Matter** pour chaque roquette **N.I.K.E.** qui l’atteint. Une N.I.K.E. est une roquette de 67 500 à 75 000 dégâts qui frappe le premier vaisseau qu’elle peut blesser et s’y épuise ; si rien n’est sur son chemin, elle vole jusqu’au trou et se consume en franchissant l’horizon des événements. L’[Assemblage](/wiki/06-Items/Rockets.md) fabrique les N.I.K.E. une fois leur technologie recherchée ([Recherche](/wiki/03-Mechanics/Research.md)), cinq par fabrication (100 000 crédits, 1 500 Thulium, 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite).

- **Le tir.** Une N.I.K.E. parcourt 4 050 unités en 4,5 secondes (900 par seconde), tout droit vers l’endroit visé : sans cible sélectionnée, placez le curseur sur le trou noir (ou pointez votre vaisseau vers lui). Elle atteint l’horizon depuis n’importe quel point entre la limite de la radiation (4 000 unités) et 4 380 unités du centre. Plus loin, elle tombe trop court et est perdue. Comme toute roquette, elle utilise le minuteur commun de 5 secondes (aucun laser n’a besoin d’être installé) ; la tirer met fin à votre protection de zone sûre et à votre occultation. **Un vaisseau sur la trajectoire la prend à la place** : un rival qui attend à la limite, ou un pilote d’une autre corporation qui ramasse des caisses sur le chemin, encaisse 67 500 à 75 000 dégâts et le trou n’a rien. Les aliens et les pilotes de corporation n’entrent jamais dans l’anneau : une trajectoire dégagée, c’est donc à vous de la garder dégagée ; la roquette traverse votre propre corporation et les vaisseaux qui sont à l’abri de vos tirs. Si vous quittez la carte après le tir, elle continue sans blesser personne et produit quand même votre Dark Matter. Une formation de drones peut changer ce délai et les dégâts du coup (voir [Formations de drones et roquettes](/wiki/06-Items/Rockets.md#drone-formations-and-rockets)).
- **Ce qui revient.** Chaque N.I.K.E. qui atteint l’horizon donne **1, 2 ou 3 Dark Matter** (2 en moyenne : cinq N.I.K.E. en font donc environ dix), dans une ou deux petites caisses qui apparaissent sur le bord de la zone du trou, **entre 3 050 et 3 950 unités du centre**, près de la ligne par laquelle votre tir est arrivé. L’attraction s’arrête à 3 000 : les caisses et les vaisseaux qui les ramassent ne sont donc pas attirés, et la radiation y est de 0,3 à 0,8 % des PV d’un vaisseau par seconde : une minute au milieu de la bande coûte un tiers de votre vaisseau. Un vaisseau plein y tient trois minutes.
- **À qui.** Les caisses sont à vous, et à votre clan, pendant **60 secondes** à partir du tir. Ensuite, n’importe qui sur la carte peut les prendre, et elles dérivent au loin au bout de **4 minutes**. Le Secteur dangereux est un secteur PvP : attendez-vous à de la compagnie. Un pilote qui se déconnecte après avoir tiré garde ses caisses.
- **Combien.** Une carte contient au plus 32 caisses de Dark Matter ; une nouvelle chasse la plus ancienne d’entre elles, et jamais une caisse d’un autre type. Le [Resource Magnet Booster](/wiki/03-Mechanics/Cargo.md) n’ajoute rien à la Dark Matter.
- **Ce que vous voyez.** Quand une N.I.K.E. franchit l’horizon, elle est étirée dans le trou, l’espace ondule à partir de son point d’entrée, et le disque et l’anneau de photons s’embrasent pendant environ une seconde et demie (un tiers de ce temps, deux fois moins lumineux, avec **Réduire les animations**). Un instant plus tard, les caisses sortent du trou et dérivent jusqu’à leur place sur le bord : chacune est un orbe violet-noir au bord brillant, parsemé d’étincelles, facile à voir de loin, et intitulé **Dark Matter** quand vous le survolez. Les vôtres affichent au-dessus d’elles les secondes qui vous restent, et apparaissent sur la mini-carte sous la forme d’une petite marque violette, comme pour votre clan ; les caisses des autres pilotes n’apparaissent sur la mini-carte qu’une fois leur minute écoulée.
- **À quoi elle sert.** L’Assemblage presse 5 Dark Matter avec une Velkonite Reinforced Plate et une Orvium Reinforced Plate en une **Dark Matter Plate**, et [la Forge](/wiki/06-Items/Forge.md) en demande deux pour faire passer un objet de Divin à Fracturant, puis de nouveau de Fracturant à Éternel : dix Dark Matter par étape. Le dernier palier de chaque chaîne d’amélioration demande 3 plates, soit 15 Dark Matter par pièce : les amps, cellules de bouclier et propulseurs du palier IV, le Heavy Shield Core, l’Engine III, le Helios Beam, l’Extra Slots CPU III et le Base CPU II. Le [Centre de recherche](/wiki/03-Mechanics/Research.md#dark-matter) du Skylab exige lui aussi de la Dark Matter : 10 pour chacune des 16 technologies du haut de son arbre, 160 en tout, ajoutées au Centre avant le début de la recherche. Les formations de drones en demandent aussi, 5, 13 ou 20 selon leur puissance : 189 de plus, 349 en tout. Un Helios Beam avec ses trois amps du palier IV contient 60 Dark Matter, et un Wraith qui ne porte que des pièces du dernier palier, 900 ([Dark Matter et Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md#what-the-last-tier-asks-for)).
