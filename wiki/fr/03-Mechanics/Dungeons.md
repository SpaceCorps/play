<!-- wiki-i18n source: c3506248209cf351 -->
<!-- wiki-i18n title: Donjons -->
# Donjons {#dungeons}

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; portal; clan portal; join; clan gate alerts; clan dungeon window; clan dungeon alerts; dungeon goombah; dungeon pirate; dungeon crystalys; dungeon warlord; 75 percent; three quarters; start room; fog; guards; locked room; boss room; booster; boosters; swarm assist; focus most wanted; zone of chaos; rocket barrage; donjon; donjons; porte; portes; seigneur de guerre; labyrinthe; étape; zone de butin; carte; portail; portail du clan; booster; boosters; brouillard; gardiens; salle de départ; salle verrouillée; renfort d’essaim; zone du chaos; alertes de porte du clan; donjon de clan; alertes de donjon du clan; trois quarts; 75 pour cent -->

Un **donjon** est un labyrinthe fermé avec un **Seigneur de guerre** au bout (avant la 0.5.2, le jeu l’appelait une porte). Un chef adjoint ou le chef d’un [clan](/wiki/03-Mechanics/Clans.md) en ouvre une et la paie avec la banque du clan, et les membres du clan y volent ensemble en un seul [groupe](/wiki/03-Mechanics/Groups.md). Ils se frayent un chemin parmi les aliens du labyrinthe, ouvrent des zones de butin pour choisir une carte dans chacune, et abattent le Seigneur de guerre. Tout pilote qui a pris part au combat est payé à la chute du Seigneur de guerre, dans les limites plus bas. Les donjons se trouvent dans l’onglet **Donjons** de la page du clan.

