<!-- wiki-i18n source: 0d92c80e748fc9b8 -->
<!-- wiki-i18n title: Aptitudes de pilote -->
# Aptitudes de pilote {#pilot-skills}

<!-- wiki-search: skills; skill tree; pilot skill tree; pilot skills; skill xp; xp; level up; stats; attributes; heft; grit; reflex; instinct; laser tech; rocket tech; antimatter; marksmanship; sabotage; evasion; tactics; radiation tech; thruster theory; science; extraction; logistics; fabrication; commerce; soft cap; hold; training; day one; pilot button; pilot page; buffs; aptitudes; aptitudes de pilote; arbre d’aptitudes; expérience; monter de niveau; statistiques; attributs; masse; ténacité; réflexes; instinct; technique laser; technique des roquettes; antimatière; précision de tir; esquive; tactique; technique anti-radiations; théorie des propulseurs; commerce; plafond horaire; soute -->

Votre pilote a un **arbre d’aptitudes** : un ensemble de statistiques qui montent de niveau selon ce que vous faites. Combattez, et votre Technique laser et votre Ténacité montent ; collectez dans votre Skylab, et votre Extraction monte. Chaque niveau donne un petit bonus permanent à quelque chose que vous faites déjà, et rien n’est dépensé ni choisi : il n’y a aucun point à répartir et rien à réinitialiser. Vous faites monter ce que vous utilisez.

