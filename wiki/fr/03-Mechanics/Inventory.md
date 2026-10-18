<!-- wiki-i18n source: da8af0d25d34a2c4 -->
<!-- wiki-i18n title: Inventaire -->
# Inventaire et équipement {#inventory-equipment}

Le hangar vous permet de gérer vos vaisseaux et votre équipement. Bien équiper vos objets est la clé de la survie et de la domination. Vous pouvez le faire à la station, et en vol depuis l’intérieur d’une zone sûre : voir [Le hangar en vol](/wiki/03-Mechanics/Hangar.md).

![The Hangar's inventory: the category chips are one glyph each (the name is the tooltip) with the count of what you hold](../../img/wiki-img/shots/inventory-chips.jpg)
![Dragging a rectangle over the empty space of the inventory: every tile it touches is selected and the title row counts them](../../img/wiki-img/shots/inventory-marquee.jpg)

## Emplacements d’équipement et efficacité des stats {#equipment-slots-stat-efficiencies}

Contrairement aux jeux spatiaux traditionnels, SpaceCorps propose des emplacements d’équipement à paliers dynamiques, qui modulent l’efficacité des modules installés.

- **Emplacements laser** : pour les armes offensives (lasers). Ils fonctionnent toujours à **100 % des dégâts et de la portée**.
- **Emplacements de générateur** : emplacements communs aux boucliers, aux moteurs et aux cœurs adaptatifs. Ils se divisent en trois paliers d’efficacité, et le palier décide quelle part des stats de base d’un objet compte. Dans le hangar, chaque palier a un (i) à côté de son nom qui l’explique :
  - **Emplacements principaux** : les objets placés ici reçoivent **100 %** de leurs stats de base. Tous les vaisseaux en ont : mettez-y vos boucliers et vos moteurs les plus puissants.
  - **Emplacements de soutien** : les objets placés ici reçoivent **75 %** de leurs stats de base (p. ex. 75 % de la vitesse ou de la capacité du bouclier). Tous les vaisseaux en ont.
  - **Emplacements auxiliaires** : les objets placés ici reçoivent **50 %** de leurs stats de base. Seuls certains vaisseaux en ont (le Nomad en a 1, le Paragon et le Storm 2, l’Ironclad 3 et le Wraith 4 ; le Protos, le Kitefin et l’Ostirion n’en ont aucun). Ils conviennent surtout aux boucliers et moteurs supplémentaires, plus faibles, tandis que vos plus puissants vont dans les emplacements principaux.
  - **Emplacements de drone** : un bouclier sur l’un de vos drones compte comme un bouclier dans un emplacement principal, soit **100 %** de ses stats (voir [Mécaniques des drones](/wiki/03-Mechanics/Drones.md)).
  - **Emplacements non attribués ou hérités** : les objets placés ici ne contribuent pas aux stats.
  - **Le cumul s’estompe aussi** : les boucliers et les moteurs sont classés du plus fort au plus faible (selon ce que chacun compte après la part de son emplacement), et la part du palier est ensuite multipliée par celle de leur rang : du 1er au 4e, ils comptent en entier, le 5e, le 6e et le 7e comptent respectivement 85 %, 70 % et 55 %, et à partir du 8e, 50 % pour les boucliers et 25 % pour les moteurs. Voir [Boucliers](/wiki/03-Mechanics/Shields.md) et [Vitesse](/wiki/03-Mechanics/Speed.md).
- **Emplacements extras** : pour les objets utilitaires spécialisés, comme les Repair Drones. Le Protos, le Kitefin, l’Ostirion et le Nomad en ont deux ; le Paragon, l’Ironclad, le Wraith et le Storm, que vous fabriquez, en ont trois. Les Extra Slots CPU ([Extras](/wiki/06-Items/Extras.md#extra-slots-cpus)) en ajoutent 3, 5 ou 7.
- **Emplacements de blindage** : pour le [blindage de coque](/wiki/06-Items/Hull-Plating.md#hull-plate-slots), qui ajoute de la coque. Seuls les quatre vaisseaux que vous fabriquez en ont (le Paragon 5, le Storm 7, l’Ironclad 15 et le Wraith 9), chacun verrouillé tant que vous ne l’avez pas recherché dans le Skylab, et ils sont identiques dans les deux configurations.

## Ordre de l’inventaire {#inventory-order}

L’inventaire liste vos objets dans le même ordre que la boutique, quel que soit l’ordre dans lequel vous les avez achetés, fabriqués ou trouvés. Les catégories qui vont ensemble sont regroupées : lasers, amplis laser et munitions laser ; boucliers et cellules de bouclier ; moteurs et propulseurs ; cœurs adaptatifs ; extras (Repair Drones) ; drones et formations de drones ; puis ressources. Au sein d’une catégorie, le moins cher vient en premier (les crédits avant le Thulium), puis ce qui n’a pas de prix : l’équipement à fabriquer uniquement et les objets de butin, de la rareté la plus faible à la plus élevée (pour les lasers d’une même rareté, les dégâts les plus faibles en premier). Les munitions laser vont de x1 à x4, puis vient la Siphon Battery. Les roquettes se classent par type (cible unique avant explosion de zone, guidée avant droite) puis par rang : la roquette Épique, qui coûte du Thulium, arrive donc en dernier dans son type. Les exemplaires d’un même objet se classent selon leur rang d’enchantement. Au-dessus de la grille, une pastille par catégorie suit le même ordre, avec le nombre d’objets que la recherche y trouve. Chaque pastille s’active ou se désactive seule : vous pouvez donc masquer les munitions et les Repair Drones pendant que vous travaillez sur les lasers, les boucliers et les moteurs. Cliquez sur une pastille pour afficher ou masquer sa catégorie, Shift+clic (ou double-clic) pour ne laisser que cette catégorie activée, et cliquez de nouveau dessus pour ramener les autres. **Toutes** affiche toutes les catégories et **Aucune** les masque toutes, pour n’activer que celles que vous voulez. Une pastille barrée est désactivée, une pastille avec une coche est activée. La recherche porte sur les catégories activées, et votre choix est mémorisé avec votre pilote. Si tout est masqué, la grille l’indique et propose **Afficher toutes les catégories**.

## Objets vendables {#marketable-items}

Les objets que vous avez gagnés (butin, récompenses de missions et ce que fabriquent l’Assemblage et la Forge) portent une petite étiquette **Vendable** sur leur case, et la fiche de l’objet indique « Vendable » ou, pour une pile dont seule une partie peut être vendue, « Vendable (3 sur 5) ». La pastille **Vendable uniquement**, à côté des pastilles de catégorie, ne montre que ces objets. Un **marteau** à côté de la corbeille d’un objet étiqueté ouvre la fiche de vente des [Enchères](/wiki/03-Mechanics/Auction.md) (il n’est pas affiché en vol : vendre se fait sur une page de la station). Ce que vous avez acheté, gagné ou reçu en cadeau n’a pas d’étiquette et ne peut pas être revendu.

## Sélectionner plusieurs objets {#select-several-items}

Appuyez sur une partie vide de l’inventaire (la marge à côté des cases, l’espace entre deux cases ou la place sous la dernière rangée) et faites glisser : un rectangle translucide suit le pointeur, et chaque case qu’il touche est sélectionnée pendant que vous glissez. Relâchez : la sélection reste, et la ligne du titre la compte (« 3 sélectionnés »). Maintenez **Maj**, **Ctrl** ou **Cmd** en glissant pour ajouter à la sélection : les cases déjà sélectionnées que le rectangle touche sont alors relâchées. Un glissement simple commence une nouvelle sélection. **Échap**, un clic sur un espace vide ou le bouton à côté de la corbeille dans la ligne du titre l’efface ; **Échap** en plein glissement annule le glissement. Au bord haut ou bas d’un long inventaire, la liste défile toute seule. Un appui sur une case reste celui de la case : clic pour équiper, glisser vers un emplacement. La corbeille de la ligne du titre supprime les objets sélectionnés après une question qui les énumère (une pile d’Extras identiques part en entier) ; elle n’est pas proposée tant que le Hangar en vol est verrouillé. Un objet monté dans le Skylab ne peut pas être sélectionné, et seul ce que la recherche et les pastilles de catégorie laissent dans la grille le peut. Un léger tic retentit quand le rectangle prend une case de plus (il suit l’interrupteur « Sons des boutons » des réglages).

**Équiper toute la sélection.** Faites glisser l’une des cases sélectionnées et toute la sélection vous suit, comme une pile de cases avec un nombre devant le pointeur (une case qui n’est pas sélectionnée glisse seule, et un clic sur une case sélectionnée n’équipe toujours que cet objet). Si vous relâchez sur un emplacement ou sur une carte, l’objet sous le pointeur y va s’il convient, et tous les autres vont à leur meilleur emplacement ; si vous relâchez sur les parties vides du vaisseau, chaque objet va à son meilleur emplacement ; partout ailleurs il ne se passe rien, et **Échap** abandonne le glissement. Le bouton à flèche à côté de la corbeille dans la ligne du titre (son infobulle dit qu’il équipe les objets sélectionnés dans leurs meilleurs emplacements) fait la même chose sans glisser ; il n’est pas proposé dans la vue P.E.T. ni tant que le Hangar en vol est verrouillé. Le meilleur emplacement est celui où un clic mettrait l’objet, calculé objet après objet : d’abord les lasers, les plus puissants en premier, puis les boucliers, les moteurs et les cœurs adaptatifs, les extras, les Repair Drones (dans un emplacement de compétence libre quand les extras sont pleins), les blindages de coque et enfin les amplis, cellules et propulseurs, qui ont besoin que leurs lasers, boucliers et moteurs soient déjà montés. Ce qui n’a pas pu être placé reste sélectionné, et un message dit combien sont passés (« Équipés : 7 sur 9. ») et pourquoi les autres non. Un seul son léger retentit pour tout le dépôt.

## Équiper un objet dans un autre (sous-emplacements) {#item-to-item-equipping-sub-sockets-}

Certains objets principaux peuvent « équiper » des objets de soutien secondaires (c’est ce qu’on appelle le sous-emplacement) pour amplifier leurs paramètres. Pour installer un objet dans un sous-emplacement, faites glisser l’objet de soutien directement sur l’objet principal dans l’inventaire de votre hangar.

### Tableau de compatibilité {#compatibility-table}

| Objet principal | Objets acceptés en sous-emplacement | Effet obtenu |
| :--- | :--- | :--- |
| **Laser** | Ampli laser (amplificateur) | Augmente les dégâts de base et les stats de coup critique, ou retranche des points à l’absorption de la cible (Penetration Amp) |
| **Bouclier** | Cellule de bouclier | Augmente la capacité du bouclier et la vitesse de recharge |
| **Moteur** | Propulseur | Augmente la vitesse du moteur et ses multiplicateurs |
| **Générateur hybride** | Cellule de bouclier OU propulseur | Augmente la capacité du bouclier, la vitesse de recharge ou la vitesse |
| **Drone** | Laser ou bouclier, dans chacun de ses emplacements (un Master Drone en a deux) | Un laser ajoute ses dégâts à votre salve ; un bouclier compte comme un bouclier dans un emplacement principal (100 % de ses stats) |

---

## Gestion des munitions {#ammo-management}

Les munitions laser sont une ressource consommable.
- Les munitions s’empilent dans votre inventaire.
- Vous pouvez changer de munitions laser actives via la barre rapide de votre HUD.
- Les munitions de meilleure qualité apportent des multiplicateurs de dégâts (p. ex. standard x1, Advanced Plasma x2, Ultra Core x3, Experimental Fusion Core x4). La Siphon Battery inflige des dégâts x1 aux boucliers uniquement et les ajoute à votre bouclier.
