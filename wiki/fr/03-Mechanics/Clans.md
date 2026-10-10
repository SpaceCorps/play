<!-- wiki-i18n source: 9eea417792cfb043 -->
<!-- wiki-i18n title: Clans -->
# Clans

Fonder un clan ou en rejoindre un vous permet de mettre vos ressources en commun, d’améliorer la banque partagée, de fixer les taux de taxe, de vous coordonner avec les membres de votre faction et de gérer la diplomatie. Un clan a aussi du travail à faire ensemble : chaque jour il reçoit une **ligne du jour** de missions qui se termine par un boss que seul le clan peut blesser, et les points qu’il gagne achètent des **bonus permanents** pour chaque membre. (Sur la page Clan du jeu, un clan s’appelle une *flotte* ; ses points et ses bonus y sont les points de flotte et les bonus de flotte.) **Un clan appartient à un monde et disparaît avec la réinitialisation :** vous ne pouvez rejoindre que les clans de votre propre monde, et à chaque réinitialisation tous les clans sont dissous ([Clans et mondes](#clans-and-worlds)).

**En une minute**

- Chaque clan a une **page du clan** que tout pilote de son monde peut ouvrir : niveau, pilotes, chef, description, lien Discord, conditions, points cumulés et bonus ([La page du clan](#the-clan-page)). Le chef et les chefs adjoints la règlent dans **Gestion** ([Gestion](#management)).
- Un clan a un **monde** (celui de son fondateur), n’accepte que des pilotes de ce monde, et **la réinitialisation le dissout avec son trésor** : versez le Trésor de la flotte avant la fin du compte à rebours ([la réinitialisation](#the-wipe-disbands-every-clan)).
- Le chef et les chefs adjoints écrivent des [annonces](#clan-posts) pour tout le clan, chaque membre voit [sur quelle carte](#where-your-clan-mates-are) volent les autres, la fenêtre [Qui est en ligne](#who-is-online) (touche **H**) invite dans votre groupe n’importe quel pilote de votre monde, le chef peut verser une [prime quotidienne](#4-daily-bonus) depuis le Trésor de la flotte, et l’onglet [Journal](#fleet-log) raconte au clan ce qui s’y est passé.
- Une guerre ne prend fin que si l’autre clan est d’accord, et une alliance ou un pacte prend fin aussitôt quand l’un des deux clans le rompt ([Diplomatie](#diplomacy)).
- Chaque jour de saison, votre clan reçoit une [ligne du jour](#daily-line) : quatre missions à faire dans l’ordre (détruire des aliens, parcourir une distance, parfois abattre des boss d’essaim), puis un [Gardien de clan](#clan-wardens), un boss que vous invoquez et que seul votre clan peut blesser.
- Chaque étape terminée rapporte aussitôt des points de clan : 15, 15, 20, 20 et 30, soit **100 points** pour une ligne complète.
- Le chef et les chefs adjoints dépensent les points dans trois [bonus](#clan-points-and-boosts) de dix niveaux chacun : **Dégâts** (jusqu’à +5 %), **Thulium** (jusqu’à +10 %) et **Crédits** (jusqu’à +10 %).
- Un clan qui termine chaque ligne a acheté tous les niveaux au **jour 12 de la saison**. Les points, les niveaux et le clan lui-même prennent fin avec la réinitialisation.
- Il faut au moins **trois membres** qui ont fait leur part, et **un grand équipage** pour le combat contre le Gardien : depuis la 0.4.13, un Gardien a cinq fois la coque, le bouclier et les dégâts laser qu’il avait, si bien que les équipages qui gagnaient avant, d’environ sept pilotes, perdent maintenant ([quel équipage il faut](#how-big-a-crew)). Un équipage trop petit perd le combat : le clan garde alors les **70 points** des quatre missions, mais la ligne n’est pas terminée et ne paie pas [votre récompense](#the-reward-for-you).
- Un Gardien paie une grosse cagnotte, partagée selon les dégâts, et **chaque pilote qui a infligé 5 % des dégâts ou plus reçoit une caisse privée** avec sa part du butin, que lui seul voit et que lui seul peut ramasser ([gain et butin](#warden-pay-and-loot)). Depuis la 0.4.16, le gain est triplé, et tant qu’un Gardien tient debout, **une vague d’aliens de la carte arrive chaque minute** (toutes les 40 secondes pour le Wrath Warden III, avec un Crystalys dans chaque vague dès qu’il passe sous la moitié de sa coque), dirigée contre les pilotes qui ont touché le Gardien ([vagues](#waves-of-aliens)).
- Votre vaisseau affiche les bonus qu’il a dans la fenêtre **Boosters**, sur une carte à part ([où les voir](#the-three-boosts)).
- La ligne et les bonus demandent un jeu en version 0.4.10 ou plus récente ; la carte de la fenêtre Boosters, la 0.4.12 ou plus récente ; la page du clan, les annonces, la fenêtre des pilotes en ligne, la prime quotidienne, les demandes de paix, le journal et les clans par monde, la 0.4.16 ou plus récente.

![The Boosters window in flight: the Clan boosts card under the timed boosters lists your clan's tag and each boost with its bonus and level](../../img/wiki-img/shots/clan-boosters-window.jpg)
![Buying a level of a clan boost: the sheet shows the level, the bonus the whole fleet gets and the cost in clan points](../../img/wiki-img/shots/clan-boosts.jpg)
![Summoning a Warden for the clan](../../img/wiki-img/shots/clan-warden.jpg)

## Clans et mondes {#clans-and-worlds}

### Un clan, un monde {#one-clan-one-world}

Un clan appartient à un **monde**, Alpha, Beta ou Gamma ([Mondes](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)) : celui du pilote qui le fonde. Fonder ne coûte rien, mais il faut avoir choisi son monde avant.

- **Vous ne pouvez rejoindre qu’un clan de votre propre monde.** Vous ne pouvez ni postuler à un clan d’un autre monde, ni le rejoindre, ni être invité par lui, ni vous allier avec lui, et le jeu vous dit pourquoi quand vous essayez. Un pilote d’un autre monde ne peut pas non plus être invité ni accepté.
- **Vous ne voyez que les clans de votre monde.** Le registre des flottes et les deux classements (PvE et PvP) ne listent qu’eux, et la page d’un clan d’un autre monde ne s’ouvre pas. Les noms et les tags de clan restent uniques entre les trois mondes : un nom pris en Gamma n’est pas libre en Alpha avant la réinitialisation.
- **Les alliances, les pactes et les guerres n’existent qu’entre clans d’un même monde.** Ceux qui ont été conclus entre mondes avant la 0.4.16 tiennent jusqu’à ce qu’on les rompe, et une guerre de ce genre peut encore se terminer d’un commun accord ([Diplomatie](#diplomacy)).
- **Les clans qui existaient déjà** ont pris le monde de leur chef. Un membre d’un autre monde qui était déjà dedans reste jusqu’à la réinitialisation ou jusqu’à ce qu’il parte ; on ne peut pas le réadmettre.

### La réinitialisation dissout tous les clans {#the-wipe-disbands-every-clan}

À la [réinitialisation](/wiki/03-Mechanics/Wipe-Timeline.md), tous les clans sont dissous, dans les trois mondes. Disparaissent avec eux : les membres, le **Trésor de la flotte**, les candidatures et les invitations, les alliances, les pactes et les guerres, les annonces, le journal, les conditions, la description et le lien Discord, la prime quotidienne, les points de clan et les niveaux de bonus, et la ligne du jour. Le nom et le tag du clan redeviennent libres, et un nouveau clan repart du niveau 1.

- **Vous gardez** tous les crédits que le clan vous a déjà versés (versements, primes quotidiennes, récompenses de la ligne) et votre plafond de dons, que la réinitialisation ne remet pas à zéro ([Dons](#2-donations)).
- **Vous perdez** le clan et **tout ce qui reste dans son Trésor de la flotte**, sauf si le chef ou un chef adjoint l’a versé aux pilotes avant la réinitialisation ([Versements de la banque](#3-bank-payouts)).
- **Le compte à rebours prévient les clans.** Avec sa première alerte, 5 minutes avant la réinitialisation, chaque pilote qui est dans un clan reçoit une ligne et une notification : la réinitialisation dissout tous les clans, leur trésor est perdu, et les chefs et chefs adjoints doivent verser le Trésor de la flotte à leurs pilotes maintenant. La carte du Trésor de la flotte dans Gestion le dit aussi.

---

## La page du clan {#the-clan-page}

Chaque clan a une page que **tout pilote de son monde peut ouvrir**, qu’il soit dans un clan ou non. Cliquez sur le nom du clan dans le **registre des flottes** (Communauté › Clan, tant que vous n’êtes dans aucun clan), dans l’un des deux **classements** ou sur le **profil d’un pilote** ; le bouton **Aperçu de la page du clan** de Gestion montre votre propre clan tel que le voit un pilote extérieur. La page montre :

- **Le clan** : son nom et son tag, son niveau, ses pilotes actuels et le nombre que son niveau permet (« Niveau 2 · 14/25 pilotes »), le chef (cliquez sur son nom pour ouvrir son profil), son monde, la façon dont les pilotes le rejoignent (Ouvert, Candidatures ou Sur invitation), la **description** (200 caractères au plus, écrite par le chef ou un chef adjoint) et le **lien Discord** avec un bouton **Ouvrir Discord**. Seuls les liens `discord.gg` et `discord.com/invite` sont acceptés, et le jeu n’en ouvre aucun autre.
- **Points cumulés** : les points d’expérience, d’honneur, de classement PvE et de classement PvP de tous les pilotes qui sont dans le clan en ce moment, additionnés.
- **Conditions** ([plus bas](#requirements)), avec une coche ou une croix pour ce que vous remplissez.
- **Boosters du clan** : les bonus que le clan a achetés et pendant combien de jours ils durent, jusqu’à la réinitialisation.
- **Postuler** ou **Rejoindre**, comme dans le registre des flottes. Le bouton est grisé, avec la raison, quand le clan est plein ou qu’il vous manque une condition.

La page ne montre jamais la liste des membres, les trésors, les candidatures ni les points de clan : cela est réservé aux membres du clan.

### Conditions {#requirements}

Le chef et les chefs adjoints peuvent demander deux choses à un pilote qui veut entrer :

- **Un niveau minimum**, de 1 (aucune condition) à 21.
- **Un grade minimum** : un palier de grade de corporation, de **Pilote** (aucune condition) à **Amiral** : Pilote, Sergent, Lieutenant, Capitaine, Commandant, Colonel, Général, Amiral ([Grades](/wiki/03-Mechanics/Ranks.md)). Un palier compte à partir de son grade le plus bas : un clan qui demande Capitaine accepte un Capitaine junior et tous les pilotes au-dessus. C’est le grade que vous avez maintenant dans le classement de votre corporation, pas le monde dans lequel vous volez.

Elles sont vérifiées quand un pilote **postule ou rejoint**. L’**invitation** d’un officier les ignore, de même qu’une candidature qu’un officier accepte. Le registre des flottes les montre sous forme de petites pastilles sous le nom du clan, en rouge pour celle que vous ne remplissez pas ; un clan qui n’a rien réglé n’exige rien.

---

## Progression du clan {#clan-progression}

Les clans commencent au niveau 1 et peuvent monter jusqu’au niveau 5. Améliorer le clan demande de payer des crédits depuis la **banque du clan** (le jeu l’appelle le **Trésor de la flotte**). Les améliorations augmentent la capacité de membres et les plafonds de versement quotidiens ; les bonus du clan s’achètent avec des points de clan, pas avec des niveaux.

| Niveau du clan | Limite de membres | Limite de versement quotidienne (par membre) | Coût d’amélioration (crédits) |
| :---: | :---: | :---: | :--- |
| **Niveau 1** | 15 | 1 000 000 cr | — |
| **Niveau 2** | 25 | 2 000 000 cr | 10 000 000 cr |
| **Niveau 3** | 50 | 3 000 000 cr | 100 000 000 cr |
| **Niveau 4** | 75 | 4 000 000 cr | 1 000 000 000 cr |
| **Niveau 5** | 100 | 5 000 000 cr | 10 000 000 000 cr |

---

## Gestion {#management}

L’onglet **Gestion** de la fenêtre du clan (appelé Admin jusqu’à la 0.4.16) est réservé au chef et aux chefs adjoints ; les autres membres voient un cadenas. Ses cartes, de haut en bas :

- **Protocole de recrutement** : la façon dont les pilotes rejoignent. **Ouvert** accepte aussitôt tout pilote qui remplit les conditions, **Candidatures** laisse un officier décider de chaque candidature, **Sur invitation** n’accepte personne qui n’a pas été invité.
- **Configuration fiscale** : le taux de taxe quotidien, de 0 % à 5 % ([Taxation quotidienne](#1-daily-taxation)).
- **Conditions de candidature** : le niveau minimum et le grade minimum ([Conditions](#requirements)).
- **Page du clan** : la description (200 caractères) et le lien Discord que lisent les pilotes extérieurs au clan, et le bouton **Aperçu de la page du clan** ([La page du clan](#the-clan-page)). Les membres du clan lisent le lien dans l’Aperçu.
- **Trésor de la flotte** : les crédits des dons et de la taxe quotidienne, avec le rappel que la réinitialisation dissout le clan et que le trésor est perdu.
- **Trésor de Thulium** : une seconde bourse, affichée à côté du Trésor de la flotte dans l’en-tête de la fenêtre du clan. Elle est vide et rien n’y entre ni n’en sort : elle est réservée à une mise à jour future.
- **Progression de la flotte** et **Améliorations** : les cinq niveaux avec le nombre de pilotes que chacun accueille, le plus qu’on puisse verser à un membre par jour et le prix, et le bouton d’amélioration du chef. Seul le chef améliore le clan.
- **Prime quotidienne** : le montant du chef pour chaque grade ([Prime quotidienne](#4-daily-bonus)).

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

### 4. Prime quotidienne {#4-daily-bonus}

Le chef peut verser à chaque membre une prime fixe depuis le Trésor de la flotte, une fois par jour.

- **La fixer.** Dans la carte **Prime quotidienne** de Gestion, le chef saisit un montant pour chaque rang : Pilote, Aîné, Chef adjoint et Chef. **0 désactive un rang** ; tout autre montant va de **1 000 à 1 000 000 de crédits**. Les chefs adjoints voient la carte et ne peuvent pas la changer. Enregistrer ne prend rien au trésor. La carte montre ce que coûterait une journée complète si tous les pilotes jouaient, et pour combien de jours le trésor suffirait.
- **Le versement.** Un membre est payé **une fois par jour de saison**, à sa première vérification du jour : quand il se connecte, quand le jour change pendant qu’il est en ligne, et quand le chef enregistre de nouveaux montants. Un jour de saison, ce sont les 24 heures de la ligne du clan, pas minuit UTC ([Le jour](#the-day)). Le pilote reçoit une ligne Système et une ligne dans le Journal de jeu, et l’Aperçu affiche « Prime quotidienne : X crédits » et si elle a été versée aujourd’hui.
- **Qui.** Un pilote qui est dans le clan depuis **au moins 24 heures**, et **une prime par pilote et par jour de saison, tous clans confondus** : qui change de clan pour en toucher davantage est payé une fois.
- **Un trésor trop court.** Le trésor ne paie que ce qu’il a et ne descend jamais sous zéro. Quand il ne peut pas payer le montant d’un membre, celui-ci est sauté pour la journée, même si le trésor est rempli plus tard dans le jour, et le [Journal de la flotte](#fleet-log) le note une fois. Les pilotes sont payés dans l’ordre de leur connexion jusqu’à ce que le trésor soit vide.
- **Pas un versement.** La prime n’utilise pas le plafond de versement quotidien d’un membre.

---

## Hiérarchie et rôles {#hierarchy-roles}

Les clans utilisent une structure de grades fondée sur les rôles pour gérer les permissions :

- **Chef (rôle 3)** : dispose d’un accès administratif complet, dont l’amélioration du clan, la fixation des taxes, des conditions, de la page du clan et de la prime quotidienne, la diplomatie, les annonces, les promotions, les renvois et la dissolution du clan.
- **Chef adjoint (rôle 2)** : peut fixer les taux de taxe, les conditions et la page du clan, verser des crédits, gérer la diplomatie, écrire des annonces, et promouvoir ou rétrograder les grades inférieurs.
- **Aîné (rôle 1)** : membre de confiance qui peut accepter les nouvelles candidatures au clan.
- **Membre (rôle 0)** : joueur standard, sans permission d’administration.

### Tableau des permissions {#permissions-table}

| Action | Chef | Chef adjoint | Aîné | Membre |
| :--- | :---: | :---: | :---: | :---: |
| **Dissoudre le clan** | ✅ | ❌ | ❌ | ❌ |
| **Améliorer le clan** | ✅ | ❌ | ❌ | ❌ |
| **Fixer le taux de taxe** | ✅ | ✅ | ❌ | ❌ |
| **Fixer les conditions et la page du clan** | ✅ | ✅ | ❌ | ❌ |
| **Fixer la prime quotidienne** | ✅ | ❌ | ❌ | ❌ |
| **Écrire des annonces du clan** | ✅ | ✅ | ❌ | ❌ |
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

## Annonces du clan {#clan-posts}

Une **annonce** est une courte note pour tout le clan, un tableau d’affichage pour les nouvelles des officiers. Elle se trouve dans l’onglet **Annonces** de la fenêtre du clan.

- **Qui écrit.** Le chef et les chefs adjoints. Tous les membres lisent. Le chef et les chefs adjoints suppriment n’importe quelle annonce, et un auteur supprime la sienne, même après avoir été rétrogradé.
- **Le texte.** Jusqu’à **200 caractères** sur une seule ligne, avec un compteur sous la zone de saisie ; Entrée l’envoie. **Pas de liens** : une annonce qui en contient un est refusée.
- **Limites.** Une annonce par auteur toutes les **10 secondes**, et le clan en garde **20** à la fois : la 21e chasse la plus ancienne.
- **Combien de temps.** Une annonce dure jusqu’à la réinitialisation.
- **Notification.** Les membres en ligne reçoivent une notification (« Nova a publié une annonce pour la flotte. ») et un son discret, au plus une fois toutes les secondes et demie, quel que soit le nombre d’annonces. La liste montre la plus récente en premier, avec l’auteur et depuis combien de temps.

## Où sont vos camarades de clan {#where-your-clan-mates-are}

La colonne **Carte** de la liste des membres montre le secteur dans lequel vole chaque pilote de votre clan (« T-2 »), avec le monde devant quand ce n’est pas le vôtre (« Beta · T-2 »). Elle est relue toutes les 10 secondes tant que la liste est ouverte. Seule la **carte** est montrée, jamais de coordonnées, et rien n’est conservé. Un pilote **amarré ou déconnecté** apparaît **Hors ligne**, tout comme un pilote dont le vaisseau occulté ne serait pas visible pour vous sur une carte ([Cloaking CPU](/wiki/06-Items/Extras.md#cloaking-cpu)) : un clan ne lève pas une occultation.

## Qui est en ligne {#who-is-online}

Le bouton **Qui est en ligne** de la barre d’outils système (en haut à droite) ou la touche **H** (réassignable dans Paramètres › Commandes) ouvre la fenêtre **Pilotes en ligne**.

- **Qui est listé.** Les pilotes qui volent en ce moment dans **votre monde**, vous excepté : Alpha, Beta et Gamma ne se croisent pas. Un pilote dont le vaisseau occulté ne vous est pas visible n’est ni listé ni compté. La fenêtre montre au plus **100** lignes, vos camarades de clan d’abord, puis les niveaux les plus élevés, puis par nom, et le vrai nombre de pilotes en ligne en haut.
- **Ce que montre une ligne.** Le nom, le niveau, la corporation, le tag de clan et le symbole de grade du pilote : ce que le chat et les classements montrent déjà. Jamais une position, une carte ni l’état du vaisseau.
- **Recherche.** Tapez une partie d’un nom ou d’un tag de clan ; la fenêtre interroge de nouveau le serveur quand la liste a été coupée.
- **Inviter.** Le bouton **Inviter** d’une ligne est l’invitation propre de la fenêtre Groupe ([Groupes](/wiki/03-Mechanics/Groups.md)), avec les mêmes réponses et les mêmes refus (le pilote est dans un groupe, le groupe est plein, Ne pas déranger est activé). Le bouton est grisé, avec la raison au survol, quand le jeu sait déjà que l’invitation sera refusée.
- La liste est relue toutes les 10 secondes tant que la fenêtre est ouverte.

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
- Une étape rapporte ses points **à l’instant où elle est terminée**. Un clan qui finit les quatre missions puis ne parvient pas à réunir un équipage pour le Gardien, ou perd le combat, garde tout de même **70 points** ; [votre récompense](#the-reward-for-you) ne vient qu’avec la ligne terminée.
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
- **Quelles destructions.** Seulement l’alien de l’étape ouverte : le Seeker, Phantasm, Bulwark ou Goombah ordinaire. Les vaisseaux d’essaim, les autres pilotes et les auxiliaires d’un Gardien ne comptent pas comme ces aliens. Une destruction compte pour le monde où elle a lieu, et plus dans un monde plus fort : **1 en Alpha, 1,5 en Beta, 2 en Gamma** ([Mondes](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)). Une étape de boss compte les boss des [essaims](/wiki/05-Swarms/Swarms.md), un pour chaque clan qui a un pilote ayant infligé au moins 5 % des dégâts.
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

Quand la ligne est terminée, c’est-à-dire quand le Gardien est détruit, chaque membre qui a atteint le minimum et qui est toujours dans le clan est payé, même hors ligne. Une ligne qui se termine sans le Gardien ne paie aucune récompense, quoi qu’aient fait les quatre missions. Le versement est fixe : les bonus, les boosters et le monde ne le changent pas.

| Palier | Crédits | Thulium |
| :--- | ---: | ---: |
| Recrue | 5 000 | 20 |
| Vétéran | 15 000 | 60 |
| Élite | 22 000 | 90 |

---

## Gardiens de clan {#clan-wardens}

Un **Gardien de clan** est le boss de la fin de la ligne du jour. Ce n’est pas l’un des [essaims](/wiki/05-Swarms/Swarms.md) publics qui rôdent dans un secteur : votre clan **l’invoque** et **seul votre clan peut le blesser**. Trois Gardiens se relaient, un par jour : jour 1 **Brood**, jour 2 **Siege**, jour 3 **Wrath**, jour 4 de nouveau Brood, et ainsi de suite (le jour 15 est un jour Wrath). Chacun existe en trois forces, **I, II et III**, fixées par le palier du clan. Un Gardien est un alien d’un genre à part, comme les vaisseaux d’un essaim : il ne compte pas comme un Seeker, un Phantasm ni aucun autre alien. Un Gardien est très fort : il a cinq fois la coque, le bouclier et les dégâts laser qu’il avait avant la 0.4.13, c’est donc un combat pour le plus grand équipage que votre clan puisse réunir ([quel équipage il faut](#how-big-a-crew)). Depuis la 0.4.16, le Brood Warden III a **moitié moins** de coque et de bouclier, ses drones soignent moitié moins et arrivent moitié moins vite, et chaque Gardien amène des [vagues d’aliens](#waves-of-aliens) tant qu’il tient debout. Depuis la 0.4.20, un Wrath Warden **fonce sur le pilote qui l’a touché** au lieu de rester là où il a été appelé, le Wrath Warden III amène plus d’aliens, plus souvent, et un Crystalys sous la moitié de sa coque, et tout ce qu’un Gardien amène arrive dirigé contre les pilotes qui l’ont touché.

| Gardien | Jours de saison | Rôle | Comment il combat |
| :--- | :--- | :--- | :--- |
| **Brood Warden** | 1, 4, 7, 10 … | Gardien de la ruche : répartissez votre tir | Quatre petits **Brood Drones** soignent sa coque, et un nouveau arrive toutes les 8 secondes tant que moins de quatre sont en vie (toutes les 16 secondes pour le Brood Warden III). Tirez d’abord sur les drones, puis sur le Gardien. |
| **Siege Warden** | 2, 5, 8, 11 … | Briseur de siège : restez en mouvement | Il rôde et tire une [roquette Rivet](/wiki/06-Items/Rockets.md#the-twelve-rockets) droite sur le premier pilote qui l’a touché, et il se répare tout seul. Deux **Siege Escorts** ajoutent un tir laser. Restez en mouvement et servez de cible à tour de rôle. |
| **Wrath Warden** | 3, 6, 9, 12 … | Seigneur de guerre : battez la rage | Il fonce sur le premier pilote qui l’a touché, s’arrête à portée de ses lasers et se répare tout seul. Sous la moitié de sa coque, ses lasers frappent **une fois et demie plus fort**. Deux **Wrath Guards** restent avec lui et ajoutent du tir laser. Abattez-le vite et gardez vos boucliers levés. |

### Invoquer un Gardien {#calling-a-warden}

- **Quand.** Une fois l’étape 4 terminée. Un clan a **deux invocations par jour**, un seul Gardien dehors à la fois, et il doit rester **au moins 30 minutes** de jour.
- **Qui.** Le chef ou un chef adjoint.
- **Comment.** En vol : le bouton **Invoquer ici** apparaît sur l’écran de vol dès que l’étape 4 est terminée, et vous demande de confirmer. Soyez hors des zones sûres, dans un secteur de corporation **x-2, x-3 ou x-4** (de n’importe quelle corporation) de votre monde. L’onglet Opérations montre le Gardien du jour, les invocations restantes et pourquoi le bouton est grisé, mais un Gardien s’invoque depuis le vaisseau.
- **Où il apparaît.** À 3 000 à 4 500 unités de votre vaisseau, dans votre monde : seuls les pilotes de ce monde peuvent l’atteindre. L’onglet recommande **x-2 pour un clan Recrue, x-3 pour Vétéran et x-4 pour Élite**. Les [règles de PvP](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) habituelles du secteur choisi s’appliquent toujours.
- **Montée en charge.** Il reste **90 secondes** protégé et passif (« montée en charge »), et chaque pilote du clan en ligne est informé de l’endroit. Volez vers lui pendant qu’il se charge : passé les 90 secondes, il est actif. Une capsule sous le badge de zone sûre de l’écran de vol le suit : son nom, « montée en charge » avec le temps restant, puis « actif » avec son secteur et le temps avant son retrait, et « enragé » quand un Wrath Warden passe sous la moitié de sa coque.
- **Seulement votre clan.** Les tirs des pilotes de tout autre clan sont ignorés et ne le font pas riposter.
- **Comment cela se termine.** Quand il est détruit. Il **se retire** 40 minutes après son activation, à la fin du jour, quand aucun pilote de votre clan n’a été en vol sur sa carte pendant 2 minutes, ou au redémarrage du serveur (l’invocation est alors rendue). Un Gardien qui se retire coûte une invocation, et l’appel suivant est le même Gardien à pleine force.

### Combattre un Gardien {#fighting-a-warden}

- **Un Gardien combat le premier pilote qui l’a touché**, comme tout boss : laissez le vaisseau le plus robuste de l’équipage commencer, et utilisez [Shield Surge et Emergency Repair](/wiki/03-Mechanics/Abilities.md).
- **Venez avec le plus grand équipage possible et des munitions x2** ([Lasers](/wiki/06-Items/Lasers.md#laser-ammunition)). Les équipages qui gagnaient avant la 0.4.13, d’environ sept pilotes, perdent maintenant. Le tableau ci-dessous est un calcul et le meilleur cas : même là, dix pilotes perdent contre tous les Gardiens, et le plus petit équipage qui peut gagner compte 18 à 26 pilotes avec des munitions x2 et 26 à 38 avec des munitions x1. Les vagues ci-dessous ne sont pas dans ce calcul.
- **Brood :** les drones soignent sa coque, et un équipage qui les ignore perd, même un grand. Tuez-les d’abord et continuez à les tuer : un nouveau arrive au bout de 8 secondes (16 pour le Brood Warden III).
- **Siege :** ses roquettes sont droites et non guidées, un vaisseau qui reste en mouvement en esquive donc la plupart. Restez en mouvement et servez de cible à tour de rôle.
- **Wrath :** dès que sa coque passe sous la moitié, chaque salve frappe une fois et demie plus fort, la seconde moitié du combat est donc la dangereuse. Abattez la première moitié vite, gardez les boucliers levés et gardez Emergency Repair pour la rage. Depuis la 0.4.20, il ne reste plus immobile : il fonce sur le premier pilote qui l’a touché, à 90 unités par seconde, jusqu’à être à portée de ses lasers (700, 800 ou 900 unités selon la force) et tire de là, si bien qu’une arme à plus longue portée ne peut plus le tirer sans qu’il riposte. Les Brood et Siege Wardens n’ont pas changé : le Brood Warden reste là où il a été appelé, le Siege Warden reste en mouvement.
- **Ce qu’un Gardien amène vient pour le pilote qui l’a touché.** Depuis la 0.4.20, chaque alien d’une vague, et chaque drone, escorte ou garde qui arrive pendant qu’on combat le Gardien, va sur les pilotes qui ont touché le Gardien, le premier d’abord, à l’instant où il arrive, sans avoir été touché lui-même.

### Vagues d’aliens {#waves-of-aliens}

Depuis la 0.4.16, un Gardien ne se tient pas seul. À partir du moment où il est **armé** (les 90 secondes de chauffe n’ont pas de vagues, pour que l’équipage puisse se rassembler), une **vague** d’aliens ordinaires de la carte où il se trouve arrive **toutes les 60 secondes**, tant que le Gardien tient debout. Le tableau donne les vagues de huit des neuf Gardiens ; les [vagues du Wrath Warden III](#wrath-iii-waves) sont plus lourdes.

| Carte | Une vague | Au plus en vie à la fois |
| :--- | :--- | ---: |
| x-2 | 5 Phantasm | 15 |
| x-3 | 10 Phantasm | 30 |
| x-4 | 10 Bulwarks | 30 |

- **Trois vagues au plus sont en vie.** Une vague est en vie tant que l’un de ses aliens l’est. Une vague due quand trois sont en vie est sautée, pas gardée pour plus tard ; la suivante est due une minute après.
- **Ce sont les propres aliens de la carte**, du genre qui attaque les pilotes, faits comme la carte les fait : un monde plus fort leur donne plus de coque, de bouclier et de dégâts ([Mondes](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)). Ils arrivent à 500 à 1 200 unités du Gardien, répartis autour de lui.
- **Ils ne font pas partie du combat pour le Gardien.** Ils ne soignent rien, et leur tirer dessus n’ajoute rien à votre part des dégâts au Gardien. N’importe quel pilote de la carte peut les tuer. Chacun paie le gain ordinaire de son alien dans votre monde et rapporte des points PvE : une vague entière de 5 Phantasm paie 15 000 crédits en Alpha, une vague de 10 Bulwarks 50 000, moins de 2 % de ce que paie le Gardien le plus faible.
- **Ils s’arrêtent avec le Gardien.** Quand il est détruit ou se retire, il n’en vient plus ; les aliens déjà sortis restent et sont les aliens ordinaires de la carte. Un redémarrage du serveur les fait disparaître avec le Gardien.
- **Le clan est prévenu.** Chaque vague est annoncée dans l’onglet Système du chat et dans le Journal de jeu : « Brood Warden I appelle des renforts dans M-3 : 10 Phantasm. »
- **Elles arrivent dirigées (0.4.20).** Les aliens d’une vague arrivent en sachant qui le Gardien combat : ils vont sur les pilotes qui l’ont touché, le premier d’abord, dès qu’ils apparaissent, et restent après eux tant que le Gardien est touché. Un Gardien que personne ne combat envoie des aliens qui rôdent et attirent quiconque s’approche, comme avant.

#### Les vagues du Wrath Warden III {#wrath-iii-waves}

Depuis la 0.4.20, le **Wrath Warden III** amène plus, et plus souvent : une vague toutes les **40 secondes**, les trois quarts du nombre de cet alien que la carte contient, et jusqu’à **quatre vagues** en vie. Sous la moitié de sa coque (la ligne où il entre en rage), **chaque vague compte aussi un Crystalys**, en plus de la taille de la vague.

| Carte | Une vague | Au plus en vie à la fois |
| :--- | :--- | ---: |
| x-2 | 8 Phantasm | 32, et jusqu’à 4 Crystalys |
| x-3 | 15 Phantasm | 60, et jusqu’à 4 Crystalys |
| x-4 | 15 Bulwarks | 60, et jusqu’à 4 Crystalys |

- **Le Crystalys** est l’alien ordinaire le plus lourd du jeu : 256 000 de coque, 160 000 de bouclier, 10 000 de dégâts par salve à 900 unités, vitesse 230 (dans un monde plus fort, plus de coque, de bouclier et de dégâts). Il paie ce que paie tout Crystalys : **75 000 crédits, 200 Thulium, 12 000 XP et 52 d’honneur en Alpha** (le double en Beta, le triple en Gamma), et lâche son butin ordinaire. Il fait partie de sa vague : une vague est en vie tant que son Crystalys l’est, donc un Crystalys laissé debout garde en vie l’une des quatre vagues.
- **Quatre vagues au plus sont en vie.** Une vague due quand quatre sont en vie est sautée, comme pour les autres Gardiens. Au-dessus de la moitié de sa coque, le Gardien envoie la vague sans le Crystalys.
- **Elles sont annoncées en deux lignes** : « Wrath Warden III appelle des renforts dans M-3 : 15 Phantasm. » et « Wrath Warden III appelle des renforts dans M-3 : 1 Crystalys. »
- **Ce qu’elles paient.** Une vague entière de 15 Bulwarks paie 75 000 crédits en Alpha, et avec son Crystalys 150 000 : environ 2 % des 7 200 000 que paie le Gardien lui-même.
- **Ce qu’elles demandent à l’équipage.** Le calcul de [quel équipage il faut](#how-big-a-crew), avec ces vagues et le Crystalys, donne **31 pilotes en x-2, 32 en x-3 et 38 en x-4** avec des munitions x2 (26 sans vagues), et 36, 38 et 50 en Gamma, où les aliens des vagues sont deux fois plus forts. Un clan de niveau 3 compte 50 membres. Comme le tableau de cette section, c’est calculé et non mesuré, et c’est le meilleur cas.

### Quel équipage il faut {#how-big-a-crew}

> [!NOTE]
> Depuis la 0.4.13, chaque Gardien et chaque aide a **cinq fois** la coque, le bouclier, les dégâts laser, l’auto-réparation et le soin qu’ils avaient en 0.4.12 (la vitesse, la portée et le nombre d’aides sont les mêmes) ; depuis la 0.4.16, le Brood Warden III n’a que la moitié de cette coque et de ce bouclier, et ses drones la moitié de ce soin. Il met cinq fois plus de temps à tomber et frappe cinq fois plus fort pendant tout ce temps, si bien que les équipages qui gagnaient avant perdent maintenant. **Nous n’avons pas encore combattu les nouveaux Gardiens dans le jeu : les durées ci-dessous sont calculées, pas mesurées.** Elles montrent le **meilleur cas** de l’équipage : l’équipage est dans les vaisseaux et l’équipement pour lesquels le palier est fait, chaque pilote utilise Shield Surge et Emergency Repair dès qu’ils sont prêts, l’équipage tire d’abord sur les aides du Gardien quand c’est mieux, le Gardien et ses aides tirent tous sur le pilote qui a touché le premier, et personne n’esquive. En 0.4.12, le même calcul était plus optimiste que les combats menés dans le jeu lui-même avec des pilotes scriptés : un vrai combat peut donc être plus dur que le tableau, et un bon équipage peut faire mieux. Prenez-le comme un repère, pas comme une promesse. **Les vagues d’aliens ne sont pas dans le calcul** : un vrai combat est donc plus dur que le tableau.

Le tableau montre le meilleur cas ; en jeu, amenez autant de monde que possible.

| Équipage | Avec munitions x2 | Avec munitions x1 |
| :--- | :--- | :--- |
| 5 pilotes | perdent contre tous les Gardiens ; le Gardien garde 88 à 96 % de sa coque et de son bouclier | perdent |
| 10 pilotes | perdent contre tous les Gardiens ; le Gardien garde 55 à 85 % de sa coque et de son bouclier | perdent |
| 20 pilotes | ne gagnent que contre les Siege Warden I et II, en 8,5 à 8,6 minutes, en perdant 7 vaisseaux, et contre le Brood Warden III, en 3,7 minutes, en perdant 8 vaisseaux | perdent |
| 30 pilotes | gagnent contre tous les Gardiens en 2,0 à 5,1 minutes, en perdant de 3 à 10 vaisseaux | ne gagnent que contre les Siege Warden I et II, en 12,6 à 12,8 minutes, en perdant 10 vaisseaux, et contre le Brood Warden III, en 5,0 minutes, en perdant 11 vaisseaux |

Dans le calcul, le plus petit équipage qui gagne avec des munitions x2 compte **18 à 26 pilotes** (le moins contre les Siege Warden I et II et le Brood Warden III) et perd **9 à 17** vaisseaux en le faisant ; avec des munitions x1, il compte **26 à 38** pilotes et perd 13 à 27. Les lasers d’un Gardien frappent par centaines par salve en force I (240 à 645) et par milliers en force III (9 225 à 15 450), et ses aides s’y ajoutent : le vaisseau qu’il combat tombe en 19 à 59 secondes, puis il se tourne vers le suivant, si bien que même un équipage qui gagne perd beaucoup de vaisseaux.

Le tableau vaut pour un équipage dans l’équipement du palier propre au Gardien. Des vaisseaux plus faibles font moins bien. Le Gardien de **votre** clan correspond toujours à **votre** palier, que fixent les cinq meilleurs pilotes du clan : amenez-les.

**Un clan trop petit pour son Gardien** n’est pas exclu. Les quatre missions paient leurs **70 points** quoi qu’il arrive au Gardien, les points achètent des bonus, et le clan peut rappeler le Gardien s’il lui reste une invocation (il y en a deux par jour) : si l’équipage tombe et reste à l’écart, le Gardien se retire, ce qui coûte une invocation, et l’appel suivant le ramène à pleine force. Mais la ligne n’est pas terminée, donc personne ne reçoit [votre récompense](#the-reward-for-you), et un clan qui ne tue jamais son Gardien a les 30 niveaux de bonus au plus tôt au jour de saison 18, et non au jour 12 ([combien de temps cela prend](#how-long-it-takes)).

### Les chiffres des Gardiens {#warden-numbers}

Les Gardiens ont les mêmes chiffres dans tous les mondes (ceux d’Alpha), ainsi que leur gain. Chaque drone, escorte ou garde a les chiffres du second tableau, et ils restent auprès du Gardien : un Brood Drone soigne la coque du Gardien, un Siege Escort ou un Wrath Guard tire au laser. Une salve est l’ensemble des tirs de tous les lasers d’un vaisseau en une seconde, tirée entre 80 et 100 % du chiffre indiqué ; un Wrath Warden sous la moitié de sa coque frappe une fois et demie plus fort. Le Gardien et ses aides tirent tous sur le pilote que le Gardien combat, leurs salves s’additionnent donc : un Brood Warden III avec ses quatre drones met jusqu’à 21 750 par seconde sur un seul vaisseau. La [roquette Rivet](/wiki/06-Items/Rockets.md#the-twelve-rockets) du Siege Warden n’est pas tirée au hasard : elle frappe à **2 500** au plus en force I, **5 000** en force II et **7 500** en force III, alors que le Rivet d’un pilote est tiré entre un plus petit et un plus grand chiffre. Elle file droit : un vaisseau qui continue de bouger est manqué.

| Gardien | Coque | Bouclier | Dégâts des lasers (une salve par seconde) | Vitesse | Portée des lasers | Se répare (coque par seconde) | Roquette et secondes entre les tirs |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| Brood Warden I | 830 000 | 680 000 | 645 | 90 | 600 | – | – |
| Brood Warden II | 1 440 000 | 1 180 000 | 3 885 | 90 | 700 | – | – |
| Brood Warden III | 2 650 000 | 2 175 000 | 15 450 | 90 | 800 | – | – |
| Siege Warden I | 715 000 | 585 000 | 240 | 110 | 600 | 1 075 | Rivet I: 24 |
| Siege Warden II | 1 240 000 | 1 015 000 | 1 455 | 110 | 700 | 1 875 | Rivet II: 12 |
| Siege Warden III | 4 575 000 | 3 725 000 | 9 225 | 110 | 800 | 6 925 | Rivet III: 8 |
| Wrath Warden I | 815 000 | 665 000 | 480 | 90 | 700 | 1 075 | – |
| Wrath Warden II | 1 410 000 | 1 155 000 | 2 910 | 90 | 800 | 1 875 | – |
| Wrath Warden III | 5 200 000 | 4 250 000 | 12 300 | 90 | 900 | 6 925 | – |

| Auxiliaire | Nombre | Coque | Bouclier | Dégâts des lasers (une salve par seconde) | Vitesse | Soigne le Gardien (coque par seconde) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Brood Drone I | 4 | 3 500 | 2 500 | 60 | 170 | 600 |
| Brood Drone II | 4 | 6 000 | 4 500 | 390 | 170 | 1 050 |
| Brood Drone III | 4 | 20 000 | 17 500 | 1 575 | 170 | 1 925 |
| Siege Escort I | 2 | 21 500 | 17 500 | 30 | 175 | – |
| Siege Escort II | 2 | 37 000 | 30 500 | 225 | 175 | – |
| Siege Escort III | 2 | 137 500 | 112 500 | 1 425 | 175 | – |
| Wrath Guard I | 2 | 24 500 | 20 000 | 90 | 180 | – |
| Wrath Guard II | 2 | 42 500 | 34 500 | 585 | 180 | – |
| Wrath Guard III | 2 | 155 000 | 127 500 | 2 475 | 180 | – |

### Gain et butin {#warden-pay-and-loot}

Un Gardien paie ce que paierait un tas de l’alien lourd du palier : **900 Phantasms** pour un Gardien I, **720 Bulwarks** pour un II et **480 Goombahs** pour un III, trois fois plus qu’avant la 0.4.16. C’est une seule cagnotte, partagée selon les dégâts entre les pilotes qui ont infligé au moins 5 % des dégâts, comme pour le meneur d’un [essaim](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays). Vos [bonus de clan](#what-the-boosts-apply-to) s’appliquent à votre part. La cagnotte ne grandit pas avec les dégâts que vous encaissez, les munitions que vous brûlez ou les vaisseaux que vous perdez.

| Force du Gardien | Crédits | Thulium | Expérience (XP) | Honneur |
| :--- | ---: | ---: | ---: | ---: |
| I | 2 700 000 | 10 800 | 270 000 | 5 400 |
| II | 3 600 000 | 18 000 | 576 000 | 7 200 |
| III | 7 200 000 | 36 000 | 1 440 000 | 11 520 |

**Chaque pilote payé reçoit une caisse à lui**, sur l’épave, avec sa part du butin. Le tableau liste ce que tire l’élimination entière, et un pilote qui a infligé 20 % des dégâts tire environ un cinquième de chaque quantité : une part est arrondie au hasard, la moyenne est donc exacte, et une petite part obtient quand même parfois une ligne rare. **Vous seul voyez votre caisse et vous seul pouvez la ramasser**, ni votre clan ni votre groupe, et elle reste **10 minutes**, sans l’attente de 30 secondes ([caisses privées](/wiki/03-Mechanics/Cargo.md#private-boxes)). Dans un [groupe](/wiki/03-Mechanics/Groups.md#sharing-kills), les membres comptent comme un seul pilote pour les 5 %, et sa part se partage comme se partage n’importe quelle élimination dans un groupe (les coéquipiers qui sont proches et qui tirent, selon le niveau) : chaque coéquipier payé d’une part reçoit une caisse privée de cette part. Le Journal de jeu vous donne votre part. Un pilote qui a infligé moins de 5 % n’est pas payé et aucune caisse n’est posée pour lui ; le Journal de jeu le lui dit. Une chance entre parenthèses vaut pour chacun des tirages indiqués : (5 × 50 %) fait cinq tirages à 50 % de chance chacun.

| Gardien | Objet | I | II | III |
| :--- | :--- | :---: | :---: | :---: |
| Brood Warden | Ship Fragment | 30–50 | 80–120 | 150–250 |
| Brood Warden | Advanced Plasma | 6 000–12 000 | 18 000–36 000 | – |
| Brood Warden | Daraxium | 10–20 (5 × 50 %) | – | – |
| Brood Warden | Nyxite | – | 20–40 (5 × 50 %) | – |
| Brood Warden | Ultra Core | – | – | 18 000–30 000 |
| Brood Warden | Quorvium | – | – | 50–100 (60 %) |
| Siege Warden | Ship Fragment | 20–40 | 60–100 | 120–200 |
| Siege Warden | Siphon Battery | 6 000–12 000 | 18 000–30 000 | 48 000–72 000 |
| Siege Warden | Roquette de la boutique à crédits (un type, au hasard) | 20–30 | 50–80 | 80–120 |
| Siege Warden | Reinforced Hull Plate | – | 10 (30 %) | – |
| Siege Warden | Roquette épique (un type, au hasard) | – | – | 10–20 (50 %) |
| Wrath Warden | Ship Fragment | 40–60 | 80–120 | – |
| Wrath Warden | Cataclysite | 30–50 | 50–100 | – |
| Wrath Warden | Reinforced Hull Plate | 10 (25 %) | 10 (50 %) | 10–20 (70 %) |
| Wrath Warden | Power Core | – | 10 (15 %) | 10 (35 %) |
| Wrath Warden | Quorvium | – | – | 50–100 (70 %) |
| Wrath Warden | Ancient Control Unit | – | – | 10 (8 %) |

Depuis la 0.4.16, les lignes de munitions laser (Advanced Plasma, Ultra Core et Siphon Battery) valent trois fois ce qu’elles valaient ; les autres lignes sont inchangées.

Un Gardien est compté sous son propre nom dans vos statistiques de destructions et ajoute des points PvE à votre [grade](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points) : **13 à 35** pour le meneur, selon le Gardien et sa force (un Gardien III vaut le plus), et **1 à 6** pour chaque auxiliaire, plus pour un équipage plus fort.

---

## Points et bonus de clan {#clan-points-and-boosts}

Les points de clan appartiennent au clan. Chaque étape que le clan termine ajoute à son solde. Le **chef et les chefs adjoints** le dépensent sur la carte **Bonus de flotte** de l’onglet Opérations : trois bonus de dix niveaux chacun, et chaque membre les a aussitôt. Un achat est définitif : pas de remboursement, pas de réattribution.

### Les trois bonus {#the-three-boosts}

| Bonus | Niveaux | Par niveau | Niveau maximal | Agit sur |
| :--- | :---: | :---: | :---: | :--- |
| **Dégâts de flotte** | 10 | +0,5 % | +5 % | Dégâts laser aux aliens et aux pilotes |
| **Thulium de flotte** | 10 | +1 % | +10 % | Thulium des destructions et des récompenses de mission |
| **Crédits de flotte** | 10 | +1 % | +10 % | Crédits des destructions et des récompenses de mission |

**Où les voir.** En vol, la fenêtre **Boosters** liste les bonus que votre vaisseau a sur une carte à part, **Bonus de flotte**, sous les boosters à durée : le tag de votre clan, puis une ligne par bonus avec sa valeur et son niveau (Niv. 3/10). Ils n’ont pas de minuteur, car un bonus de clan dure tant que vous êtes dans le clan. Survolez une ligne pour voir sur quoi il agit. Un clan qui n’a encore rien acheté affiche « Votre flotte n’a pas encore de bonus », et un pilote sans clan ne voit pas de carte. La carte Boosters du **tableau de bord** et le profil d’un pilote les listent aussi. La carte montre ce que votre vaisseau applique, tel que le serveur le dit au jeu, si bien qu’un niveau que les officiers viennent d’acheter apparaît tout de suite. Un jeu antérieur à la 0.4.12 applique les bonus et n’affiche pas de carte.

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
- **Ils s’ajoutent à vos autres bonus** (boosters comme le Laser Damage Booster, les bonus de la [boutique des bonus permanents](/wiki/03-Mechanics/Wipe-Timeline.md#the-permanent-buff-store)) : les pourcentages s’additionnent. Les amplificateurs laser (Amps) n’en font pas partie : ils ajoutent des dégâts fixes, et les pourcentages s’appliquent au total. Cinq points de Dégâts de flotte à côté de 50 d’autres sources font 55, soit 3,3 % de dégâts en plus qu’avant.
- **Une fraction n’est pas perdue.** Un bonus ajoute souvent moins d’une unité à une destruction : 10 % des 4 Thulium d’un Seeker font 0,4. Le jeu garde la fraction et la verse avec les unités de vos destructions suivantes, si bien que dix Seekers paient les 4 qui vous sont dus. La fraction que vous détenez est perdue quand vous vous déconnectez.
- **Arrivées et départs.** Un pilote a les bonus dès l’instant où il rejoint le clan et les perd à l’instant où il le quitte, est renvoyé ou que le clan est dissous. Le clan garde ses niveaux.

### Combien de temps cela prend {#how-long-it-takes}

Un clan qui termine chaque ligne gagne 100 points par jour. Si les officiers achètent à parts égales dans les trois bonus, il a **4 niveaux après la première ligne, 10 après la troisième, 16 après la cinquième et les 30 au jour de saison 12**. Quatorze lignes sont passées quand le jour 15 commence, un tel clan a donc deux lignes d’avance. Un jour non terminé paie tout de même les étapes faites : un clan qui vient à bout des quatre missions mais ne tue jamais son Gardien gagne 70 points par jour et a les 30 niveaux au plus tôt au jour de saison 18. Après le dernier niveau, la ligne continue et continue de payer votre récompense ; les points continuent de s’ajouter à ce que le clan a gagné cette saison, ce que l’info-bulle des points de clan sur la carte Bonus de flotte indique.

### Points et réinitialisation {#clan-points-and-the-wipe}

La réinitialisation dissout tous les clans ([La réinitialisation dissout tous les clans](#the-wipe-disbands-every-clan)) : les **points, les niveaux de bonus et les lignes d’un clan prennent donc fin avec lui**, et un clan fondé après la réinitialisation repart de zéro : chaque saison est une nouvelle course aux bonus maximaux.

---

## Diplomatie {#diplomacy}

Le chef et les chefs adjoints peuvent établir des relations diplomatiques formelles avec un autre clan de leur **monde** en saisissant son tag ([Clans et mondes](#clans-and-worlds)) :

- **Alliance** : clans formellement alliés. Le statut amical s’affiche sur la carte.
- **Pacte de non-agression (NAP)** : accord pour ne pas engager d’hostilités.
- **Guerre** : déclaration de guerre formelle. Les cibles de guerre peuvent être attaquées n’importe où sans pénalité.

### Changer et mettre fin à un traité {#changing-and-ending-a-treaty}

Une alliance, un pacte et une guerre commencent tous aussitôt, sans le consentement de l’autre clan. Leur fin diffère :

| Maintenant | Vous pouvez | Ce qui se passe |
| :--- | :--- | :--- |
| **Alliance** | Passer à un pacte, rompre, déclarer la guerre | Un pacte la remplace aussitôt ; une rupture y met fin aussitôt pour les deux clans ; une guerre la remplace. |
| **Pacte** | Passer à une alliance, rompre, déclarer la guerre | Une alliance le remplace aussitôt ; une rupture y met fin aussitôt pour les deux clans ; une guerre le remplace. |
| **Guerre** | Demander la paix | Elle ne prend fin **que si l’autre clan est d’accord**. Une alliance ou un pacte ne peut pas la remplacer, et personne ne peut la rompre seul. |

- **Rompre et changer** se font d’une seule pression par un chef ou un chef adjoint de l’un des deux clans, avec une confirmation pour une rupture. Il n’y a pas de préavis.
- **Demander la paix.** Un chef ou un chef adjoint d’un clan en guerre appuie sur **Demander la paix**. La demande dure **24 heures**. Le chef ou un chef adjoint de l’autre clan l’**accepte** (la guerre est finie pour les deux) ou la **refuse** (la guerre continue, et vous pouvez redemander **1 heure** après le refus). Vous pouvez **retirer la demande** à tout moment. Si les deux clans la demandent, la paix est faite aussitôt.
- **Les demandes de fin de guerre** sont listées dans une carte de l’onglet Diplomatie, avec Accepter et Refuser pour les officiers.
- **Tout le monde est prévenu.** Chaque changement entre dans le [Journal de la flotte](#fleet-log) des deux clans, et le chef et les chefs adjoints en ligne de l’autre clan reçoivent une ligne Système, une notification et un son. Un pilote extérieur aux deux clans n’est prévenu de rien.
- **Anciens traités.** Une alliance, un pacte ou une guerre conclus entre clans de mondes différents avant la 0.4.16 peuvent encore être rompus ou terminés d’un commun accord, et il n’est plus possible d’en conclure de nouveaux.

---

## Journal de la flotte {#fleet-log}

L’onglet **Journal**, le dernier de la fenêtre du clan, est l’histoire propre du clan. **Seuls les pilotes du clan peuvent le lire.** Il garde les **200 dernières lignes** jusqu’à la réinitialisation, en montre 50 par page, la plus récente d’abord, et il est relu toutes les 10 secondes tant qu’il est ouvert. Il raconte :

- **Les quêtes du clan.** Chaque étape terminée de la ligne du jour, avec les pilotes dont le travail a compté pour cette étape, même quand c’était un seul pilote : La quête de flotte « Seeker Sweep » est terminée. Pilotes y ayant pris part : « Nova », « Vega ». Le Gardien est l’étape 5 et est noté avec son genre et sa force ; la ligne terminée a une ligne à elle. Un pilote dont le travail a été retiré, ou dont la part du Gardien est inférieure à 5 %, n’est pas nommé.
- **Le Trésor de la flotte.** Les dons, la taxe quotidienne (une ligne par jour), les versements, les améliorations, chaque prime quotidienne versée, un jour où il n’a pas pu payer (une ligne par jour pour tout le clan) et chaque fois que le chef change les montants.
- **L’effectif.** La fondation du clan, les pilotes qui arrivent (clan ouvert, candidature ou invitation acceptée), partent ou sont renvoyés, les changements de grade et un nouveau chef.
- **Diplomatie.** Chaque alliance, pacte, guerre, rupture et demande de fin de guerre, formulé du côté de votre clan (« Notre flotte a conclu une alliance avec [TAG] Name. »).

---

## Amener un ami {#bringing-a-friend}

Un ami qui découvre le jeu peut le rejoindre avec votre code d’invitation personnel et reçoit un pack de départ ; voir [Inviter des amis](/wiki/03-Mechanics/Invite-Friends.md). Une fois dans le jeu, il peut postuler à votre clan comme n’importe quel pilote du même monde.