<!-- wiki-i18n source: 21f10d185095b346 -->
<!-- wiki-i18n title: Clans -->
# Clans {#clans}

Fonder un clan ou en rejoindre un vous permet de mettre vos ressources en commun, de faire monter en niveau la banque partagée, de fixer les taux de taxe, de vous coordonner avec les membres de votre faction et de gérer la diplomatie.

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
| **Promouvoir / Renvoyer** | ✅ | ✅* | ❌ | ❌ |
| **Accepter les candidatures** | ✅ | ✅ | ✅ | ❌ |

*\*Les chefs adjoints ne peuvent promouvoir, rétrograder ou renvoyer que des membres d’un grade inférieur au leur.*

### Quand le chef part {#when-the-leader-leaves}

Un chef ne peut pas quitter un clan qui compte encore d’autres membres : il doit d’abord promouvoir un chef adjoint au rang de chef (le chef redevient alors chef adjoint), ou partir en dernier, ce qui dissout le clan. Si le chef supprime son compte (Paramètres › Compte), la direction passe au membre le plus haut gradé, et à égalité à celui qui a le plus d’ancienneté ; un chef seul dans le clan le dissout, banque comprise.

---

## Diplomatie {#diplomacy}

Les clans peuvent établir des relations diplomatiques formelles avec d’autres organisations en saisissant le tag du clan visé :

- **Alliance** : clans formellement alliés. Le statut amical s’affiche sur la carte.
- **Pacte de non-agression (NAP)** : accord pour ne pas engager d’hostilités.
- **Guerre** : déclaration de guerre formelle. Les cibles de guerre peuvent être attaquées n’importe où sans pénalité.

---

## Amener un ami {#bringing-a-friend}

Un ami qui découvre le jeu peut le rejoindre avec votre code d’invitation personnel et reçoit un pack de départ ; voir [Inviter des amis](/wiki/03-Mechanics/Invite-Friends.md). Une fois dans le jeu, il peut postuler à votre clan comme n’importe quel pilote.
