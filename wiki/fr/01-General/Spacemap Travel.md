<!-- wiki-i18n source: 1b81da9c3cf72282 -->
<!-- wiki-i18n title: Navigation spatiale -->
# Navigation sur la carte spatiale {#spacemap-travel}

La carte spatiale est votre interface de navigation pour parcourir l’univers de SpaceCorps. Chaque corporation contrôle un secteur de l’espace, organisé selon une topologie précise qui permet à la fois une exploration sûre et des affrontements PvP dangereux.

![Galaxy Gates](../../img/wiki-img/shots/gates.jpg)
![Sector DS-1 as the game draws it](../../img/wiki-img/shots/sector-DS-1.jpg)
![Sector DS-2 as the game draws it](../../img/wiki-img/shots/sector-DS-2.jpg)
![Sector DS-3 as the game draws it](../../img/wiki-img/shots/sector-DS-3.jpg)
![Sector DS-4 as the game draws it](../../img/wiki-img/shots/sector-DS-4.jpg)
![Sector G-1 as the game draws it](../../img/wiki-img/shots/sector-G-1.jpg)
![Sector G-2 as the game draws it](../../img/wiki-img/shots/sector-G-2.jpg)
![Sector G-3 as the game draws it](../../img/wiki-img/shots/sector-G-3.jpg)
![Sector G-4 as the game draws it](../../img/wiki-img/shots/sector-G-4.jpg)
![Sector M-1 as the game draws it](../../img/wiki-img/shots/sector-M-1.jpg)
![Sector M-2 as the game draws it](../../img/wiki-img/shots/sector-M-2.jpg)
![Sector M-3 as the game draws it](../../img/wiki-img/shots/sector-M-3.jpg)
![Sector M-4 as the game draws it](../../img/wiki-img/shots/sector-M-4.jpg)
![Sector T-1 as the game draws it](../../img/wiki-img/shots/sector-T-1.jpg)
![Sector T-2 as the game draws it](../../img/wiki-img/shots/sector-T-2.jpg)
![Sector T-3 as the game draws it](../../img/wiki-img/shots/sector-T-3.jpg)
![Sector T-4 as the game draws it](../../img/wiki-img/shots/sector-T-4.jpg)
![The Star System map: the sectors, the PvP sectors, the gates and the company routes, with the portal ring that joins each company's x-4 sector to the next company's x-3 sector](../../img/wiki-img/shots/star-system.jpg)

## La structure de l’univers {#the-universe-structure}

L’univers comprend trois grands secteurs de corporation (Mars, Terra, Galactic) et une zone PvP centrale.

- **x-1 (base d’origine)** : la carte de départ de chaque corporation (M-1, T-1, G-1). La zone la plus sûre.
- **x-2 -> x-3** : des zones d’expansion aux aliens de plus en plus coriaces.
- **x-4 (frontière)** : la porte d’entrée du secteur PvP et du `x-3` d’une autre corporation (l’Anneau, plus bas).
- **DS-x (secteurs dangereux)** : la zone PvP centrale qui relie toutes les corporations : DS-1 à DS-4. Dès le jour 11 de la saison, il contient aussi des pulsars avec des excavatrices géantes et le Dormant Swamp ([Secteurs dangereux](/wiki/01-General/Danger-Sectors.md)).

Seules les bases d’origine ont une station. C’est là que s’ouvre **Mission Control**, et sa zone sûre s’étend sur 1 600 unités autour d’elle. Les secteurs dangereux n’ont pas de station, `DS-1` compris : les seules zones sûres y sont les anneaux de 660 unités autour des portes de saut, et Mission Control ne peut pas s’y ouvrir ; regagnez votre base en vol pour vos missions.

Chaque [monde](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) (Alpha, Beta, Gamma) possède sa propre copie de toute cette carte, et c’est lui qui décide où les pilotes peuvent s’affronter : dans Alpha seulement en `x-4` et `DS-x`, dans Beta partout sauf en `x-1`, dans Gamma partout. La carte de la galaxie colore les secteurs selon la règle de votre monde.

## Visualisation {#visualization}

