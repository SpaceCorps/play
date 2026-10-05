<!-- wiki-i18n source: e65164e763773d17 -->
<!-- wiki-i18n title: Drones -->
# Mécaniques des drones {#drone-mechanics}

Les drones sont des unités de soutien autonomes qui volent à côté de votre vaisseau. Ils fournissent des emplacements d’équipement supplémentaires et contribuent directement aux performances de combat de votre vaisseau. Un Slave Drone progresse aussi : il gagne de l’expérience chaque fois que vous détruisez un alien et monte de **huit niveaux**, d’une petite sphère blindée à une canonnière aux ailes en croissant. À l’Assemblage, un Slave Drone peut être amélioré en **Master Drone**, dont les niveaux repartent du début (voir Master Drone plus bas). Les drones vous permettent aussi de porter une **formation de drones** : elle ne fonctionne que si vous avez au moins un drone dans votre flotte (voir [Formations de drones](/wiki/03-Mechanics/Formations.md)).

![Emergency Repair: repair drones beam the hull](../../img/wiki-img/shots/emergency-repair.jpg)

## Obtenir des drones {#getting-drones}

Chaque drone que vous possédez, **Slave Drone** ou Master Drone, ouvre ses emplacements de drone (un pour un Slave Drone, deux pour un Master Drone), jusqu’à **8** drones. La boutique vend les Slave Drones contre des crédits, et à partir du quatrième aussi contre du Thulium. Chacun coûte plus cher que le précédent : les prix sont dans [Drones](/wiki/06-Items/Drones.md).

## Disposition de vol et déplacement {#formation-movement}

Les drones volent selon la **disposition « Ailier » standard (2-2-4)** :

- **2 drones** à côté du vaisseau, un sur chaque flanc.
- **2 drones** à côté et juste derrière lui.
- **4 drones** qui suivent derrière.

Ils utilisent un algorithme de suivi fluide qui ajuste leur position selon la vitesse et la rotation de votre vaisseau, en resserrant la disposition lors des manœuvres brusques. Personne ne vole devant vous.

Les drones sont petits et restent près de vous : un drone de niveau 8 fait environ 19,5 unités de large (un Protos en fait 50) et un drone de niveau 1 est une boule d’environ 8, si bien que toute la disposition tient à environ 135 unités de votre vaisseau au plus. Le drone acheté en premier a le plus d’expérience et vole sur votre flanc gauche, le deuxième sur votre flanc droit, et les plus récents suivent derrière.

Cette disposition ne concerne que l’apparence des drones, et elle est la même quelle que soit la [formation de drones](/wiki/03-Mechanics/Formations.md) que vous portez. Une formation de drones est un ensemble de bonus et de prix, pas une autre façon de voler.

## Équipement et statistiques {#equipment-stats}

Les drones servent de supports d’équipement supplémentaires pour votre vaisseau.

- Un Slave Drone a **1 emplacement** et un Master Drone **2**, jusqu’à **8 drones**.
- Vous pouvez équiper des **lasers** et des **boucliers** dans ces emplacements, dans l’un comme dans l’autre emplacement d’un Master Drone. Rien d’autre n’y entre : ni moteurs, ni cœurs adaptatifs.
- **Les lasers comptent pleinement.** Un laser sur un drone tire quand vous tirez, ajoute ses dégâts à votre salve et consomme des munitions comme n’importe quel autre laser (chaque laser brûle une unité de munitions par salve). Les deux lasers d’un Master Drone comptent pour deux lasers.
- **Les boucliers comptent pleinement eux aussi.** Un bouclier sur un drone compte comme un bouclier dans un emplacement principal, dans l’un comme dans l’autre emplacement : sa capacité et sa recharge avec ses cellules, son absorption dans la moyenne de votre vaisseau, son bonus de bouclier et sa pénalité de vitesse. Il est classé avec les boucliers du vaisseau lui-même selon ce qui compte après la part de l’emplacement (l’emplacement d’un drone compte 100 % ; les quatre meilleurs comptent pleinement, le cinquième et les suivants pour moins, voir [Mécaniques des boucliers](/wiki/03-Mechanics/Shields.md)), et les bonus de la Forge, ceux de la Boutique de saison et la pénétration de bouclier d’un attaquant agissent sur lui comme sur n’importe quel bouclier. Le niveau du drone ne fait monter que son laser, jamais son bouclier. Pendant qu’un drone est en cours d’amélioration, ses emplacements sont hors ligne, le bouclier comme le laser. Avant la version 0.4.7, un bouclier sur un drone n’ajoutait rien.
- **Un laser ou un bouclier ?** Un emplacement contient l’un ou l’autre : un laser ajoute un laser à votre salve, un bouclier ajoute ses points de bouclier. Sur un petit vaisseau doté de bons boucliers, les points supplémentaires n’apportent pas grand-chose, car sa coque cède la première ; sur une grande coque, ils permettent d’en encaisser bien davantage.
- **Les formations demandent un drone, pas un emplacement.** Une [formation de drones](/wiki/03-Mechanics/Formations.md) fonctionne tant que vous possédez au moins un drone. Elle n’occupe aucun emplacement de drone, et le nombre de drones, leur niveau et ce qu’ils portent n’y changent rien.

