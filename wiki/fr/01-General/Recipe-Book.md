<!-- wiki-i18n source: b15e3e40418c232b -->
<!-- wiki-i18n title: Livre de recettes -->
# Livre de recettes et builds {#recipe-book-and-builds}

<!-- wiki-search: recipe; recipes; recipe book; bill; steps; chart; craft tree; what do i need; build; builds; loadout; preset; presets; import; export; json; my builds; share a build; recette; recettes; coût; étapes; schéma; fabriquer; équipement; préréglage; importer; exporter; mes builds; partager un build -->

Le **Livre de recettes** répond à « qu’est-ce que ça demande ? » pour n’importe quel objet du jeu : un schéma de ce dont il est fait, les étapes dans l’ordre, le coût complet et l’origine de chaque matière première. **Builds** fait la même chose pour un vaisseau entier : importez l’équipement de votre hangar ou le build d’un ami, partez de l’un des 15 préréglages ou créez le vôtre, et voyez ses statistiques et son coût complet, étape par étape. Les deux se trouvent dans la **Bibliothèque** de la station, sous le Wiki.

Le Livre de recettes ne tient aucune liste de prix à lui : il calcule ses chiffres au moment où vous regardez, à partir des recettes, des prix, des technologies et des tables de butin que la Boutique, l’[Assemblage](/wiki/06-Items/Overview.md#upgrading-modules) et la [Recherche](/wiki/03-Mechanics/Research.md) utilisent, et il suit donc le jeu quand un prix ou une recette change. C’est pourquoi cette page ne cite ni prix ni statistique : ouvrez l’objet ou le build.

## L’ouvrir {#open-it}

Ouvrez le menu de la station et choisissez **Bibliothèque › Livre de recettes** ou **Bibliothèque › Builds**. Le Livre de recettes se souvient du dernier objet que vous avez regardé, de ses filtres et de son zoom, sur cet ordinateur seulement ; vos builds n’en font pas partie ([Enregistrés sur votre compte](#saved-on-your-account)). Quand le jeu est plus récent que le serveur auquel il parle, la page le dit et en montre moins : le Livre de recettes calcule toujours tout ce qui s’achète, se fabrique ou s’améliore, mais ne peut pas dire où le monde donne un objet (il écrit seulement « Obtenir »), et Builds nomme les parties qui demandent le serveur plus récent : les préréglages, Mes builds et les statistiques.

## Trouver un objet {#find-an-item}

La grande liste de gauche contient tous les objets du jeu, groupés par type et, dans un type, dans l’ordre propre au jeu : le rang le plus faible d’abord. L’EMP Charge, le seul consommable, y figure aussi.

- **Recherche.** Commencez à taper n’importe où sur la page et le texte va dans le champ de recherche. La liste devient une seule liste, classée selon la qualité de la correspondance avec le nom (le nom entier, son début, le début d’un mot, une partie quelconque, puis le type). Les majuscules et les accents ne comptent pas, et l’ancien nom d’un objet renommé retrouve l’objet. `Esc` efface la recherche.
- **Type.** Le menu déroulant au-dessus de la liste la limite à un type et indique combien d’objets chaque type compte. Le bouton à côté trie de A à Z dans chaque type.
- **Lignes.** Une ligne montre l’image, le nom, le type et la rareté de l’objet, un petit symbole pour la voie par laquelle vous l’obtiendriez d’ordinaire (fabriqué à l’Assemblage, vendu à la Boutique, butin ou trouvaille, pressé, ou produit dans le trou noir) et une coche si vous l’avez.
- **Touches.** Les flèches, Page précédente, Page suivante, Début et Fin parcourent la liste, et `Enter` passe au schéma. `Alt+Left` et `Alt+Right` reculent et avancent dans les objets que vous avez ouverts.

## Le schéma {#the-chart}

Cliquez sur un objet et le côté droit l’affiche. En haut figurent son image, son nom, sa rareté et son type, et une pastille pour chaque **voie** qui permet de l’obtenir : **Fabriquer** (à l’Assemblage, avec son temps et son coût), **Acheter** (à la Boutique, avec son prix), **Presser** (à partir de minerai, dans la Fonderie du Skylab), **Butin** (le monde le donne : aliens, rochers, récompenses) et **Produire** ([Dark Matter](/wiki/03-Mechanics/Dark-Matter.md), à partir de N.I.K.E. tirés dans le trou noir). La pastille pleine est la voie que suivent le schéma et le coût ; cliquez sur une autre pastille pour suivre celle-là à la place. Si vous n’avez pas recherché ce qui permet de fabriquer l’objet, une ligne dit quelle technologie il faut et combien de temps elle prend, avec un bouton qui ouvre la Recherche.

Le **Schéma** dessine l’objet comme un arbre de gauche à droite : l’objet à gauche, ce dont il est fait à sa droite, jusqu’aux matières premières.

- Chaque case montre l’objet, combien vous en avez besoin et un symbole pour la façon de l’obtenir (celui de la pastille de cette voie, plus haut ; survolez la case pour lire les mots, la couleur n’est donc jamais le seul signe). Un cadenas dit que sa technologie n’est pas encore recherchée, et une coche verte suivie d’un nombre, combien vous en avez.
- Une case qui a des branches possède une petite poignée qui les replie ; les branches profondes d’un grand arbre démarrent repliées. **Tout déplier**, **Tout replier**, **Ajuster** et les boutons de zoom se trouvent au-dessus du schéma.
- Cliquez sur une case pour lire sa fiche sous le schéma : l’objet, les voies pour l’obtenir (cliquez sur une autre pastille pour suivre cette voie), ce que demande la voie (les fournées, le temps et le coût d’une fabrication, ou son prix à la Boutique), combien vous en avez et, pour une case verrouillée, la technologie qu’il faut. Un double-clic, ou `Enter`, ouvre cet objet dans le Livre de recettes. Les flèches passent d’une case à l’autre, `Space` replie ou déplie une branche et `0` ajuste le schéma. Faites défiler pour vous déplacer ; `Ctrl` et la molette zooment.
- Un objet qui ne fait que s’acheter ou se trouver est une seule case qui dit « Rien à fabriquer : cela s’achète ou se trouve. Voir Sources. »

Dans une fenêtre large, le schéma prend la gauche et les autres panneaux forment une colonne à sa droite ; dans une fenêtre étroite, les onglets **Schéma**, **Étapes**, **Coût**, **Sources** et **Utilisé dans** montrent un panneau à la fois.

## Étapes et coût {#steps-and-the-bill}

Sous l’en-tête, trois commandes décident de ce qui est compté : **Quantité** d’exemplaires voulus, **Compter ce que j’ai** (activé : ce que vous avez déjà est déduit) et **Inclure ce qui est équipé** (désactivé : une pièce montée sur un vaisseau n’est pas comptée, car améliorer consomme une pièce et une pièce montée quitterait son emplacement).

- **Étapes** est le schéma en liste numérotée, dans l’ordre où il faut faire les choses, en groupes : Recherche, Obtenir, Acheter, Presser et fabriquer, et Dans votre stock. La recherche vient d’abord parce que l’Assemblage ne fabrique rien avant que sa technologie soit recherchée. Chaque étape dit quoi et combien, ce que cela coûte et combien de temps cela prend, et une étape Obtenir peut montrer où l’obtenir. **Copier les étapes** copie la liste en texte.
- **Coût** fait la somme : vos Credits et votre Thulium face à ce que vous avez, chaque matière première avec ce dont vous avez **Besoin**, ce que vous avez (**Possédé**) et ce qui **Manque**, le Dark Matter que prend la recherche, le temps de fabrication et de pressage, le temps de recherche (une technologie à la fois) et une **Valeur**. La Valeur sert à comparer deux façons d’obtenir un objet, le Thulium et ce qu’il faut trouver étant comptés en Credits : ce n’est pas un prix. **Copier le coût** copie le coût sous forme de tableau que vous pouvez coller dans un chat ou une note.

## Sources et Utilisé dans {#sources-and-used-in}

- **Sources** dit où le monde donne l’objet et chaque matière première dont le plan a besoin, par type : aliens, astéroïdes et rochers, essaims, le Dormant Swamp, gardiens de clan, [Davidski](/wiki/03-Mechanics/Davidski.md), expéditions du Skylab, l’excavatrice géante, production du Skylab, quêtes, Inviter des amis et le pack de départ. Une ligne nomme qui le donne et où, la chance et combien. « Aussi chez » énumère les [Enchères](/wiki/03-Mechanics/Auction.md), le stock de Davidski et d’autres pilotes. Une chance est une chance, pas un rythme par heure : la durée d’une destruction ne dépend que de vous.
- **Utilisé dans** énumère les objets qui se fabriquent avec celui-ci. Cliquez sur l’un d’eux pour l’ouvrir.

## Ajouter au build {#add-to-build}

Un objet qui se place dans un emplacement ou qui s’emporte a un bouton **Ajouter au build** : vaisseaux, blindages de coque, lasers, amplificateurs, boucliers, cellules, moteurs, propulseurs, Adaptive Cores, extras, drones, formations, munitions, roquettes et l’EMP Charge. Il met l’objet dans le build que vous modifiez dans **Builds**, au premier endroit où il tient (un nouveau build appelé « Nouveau build » est créé s’il n’y en a aucun), et un message dit où il est allé ou pourquoi il n’a pas tenu (« Choisissez d’abord un vaisseau. »). Ajouter un vaisseau à un build qui en a déjà un demande de cliquer une seconde fois pour le remplacer. L’EMP Charge s’emporte, elle ne se monte pas : elle va dans les roquettes du build.

## Builds

Un **build** est l’équipement d’un vaisseau, écrit en noms d’objets pour qu’il signifie la même chose sur tous les serveurs : le vaisseau, les lasers avec leurs amplificateurs, les boucliers, moteurs et Adaptive Cores avec leurs cellules et propulseurs, les extras, les pièces des emplacements de capacité, les blindages de coque, les drones avec ce qu’ils transportent, une formation, et les munitions et roquettes à emporter. Il a aussi un nom, une note, une phase (Début, Milieu ou Fin) et un type.

La liste de gauche contient les **Préréglages** par phase, **Mes builds**, **Nouveau build** et **Importer** ; dans une fenêtre étroite, c’est une rangée d’onglets. Choisissez un build et vous voyez son plateau, ses statistiques et son coût.

### Importer {#import}

**Importer** ouvre une fenêtre avec trois portes :

- **Coller** : collez le texte d’un build, ou appuyez sur **Coller depuis le presse-papiers**.
- **Depuis un fichier** : les fichiers de build du dossier `exports` du dossier de données du jeu (`.spacecorps2027` dans votre dossier personnel), le dossier dans lequel écrit **Enregistrer dans un fichier**.
- **Depuis mon hangar** : choisissez l’un de vos vaisseaux et une configuration, et le jeu lit ce qui est équipé : lasers et amplificateurs, générateurs avec leurs cellules et propulseurs, extras, pièces de capacité, blindages de coque, drones avec ce qu’ils transportent et le niveau de votre Extra Slots CPU. Il propose aussi la formation, les munitions et les roquettes de votre barre rapide ; cochez ce que vous voulez.

Vous voyez ce qui arrive avant que quoi que ce soit soit enregistré, et le jeu vous dit exactement ce qu’il n’a pas pu importer : un objet qui n’existe pas dans ce jeu, une pièce qui ne va pas à sa place, plus de pièces que le vaisseau n’a d’emplacements, un build fait par un jeu plus récent. **Importé sans changement** veut dire que tout est entré. Ensuite, **Enregistrer dans Mes builds**, **Ouvrir dans l’éditeur**, ou fermez la fenêtre. Vos rangs de [Forge](/wiki/06-Items/Forge.md), les bonus de la Forge, les niveaux des drones, les boosters, le P.E.T., l’apparence de votre vaisseau et l’autre configuration du [Hangar](/wiki/03-Mechanics/Hangar.md) ne font pas partie d’un build (importez l’autre configuration comme un second build).

### Les 15 préréglages {#the-15-presets}

Quinze builds sont prêts à l’emploi : trois phases du jeu, **Début**, **Milieu** et **Fin**, avec cinq types dans chacune. **Farm** obtient le plus de destructions pour ce qu’il coûte, **Défense** a le plus grand bouclier et la régénération la plus rapide, **Attaque** les plus gros dégâts et la plus forte pénétration, **Situationnel** choisit ses combats grâce à l’occultation, aux sauts et à la vitesse, et **Tank** a la coque et le bouclier les plus élevés ensemble. Un préréglage ne se modifie pas : **Modifier une copie** l’ouvre comme votre propre brouillon, et **Ajouter à Mes builds** le garde tel quel. Chaque ligne montre sa Valeur en quelques caractères, calculée à partir des recettes pendant que vous regardez ; ouvrez un préréglage pour ses statistiques et son coût.

### Modifier {#edit}

Un build est dessiné comme un hangar : lasers, générateurs, extras, capacités, blindages et drones, puis le niveau de l’Extra Slots CPU, une formation et les munitions et roquettes à emporter. Cliquez sur un emplacement vide et une liste montre seulement ce qui y va, avec son prix ou la voie pour l’obtenir ; cliquez sur une pièce pour la **Remplacer**, **Ajouter un module** ou la **Retirer**. Un drone transporte un laser ou un cœur de bouclier. Si vous changez de vaisseau, les pièces qui vont encore restent, et le reste est énuméré comme retiré. Donnez au build un nom, une phase, un type et une note, puis **Enregistrer**, **Enregistrer une copie**, **Supprimer** ou **Fermer** (Fermer demande d’abord confirmation s’il y a des changements non enregistrés).

### Statistiques {#stats}

Sous le plateau se trouve la fiche de statistiques du hangar : points de vie, dégâts, portée, taux critique, boucliers et leur recharge, absorption, vitesse, bonus de bouclier et de vitesse, pénétration et, sur un vaisseau qui a des emplacements de blindage, la coque que ses blindages ajoutent. La fiche n’a aucune ligne pour les capacités : les pièces des emplacements de capacité sont sur le plateau. Le serveur calcule les chiffres avec le même code que votre hangar, pour un build qui n’est monté sur aucun vaisseau. Deux commutateurs règlent le **Rang de Forge** et le **Niveau des drones** que supposent les chiffres. Une formation agit en vol : elle est donc énumérée en texte et non comptée dans les chiffres, pas plus que les boosters ou vos propres rangs de Forge.

### Coût {#cost}

Le coût comporte quatre blocs :

- **Totaux** : Credits, Thulium, Dark Matter, chaque matière première avec Besoin, Possédé et Manque, les durées et la Valeur. **Il vous faut encore** est ce qui reste une fois ce que vous possédez déduit.
- **Où va l’argent** : chaque pièce, la plus chère d’abord.
- **Étapes** : rechercher, obtenir, acheter, presser et fabriquer, dans l’ordre, pour le build entier. Cliquez sur une étape Obtenir pour voir où le monde le donne, ou ouvrez l’objet dans le Livre de recettes.
- **Avant de commencer** : ce qui n’est pas une pièce, comme les niveaux de l’Extra Slots CPU, la recherche des emplacements de blindage, les drones que vous devez encore acheter et le niveau du Cœur du Skylab qu’exige la Fonderie.

Trois commutateurs : **Déduire ce que j’ai** (activé), **Inclure ce qui est monté** (désactivé) et **Inclure munitions et roquettes** (désactivé : elles se consomment sans cesse, elles ne font donc pas le prix du build).

## Enregistrés sur votre compte {#saved-on-your-account}

**Mes builds sont enregistrés sur votre compte**, sur le serveur et non sur cet ordinateur, de sorte qu’ils vous suivent sur n’importe quel ordinateur. Vous pouvez en garder jusqu’à 50 ; la liste montre combien vous en avez, et quand elle est pleine la page vous demande d’en supprimer un pour en enregistrer un autre. Un build est enregistré quand le serveur le dit : la page affiche **Enregistrement…** pendant l’attente, et si le serveur refuse ou reste injoignable, elle dit pourquoi et le build reste non enregistré, vos modifications étant toujours dans l’éditeur. Un build enregistré n’est que des noms d’objets, quelques étiquettes et le nom et la note que vous avez saisis, et aucun autre pilote ne peut le voir. Pour en donner un à un ami, exportez-le.

## Partager et exporter {#share-and-export}

**Exporter** sur un build ouvre une fenêtre avec le build en texte (JSON). **Copiez**-le pour le coller dans un chat, ou choisissez **Enregistrer dans un fichier**, qui écrit `spacecorps-build-<name>.json` dans le dossier `exports` et n’écrase jamais un fichier plus ancien. Un ami colle le texte sous **Importer › Coller**, ou met le fichier dans son propre dossier `exports` et le choisit sous **Depuis un fichier**. Le texte contient les noms d’objets de l’équipement, le vaisseau et le nom et la note du build, et rien de votre compte.

## Conseils {#tips}

1. **Regardez avant de farmer.** Ouvrez un objet dans le Livre de recettes et lisez ses Sources et ses Étapes avant de passer une journée sur un butin qui n’est pas le bon.
2. **Comptez à partir de zéro.** Désactivez **Compter ce que j’ai** (dans Builds : **Déduire ce que j’ai**) pour voir ce que coûte un objet ou un build à partir de rien ; laissez-le activé pour voir ce qu’il vous faut encore.
3. **Partez d’un préréglage.** **Modifier une copie**, changez une pièce, et les statistiques et le coût suivent.
4. **Lisez aussi les arbres.** Les [Arbres d’objets](/wiki/06-Items/Item-Trees.md) montrent chaque sorte d’objet côte à côte, et le Livre de recettes en calcule le prix pour vous.