Un donjon est un combat contre les aliens uniquement : personne ne peut y attaquer un camarade de clan, ni qui que ce soit d’autre. Les aliens paient en tombant, comme les aliens du jeu dont ils s’inspirent ([ce que paient les aliens](#what-the-aliens-pay)). La réussite appartient au Seigneur de guerre : la seule façon d’être payé pour elle est d’être dans le combat quand il tombe.

Un donjon n’est pas une [porte solo](/wiki/03-Mechanics/Solo-Gates.md). Une porte solo est une arène où vous êtes seul, ouverte avec des pièces que vous trouvez avec le Matérialiseur d’énergie : les deux ont des règles, des paiements et des limites séparés.

## En un coup d’œil {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Ouverture** : À partir du jour 1 de la saison
- **Qui ouvre un donjon** : Un chef adjoint ou le chef, qui paie le prix avec la banque du clan
- **Groupe** : De 4 à 10 membres du clan, dans un même groupe
- **Donjons par jour** : 3 par clan et par jour UTC, une seule ouverte à la fois
- **Donjons en même temps** : 6 dans un monde
- **Cartes** : Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Labyrinthes** : 8 ; l’un est tiré à l’ouverture d’un donjon
- **Salle du boss** : S’ouvre quand 75 % des Crystalys et de leurs Twins sont détruits, arrondi à l’entier supérieur
- **Rassemblement** : 10 min pour se rassembler et lancer. Un donjon que personne ne lance se ferme, et son prix retourne à la banque du clan
- **Limite de temps** : Étape 1: 95 min, Étape 2: 130 min, Étape 3: 165 min à partir du lancement. Si le temps s’écoule, le donjon échoue et la réussite ne paie rien
- **Laissée vide** : Un donjon où personne ne reste pendant 3 min échoue
- **Après la chute du Seigneur de guerre** : Le donjon reste ouvert 2 min pour les pilotes à l’intérieur
- **Retour** : Un pilote qui est parti ou a été détruit peut revenir aussi souvent qu’il le veut, avec au moins 20 s entre deux retours

<!-- dungeons-glance:end -->

## Le déroulement {#how-a-run-goes}

1. **Invoquer.** Dans l’onglet Donjons, un [chef adjoint ou le chef](/wiki/03-Mechanics/Clans.md#hierarchy-roles) choisit une étape et appuie sur **Invoquer**. Le prix est prélevé sur la [banque du clan](/wiki/03-Mechanics/Clans.md#clan-economy-taxation), et le donjon prend l’une des cartes listées plus haut. Un donjon que personne ne lance se ferme, et le prix retourne à la banque.
2. **Entrer.** Les membres du clan appuient sur **Entrer** dans la fenêtre du Clan pendant qu’ils volent, sautent par le portail du clan ou appuient sur **Rejoindre** sur la carte d’alerte (voir Entrer). Tout le monde atterrit dans la salle de départ, et les pilotes à l’intérieur forment le groupe du donjon.
3. **Lancer.** La salle de départ est une petite salle à une extrémité du labyrinthe, et son sas reste fermé tant que le donjon se rassemble. Il n’y a pas d’aliens dedans, on peut donc y attendre en sécurité. Le donjon **se lance toute seule** quand chaque pilote qu’elle attend est à l’intérieur et que le groupe est assez grand. Elle attend les membres du clan qui sont en ligne, pas absents, et dans le groupe d’un pilote qui est entré, et elle se lance aussitôt quand le groupe est plein. Le pilote qui a ouvert le donjon, ou un officier, peut appuyer sur **Lancer** pour commencer plus tôt avec les pilotes qui sont à l’intérieur, s’ils sont assez nombreux. Un pilote qui part n’est plus attendu. Quand le donjon se lance, le sas s’ouvre pour de bon, et ensuite seuls les pilotes qui étaient déjà à l’intérieur peuvent revenir.
4. **Traverser le labyrinthe.** Vous entrez par une extrémité du labyrinthe et le Seigneur de guerre attend à l’autre, dans une salle verrouillée. Le labyrinthe est sombre : vous ne voyez que ce que le groupe a exploré et ce qui est proche de ses vaisseaux. Les aliens attendent en meutes dans les couloirs, et une meute sort dès qu’un pilote vole dans le tronçon de couloir où elle attend, puis traque le groupe à travers le labyrinthe.
5. **Ouvrir les zones de butin.** Des anneaux dans le labyrinthe marquent les zones. Tenez-en une et le groupe vote pour une carte, qui est versée avec la paie du Seigneur de guerre.
6. **Déverrouiller la salle du boss.** Détruisez les trois quarts des Crystalys et de leurs Twins du labyrinthe, et le sas de la salle du Seigneur de guerre s’ouvre. Jusque-là, le Seigneur de guerre ne peut pas être blessé. Les autres aliens restent où ils sont, et vous pouvez aussi les détruire.
7. **Vaincre le Seigneur de guerre.** Brisez son bouclier et sa coque, et répondez à ses compétences. Quand il tombe, le donjon est terminé.
8. **Être payé.** La paie arrive à l’instant où le Seigneur de guerre tombe. Le donjon reste ouvert un peu plus longtemps pour les pilotes à l’intérieur, puis se ferme.

## Entrer {#entering}

Pour entrer dans un donjon, il vous faut un **vaisseau en vol**, donc décollez d’abord puis ouvrez la fenêtre du Clan, et un [groupe](/wiki/03-Mechanics/Groups.md) comptant assez de membres du clan. Il vous faut aussi le **niveau** que demande l’étape, et vous ne pouvez pas être déjà dans un autre donjon. Le groupe d’un donjon a une taille limite : une fois plein, personne d’autre ne peut entrer.

Un chef adjoint ou le chef ouvre un donjon, un seul à la fois pour le clan, et seulement jusqu’au nombre de donjons par jour. La banque du clan doit avoir le prix. Un clan ne peut ouvrir une étape qu’après avoir terminé la précédente.

Dans un donjon, vous ne pouvez pas changer de monde, et la Jump CPU et la Base CPU ne fonctionnent pas. Le bouton **Quitter** de la fenêtre Donjon de clan vous fait sortir. Il demande d’abord une confirmation, sauf si le Seigneur de guerre est déjà tombé : vous partez alors aussitôt. Un pilote qui est parti, ou qui a été détruit, peut revenir ; la liste sous **En un coup d’œil** dit combien de fois, et combien de temps il attend entre deux retours.

### Le portail du clan et l’alerte {#the-clan-portal-and-the-call}

Quand un donjon est ouvert, le clan reçoit pour elle un **portail** sur la carte d’origine de chaque corporation (`M-1`, `T-1` et `G-1`), un peu en dehors de la zone sûre de la station. Seuls les pilotes du clan le voient : pour tous les autres, il n’existe pas. Il n’a pas de zone sûre à lui. Volez jusqu’à lui et sautez comme à n’importe quel autre portail, et il vous amène dans le donjon selon les règles d’**Entrer** : un vaisseau en vol, un groupe avec assez de membres du clan, le niveau de l’étape et de la place dans le groupe. Une fois le donjon lancé, seuls les pilotes qui étaient déjà à l’intérieur peuvent l’utiliser. Le portail disparaît quand le donjon est terminé.

Tant que le donjon de votre clan se rassemble et que vous volez ailleurs, une **alerte** vous parvient : une carte en haut de l’écran de vol, avec un son. Elle dit qui a ouvert le donjon, combien de pilotes sont à l’intérieur et combien de temps le donjon reste ouvert. **Rejoindre** vous y envoie, comme **Entrer** dans l’onglet Donjons, et quand vous quittez le donjon, votre vaisseau revient là où il était. Rejoindre est grisé tant que votre groupe est trop petit. **Pas maintenant** masque la carte pour ce donjon. Si votre groupe est déjà à l’intérieur et que le donjon vous attend, la carte le dit. La carte atteint les pilotes du clan qui volent (pas ceux qui sont amarrés à une station) et qui ont le niveau que demande l’étape. Vous pouvez désactiver la carte et son son avec **Alertes de donjon du clan** dans Paramètres › Général › Groupes.

### La fenêtre Donjon de clan {#the-clan-dungeon-window}

Dans un donjon, la partie a sa propre fenêtre, **Donjon de clan**. Elle montre le temps écoulé et ce qui reste, combien d’aliens volent et combien ont été détruits, ce que le groupe doit faire maintenant (explorer le labyrinthe, tenir une zone, trouver le boss, détruire les trois quarts des Crystalys et de leurs Twins, vaincre le Seigneur de guerre), la barre de tenue quand vous êtes dans une zone, la compétence du Seigneur de guerre avec son compte à rebours, et le bouton **Quitter**. C’est une fenêtre comme les autres : faites-la glisser par sa barre de titre et fermez-la avec le voyant rouge de son coin. Elle s’ouvre toute seule quand vous entrez dans un donjon, une fois pour chaque donjon : si vous la fermez, elle reste fermée jusqu’au donjon suivant. La barre d’outils a pour elle un bouton **Donjon de clan** tant que vous êtes dans un donjon. Quand la fenêtre est fermée, une compétence du Seigneur de guerre qui va démarrer ou qui est en cours s’affiche comme un bandeau d’une ligne avec son nom et son compte à rebours. Cliquez sur le bandeau pour rouvrir la fenêtre.

## Les étapes {#the-stages}

Un donjon a une étape, et l’étape est sa difficulté. Une étape plus élevée a des aliens plus résistants qui frappent plus fort, et elle paie plus. Les multiplicateurs du tableau sont ceux des aliens. Les dégâts désignent leurs lasers et leurs roquettes. Le Seigneur de guerre ne suit pas le tableau : il garde ses propres valeurs pour chaque étape, plus bas. Le tableau indique aussi combien d’aliens une étape envoie par rapport à la première. Le **prix** est prélevé sur la banque du clan à l’ouverture du donjon.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Étape | Prérequis | Coque et bouclier des aliens | Nombre d’aliens | Dégâts des aliens | Prix du donjon (crédits, prélevés sur la banque du clan) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Étape 1** | À partir du niveau 6 | ×1 | ×1 | ×1 | 500 000 |
| **Étape 2** | À partir du niveau 7 | ×1,5 | ×1 | ×1,5 | 1 000 000 |
| **Étape 3** | À partir du niveau 8 | ×2 | ×1 | ×2 | 2 000 000 |

<!-- dungeons-stages:end -->

## Le labyrinthe {#the-maze}

Chaque donjon est un labyrinthe fermé sur une carte à part, l’une des cartes de la liste ci-dessus, et le labyrinthe est l’une de plusieurs dispositions. Le labyrinthe remplit toute la carte, d’un bord à l’autre : une grille de salles et de couloirs aux murs pleins. Les vaisseaux ne peuvent pas traverser un mur, et un mur bloque les tirs, c’est donc un abri. Un météore tombe d’en haut, et un mur ne l’arrête pas.

**Salles et sas.** La salle de départ, où vous atterrissez, et la salle du Seigneur de guerre, à l’autre bout, ont chacune un sas. Un sas fermé est un mur pour les vaisseaux, les tirs et les aliens. Le sas de départ s’ouvre quand le donjon se lance. Celui du Seigneur de guerre reste verrouillé tant que les trois quarts des Crystalys et de leurs Twins ne sont pas détruits (voir [La salle verrouillée](#the-locked-room)). Entre les deux, le labyrinthe a une salle de butin pour chaque zone de butin.

**Brouillard.** Le labyrinthe est sombre. En vol, vous ne voyez ses murs et ses aliens que là où le groupe est passé, et sur une courte distance autour de chaque vaisseau du groupe. Une salle compte comme explorée dès que l’un de vous y entre. La mini-carte fait de même : c’est un plan de tout l’étage qui se remplit à mesure que le groupe l’explore, avec l’entrée, le sas du Seigneur de guerre, les zones que vous avez trouvées et le Seigneur de guerre une fois trouvé. Les pilotes de votre propre groupe sont toujours affichés.

## Les aliens {#the-aliens}

Quatre sortes d’aliens gardent le labyrinthe. Ils attendent en meutes dans les couloirs, jamais dans une salle, et une meute sort dès qu’un pilote vole dans le tronçon de couloir où elle attend. Il n’y a rien sur la carte là où aucun pilote n’est allé, donc aucune meute ne se tient derrière les murs, au fond du labyrinthe, avant que vous n’y arriviez. Une meute n’attend pas de place : elle est sur la carte à ce même instant, quel que soit le nombre d’aliens déjà sortis. Un tronçon de couloir ne contient qu’une meute, donc le tronçon dans lequel vous volez n’a qu’une meute à affronter, et non la somme de plusieurs (un groupe de dix a plus de meutes que de tronçons, et là un tronçon en contient deux, qui sortent toutes les deux). Une meute sortie ne vous attend pas : elle traque le groupe à travers le labyrinthe, et une meute qui perd tout le monde retourne là où elle est sortie et se soigne. Une meute ne sort qu’une fois : celle que vous détruisez ne revient pas, et celle que vous quittez en volant reste sur la carte. Les vagues des zones de butin sont différentes : le donjon ne garde en l’air qu’un certain nombre d’aliens à la fois, et ce nombre grandit avec la taille du groupe, donc une vague qui le dépasserait attend de la place, et une meute que vous détruisez laisse entrer la vague suivante. Un groupe plus grand rencontre plus d’aliens, en proportion, un groupe plus petit moins, et une sorte d’alien ne descend jamais sous un.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Aliens, pour un groupe de 5 | Étape 1 | Étape 2 | Étape 3 |
| :--- | ---: | ---: | ---: |
| Dungeon Goombah | 156 | 156 | 156 |
| Dungeon Pirate | 34 | 34 | 34 |
| Dungeon Crystalys | 34 | 34 | 34 |
| Dungeon Crystalys Twin | 11 | 11 | 11 |
| Total | 235 | 235 | 235 |
| Pour ouvrir la salle du boss | 34 | 34 | 34 |
| La vague d’une zone de butin | 12 × Dungeon Goombah et 1 × Dungeon Crystalys | 12 × Dungeon Goombah et 1 × Dungeon Crystalys | 12 × Dungeon Goombah et 1 × Dungeon Crystalys |

- **La vague d’une zone de butin attend de la place** : Dès que 10 par pilote du groupe sont en vie, ou 70 en tout

<!-- dungeons-population:end -->

Chaque sorte à tour de rôle. La coque et le bouclier sont les valeurs habituelles multipliées par le facteur de l’étape de la colonne.

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Dungeon Goombah

- **Ressemble à** : Goombah
- **Vole en meutes de** : 6
- **Rapporte et lâche comme** : Goombah

|  | Étape 1 | Étape 2 | Étape 3 |
| :--- | ---: | ---: | ---: |
| Coque | 32 000 | 48 000 | 64 000 |
| Bouclier | 48 000 | 72 000 | 96 000 |
| Dégâts des lasers (une salve par seconde) | 3 000 | 4 500 | 6 000 |
| Vitesse | 180 | 180 | 180 |
| Portée des lasers | 800 | 800 | 800 |
| Rayon d’aggro | 1 800 | 1 800 | 1 800 |
| Gains et butin, multiples de l’original | ×1 | ×1,5 | ×2 |
| Crédits par destruction | 15 000 | 22 500 | 30 000 |
| Thulium par destruction | 75 | 113 | 150 |
| Expérience par destruction | 3 000 | 4 500 | 6 000 |
| Honneur par destruction | 24 | 36 | 48 |

### Dungeon Pirate

- **Ressemble à** : Pirate Boss
- **Vole en meutes de** : 2
- **Rapporte et lâche comme** : Pirate Boss
- **Roquette** : Une roquette droite toutes les 5 s, portée de 1 000 unités

|  | Étape 1 | Étape 2 | Étape 3 |
| :--- | ---: | ---: | ---: |
| Coque | 250 000 | 375 000 | 500 000 |
| Bouclier | 50 100 | 75 150 | 100 200 |
| Dégâts des lasers (une salve par seconde) | 200 | 300 | 400 |
| Dégâts de roquette | 5 000 | 7 500 | 10 000 |
| Vitesse | 110 | 110 | 110 |
| Portée des lasers | 700 | 700 | 700 |
| Rayon d’aggro | 1 800 | 1 800 | 1 800 |
| Gains et butin, multiples de l’original | ×1 | ×1,5 | ×2 |
| Crédits par destruction | 145 000 | 217 500 | 290 000 |
| Thulium par destruction | 725 | 1 088 | 1 450 |
| Expérience par destruction | 29 000 | 43 500 | 58 000 |
| Honneur par destruction | 232 | 348 | 464 |

### Dungeon Crystalys

- **Ressemble à** : Crystalys
- **Vole en meutes de** : 2
- **Rapporte et lâche comme** : Crystalys

|  | Étape 1 | Étape 2 | Étape 3 |
| :--- | ---: | ---: | ---: |
| Coque | 256 000 | 384 000 | 512 000 |
| Bouclier | 160 000 | 240 000 | 320 000 |
| Dégâts des lasers (une salve par seconde) | 10 000 | 15 000 | 20 000 |
| Vitesse | 230 | 230 | 230 |
| Portée des lasers | 900 | 900 | 900 |
| Rayon d’aggro | 2 400 | 2 400 | 2 400 |
| Gains et butin, multiples de l’original | ×1 | ×1,5 | ×2 |
| Crédits par destruction | 75 000 | 112 500 | 150 000 |
| Thulium par destruction | 200 | 300 | 400 |
| Expérience par destruction | 12 000 | 18 000 | 24 000 |
| Honneur par destruction | 52 | 78 | 104 |

### Dungeon Crystalys Twin

- **Ressemble à** : Crystalys, 1,4 fois plus grand
- **Vole en meutes de** : 1
- **Rapporte et lâche comme** : Crystalys

|  | Étape 1 | Étape 2 | Étape 3 |
| :--- | ---: | ---: | ---: |
| Coque | 512 000 | 768 000 | 1 024 000 |
| Bouclier | 320 000 | 480 000 | 640 000 |
| Dégâts des lasers (une salve par seconde) | 20 000 | 30 000 | 40 000 |
| Vitesse | 230 | 230 | 230 |
| Portée des lasers | 900 | 900 | 900 |
| Rayon d’aggro | 2 400 | 2 400 | 2 400 |
| Gains et butin, multiples de l’original | ×2 | ×3 | ×4 |
| Crédits par destruction | 150 000 | 225 000 | 300 000 |
| Thulium par destruction | 400 | 600 | 800 |
| Expérience par destruction | 24 000 | 36 000 | 48 000 |
| Honneur par destruction | 104 | 156 | 208 |

<!-- dungeons-enemies:end -->

## Le Seigneur de guerre {#the-warlord}

Le Seigneur de guerre attend dans la salle au bout du labyrinthe, et c’est sa chute qui paie la réussite. Il ne paie pas de destruction à lui seul, contrairement aux autres aliens. C’est un Crystalys devenu énorme. Sa coque et son bouclier grandissent avec la taille du groupe : plus il entre de pilotes, plus il est résistant, en proportion. Il ne quitte jamais sa salle, porte fermée ou ouverte : il reste entre les murs de la salle et ne traque pas dans les couloirs. Un pilote à l’extérieur ne peut l’attirer que jusqu’au bord de la salle, et il tire quand même par une porte ouverte sur tout ce que son laser atteint. Il utilise ses compétences une à la fois, dans un ordre aléatoire, chacune avec son propre temps de recharge.

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

La coque et le bouclier ci-dessus valent pour un groupe de 5. Ils croissent avec le groupe : ce sont la coque et le bouclier du Seigneur de guerre réunis, selon le nombre de pilotes du groupe au lancement du donjon.

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

Le sas de la salle du Seigneur de guerre est fermé dès l’ouverture du donjon, et tant qu’il l’est, le Seigneur de guerre ne peut pas être blessé  aucun laser, aucune roquette, aucune explosion ne le touche, et il n’utilise aucune compétence. Le sas s’ouvre pour de bon quand **les trois quarts des Crystalys et de leurs Twins** avec lesquels le donjon a été fait sont détruits, arrondis à l’entier supérieur (le tableau des aliens ci-dessus les compte pour un groupe de 5, et sa dernière ligne dit combien il en faut). Comptent les Crystalys et les Twins des meutes du labyrinthe, et quel que soit celui qui les détruit. Une meute ne sort que lorsqu’un pilote vole dans son tronçon de couloir : le groupe doit donc en trouver assez pour ouvrir le sas. Ne comptent pas pour le sas les autres aliens, les vagues des zones de butin, les Goombahs que le Seigneur de guerre appelle, ni le Seigneur de guerre lui-même.

La fenêtre Donjon de clan compte combien d’entre eux il reste à détruire pour ouvrir la salle et dit, dans une pastille, que le Seigneur de guerre ne peut pas être blessé, et un message vous prévient quand la salle est déverrouillée. Une meute qui n’est pas encore sortie compte en entier, le groupe doit donc trouver les Crystalys et leurs Twins dans le labyrinthe et voler dans leurs tronçons de couloir. **Les autres aliens ne disparaissent pas quand le sas s’ouvre.** Ils restent dans le labyrinthe, sortent quand un pilote vole dans leur tronçon de couloir et peuvent être détruits comme avant  un groupe qui le veut peut donc tous les détruire avant d’affronter le Seigneur de guerre, le compte d’aliens de la fenêtre va alors jusqu’à tous les aliens avec lesquels le donjon a été fait et affiche le total quand il n’en reste plus. Ils paient en tombant ([ce que paient les aliens](#what-the-aliens-pay)), et ceux qui sont encore en vie quand le Seigneur de guerre tombe partent avec le donjon. Sur la mini-carte, le sas est une ligne rouge tant qu’il est verrouillé et une ligne verte quand il est ouvert. Un donjon n’est jamais un piège : la limite de temps met quand même fin à un donjon dont le sas reste fermé, et un administrateur peut déverrouiller la salle d’un donjon bloqué.

### Ses compétences {#its-abilities}

- **L’anneau rouge** de l’Aura de vol de vie blesse tout pilote à l’intérieur et soigne le Seigneur de guerre de ces dégâts. L’Absorption de bouclier a aussi un anneau rouge : il draine les boucliers des pilotes à l’intérieur et charge celui du Seigneur de guerre. Dans les deux cas, quittez l’anneau ou mettez-vous derrière un mur.
- **Les anneaux ambrés** de la Chute de météores montrent où les météores tomberont un instant plus tard. Bougez sans cesse et sortez de l’anneau avant l’impact.
- **Focus sur le plus recherché** marque le pilote qui a infligé le plus de dégâts au Seigneur de guerre, d’un crochet doré sur son vaisseau, et le Seigneur de guerre tire sur lui un trait de plus chaque seconde tant que la compétence dure. Sa visée ne change pas : il continue de tirer sur le pilote le plus proche qu’il voit, un pilote marqué qui est aussi le plus proche prend donc les deux. Le trait supplémentaire demande une ligne dégagée et la portée du laser du Seigneur de guerre, donc un mur ou un peu de distance le sauve. Elle ne démarre pas tant que personne n’a infligé de dégâts.
- **La Salve de roquettes** lance des roquettes à tête chercheuse sur des pilotes au hasard, mais seulement sur des pilotes que le Seigneur de guerre peut voir, et un mur sur le chemin arrête une roquette. Un anneau montre quel pilote une roquette suit. Une EMP Charge ou une occultation les fait lâcher prise.
- **Le Renfort d’essaim** est le Seigneur de guerre qui appelle ses Goombahs. Tant qu’ils vivent, il ne peut pas être blessé, et il ne tire pas et n’utilise aucune autre compétence. Détruisez-les tous : la bannière compte combien il en reste. Si une minute passe, le Seigneur de guerre peut de nouveau être blessé et les Goombahs qui restent continuent le combat. Ils ne comptent pas pour la salle du boss, et ils ne paient rien.
- **La Zone du Chaos** est un anneau violet au sol, autour du Seigneur de guerre, et tant qu’elle dure, il va partout où va le Seigneur de guerre. Personne dans l’anneau ne peut attaquer, ni avec des lasers ni avec des roquettes, mais les réparations, l’occultation et le vol fonctionnent toujours, et le Seigneur de guerre et ses aliens tirent comme toujours. L’anneau apparaît un instant avant de faire effet  sortez-en et restez dehors, car il suit le Seigneur de guerre. Un pilote à l’extérieur peut toujours tirer, aussi loin que portent ses armes.

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
| **Salve de roquettes** | 26 000 par roquette, une toutes les 15 s | 32 500 par roquette, une toutes les 15 s | 39 000 par roquette, une toutes les 15 s |
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

Aux étapes 2 et 3, le groupe gagne des boosters en détruisant les aliens du donjon. Un booster tombe à chaque dixième d’entre eux  quand un dixième des aliens est détruit, puis deux dixièmes, et ainsi de suite jusqu’à tous, dix chutes en tout. Chaque alien avec lequel le donjon a été fait compte, quel que soit celui qui le détruit (c’est le compte des aliens détruits de la fenêtre Donjon de clan)  les vagues des zones de butin et les aliens que le Seigneur de guerre appelle ne comptent pas, donc une zone n’apporte aucun booster. À chaque chute, chaque pilote reçoit une fenêtre d’une demi-minute pour choisir un booster temporaire pour lui-même parmi trois que le jeu tire au hasard sur cinq  **Dégâts** (vos lasers frappent plus fort), **Points de vie** (votre vaisseau tient plus de coque), **Bouclier** (votre bouclier tient plus), **Vitesse** (votre vaisseau vole plus vite) et **Recharge bouclier** (votre bouclier se recharge plus vite). Appuyez sur une carte pour la choisir. Si vous ne répondez pas à temps, le jeu choisit Points de vie pour vous, ou le premier des trois si Points de vie n’en fait pas partie. Un choix vaut 3 % à l’étape 3 et 1,5 % à l’étape 2, donc dix choix s’additionnent jusqu’à trente pour cent au plus à l’étape 3 et quinze pour cent à l’étape 2, quels que soient les types. L’étape 1 n’a pas de boosters.

La dixième chute vient avec le dernier alien. Un groupe qui détruit tous les aliens avant d’affronter le Seigneur de guerre obtient les dix chutes  un groupe qui ouvre la salle du Seigneur de guerre et poursuit sa route obtient les chutes des aliens qu’il a détruits d’ici là, et les aliens qui restent restent et peuvent encore être détruits. Une fois le combat contre le Seigneur de guerre commencé, plus aucun booster ne tombe.

Un booster dure jusqu’à ce que le donjon soit terminé. Si vous quittez le donjon, ou si vous êtes détruit, vous perdez vos boosters, et vous les retrouvez quand vous revolez dedans. Une pastille sous la fenêtre Donjon de clan liste ce que vous avez.

### Les cartes {#the-cards}

Les cartes sont tirées une à une dans la réserve ci-dessous. La chance est celle d’une carte lors d’un tirage. Chaque carte va à chaque pilote payé, les cartes d’équipement aussi : une carte à nombreux exemplaires en donne autant à chacun, et une carte d’équipement donne à chacun une pièce à lui, forgée pour lui. Un pilote qui n’est pas payé ne reçoit pas de carte non plus, et une zone ouverte dans un donjon qui échoue ne paie rien.

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
| Dark Matter | 10 | 16 | 24 | 9,1 % | Chaque pilote payé |
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

Les cartes à un seul exemplaire sont de l’**équipement**, et seul un donjon d’étape 3 peut en proposer. Une pièce d’équipement est forgée pour chaque pilote payé au moment du paiement : chacun tire son propre [rang d’enchantement](/wiki/06-Items/Overview.md#item-enchants) avec les mêmes chances qu’une pièce que vous fabriquez à l’Assemblage, la plupart sortent donc Standard, et un rang plus élevé, jusqu’à Éternel, avec des bonus, est une trouvaille rare.

## Paie {#pay}

À la chute du Seigneur de guerre, tout pilote qui l’a mérité est payé, une fois par partie. Les cartes choisies par le groupe s’ajoutent à la paie de l’étape. Il n’y a pas de multiplicateur de monde : la paie est la même dans tous les mondes.

Les **Orvium Reinforced Plates** ne sont pas une carte du vote. Elles font partie de la paie de l’étape, et chaque pilote payé les reçoit une fois pour la réussite. Les objets que paie la réussite ne sont pas vendables : vous ne pouvez pas [les vendre aux Enchères](/wiki/03-Mechanics/Auction.md#marketable-items).

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Étape | Honneur | Expérience | Crédits | Thulium | Munitions x4 | Orvium Reinforced Plates | Points de classement PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Étape 1** | 25 000 | 600 000 | 5 000 000 | 4 000 | 4 000 | 5 | 600 |
| **Étape 2** | 50 000 | 1 500 000 | 10 000 000 | 9 000 | 9 000 | 10 | 1 500 |
| **Étape 3** | 100 000 | 2 400 000 | 17 500 000 | 15 000 | 15 000 | 15 | 2 400 |

<!-- dungeons-pay:end -->

### Qui est payé {#who-is-paid}

Ces règles décident qui est payé **pour la réussite**. Une partie se joue en entier même quand elle ne paie rien, et l’écran de résultat dit pourquoi. L’entrée n’est jamais refusée parce que vous avez déjà été payé pour une étape : la réussite ne paie simplement rien. Les aliens lisent les mêmes règles, destruction par destruction, sauf la part au combat ([ce que paient les aliens](#what-the-aliens-pay)).

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Un jour** : Une étape paie un pilote une fois par jour UTC : le jour où le Seigneur de guerre tombe
- **Une semaine** : Un pilote est payé pour un maximum de 10 étapes terminées par semaine UTC, du lundi au dimanche
- **À l’intérieur** : Au moins 2 min en tout
- **Part au combat** : Au moins l’un de ceux-ci : a infligé 2 % de la coque et du bouclier du Seigneur de guerre; a détruit 10 aliens du donjon; a soigné d’autres pilotes à hauteur de 50 000 pendant le combat contre le Seigneur de guerre

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

### Ce que paient les aliens {#what-the-aliens-pay}

Chaque alien d’un donjon paie en tombant, et lâche du butin, comme l’alien du jeu dont il s’inspire : un Dungeon Goombah comme un [Goombah](/wiki/04-Aliens/Goombah.md), un Dungeon Crystalys et son Twin comme un [Crystalys](/wiki/04-Aliens/Crystalys.md), un Dungeon Pirate comme le Pirate Boss de l’[Essaim Pirate](/wiki/05-Swarms/Pirate-Swarm.md). Ce que paie et lâche une destruction est ce que paie et lâche l’original, **multiplié par le rapport de leur coque et de leur bouclier réunis** : un alien aussi résistant que son original paie ce que paie l’original, un alien deux fois plus résistant paie deux fois plus et lâche deux fois plus de chaque objet, et ainsi de suite. La section de chaque sorte d’alien sous [Les aliens](#the-aliens) donne le rapport et la paie d’une destruction à chaque étape.

- **Qui est payé.** Les pilotes qui ont blessé l’alien, selon les dégâts infligés, comme pour les aliens des essaims : un pilote ou un groupe qui l’a seulement effleuré ne reçoit rien, un groupe est payé comme un seul, et dans un groupe les membres proches de l’épave qui ont tiré récemment se partagent la paie selon leur niveau. Un pilote qui n’a infligé aucun dégât à l’alien ne reçoit rien pour lui, même s’il volait tout près, et un alien qu’aucun pilote n’a blessé ne paie personne. Seuls entrent les pilotes que les règles ci-dessus paient. Celui qui est parti, qui n’est pas resté assez longtemps, qui a déjà été payé pour l’étape aujourd’hui ou qui a eu toutes les réussites payées de la semaine ne reçoit rien pour les aliens, et les autres ont sa part. Une destruction ne demande pas la part au combat, car avoir blessé l’alien en est la part. Si le membre d’un groupe qui a infligé le plus de dégâts a été détruit ou n’est plus sur la carte, les membres proches de l’épave qui ont tiré récemment se partagent la paie sans lui.
- **Ce qui est payé.** Crédits, Thulium, expérience et honneur, une fois par destruction. La paie est celle de l’original en Alpha, dans tous les mondes : un donjon n’a pas de multiplicateur de monde. Vos boosters, Premium, formation et les bonus de votre clan comptent comme pour toute destruction, et l’expérience compte pour vos [points PvE](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points) comme celle de la réussite.
- **Le butin.** Il est tiré avec les chances de l’original, puis chaque quantité est multipliée par le rapport (une fraction d’unité est une chance d’en avoir une de plus). Il tombe dans une caisse sur l’épave, d’abord pour le pilote qui a infligé le plus de dégâts et son clan, puis pour n’importe qui sur la carte, et ensuite il disparaît. La carte ne tient qu’un certain nombre de caisses à la fois : ramassez-les au fil du combat, et ce qui reste sur la carte à la fermeture du donjon part avec lui. Contrairement aux objets de la réussite, ce sont des butins ordinaires d’alien : on peut les [vendre aux Enchères](/wiki/03-Mechanics/Auction.md#marketable-items) quand l’objet est vendable.
- **Ce qui ne paie pas.** Le Seigneur de guerre ne paie pas de destruction, seulement la réussite. Les Goombahs qu’il appelle ne paient rien, car l’appel revient tant que le combat dure.
- **Pas une destruction du jeu.** Une destruction dans un donjon ne compte ni pour les quêtes, ni pour les succès, ni pour les compteurs de destructions, ni pour les points de réinitialisation, ni pour les points PvE d’une destruction, ni pour les drones ou les P.E.T.s : un Dungeon Goombah n’est pas un Goombah du jeu.
- **Les limites.** Les limites du jour et de la semaine ci-dessus retiennent la paie des aliens comme celle de la réussite. Un pilote déjà payé pour l’étape aujourd’hui, ou qui a eu toutes les réussites payées de la semaine, ne reçoit rien non plus pour ses aliens, et la cagnotte d’une destruction va aux autres. Un donjon qui n’est pas réussi paie ses destructions aux pilotes que les règles paient, et rien pour la réussite.

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
- **Pilotes payés** : Au moins 3 dans le donjon

<!-- dungeons-clan:end -->

## Conseils {#tips}

- Éliminez la vague d’une zone avant d’essayer de la tenir, et battez-vous dans l’anneau si des aliens y entrent.
- Amenez tout le groupe dans une zone : plus il y a de pilotes dans l’anneau, plus vite elle est tenue.
- Cherchez les Crystalys et leurs Twins dans le labyrinthe  le sas du Seigneur de guerre s’ouvre quand les trois quarts d’entre eux sont morts, et pas avant. Les autres aliens peuvent attendre, ou être détruits aussi.
- Servez-vous des murs : les lasers ne les traversent pas, les anneaux rouges des auras du Seigneur de guerre s’y arrêtent, et un mur arrête aussi ses roquettes.
- Gardez une EMP Charge pour la Salve de roquettes.
- Quand le Seigneur de guerre appelle ses Goombahs, détruisez-les d’abord : il ne peut pas être blessé tant qu’ils ne sont pas partis. Dans la Zone du Chaos, sortez de l’anneau avant de tirer.
- Surveillez l’horloge de la fenêtre Donjon de clan. Quand le temps est écoulé, le donjon échoue et la réussite ne paie rien.