## Niveaux {#levels}

Chaque Slave Drone commence au niveau 1 et gagne de l’expérience (XP) chaque fois que vous détruisez un alien. Un Master Drone commence lui aussi au niveau 1, sans XP, et progresse de la même façon. Chaque niveau demande plus que le précédent, et l’apparence change avec lui : vous voyez ainsi jusqu’où un drone est arrivé. Le tableau donne, pour chaque niveau, l’XP nécessaire pour y monter depuis le niveau précédent, et le nombre d’éliminations que cela représente avec un seul type d’alien (dans le monde Alpha : Beta en demande environ moitié moins, Gamma environ un tiers) :

<!-- drones:begin -->
<!-- Generated from server/Resources/drone-levels.json by scripts/drones-wiki.sh: don't edit by hand. -->

- **Niveau 1, Graine :** une petite sphère blindée dotée d’une lentille cyan.
- **Niveau 2, Halo :** la sphère dans un anneau flottant.
- **Niveau 3, Disque :** un disque plat sous un dôme de verre.
- **Niveau 4, Soucoupe :** une soucoupe à plaques de blindage et à entrées d’air.
- **Niveau 5, Canonnière :** une proue et deux canons s’ajoutent à la soucoupe.
- **Niveau 6, Bourgeons d’ailes :** des canons et de courtes lames d’aile sur des pylônes.
- **Niveau 7, Demi-ailes :** des lames d’aile plus longues aux pointes dorées.
- **Niveau 8, Croissant :** la canonnière achevée : de grandes ailes en croissant bordées de bandes lumineuses cyan.

| Niveau | XP à atteindre | XP du niveau | Dégâts du laser | Éliminations de Seeker | Éliminations de Bulwark | Éliminations de Goombah |
| --: | --: | --: | --: | --: | --: | --: |
| 1 | 0 | – | – | – | – | – |
| 2 | 350 | 350 | – | 350 | 44 | 15 |
| 3 | 900 | 550 | +1 % | 550 | 69 | 23 |
| 4 | 2 000 | 1 100 | +2 % | 1 100 | 138 | 46 |
| 5 | 3 700 | 1 700 | +3 % | 1 700 | 213 | 71 |
| 6 | 6 000 | 2 300 | +4 % | 2 300 | 288 | 96 |
| 7 | 9 500 | 3 500 | +5 % | 3 500 | 438 | 146 |
| 8 | 14 000 | 4 500 | +7 % | 4 500 | 563 | 188 |

| Alien | XP par drone |
| :--- | --: |
| Seeker | 1 |
| Phantasm | 2 |
| Bulwark | 8 |
| Goombah | 24 |
| Crystalys | 72 |

<!-- drones:end -->

### Comment les drones gagnent de l’XP {#how-drones-earn-xp}

- **Chaque drone que vous possédez gagne la même XP** pour chaque élimination d’alien qui vous est payée : les 8 premiers drones, qu’ils portent un laser ou non. Un drone acheté plus tard commence au niveau 1 sans XP : vos premiers drones ont donc toujours le niveau le plus élevé.
- **Les aliens plus coriaces valent plus.** L’XP que donne un alien figure dans le deuxième tableau ci-dessus (un Crystalys vaut 72 Seekers). Tout autre alien en donne 1.
- **Les mondes paient plus.** Beta double l’XP, Gamma la triple (les aliens y ont aussi plus de vie). Les boosters et le Premium ne la changent pas.
- **Les éliminations comptent quand elles vous sont payées.** Un alien que vous achevez pendant qu’un autre pilote détient sa revendication ne rapporte rien à vos drones, tout comme il ne vous rapporte rien. Les éliminations de pilotes, les quêtes et les éliminations des pilotes de corporation eux-mêmes ne donnent pas d’XP aux drones.
- **Le niveau 8 est le dernier.** L’XP continue de compter après lui.

### Ce que donne un niveau {#what-a-level-gives}

