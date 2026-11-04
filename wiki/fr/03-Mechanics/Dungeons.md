<!-- wiki-i18n source: a3ead40fe6402d78 -->
<!-- wiki-i18n title: Donjons -->
# Donjons {#dungeons}

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; donjon; donjons; porte; portes; seigneur de guerre; labyrinthe; étape; zone de butin; carte -->

Un **donjon** est ce que le jeu appelle une **porte** : un labyrinthe fermé avec un **Seigneur de guerre** au bout. Un chef adjoint ou le chef d’un [clan](/wiki/03-Mechanics/Clans.md) en ouvre une et la paie avec la banque du clan, et les membres du clan y volent ensemble en un seul [groupe](/wiki/03-Mechanics/Groups.md). Ils se frayent un chemin parmi les aliens du labyrinthe, ouvrent des zones de butin pour choisir une carte dans chacune, et abattent le Seigneur de guerre. Tout pilote qui a pris part au combat est payé à la chute du Seigneur de guerre, dans les limites plus bas. Les portes se trouvent dans l’onglet **Portes** de la page du clan.

Une porte est un combat contre les aliens uniquement : personne ne peut y attaquer un camarade de clan, ni qui que ce soit d’autre. Les aliens ne paient rien. La paie vient du seul Seigneur de guerre, donc la seule façon d’être payé est d’être dans le combat quand il tombe.

## En un coup d’œil {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Ouverture** : À partir du jour 4 de la saison
- **Qui ouvre une porte** : Un chef adjoint ou le chef, qui paie le prix avec la banque du clan
- **Groupe** : De 4 à 10 membres du clan, dans un même groupe
- **Portes par jour** : 3 par clan et par jour UTC, une seule ouverte à la fois
- **Portes en même temps** : 6 dans un monde
- **Cartes** : Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Labyrinthes** : 8 ; l’une est tirée à l’ouverture d’une porte
- **Rassemblement** : 10 min pour se rassembler et lancer. Une porte que personne ne lance se ferme, et son prix retourne à la banque du clan
- **Limite de temps** : Étape 1: 80 min, Étape 2: 110 min, Étape 3: 150 min à partir du lancement. Si le temps s’écoule, la porte échoue et ne paie rien
- **Laissée vide** : Une porte où personne ne reste pendant 3 min échoue
- **Après la chute du Seigneur de guerre** : La porte reste ouverte 2 min pour les pilotes à l’intérieur
- **Retour** : Un pilote qui est parti ou a été détruit peut revenir 3 fois, avec 20 s d’écart

<!-- dungeons-glance:end -->

## Le déroulement {#how-a-run-goes}

