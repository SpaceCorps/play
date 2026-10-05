<!-- wiki-i18n source: b98e7995bde4597b -->
<!-- wiki-i18n title: Clans -->
# Clans

Fonder un clan ou en rejoindre un vous permet de mettre vos ressources en commun, d’améliorer la banque partagée, de fixer les taux de taxe, de vous coordonner avec les membres de votre faction et de gérer la diplomatie. Un clan a aussi du travail à faire ensemble : chaque jour il reçoit une **ligne du jour** de missions qui se termine par un boss que seul le clan peut blesser, et les points qu’il gagne achètent des **bonus permanents** pour chaque membre. (Sur la page Clan du jeu, un clan s’appelle une *flotte* ; ses points et ses bonus y sont les points de flotte et les bonus de flotte.)

**En une minute**

- Chaque jour de saison, votre clan reçoit une [ligne du jour](#daily-line) : quatre missions à faire dans l’ordre (détruire des aliens, parcourir une distance, parfois abattre des boss d’essaim), puis un [Gardien de clan](#clan-wardens), un boss que vous invoquez et que seul votre clan peut blesser.
- Chaque étape terminée rapporte aussitôt des points de clan : 15, 15, 20, 20 et 30, soit **100 points** pour une ligne complète.
- Le chef et les chefs adjoints dépensent les points dans trois [bonus](#clan-points-and-boosts) de dix niveaux chacun : **Dégâts** (jusqu’à +5 %), **Thulium** (jusqu’à +10 %) et **Crédits** (jusqu’à +10 %).
- Un clan qui termine chaque ligne a acheté tous les niveaux au **jour 12 de la saison**. Les points et les niveaux repartent de zéro à chaque réinitialisation.
- Il faut au moins **trois membres** qui ont fait leur part, et environ cinq pilotes pour le combat contre le Gardien.
- La ligne et les bonus demandent un jeu en version 0.4.10 ou plus récente.

![Buying a level of a clan boost: the sheet shows the level, the bonus the whole fleet gets and the cost in clan points](../../img/wiki-img/shots/clan-boosts.jpg)
![Summoning a Warden for the clan](../../img/wiki-img/shots/clan-warden.jpg)

## Progression du clan {#clan-progression}

Les clans commencent au niveau 1 et peuvent monter jusqu’au niveau 5. Améliorer le clan exige de payer des crédits depuis la **Banque du clan**. Les améliorations augmentent la capacité en membres et les limites de versement quotidiennes.

| Niveau du clan | Limite de membres | Limite de versement quotidienne (par membre) | Coût d’amélioration (crédits) |
| :---: | :---: | :---: | :--- |
| **Niveau 1** | 10 | 1 000 000 cr | — |
| **Niveau 2** | 25 | 2 000 000 cr | 10 000 000 cr |
| **Niveau 3** | 50 | 3 000 000 cr | 100 000 000 cr |
| **Niveau 4** | 75 | 4 000 000 cr | 1 000 000 000 cr |
| **Niveau 5** | 100 | 5 000 000 cr | 10 000 000 000 cr |

---

## Économie et taxation du clan {#clan-economy-taxation}

Les clans fonctionnent selon un système financier fondé sur la taxe :

### 1. Taxation quotidienne {#1-daily-taxation}

- **Taux de taxe** : le chef ou les chefs adjoints peuvent fixer un taux de taxe quotidien compris entre **0 % et 5 %**.
- **Prélèvement automatique** : une fois par jour (UTC), le serveur prélève automatiquement la taxe sur tous les membres du clan.
- **Formule** : la taxe est calculée comme `ClanTaxRate` du solde de crédits actuel de chaque membre.
  - *Exemple* : si vous avez 10 000 000 crédits et que la taxe du clan est de 2 %, 200 000 crédits seront déduits de votre compte et déposés dans la Banque du clan.
  - Des dons volontaires de crédits sont aussi possibles, jusqu’au plafond indiqué dans la section suivante.

### 2. Dons {#2-donations}

- **Faire un don** : tout membre peut envoyer des crédits dans la Banque du clan depuis la page Clan. La fiche indique ce que vous pouvez encore envoyer.
- **Limite de dons** : un pilote peut envoyer au plus **1 000 000 crédits à des clans sur n’importe quelle période de 24 heures**, tous les clans où il a été confondus. Quitter un clan pour en rejoindre un autre ne donne pas de nouveau quota.
- **Pas de remise à zéro quotidienne** : les 24 heures sont glissantes. Chaque don cesse de compter exactement 24 heures après avoir été fait, et la fiche vous indique quand le plus ancien le fait et combien vous est rendu. Un don supérieur à ce qu’il reste est refusé en entier.
- La taxe quotidienne n’est pas un don et n’entame pas votre quota.

### 3. Versements de la banque {#3-bank-payouts}

- **Limites de versement** : les chefs et les officiers du clan peuvent distribuer des crédits de la Banque du clan à des membres, individuellement.
- **Plafond quotidien** : un membre ne peut pas recevoir plus de `1,000,000 * ClanLevel` crédits en versements au cours d’un même jour calendaire (UTC).

---

## Hiérarchie et rôles {#hierarchy-roles}

Les clans utilisent une structure de grades fondée sur les rôles pour gérer les permissions :

- **Chef (rôle 3)** : dispose d’un accès administratif complet, dont l’amélioration du clan, la fixation des taxes, la diplomatie, les promotions, les renvois et la dissolution du clan.
- **Chef adjoint (rôle 2)** : peut fixer les taux de taxe, verser des crédits, gérer la diplomatie, et promouvoir ou rétrograder les grades inférieurs.
- **Aîné (rôle 1)** : membre de confiance qui peut accepter les nouvelles candidatures au clan.
- **Membre (rôle 0)** : joueur standard, sans permission d’administration.

### Tableau des permissions {#permissions-table}

| Action | Chef | Chef adjoint | Aîné | Membre |
| :--- | :---: | :---: | :---: | :---: |
| **Dissoudre le clan** | ✅ | ❌ | ❌ | ❌ |
| **Améliorer le clan** | ✅ | ❌ | ❌ | ❌ |
| **Fixer le taux de taxe** | ✅ | ✅ | ❌ | ❌ |
| **Verser des crédits** | ✅ | ✅ | ❌ | ❌ |
| **Gérer la diplomatie** | ✅ | ✅ | ❌ | ❌ |
| **Acheter les bonus du clan** | ✅ | ✅ | ❌ | ❌ |
| **Invoquer le Gardien du clan** | ✅ | ✅ | ❌ | ❌ |
| **Promouvoir / Renvoyer** | ✅ | ✅* | ❌ | ❌ |
| **Accepter les candidatures** | ✅ | ✅ | ✅ | ❌ |

*\*Les chefs adjoints ne peuvent promouvoir, rétrograder ou renvoyer que des membres d’un grade inférieur au leur.*

### Quand le chef part {#when-the-leader-leaves}

Un chef ne peut pas quitter un clan qui compte encore d’autres membres : il doit d’abord promouvoir un chef adjoint au rang de chef (le chef redevient alors chef adjoint), ou partir en dernier, ce qui dissout le clan. Si le chef supprime son compte (Paramètres › Compte), la direction passe au membre le plus haut gradé, et à égalité à celui qui a le plus d’ancienneté ; un chef seul dans le clan le dissout, banque comprise.

---

## Ligne du jour {#daily-line}

Chaque clan reçoit une **ligne du jour** par jour : cinq étapes, à faire **dans l’ordre**, par tout le clan ensemble. Les quatre premières sont des missions : détruire tant d’aliens, parcourir tant de distance ou, certains jours, abattre des boss d’essaim. La cinquième est un **Gardien de clan**, un boss que vous invoquez et détruisez. Ouvrez **Communauté › Clan** et son onglet **Opérations** pour voir la ligne du jour, l’étape ouverte avec sa barre, votre propre part et le temps restant.

### Les cinq étapes {#the-five-steps}

| Étape | Quoi | Points de clan |
| :---: | :--- | ---: |
| 1 | Première mission | 15 |
| 2 | Deuxième mission | 15 |
| 3 | Troisième mission | 20 |
| 4 | Quatrième mission | 20 |
| 5 | Le Gardien de clan du jour | 30 |
| | **Une ligne terminée** | **100** |

- Seule l’**étape ouverte compte**. Une destruction faite pendant que l’étape 1 est ouverte compte pour l’étape 1 et pour rien d’autre. Quand l’étape 1 est terminée, l’étape 2 s’ouvre à zéro. Ce que vous détruisez au-delà de l’objectif d’une étape n’est pas gardé pour la suivante.
- Une étape rapporte ses points **à l’instant où elle est terminée**. Un clan qui finit les quatre missions puis ne parvient pas à réunir un équipage pour le Gardien garde tout de même **70 points**.
- Le travail de tous va dans **un seul compteur partagé** : les destructions de l’alien de l’étape ouverte et la distance parcourue par tous vos membres s’additionnent, personne n’a donc à faire une étape seul.

### Le jour {#the-day}

- Le jour d’un clan est un **jour de saison** : 24 heures comptées depuis le début de la saison ([Chronologie des réinitialisations](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule)). Une nouvelle ligne commence à la même heure chaque jour, qui n’est pas minuit UTC (la taxe quotidienne du clan reste prélevée à minuit UTC). L’onglet Opérations décompte jusqu’au changement.
- Une ligne non terminée **expire** à la fin du jour. Les étapes déjà faites gardent leurs points, la progression de l’étape ouverte est perdue, et il n’y a pas de rattrapage. Les lignes courent les jours de saison 1 à 29.
- Les pilotes du clan qui sont en ligne reçoivent un message Système quand la nouvelle ligne commence, quand une étape est terminée et **une heure avant le changement** si la ligne n’est pas terminée.

### Niveaux de difficulté {#difficulty-tiers}

Chaque jour, le jeu prend le **niveau moyen des cinq pilotes de plus haut niveau** du clan (tous, s’il en a moins de cinq) et en tire le palier du jour :

| Palier | Niveau moyen | Gardien |
| :--- | :--- | :---: |
| Recrue | moins de 4 | I |
| Vétéran | de 4 à moins de 7 | II |
| Élite | 7 ou plus | III |

Le palier décide combien d’aliens les missions demandent, quel alien demande l’étape « lourde » et quelle est la force du Gardien. **Les points sont les mêmes à chaque palier.** Les nouveaux pilotes de bas niveau ne font pas baisser le palier : seuls les cinq meilleurs comptent.

### Qui compte {#who-counts}

- **Le total du clan compte.** Les barres de l’onglet Opérations sont celles du clan entier.
- **Votre minimum.** Pour partager la récompense du jour, vous devez faire **5 % du travail du jour**, environ huit minutes de vraie chasse. L’onglet l’affiche ainsi : « Votre travail aujourd’hui : 312 sur 469 unités ». Une unité de travail est une seconde de jeu : une destruction compte le temps qu’il faut pour trouver et détruire cet alien, et un trajet en vol le temps qu’il prend. Pour un clan Vétéran, un Seeker vaut environ 12 unités, un Phantasm 22, un Bulwark 123 et 1 000 unités parcourues environ 5 ; le minimum est de 446 à 480 unités, quels que soient le jour et le palier.
- **Au moins trois membres** doivent avoir atteint leur minimum pour qu’une étape puisse être terminée. Si une étape est pleine et que moins de membres l’ont atteint, elle **attend** (« L’étape 3 est pleine, mais seuls 2 membres ont atteint leur minimum »), et les destructions de l’alien de cette étape continuent d’ajouter au travail des membres qui les ont faites jusqu’à ce que le troisième y arrive. Un clan de moins de trois pilotes ne peut terminer aucune étape.
- **À qui va une destruction.** Au pilote qui est payé pour la destruction et à ses coéquipiers de groupe à moins de 4 000 unités qui ont tiré dans les 15 dernières secondes ([Groupes](/wiki/03-Mechanics/Groups.md#sharing-kills)). Un clan compte une destruction **une seule fois**, quel que soit le nombre de ses pilotes dans le groupe, et le travail de la destruction est partagé à parts égales entre eux. Deux clans dans un même groupe la comptent chacun une fois.
- **Quelles destructions.** Seulement l’alien de l’étape ouverte : le Seeker, Phantasm, Bulwark ou Goombah ordinaire. Les vaisseaux d’essaim, les autres pilotes et les auxiliaires d’un Gardien ne comptent pas comme ces aliens. Tous les mondes comptent, et une destruction compte plus dans un monde plus fort : **1 en Alpha, 1,5 en Beta, 2 en Gamma** ([Mondes](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)). Une étape de boss compte les boss des [essaims](/wiki/05-Swarms/Swarms.md), un pour chaque clan qui a un pilote ayant infligé au moins 5 % des dégâts.
- **Voler.** Une étape de patrouille compte la distance que chaque pilote parcourt hors des zones sûres ; cinq pilotes qui volent ensemble ajoutent cinq fois la distance.
- **Arrivées et départs.** Ce que vous avez fait reste compté si vous partez. Un pilote qui arrive compte à partir de cet instant.

### Les sept lignes {#the-seven-lines}

Les lignes tournent sur un cycle de sept : la ligne du jour de saison *d* porte le numéro 1 + ((*d* − 1) mod 7), chacune revient donc tous les sept jours. Les chiffres sont ceux d’un clan **Recrue / Vétéran / Élite**. Les deux lignes **Swarm Break** demandent des boss d’essaim et n’arrivent qu’à partir du jour 4, quand les [essaims](/wiki/05-Swarms/Swarms.md) apparaissent. Tous les chiffres sont faits pour environ **2,6 heures de jeu au total**, une demi-heure chacun pour cinq pilotes (une estimation, pas une mesure).

| Ligne | Jours de saison | Étape 1 | Étape 2 | Étape 3 | Étape 4 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Seeker Sweep | 1, 8, 15, 22, 29 | 150 / 300 / 425 Seeker | 115 000 / 155 000 / 185 000 unités | 21 / 70 / 130 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah |
| Phantasm Purge | 2, 9, 16, 23 | 40 / 140 / 270 Phantasm | 60 / 120 / 170 Seeker | 175 000 / 230 000 / 275 000 unités | 26 Phantasm / 15 Bulwark / 17 Goombah |
| Long Haul | 3, 10, 17, 24 | 290 000 / 385 000 / 460 000 unités | 90 / 180 / 260 Seeker | 26 / 85 / 170 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah |
| Swarm Break I | 4, 11, 18, 25 | 75 / 150 / 220 Seeker | 3 Boss Seeker / 3 Boss Seeker / 2 Pirate Boss | 26 / 85 / 170 Phantasm | 30 Phantasm / 18 Bulwark / 21 Goombah |
| Heavy Iron | 5, 12, 19, 26 | 40 Phantasm / 24 Bulwark / 28 Goombah | 21 / 70 / 130 Phantasm | 175 000 / 230 000 / 275 000 unités | 75 / 150 / 220 Seeker |
| Swarm Break II | 6, 13, 20, 27 | 75 / 150 / 220 Seeker | 21 / 70 / 130 Phantasm | 4 Boss Seeker / 1 Pirate Boss / 3 Pirate Boss | 350 000 / 460 000 / 550 000 unités |
| Grand Round | 7, 14, 21, 28 | 100 / 210 / 300 Seeker | 26 / 85 / 170 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah | 230 000 / 305 000 / 365 000 unités |

### Votre récompense {#the-reward-for-you}

Quand la ligne est terminée, chaque membre qui a atteint le minimum et qui est toujours dans le clan est payé, même hors ligne. Le versement est fixe : les bonus, les boosters et le monde ne le changent pas.

| Palier | Crédits | Thulium |
| :--- | ---: | ---: |
| Recrue | 5 000 | 20 |
| Vétéran | 15 000 | 60 |
| Élite | 22 000 | 90 |

---

## Gardiens de clan {#clan-wardens}

Un **Gardien de clan** est le boss de la fin de la ligne du jour. Ce n’est pas l’un des [essaims](/wiki/05-Swarms/Swarms.md) publics qui rôdent dans un secteur : votre clan **l’invoque** et **seul votre clan peut le blesser**. Trois Gardiens se relaient, un par jour : jour 1 **Brood**, jour 2 **Siege**, jour 3 **Wrath**, jour 4 de nouveau Brood, et ainsi de suite (le jour 15 est un jour Wrath). Chacun existe en trois forces, **I, II et III**, fixées par le palier du clan. Un Gardien est un alien d’un genre à part, comme les vaisseaux d’un essaim : il ne compte pas comme un Seeker, un Phantasm ni aucun autre alien.

| Gardien | Jours de saison | Rôle | Comment il combat |
| :--- | :--- | :--- | :--- |
| **Brood Warden** | 1, 4, 7, 10 … | Gardien de la ruche : répartissez votre tir | Quatre petits **Brood Drones** soignent sa coque, et un nouveau arrive toutes les 8 secondes tant que moins de quatre sont en vie. Tirez d’abord sur les drones, puis sur le Gardien. |
| **Siege Warden** | 2, 5, 8, 11 … | Briseur de siège : restez en mouvement | Il rôde et tire une [roquette Rivet](/wiki/06-Items/Rockets.md#the-twelve-rockets) droite sur le premier pilote qui l’a touché, et il se répare tout seul. Deux **Siege Escorts** ajoutent un tir laser. Restez en mouvement et servez de cible à tour de rôle. |
| **Wrath Warden** | 3, 6, 9, 12 … | Seigneur de guerre : battez la rage | Il combat sur place et se répare tout seul. Sous la moitié de sa coque, ses lasers frappent **une fois et demie plus fort**. Deux **Wrath Guards** ajoutent un tir laser. Abattez-le vite et gardez vos boucliers levés. |

### Invoquer un Gardien {#calling-a-warden}

- **Quand.** Une fois l’étape 4 terminée. Un clan a **deux invocations par jour**, un seul Gardien dehors à la fois, et il doit rester **au moins 30 minutes** de jour.
- **Qui.** Le chef ou un chef adjoint.
- **Comment.** En vol : le bouton **Invoquer ici** apparaît sur l’écran de vol dès que l’étape 4 est terminée, et vous demande de confirmer. Soyez hors des zones sûres, dans un secteur de corporation **x-2, x-3 ou x-4** (de n’importe quelle corporation) de votre monde. L’onglet Opérations montre le Gardien du jour, les invocations restantes et pourquoi le bouton est grisé, mais un Gardien s’invoque depuis le vaisseau.
- **Où il apparaît.** À 3 000 à 4 500 unités de votre vaisseau, dans votre monde : seuls les pilotes de ce monde peuvent l’atteindre. L’onglet recommande **x-2 pour un clan Recrue, x-3 pour Vétéran et x-4 pour Élite**. Les [règles de PvP](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) habituelles du secteur choisi s’appliquent toujours.
- **Montée en charge.** Il reste **90 secondes** protégé et passif (« montée en charge »), et chaque pilote du clan en ligne est informé de l’endroit. Volez vers lui pendant qu’il se charge : passé les 90 secondes, il est actif.
- **Seulement votre clan.** Les tirs des pilotes de tout autre clan sont ignorés et ne le font pas riposter.
- **Comment cela se termine.** Quand il est détruit. Il **se retire** 40 minutes après son activation, à la fin du jour, quand aucun pilote de votre clan n’a été en vol sur sa carte pendant 2 minutes, ou au redémarrage du serveur (l’invocation est alors rendue). Un Gardien qui se retire coûte une invocation, et l’appel suivant est le même Gardien à pleine force.

### Combattre un Gardien {#fighting-a-warden}

- **Un Gardien combat le premier pilote qui l’a touché**, comme tout boss : laissez le vaisseau le plus robuste de l’équipage commencer, et utilisez [Shield Surge et Emergency Repair](/wiki/03-Mechanics/Abilities.md).
- **Emportez des munitions x2** ([Lasers](/wiki/06-Items/Lasers.md#laser-ammunition)). Un équipage de cinq gagne même avec des munitions x1, plus lentement ; un équipage de trois, non.
- **Brood :** les drones soignent sa coque, et un équipage de trois qui les ignore perd. Détruisez-les d’abord : l’un meurt en une seconde ou moins sous le tir de cinq pilotes, et le suivant arrive après 8 secondes.
- **Siege :** ses roquettes sont droites et non guidées, un vaisseau qui reste en mouvement en esquive donc la plupart. Restez en mouvement et servez de cible à tour de rôle.
- **Wrath :** dès que sa coque passe sous la moitié, chaque salve frappe une fois et demie plus fort, la seconde moitié du combat est donc la dangereuse. Abattez la première moitié vite, gardez les boucliers levés et gardez Emergency Repair pour la rage.

### Quel équipage il faut {#how-big-a-crew}

> [!NOTE]
> Ces durées sont **calculées** à partir des chiffres ci-dessous, pas mesurées en jeu : un équipage dans les vaisseaux et l’équipement pour lesquels le palier est fait, tous tirant sur le Gardien. Un tiret signifie que nous ne l’avons pas calculé.

| Équipage | Avec munitions x2 | Avec munitions x1 |
| :--- | :--- | :--- |
| 2 pilotes | perdent contre Brood et Siege ; gagnent contre Wrath en environ 17 minutes | – |
| 3 pilotes | gagnent en 9 à 10 minutes, de justesse : la coque du tank finit basse et un pilote peut tomber | perdent |
| 5 pilotes | gagnent en environ 5 minutes | gagnent en 12 à 14 minutes |
| 7 pilotes | gagnent en environ 3,4 minutes | – |
| 10 pilotes | gagnent en environ 2,3 minutes | – |

Un équipage d’un palier inférieur à celui du Gardien perd : un équipage Recrue de cinq ne peut pas tuer un Gardien Vétéran, ni un équipage Vétéran un Gardien Élite. Le Gardien de **votre** clan correspond toujours à **votre** palier.

### Les chiffres des Gardiens {#warden-numbers}

Les Gardiens ont les mêmes chiffres dans tous les mondes (ceux d’Alpha), ainsi que leur gain. Chaque drone, escorte ou garde a les chiffres du second tableau, et ils restent auprès du Gardien : un Brood Drone soigne la coque du Gardien, un Siege Escort ou un Wrath Guard tire au laser.

| Gardien | Coque | Bouclier | Dégâts des lasers (une salve par seconde) | Vitesse | Portée des lasers | Se répare (coque par seconde) | Roquette et secondes entre les tirs |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| Brood Warden I | 166 000 | 136 000 | 43 | 90 | 600 | – | – |
| Brood Warden II | 288 000 | 236 000 | 259 | 90 | 700 | – | – |
| Brood Warden III | 1 060 000 | 870 000 | 1 030 | 90 | 800 | – | – |
| Siege Warden I | 143 000 | 117 000 | 16 | 110 | 600 | 215 | Rivet I: 24 |
| Siege Warden II | 248 000 | 203 000 | 97 | 110 | 700 | 375 | Rivet II: 12 |
| Siege Warden III | 915 000 | 745 000 | 615 | 110 | 800 | 1 385 | Rivet III: 8 |
| Wrath Warden I | 163 000 | 133 000 | 32 | 90 | 700 | 215 | – |
| Wrath Warden II | 282 000 | 231 000 | 194 | 90 | 800 | 375 | – |
| Wrath Warden III | 1 040 000 | 850 000 | 820 | 90 | 900 | 1 385 | – |

| Auxiliaire | Nombre | Coque | Bouclier | Dégâts des lasers (une salve par seconde) | Vitesse | Soigne le Gardien (coque par seconde) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Brood Drone I | 4 | 700 | 500 | 4 | 170 | 120 |
| Brood Drone II | 4 | 1 200 | 900 | 26 | 170 | 210 |
| Brood Drone III | 4 | 4 000 | 3 500 | 105 | 170 | 770 |
| Siege Escort I | 2 | 4 300 | 3 500 | 2 | 175 | – |
| Siege Escort II | 2 | 7 400 | 6 100 | 15 | 175 | – |
| Siege Escort III | 2 | 27 500 | 22 500 | 95 | 175 | – |
| Wrath Guard I | 2 | 4 900 | 4 000 | 6 | 180 | – |
| Wrath Guard II | 2 | 8 500 | 6 900 | 39 | 180 | – |
| Wrath Guard III | 2 | 31 000 | 25 500 | 165 | 180 | – |

### Gain et butin {#warden-pay-and-loot}

Un Gardien paie autant qu’un tas de l’alien lourd du palier : **30 Phantasms** pour un Gardien I, **24 Bulwarks** pour un II et **16 Goombahs** pour un III. C’est une seule cagnotte, partagée selon les dégâts entre les pilotes qui ont infligé au moins 5 % des dégâts, comme pour le meneur d’un [essaim](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays). Vos [bonus de clan](#what-the-boosts-apply-to) s’appliquent à votre part. Selon notre calcul, les crédits couvrent les munitions x1 que brûle un équipage de cinq, et les munitions x2 coûtent plus de Thulium que le Gardien n’en paie : c’est un combat pour les points et la caisse.

| Force du Gardien | Crédits | Thulium | Expérience (XP) | Honneur |
| :--- | ---: | ---: | ---: | ---: |
| I | 90 000 | 360 | 9 000 | 180 |
| II | 120 000 | 600 | 19 200 | 240 |
| III | 240 000 | 1 200 | 48 000 | 384 |

Le Gardien lâche **une caisse** pour le pilote qui a infligé le plus de dégâts ; elle est à lui et à son clan pendant 30 secondes ([Cargaison](/wiki/03-Mechanics/Cargo.md)). Une chance entre parenthèses vaut pour chacun des tirages indiqués : (5 × 50 %) fait cinq tirages à 50 % de chance chacun.

| Gardien | Objet | I | II | III |
| :--- | :--- | :---: | :---: | :---: |
| Brood Warden | Ship Fragment | 3–5 | 8–12 | 15–25 |
| Brood Warden | Advanced Plasma | 100–200 | 300–600 | – |
| Brood Warden | Daraxium | 1–2 (5 × 50 %) | – | – |
| Brood Warden | Nyxite | – | 2–4 (5 × 50 %) | – |
| Brood Warden | Ultra Core | – | – | 300–500 |
| Brood Warden | Quorvium | – | – | 5–10 (60 %) |
| Siege Warden | Ship Fragment | 2–4 | 6–10 | 12–20 |
| Siege Warden | Siphon Battery | 100–200 | 300–500 | 800–1 200 |
| Siege Warden | Roquette de la boutique à crédits (un type, au hasard) | 2–3 | 5–8 | 8–12 |
| Siege Warden | Reinforced Hull Plate | – | 1 (30 %) | – |
| Siege Warden | Roquette épique (un type, au hasard) | – | – | 1–2 (50 %) |
| Wrath Warden | Ship Fragment | 4–6 | 8–12 | – |
| Wrath Warden | Cataclysite | 3–5 | 5–10 | – |
| Wrath Warden | Reinforced Hull Plate | 1 (25 %) | 1 (50 %) | 1–2 (70 %) |
| Wrath Warden | Power Core | – | 1 (15 %) | 1 (35 %) |
| Wrath Warden | Quorvium | – | – | 5–10 (70 %) |
| Wrath Warden | Ancient Control Unit | – | – | 1 (8 %) |

Un Gardien est compté sous son propre nom dans vos statistiques de destructions et ajoute des points PvE à votre [grade](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points) : **10, 15 ou 25** pour le meneur d’un Gardien I, II ou III, et 1 pour chaque auxiliaire.

---

## Points et bonus de clan {#clan-points-and-boosts}

Les points de clan appartiennent au clan. Chaque étape que le clan termine ajoute à son solde. Le **chef et les chefs adjoints** le dépensent sur la carte **Bonus de flotte** de l’onglet Opérations : trois bonus de dix niveaux chacun, et chaque membre les a aussitôt. Un achat est définitif : pas de remboursement, pas de réattribution.

### Les trois bonus {#the-three-boosts}

| Bonus | Niveaux | Par niveau | Niveau maximal | Agit sur |
| :--- | :---: | :---: | :---: | :--- |
| **Dégâts de flotte** | 10 | +0,5 % | +5 % | Dégâts laser aux aliens et aux pilotes |
| **Thulium de flotte** | 10 | +1 % | +10 % | Thulium des destructions et des récompenses de mission |
| **Crédits de flotte** | 10 | +1 % | +10 % | Crédits des destructions et des récompenses de mission |

### Prix {#boost-prices}

Le prix d’un niveau est de **22 points de clan plus 4 par niveau précédent**, et il est le même pour les trois bonus : 400 points pour un bonus, **1 200 pour les trois**, soit douze lignes terminées.

| Niveau | Prix | Total pour ce bonus | Dégâts de flotte | Thulium de flotte | Crédits de flotte |
| :---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 22 | 22 | +0,5 % | +1 % | +1 % |
| 2 | 26 | 48 | +1 % | +2 % | +2 % |
| 3 | 30 | 78 | +1,5 % | +3 % | +3 % |
| 4 | 34 | 112 | +2 % | +4 % | +4 % |
| 5 | 38 | 150 | +2,5 % | +5 % | +5 % |
| 6 | 42 | 192 | +3 % | +6 % | +6 % |
| 7 | 46 | 238 | +3,5 % | +7 % | +7 % |
| 8 | 50 | 288 | +4 % | +8 % | +8 % |
| 9 | 54 | 342 | +4,5 % | +9 % | +9 % |
| 10 | 58 | 400 | +5 % | +10 % | +10 % |

### Sur quoi agissent les bonus {#what-the-boosts-apply-to}

- **Dégâts de flotte** s’ajoute à tous les dégâts laser de votre vaisseau : sur les aliens, les vaisseaux d’essaim, les Gardiens et les autres pilotes. Il **n’agit pas sur les roquettes**, de quelque sorte que ce soit.
- **Thulium de flotte et Crédits de flotte** s’ajoutent au gain des destructions d’aliens (les vôtres, votre part d’un boss et votre part d’une destruction en groupe) et à la récompense de chaque mission que vous réclamez, de niveau, Station ou Défi ([Quêtes](/wiki/03-Mechanics/Quests.md#rewards)). Ils **n’agissent pas sur** les fermes du [Skylab](/wiki/03-Mechanics/Skylab.md#credit-farm-and-thulium-farm), les versements de la banque, les codes bonus ni la récompense de la ligne du jour.
- **Ils s’ajoutent à vos autres bonus** (boosters comme le Damage Amp, les bonus de la [boutique des bonus permanents](/wiki/03-Mechanics/Wipe-Timeline.md#the-permanent-buff-store)) : les pourcentages s’additionnent. Les amplificateurs laser (Amps) n’en font pas partie : ils ajoutent des dégâts fixes, et les pourcentages s’appliquent au total. Cinq points de Dégâts de flotte à côté de 50 d’autres sources font 55, soit 3,3 % de dégâts en plus qu’avant.
- **Une fraction n’est pas perdue.** Un bonus ajoute souvent moins d’une unité à une destruction : 10 % des 4 Thulium d’un Seeker font 0,4. Le jeu garde la fraction et la verse avec les unités de vos destructions suivantes, si bien que dix Seekers paient les 4 qui vous sont dus. La fraction que vous détenez est perdue quand vous vous déconnectez.
- **Arrivées et départs.** Un pilote a les bonus dès l’instant où il rejoint le clan et les perd à l’instant où il le quitte, est renvoyé ou que le clan est dissous. Le clan garde ses niveaux.

### Combien de temps cela prend {#how-long-it-takes}

Un clan qui termine chaque ligne gagne 100 points par jour. Si les officiers achètent à parts égales dans les trois bonus, il a **4 niveaux après la première ligne, 10 après la troisième, 16 après la cinquième et les 30 au jour de saison 12**. Quatorze lignes sont passées quand le jour 15 commence, un tel clan a donc deux lignes d’avance. Un jour non terminé paie tout de même les étapes faites. Après le dernier niveau, la ligne continue et continue de payer votre récompense ; les points continuent de s’ajouter à ce que le clan a gagné cette saison, ce que l’info-bulle des points de clan sur la carte Bonus de flotte indique.

### Points et réinitialisation {#clan-points-and-the-wipe}

À chaque réinitialisation, les **points, les niveaux de bonus et les lignes du clan repartent de zéro**, chaque saison est donc une nouvelle course aux bonus maximaux. Le clan lui-même, ses membres, sa banque et sa taxe restent tels quels.

---

## Diplomatie {#diplomacy}

Les clans peuvent établir des relations diplomatiques formelles avec d’autres organisations en saisissant le tag du clan visé :

- **Alliance** : clans formellement alliés. Le statut amical s’affiche sur la carte.
- **Pacte de non-agression (NAP)** : accord pour ne pas engager d’hostilités.
- **Guerre** : déclaration de guerre formelle. Les cibles de guerre peuvent être attaquées n’importe où sans pénalité.

---

## Amener un ami {#bringing-a-friend}

Un ami qui découvre le jeu peut le rejoindre avec votre code d’invitation personnel et reçoit un pack de départ ; voir [Inviter des amis](/wiki/03-Mechanics/Invite-Friends.md). Une fois dans le jeu, il peut postuler à votre clan comme n’importe quel pilote.