La carte de la galaxie ci-dessous montre en temps réel la disposition de l’univers connu. Dans le jeu, cette même carte est la fenêtre **Système stellaire**.

```spacemap

```

Avec un [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) installé, la carte sert aussi à choisir votre destination : appuyez sur l’emplacement du CPU dans la barre rapide (**JMP**) et la fenêtre Système stellaire s’ouvre en mode sélection. Les secteurs où le CPU peut vous emmener sont éclairés ; votre propre secteur et les secteurs dangereux ne le sont pas. Pointez un secteur éclairé pour lire le prix, cliquez dessus et confirmez le saut quand la carte le demande (500 Thulium).

## Comment voyager {#how-to-travel}

Les déplacements sur la carte spatiale passent par les **portes de saut** (les portails). Le [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) est l’autre voie : il n’a pas besoin de porte (voir la fin de cette page).

1. **Trouvez un portail** : les portails se trouvent généralement dans les coins ou sur les bords d’une carte.
2. **Navigation** : approchez votre vaisseau de la structure du portail.
3. **Activation** : appuyez sur **'J'** à moins de 500 unités du portail pour lancer le saut.
4. **Patientez** : le saut **dure 3 secondes**. Pendant ce temps, une barre au-dessus de votre barre rapide (« Saut en cours… ») se remplit, et le portail brille de plus en plus fort à mesure qu’il se charge ; les autres pilotes voient la même charge sur le portail quand vous sautez. Votre vaisseau continue de voler, mais vous devez rester à moins de 500 unités du portail jusqu’à la fin du délai : sortez de la portée et le saut est annulé (« Portail trop éloigné pour sauter. », et la barre devient rouge). Appuyer de nouveau sur **'J'** pendant le saut ne fait rien, sinon vous le signaler.
5. **Destination** : vous arrivez au portail correspondant de la carte de destination.

### Sauter sous le feu {#jumping-under-fire}

- **Hors des secteurs dangereux**, être attaqué, par des aliens ou par d’autres pilotes, n’interrompt **pas** votre saut : il va jusqu’au bout.
- **Dans les secteurs dangereux (`DS-1` à `DS-4`)**, vous ne pouvez pas sauter pour en sortir tant que vous êtes attaqué. Si un pilote ou un alien a touché votre vaisseau (ses boucliers ou sa coque) au cours des **10 dernières secondes**, le saut ne démarre pas (« Vous êtes attaqué : impossible de sauter hors d’un secteur dangereux. »), et un coup reçu pendant le saut l’annule (la barre devient rouge et le jeu vous en donne la raison). Les dégâts de la radiation du trou noir ne comptent pas comme une attaque, pas plus qu’un tir arrêté par une zone sûre. Un coup reçu sur la carte que vous quittez ne vous suit pas à travers le portail : vous arrivez avec un casier vierge.
- Vous ne faites qu’une chose à la fois : impossible de récupérer une [cargaison](/wiki/03-Mechanics/Cargo.md) pendant un saut, et lancer un saut abandonne une récupération en cours.
- Fermer le jeu ou retourner à la base au milieu d’un saut l’annule : vous n’arrivez pas à destination.
- **La téléportation d’un CPU se charge comme un saut par portail.** Un Jump CPU se charge pendant 5 secondes et un Base CPU pendant 10, avec une barre au-dessus de la barre rapide. Un tir de votre part ou un coup reçu, dans n’importe quel secteur, l’annule (rien n’est payé ni consommé), et aucun des deux CPU ne démarre dans les 10 secondes qui suivent un tir ou un coup. Appuyez de nouveau sur l’emplacement du CPU pour l’annuler vous-même.

### Liaisons de saut {#jump-links}

- **La boucle de corporation** : Mars, Terra et Galactic ont la même disposition. Les liaisons suivent le schéma `1 <-> 2 <-> 3`, `2 <-> 4` et `3 <-> 4`. Cela forme une boucle entre les cartes secondaires (`x-2` et `x-3`) et la carte frontalière (`x-4`), `x-1` servant de point d’entrée sûr en bout de chaîne, relié uniquement à `x-2` : votre carte de départ n’a qu’un seul portail.
- **Portes d’accès aux secteurs dangereux** : la carte frontalière de chaque corporation (`x-4`) est reliée directement à son propre secteur dangereux :
  - `M-4` est relié à `DS-1`
  - `T-4` est relié à `DS-2`
  - `G-4` est relié à `DS-3`
