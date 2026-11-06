<!-- wiki-i18n source: 76933ad9dd56b71f -->
<!-- wiki-i18n title: Donjons -->
# Donjons {#dungeons}

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; portal; clan portal; join; clan gate alerts; clan dungeon window; start room; fog; guards; locked room; boss room; booster; boosters; swarm assist; focus most wanted; zone of chaos; rocket barrage; donjon; donjons; porte; portes; seigneur de guerre; labyrinthe; étape; zone de butin; carte; portail; portail du clan; booster; boosters; brouillard; gardiens; salle de départ; salle verrouillée; renfort d’essaim; zone du chaos; alertes de porte du clan -->

Un **donjon** est ce que le jeu appelle une **porte** : un labyrinthe fermé avec un **Seigneur de guerre** au bout. Un chef adjoint ou le chef d’un [clan](/wiki/03-Mechanics/Clans.md) en ouvre une et la paie avec la banque du clan, et les membres du clan y volent ensemble en un seul [groupe](/wiki/03-Mechanics/Groups.md). Ils se frayent un chemin parmi les aliens du labyrinthe, ouvrent des zones de butin pour choisir une carte dans chacune, et abattent le Seigneur de guerre. Tout pilote qui a pris part au combat est payé à la chute du Seigneur de guerre, dans les limites plus bas. Les portes se trouvent dans l’onglet **Portes** de la page du clan.

Une porte est un combat contre les aliens uniquement : personne ne peut y attaquer un camarade de clan, ni qui que ce soit d’autre. Les aliens ne paient rien. La paie vient du seul Seigneur de guerre, donc la seule façon d’être payé est d’être dans le combat quand il tombe.

## En un coup d’œil {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Ouverture** : À partir du jour 1 de la saison
- **Qui ouvre une porte** : Un chef adjoint ou le chef, qui paie le prix avec la banque du clan
- **Groupe** : De 4 à 10 membres du clan, dans un même groupe
- **Portes par jour** : 3 par clan et par jour UTC, une seule ouverte à la fois
- **Portes en même temps** : 6 dans un monde
- **Cartes** : Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Labyrinthes** : 8 ; l’une est tirée à l’ouverture d’une porte
- **Rassemblement** : 10 min pour se rassembler et lancer. Une porte que personne ne lance se ferme, et son prix retourne à la banque du clan
- **Limite de temps** : Étape 1: 95 min, Étape 2: 130 min, Étape 3: 165 min à partir du lancement. Si le temps s’écoule, la porte échoue et ne paie rien
- **Laissée vide** : Une porte où personne ne reste pendant 3 min échoue
- **Après la chute du Seigneur de guerre** : La porte reste ouverte 2 min pour les pilotes à l’intérieur
- **Retour** : Un pilote qui est parti ou a été détruit peut revenir 3 fois, avec 20 s d’écart

<!-- dungeons-glance:end -->

## Le déroulement {#how-a-run-goes}

