<!-- wiki-i18n source: 8e594dc8a7d6e482 -->
<!-- wiki-i18n title: Roquettes -->
# Roquettes {#rockets}

Les roquettes sont une seconde arme à côté de vos lasers : un tir toutes les quelques secondes, qui frappe bien plus fort qu’une salve laser. Douze roquettes en quatre types, de trois gammes chacun, deux autres que seul l’Assemblage fabrique, et **un seul minuteur de rechargement de 5 secondes que toutes partagent**, quelle que soit celle que vous tirez. Les roquettes communes et rares s’achètent avec des **crédits** ; les quatre roquettes épiques s’achètent avec du **Thulium**. Une [formation de drones](/wiki/03-Mechanics/Formations.md) peut augmenter les dégâts d’une roquette et allonger ou raccourcir ce minuteur : voir [Formations de drones et roquettes](#drone-formations-and-rockets).

## En une minute {#in-one-minute}

- **Douze roquettes à acheter.** Quatre types (Lancet, Rivet, Ember, Scatter), trois gammes chacun. Les communes et les rares coûtent des crédits, les épiques du Thulium. Deux autres roquettes, la N.U.K.E. et la N.I.K.E., sont fabriquées à l’Assemblage.
- **Chaque roquette tire ses dégâts au sort.** Au moment du tir, le jeu choisit un nombre entre les dégâts les plus bas et les plus hauts de la roquette (une Lancet I : de 1 700 à 2 100). Votre vaisseau, vos lasers, vos amplis et vos boosters n’y changent rien, seule une formation de drones le fait. Les roquettes que tirent les aliens ne font pas de jet : elles infligent un nombre fixe ([Contre les aliens](#against-the-aliens)).
- **Les explosions sont plus fortes au milieu.** Les roquettes Ember et Scatter éclatent et blessent tous les vaisseaux dans l’anneau : le nombre entier au centre, la moitié au bord.
- **Un seul minuteur pour toutes.** Après un tir, vous attendez 5 secondes avant le suivant, quelle que soit la roquette.
- **Guidée ou droite.** Une roquette guidée (Lancet, Ember) a besoin d’une cible que vous avez sélectionnée. Une droite (Rivet, Scatter) vole vers votre curseur.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Arbre d’objets {#item-tree}

Ce que fabrique l’Assemblage exige d’abord sa technologie ; pointez un objet pour voir combien de temps sa recherche prend. L’arbre des technologies, le carburant et le boost : [Recherche](/wiki/03-Mechanics/Research.md).

```tree
Lancet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets

Lancet I -> Lancet II -> Lancet III
Rivet I -> Rivet II -> Rivet III
Ember I -> Ember II -> Ember III
Scatter I -> Scatter II -> Scatter III => N.U.K.E.
```
<!-- item-tree:end -->

## Les quatre types {#the-four-kinds}

| | Cible unique : touche un vaisseau | Explosion de zone : éclate et blesse tout ce qui est proche |
| :--- | :--- | :--- |
| **Guidée** : verrouille la cible que vous avez sélectionnée et la poursuit | Lancet I, Lancet II, Lancet III | Ember I, Ember II, Ember III |
| **Droite** : vole vers votre curseur | Rivet I, Rivet II, Rivet III | Scatter I, Scatter II, Scatter III |

Chaque type est une **famille**, qui porte le nom de sa roquette commune, et la gamme est un chiffre romain : **Lancet I**, **Lancet II** et **Lancet III** sont la roquette guidée à cible unique commune, rare et épique, et les familles Rivet, Ember et Scatter suivent le même modèle. Le code d’une roquette sur sa vignette dans le sélecteur de roquettes et dans le hangar est formé des trois lettres de sa famille et de son chiffre (LNC II, RVT III, EMB I, SCT II) ; les deux roquettes que seul l’Assemblage fabrique gardent leur nom et leur code (N.U.K.E., NUK ; N.I.K.E., NIK).

- Les roquettes **guidées** ont besoin d’une cible sélectionnée dans leur **portée de verrouillage** au départ. Elles la poursuivent avec une vitesse de virage limitée, si bien qu’un vaisseau rapide et éloigné peut distancer une roquette bon marché. Si la cible meurt, quitte la carte ou atteint une zone sûre, la roquette continue tout droit et n’en choisit pas une autre.
- Les roquettes **droites** n’ont besoin d’aucune cible et ignorent celle que vous avez sélectionnée : elles volent toujours vers votre **curseur**, au point situé dessous dans la vue de vol. **Cliquez sur l’emplacement d’une roquette droite pour l’armer** (l’emplacement reçoit un cadre blanc et un réticule, et votre curseur de souris devient un réticule au-dessus de l’espace), puis **cliquez dans l’espace** : la roquette vole vers le point sur lequel vous avez cliqué et votre vaisseau reste où il est. Esc, un clic droit ou un nouveau clic sur le même emplacement la relâche. Si les roquettes sont encore en rechargement, le clic ne fait que vous le dire et la roquette reste armée. Les touches numériques et **Tirer roquette** tirent aussitôt vers le dernier point où se trouvait le curseur dans la vue de vol ; tant que le curseur n’y est pas passé, elles volent dans la direction où votre vaisseau **pointe**. Elles volent droit, donc un vaisseau qui traverse à vitesse élevée peut les esquiver.
- Une roquette à **cible unique** touche le premier vaisseau qu’elle peut toucher (une guidée, seulement sa cible). Une **explosion de zone** éclate à côté du premier vaisseau qu’elle rencontre, au point où vous l’avez visée, ou là où son vol s’achève, et blesse tous les vaisseaux situés dans son **rayon d’explosion** : pleins dégâts au centre, la moitié au bord. L’anneau que l’explosion dessine sur la carte est sa portée exacte.
- **Astéroïdes.** Une roquette tirée sur un [astéroïde](/wiki/03-Mechanics/Asteroid-Mining.md) touche cet astéroïde et rien d’autre, et une roquette qui n’est pas tirée sur un astéroïde les traverse tous. Les douze roquettes de la boutique et la N.U.K.E. peuvent en briser un ; la N.I.K.E. non.

## Les douze roquettes {#the-twelve-rockets}

Chaque roquette a **ses propres dégâts, déterminés par un jet au moment du tir** : n’importe où entre son nombre le plus bas et son nombre le plus haut, et le tableau donne les deux et la moyenne. Cela ne dépend ni de votre vaisseau, ni de vos lasers et de leurs amplis, ni de vos boosters, ni de vos munitions, ni de vos drones, et une roquette ne fait jamais de coup critique. Seule une **formation de drones** les change : le tableau ci-dessous donne les dégâts sans formation (voir [Formations de drones et roquettes](#drone-formations-and-rockets)). Une roquette à cible unique inflige les dégâts de son jet au vaisseau qu’elle touche ; une explosion ne fait qu’un jet et en inflige le résultat à **tous les vaisseaux qu’elle couvre**, le nombre entier au centre et la moitié au bord. La *pénétration de bouclier* est retranchée de l’absorption de votre cible pour ce coup (l’absorption d’un vaisseau est la part d’un tir que prennent ses boucliers, voir [Mécaniques des boucliers](/wiki/03-Mechanics/Shields.md#shield-penetration)) : les 35 % d’une Lancet III laissent aux boucliers d’un vaisseau à 80 % 45 % du tir et envoient les 55 % restants à la coque. Une explosion n’en a aucune.

| Nom | Type | Rareté | Dégâts | Moyenne | Pénétration de bouclier | Rayon d’explosion | Portée de verrouillage | Portée | Vitesse | Prix | Maximum transportable |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **Lancet I** | Guidée, cible unique | Commun | 1 700–2 100 | 1 900 | 10 % | – | 700 | 1 040 | 520 | 500 crédits | 5 000 |
| **Lancet II** | Guidée, cible unique | Rare | 3 500–4 200 | 3 850 | 25 % | – | 1 000 | 1 584 | 660 | 800 crédits | 2 000 |
| **Lancet III** | Guidée, cible unique | Épique | 5 200–6 200 | 5 700 | 35 % | – | 1 300 | 2 296 | 820 | 5 Thulium | 500 |
| **Rivet I** | Droite, cible unique | Commun | 2 200–2 700 | 2 450 | 5 % | – | – | 1 080 | 900 | 500 crédits | 5 000 |
| **Rivet II** | Droite, cible unique | Rare | 4 500–5 250 | 4 875 | 25 % | – | – | 1 120 | 700 | 800 crédits | 2 000 |
| **Rivet III** | Droite, cible unique | Épique | 7 000–8 000 | 7 500 | 35 % | – | – | 1 100 | 500 | 5 Thulium | 500 |
| **Ember I** | Guidée, explosion de zone | Commun | 1 200–1 400 | 1 300 | – | 170 | 700 | 1 000 | 500 | 500 crédits | 5 000 |
| **Ember II** | Guidée, explosion de zone | Rare | 2 400–2 900 | 2 650 | – | 230 | 920 | 1 500 | 600 | 800 crédits | 2 000 |
| **Ember III** | Guidée, explosion de zone | Épique | 3 500–4 500 | 4 000 | – | 300 | 1 150 | 2 030 | 700 | 5 Thulium | 500 |
| **Scatter I** | Droite, explosion de zone | Commun | 1 500–1 750 | 1 625 | – | 210 | – | 1 088 | 640 | 500 crédits | 5 000 |
| **Scatter II** | Droite, explosion de zone | Rare | 3 000–3 500 | 3 250 | – | 290 | – | 1 080 | 540 | 800 crédits | 2 000 |
| **Scatter III** | Droite, explosion de zone | Épique | 4 500–5 500 | 5 000 | – | 400 | – | 1 092 | 420 | 5 Thulium | 500 |

Plus la gamme est chère, plus la roquette frappe fort, plus elle porte loin, plus elle a de pénétration de bouclier et moins vous pouvez en emporter ; les chères donnent aussi le plus de dégâts pour leur prix. Une roquette droite inflige d’un quart à un tiers de plus que la roquette guidée de même gamme et de même type pour le même prix (23 à 32 % en moyenne), parce qu’il faut la viser. Une explosion inflige environ les deux tiers de la roquette à cible unique de sa gamme et de son type (66 à 70 % en moyenne : une Ember face à une Lancet, une Scatter face à une Rivet), à tous les vaisseaux qu’elle couvre. Les dégâts d’une explosion sont pleins au centre et retombent en ligne droite à **la moitié au bord** : un vaisseau dont la coque est à mi-chemin du bord subit 75 %, et un vaisseau dont la coque est hors de l’anneau ne subit rien. Un tir inflige en moyenne le milieu de sa fourchette, soit 89 à 94 % de son nombre maximal, et le tableau qui compte les roquettes plus bas s’en sert.

## Ce qu’elles coûtent {#what-they-cost}

Une roquette commune coûte 500 crédits, une rare 800 crédits et une épique 5 Thulium, quel que soit le type. Tirée dès que le minuteur le permet, cela fait 6 000 crédits par minute pour une roquette commune, 9 600 pour une rare et 60 Thulium pour une épique, contre les 1 800 crédits par minute que brûlent les trois lasers d’un Ostirion en x1. Un stock plein, c’est 5 000 roquettes communes (2 500 000 crédits), 2 000 rares (1 600 000 crédits) ou 500 épiques (2 500 Thulium) : vous en achetez autant que vous voulez jusque-là, et le *maximum transportable* d’une roquette est la seule limite au nombre que vous en détenez. Les roquettes ne pèsent rien : elles ne prennent aucune place dans la cache de transport. Une roquette toutes les 5 secondes, ce n’est que douze par minute, donc une roquette est un pic de puissance en plus de vos lasers : les bon marché pour les aliens faibles, les chères pour les gros combats. Ce que vous avez mis aux [Enchères](/wiki/03-Mechanics/Auction.md#limits) et les lots que vous y menez comptent dans cette limite quand vous achetez une roquette ou enchérissez dessus.

La boutique liste les roquettes un type à la fois, chacune sous son nom, la roquette commune en premier et l’épique en dernier ; le hangar, la cache de transport et le sélecteur de roquettes suivent le même ordre.

## Contre les aliens {#against-the-aliens}

Le nombre de roquettes nécessaires pour détruire un alien, chaque type de roquette utilisé seul, chaque roquette faisant la moyenne de sa fourchette (Alpha ; les aliens de Beta et de Gamma sont 1,5 et 2 fois plus forts). Une explosion compte comme le vaisseau près duquel elle éclate la reçoit, un peu avant le centre (87 à 93 % des dégâts du centre). Le bouclier d’un alien encaisse 80 % d’un tir, moins la pénétration de bouclier de la roquette. Au jet le plus bas, une élimination demande jusqu’à 15 % de roquettes de plus que le tableau (une Lancet I en demande 48 pour un Goombah, et non 43) ; au meilleur jet, jusqu’à 13 % de moins (39). Une Rivet II, une Lancet III et une Rivet III détruisent un Phantasm en un coup quel que soit le jet ; une Rivet I en demande deux à partir d’un jet de 2 600, et trois en dessous.

| Roquettes nécessaires | Seeker (1 600) | Phantasm (5 200) | Bulwark (26 000) | Goombah (80 000) | Crystalys (416 000) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Lancet I** | 1 | 3 | 14 | 43 | 219 |
| **Lancet II** | 1 | 2 | 7 | 19 | 109 |
| **Lancet III** | 1 | 1 | 5 | 11 | 73 |
| **Rivet I** | 1 | 3 | 11 | 33 | 170 |
| **Rivet II** | 1 | 1 | 6 | 15 | 86 |
| **Rivet III** | 1 | 1 | 4 | 8 | 56 |
| **Ember I** | 2 | 5 | 24 | 71 | 369 |
| **Ember II** | 1 | 3 | 12 | 34 | 177 |
| **Ember III** | 1 | 2 | 8 | 23 | 116 |
| **Scatter I** | 2 | 4 | 18 | 56 | 287 |
| **Scatter II** | 1 | 2 | 9 | 27 | 141 |
| **Scatter III** | 1 | 2 | 6 | 18 | 90 |

- Les roquettes **communes** à cible unique détruisent un Seeker en un coup quel que soit le jet et un Phantasm en trois (une Lancet I en demande une quatrième à son jet le plus bas) ; ce sont les roquettes de tous les jours des premiers secteurs. Les **rares** sont pour le Bulwark et le Goombah : sept roquettes Lancet II viennent à bout d’un Bulwark en environ 30 secondes de minuteur. Les **épiques** à cible unique détruisent un Goombah en huit (Rivet III) à onze (Lancet III). Les explosions valent leur prix quand plusieurs aliens sont proches les uns des autres : une Scatter III qui éclate sur une meute de cinq Phantasms (tous à moins de 250 unités de la cible que vous avez visée) inflige environ 21 000 dégâts à la meute en un seul tir.
- Une élimination aux seules roquettes est une vraie dépense, pas un moyen de s’enrichir : une roquette à cible unique coûte de 15 % (une Rivet II sur un Phantasm) à 95 % (une Lancet I sur un Crystalys) de ce que rapporte l’élimination (en crédits, et en Thulium à 200 crédits l’unité), et les explosions faibles sur les aliens forts coûtent plus que ce que l’élimination rapporte (une Ember I sur un Bulwark : 120 %). Détruire le **Crystalys** avec un seul type exige de 56 à 369 roquettes et au moins quatre minutes et demie de minuteur ; un stock plein de 500 roquettes épiques suffit pour en détruire de quatre à huit. L’alien le plus fort demande un plan : vos lasers avec des munitions x2, une roquette de gamme moyenne toutes les 5 secondes dès la première seconde, et les grosses roquettes décrites plus bas comme pic de puissance.
- Le gain d’une élimination est le même quelle que soit la manière de l’obtenir (voir [le Crystalys](/wiki/04-Aliens/Crystalys.md) pour le plus gros), si bien qu’une élimination à la roquette vaut le coup quand elle vous fait gagner du temps et coûte moins qu’elle ne rapporte.
- **Les aliens tirent aussi des roquettes.** Le Pirate Boss, la Dormant Force et les Pulses des [essaims](/wiki/05-Swarms/Swarms.md) et les Siege Wardens des [clans](/wiki/03-Mechanics/Clans.md#clan-wardens) lancent des roquettes Rivet droites sur le pilote qui les a attaqués, avec le même minuteur de 5 secondes. **La roquette d’un alien ne fait pas de jet et n’utilise pas les fourchettes ci-dessus** : elle inflige un nombre fixe, 2 500 (Rivet I), 5 000 (Rivet II) ou 7 500 (Rivet III), davantage en Beta et en Gamma, où les aliens sont 1,5 et 2 fois plus forts (celle d’un Clan Warden est la même dans tous les mondes). Un vaisseau qui reste en mouvement les esquive. Les boss des essaims laissent aussi des roquettes dans leurs caisses.

## Les roquettes à fabriquer {#the-craft-only-rockets}

Deux roquettes ne sont pas en boutique. **L’Assemblage** les fabrique, et elles suivent toutes les règles ci-dessous (le minuteur partagé, les zones sûres, votre corporation). Ce sont toutes deux des roquettes droites : elles volent vers le point situé sous votre curseur, comme toute roquette droite (le jeu envoie la direction du curseur quelle que soit votre sélection ; seul un ancien client 0.4.3, qui n’envoie aucune direction, voit le serveur les faire voler vers la cible sélectionnée, sinon vers le point situé sous son curseur, sinon dans la direction où pointe le vaisseau). Leur jet va de **90 % à 100 %** de leur nombre maximal, une plage plus étroite que celle des douze, si bien que ce qu’elles détruisent en un coup plus bas vaut aussi au jet le plus bas.

| Nom | Type | Rareté | Dégâts | Pénétration de bouclier | Rayon d’explosion | Portée | Vitesse | Maximum transportable | Fabriquée à partir de |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **N.U.K.E.** | Droite, explosion de zone | Légendaire | 45 000–50 000 | – | 900 | 1 200 | 300 | 10 | 1 N.U.K.E. par fabrication : 150 000 crédits, 3 000 Thulium, 6 Scatter III, 4 Power Core, 10 Reinforced Hull Plate, 40 Ship Fragment, 80 Cataclysite |
| **N.I.K.E.** | Droite, cible unique | Mythique | 67 500–75 000 | 35 % | – | 4 050 | 900 | 20 | 5 N.I.K.E. par fabrication : 100 000 crédits, 1 500 Thulium, 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite |

- **N.U.K.E.** : la plus grosse explosion du jeu. Une explosion de 900 unités, soit deux fois la portée des 400 de la Scatter III et cinq fois sa surface : de 45 000 à 50 000 à chaque vaisseau pris dedans au centre, tombant à la moitié, soit de 22 500 à 25 000, au bord. Elle est lente (quatre secondes en vol). Une N.U.K.E. anéantit tous les Seekers et Phantasms de toute son explosion et un Bulwark à 830 unités de l’éclatement (934 au meilleur jet), soit presque toute l’explosion ; elle retire plus de la moitié de la vie d’un Goombah et un neuvième de celle d’un Crystalys. Contre les pilotes, c’est le plus gros coup qui existe : voir les règles plus bas. L’anneau sur la carte est sa portée exacte.
- **N.I.K.E.** : une roquette à cible unique comme une Rivet I, avec 67 500 à 75 000 dégâts et une pénétration de bouclier de 35 % : **elle touche le premier vaisseau qu’elle rencontre et s’y épuise.** C’est aussi la roquette qui produit de la [Dark Matter](/wiki/03-Mechanics/Black-Hole.md) : tirée sur le trou noir au centre du Secteur dangereux 4, elle est engloutie quand elle franchit l’horizon des événements, et le trou rend de la Dark Matter. Elle vole sur 4 050 unités en 4,5 secondes : tirez-la de n’importe où entre le bord de la zone de radiation et 4 380 unités du centre. De plus loin, elle retombe trop court et est perdue. Cinq N.I.K.E. produisent environ dix Dark Matter.
- **Le piège.** Une N.I.K.E. qui rencontre un vaisseau en chemin, un rival qui attend sur la ligne de tir ou tout ce qu’elle peut blesser, lui inflige 67 500 à 75 000 dégâts et disparaît : le trou noir n’obtient rien, et vous non plus. Rien d’autre ne rôde à l’intérieur de l’anneau du trou qu’elle pourrait toucher par accident (les aliens et les pilotes de corporation s’en tiennent à l’écart) : seulement des pilotes venus chercher de la Dark Matter, ou qui vous attendent au bord. Elle traverse votre propre corporation, les vaisseaux en zone sûre et ceux que vous n’avez pas encore le droit de blesser. Si vous quittez la carte après l’avoir tirée, elle poursuit sa route sans blesser personne et produit quand même votre Dark Matter.
- L’Assemblage ne lance pas une fabrication qui vous ferait dépasser le *maximum transportable* d’une roquette, en comptant ce que vous avez en file.

## Tirer {#firing}

1. Achetez des roquettes à la boutique (la catégorie **Roquettes**), jusqu’au *maximum transportable* de chacune : des crédits pour les communes et les rares, du Thulium pour les épiques.
2. Ouvrez **Roquettes** au-dessus de la barre rapide, et faites glisser celles que vous voulez sur des emplacements. Le sélecteur affiche une colonne par type et une ligne par gamme, avec ce que vous portez de chacune. Dessous se trouve une ligne à part, **Spéciales · Assemblage seul**, pour la N.U.K.E. et la N.I.K.E. (un petit marteau marque celle dont vous ne portez aucune).
3. Appuyez sur la touche de l’emplacement. Cliquer sur l’emplacement d’une roquette **guidée** la tire sur votre cible sélectionnée ; cliquer sur celui d’une roquette **droite** l’arme, et votre prochain clic dans l’espace la tire là. La touche **Tirer roquette** (`R` par défaut, reconfigurable dans Paramètres › Commandes) tire la roquette que vous avez tirée en dernier, ou la première de la barre.
4. Un balayage circulaire recouvre **chaque** emplacement de roquette pendant les 5 secondes qui précèdent le prochain lancement, avec les secondes restantes au centre. Un appui avant la fin vous indique seulement que les roquettes se rechargent (un appui dans le dernier dixième de seconde tire quand même). Une formation de drones peut fixer l’attente entre 3,65 et 6,75 secondes (voir plus bas).

Survolez un emplacement de roquette pour voir ses chiffres (ses dégâts les plus bas et les plus hauts ; la boutique et le hangar indiquent la même chose) et, dans le monde, son anneau de verrouillage (vert quand la cible sélectionnée est à portée) ou sa ligne et son cercle d’explosion. Une roquette verrouillée sur **vous** fait clignoter le bord de votre écran en rouge.

La **N.U.K.E.** dessine son explosion sur la carte avant que vous ne tiriez (le cercle de 900 unités au point visé) et, quand elle éclate, un flash blanc sur la vue, un anneau qui s’étend jusqu’à la portée exacte en une seconde environ et reste deux secondes de plus, un nuage qui s’élève comme un champignon, et une secousse de la caméra d’autant plus forte que vous êtes près. **Réduire les tremblements de l’écran** supprime la secousse, et **Réduire les animations** raccourcit le flash à un tiers de seconde, à moins de la moitié de sa lumière (les deux se trouvent dans les Paramètres, sous Graphismes) ; une qualité de particules plus basse rend le nuage plus clairsemé et supprime les étincelles, jamais le flash ni l’anneau. La **N.I.K.E.** se vise comme une Rivet I, par la ligne qui va de votre vaisseau au curseur, et le jeu ne la refuse jamais parce que vous êtes loin du trou noir ou sur une carte qui n’en a pas : c’est à vous de juger où elle va. Sa carte indique **Trou noir : Produit de la Dark Matter** à côté de ses dégâts. Elle laisse une traînée violette avec des étincelles qui s’enroulent autour ; un vaisseau qu’elle rencontre prend le coup comme avec n’importe quelle roquette, et quand elle franchit l’horizon à la place, le trou s’embrase.

## Formations de drones et roquettes {#drone-formations-and-rockets}

Une [formation de drones](/wiki/03-Mechanics/Formations.md) portée est la seule chose qui change une roquette. Tous les chiffres de dégâts de cette page sont ceux d’un vaisseau sans formation.

- **Dégâts.** Le bonus de roquettes de Ballista (+55 %), Bodkin (+29 %) et Asterism (+24 %) multiplie les dégâts des 14 roquettes, N.U.K.E. et N.I.K.E. compris. Le prix de tous les dégâts de Testudo compte aussi sur les roquettes, et les dégâts aux aliens de Culler comptent sur une roquette qui touche un alien. Tous les facteurs d’une roquette ensemble s’arrêtent à ×1,59.
- **Rechargement.** Asterism allonge le minuteur commun de 35 % (6,75 secondes), Cordon de 11 % (5,55) et Redoubt le raccourcit de 27 % (3,65), mais jamais en dessous du vol de la roquette plus un instant : 4,1 secondes après une N.U.K.E. et 4,6 après une N.I.K.E. L’attente est fixée au tir, donc changer de formation ensuite ne la raccourcit pas, et le balayage sur les emplacements de roquette la suit.
- **Les limites des deux grosses tiennent.** Avec la meilleure formation, une N.I.K.E. frappe jusqu’à 116 250, ce qu’un Paragon intact (128 000) survit, et une N.U.K.E. jusqu’à 77 500, ce qu’un Goombah (80 000) survit.
- **Esquive.** Les 7 % d’esquive d’Asterism donnent à une roquette directe qui vous touche 7 % de chances de ne faire aucun dégât, et un « Raté » flottant s’affiche au-dessus de votre vaisseau ; une explosion de zone ne vise pas et n’est jamais esquivée.
- **Pénétration.** Gemini et Stiletto ajoutent leurs points à la pénétration de bouclier d’une roquette directe (une explosion n’en a pas), jusqu’à 40 % en tout. Un tir laser va jusqu’à 50 % ([Lasers et munitions](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)).

## Règles {#rules}

- Il ne vous faut **aucun laser équipé** pour tirer une roquette, et vos lasers ne changent ni ce qu’elle inflige ni sa portée : une roquette guidée verrouille une cible dans sa propre portée de verrouillage, une droite vole sur sa propre distance. Sans laser équipé, la tuile Portée du hangar affiche un tiret, et seules vos roquettes tirent.
- Une roquette est consommée par lancement, qu’elle touche ou non.
- Les roquettes suivent les règles des lasers : rien ne subit de dégâts dans une **zone sûre**, aucun pilote n’est blessé avant la fin du **Protocole de paix** ni là où un secteur interdit le PvP, et **votre propre corporation et votre propre groupe ne sont jamais blessés** par vos roquettes, en coup direct comme en explosion.
- Lancer une roquette met fin aussitôt à votre propre protection de zone sûre. C’est un tir : cela met aussi fin à votre propre **occultation**, et le Cloaking CPU se recharge alors pendant une minute, comme après toute fin d’occultation. Occulté ou non, un lancement vous empêche de vous occulter pendant les 10 secondes qui suivent (voir [Extras](/wiki/06-Items/Extras.md)).
- Un vaisseau **occulté** ou dans les **3 secondes de son EMP** ne peut pas être verrouillé : une roquette guidée est refusée, et celle qui vole déjà vers lui perd son verrouillage et continue tout droit. Une roquette droite à cible unique traverse un tel vaisseau. Une **explosion de zone** n’a besoin d’aucun verrouillage, elle blesse donc les vaisseaux qu’elle couvre, occultés ou non, et elle met fin à une occultation (voir [Extras](/wiki/06-Items/Extras.md)).
- **Rien ne plafonne ce qu’une roquette inflige à un pilote.** Le vaisseau d’un autre pilote encaisse tous les dégâts : le bouclier d’abord (son absorption moins la pénétration de bouclier de la roquette), puis la coque. Les petits vaisseaux ne tiennent pas. Avec les boucliers de série (Light, 45 % d’absorption), une N.I.K.E. détruit, quel que soit le jet, un Protos, un Kitefin ou un Ostirion intact en un coup (un Paragon perd de 47 à 53 % de sa coque, un Wraith environ un cinquième), et une N.U.K.E. détruit un Protos n’importe où dans son explosion, un Kitefin à environ 50 unités de l’éclatement (220 au meilleur jet) et rien de plus gros en une seule explosion. Deux roquettes Lancet III ou deux Rivet III détruisent un Protos, quel que soit le jet ; un Wraith en demande entre 45 et 70. Le Protocole de paix, les zones sûres et votre corporation sont ce qui se dresse entre un pilote et une roquette. Ces chiffres valent pour un vaisseau sans formation ; une formation de roquettes les augmente jusqu’à 55 % (voir [Formations de drones et roquettes](#drone-formations-and-rockets)).
- Seul le **coup direct** d’une roquette revendique un alien (voir [Combat](/wiki/03-Mechanics/Combat.md)) ; le bord d’une explosion peut blesser un alien revendiqué sans le lui prendre. Tout alien qu’une explosion blesse, même endormi, se retourne contre vous, comme avec un tir laser (un Seeker ou un Goombah, qui ne font que riposter, compris) ; celui que l’explosion manque reste endormi.
- Le minuteur est le vôtre : il survit à un saut, à une reconnexion, à un changement de vaisseau et à un vaisseau détruit.

Les douze roquettes du premier tableau s’achètent (des crédits pour les communes et les rares, du Thulium pour les épiques) ; la N.U.K.E. et la N.I.K.E. se fabriquent.

Voir aussi : [Lasers et munitions](/wiki/06-Items/Lasers.md), [Combat](/wiki/03-Mechanics/Combat.md), [Le trou noir](/wiki/03-Mechanics/Black-Hole.md).