Le **laser installé dans l’emplacement d’un drone** inflige plus de dégâts de base à mesure que son drone monte de niveau : rien aux niveaux 1 et 2, puis +1 % au niveau 3 jusqu’à **+7 % au niveau 8**. Le bonus multiplie les dégâts propres de ce laser (après son enchantement) ; les amplis qui y sont installés s’ajoutent par-dessus et ne sont pas multipliés. Le hangar affiche le niveau de chaque drone, sa barre d’XP et le nombre d’éliminations que demande le niveau suivant, et ses chiffres de dégâts incluent déjà le bonus. Quand un drone monte de niveau, le Journal de jeu l’indique (« Le drone 2 a atteint le niveau 4. ») et un anneau de lumière jaillit du drone.

### Combien de temps cela prend {#how-long-it-takes}

La courbe est réglée pour qu’un nouveau drone atteigne le niveau 2 en environ une heure de jeu normal (en chassant des Bulwarks et des Goombahs), et le niveau 8 en environ 27 heures de jeu. Ces heures valent pour un pilote qui achète le premier drone à peu près au moment des quêtes du niveau 7 ; avec un équipement plus faible, c’est plus long (jusqu’à environ 4 heures pour le niveau 2 et 150 heures pour le niveau 8). Chasser un seul type d’alien est, au mieux, environ 1,5 fois plus rapide qu’un mélange normal. Les drones restent à la réinitialisation de la saison avec leurs niveaux et leur expérience : ces heures ne se dépensent donc qu’une fois, sur autant de saisons qu’il le faut. Un pilote qui joue une demi-heure par jour y arrive en deux saisons environ.

### Master Drone

Un Slave Drone devient un **Master Drone** quand vous l’améliorez à l’Assemblage, une fois la technologie du Master Drone recherchée ([Recherche](/wiki/03-Mechanics/Research.md)). La recette coûte 40 000 Thulium et 100 Ship Fragments et prend 60 secondes, et elle ne consomme aucun drone : **vous choisissez quel Slave Drone** (le sélecteur affiche le niveau et l’XP de chacun), et ce même drone, avec son numéro, son emplacement de drone et tout ce qui y est installé, se transforme en Master Drone à la fin de la production, avec un second emplacement vide. Rien n’arrive dans votre inventaire et il n’y a rien à récupérer : le Journal de jeu vous prévient quand c’est terminé, y compris pour une amélioration achevée pendant votre absence.

**Son niveau et son XP sont remis à 0 à la fin de l’amélioration.** Un Master Drone repart du niveau 1, sans XP, et progresse comme un Slave Drone (voir le tableau ci-dessus) ; le bonus de laser du niveau qu’il avait disparaît avec lui. L’Assemblage vous le dit avant que vous commenciez et vous demande de confirmer, en nommant le drone, quand il a de l’XP. Le choix par défaut est le drone qui a le moins d’XP.

Pendant l’amélioration, le drone est verrouillé : vous ne pouvez ni l’améliorer de nouveau ni le supprimer, et son emplacement est **hors ligne** : le laser qui s’y trouve ne tire donc pas avant la fin de la production (d’ici là, c’est toujours un Slave Drone à un seul emplacement). L’amélioration se place dans la file de production derrière vos autres travaux, comme n’importe quelle fabrication.

Un Master Drone compte parmi vos 8 drones : il entre dans la limite de drones et dans le prix du prochain Slave Drone, si bien que l’amélioration ne change ni l’une ni l’autre, et il reste à la réinitialisation de la saison avec son niveau et son XP. En vol, c’est la canonnière achevée, en or. Un Master Drone a **deux emplacements d’équipement** là où un Slave Drone n’en a qu’un : chacun accepte un laser ou un bouclier, et le bonus de niveau s’applique au laser de l’un comme de l’autre. Pour le reste, c’est un Slave Drone : les mêmes huit niveaux et le même bonus de laser. Les Master Drones que vous aviez fabriqués avant que le second emplacement n’existe l’ont maintenant, et ce qu’ils portaient est resté à sa place. Les Master Drones fabriqués avant l’existence de l’amélioration sur place sont des objets ordinaires de votre inventaire et ne volent pas.

## Comportement au combat {#combat-behavior}

- **Lasers** : les drones tirent avec leurs lasers équipés sur votre cible verrouillée.
- **Dégâts** : les drones peuvent subir des dégâts (si une logique d’entité distincte existe ; actuellement, ils partagent pour l’essentiel la réserve de points du vaisseau tout en étant visuellement distincts). _Remarque : actuellement, les drones sont des extensions indestructibles du vaisseau._
- **Repair Drones** : les objets Repair Drone (I à IV) sont des [extras](/wiki/06-Items/Extras.md#repair-drones), pas des drones de votre flotte. Pendant que l’un répare votre coque, de petits drones de réparation sortent du vaisseau, tournent autour et l’arrosent de faisceaux, et les pilotes proches les voient.
