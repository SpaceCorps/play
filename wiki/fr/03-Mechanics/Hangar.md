<!-- wiki-i18n source: 2a7cab0f9ad6437b -->
<!-- wiki-i18n title: Hangar -->
# Le hangar en vol {#the-hangar-in-flight}

Vous n’avez pas besoin de retourner à la base pour changer de vaisseau. Depuis une zone sûre, vous pouvez ouvrir la fenêtre **Hangar** (le bouton en forme d’entrepôt dans la barre d’outils en haut à gauche) et modifier ce qui est installé, passer à l’autre configuration ou piloter un autre vaisseau que vous possédez, sans quitter le jeu. Cette fenêtre est la page Hangar de la station, avec les mêmes emplacements, les mêmes stats et le même inventaire, dans une fenêtre par-dessus le jeu. Voir [Inventaire et équipement](/wiki/03-Mechanics/Inventory.md) pour savoir comment les objets s’installent.

## Quand il est ouvert {#when-it-is-open}

Une modification n’est autorisée que lorsque toutes ces conditions sont réunies :

- **Une zone sûre vous protège.** Chaque station et chaque portail est entouré d’un anneau protecteur (voir [Combat](/wiki/03-Mechanics/Combat.md)). À l’intérieur, vous êtes protégé dès que 5 secondes se sont écoulées depuis votre dernier coup reçu et 15 depuis votre dernier tir.
- **Vous êtes sorti du combat** depuis quelques secondes de plus : **10** par défaut. Cela compte quand vous arrivez protégé aussitôt, par un portail, avec un combat derrière vous.
- Vous n’êtes pas occulté, pas dans la fenêtre de votre propre EMP et pas près du [trou noir](/wiki/03-Mechanics/Black-Hole.md), et aucune de vos roquettes n’est encore en vol.

Les réparations en cours ne vous bloquent pas. Partout ailleurs, la fenêtre Hangar s’ouvre quand même, mais en lecture seule. Une bannière ambre en donne la raison, et décompte les secondes quand il s’agit d’une attente (« Vous étiez en combat il y a un instant. Attendez 6 s pour modifier votre vaisseau. »). Le serveur l’impose lui aussi : rien ne peut donc modifier un vaisseau sur le terrain.

## Ce que vous pouvez modifier {#what-you-can-change}

- **Équiper et déséquiper n’importe quoi**, dans tous les types d’emplacements : lasers, générateurs (boucliers, moteurs, cœurs adaptatifs), extras, emplacements de compétence et emplacements de drone, ainsi que les amplis, cellules et propulseurs qui y sont installés. Faites glisser les objets sur les emplacements, ou cliquez dessus, exactement comme à la station. Votre vaisseau suit aussitôt : stats, lasers, compétences et barre rapide.
- **L’une ou l’autre configuration.** Vous pouvez préparer la config 2 en pilotant avec la config 1, puis basculer avec la touche Changer config. Un bouton **Piloter avec config** du hangar fait le même changement.
- **N’importe quel vaisseau.** Activez un autre vaisseau et vous le pilotez depuis l’endroit où vous êtes. Le modèle de votre vaisseau change devant tous ceux qui sont à proximité.
- **Un nouveau bouclier, moteur ou cœur adaptatif démarre vide**, comme à la station : la charge de bouclier de sa configuration est vide jusqu’à ce qu’elle se recharge.

## Changer de vaisseau {#changing-ship}

Le vaisseau vers lequel vous passez a **la coque et les boucliers qu’il avait** la dernière fois que vous l’avez piloté, exactement comme si vous l’aviez lancé. L’anneau ne répare pas : changer de vaisseau ne vous soigne donc jamais. Le vaisseau que vous quittez garde ses dégâts et revient avec eux. Un vaisseau détruit ne peut pas être piloté tant que vous ne l’avez pas réparé.

Ce qui est à vous reste à vous : vos munitions, vos roquettes et leur minuteur, les temps de recharge de vos compétences, vos boosters, votre XP et vos Slave Drones. Ce qui appartenait au vaisseau prend fin : un Shield Surge ou un Afterburner en cours, les réparations, votre verrouillage de cible, votre attaque et la route que vous suiviez. Les équipements restent sur le vaisseau qui les porte.

## Requêtes provenant d’autres outils {#requests-from-other-tools}

Côté serveur aussi, le hangar ne change que depuis une zone sûre : installer, retirer ou supprimer un objet, réparer un vaisseau ou activer un autre vaisseau en vol renvoie « Vous ne pouvez modifier votre vaisseau que dans une zone sûre. » Le changement de configuration fait exception, et fonctionne partout (une fois toutes les 5 secondes).
