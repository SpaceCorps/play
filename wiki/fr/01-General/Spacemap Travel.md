<!-- wiki-i18n source: 48e9736362e10347 -->
<!-- wiki-i18n title: Navigation spatiale -->
# Navigation sur la carte spatiale {#spacemap-travel}

La carte spatiale est votre interface de navigation pour parcourir l’univers de SpaceCorps. Chaque corporation contrôle un secteur de l’espace, organisé selon une topologie précise qui permet à la fois une exploration sûre et des affrontements PvP dangereux.

## La structure de l’univers {#the-universe-structure}

L’univers comprend trois grands secteurs de corporation (Mars, Terra, Galactic) et une zone PvP centrale.

- **x-1 (base d’origine)** : la carte de départ de chaque corporation (M-1, T-1, G-1). La zone la plus sûre.
- **x-2 -> x-3** : des zones d’expansion aux aliens de plus en plus coriaces.
- **x-4 (frontière)** : la porte d’entrée du secteur PvP.
- **DS-x (secteurs dangereux)** : la zone PvP centrale qui relie toutes les corporations : DS-1 à DS-4.

Chaque [monde](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) (Alpha, Beta, Gamma) possède sa propre copie de toute cette carte, et c’est lui qui décide où les pilotes peuvent s’affronter : dans Alpha seulement en `x-4` et `DS-x`, dans Beta partout sauf en `x-1`, dans Gamma partout. La carte de la galaxie colore les secteurs selon la règle de votre monde.

## Visualisation {#visualization}

La carte de la galaxie ci-dessous montre en temps réel la disposition de l’univers connu.

```spacemap

```

## Comment voyager {#how-to-travel}

Les déplacements sur la carte spatiale passent par les **portes de saut** (les portails).

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

### Liaisons de saut {#jump-links}

- **La boucle de corporation** : Mars, Terra et Galactic ont la même disposition. Les liaisons suivent le schéma `1 <-> 2 <-> 3`, `2 <-> 4` et `3 <-> 4`. Cela forme une boucle entre les cartes secondaires (`x-2` et `x-3`) et la carte frontalière (`x-4`), `x-1` servant de point d’entrée sûr en bout de chaîne, relié uniquement à `x-2` : votre carte de départ n’a qu’un seul portail.
- **Portes d’accès aux secteurs dangereux** : la carte frontalière de chaque corporation (`x-4`) est reliée directement à son propre secteur dangereux :
  - `M-4` est relié à `DS-1`
  - `T-4` est relié à `DS-2`
  - `G-4` est relié à `DS-3`
- **Routes d’invasion (voyages entre corporations)** : pour entrer sur le territoire d’une corporation ennemie, vous devez traverser la zone PvP. Par exemple, un pilote de Mars qui veut envahir Terra doit voler de `M-4` jusqu’au secteur dangereux `DS-1`, franchir la porte de saut vers `DS-2`, puis entrer dans l’espace de Terra par `T-4` ; pour atteindre Galactic, il franchit la porte de saut vers `DS-3` et entre par `G-4`.
- **Le triangle des secteurs dangereux** : `DS-1`, `DS-2` et `DS-3` sont tous reliés entre eux. Chacun abrite la porte d’une corporation (Mars dans `DS-1`, Terra dans `DS-2`, Galactic dans `DS-3`) ; `DS-4` n’en a aucune.
- **Le cœur central** : les trois secteurs dangereux extérieurs (`DS-1`, `DS-2` et `DS-3`) sont reliés directement à la carte centrale **`DS-4`**, la zone PvP la plus dangereuse et la plus lucrative de l’univers. Un **trou noir** se trouve exactement en son milieu : les portails et les couloirs qui les relient en restent bien éloignés, mais un vaisseau qui s’y aventure subit sa radiation, puis son attraction, et est détruit à son horizon des événements. Voir [Le trou noir](/wiki/03-Mechanics/Black-Hole.md).