1. **Invoquer.** Dans l’onglet Portes, un [chef adjoint ou le chef](/wiki/03-Mechanics/Clans.md#hierarchy-roles) choisit une étape et appuie sur **Invoquer**. Le prix est prélevé sur la [banque du clan](/wiki/03-Mechanics/Clans.md#clan-economy-taxation), et la porte prend l’une des cartes listées plus haut. Une porte que personne ne lance se ferme, et le prix retourne à la banque.
2. **Entrer.** Les membres du clan appuient sur **Entrer** dans la fenêtre du Clan pendant qu’ils volent. Les pilotes à l’intérieur forment le groupe de la porte.
3. **Lancer.** Le pilote qui a ouvert la porte, ou un officier, appuie sur **Lancer** quand assez de pilotes sont à l’intérieur. Ensuite, seuls les pilotes qui étaient déjà à l’intérieur peuvent revenir.
4. **Traverser le labyrinthe.** Vous entrez à une extrémité du labyrinthe et le Seigneur de guerre attend à l’autre. Les aliens dorment dans leurs salles et se réveillent en meutes quand le groupe approche.
5. **Ouvrir les zones de butin.** Des anneaux dans le labyrinthe marquent les zones. Tenez-en une et le groupe vote pour une carte, qui est versée avec la paie du Seigneur de guerre.
6. **Vaincre le Seigneur de guerre.** Brisez son bouclier et sa coque, et répondez à ses compétences. Quand il tombe, la porte est terminée.
7. **Être payé.** La paie arrive à l’instant où le Seigneur de guerre tombe. La porte reste ouverte un peu plus longtemps pour les pilotes à l’intérieur, puis se ferme.

## Entrer {#entering}

Pour entrer dans une porte, il vous faut un **vaisseau en vol**, donc décollez d’abord puis ouvrez la fenêtre du Clan, et un [groupe](/wiki/03-Mechanics/Groups.md) comptant assez de membres du clan. Il vous faut aussi le **niveau** que demande l’étape, et vous ne pouvez pas être déjà dans une autre porte. Le groupe d’une porte a une taille limite : une fois plein, personne d’autre ne peut entrer.

Un chef adjoint ou le chef ouvre une porte, une seule à la fois pour le clan, et seulement jusqu’au nombre de portes par jour. La banque du clan doit avoir le prix. Un clan ne peut ouvrir une étape qu’après avoir terminé la précédente.

Dans une porte, vous ne pouvez pas changer de monde, et la Jump CPU et la Base CPU ne fonctionnent pas. Le bouton **Quitter** de la barre de la porte vous fait sortir après confirmation. Un pilote qui est parti, ou qui a été détruit, peut revenir quelques fois, avec une courte attente entre deux.

## Les étapes {#the-stages}

Une porte a une étape, et l’étape est sa difficulté. Une étape plus élevée a des aliens plus résistants qui frappent plus fort, et elle paie plus. Les multiplicateurs du tableau s’appliquent à chaque alien et au Seigneur de guerre. Les dégâts désignent les lasers, les roquettes et les compétences du Seigneur de guerre. Le tableau indique aussi combien d’aliens une étape envoie par rapport à la première. Le **prix** est prélevé sur la banque du clan à l’ouverture de la porte.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Étape | Prérequis | Coque et bouclier des aliens | Nombre d’aliens | Dégâts des aliens | Prix de la porte (crédits, prélevés sur la banque du clan) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Étape 1** | À partir du niveau 6 | ×1 | ×1 | ×1 | 500 000 |
| **Étape 2** | À partir du niveau 7 | ×1,5 | ×1 | ×1,25 | 1 000 000 |
| **Étape 3** | À partir du niveau 8 | ×2,5 | ×1 | ×1,5 | 2 000 000 |

<!-- dungeons-stages:end -->

## Le labyrinthe {#the-maze}

Chaque porte est un labyrinthe fermé sur une carte à elle, l’une des cartes de la liste plus haut, et le labyrinthe est l’un de plusieurs plans. Un labyrinthe est une grille de salles et de couloirs aux murs pleins. Les vaisseaux ne peuvent pas traverser un mur, et un mur arrête les tirs, c’est donc un abri. Un météore tombe d’en haut, et un mur ne l’arrête pas.

## Les aliens {#the-aliens}

Quatre sortes d’aliens gardent le labyrinthe. Ils dorment dans leurs salles et se réveillent quand un pilote approche. La porte ne garde qu’un certain nombre d’aliens en l’air à la fois, et ce nombre grandit avec la taille du groupe, si bien qu’une meute que vous détruisez laisse entrer la suivante. Un groupe plus grand rencontre plus d’aliens en proportion, un plus petit moins, et une sorte d’alien ne tombe jamais sous un.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Aliens, pour un groupe de 5 | Étape 1 | Étape 2 | Étape 3 |
| :--- | ---: | ---: | ---: |
| Gate Goombah | 130 | 130 | 130 |
| Gate Pirate | 28 | 28 | 28 |
| Gate Crystalys | 28 | 28 | 28 |
| Gate Crystalys Twin | 9 | 9 | 9 |
| Total | 195 | 195 | 195 |
| La vague d’une zone de butin | 10 × Gate Goombah et 1 × Gate Crystalys | 10 × Gate Goombah et 1 × Gate Crystalys | 10 × Gate Goombah et 1 × Gate Crystalys |

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
| Coque | 32 000 | 48 000 | 80 000 |
| Bouclier | 48 000 | 72 000 | 120 000 |
| Dégâts des lasers (une salve par seconde) | 3 000 | 3 750 | 4 500 |
| Vitesse | 180 | 180 | 180 |
| Portée des lasers | 800 | 800 | 800 |
| Rayon d’aggro | 1 800 | 1 800 | 1 800 |

### Gate Pirate

- **Ressemble à** : Pirate Boss
- **Vole en meutes de** : 2
- **Roquette** : Une roquette droite toutes les 5 s, portée de 970 unités

|  | Étape 1 | Étape 2 | Étape 3 |
| :--- | ---: | ---: | ---: |
| Coque | 300 000 | 450 000 | 750 000 |
| Bouclier | 50 100 | 75 150 | 125 250 |
| Dégâts des lasers (une salve par seconde) | 200 | 250 | 300 |
| Dégâts de roquette | 5 000 | 6 250 | 7 500 |
| Vitesse | 92 | 92 | 92 |
| Portée des lasers | 700 | 700 | 700 |
| Rayon d’aggro | 1 800 | 1 800 | 1 800 |

### Gate Crystalys

- **Ressemble à** : Crystalys
- **Vole en meutes de** : 2

|  | Étape 1 | Étape 2 | Étape 3 |
| :--- | ---: | ---: | ---: |
| Coque | 256 000 | 384 000 | 640 000 |
| Bouclier | 160 000 | 240 000 | 400 000 |
| Dégâts des lasers (une salve par seconde) | 10 000 | 12 500 | 15 000 |
| Vitesse | 230 | 230 | 230 |
| Portée des lasers | 900 | 900 | 900 |
| Rayon d’aggro | 2 400 | 2 400 | 2 400 |

### Gate Crystalys Twin

- **Ressemble à** : Crystalys, 1,4 fois plus grand
- **Vole en meutes de** : 1

|  | Étape 1 | Étape 2 | Étape 3 |
| :--- | ---: | ---: | ---: |
| Coque | 512 000 | 768 000 | 1 280 000 |
| Bouclier | 320 000 | 480 000 | 800 000 |
| Dégâts des lasers (une salve par seconde) | 20 000 | 25 000 | 30 000 |
| Vitesse | 230 | 230 | 230 |
| Portée des lasers | 900 | 900 | 900 |
| Rayon d’aggro | 2 400 | 2 400 | 2 400 |

<!-- dungeons-enemies:end -->

## Le Seigneur de guerre {#the-warlord}

Le Seigneur de guerre attend dans la salle au bout du labyrinthe, et c’est la seule chose d’une porte qui paie. C’est un Crystalys devenu immense. Sa coque et son bouclier grandissent avec la taille du groupe : plus il entre de pilotes, plus il est résistant, en proportion. Il reste dans sa salle et utilise ses compétences une à la fois, dans un ordre aléatoire, chacune avec son propre temps de recharge.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Ressemble à** : Crystalys, 3 fois plus grand
- **Recharge du bouclier** : 3 000 par seconde, après 15 s sans dégâts

|  | Étape 1 | Étape 2 | Étape 3 |
| :--- | ---: | ---: | ---: |
| Coque | 10 000 000 | 15 000 000 | 25 000 000 |
| Bouclier | 8 000 000 | 12 000 000 | 20 000 000 |
| Dégâts des lasers (une salve par seconde) | 8 000 | 10 000 | 12 000 |
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

### Ses compétences {#its-abilities}

- **L’anneau rouge** de l’Aura de vol de vie blesse tout pilote à l’intérieur et soigne le Seigneur de guerre de ces dégâts. L’Absorption de bouclier a aussi un anneau rouge : il draine les boucliers des pilotes à l’intérieur et charge celui du Seigneur de guerre. Dans les deux cas, quittez l’anneau ou mettez-vous derrière un mur.
- **Les anneaux ambrés** de la Chute de météores montrent où les météores tomberont un instant plus tard. Bougez sans cesse et sortez de l’anneau avant l’impact.
- **Cible : les soigneurs** retourne le Seigneur de guerre contre quiconque soigne un autre pilote, et il frappe ce pilote plus fort. Répartissez les soins.
- **La Salve de roquettes** envoie des roquettes à tête chercheuse sur des pilotes au hasard. Une EMP Charge ou une occultation les fait lâcher prise.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Compétence | Préparation | Durée | Temps de recharge | Rayon de l’anneau (unités) | Le Seigneur de guerre regagne, au plus |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Aura de vol de vie** | 2 s | 15 s | 2 min | 900 | 8 % de sa coque et de son bouclier |
| **Chute de météores** | 1,5 s | 3 salves, espacées de 4 s | 2 min | 420 | – |
| **Cible : les soigneurs** | 1 s | 45 s | 2 min | – | – |
| **Salve de roquettes** | 1,5 s | 45 s | 2 min | – | – |
| **Absorption de bouclier** | 2 s | 15 s | 2 min | 900 | 6 % de son bouclier |

| Compétence | Étape 1 | Étape 2 | Étape 3 |
| :--- | :--- | :--- | :--- |
| **Aura de vol de vie** | 8 000 par seconde | 10 000 par seconde | 12 000 par seconde |
| **Chute de météores** | 6 météores par salve, 40 000 chacun | 8 météores par salve, 50 000 chacun | 10 météores par salve, 60 000 chacun |
| **Cible : les soigneurs** | Son laser frappe ×1,5 plus fort le pilote sur lequel il se tourne | Son laser frappe ×1,5 plus fort le pilote sur lequel il se tourne | Son laser frappe ×1,5 plus fort le pilote sur lequel il se tourne |
| **Salve de roquettes** | 6 500 par roquette, une toutes les 15 s | 8 125 par roquette, une toutes les 15 s | 9 750 par roquette, une toutes les 15 s |
| **Absorption de bouclier** | 10 000 de bouclier par seconde | 12 500 de bouclier par seconde | 15 000 de bouclier par seconde |

<!-- dungeons-abilities:end -->

## Zones de butin {#loot-zones}

Un anneau au sol du labyrinthe marque chaque zone de butin dès que le groupe l’a trouvée. Restez un moment à l’intérieur et la zone se réveille, et une vague d’aliens arrive dessus. Le groupe doit alors **tenir** la zone : garder un pilote à l’intérieur jusqu’à ce que la jauge soit pleine. Les aliens dans l’anneau arrêtent la jauge, et elle recule tant que personne n’est à l’intérieur, donc éliminez d’abord la vague. Quand la zone s’ouvre, le groupe voit trois cartes différentes et **vote** pour l’une d’elles. Une zone s’ouvre une seule fois, et sa vague ne revient pas.

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Zones de butin** : 4 dans chaque labyrinthe
- **Rayon** : 450 unités
- **Réveil** : Restez 2 s à l’intérieur de l’anneau
- **Tenue** : Gardez un pilote à l’intérieur pendant 30 s. La jauge s’arrête tant que 3 aliens ou plus sont dans l’anneau, et recule tant que personne n’y est
- **Choix** : Le groupe a 45 s pour voter. Le vote se termine plus tôt si tous les pilotes présents ont voté ou si une carte a plus de la moitié des voix

<!-- dungeons-zones:end -->

### Les cartes {#the-cards}

Les cartes sont tirées une à une dans la réserve ci-dessous. La chance est celle d’une carte lors d’un tirage. Une carte à nombreux exemplaires va à chaque pilote payé, et une carte d’équipement, à un seul exemplaire, va à un pilote du groupe. Un pilote qui n’est pas payé ne reçoit pas de carte non plus, et une zone ouverte dans une porte qui échoue ne paie rien.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Carte | Étape 1 | Étape 2 | Étape 3 | Chance | Revient à |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2 000 | 3 000 | 5 000 | 21 % | Chaque pilote payé |
| Velkonite Reinforced Plate | 10 | 15 | 25 | 12 % | Chaque pilote payé |
| Orvium Reinforced Plate | 10 | 15 | 25 | 12 % | Chaque pilote payé |
| Velkonite | 200 | 300 | 500 | 12 % | Chaque pilote payé |
| Orvium | 200 | 300 | 500 | 12 % | Chaque pilote payé |
| Ultra Core | 5 000 | 7 500 | 12 500 | 10 % | Chaque pilote payé |
| Experimental Fusion Core | 3 000 | 4 500 | 7 500 | 8 % | Chaque pilote payé |
| Dark Matter | 5 | 8 | 12 | 8 % | Chaque pilote payé |
| Dark Matter Plate | 1 | 1 | 2 | 4 % | Chaque pilote payé |
| Engine III | 1 | 1 | 1 | 0,25 % | Un pilote du groupe |
| Heavy Shield Core | 1 | 1 | 1 | 0,25 % | Un pilote du groupe |
| Adaptive Core III | 1 | 1 | 1 | 0,25 % | Un pilote du groupe |
| Starfire-III | 1 | 1 | 1 | 0,25 % | Un pilote du groupe |

- **Équipement** : Les cartes à un seul exemplaire sont de l’équipement : ensemble 1 % des cartes

<!-- dungeons-cards:end -->

## Paie {#pay}

À la chute du Seigneur de guerre, tout pilote qui l’a mérité est payé, une fois par partie. Les cartes choisies par le groupe s’ajoutent à la paie de l’étape. Il n’y a pas de multiplicateur de monde : la paie est la même dans tous les mondes.

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Étape | Honneur | Expérience | Crédits | Thulium | Munitions x4 | Points de classement PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| **Étape 1** | 25 000 | 600 000 | 5 000 000 | 4 000 | 4 000 | 600 |
| **Étape 2** | 50 000 | 1 500 000 | 10 000 000 | 9 000 | 9 000 | 1 500 |
| **Étape 3** | 100 000 | 2 400 000 | 17 500 000 | 15 000 | 15 000 | 2 400 |

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

| Paie de chaque pilote | Honneur | Expérience | Crédits | Thulium | Munitions x4 | Points de classement PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Un jour, chaque étape une fois | 175 000 | 4 500 000 | 32 500 000 | 28 000 | 28 000 | 4 500 |
| La meilleure semaine : 7 × Étape 3 et 3 × Étape 2 | 850 000 | 21 300 000 | 152 500 000 | 132 000 | 132 000 | 21 300 |

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
- Servez-vous des murs : les lasers ne les traversent pas, et les anneaux du Seigneur de guerre s’y arrêtent.
- Gardez une EMP Charge pour la Salve de roquettes.
- Surveillez l’horloge de la barre de la porte. Quand le temps est écoulé, la porte échoue et ne paie rien.
