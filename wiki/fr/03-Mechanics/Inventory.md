<!-- wiki-i18n source: ad9b37b491751af9 -->
<!-- wiki-i18n title: Inventaire -->
# Inventaire et équipement {#inventory-equipment}

Le hangar vous permet de gérer vos vaisseaux et votre équipement. Bien équiper vos objets est la clé de la survie et de la domination. Vous pouvez le faire à la station, et en vol depuis l’intérieur d’une zone sûre : voir [Le hangar en vol](/wiki/03-Mechanics/Hangar.md).

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

## Ordre de l’inventaire {#inventory-order}

L’inventaire liste vos objets dans le même ordre que la boutique, quel que soit l’ordre dans lequel vous les avez achetés, fabriqués ou trouvés. Les catégories qui vont ensemble sont regroupées : lasers, amplis laser et munitions laser ; boucliers et cellules de bouclier ; moteurs et propulseurs ; cœurs adaptatifs ; extras (Repair Drones) ; drones et formations de drones ; puis ressources. Au sein d’une catégorie, le moins cher vient en premier (les crédits avant le Thulium), puis ce qui n’a pas de prix : l’équipement à fabriquer uniquement et les objets de butin, de la rareté la plus faible à la plus élevée (pour les lasers d’une même rareté, les dégâts les plus faibles en premier). Les munitions laser vont de x1 à x4, puis vient la Siphon Battery. Les roquettes se classent par type (cible unique avant explosion de zone, guidée avant droite) puis par rang : la roquette Épique, qui coûte du Thulium, arrive donc en dernier dans son type. Les exemplaires d’un même objet se classent selon leur rang d’enchantement. Au-dessus de la grille, une pastille par catégorie suit le même ordre, avec le nombre d’objets que la recherche y trouve. Chaque pastille s’active ou se désactive seule : vous pouvez donc masquer les munitions et les Repair Drones pendant que vous travaillez sur les lasers, les boucliers et les moteurs. Cliquez sur une pastille pour afficher ou masquer sa catégorie, Shift+clic (ou double-clic) pour ne laisser que cette catégorie activée, et cliquez de nouveau dessus pour ramener les autres. **Toutes** affiche toutes les catégories et **Aucune** les masque toutes, pour n’activer que celles que vous voulez. Une pastille barrée est désactivée, une pastille avec une coche est activée. La recherche porte sur les catégories activées, et votre choix est mémorisé avec votre pilote. Si tout est masqué, la grille l’indique et propose **Afficher toutes les catégories**.

## Équiper un objet dans un autre (sous-emplacements) {#item-to-item-equipping-sub-sockets-}

Certains objets principaux peuvent « équiper » des objets de soutien secondaires (c’est ce qu’on appelle le sous-emplacement) pour amplifier leurs paramètres. Pour installer un objet dans un sous-emplacement, faites glisser l’objet de soutien directement sur l’objet principal dans l’inventaire de votre hangar.

### Tableau de compatibilité {#compatibility-table}

| Objet principal | Objets acceptés en sous-emplacement | Effet obtenu |
| :--- | :--- | :--- |
| **Laser** | Ampli laser (amplificateur) | Augmente les dégâts de base et les stats de coup critique |
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
