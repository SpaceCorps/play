<!-- wiki-i18n source: 8adf8c0b49b112f5 -->
<!-- wiki-i18n title: Forge -->
# La Forge {#the-forge}

La **Forge** est le deuxième onglet de la page Assemblage (et de la fenêtre Assemblage en vol). Elle fait deux choses avec l’équipement que vous possédez : elle **fait monter un objet d’un rang** contre des crédits et du butin d’aliens, et elle **fusionne deux exemplaires** d’un objet en un seul qui garde le meilleur des deux. Elle a remplacé l’ancienne Chambre de fusion, qui demandait cinq objets identiques et laissait le résultat à un tirage à 25 %.

## Ce qui peut être forgé {#what-can-be-forged}

Lasers, amplis laser, boucliers, cellules de bouclier, moteurs, propulseurs, cœurs adaptatifs et Repair Drones : toute pièce d’équipement qui peut porter des [bonus d’enchantement](/wiki/05-Items/Overview.md). Elle peut se trouver dans votre inventaire, sur un vaisseau (elle y reste et fonctionne aussitôt avec son nouveau rang) ou installée dans un autre objet. Les drones, les vaisseaux, les munitions, les ressources et les boosters ne peuvent pas être forgés, pas plus que ce qui se trouve dans la cache de transport : sortez-le d’abord.

## Monter de rang {#tier-up}

Choisissez un objet et le panneau affiche son rang, le rang qu’il atteindrait, ce que cela change (combien de bonus il peut porter et leur taille), et le prix avec ce que vous possédez de chaque élément : en vert quand vous en avez assez, en rouge sinon, avec ce qu’il vous manque. Quand vous avez tout, **Monter de rang** élève l’objet d’un rang exactement. Il n’y a pas de saut : pour atteindre Éternel, un objet passe par Souillé, Divin et Fracturant, chacun avec son propre prix.

| Étape | Réussite | Crédits | Thulium | Matériaux |
| :--- | :---: | :---: | :---: | :--- |
| De Standard à Souillé | 100 % | 10 000 | – | 5 Ship Fragment, 15 Daraxium |
| De Souillé à Divin | 90 % | 50 000 | – | 30 Ship Fragment, 45 Nyxite |
| De Divin à Fracturant | 75 % | 200 000 | – | 20 Reinforced Hull Plate, 120 Cataclysite, 2 Dark Matter Plate |
| De Fracturant à Éternel | 60 % | 500 000 | 2 000 | 8 Power Core, 240 Quorvium, 2 Dark Matter Plate |

- Les **matériaux** viennent de vos piles libres : ce qui est sur un vaisseau et les piles de la cache de transport ne sont pas utilisés. Le panneau vous signale quand ceux qui manquent se trouvent dans la cache.
- **Une étape peut échouer.** L’objet reste exactement tel quel, les crédits sont perdus, et la moitié des matériaux ainsi que la moitié du Thulium vous reviennent (en arrondissant à l’entier inférieur ; sur deux Dark Matter Plates, une seule). Le panneau indique la probabilité et cette règle avant que vous n’appuyiez.
- **En cas de réussite**, chaque bonus de l’objet est tiré de nouveau dans la fourchette du nouveau rang et garde la meilleure valeur, et les emplacements de bonus supplémentaires du rang reçoivent de nouveaux bonus sur d’autres stats de l’objet. Le résultat s’affiche au-dessus du panneau ; l’objet reste sélectionné, de sorte que son étape suivante est déjà à l’écran.
- Une montée de rang est instantanée.

### Plaques de Dark Matter {#dark-matter-plates}

Les deux dernières étapes demandent chacune **2 Dark Matter Plates**, en plus de tout le reste. Une plaque est pressée à l’[Assemblage](/wiki/05-Items/Overview.md) à partir de **5 Dark Matter, 1 Velkonite Reinforced Plate et 1 Orvium Reinforced Plate** (250 Thulium, 2 minutes) ; une étape prend donc 10 Dark Matter, 2 plaques de Velkonite et 2 plaques d’Orvium. La Dark Matter vient du [trou noir](/wiki/03-Mechanics/Black-Hole.md) : environ cinq roquettes N.I.K.E. (voir [Roquettes](/wiki/05-Items/Rockets.md)) en produisent dix ; une N.I.K.E. qui rencontre un vaisseau en chemin touche ce vaisseau à la place et n’en produit pas. Les plaques sont prélevées dans vos piles libres comme les autres matériaux, et le panneau les nomme s’il vous en manque.

