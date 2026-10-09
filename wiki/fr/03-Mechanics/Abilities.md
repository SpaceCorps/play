<!-- wiki-i18n source: 72b805cb24d9b8a4 -->
<!-- wiki-i18n title: Compétences -->
# Compétences actives du vaisseau {#active-ship-abilities}

Les compétences sont les boutons sur lesquels vous appuyez dans le feu de l’action : un bouclier qui revient, une pointe de vitesse pour sortir de portée, une réparation quand votre coque est presque à bout. Elles viennent du **bouclier, du moteur ou du Repair Drone** que vous installez dans les **emplacements de compétence** de votre vaisseau, et meilleur est l’objet, meilleure est la compétence. Elles sont faites pour le moment où vous en avez besoin, pas pour être déclenchées à chaque fin de recharge : chacune dure une dizaine de secondes, puis se repose entre une minute et demie et deux minutes. Quelques [designs de vaisseaux](/wiki/03-Mechanics/Ship-Designs.md) en ont une de plus, qui leur est propre : voir [Compétences de vaisseau](#ship-abilities).

Un nouveau pilote commence avec une compétence : le **Repair Drone I** du kit de départ est déjà installé dans l’emplacement de compétence du Protos, et le bouton Emergency Repair (`E`) est donc là dès la première minute. Un second Repair Drone I du kit est dans un emplacement extra : celui-là répare la coque lentement tout seul et n’est pas une compétence (voir [Extras](/wiki/06-Items/Extras.md#repair-drones)).

![The Afterburner](../../img/wiki-img/shots/afterburner.jpg)
![Emergency Repair: repair drones beam the hull](../../img/wiki-img/shots/emergency-repair.jpg)
![Shield Surge: a bubble of shield around the ship and its drones](../../img/wiki-img/shots/surge.jpg)

## Emplacements de compétence {#ability-slots}

Chaque vaisseau a un nombre fixe d’emplacements de compétence dans le hangar :

- **Protos** (de départ) : 1 emplacement
- **Kitefin** : 1 emplacement
- **Ostirion** : 2 emplacements
- **Nomad** : 2 emplacements
- **Paragon** : 3 emplacements
- **Storm** : 3 emplacements
- **Ironclad** : 3 emplacements
- **Wraith** : 3 emplacements

Un emplacement de compétence accepte un **bouclier**, un **moteur** ou un **Repair Drone**, et chacun donne sa propre compétence. Faites glisser l’objet sur l’emplacement. La configuration 1 et la configuration 2 ont chacune leurs propres emplacements.

- **Les cellules de bouclier et les propulseurs ne vont pas dans un emplacement de compétence.** Ce sont des modules des boucliers, des moteurs et des cœurs adaptatifs.
- **Un objet dans un emplacement de compétence n’apporte rien d’autre.** Il ne donne ni capacité de bouclier, ni recharge, ni absorption, ni vitesse, et aucun des ralentissements d’un bouclier. Un même Heavy Shield Core est soit dans un emplacement de générateur pour son bouclier à chaque instant, soit dans un emplacement de compétence pour son Surge. À vous de choisir.
- Un bouclier ou un moteur qui contient des cellules ou des propulseurs les renvoie dans votre inventaire quand vous le faites glisser sur un emplacement de compétence.
- Un Repair Drone dans un emplacement de compétence donne l’Emergency Repair et ne répare pas la coque de lui-même. Le drone lent (**REP**) nécessite un Repair Drone dans un emplacement extra.

## Plusieurs modules du même type {#several-modules-of-one-kind}

Vous pouvez installer **plusieurs boucliers, moteurs ou Repair Drones** dans les emplacements de compétence d’une même configuration. Ils restent une seule compétence, un seul bouton et un seul temps de recharge, mais une compétence plus forte :

- **Le module de plus bas rang fixe la base.** Son rang donne la puissance et le temps de recharge. Un Heavy Shield Core à côté d’un Light Shield Core se comporte comme deux modules de rang I : un second module meilleur apporte le bonus, jamais une meilleure puissance ni un temps de recharge plus court.
- **Chaque autre module ajoute 50 % de la base**, en s’additionnant, pas en se multipliant. Les moteurs font **durer plus longtemps** l’Afterburner : 10 s, 15 s avec deux moteurs, 20 s avec trois (le bonus de vitesse et le temps de recharge ne changent pas). Avec plusieurs boucliers, le Shield Surge **restaure davantage**, et avec plusieurs Repair Drones, l’Emergency Repair **répare davantage**, dans les mêmes dix secondes : 100 %, 150 % et 200 % du total pour un, deux et trois modules.
- **Les modules supplémentaires coûtent des emplacements.** Un vaisseau à trois emplacements de compétence peut avoir trois modules du même type, ou un de chaque, ou deux et un. Un Protos ou un Kitefin n’a qu’un emplacement et ne peut pas cumuler ; un Ostirion ou un Nomad peut en avoir deux du même type.
- Des rangs égaux donnent simplement ce rang. De deux modules du même rang, celui dont l’enchantement est le plus faible fixe la base.

## Les trois compétences {#the-three-abilities}

### Shield Surge (boucliers), touche `Q` {#shield-surge-shields-key-q}

Pendant dix secondes, le bouclier de votre vaisseau est **réparé** : le Surge restaure une part de votre bouclier max de façon régulière, jusqu’au maximum et jamais au-delà. Ce n’est pas une barrière et il ne change pas la répartition des coups ; il remet du bouclier, et ce qu’il a remis reste. Il ne s’arrête pas quand vous êtes touché (la recharge ordinaire attend 15 secondes après un coup ; le Surge, non). Un vaisseau au bouclier plein en tire peu : déclenchez-le quand le bouclier faiblit. Le total n’est jamais inférieur à la capacité propre du Shield Core : un vaisseau avec peu de bouclier reçoit quand même une vraie réparation (jusqu’à son maximum).

- Refusé sous la protection d’une zone sûre, et sur un vaisseau sans aucun bouclier, pour qu’un clic malheureux ne le gaspille pas.
- Les roquettes perforantes contournent toujours en partie les boucliers, comme elles l’ont toujours fait.

### Afterburner (moteurs), touche `W` {#afterburner-engines-key-w}

Votre vitesse finale est multipliée par le bonus du rang pendant toute sa durée. Il ne change ni les virages, ni le ciblage, ni les dégâts subis : il transforme du temps en distance. Utilisez-le pour quitter un combat, pour atteindre l’anneau d’une station ou d’un portail, ou pour rattraper une cible qui fuit. Il fonctionne partout, zones sûres comprises. Plus de moteurs le font durer plus longtemps, pas aller plus vite.

### Emergency Repair (Repair Drones), touche `E` {#emergency-repair-repair-drones-key-e}

Répare une part de votre **coque max de façon régulière sur dix secondes**, jamais au-delà du maximum. Les coups ne l’interrompent pas : c’est une compétence d’urgence, qui fonctionne sous le feu, dans la radiation du trou noir, sous occultation et pendant la fenêtre d’une EMP. L’Emergency Repair prend fin quand le temps est écoulé ou quand votre vaisseau est détruit. Il ne touche pas à votre bouclier, ne compte pas comme un coup, et laisse la réparation lente REP telle qu’elle était. Refusé à coque pleine.

## Compétences de vaisseau {#ship-abilities}

Huit des treize [designs de vaisseaux](/wiki/03-Mechanics/Ship-Designs.md) ont une compétence qui appartient au design, pas à un objet. Elle ne prend **aucun emplacement de compétence** et n’a besoin de rien d’installé : elle est là tant que vous pilotez le design. Elle a un bouton à elle, le quatrième de la colonne de la barre rapide, et sa touche est `F` (modifiable dans les paramètres). Elle a son propre temps de recharge, conservé comme les autres : changer de configuration, sauter et se déconnecter ne le remettent pas à zéro, et un vaisseau détruit commence le vol suivant avec toutes ses compétences prêtes.

| Compétence | Design | Ce qu’elle fait | Durée | Temps de recharge |
| :--- | :--- | :--- | ---: | ---: |
| **Blink** | Storm NOTSUM, Ironclad TITANIC | Vitesse 2 500 (TITANIC : 1 500) vers votre ordre de déplacement | 1 s | 120 s |
| **Chameleon** | Storm RECON | Invisible pour tous les autres pilotes, mini-carte comprise | jusqu’à ce qu’elle cède | 60 s |
| **Focus Fire** | Ironclad DUMA | Les vaisseaux ennemis à moins de 1 000 unités sont forcés de vous attaquer | 5 s | 60 s |
| **Venom** | Wraith RAPTOR | 100 000 de dégâts directement sur la coque d’une cible | 30 s | 120 s |
| **Diminisher** | Wraith BILLY | Vous subissez 75 % de dégâts en moins et en infligez 25 % de moins | 10 s | 120 s |
| **Heal Pod** | Wraith MENATI | Une capsule soigne les vaisseaux alliés à moins de 600 unités de 10 000 + 1 % de leur coque maximale par seconde | 5 s | 120 s |
| **Shield Buff** | Wraith ATARAXIS | Votre capacité de bouclier double et se régénère de 2 % de son maximum par seconde | 10 s | 120 s |

- **Blink.** Pendant 1 seconde, votre vitesse est de 2 500 (celle d’un TITANIC est plafonnée à 1 500), vers votre ordre de déplacement. Vous vous arrêtez là où l’ordre se termine, et le bord de la carte vous arrête aussi. Ensuite, elle se repose 120 secondes.
- **Chameleon.** Vous disparaissez : aucun autre pilote ne vous voit, ni sur la carte ni sur la mini-carte, et personne ne peut vous verrouiller. Votre propre corporation vous voit encore, comme un fantôme. Un EMP ne peut pas la briser. Elle prend fin quand vous subissez le moindre dégât, tirez une salve de laser, lancez une roquette, ramassez une caisse ou entrez dans une zone sûre, ou quand vous appuyez de nouveau sur le bouton ; ses 60 secondes commencent quand elle prend fin, quelle que soit la façon. Vous ne pouvez pas l’activer dans les 10 secondes qui suivent un tir ou un coup reçu, ni dans l’anneau d’une zone sûre, ni tant qu’un Cloaking CPU est actif.
- **Focus Fire.** Pendant 5 secondes, chaque pilote ennemi et chaque alien à moins de 1 000 unités est forcé de vous attaquer : le verrouillage d’un pilote est posé sur vous et ne peut pas être changé, un alien se tourne vers vous. Les pilotes de votre groupe et de votre corporation, les vaisseaux protégés par une zone sûre et les vaisseaux occultés sont laissés tranquilles, et elle est refusée dans une zone sûre ou sans ennemi à portée. Les pilotes forcés peuvent toujours voler où ils veulent.
- **Venom.** Verrouillez une cible à portée de vos lasers et appuyez : 100 000 de dégâts vont directement sur sa coque sur 30 secondes, de façon égale, et son bouclier n’en prend aucune part. Elle agit aussi bien sur les pilotes d’autres corporations que sur les aliens, pas sur votre groupe ni votre corporation, pas sur un vaisseau qu’une zone sûre protège, et pas là où un verrouillage au laser est refusé (le Protocole de paix, un secteur sans PvP). Un vaisseau ne porte qu’un Venom à la fois. Chaque tic compte comme un coup, la cible ne peut donc pas se cacher dans une zone sûre avant la fin. La réparation, un Heal Pod et un Diminisher sur la cible l’atténuent, elle prend fin quand la cible ou vous mourez, et l’élimination et ses points sont à vous.
- **Diminisher.** Pendant 10 secondes, chaque coup que vous recevez est réduit au quart avant que votre bouclier n’en prenne sa part, si bien que bouclier et coque perdent chacun un quart, et chaque coup que vous infligez est réduit aux trois quarts : lasers, roquettes directes et explosions. Un second appui ne fait rien tant qu’elle agit.
- **Heal Pod.** Une capsule tombe là où vous êtes et reste 5 secondes. Chaque seconde, elle soigne chaque vaisseau allié à moins de 600 unités de 10 000 plus 1 % de la coque maximale de ce vaisseau : vous, votre groupe et votre corporation, personne d’autre, et jamais au-delà du maximum. Rien ne peut verrouiller la capsule ni lui tirer dessus, et elle continue de soigner si vous mourez.
- **Shield Buff.** Pendant 10 secondes, votre capacité de bouclier est doublée, le bouclier que vous avez est doublé lui aussi, et le bouclier se régénère de 2 % du maximum doublé chaque seconde. Quand elle prend fin, la capacité revient à la normale et le bouclier avec elle, en gardant sa proportion : elle ne vous soigne donc jamais, c’est de la place pour encaisser. Elle est refusée sur un vaisseau sans bouclier.

Un **EMP** qui explose près de vous bloque le bouton pendant 5 secondes : un appui est refusé et aucun temps de recharge ne commence. Une compétence déjà en cours continue, et un Chameleon reste caché. Les autres pilotes voient aussi ces compétences : une traînée derrière un Blink, un anneau rouge et des lignes vers les vaisseaux qu’un Focus Fire force, un Chameleon seulement comme un fantôme pour sa propre corporation.

## Rangs {#ranks}

La puissance d’une compétence est une **part d’une valeur de votre propre vaisseau** (bouclier max, vitesse, coque max) : elle grandit donc avec le vaisseau. Le rang vient de l’objet : un meilleur modèle donne une meilleure compétence. Un objet enchanté ajoute son bonus d’enchantement à la puissance, 15 % au plus. Le tableau vaut pour un module ; le cumul est en dessous.

<!-- abilities:begin -->
<!-- Generated from server/Resources/AbilityConfig.json and the items' stats by scripts/abilities-wiki.sh: don't edit by hand. -->

| Compétence | Rang | Objet | Puissance (un module) | Durée | Temps de recharge | Actif |
| :--- | :---: | :--- | :--- | --: | --: | --: |
| **Shield Surge** | I | Light Shield Core | restaure 30 % de votre bouclier max | 10 s | 120 s | 8,3 % |
| **Shield Surge** | II | Basic Shield Core | restaure 60 % de votre bouclier max | 10 s | 105 s | 9,5 % |
| **Shield Surge** | III | Heavy Shield Core | restaure 100 % de votre bouclier max | 10 s | 90 s | 11,1 % |
| **Afterburner** | I | Engine I | +30 % de vitesse | 10 s | 120 s | 8,3 % |
| **Afterburner** | II | Engine II | +45 % de vitesse | 10 s | 105 s | 9,5 % |
| **Afterburner** | III | Engine III | +60 % de vitesse | 10 s | 90 s | 11,1 % |
| **Emergency Repair** | I | Repair Drone I | répare 20 % de votre coque max | 10 s | 120 s | 8,3 % |
| **Emergency Repair** | II | Repair Drone II | répare 25 % de votre coque max | 10 s | 105 s | 9,5 % |
| **Emergency Repair** | III | Repair Drone III | répare 32 % de votre coque max | 10 s | 90 s | 11,1 % |
| **Emergency Repair** | IV | Repair Drone IV | répare 40 % de votre coque max | 10 s | 75 s | 13,3 % |

Plusieurs modules d’un même type dans une même configuration : celui de plus bas rang fixe la puissance et le temps de recharge ci-dessus, et chacun des autres en ajoute 50 %.

| Modules d’un même type | L’Afterburner dure | Le Shield Surge restaure | L’Emergency Repair répare |
| :---: | --: | --: | --: |
| 1 | 10 s | 100 % | 100 % |
| 2 | 15 s | 150 % | 150 % |
| 3 | 20 s | 200 % | 200 % |

<!-- abilities:end -->

Les boucliers et moteurs de rang III (le Heavy Shield Core, l’Engine III) ne sont pas en vente : on les fabrique à l’[Assemblage](/wiki/06-Items/Overview.md#upgrading-modules) à partir d’un Basic Shield Core et d’un Engine II, avec du Thulium, le butin des aliens et 3 Dark Matter Plates ([Dark Matter et Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)). L’Emergency Repair a un quatrième rang, le Repair Drone IV.

## Temps de recharge et limites {#cooldowns-and-limits}

- **Le temps de recharge commence quand vous appuyez** sur la compétence et inclut sa durée. Un Surge de 10 secondes avec un temps de recharge de 90 secondes est donc actif 11 % du temps au plus, et indisponible pendant 80 secondes après sa fin. Plusieurs modules ne le raccourcissent pas (c’est celui du module de plus bas rang) ; même trois Afterburners sont actifs 22 % du temps au plus.
- **Les temps de recharge vous appartiennent, pas à l’objet.** Changer de configuration, changer d’objet, sauter vers un autre secteur ou se déconnecter ne les remet pas à zéro. Un vaisseau détruit commence le vol suivant avec toutes ses compétences prêtes.
- **Chaque compétence a son propre temps de recharge.** En utiliser une ne bloque pas les autres.
- **Un effet en cours garde les valeurs avec lesquelles il a commencé.** Désinstaller l’objet ou changer de configuration ne le modifie pas et n’y met pas fin. Un saut ou une reconnexion n’y met pas fin non plus ; une déconnexion, si, et son temps de recharge reste.
- Les autres pilotes voient les minuteurs de vos compétences sur la carte, comme toujours : un Surge épuisé leur indique que la voie est libre pour les prochaines minutes.

## Touches et boutons {#keys-and-buttons}

`Q` Shield Surge, `W` Afterburner, `E` Emergency Repair et `F` la compétence du design de votre vaisseau (toutes configurables dans les paramètres). Chaque bouton n’apparaît à côté de la barre rapide que si votre configuration a cette compétence (le bouton `F`, quand le vaisseau que vous pilotez en a une) : le `E` d’un nouveau pilote est donc là dès la première minute. L’anneau autour de son icône indique où en est la compétence : plein, dans la couleur de la compétence, quand elle est prête ; il se vide avec les secondes restantes pendant qu’elle agit (l’Emergency Repair aussi, maintenant qu’il répare sur dix secondes) ; et il se remplit de nouveau pendant la recharge, avec les secondes restantes au centre. Un cumul de plusieurs modules porte sa marque (`x2`, `x3`) dans le coin du bouton. Le bouton Emergency Repair est grisé tant que votre coque est pleine, et le bouton Shield Surge sur un vaisseau sans aucun bouclier. Survolez un bouton pour voir les valeurs sur votre vaisseau, cumul compris (par exemple *Afterburner II x2 : +45 % de vitesse pendant 15 s*), et, pendant un Surge ou une réparation, combien il donne par seconde et combien il reste à venir.

## Dans le hangar {#in-the-hangar}

Faites glisser un bouclier, un moteur ou un Repair Drone sur un emplacement de compétence, ou faites un clic droit dessus dans votre inventaire pour le placer dans le premier emplacement libre. Un deuxième et un troisième du même type vont dans les emplacements libres suivants et se cumulent. Le nom et le rang de la compétence s’affichent sous chaque emplacement occupé, avec la marque du cumul et les valeurs de tous ses modules réunis (*Afterburner II x2*, *x2 · 15 s* ; pour un seul Repair Drone II sur un Wraith, *+81 000 de coque*), et survoler un emplacement montre ce qu’il vaut sur votre vaisseau, cumul compris, et quel module du cumul fixe le rang. Tous les modules d’un même type affichent la même compétence, car ils n’en font qu’une. Survoler l’objet n’importe où ailleurs montre la compétence avec les parts de votre propre vaisseau et une phrase sur ce qu’apporte un module de plus.

## Ce que tout le monde voit {#what-everyone-sees}

Un Shield Surge forme une bulle autour du vaisseau tant qu’il agit ; elle vacille pendant ses deux dernières secondes et se referme à la fin. Les barres de bouclier (la vôtre dans la fenêtre Vaisseau, et celle d’une cible dans la fenêtre Cible) se remplissent simplement à mesure que le Surge remet du bouclier, et la barre pulse légèrement tant qu’il reste de la place à remplir. Un Afterburner fait chauffer davantage les moteurs tant qu’il agit, 10, 15 ou 20 secondes, et émet un anneau depuis le vaisseau à son déclenchement, plus large pour un cumul. Un Emergency Repair émet une pulsation verte à son déclenchement, puis, pendant ses dix secondes, enveloppe la coque d’une douce lueur verte d’où s’élèvent quelques signes plus, affiche au-dessus de votre propre vaisseau la coque qu’il répare chaque seconde, et se termine par un dernier éclair. Pendant qu’il agit, de petits drones de réparation tournent autour du vaisseau et le réparent : un pour un Repair Drone I, deux pour un II, trois pour un III ou un IV, et un de plus pour chaque Repair Drone supplémentaire d’un cumul (jamais plus de trois). Ils quittent la coque, dirigent de doux rayons verts vers ses plaques, envoient des pulsations le long des rayons à partir du rang II, et reviennent s’amarrer une fois les dix secondes écoulées ; un Shield Surge en a jusqu’à deux, bleus, dans sa bulle. Tous les pilotes de la carte voient les trois compétences, drones compris (plus petits sur le vaisseau d’un autre pilote, et moins nombreux avec les réglages graphiques plus bas : en Faible, des rayons et des lueurs sans modèles de drones, avec un rayon un peu plus large pour chaque rang du drone) : un Surge épuisé est donc un signal pour l’ennemi autant que pour vous. Les drones émettent trois sons discrets qui leur sont propres, bien en dessous de la cloche de la réparation : un léger bip quand ils quittent la coque, un autre quand ils s’amarrent et une faible tonalité sous leurs rayons pendant qu’ils travaillent (un peu plus aiguë pour les drones d’un Surge) ; vous les entendez depuis les vaisseaux présents à votre écran, quelques-uns au plus à la fois, et le volume Effets sonores les atténue. Avec *Réduire les animations* activé, la lueur reste fixe, les signes plus sont omis, le dernier éclair devient un fondu, et les drones restent garés à côté du vaisseau avec un rayon fixe (les sons restent). Un Repair Drone dans un emplacement extra (REP) affiche lui aussi ses drones tant qu’il répare la coque : un pour un Repair Drone I, deux pour un II, trois pour un III ou un IV, qui tournent autour du vaisseau et l’arrosent de faisceaux, et tous les pilotes de la carte les voient. Ils retournent s’arrimer quand la réparation s’arrête.

## Ce qui a changé {#what-changed}

Avant la mise à jour 0.4.3, les emplacements de compétence acceptaient les cellules de bouclier (Régén. bouclier) et les propulseurs (Accélération). Les cellules de bouclier et les propulseurs qui se trouvaient dans des emplacements de compétence sont retournés dans votre inventaire lors de la mise à jour du jeu, et vous les gardez : ce sont toujours des modules des boucliers, des moteurs et des cœurs adaptatifs. Depuis, le Shield Surge ne donne plus de barrière de surbouclier mais répare votre bouclier sur dix secondes, l’Emergency Repair répare sur dix secondes au lieu d’un coup, et vous pouvez installer plusieurs modules du même type pour un Afterburner plus long, un Surge plus fort ou une réparation plus importante.