L’arbre est **à vous**, pas à un vaisseau. Chaque vaisseau que vous pilotez a vos niveaux, celui que vous achèterez demain aussi, et les niveaux sont conservés à travers chaque réinitialisation ([ce qui est conservé](#what-is-kept)).

Un nouveau pilote n’est pas à pleine puissance. Au niveau 1, un laser et une roquette font moins de dégâts que ne l’indiquent les pages d’objets, et la Technique laser et la Technique des roquettes les portent au-delà des chiffres indiqués à mesure qu’elles montent. Chaque chiffre des pages d’objets est celui de l’objet lui-même, avant vos aptitudes.

## En un coup d’œil {#at-a-glance}

<!-- skills-glance:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

- **Statistiques** : 19 statistiques : 4 attributs et 15 aptitudes en 5 groupes
- **Niveaux** : De 1 à 100. Chaque pilote commence chaque statistique au niveau 1, et il n’y a rien à dépenser ni à réinitialiser
- **Coût d’un niveau** : 40 XP du niveau 1 au 2, 875 XP du niveau 50 au 51, 19 157 XP du niveau 99 au 100 ; 313 258 XP en tout
- **Ce que donne un niveau** : Un bonus croît en ligne droite de sa valeur au niveau 1 à sa valeur au niveau 100. Rien n’est plafonné
- **Votre laser au niveau 1** : Il fait 100 % de ses dégâts et touche 80 % du temps, soit 80 % des dégâts qu’indiquent les pages d’objets
- **Votre roquette au niveau 1** : Elle fait 100 % de ses dégâts et est un raté 10 % du temps, soit 90 % des dégâts qu’indiquent les pages d’objets
- **Esquive** : Le vaisseau de chaque pilote esquive 3 % des coups qui peuvent être esquivés, avant qu’aucune aptitude ou formation n’y ajoute
- **Niveau de coque** : La rareté de votre vaisseau le fixe, comme le montre le tableau ci-dessous. La taille de votre soute et l’XP de la Masse le suivent
- **Soute** : Elle compte les unités de ressources que vous ramassez après le lancement, jusqu’à la taille que lui donne son niveau de coque. Elle est pleine à partir de 90 % de cela, et une soute pleine fait payer la Masse ×1,5. Rien n’est jamais refusé
- **Plafond horaire souple** : La plupart des statistiques ne paient l’XP entière que jusqu’à un plafond par heure, compté dans l’unité propre de la statistique sur l’heure d’horloge UTC. Au-delà, un événement paie 25 % de son XP
- **Entraînement** : L’XP d’une aptitude verse aussi 10 % d’elle-même à son attribut. Un attribut au niveau 100 entraîne ses aptitudes 25 % plus vite qu’au niveau 1

| Niveau de coque | Rareté du vaisseau | Taille de la soute |
| :--- | :--- | ---: |
| 1 | Médiocre / Commun | 60 |
| 2 | Peu commun | 120 |
| 3 | Rare | 250 |
| 4 | Épique | 500 |
| 5 | Mythique / Légendaire / Éternel | 1 000 |

<!-- skills-glance:end -->

## Les statistiques {#the-stats}

Les statistiques sont de deux sortes. Les **attributs** (Masse, Ténacité, Réflexes et Instinct) sont les bases d’un pilote. Les **aptitudes** sont réparties en cinq groupes, et chaque aptitude est régie par un attribut, que les tableaux nomment entre parenthèses : l’XP d’une aptitude nourrit aussi son attribut, et un attribut élevé entraîne plus vite ses aptitudes ([comment l’XP est payée](#how-xp-is-paid)). Les noms sont ceux de la page Aptitudes de pilote du jeu.

Les tableaux donnent chaque bonus au niveau 1 et au dernier niveau ; entre les deux, un bonus croît en ligne droite. Un **facteur** multiplie un nombre : au-dessus de 1 il l’augmente, en dessous de 1 il le réduit. La plupart des bonus changent un chiffre de votre vaisseau, et l’infobulle d’un chiffre qu’une aptitude a modifié a une ligne qui dit quelle part vient de vos aptitudes.

<!-- skills-buffs:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

### Attributs {#attributes}

| Statistique | Ce qu’elle change | Niveau 1 | Niveau 100 |
| :--- | :--- | ---: | ---: |
| **Masse** | Coque | +0 % | +20 % |
| **Ténacité** | Dégâts subis | ×1 | ×0,92 |
| **Réflexes** | Vitesse de recharge des compétences | ×1 | ×1,1 |
| **Instinct** | Chance de chaque ligne de butin | +0 points | +7,5 points |
|  | Orvium et Velkonite des collecteurs | ×1 | ×1,5 |

### Armes {#weapons}

| Statistique | Ce qu’elle change | Niveau 1 | Niveau 100 |
| :--- | :--- | ---: | ---: |
| **Technique laser** (Réflexes) | Dégâts laser | ×1 | ×1,3 |
|  | Chance qu’une salve laser touche | 80 % | 89 % |
| **Technique des roquettes** (Réflexes) | Dégâts de roquette | ×1 | ×1,3 |
|  | Chance qu’une roquette soit un raté | 10 % | 1 % |
| **Antimatière** (Instinct) | Dark Matter des ramassages | ×1 | ×1,25 |

### Combat

| Statistique | Ce qu’elle change | Niveau 1 | Niveau 100 |
| :--- | :--- | ---: | ---: |
| **Précision de tir** (Réflexes) | Portée du lancer d’une Mine | ×1 | ×1,15 |
|  | Vitesse d’une Mine lancée | ×1 | ×1,15 |
| **Sabotage** (Réflexes) | Dégâts des poisons et des Mines | ×1 | ×1,3 |
|  | Durée des poisons | ×1 | ×1,2 |
| **Esquive** (Réflexes) | Chance d’esquiver un coup, ajoutée à celle du vaisseau | 0 % | 15 % |
| **Tactique** (Réflexes) | Durée des compétences | ×1 | ×1,2 |
| **Absorption du bouclier** (Ténacité) | Absorption de vos boucliers | +0 points | +5 points |

### Pilotage {#ship-control}

| Statistique | Ce qu’elle change | Niveau 1 | Niveau 100 |
| :--- | :--- | ---: | ---: |
| **Technique anti-radiations** (Ténacité) | Dose de radiation | ×1 | ×0,4 |
| **Théorie des propulseurs** (Masse) | Vitesse | +0 % | +10 % |
| **Science** (Instinct) | Science par unité de carburant | ×1 | ×1,25 |

### Skylab

| Statistique | Ce qu’elle change | Niveau 1 | Niveau 100 |
| :--- | :--- | ---: | ---: |
| **Extraction** (Instinct) | Ce que produit le Skylab | ×1 | ×1,3 |
| **Logistique** (Masse) | Ce que contient la banque de l’Entrepôt de ressources | ×1 | ×1,4 |
| **Fabrication** (Réflexes) | Durée d’une fabrication | ×1 | ×0,65 |

### Commerce {#trading}

| Statistique | Ce qu’elle change | Niveau 1 | Niveau 100 |
| :--- | :--- | ---: | ---: |
| **Commerce** (Instinct) | Prix de la boutique | ×1 | ×0,85 |
|  | Ce que paie la boutique au rachat | ×1 | ×1,1 |
|  | Caution d’une annonce aux Enchères | ×1 | ×0,5 |


<!-- skills-buffs:end -->

## Où vous le sentez {#where-you-feel-it}

- **Lasers.** La Technique laser change les dégâts de chaque salve et sa chance de toucher ; une salve qui part à côté affiche un « Miss » flottant et consomme quand même ses munitions ([Combat](/wiki/03-Mechanics/Combat.md#laser-tech)). La portée de vos lasers est celle de votre vaisseau : la Précision de tir progresse grâce à vos coups portés avec une autre munition que le x1 simple, mais elle n’agit que sur les Mines (ci-dessous).
- **Roquettes.** La Technique des roquettes change les dégâts de chaque roquette et la chance qu’une soit un raté ([Technique des roquettes](/wiki/06-Items/Rockets.md#rocket-tech)).
- **Encaisser les coups.** La Ténacité retire une part de chaque coup que vous encaissez, l’Esquive augmente la chance qu’un coup direct ne fasse rien, et l’Absorption du bouclier augmente la part d’un coup que prennent vos boucliers ([Combat](/wiki/03-Mechanics/Combat.md#grit-and-evasion)). La Masse augmente votre coque.
- **Compétences.** Les Réflexes raccourcissent le temps de recharge de vos compétences et la Tactique les fait durer plus longtemps ([Compétences](/wiki/03-Mechanics/Abilities.md#pilot-skills)). Le Sabotage renforce les poisons.
- **Mines.** Le Sabotage augmente les dégâts d’une Mine, et la Précision de tir la lance plus vite et plus loin ([Extras](/wiki/06-Items/Extras.md#mine)).
- **Vitesse.** La Théorie des propulseurs s’ajoute à votre vitesse, en plus des moteurs et d’un Afterburner ([Vitesse](/wiki/03-Mechanics/Speed.md)).
- **Ramassages.** L’Instinct augmente la chance de chaque ligne de butin, comme le fait un Loot Luck Booster, et les deux s’additionnent ; l’Antimatière augmente la Dark Matter que vous ramassez ([Cargaison](/wiki/03-Mechanics/Cargo.md), [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md)).
- **Radiations.** La Technique anti-radiations réduit la dose du trou noir, des cercles des excavateurs, des pulsars et de l’aura des Unwakened ([Trou noir](/wiki/03-Mechanics/Black-Hole.md)).
- **À la maison.** L’Extraction et la Logistique changent ce que le [Skylab](/wiki/03-Mechanics/Skylab.md) produit et contient, l’Instinct augmente ses deux collecteurs, la Fabrication raccourcit les fabrications de l’Assemblage, la Science remplit plus vite le Centre de [recherche](/wiki/03-Mechanics/Research.md), et le Commerce baisse les prix de la boutique, augmente ce qu’elle paie au rachat et baisse la caution d’une annonce aux [Enchères](/wiki/03-Mechanics/Auction.md).

## Comment l’XP est payée {#how-xp-is-paid}

Le serveur paie de l’XP pour ce que vous faites, où que vous voliez, dans cet ordre :

1. **La règle anti-farm.** Un coup venant d’un équipier de corporation ou de groupe, ou qui l’atteint, ne paie rien, pas plus que ce qui est fait à un vaisseau en zone sûre ou à l’abri d’une réapparition, ou par lui. Les secondes de Masse, de coque basse de la Ténacité et de Théorie des propulseurs ne comptent que tant que votre vaisseau est en vie, hors d’un abri, et que vous avez donné un ordre dans la dernière minute : un vaisseau garé à découvert ne gagne rien.
2. **Le plafond horaire souple.** Une statistique avec plafond paie l’XP entière jusqu’à lui et une part au-delà, comptée dans l’unité propre de la statistique (les tirs que vous faites, les ordres que vous donnez, l’XP qu’elle a gagnée) sur l’heure d’horloge UTC. Une nouvelle connexion ne rouvre pas la fenêtre, et les chiffres sont dans la liste plus haut et dans le tableau plus bas.
3. **Vitesse d’entraînement.** L’attribut qui régit une aptitude augmente l’XP que l’aptitude gagne, davantage à chaque niveau de l’attribut (le plafond est compté avant cela : il limite donc l’activité et non la vitesse).
4. **La part de l’attribut.** L’aptitude reçoit l’XP, et son attribut en reçoit une part, qui n’est jamais plafonnée ni accélérée.

Le tableau liste ce qui paie de l’XP, statistique par statistique. L’XP vaut pour chaque unité de ce qui est nommé dans la deuxième colonne.

<!-- skills-xp:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

| Statistique | Ce qui paie de l’XP | XP | Plafond horaire souple |
| :--- | :--- | ---: | ---: |
| **Masse** | Toutes les 10 s de vol avec un ordre donné dans les 1 min précédentes : le niveau de coque du vaisseau, plus 0,2 par plaque installée, ×1,5 avec une soute pleine | 1 | Aucun |
| **Ténacité** | Chaque 1 % de votre coque maximale perdu face à un ennemi ou un danger | 1 | 300 XP par heure |
|  | Toutes les 10 s sous 25 % de votre coque maximale | 5 |  |
| **Réflexes** | Chaque ordre que prend le jeu : une compétence, un extra, une nouvelle cible, un ramassage, une fabrication, un changement de formation, une roquette ou un saut. Une nouvelle cible paie au plus une fois en 4 s, un ramassage au plus une fois en 1 s et une roquette au plus une fois en 1 s | 1 | 600 ordres par heure |
| **Instinct** | Chaque caisse de cargaison que vous ramassez, à la main ou avec un Retriever | 2 | 600 XP par heure |
|  | Chaque objet d’une récompense de quête que vous réclamez | 10 |  |
|  | La première fois que vous ramassez un objet de qualité Rare ou mieux (une fois par objet, pour toujours) | 25 |  |
| **Technique laser** (Réflexes) | Chaque salve que vous tirez | 0,1 | 1 800 tirs par heure |
|  | Chaque salve qui touche un vaisseau | 0,1 |  |
| **Technique des roquettes** (Réflexes) | Chaque roquette que vous lancez | 0,15 | 130 roquettes par heure |
|  | Chaque roquette qui touche un vaisseau (une fois par roquette, quel que soit le nombre de vaisseaux que son explosion blesse) | 0,3 |  |
| **Antimatière** (Instinct) | Chaque unité de Dark Matter que vous recevez à un ramassage | 2,2 | Aucun |
| **Précision de tir** (Réflexes) | Chaque coup d’une salve tirée avec une autre munition que le x1 simple (×1,5 pendant les 10 min premières de chaque sorte de munition dans une heure d’horloge) | 0,1 | 3 000 coups par heure |
|  | Chaque coup d’une Mine, et chaque seconde qu’un ennemi passe dans votre Energetic Wall | 0,1 |  |
| **Sabotage** (Réflexes) | Chaque coup d’une Mine, et chaque seconde qu’un ennemi passe dans votre Energetic Wall | 0,5 | 1 200 XP par heure |
|  | Chaque seconde qu’un poison à vous agit sur un ennemi | 0,05 |  |
| **Esquive** (Réflexes) | Chaque attaque hostile contre vous qui rate ou est esquivée | 1 | 600 XP par heure |
| **Tactique** (Réflexes) | Chaque compétence que vous activez avec un hostile à portée du laser | 2 | 600 XP par heure |
| **Absorption du bouclier** (Ténacité) | Chaque 1 % de votre bouclier maximal pris par les tirs ennemis | 0,1 | 300 XP par heure |
| **Technique anti-radiations** (Ténacité) | Chaque seconde dans une bande de radiation | 0,2 | Aucun |
|  | Chaque 1 % de votre coque maximale que prend la radiation | 1 |  |
| **Théorie des propulseurs** (Masse) | Chaque seconde de vol au-dessus de 80 % de la vitesse de votre vaisseau, le double sous un Afterburner | 0,1 | Aucun |
| **Science** (Instinct) | Chaque unité de science que brûle le Centre de recherche | 0,1 | Aucun |
|  | Chaque technologie que vous terminez | 50 |  |
| **Extraction** (Instinct) | Chaque unité de ressource que produit votre Skylab, payée à la collecte | 0,1 | Aucun |
| **Logistique** (Masse) | Chaque unité de ressource que vous déposez dans la banque du Skylab | 0,05 | Aucun |
| **Fabrication** (Réflexes) | Chaque seconde de temps de fabrication que vous terminez, payée à la collecte | 0,1 | Aucun |
| **Commerce** (Instinct) | Chaque échange aux Enchères ou à la boutique, compté comme le logarithme décimal de 1 plus sa valeur en Credits (un Thulium vaut ce que lui donnent les Enchères) | 2 | 600 XP par heure |

<!-- skills-xp:end -->

Pendant que vous volez, l’écran de vol affiche l’XP que vous gagnez en courtes lignes, regroupées toutes les quelques secondes, et une bannière vous dit quand une statistique monte de niveau et ce qui a changé (le Journal de jeu en garde une ligne). Une statistique qui gagne sa première XP est annoncée une fois. Les infobulles des chiffres que les aptitudes ont modifiés le disent aussi, dans une ligne Pilote à part, et la tuile Dégâts du hangar laisse les aptitudes de côté et le dit : elles s’appliquent quand vous tirez.

## Monter de niveau {#levelling-up}

Un niveau coûte plus d’XP que le précédent, d’une part fixe, si bien que les premiers niveaux viennent vite et que les derniers sont longs. Chaque statistique a la même courbe. Le bonus que vous avez à un niveau est le même pour tous les pilotes : seule la vitesse à laquelle vous l’atteignez dépend de ce que vous faites.

<!-- skills-curve:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

| Niveau | XP du niveau | XP en tout depuis le niveau 1 | Part de chaque bonus |
| :--- | ---: | ---: | ---: |
| 2 | 40 | 40 | 1,01 % |
| 10 | 66 | 468 | 9,09 % |
| 25 | 170 | 2 174 | 24,24 % |
| 50 | 822 | 12 851 | 49,49 % |
| 75 | 3 968 | 64 397 | 74,75 % |
| 100 | 19 157 | 313 258 | 100 % |

<!-- skills-curve:end -->

## La page Aptitudes de pilote {#the-pilot-skills-page}

La page **Aptitudes de pilote** est une page de la station, avec sa propre ligne dans la barre latérale. C’est une feuille compacte de tout l’arbre : les attributs et les cinq groupes d’aptitudes se tiennent côte à côte en colonnes (trois sur un écran large, moins sur un écran étroit), avec une ligne par statistique, son niveau au bord droit et une fine barre d’XP dessous. Une statistique qui n’a pas encore gagné d’XP est grise, avec un tiret pour niveau. Posez le pointeur sur une ligne pour voir ce que fait la statistique, quel attribut la régit ou quelles aptitudes elle entraîne, son XP et ce qui la fait croître. Cliquez sur une ligne pour ouvrir ses détails sous sa rangée de colonnes : les mêmes mots, la barre d’XP et un curseur pour prévisualiser n’importe quel niveau, du 1 au dernier, avec un petit tableau de ce que la statistique change au niveau 1, à votre niveau actuel, au niveau prévisualisé et au dernier niveau. Une seule statistique est ouverte à la fois ; cliquez de nouveau sur la ligne, utilisez le bouton de fermeture ou appuyez sur Échap pour la ranger. La ligne de la barre latérale porte un badge quand une statistique est montée de niveau depuis votre dernière ouverture de la page, et une carte de la fenêtre des Boosters résume ce que vos aptitudes changent.

En vol, la même feuille est la fenêtre **Aptitudes de pilote**. Ouvrez-la avec le bouton Aptitudes de pilote de la barre d’outils (sur un écran large) ou avec sa touche, K par défaut (Paramètres, Commandes). C’est une fenêtre comme les autres : déplacez-la, redimensionnez-la, et elle se souvient de sa place et de son état ouvert. Elle ne fait que montrer vos aptitudes : les niveaux avancent à mesure que les lignes d’XP du vol arrivent, et un clic sur une ligne ouvre les mêmes détails dans la fenêtre.

## Ce qui est conservé {#what-is-kept}

- **À travers chaque réinitialisation.** L’arbre fait partie de votre compte : une réinitialisation ne change aucun niveau ni aucune XP, et le Cache de transport n’y est pour rien ([Ce que vous conservez](/wiki/03-Mechanics/Wipe-Timeline.md#what-you-keep)).
- **Sur les serveurs régionaux.** L’XP que vous gagnez en volant à Singapore ou US East est ajoutée à vos aptitudes à votre retour, y compris pour une statistique utilisée là-bas pour la première fois, et le plafond horaire que vous y avez épuisé vous suit. La page Aptitudes de pilote d’un pilote qui vole là-bas lit les chiffres du serveur régional, avec l’XP que son vaisseau a gagnée depuis sa dernière sauvegarde.
- **Jusqu’à la suppression du compte.** Supprimer un compte supprime ses niveaux.

Les bonus n’ont pas d’autre plafond que le dernier niveau : un pilote qui a tout fait monter est aussi fort que le disent les tableaux.