### Bonus par rang {#buffs-by-tier}

| Rang | Bonus portés (maximum) | Taille de chaque bonus |
| :--- | :---: | :---: |
| Souillé | 1 | +2 % à +5 % |
| Divin | 2 | +4 % à +8 % |
| Fracturant | 3 | +6 % à +11 % |
| Éternel | 4 | +9 % à +15 % |

L’équipement fabriqué avant la Forge garde les bonus qu’il avait obtenus, et ceux-ci sont souvent plus petits que ceux du tableau (une pièce de rang Divin de cette époque peut porter +2 %). Rien ne les augmente automatiquement : une montée de rang tire de nouveau chaque bonus dans la fourchette du nouveau rang et garde la meilleure valeur, et une fusion garde la meilleure valeur de chaque stat.

Un objet ne peut pas porter plus de bonus qu’il n’a de stats : un bouclier en a quatre, un laser trois (les Quantum Laser 1 et 2 en ont deux), un moteur, un propulseur ou un cœur adaptatif deux, un Crit Amp 1 ou un Repair Drone un, les amplis critiques de niveau supérieur deux, les amplis de dégâts et les cellules de bouclier trois. Quand le rang suivant ne porte pas plus de bonus que l’objet n’en peut recevoir, le panneau le signale : le rang ne fait alors que renforcer les bonus. Les bonus de portée ne dépassent jamais +5 %.

Le **bonus d’absorption d’un bouclier** (et le Boost d’absorption d’une cellule de bouclier) multiplie la stat : il vaut donc des points d’[absorption](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-) en proportion : +5 % sur les 50 % d’un Heavy Shield Core font +2,5 points, et +15 % sur chaque pièce du meilleur ensemble (un Heavy Shield Core et trois cellules Sovereign, 80 % au total) font +12 points. Un ensemble Éternel apporte entre +7 et +12 points, environ 10 en moyenne ; avec le Shield Absorbance Boost de la Boutique de saison (+10 points à son maximum ; les points de réinitialisation de tout le jeu achètent 34 de ses 100 niveaux, soit +3,4 points), cela porte un vaisseau à 95 %, et au-delà de 100 % seulement avec le maximum du bonus, ce que la stat permet : la pénétration de bouclier d’un attaquant en est retranchée. Un ensemble Divin apporte entre 3 et 6 points.

Les moteurs, propulseurs, cœurs adaptatifs et Repair Drones bougent très peu avec un bonus en pourcentage (un Engine II ajoute 4 de vitesse, donc +12 % font un demi-point) : forgez-les si vous voulez le rang, pas pour les stats.

### Où tombent les matériaux {#where-the-materials-drop}