1. **Invoquer.** Dans l’onglet Portes, un [chef adjoint ou le chef](/wiki/03-Mechanics/Clans.md#hierarchy-roles) choisit une étape et appuie sur **Invoquer**. Le prix est prélevé sur la [banque du clan](/wiki/03-Mechanics/Clans.md#clan-economy-taxation), et la porte prend l’une des cartes listées plus haut. Une porte que personne ne lance se ferme, et le prix retourne à la banque.
2. **Entrer.** Les membres du clan appuient sur **Entrer** dans la fenêtre du Clan pendant qu’ils volent, sautent par le portail du clan ou appuient sur **Rejoindre** sur la carte d’alerte (voir Entrer). Tout le monde atterrit dans la salle de départ, et les pilotes à l’intérieur forment le groupe de la porte.
3. **Lancer.** La salle de départ est une petite salle à une extrémité du labyrinthe, et son sas reste fermé tant que la porte se rassemble. Il n’y a pas d’aliens dedans, on peut donc y attendre en sécurité. La porte **se lance toute seule** quand chaque pilote qu’elle attend est à l’intérieur et que le groupe est assez grand. Elle attend les membres du clan qui sont en ligne, pas absents, et dans le groupe d’un pilote qui est entré, et elle se lance aussitôt quand le groupe est plein. Le pilote qui a ouvert la porte, ou un officier, peut appuyer sur **Lancer** pour commencer plus tôt avec les pilotes qui sont à l’intérieur, s’ils sont assez nombreux. Un pilote qui part n’est plus attendu. Quand la porte se lance, le sas s’ouvre pour de bon, et ensuite seuls les pilotes qui étaient déjà à l’intérieur peuvent revenir.
4. **Traverser le labyrinthe.** Vous entrez par une extrémité du labyrinthe et le Seigneur de guerre attend à l’autre, dans une salle verrouillée. Le labyrinthe est sombre : vous ne voyez que ce que le groupe a exploré et ce qui est proche de ses vaisseaux. Les aliens dorment en meutes dans les couloirs, et une meute qui se réveille traque le groupe à travers le labyrinthe.
5. **Ouvrir les zones de butin.** Des anneaux dans le labyrinthe marquent les zones. Tenez-en une et le groupe vote pour une carte, qui est versée avec la paie du Seigneur de guerre.
6. **Déverrouiller la salle du boss.** Détruisez les gardiens, les Crystalys et leurs Jumeaux, et le sas de la salle du Seigneur de guerre s’ouvre. Jusque-là, le Seigneur de guerre ne peut pas être blessé.
7. **Vaincre le Seigneur de guerre.** Brisez son bouclier et sa coque, et répondez à ses compétences. Quand il tombe, la porte est terminée.
8. **Être payé.** La paie arrive à l’instant où le Seigneur de guerre tombe. La porte reste ouverte un peu plus longtemps pour les pilotes à l’intérieur, puis se ferme.

## Entrer {#entering}

Pour entrer dans une porte, il vous faut un **vaisseau en vol**, donc décollez d’abord puis ouvrez la fenêtre du Clan, et un [groupe](/wiki/03-Mechanics/Groups.md) comptant assez de membres du clan. Il vous faut aussi le **niveau** que demande l’étape, et vous ne pouvez pas être déjà dans une autre porte. Le groupe d’une porte a une taille limite : une fois plein, personne d’autre ne peut entrer.

Un chef adjoint ou le chef ouvre une porte, une seule à la fois pour le clan, et seulement jusqu’au nombre de portes par jour. La banque du clan doit avoir le prix. Un clan ne peut ouvrir une étape qu’après avoir terminé la précédente.

Dans une porte, vous ne pouvez pas changer de monde, et la Jump CPU et la Base CPU ne fonctionnent pas. Le bouton **Quitter** de la fenêtre Porte de clan vous fait sortir. Il demande d’abord une confirmation, sauf si le Seigneur de guerre est déjà tombé : vous partez alors aussitôt. Un pilote qui est parti, ou qui a été détruit, peut revenir quelques fois, avec une courte attente entre deux.

### Le portail du clan et l’alerte {#the-clan-portal-and-the-call}

Quand une porte est ouverte, le clan reçoit pour elle un **portail** sur la carte d’origine de chaque corporation (`M-1`, `T-1` et `G-1`), un peu en dehors de la zone sûre de la station. Seuls les pilotes du clan le voient : pour tous les autres, il n’existe pas. Il n’a pas de zone sûre à lui. Volez jusqu’à lui et sautez comme à n’importe quel autre portail, et il vous amène dans la porte selon les règles d’**Entrer** : un vaisseau en vol, un groupe avec assez de membres du clan, le niveau de l’étape et de la place dans le groupe. Une fois la porte lancée, seuls les pilotes qui étaient déjà à l’intérieur peuvent l’utiliser. Le portail disparaît quand la porte est terminée.

Tant que la porte de votre clan se rassemble et que vous volez ailleurs, une **alerte** vous parvient : une carte en haut de l’écran de vol, avec un son. Elle dit qui a ouvert la porte, combien de pilotes sont à l’intérieur et combien de temps la porte reste ouverte. **Rejoindre** vous y envoie, comme **Entrer** dans l’onglet Portes, et quand vous quittez la porte, votre vaisseau revient là où il était. Rejoindre est grisé tant que votre groupe est trop petit. **Pas maintenant** masque la carte pour cette porte. Si votre groupe est déjà à l’intérieur et que la porte vous attend, la carte le dit. La carte atteint les pilotes du clan qui volent (pas ceux qui sont amarrés à une station) et qui ont le niveau que demande l’étape. Vous pouvez désactiver la carte et son son avec **Alertes de porte du clan** dans Paramètres › Général › Groupes.

### La fenêtre Porte de clan {#the-clan-dungeon-window}

Dans une porte, la partie a sa propre fenêtre, **Porte de clan**. Elle montre le temps écoulé et ce qui reste, combien d’aliens volent et combien ont été détruits, ce que le groupe doit faire maintenant (explorer le labyrinthe, tenir une zone, trouver le boss, détruire les gardiens, vaincre le Seigneur de guerre), les barres de coque du groupe, la barre de tenue quand vous êtes dans une zone, la compétence du Seigneur de guerre avec son compte à rebours, et le bouton **Quitter**. C’est une fenêtre comme les autres : faites-la glisser par sa barre de titre et fermez-la avec le voyant rouge de son coin. Elle s’ouvre toute seule quand vous entrez dans une porte, une fois pour chaque porte : si vous la fermez, elle reste fermée jusqu’à la porte suivante. La barre d’outils a pour elle un bouton **Porte de clan** tant que vous êtes dans une porte. Quand la fenêtre est fermée, une compétence du Seigneur de guerre qui va démarrer ou qui est en cours s’affiche comme un bandeau d’une ligne avec son nom et son compte à rebours. Cliquez sur le bandeau pour rouvrir la fenêtre.

## Les étapes {#the-stages}

Une porte a une étape, et l’étape est sa difficulté. Une étape plus élevée a des aliens plus résistants qui frappent plus fort, et elle paie plus. Les multiplicateurs du tableau sont ceux des aliens. Les dégâts désignent leurs lasers et leurs roquettes. Le Seigneur de guerre ne suit pas le tableau : il garde ses propres valeurs pour chaque étape, plus bas. Le tableau indique aussi combien d’aliens une étape envoie par rapport à la première. Le **prix** est prélevé sur la banque du clan à l’ouverture de la porte.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Étape | Prérequis | Coque et bouclier des aliens | Nombre d’aliens | Dégâts des aliens | Prix de la porte (crédits, prélevés sur la banque du clan) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Étape 1** | À partir du niveau 6 | ×1 | ×1 | ×1 | 500 000 |
| **Étape 2** | À partir du niveau 7 | ×1,5 | ×1 | ×1,5 | 1 000 000 |
| **Étape 3** | À partir du niveau 8 | ×2 | ×1 | ×2 | 2 000 000 |

<!-- dungeons-stages:end -->

## Le labyrinthe {#the-maze}

Chaque porte est un labyrinthe fermé sur une carte à part, l’une des cartes de la liste ci-dessus, et le labyrinthe est l’une de plusieurs dispositions. Le labyrinthe remplit toute la carte, d’un bord à l’autre : une grille de salles et de couloirs aux murs pleins. Les vaisseaux ne peuvent pas traverser un mur, et un mur bloque les tirs, c’est donc un abri. Un météore tombe d’en haut, et un mur ne l’arrête pas.

**Salles et sas.** La salle de départ, où vous atterrissez, et la salle du Seigneur de guerre, à l’autre bout, ont chacune un sas. Un sas fermé est un mur pour les vaisseaux, les tirs et les aliens. Le sas de départ s’ouvre quand la porte se lance. Celui du Seigneur de guerre reste verrouillé tant que les gardiens ne sont pas détruits (voir [La salle verrouillée](#the-locked-room)). Entre les deux, le labyrinthe a une salle de butin pour chaque zone de butin.

**Brouillard.** Le labyrinthe est sombre. En vol, vous ne voyez ses murs et ses aliens que là où le groupe est passé, et sur une courte distance autour de chaque vaisseau du groupe. Une salle compte comme explorée dès que l’un de vous y entre. La mini-carte fait de même : c’est un plan de tout l’étage qui se remplit à mesure que le groupe l’explore, avec l’entrée, le sas du Seigneur de guerre, les zones que vous avez trouvées et le Seigneur de guerre une fois trouvé. Les pilotes de votre propre groupe sont toujours affichés.

## Les aliens {#the-aliens}

Quatre sortes d’aliens gardent le labyrinthe. Ils dorment en meutes dans les couloirs, jamais dans une salle, et une meute se réveille quand un pilote approche. Une meute réveillée ne vous attend pas : elle traque le groupe à travers le labyrinthe, et une meute qui perd tout le monde retourne là où elle dormait et se soigne. Quelques meutes sont réveillées dès la première seconde, postées dans les couloirs loin de l’entrée, jusqu’à ce qu’un pilote approche. La porte ne garde en l’air qu’un certain nombre d’aliens à la fois, et ce nombre grandit avec la taille du groupe : une meute qui se réveille peut donc devoir attendre de la place, et une meute que vous détruisez laisse entrer la suivante. Un groupe plus grand rencontre plus d’aliens, en proportion, un groupe plus petit moins, et une sorte d’alien ne descend jamais sous un.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Aliens, pour un groupe de 5 | Étape 1 | Étape 2 | Étape 3 |
| :--- | ---: | ---: | ---: |
| Gate Goombah | 156 | 156 | 156 |
| Gate Pirate | 34 | 34 | 34 |
| Gate Crystalys | 34 | 34 | 34 |
| Gate Crystalys Twin | 11 | 11 | 11 |
| Total | 235 | 235 | 235 |
| La vague d’une zone de butin | 12 × Gate Goombah et 1 × Gate Crystalys | 12 × Gate Goombah et 1 × Gate Crystalys | 12 × Gate Goombah et 1 × Gate Crystalys |

- **Vivants en même temps** : Au plus 10 par pilote du groupe, et 70 en tout

<!-- dungeons-population:end -->

Chaque sorte à tour de rôle. La coque et le bouclier sont les valeurs habituelles multipliées par le facteur de l’étape de la colonne.

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Gate Goombah

- **Ressemble à** : Goombah
- **Vole en meutes de** : 6

|  | Étape 1 | Étape 2 | Étape 3 |
| :--- | ---: | ---: | ---: |
| Coque | 32 000 | 48 000 | 64 000 |
| Bouclier | 48 000 | 72 000 | 96 000 |
| Dégâts des lasers (une salve par seconde) | 3 000 | 4 500 | 6 000 |
| Vitesse | 180 | 180 | 180 |
| Portée des lasers | 800 | 800 | 800 |
| Rayon d’aggro | 1 800 | 1 800 | 1 800 |

### Gate Pirate

- **Ressemble à** : Pirate Boss
- **Vole en meutes de** : 2
- **Roquette** : Une roquette droite toutes les 5 s, portée de 970 unités

|  | Étape 1 | Étape 2 | Étape 3 |
| :--- | ---: | ---: | ---: |
| Coque | 300 000 | 450 000 | 600 000 |
| Bouclier | 50 100 | 75 150 | 100 200 |
| Dégâts des lasers (une salve par seconde) | 200 | 300 | 400 |
| Dégâts de roquette | 5 000 | 7 500 | 10 000 |
| Vitesse | 92 | 92 | 92 |
| Portée des lasers | 700 | 700 | 700 |
| Rayon d’aggro | 1 800 | 1 800 | 1 800 |

### Gate Crystalys

- **Ressemble à** : Crystalys
- **Vole en meutes de** : 2

|  | Étape 1 | Étape 2 | Étape 3 |
| :--- | ---: | ---: | ---: |
| Coque | 256 000 | 384 000 | 512 000 |
| Bouclier | 160 000 | 240 000 | 320 000 |
| Dégâts des lasers (une salve par seconde) | 10 000 | 15 000 | 20 000 |
| Vitesse | 230 | 230 | 230 |
| Portée des lasers | 900 | 900 | 900 |
| Rayon d’aggro | 2 400 | 2 400 | 2 400 |

### Gate Crystalys Twin

- **Ressemble à** : Crystalys, 1,4 fois plus grand
- **Vole en meutes de** : 1

|  | Étape 1 | Étape 2 | Étape 3 |
| :--- | ---: | ---: | ---: |
| Coque | 512 000 | 768 000 | 1 024 000 |
| Bouclier | 320 000 | 480 000 | 640 000 |
| Dégâts des lasers (une salve par seconde) | 20 000 | 30 000 | 40 000 |
| Vitesse | 230 | 230 | 230 |
| Portée des lasers | 900 | 900 | 900 |
| Rayon d’aggro | 2 400 | 2 400 | 2 400 |

<!-- dungeons-enemies:end -->

## Le Seigneur de guerre {#the-warlord}

Le Seigneur de guerre attend dans la salle au bout du labyrinthe, et c’est la seule chose dans une porte qui paie. C’est un Crystalys devenu énorme. Sa coque et son bouclier grandissent avec la taille du groupe : plus il entre de pilotes, plus il est résistant, en proportion. Il ne quitte jamais sa salle, porte fermée ou ouverte : il reste entre les murs de la salle et ne traque pas dans les couloirs. Un pilote à l’extérieur ne peut l’attirer que jusqu’au bord de la salle, et il tire quand même par une porte ouverte sur tout ce que son laser atteint. Il utilise ses compétences une à la fois, dans un ordre aléatoire, chacune avec son propre temps de recharge.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Ressemble à** : Crystalys, 3 fois plus grand
- **Recharge du bouclier** : 3 000 par seconde, après 15 s sans dégâts

|  | Étape 1 | Étape 2 | Étape 3 |
| :--- | ---: | ---: | ---: |
| Coque | 10 000 000 | 15 000 000 | 25 000 000 |
| Bouclier | 8 000 000 | 12 000 000 | 20 000 000 |
| Dégâts des lasers (une salve par seconde) | 12 500–15 000 | 15 000–17 500 | 20 000–25 000 |
| Vitesse | 120 | 120 | 120 |
| Portée des lasers | 1 100 | 1 100 | 1 100 |

La coque et le bouclier ci-dessus valent pour un groupe de 5. Ils croissent avec le groupe : ce sont la coque et le bouclier du Seigneur de guerre réunis, selon le nombre de pilotes du groupe au lancement de la porte.

| Pilotes dans le groupe | Étape 1 | Étape 2 | Étape 3 |
| :--- | ---: | ---: | ---: |
| 4 | 14 400 000 | 21 600 000 | 36 000 000 |
| 5 | 18 000 000 | 27 000 000 | 45 000 000 |
| 6 | 21 600 000 | 32 400 000 | 54 000 000 |
| 7 | 25 200 000 | 37 800 000 | 63 000 000 |
| 8 | 28 800 000 | 43 200 000 | 72 000 000 |
| 9 | 32 400 000 | 48 600 000 | 81 000 000 |
| 10 | 36 000 000 | 54 000 000 | 90 000 000 |

<!-- dungeons-boss:end -->

### La salle verrouillée {#the-locked-room}

Le sas de la salle du Seigneur de guerre est fermé dès l’ouverture de la porte, et tant qu’il l’est, le Seigneur de guerre ne peut pas être blessé : aucun laser, aucune roquette, aucune explosion ne le touche, et il n’utilise aucune compétence. Le sas s’ouvre pour de bon quand le groupe a détruit les **gardiens** : le Gate Crystalys et le Gate Crystalys Twin avec lesquels la porte a été faite, environ un cinquième de ses aliens. Le Gate Goombah et le Gate Pirate ne comptent pas, pas plus que les vagues des zones de butin ou les Goombahs que le Seigneur de guerre appelle.

La fenêtre Porte de clan compte les gardiens qui restent et dit, dans une pastille, que le Seigneur de guerre ne peut pas être blessé, et un message vous prévient quand la salle est déverrouillée. Une meute de gardiens qui dort encore compte en entier, le groupe doit donc explorer le labyrinthe et les trouver tous. Sur la mini-carte, le sas est une ligne rouge tant qu’il est verrouillé et une ligne verte quand il est ouvert. Une porte n’est jamais un piège : la limite de temps met quand même fin à une porte dont on ne retrouve pas les derniers gardiens, et un administrateur peut déverrouiller la salle d’une porte bloquée.

### Ses compétences {#its-abilities}

- **L’anneau rouge** de l’Aura de vol de vie blesse tout pilote à l’intérieur et soigne le Seigneur de guerre de ces dégâts. L’Absorption de bouclier a aussi un anneau rouge : il draine les boucliers des pilotes à l’intérieur et charge celui du Seigneur de guerre. Dans les deux cas, quittez l’anneau ou mettez-vous derrière un mur.
- **Les anneaux ambrés** de la Chute de météores montrent où les météores tomberont un instant plus tard. Bougez sans cesse et sortez de l’anneau avant l’impact.
- **Focus sur le plus recherché** marque le pilote qui a infligé le plus de dégâts au Seigneur de guerre, d’un crochet doré sur son vaisseau, et le Seigneur de guerre tire sur lui un trait de plus chaque seconde tant que la compétence dure. Sa visée ne change pas : il continue de tirer sur le pilote le plus proche qu’il voit, un pilote marqué qui est aussi le plus proche prend donc les deux. Le trait supplémentaire demande une ligne dégagée et la portée du laser du Seigneur de guerre, donc un mur ou un peu de distance le sauve. Elle ne démarre pas tant que personne n’a infligé de dégâts.
- **La Salve de roquettes** lance des roquettes à tête chercheuse sur des pilotes au hasard, mais seulement sur des pilotes que le Seigneur de guerre peut voir, et un mur sur le chemin arrête une roquette. Un anneau montre quel pilote une roquette suit. Une EMP Charge ou une occultation les fait lâcher prise.
- **Le Renfort d’essaim** est le Seigneur de guerre qui appelle ses Goombahs. Tant qu’ils vivent, il ne peut pas être blessé, et il ne tire pas et n’utilise aucune autre compétence. Détruisez-les tous : la bannière compte combien il en reste. Si une minute passe, le Seigneur de guerre peut de nouveau être blessé et les Goombahs qui restent continuent le combat. Ce ne sont pas des gardiens, et ils ne paient rien.
- **La Zone du Chaos** est un anneau violet au sol, autour de l’endroit où se tenait le Seigneur de guerre quand il l’a lancée. Personne dans l’anneau ne peut attaquer, ni avec des lasers ni avec des roquettes, mais les réparations, l’occultation et le vol fonctionnent toujours, et le Seigneur de guerre et ses aliens tirent comme toujours. L’anneau apparaît un instant avant de faire effet : sortez-en, et tirez dedans depuis l’extérieur.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Compétence | Préparation | Durée | Temps de recharge | Rayon de l’anneau (unités) | Le Seigneur de guerre regagne, au plus |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Aura de vol de vie** | 2 s | 15 s | 2 min | 900 | 8 % de sa coque et de son bouclier |
| **Chute de météores** | 1,5 s | 3 salves, espacées de 4 s | 2 min | 420 | – |
| **Focus sur le plus recherché** | 1 s | 20 s | 2 min | – | – |
| **Salve de roquettes** | 1,5 s | 45 s | 2 min | – | – |
| **Absorption de bouclier** | 2 s | 15 s | 2 min | 900 | 6 % de son bouclier |
| **Renfort d’essaim** | 2 s | Jusqu’à 1 min | 3 min | – | – |
| **Zone du Chaos** | 2 s | 15 s | 2 min | 900 | – |

| Compétence | Étape 1 | Étape 2 | Étape 3 |
| :--- | :--- | :--- | :--- |
| **Aura de vol de vie** | 8 000 par seconde | 10 000 par seconde | 12 000 par seconde |
| **Chute de météores** | 6 météores par salve, 40 000 chacun | 8 météores par salve, 50 000 chacun | 10 météores par salve, 60 000 chacun |
| **Focus sur le plus recherché** | 18 750–22 500 par tir supplémentaire sur le pilote ayant infligé le plus de dégâts, un toutes les 1 s | 22 500–26 250 par tir supplémentaire sur le pilote ayant infligé le plus de dégâts, un toutes les 1 s | 30 000–37 500 par tir supplémentaire sur le pilote ayant infligé le plus de dégâts, un toutes les 1 s |
| **Salve de roquettes** | 6 500 par roquette, une toutes les 15 s | 8 125 par roquette, une toutes les 15 s | 9 750 par roquette, une toutes les 15 s |
| **Absorption de bouclier** | 10 000 de bouclier par seconde | 12 500 de bouclier par seconde | 15 000 de bouclier par seconde |
| **Renfort d’essaim** | 12 Goombahs | 18 Goombahs | 24 Goombahs |
| **Zone du Chaos** | Les pilotes dans l’anneau ne peuvent pas attaquer | Les pilotes dans l’anneau ne peuvent pas attaquer | Les pilotes dans l’anneau ne peuvent pas attaquer |

<!-- dungeons-abilities:end -->

## Zones de butin {#loot-zones}

Un anneau au sol du labyrinthe marque chaque zone de butin dès que le groupe l’a trouvée. Restez un moment dedans et la zone s’éveille, et une vague d’aliens arrive sur elle. Le groupe doit alors **tenir** la zone : garder un pilote dedans jusqu’à ce que la barre se remplisse. Plus il y a de pilotes dans l’anneau, plus vite la barre se remplit : un nombre à côté de la barre dit combien de fois plus vite, et le tableau ci-dessous donne les durées. Assez d’aliens dans l’anneau arrêtent la barre (la liste ci-dessous dit combien), et elle recule tant que personne n’est dedans, nettoyez donc d’abord la vague. Quand la zone s’ouvre, le groupe voit trois cartes différentes et **vote** pour l’une d’elles. Une zone ne s’ouvre qu’une fois, et sa vague ne revient pas.

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Zones de butin** : 6 dans chaque labyrinthe
- **Rayon** : 450 unités
- **Réveil** : Restez 2 s à l’intérieur de l’anneau
- **Tenue** : Gardez un pilote à l’intérieur pendant 30 s. La jauge s’arrête tant que 3 aliens ou plus sont dans l’anneau, et recule tant que personne n’y est
- **Choix** : Le groupe a 45 s pour voter. Le vote se termine plus tôt si tous les pilotes présents ont voté ou si une carte a plus de la moitié des voix

Plus il y a de pilotes dans l’anneau, plus une zone est tenue vite. Voici le temps qu’il faut pour tenir une zone :

| Pilotes dans l’anneau | Temps pour tenir la zone |
| :--- | ---: |
| 1 | 30 s |
| 2 | 20 s |
| 3 | 15 s |
| 4 | 12 s |
| 5 ou plus | 10 s |

<!-- dungeons-zones:end -->

### Boosters

Aux étapes 2 et 3, les vagues des zones de butin apportent aussi des boosters. Quand le groupe a détruit tous les aliens d’une vague, la vague compte, et après chaque deuxième vague (la deuxième, la quatrième et la sixième), chaque pilote reçoit une fenêtre d’une demi-minute pour choisir un booster temporaire pour lui-même : **Dégâts** (vos lasers frappent plus fort), **Points de vie** (votre vaisseau tient plus de coque) ou **Vitesse** (votre vaisseau vole plus vite). Appuyez sur une carte pour la choisir. Si vous ne répondez pas à temps, le jeu choisit Points de vie pour vous. Un choix vaut 3 % à l’étape 3 et 1,5 % à l’étape 2, et un type s’additionne jusqu’à 9 % à l’étape 3 et 4,5 % à l’étape 2, quel que soit le nombre de fois où vous le choisissez. L’étape 1 n’a pas de boosters. Un groupe qui laisse une vague en vie n’obtient pas de fenêtre pour elle.

Un booster dure jusqu’à ce que la porte soit terminée. Si vous quittez la porte, ou si vous êtes détruit, vous perdez vos boosters, et vous les retrouvez quand vous revolez dedans. Une pastille sous la fenêtre Porte de clan liste ce que vous avez.

### Les cartes {#the-cards}

Les cartes sont tirées une à une dans la réserve ci-dessous. La chance est celle d’une carte lors d’un tirage. Chaque carte va à chaque pilote payé, les cartes d’équipement aussi : une carte à nombreux exemplaires en donne autant à chacun, et une carte d’équipement donne à chacun une pièce à lui, forgée pour lui. Un pilote qui n’est pas payé ne reçoit pas de carte non plus, et une zone ouverte dans une porte qui échoue ne paie rien.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Carte | Étape 1 | Étape 2 | Étape 3 | Chance | Revient à |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2 000 | 3 000 | 5 000 | 23,9 % | Chaque pilote payé |
| Velkonite Reinforced Plate | 10 | 15 | 25 | 13,65 % | Chaque pilote payé |
| Velkonite | 200 | 300 | 500 | 13,65 % | Chaque pilote payé |
| Orvium | 200 | 300 | 500 | 13,65 % | Chaque pilote payé |
| Ultra Core | 5 000 | 7 500 | 12 500 | 11,4 % | Chaque pilote payé |
| Experimental Fusion Core | 3 000 | 4 500 | 7 500 | 9,1 % | Chaque pilote payé |
| Dark Matter | 5 | 8 | 12 | 9,1 % | Chaque pilote payé |
| Dark Matter Plate | 1 | 1 | 2 | 4,55 % | Chaque pilote payé |
| Starfire-III | – | – | 1 | 0,07 % | Chaque pilote payé |
| Helios Beam | – | – | 1 | 0,07 % | Chaque pilote payé |
| Engine III | – | – | 1 | 0,07 % | Chaque pilote payé |
| Adaptive Core III | – | – | 1 | 0,07 % | Chaque pilote payé |
| Heavy Shield Core | – | – | 1 | 0,07 % | Chaque pilote payé |
| Momentum Thruster IV | – | – | 1 | 0,07 % | Chaque pilote payé |
| Impulse Thruster IV | – | – | 1 | 0,07 % | Chaque pilote payé |
| Hull Plating II | – | – | 1 | 0,07 % | Chaque pilote payé |
| Hull Plating III | – | – | 1 | 0,07 % | Chaque pilote payé |
| Damage Amp IV | – | – | 1 | 0,07 % | Chaque pilote payé |
| Crit Amp IV | – | – | 1 | 0,07 % | Chaque pilote payé |
| Penetration Amp IV | – | – | 1 | 0,07 % | Chaque pilote payé |
| Capacity Shield Cell IV | – | – | 1 | 0,08 % | Chaque pilote payé |
| Absorption Shield Cell IV | – | – | 1 | 0,08 % | Chaque pilote payé |

- **Équipement** : Les cartes à un seul exemplaire sont de l’équipement : ensemble 1 % des cartes

<!-- dungeons-cards:end -->

Les cartes à un seul exemplaire sont de l’**équipement**, et seule une porte d’étape 3 peut en proposer. Une pièce d’équipement est forgée pour chaque pilote payé au moment du paiement : chacun tire son propre [rang d’enchantement](/wiki/06-Items/Overview.md#item-enchants) avec les mêmes chances qu’une pièce que vous fabriquez à l’Assemblage, la plupart sortent donc Standard, et un rang plus élevé, jusqu’à Éternel, avec des bonus, est une trouvaille rare.

## Paie {#pay}

À la chute du Seigneur de guerre, tout pilote qui l’a mérité est payé, une fois par partie. Les cartes choisies par le groupe s’ajoutent à la paie de l’étape. Il n’y a pas de multiplicateur de monde : la paie est la même dans tous les mondes.

Les **Orvium Reinforced Plates** ne sont pas une carte du vote. Elles font partie de la paie de l’étape, et chaque pilote payé les reçoit une fois pour la réussite. Les objets qu’une porte paie ne sont pas vendables : vous ne pouvez pas [les vendre aux Enchères](/wiki/03-Mechanics/Auction.md#marketable-items).

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Étape | Honneur | Expérience | Crédits | Thulium | Munitions x4 | Orvium Reinforced Plates | Points de classement PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Étape 1** | 25 000 | 600 000 | 5 000 000 | 4 000 | 4 000 | 5 | 600 |
| **Étape 2** | 50 000 | 1 500 000 | 10 000 000 | 9 000 | 9 000 | 10 | 1 500 |
| **Étape 3** | 100 000 | 2 400 000 | 17 500 000 | 15 000 | 15 000 | 15 | 2 400 |

<!-- dungeons-pay:end -->

### Qui est payé {#who-is-paid}

Les aliens ne paient jamais. Une partie se joue en entier même quand elle ne paie rien, et l’écran de résultat dit pourquoi. L’entrée n’est jamais refusée parce que vous avez déjà été payé pour une étape : cette partie ne paie simplement rien.

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Un jour** : Une étape paie un pilote une fois par jour UTC : le jour où le Seigneur de guerre tombe
- **Une semaine** : Un pilote est payé pour un maximum de 10 étapes terminées par semaine UTC, du lundi au dimanche
- **À l’intérieur** : Au moins 2 min en tout
- **Part au combat** : Au moins l’un de ceux-ci : a infligé 2 % de la coque et du bouclier du Seigneur de guerre; a détruit 10 aliens de la porte; a soigné d’autres pilotes à hauteur de 50 000 pendant le combat contre le Seigneur de guerre

<!-- dungeons-rules:end -->

### Ce que valent un jour et une semaine {#what-a-day-and-a-week-are-worth}

Ce qu’un pilote peut toucher en un jour, et dans la meilleure semaine que permettent les limites. La dernière colonne est ce que la paie ajoute à vos [points PvE](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points).

<!-- dungeons-totals:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Paie de chaque pilote | Honneur | Expérience | Crédits | Thulium | Munitions x4 | Orvium Reinforced Plates | Points de classement PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Un jour, chaque étape une fois | 175 000 | 4 500 000 | 32 500 000 | 28 000 | 28 000 | 30 | 4 500 |
| La meilleure semaine : 7 × Étape 3 et 3 × Étape 2 | 850 000 | 21 300 000 | 152 500 000 | 132 000 | 132 000 | 135 | 21 300 |

L’expérience d’une étape terminée et payée compte pour vos points de classement PvE : un point pour chaque tranche de 1 000 d’expérience.

<!-- dungeons-totals:end -->

## La récompense de la banque du clan {#clan-bank-reward}

La banque du clan est payée aussi, en crédits et non en Thulium, la première fois que le clan termine une étape pendant une saison. Le clan doit être assez ancien, et assez de pilotes de cette partie doivent être payés. La banque est payée une fois par étape et par saison.

<!-- dungeons-clan:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Étape | Crédits pour la banque du clan |
| :--- | ---: |
| **Étape 1** | 10 000 000 |
| **Étape 2** | 20 000 000 |
| **Étape 3** | 30 000 000 |

- **Ancienneté du clan** : Au moins 3 j
- **Pilotes payés** : Au moins 3 dans la porte

<!-- dungeons-clan:end -->

## Conseils {#tips}

- Éliminez la vague d’une zone avant d’essayer de la tenir, et battez-vous dans l’anneau si des aliens y entrent.
- Amenez tout le groupe dans une zone : plus il y a de pilotes dans l’anneau, plus vite elle est tenue.
- Explorez chaque recoin du labyrinthe : une meute de gardiens que vous ne trouvez jamais garde le sas du Seigneur de guerre fermé.
- Servez-vous des murs : les lasers ne les traversent pas, les anneaux rouges des auras du Seigneur de guerre s’y arrêtent, et un mur arrête aussi ses roquettes.
- Gardez une EMP Charge pour la Salve de roquettes.
- Quand le Seigneur de guerre appelle ses Goombahs, détruisez-les d’abord : il ne peut pas être blessé tant qu’ils ne sont pas partis. Dans la Zone du Chaos, sortez de l’anneau avant de tirer.
- Surveillez l’horloge de la fenêtre Porte de clan. Quand le temps est écoulé, la porte échoue et ne paie rien.