- **L’Anneau** : la carte frontalière de chaque corporation (`x-4`) a une porte de plus, vers le `x-3` de la **corporation suivante**, et chaque `x-3` a la porte de retour. Les trois liaisons forment un anneau autour des secteurs dangereux, si bien que chaque corporation a une voie vers l’extérieur et une voie vers l’intérieur :
  - `M-4` est relié au `T-3` de Terra
  - `T-4` est relié au `G-3` de Galactic
  - `G-4` est relié au `M-3` de Mars

  L’Anneau est ouvert à tous les pilotes, quelle que soit la corporation pour laquelle ils volent : c’est une seconde manière de voyager entre les cartes des corporations, qui ne traverse pas la zone PvP. Une porte de l’Anneau se tient dans un coin à part, loin des autres portes de sa carte, avec la zone sûre habituelle de 660 unités autour d’elle, et le saut fonctionne comme à n’importe quelle porte. L’endroit où l’on peut vous attaquer de l’autre côté dépend de votre monde, comme partout : dans Alpha, `T-3` n’est pas un secteur PvP mais `T-4` l’est, dans Beta les deux le sont, dans Gamma tous les secteurs le sont.
- **Routes d’invasion (voyages entre corporations)** : il y a deux façons d’entrer par les portes sur le territoire d’une autre corporation. La courte est l’Anneau : un pilote de Mars vole de `M-4` jusqu’au `T-3` de Terra par la porte de l’Anneau (trois sauts depuis la base de Mars, `M-1` → `M-2` → `M-4` → `T-3`), puis poursuit vers `T-4` ou `T-2` ; le `G-4` de Galactic mène de la même façon au `M-3` de Mars, et le `T-4` de Terra au `G-3` de Galactic. La longue traverse la zone PvP : de `M-4` jusqu’au secteur dangereux `DS-1`, par la porte de saut vers `DS-2`, puis dans l’espace de Terra par `T-4` ; pour atteindre Galactic, on franchit la porte de saut vers `DS-3` et l’on entre par `G-4`.
- **Le triangle des secteurs dangereux** : `DS-1`, `DS-2` et `DS-3` sont tous reliés entre eux. Chacun abrite la porte d’une corporation (Mars dans `DS-1`, Terra dans `DS-2`, Galactic dans `DS-3`) ; `DS-4` n’en a aucune.
- **Le cœur central** : les trois secteurs dangereux extérieurs (`DS-1`, `DS-2` et `DS-3`) sont reliés directement à la carte centrale **`DS-4`**, la zone PvP la plus dangereuse et la plus lucrative de l’univers. Un **trou noir** se trouve exactement en son milieu : les portails et les couloirs qui les relient en restent bien éloignés, mais un vaisseau qui s’y aventure subit sa radiation, puis son attraction, et est détruit à son horizon des événements. Voir [Le trou noir](/wiki/03-Mechanics/Black-Hole.md). Dès le jour 11 de la saison, le coin supérieur gauche de `DS-4` contient le [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md), dont les canons tirent sur tout vaisseau qu’ils voient.

### Le Jump CPU {#the-jump-cpu}

Le [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) emmène votre vaisseau dans n’importe quel secteur de corporation de votre monde sans passer par une porte, pour 500 Thulium le saut, secteurs d’origine ennemis compris. Il ne mène jamais à un secteur dangereux, ne démarre pas en combat, et vous le recherchez d’abord dans le Centre de recherche du Skylab ([Recherche](/wiki/03-Mechanics/Research.md)). Les [Base CPU](/wiki/06-Items/Extras.md#base-cpus) vous ramènent chez vous de la même façon. Un CPU warp, c’est-à-dire le Jump CPU ou un Base CPU, est refusé tant que vous transportez un objet de mission (« Vous ne pouvez pas utiliser de CPU warp en transportant un objet de mission. ») : rentrez par les portails ([Objets de mission](/wiki/03-Mechanics/Quests.md#quest-items)).