| Matériau | Lâché par |
| :--- | :--- |
| **Ship Fragment** | tous les aliens |
| **Daraxium** | [Seeker](/wiki/04-Aliens/Seeker.md), [Phantasm](/wiki/04-Aliens/Phantasm.md) |
| **Nyxite** | [Phantasm](/wiki/04-Aliens/Phantasm.md), [Bulwark](/wiki/04-Aliens/Bulwark.md) |
| **Reinforced Hull Plate** | [Bulwark](/wiki/04-Aliens/Bulwark.md), [Goombah](/wiki/04-Aliens/Goombah.md) |
| **Cataclysite** | [Bulwark](/wiki/04-Aliens/Bulwark.md), [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Power Core** | [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Quorvium** | [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Dark Matter Plate** | aucun alien : l’Assemblage la presse à partir de la Dark Matter (le [trou noir](/wiki/03-Mechanics/Black-Hole.md)) et des plaques du Skylab |

Les cristaux suivent les rangs : le Daraxium est bleu comme Souillé, la Nyxite jaune comme Divin, la Cataclysite orange comme Fracturant et le Quorvium violet comme Éternel. Chaque source, avec les probabilités et les quantités, figure sur la page [Ressources](/wiki/05-Items/Resources.md) et sur la page de chaque alien ; le booster Resource Magnet ajoute 25 % à ce que contient une caisse.

## Fusion {#merge}

Deux exemplaires du même objet (deux Light Shield Core, deux Quantum Laser 2) n’en font plus qu’un. Passez sur **Fusionner** et cliquez sur l’objet que vous voulez garder (la **base**), puis sur un second exemplaire (le **donneur**). Le panneau montre le résultat avant que vous ne confirmiez.

- **La base est conservée.** Elle garde sa place : elle peut être sur un vaisseau, ou installée dans un autre objet, et les modules qui y sont installés restent. **Le donneur est consommé.** Il doit être libre (pas sur un vaisseau, pas installé), et les modules qui y sont installés retournent dans votre inventaire.
- **Le résultat a le plus élevé des deux rangs**, et pour chaque stat la **meilleure des deux valeurs**.
- **Il ne porte jamais plus de bonus que son rang n’en permet.** Si les deux objets réunis ont plus de bonus que le rang du résultat n’en peut porter, les meilleurs sont gardés et les autres sont perdus ; le tableau les marque (barrés, « au-dessus de la limite »). Pour porter plus de bonus, montez d’abord l’objet de rang. Une fusion ne tire jamais rien au hasard : ce que l’aperçu montre est ce que vous obtenez.
- **Une fusion coûte des crédits selon le rang qu’elle produit** : 5 000 pour Souillé, 25 000 pour Divin, 100 000 pour Fracturant, 250 000 pour Éternel. Aucun matériau.
- Une fusion qui ne changerait rien (le résultat n’est pas meilleur que la base) est refusée.
- Après une fusion, le résultat reste sélectionné et l’emplacement du donneur est vide : placez-y le donneur suivant, ou revenez à Monter de rang.

Une fusion peaufine un objet ; elle ne le multiplie pas. Deux boucliers Divin fusionnés valent environ un point et demi de bonus de plus qu’un seul. Son intérêt est de choisir : un bouclier Divin avec les stats que vous voulez, ou un rang reporté sur l’objet de votre vaisseau sans le retirer.

## Améliorations de modules à l’Assemblage {#module-upgrades-in-the-assembly}

Les deux lasers du sommet, les amplis laser, la cellule de bouclier et les propulseurs de plus haut niveau, le Heavy Shield Core et l’Engine III ne sont pas en vente. Vous les fabriquez dans l’onglet **Fabrication** de l’Assemblage en améliorant la pièce d’un cran en dessous : un Pulse Amp en **Nova Amp**, un Prism Amp en **Apex Amp**, une Prime Shield Cell en **Sovereign Shield Cell**, un Ion Thruster en **Plasma Thruster**, un Thruster II en **Thruster III**, un Basic Shield Core en **Heavy Shield Core**, un Engine II en **Engine III**, un Quantum Laser 3 en **Starfire-3** et un Starfire-3 en **Helios Beam**. Ce que la Forge a à voir là-dedans, c’est le rang.

- **Le rang est conservé.** Une amélioration consomme un exemplaire de la pièce, et le nouvel objet a le rang de cet exemplaire : un Pulse Amp Divin donne un Nova Amp Divin, un Pulse Amp Standard un Nova Amp Standard. Ce que vous avez payé à la Forge n’est pas perdu. L’amélioration n’ajoute aucun rang de son cru : une pièce Standard donne donc toujours un résultat Standard.
- **Les bonus sont tirés de nouveau.** Le nouvel objet reçoit de nouveaux bonus pour son rang : autant que le rang en porte et que le nouvel objet a de stats pour les recevoir (un Nova Amp Divin en porte deux), chacun dans la fourchette du rang indiquée dans le tableau ci-dessus, sur des stats que le Nova Amp possède. Rien n’est copié de l’ancienne pièce, donc les nouveaux bonus peuvent être meilleurs ou moins bons que ceux qu’elle avait ; en moyenne, ils sont équivalents. Les bonus sont tirés au moment où vous mettez la tâche en file, et ce que vous récupérez est ce qui a été tiré : attendre pour récupérer n’y change rien. La raison est que l’amélioration construit un nouvel objet, et que les dés de la Forge sont lancés sur l’objet que vous tenez. Le rang est la partie qui coûte : une pièce Éternel représente plus d’un million de crédits d’étapes de Forge, alors qu’un bonus n’est que quelques pour cent d’une stat.
- **Plaques.** Outre le Thulium et le butin des aliens, chaque amélioration de module demande des **Velkonite Reinforced Plates** : 3 pour un ampli, 6 pour une cellule ou un propulseur, 6 pour un Heavy Shield Core ou un Engine III, 4 pour un Thruster III et 8 pour un Starfire-3 (le Helios Beam demande à la place des Orvium Reinforced Plates, 18 au total). Les aliens n’en lâchent pas. La Fonderie de votre [Skylab](/wiki/03-Mechanics/Skylab.md) les fabrique à partir du minerai de Velkonite, 40 unités de minerai par plaque au niveau 1 de la Fonderie. Un Collecteur de Velkonite de niveau 1 extrait 12 unités de minerai par heure : les plaques d’un ampli représentent donc 10 heures d’extraction, et celles d’une cellule ou d’un propulseur 20 (4 et 8 heures avec un collecteur de niveau 5). La page [Ressources](/wiki/05-Items/Resources.md) indique d’où vient chaque matériau. Les étapes de la Forge elles-mêmes demandent du butin et des crédits, et ses étapes supérieures demandent aussi des plaques (Divin à Fracturant : 20 Reinforced Hull Plates et 2 Dark Matter Plates ; Fracturant à Éternel : 2 Dark Matter Plates), ce qui n’a rien à voir avec les plaques de Velkonite et d’Orvium des améliorations de module.
- **Quel exemplaire est utilisé.** Vous choisissez. Quand vous avez des exemplaires qui diffèrent (un autre rang ou d’autres bonus), la carte de recette les affiche en une rangée de tuiles : cliquez sur celui à utiliser, et la ligne sous les tuiles indique ce qu’il devient (« Pulse Amp Divin », puis « Résultat : Nova Amp Divin »). Si vous n’en choisissez aucun, le plus ordinaire part en premier : le rang le plus bas d’abord, et parmi les exemplaires d’un même rang le plus ancien, quels que soient leurs bonus. Un exemplaire Divin ou supérieur n’est jamais utilisé tant qu’un plus ordinaire est libre. Utiliser un exemplaire au-dessus de Standard demande d’abord confirmation et nomme l’objet.
- **Quels exemplaires peuvent être utilisés.** Les exemplaires libres : un exemplaire sur un vaisseau (dans un emplacement de compétence aussi), installé dans un autre objet, portant ses propres cellules ou propulseurs, ou dans la [cache de transport](/wiki/03-Mechanics/Cargo.md) ne peut pas être utilisé, et l’Assemblage vous le dit. Retirez-le d’abord, ou sortez-le de la cache. Deux améliorations lancées ensemble ne peuvent pas utiliser le même exemplaire.

- **Le Starfire-3 est aussi une amélioration.** Il est fabriqué à partir d’un **Quantum Laser 3** (avec 1 500 Thulium, 100 000 crédits, du butin et 8 Velkonite Reinforced Plates : voir [Lasers](/wiki/05-Items/Lasers.md)), et tout ce qui précède s’applique : un Quantum Laser 3 Divin donne un Starfire-3 Divin avec deux nouveaux bonus, vous choisissez l’exemplaire, la carte demande confirmation avant d’en utiliser un au-dessus de Standard, et le Quantum Laser 3 doit être libre : retirez-le d’abord dans le hangar, et le bouton Assembler indique « Retirez d’abord Quantum Laser 3 » tant que vous ne l’avez pas fait. Le rang se poursuit ensuite : un Starfire-3 Divin donne un Helios Beam Divin.

- **Le Helios Beam est aussi une amélioration.** Il est fabriqué à partir d’un **Starfire-3** (avec 2 000 Thulium, du butin et 18 Orvium Reinforced Plates : voir [Lasers](/wiki/05-Items/Lasers.md)), et tout ce qui précède s’applique : un Starfire-3 Divin donne un Helios Beam Divin avec deux nouveaux bonus (il en porte deux sur ses trois stats), vous choisissez l’exemplaire, la carte demande confirmation avant d’en utiliser un au-dessus de Standard, et le Starfire-3 doit être libre. Un laser est installé sur un vaisseau et porte des amplis, il n’est donc souvent pas libre : retirez-le d’abord dans le hangar (ses amplis retournent dans votre inventaire), et le bouton Assembler indique « Retirez d’abord Starfire-3 » tant que vous ne l’avez pas fait.

Les recettes, leurs coûts et les chiffres derrière la règle figurent dans l’[aperçu des objets](/wiki/05-Items/Overview.md#upgrading-modules) et, pour le Starfire-3 et le Helios Beam, sur la page [Lasers](/wiki/05-Items/Lasers.md).

## Anciens serveurs {#old-servers}

Un serveur de jeu qui n’a pas été mis à jour pour la Forge affiche « La Forge n’est pas encore sur ce serveur » à la place de l’onglet ; la Fabrication fonctionne comme avant. Un client de jeu antérieur à la Forge affiche l’ancien onglet Fusion sur un serveur mis à jour, et il lui est demandé de se mettre à jour.
