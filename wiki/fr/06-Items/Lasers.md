<!-- wiki-i18n source: 3d97a6f4bd324d8d -->
<!-- wiki-i18n title: Lasers -->
# Lasers et munitions {#lasers-ammo}

Les armes sont le principal moyen d’infliger des dégâts dans SpaceCorps.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Arbre d’objets {#item-tree}

Ce que fabrique l’Assemblage exige d’abord sa technologie ; pointez un objet pour voir combien de temps sa recherche prend. L’arbre des technologies, le carburant et le boost : [Recherche](/wiki/03-Mechanics/Research.md).

```tree
Quantum Laser 1 | laser, shoddy | buy 8000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser 2 | laser, common | buy 80000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser 3 | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-3 | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser 3, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-3, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp 1 | laser-amp, shoddy | buy 10000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp 1 | laser-amp, shoddy | buy 15000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Arc Amp | laser-amp, uncommon | buy 60000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Focus Amp | laser-amp, uncommon | buy 60000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Pulse Amp | laser-amp, rare | buy 1500 Thulium | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Prism Amp | laser-amp, rare | buy 1500 Thulium | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Nova Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Pulse Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Apex Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Prism Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Standard Battery | ammo, common | buy 10 Credits | /wiki/06-Items/Lasers.md#laser-ammunition
Siphon Battery | ammo, rare | buy 0.25 Thulium | /wiki/06-Items/Lasers.md#siphon-battery
Advanced Plasma | ammo, rare | buy 0.5 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Ultra Core | ammo, rare | buy 1 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Experimental Fusion Core | ammo, epic | buy 2.2 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition

Quantum Laser 1 -> Quantum Laser 2 -> Quantum Laser 3 => Starfire-3 => Helios Beam
Damage Amp 1 -> Arc Amp -> Pulse Amp => Nova Amp
Crit Amp 1 -> Focus Amp -> Prism Amp => Apex Amp
Standard Battery -> Advanced Plasma -> Ultra Core -> Experimental Fusion Core
```
<!-- item-tree:end -->

## Lasers

Équipez des lasers directement dans les emplacements laser du vaisseau ou dans des drones pour accroître vos capacités offensives.

| Nom | Rareté | Dégâts de base | Taux critique | Portée | Empl. ampli | Coût |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Quantum Laser 1** | Médiocre | 55 | – | 600 | 1 | 8 000 crédits |
| **Quantum Laser 2** | Commun | 65 | – | 700 | 2 | 80 000 crédits |
| **Quantum Laser 3** | Rare | 80 | 10 % | 800 | 3 | À fabriquer |
| **Starfire-3** | Mythique | 135 | 15 % | 850 | 3 | À fabriquer |
| **Helios Beam** | Mythique | 185 | 25 % | 900 | 3 | À fabriquer |

La colonne Portée est celle de chaque laser. **Votre vaisseau tire à la moyenne des portées de ses lasers** (les lasers de vos drones comptent aussi), arrondie à l’unité la plus proche, et chaque laser tire dès que la cible se trouve à l’intérieur de cette distance. Un Starfire-3 à côté de deux Quantum Laser 2 donne au vaisseau une portée de 750, et non de 850 ; trois Starfire-3 gardent 850, et des lasers tous identiques ne changent rien. Un bonus de portée de la Forge compte sur son propre laser avant que la moyenne ne soit calculée. Sans laser, le hangar n’affiche aucune portée (un tiret) et les lasers ne peuvent pas tirer, mais vos roquettes le peuvent toujours, chacune avec sa propre portée (voir [Roquettes](/wiki/06-Items/Rockets.md)). Dans le hangar, la tuile indique « Portée moy. » quand vos lasers diffèrent, et son survol liste la portée de chaque laser.

Les Quantum Laser 1 et 2 n’ont pas de taux critique propre (« – ») : un Damage Amp ou un Crit Amp dans leurs emplacements leur en apporte un. Les coups critiques s’affichent dans une autre couleur parmi les nombres de dégâts flottants (cyan glacé, plus grands, avec un « ! »).

### Fabriquer les trois meilleurs lasers {#making-the-top-three-lasers}

Le **Quantum Laser 3**, le **Starfire-3** et le **Helios Beam** ne se fabriquent qu’à l’**Assemblage**. Le Quantum Laser 3 n’est plus vendu à la boutique ; un pilote qui en possède déjà un le garde. Chaque recette demande des plaques de la Fonderie du [Skylab](/wiki/03-Mechanics/Skylab.md) :

| Laser | Durée de fabrication | Ce qu’il faut |
| :--- | :---: | :--- |
| Quantum Laser 3 | 1 min | 10 Ship Fragments, 2 Velkonite Reinforced Plates, 1 500 Thulium |
| Starfire-3 | 1 min | 1 Quantum Laser 3, 15 Ship Fragments, 8 Velkonite Reinforced Plates, 1 Reinforced Hull Plate, 1 500 Thulium, 100 000 crédits |
| Helios Beam | 3 min | 1 Starfire-3, 50 Cataclysite, 2 Power Cores, 18 Orvium Reinforced Plates, 4 Reinforced Hull Plates, 2 000 Thulium |

La page Assemblage montre ce que vous possédez face à ce qu’une recette demande, et le bouton Assembler indique ce qui vous manque. Pointez l’image ou le nom d’une recette, ou l’un de ses matériaux, pour lire la description complète de l’objet et ses statistiques.

**Le Starfire-3 est fabriqué à partir d’un Quantum Laser 3.** Vous fabriquez d’abord le Quantum Laser 3 et le Starfire-3 le consomme. Rien de ce que le Quantum Laser 3 a déjà pris n’est redemandé : les deux ensemble coûtent donc exactement ce qu’un Starfire-3 coûtait seul : 3 000 Thulium, 100 000 crédits, 25 Ship Fragments, 10 Velkonite Reinforced Plates, 1 Reinforced Hull Plate et 2 minutes. Si vous avez déjà un Quantum Laser 3, vous ne payez que la part propre du Starfire-3. Les règles sont celles du Helios Beam, plus bas : le Starfire-3 garde le rang d’enchantement du Quantum Laser 3 qu’il consomme (un Quantum Laser 3 Divin donne un Starfire-3 Divin) et ses bonus sont tirés de nouveau ; vous choisissez quel Quantum Laser 3 part, la carte demande d’abord confirmation avant d’en utiliser un au-dessus de Standard, et le Quantum Laser 3 doit être libre : **retirez-le d’abord de votre vaisseau** (ses amplis retournent dans votre inventaire), et sortez-le de la cache de transport. Le bouton Assembler indique « Retirez d’abord Quantum Laser 3 » quand il se trouve sur un vaisseau.

**Le Helios Beam est fabriqué à partir d’un Starfire-3.** Vous fabriquez d’abord le Starfire-3 (3 000 Thulium et 100 000 crédits, Quantum Laser 3 compris) et le Helios Beam le consomme, comme le [Master Drone](/wiki/06-Items/Drones.md) consomme un Slave Drone. Rien de ce que le Starfire-3 a déjà pris n’est redemandé : les deux ensemble coûtent donc les 5 000 Thulium, la Cataclysite, les Power Cores et les Reinforced Hull Plates que le Helios Beam demandait seul, et 18 plaques d’Orvium au lieu de 20 (les dix plaques de Velkonite du Starfire-3 remplacent les deux manquantes) ; ce que vous payez en plus, ce sont les 100 000 crédits et les 25 Ship Fragments du Starfire-3. La règle est celle des [améliorations de modules](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly) : le Helios Beam garde le rang d’enchantement du Starfire-3 qu’il consomme (un Starfire-3 Divin donne un Helios Beam Divin) et ses bonus sont tirés de nouveau ; vous choisissez quel Starfire-3 part quand vous en avez plusieurs, et la carte demande d’abord confirmation avant d’en utiliser un au-dessus de Standard. Le Starfire-3 doit être libre : **retirez-le d’abord de votre vaisseau** (les amplis qui y sont installés retournent dans votre inventaire), et sortez-le de la cache de transport. Le bouton Assembler indique « Retirez d’abord Starfire-3 » quand il se trouve sur un vaisseau.

D’où viennent les plaques :

- Les **Velkonite Reinforced Plates** (Quantum Laser 3 et Starfire-3) sont forgées à partir de Velkonite, 40 unités de minerai par plaque au niveau 1 de la Fonderie. Les **Orvium Reinforced Plates** (Helios Beam) sont forgées à partir d’Orvium, 80 unités de minerai par plaque.
- Le minerai ne vient que des collecteurs de votre Skylab. Un Collecteur de Velkonite de niveau 5 extrait 18 Velkonite par heure : les plaques d’un Quantum Laser 3 demandent donc environ 4 heures d’extraction, et les dix plaques d’un Starfire-3 (deux dans son Quantum Laser 3, huit à sa propre étape) environ 22. Le Helios Beam est le plus long : ses 18 plaques demandent 1 440 Orvium, soit environ 4 jours avec un Collecteur d’Orvium de niveau 5.
- L’Entrepôt de ressources contient 240 de chaque minerai au niveau 1 : 6 plaques de Velkonite ou 3 d’Orvium avec la Fonderie au niveau 1. Forgez donc au fur et à mesure (un lot de la Fonderie fait jusqu’à 10 plaques au niveau 1) ou améliorez l’entrepôt.
- Les plaques forgées attendent dans la Fonderie que vous les récupériez, vaisseau posé, et arrivent dans votre inventaire comme des objets ordinaires.

Ce sont les aliens qui lâchent les Ship Fragments, la Cataclysite, les Power Cores et les Reinforced Hull Plates ; chaque source et chaque usage de chaque matériau figurent sur la page [Ressources](/wiki/06-Items/Resources.md) ; les listes de butin des pages du [Bulwark](/wiki/04-Aliens/Bulwark.md) et du [Goombah](/wiki/04-Aliens/Goombah.md) indiquent les quantités.

---

## Amplificateurs laser (amplis) {#laser-amplifiers-amps-}

Installez-les directement dans l’emplacement d’un laser pour augmenter ses caractéristiques. Il y a deux gammes de quatre échelons chacune : la **gamme dégâts** ajoute un montant fixe de dégâts, et la **gamme critique** ajoute du taux critique et des dégâts critiques fixes.

| Nom | Rareté | Boost de dégâts | Boost de critique | Dégâts critiques fixes | Coût |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Damage Amp 1** | Médiocre | +10 | +5 % | +5 | 10 000 crédits |
| **Arc Amp** | Peu commun | +16 | +5 % | +8 | 60 000 crédits |
| **Pulse Amp** | Rare | +26 | +6 % | +13 | 1 500 Thulium |
| **Nova Amp** | Épique | +38 | +7 % | +20 | À fabriquer |
| **Crit Amp 1** | Médiocre | +0 | +15 % | +0 | 15 000 crédits |
| **Focus Amp** | Peu commun | +0 | +20 % | +14 | 60 000 crédits |
| **Prism Amp** | Rare | +0 | +25 % | +24 | 1 500 Thulium |
| **Apex Amp** | Épique | +0 | +25 % | +44 | À fabriquer |

Le Nova Amp et l’Apex Amp se fabriquent à l’[Assemblage](/wiki/06-Items/Overview.md#upgrading-modules) à partir d’un Pulse Amp et d’un Prism Amp, avec du Thulium, du butin et 3 Velkonite Reinforced Plates de votre Skylab chacun. Ils gardent le rang d’enchantement de l’ampli qu’ils consomment, et leurs bonus sont tirés de nouveau ([Améliorations de modules](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)).

### Quel ampli où {#which-amp-goes-where}

Un ampli de dégâts ajoute les mêmes dégâts à n’importe quel laser, c’est donc sur les **lasers Quantum** qu’il vaut le plus. Un ampli critique multiplie ce que le laser fait déjà, il vaut donc d’autant plus que le laser frappe fort : il égale la gamme dégâts sur le **Starfire-3** et la devance d’environ 3,5 % sur le **Helios Beam**. Le taux critique d’un laser s’arrête à 100 % : trois Prism Amps ou Apex Amps portent un Helios Beam exactement à ce plafond.

Garni du même ampli, un laser est toujours plus fort que celui du dessous, si bien qu’un meilleur ampli ne remplace jamais un meilleur laser : un Quantum Laser 3 avec trois Nova Amps fait moins de dégâts qu’un Helios Beam avec trois Damage Amp 1 (avec des pièces du même rang d’enchantement : un Quantum Laser 3 et des Nova Amps forgés au rang Divin ou supérieur, avec les meilleurs tirages, peuvent dépasser un Helios Beam ordinaire garni de Damage Amp 1, de justesse au rang Divin).

---

## Munitions laser {#laser-ammunition}

Des batteries consommables qui multiplient les dégâts de vos salves laser :

| Nom | Rareté | Multiplicateur de dégâts | Pénétration de bouclier | Prix à l’unité |
| :--- | :--- | :---: | :---: | :--- |
| **Standard Battery** | Commun | 1,0x | – | 10 crédits |
| **Advanced Plasma** | Rare | 2,0x | – | 0,5 Thulium |
| **Ultra Core** | Rare | 3,0x | 5 % | 1,0 Thulium |
| **Experimental Fusion Core** | Épique | 4,0x | 10 % | 2,2 Thulium |
| **Siphon Battery** | Rare | 1,0x, boucliers uniquement | – | 0,25 Thulium |

La **pénétration de bouclier** est retranchée de l’absorption de votre cible à chaque tir de vos salves : les boucliers encaissent l’absorption de la cible moins la pénétration (voir [Mécaniques des boucliers](/wiki/03-Mechanics/Shields.md#shield-penetration)). Face à un vaisseau à 80 % (le meilleur bouclier avec les meilleures cellules), les 10 % des munitions x4 laissent aux boucliers 70 % du tir et à la coque 30 %. Cela compte surtout face à des vaisseaux dont la coque est petite à côté du bouclier ; un très grand vaisseau à 80 % résiste pareil dans les deux cas. Les aliens n’ont pas de stat d’absorption à proprement parler (leurs boucliers encaissent 80 % d’un tir), et la pénétration s’en retranche aussi.

### Siphon Battery

La Siphon Battery est une munition qui sert à voler des boucliers plutôt qu’à briser des coques. Elle inflige **des dégâts x1 directement au bouclier de la cible** et ajoute le même montant à **votre propre bouclier**, jusqu’à votre maximum. Choisissez-la dans le sélecteur de munitions de la barre rapide comme n’importe quelle autre munition (c’est la tuile au vortex turquoise). Elle ne tire pas de rayon : une sonde turquoise fine et discrète part vers la cible, le bouclier de la cible s’illumine en turquoise là où elle arrive, et le bouclier que vous avez drainé revient visiblement vers votre vaisseau sous forme de paquets turquoise lumineux (de trois à dix, davantage pour un drain plus important), l’un après l’autre pendant environ une demi-seconde. Chaque paquet qui arrive fait pulser votre bouclier. Vous voyez la même chose pour la Siphon Battery de tout pilote en vue, quelle que soit sa victime : aliens, autres pilotes et vaisseaux de pilotes de corporation.

- **Bouclier uniquement** : la coque n’est jamais touchée, l’absorption de la cible ne répartit pas les dégâts, et une Siphon Battery ne peut jamais rien détruire. Ses dégâts sont plafonnés par ce que le bouclier de la cible contient encore.
- **Rien à prendre** : contre une cible sans bouclier, elle ne draine rien et ne donne rien. La salve est tout de même dépensée, une batterie par laser, comme avec toute munition. Vous ne voyez que la sonde et un faible scintillement sur la coque, et aucun paquet.
- **Gain** : votre bouclier ne dépasse jamais son maximum, et absorber du bouclier ne retarde pas votre propre régénération de bouclier.
- Les **aliens comme les pilotes** ont des boucliers à drainer. Un drain qui prend du bouclier à un alien compte comme un coup pour la [revendication du premier tir](/wiki/03-Mechanics/Combat.md) ; un drain qui ne trouve aucun bouclier n’en est pas un. Il réveille aussi un Seeker ou un Goombah, qui ne font que riposter, comme n’importe quel autre coup.
- Les **coups critiques** comptent : une salve critique draine 1,5 fois plus, et son nombre s’affiche comme un coup critique. Ses paquets sont plus gros et plus brillants, et le bouclier de la cible s’illumine plus fort.
- Les [pilotes de corporation](/wiki/03-Mechanics/Company-Pilots.md) tirent des munitions standard x1.
