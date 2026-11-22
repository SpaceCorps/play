<!-- wiki-i18n source: 6fe66f282236a0de -->
<!-- wiki-i18n title: Portes solo -->
# Portes solo {#solo-gates}

<!-- wiki-search: solo gates; solo gate; gate; gates; galaxy gates; rift; rifts; alpha rift; beta breach; gamma foundry; delta siege; omega vault; chrono gate; chrono-gate; materializer; energy materializer; scan; spin; gate part; gate parts; guarantee; pity; consolation; wave; waves; nuke wave; skip; boss; lives; resume; abandon; speedrun; no death; challenge; achievement; thulium cap; davidski's nightmare; nightmare; evil davidski; angry davidski; evil ships; golden ships; portes solo; porte solo; portes galactiques; pièce; pièces; matérialiseur d’énergie; tirage; garantie; vague; vagues; vies; reprendre; abandonner; sans mourir; défi; succès; plafond de thulium; vaisseaux evil; vaisseaux dorés; davidski furieux -->

Les **portes solo** sont cinq portes des Portes galactiques que vous pilotez seul : **Alpha Rift**, **Beta Breach**, **Gamma Foundry**, **Delta Siege** et **Omega Vault**. Chacune est une arène vide à elle seule où des vagues d’aliens vous attaquent l’une après l’autre et où un boss attend à la fin. **Davidski's Nightmare** est une sixième porte, à part de ces cinq : ses vagues ne sont pas des aliens mais des **vaisseaux Evil**, des vaisseaux du jeu qui volent contre vous, et c’est la porte la plus chère à construire. Vous construisez une porte avec ses **pièces**, que vous trouvez en lançant le Matérialiseur d’énergie avec du Thulium, et une victoire paie des Credits, du Thulium, de l’expérience, de l’honneur, du minerai, des plaques et des munitions.

Une porte solo n’est pas un [donjon de clan](/wiki/03-Mechanics/Dungeons.md). Un donjon est un labyrinthe qu’un clan ouvre pour un groupe, avec un Seigneur de guerre au bout ; une porte solo est une arène où vous seul êtes, et personne d’autre ne peut y entrer avec vous. Les deux ont des règles, des paiements et des limites séparés. La page des Portes galactiques a aussi le **Chrono-Gate**, qui n’est pas un lieu où voler mais la porte qui ouvre votre [Cache de transport](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) pour la réinitialisation : ses pièces se trouvent avec les mêmes tirages.

## En un coup d’œil {#at-a-glance}

<!-- solo-glance:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Portes** : 7 : le Chrono-Gate et 6 portes solo, Alpha Rift, Beta Breach, Gamma Foundry, Delta Siege, Omega Vault et Davidski's Nightmare
- **Tirage** : 100 Thulium par tirage, et 1, 5, 10, 100 ou 1 000 tirages à la fois
- **Chance d’une pièce** : 13 % par tirage, dans la catégorie que vous scannez. La pièce appartient à l’une des portes de cette catégorie, toutes aussi probables : le Chrono-Gate seul prend tout, Alpha Rift, Beta Breach et Gamma Foundry prennent 4,33 % chacune, et Delta Siege et Omega Vault prennent 6,5 % chacune. Quand le Chrono-Gate est complet, il n’y a plus rien à scanner dans sa catégorie
- **Garantie** : Après 24 tirages de suite sans pièce, la chance monte à chaque tirage, et après 47 le tirage suivant en trouve toujours une. Une pièce de n’importe quelle porte repart le compte
- **Vies** : 3 par tentative ; chaque mort en coûte une
- **Compte à rebours** : 5 s avant chaque vague, la première et celle du boss aussi. Une vague n’a pas de minuteur, ni une partie
- **Arène** : Un espace ouvert de 8 000 × 6 000 unités sans rochers, où vous êtes seul. Un monde en a 16, et quand toutes sont occupées vous ne pouvez pas entrer
- **Aliens à la fois** : Au plus 60 d’une vague sont en vie à la fois, et 250 dans une vague facultative. Les autres attendent de la place
- **Boss** : Un boss ne peut pas être blessé pendant 3 s quand il change de phase
- **Plafond de Thulium** : Une porte ne rend pas plus de 50 % du Thulium que vous avez dépensé en tirages. Le reste est rogné, et le résultat dit combien

<!-- solo-glance:end -->

## Trouver des pièces de porte {#finding-gate-parts}

Ouvrez la page des **Portes galactiques** et lancez le Matérialiseur d’énergie. Chaque tirage se paie en Thulium et trouve au plus une pièce. Choisissez d’abord une **catégorie** : le **Chrono-Gate**, **Alpha–Gamma** (Alpha Rift, Beta Breach et Gamma Foundry), **Delta–Omega** (Delta Siege et Omega Vault) ou **Davidski's Nightmare**, qui a une catégorie à elle seule. La chance d’une pièce est la même dans toutes les catégories, et la pièce appartient à l’une des portes de la catégorie choisie, toutes aussi probables. Il vous faut un certain nombre de pièces d’une porte pour la construire, et les pièces sont à vous jusqu’à ce que vous les utilisiez. Un tirage qui ne trouve aucune pièce n’est pas perdu : il paie un lot ([plus bas](#a-spin-without-a-part)). Chaque tirage est facturé. Quand le Chrono-Gate est complet, son entrée est fermée, car il n’y a plus rien à y trouver, et les deux autres catégories gardent leur chance : une pièce d’une porte solo coûte donc pareil avec ou sans lui.

Le tableau donne le coût de chaque porte en pièces et ce qu’elles coûtent en moyenne **avec la garantie** quand vous scannez la catégorie où se trouve la porte (un tirage est une loterie : un pilote chanceux paie moins et un malchanceux plus, jusqu’à la plus longue série de tirages que la garantie permet).

<!-- solo-parts:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Porte | Pièces pour la compléter | Chance d’une pièce par tirage | Tirages en moyenne | Thulium en moyenne |
| :--- | ---: | ---: | ---: | ---: |
| **Chrono-Gate** | 13 | 13 % | 99 | 9 851 |
| **Alpha Rift** | 14 | 4,33 % | 318 | 31 825 |
| **Beta Breach** | 33 | 4,33 % | 750 | 75 016 |
| **Gamma Foundry** | 68 | 4,33 % | 1 546 | 154 579 |
| **Delta Siege** | 96 | 6,5 % | 1 455 | 145 486 |
| **Omega Vault** | 119 | 6,5 % | 1 803 | 180 343 |
| **Davidski's Nightmare** | 238 | 13 % | 1 803 | 180 343 |

<!-- solo-parts:end -->

Les pièces du Chrono-Gate retombent à zéro à la réinitialisation, et vous les retrouvez à chaque saison. **Les pièces des portes solo restent**, de même que le compteur de la garantie et le relevé de ce que vous avez dépensé en tirages et de ce que les portes ont rendu ; la réinitialisation n’en prend aucun ([Les portes et la réinitialisation](#gates-and-the-wipe)).

### Un tirage sans pièce {#a-spin-without-a-part}

La plupart des tirages ne trouvent aucune pièce. Chacun d’eux paie un lot, tiré selon les chances ci-dessous : des munitions laser du deuxième multiplicateur ou mieux, un lot de roquettes du deuxième ou du troisième niveau et, de temps en temps, un [objet spécial](/wiki/06-Items/Special-Items.md) ou un [conteneur](/wiki/06-Items/Containers.md). Un lot qui ne peut pas être donné (les objets spéciaux ou les conteneurs sont désactivés, par exemple) devient un lot de munitions ou de roquettes par le même tirage, si bien qu’un tirage ne paie jamais moins que son tableau. Le lot vaut nettement moins que ce que coûte le tirage : les portes sont un puits à Thulium.

<!-- solo-prizes:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Récompense | Chance par tirage |
| :--- | ---: |
| Un conteneur : Chroma Archive | 0,01 % |
| Un objet spécial : Magic Hammer | 0,2 % |
| Un objet spécial : Schematics | 0,2 % |
| Un objet spécial : Philosopher's Stone | 0,2 % |
| Un objet spécial : Forger's Seal | 0,2 % |
| Un objet spécial : Workforce Contract | 0,2 % |
| Un objet spécial : Tinkerer's Badge | 0,1 % |
| Munitions laser : Advanced Plasma ×75 | 12,88 % |
| Munitions laser : Antimatter Battery I ×62 | 8,59 % |
| Munitions laser : Ultra Core ×40 | 8,59 % |
| Munitions laser : Antimatter Battery II ×29 | 4,29 % |
| Munitions laser : Dark Matter Ammo I ×31 | 4,29 % |
| Munitions laser : Experimental Fusion Core ×17 | 2,15 % |
| Munitions laser : Dark Matter Ammo II ×17 | 2,15 % |
| Roquettes : Lancet II ×4 | 8,59 % |
| Roquettes : Rivet II ×4 | 8,59 % |
| Roquettes : Ember II ×4 | 8,59 % |
| Roquettes : Scatter II ×4 | 8,59 % |
| Roquettes : Lancet III ×1 | 2,15 % |
| Roquettes : Rivet III ×1 | 2,15 % |
| Roquettes : Ember III ×1 | 2,15 % |
| Roquettes : Scatter III ×1 | 2,15 % |

<!-- solo-prizes:end -->

## Y entrer {#going-in}

Vous **construisez** une porte sur la page des Portes galactiques et vous y **sautez** par son portail. On construit depuis la station, vaisseau amarré, et aussi en vol : la **fenêtre des Portes galactiques**, qu’ouvre le bouton des portes de la barre d’outils, lance les scans, construit et choisit la destination comme la page. Il faut :

- les pièces de la porte : elles sont prises **une seule fois, à la construction**, et une construction refusée ne prend rien ;
- la porte elle-même pas encore construite : vous pouvez avoir **toutes** les portes construites à la fois, avec un portail pour chacune, et vous n’en jouez qu’une à la fois ; une porte déjà construite est reprise par son portail ou abandonnée avant que vous la construisiez de nouveau ;
- le serveur principal (une porte ne se construit que sur le serveur principal : sur un serveur régional, vous retournez d’abord à la base).

La porte construite se dresse dans votre **secteur d’origine** (`M-1`, `T-1` ou `G-1`, selon votre corporation) sous la forme d’un portail qui porte son nom, et la page des Portes galactiques dit où elle se trouve. **Décollez, volez jusqu’au portail et sautez** comme par n’importe quel portail. Une faille doit être libre dans votre monde quand vous entrez : chaque monde en a un certain nombre, et quand toutes sont occupées, vous attendez. Vous ne voyez que **vos propres** portes : les portails des portes d’autres pilotes dans le même secteur ne vous sont pas montrés. Vous pouvez avoir **les cinq portes construites en même temps**, chacune avec son propre portail, et vous en jouez une à la fois : **tant que vous êtes dans une arène, aucun de vos portails ne se dresse**, et ils reviennent quand vous en sortez.

**Sur les serveurs régionaux (Singapore, US East).** Une porte construite s’y joue aussi. Son portail se dresse dans votre secteur d’origine sur un serveur régional comme sur le serveur principal, et on vous le dit à votre arrivée. **Sautez par ce portail et vous entrez dans une arène de ce serveur**, avec sa latence plutôt que celle du serveur principal. Un serveur régional n’a que **deux arènes par monde**, contre bien plus sur le serveur principal : quand les deux sont occupées, vous attendez, comme vous attendez une faille libre sur le serveur principal. Le serveur principal reste le seul endroit qui garde votre partie, vos pièces et votre paiement : le paiement arrive dans votre portefeuille quand le serveur principal a compté la partie, quelques secondes après sa fin, et le **portefeuille de votre fenêtre de vol se met à jour quand vous vous amarrez**. Vous n’entrez dans votre partie suivante qu’une fois la dernière comptée. Une partie que vous quittez dans l’arène se reprend par le portail ; pour l’abandonner, vous le faites dans l’arène ou à la station. Si l’arène d’un serveur régional est désactivée, son portail vous ramène au serveur principal, où vous décollez vers votre porte comme ci-dessus. Ce qui fonctionne d’autre sur un serveur régional est décrit dans [Serveurs](/wiki/03-Mechanics/Servers.md).

Vous atterrissez seul au milieu d’une arène vide. Personne ne peut vous y attaquer, et la Jump CPU et la Base CPU ne fonctionnent pas.

## Le déroulement d’une partie {#how-a-run-goes}

1. **Un compte à rebours précède chaque vague**, la première et celle du boss aussi. Une vague n’a pas de minuteur, ni la partie : elle dure le temps qu’il vous faut.
2. **Une vague** apparaît sur un anneau autour de vous et vous fonce dessus, au rythme de la porte. Seule une partie d’entre elle est en vie à la fois, et les autres attendent de la place. Elle se termine quand son dernier alien est mort.
3. **Votre progression est sauvegardée après chaque vague.** Si vous partez, une vague en cours recommence en entier à votre retour.
4. **Une vague facultative** est une énorme vague de Seeker, et Delta Siege et Omega Vault en ont une chacune. Pendant son compte à rebours, vous pouvez la passer : elle compte alors comme faite et ne paie **rien**. Si vous la combattez, ses éliminations paient comme celles de n’importe quelle vague.
5. **La dernière vague est le boss.** Il change de phase à mesure que sa coque tombe, et il ne peut pas être blessé un instant à chaque changement. Quand le boss meurt, la partie est gagnée, et la victoire est payée aussitôt.

**Vies.** Une mort coûte une vie et vous renvoie à votre base comme toute autre mort ; la partie vous attend, sans horloge qui tourne. Tant que la partie est ouverte et que vous êtes hors de l’arène, **le portail de chaque porte que vous avez construite se dresse dans votre secteur d’origine**, et un saut par l’un d’eux vous ramène à la vague sauvegardée avec les vies qu’il vous reste, comme **Reprendre** ; il ne demande aucune nouvelle pièce. Quand votre dernière vie est perdue, la tentative se termine mais la partie reste ouverte à la dernière vague franchie, et y retourner vous rend vos vies. **Quitter**, une déconnexion ou un changement de monde met la partie en pause sans coûter de vie. Un redémarrage du serveur garde aussi votre partie ouverte. **Abandonner** renonce à la partie : ses pièces sont perdues, et les aliens que vous avez tués sont payés tels quels. **Reprendre** ne marche que depuis un vaisseau en vol : après une mort, son bouton sur l’écran de résultat attend, avec une ligne qui dit pourquoi, que vous ayez réapparu. Un vaisseau qui réapparaît revient avec une coque plafonnée ; quand votre coque est sous la moitié, l’écran de résultat vous prévient, et **Reprendre** vous remet quand même en jeu tel que vous êtes. Les vaisseaux de réparation de votre base vous réparent dans leur aura.

Chaque monde affronte la même porte : la force et le paiement des aliens ne dépendent pas du monde où vous volez.

### Les vagues {#the-waves}

Les aliens sont ceux du jeu (Seeker, Phantasm, Bulwark, Goombah et Crystalys), rendus plus durs ou plus tendres par la porte. Les vagues de **Davidski's Nightmare** sont des **vaisseaux Evil** à la place : un pour chaque coque qu’un pilote peut piloter, aux couleurs de l’Essaim Dormant. Les petites coques viennent en premier, et chaque vague en apporte davantage et de plus grosses, jusqu’à la dernière vague avant le boss. Un vaisseau Evil porte ce que porte le vaisseau d’un pilote : des lasers, une **roquette** qu’il vous tire dessus toutes les quelques secondes, et un **drone de réparation** qui répare sa coque tant que rien ne le touche ; un vaisseau que vous laissez tranquille se soigne donc. Le temps prévu est ce que la porte est conçue pour prendre à un pilote au niveau de départ de la Technique laser ([Aptitudes de pilote](/wiki/03-Mechanics/Pilot-Skills.md)) ; un pilote qui a fait monter sa Technique laser finit plus tôt.

Certaines vagues amènent un **essaim** : un boss PNJ du jeu (un Boss Seeker, Boss Phantasm, Boss Goombah ou Boss Crystalys) avec ses gardes, qui attaquent en un seul groupe. Chaque vaisseau d’un essaim fait partie de sa vague, et la vague se termine quand le dernier d’entre eux est mort. Ils paient comme les autres vaisseaux de la vague, aux chiffres de [la table des aliens](#the-aliens). **Un boss PNJ laisse son butin comme dans les secteurs du jeu** : minerai, plaques, munitions et roquettes (ce que chacun laisse figure sur [les pages des essaims](/wiki/05-Swarms/Swarms.md)). Dans une porte, il n’y a pas de caisse à ramasser : le butin arrive avec le paiement, directement dans votre inventaire, et une seule fois par partie, comme le paiement. Ses gardes ne laissent rien, dans la porte comme dans les secteurs, et ils ne soignent pas leur boss et ne reviennent pas. La table ci-dessous dit quelles vagues de chaque porte amènent un essaim.

<!-- solo-waves:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Porte | Vagues, celle du boss comprise | Aliens dans les vagues | Boss PNJ et essaims | Boss | Temps prévu |
| :--- | ---: | :--- | :--- | :--- | :--- |
| **Alpha Rift** | 10 | 44 Seeker, 140 Phantasm | vague 5 : 1 Seeker Swarm, 1 Phantasm Swarm | Enhanced Phantasm | 10 à 15 min |
| **Beta Breach** | 14 | 64 Seeker, 158 Phantasm, 80 Bulwark, 20 Goombah | vague 4 : 2 Seeker Swarm; vague 9 : 1 Phantasm Swarm | Enhanced Bulwark | 15 à 25 min |
| **Gamma Foundry** | 18 | 78 Phantasm, 117 Bulwark, 91 Goombah, 8 Crystalys | vague 4 : 1 Phantasm Swarm; vague 9 : 1 Goombah Swarm; vague 14 : 1 Goombah Swarm | Elite Crystalys | 25 à 35 min |
| **Delta Siege** | 22 | 250 Seeker, 200 Phantasm, 141 Bulwark, 130 Goombah, 12 Crystalys | vague 5 : 2 Phantasm Swarm; vague 10 : 2 Goombah Swarm; vague 15 : 1 Goombah Swarm; vague 20 : 1 Crystalys Swarm | Siege Construct | 35 à 45 min |
| **Omega Vault** | 26 | 250 Seeker, 236 Phantasm, 170 Bulwark, 174 Goombah, 25 Crystalys | vague 6 : 1 Goombah Swarm; vague 11 : 2 Goombah Swarm; vague 16 : 1 Crystalys Swarm; vague 22 : 1 Phantasm Swarm | Omega Guardian | 50 à 60 min |
| **Davidski's Nightmare** | 13 | 50 Evil Protos, 66 Evil Kitefin, 31 Evil Ostirion, 19 Evil Nomad, 22 Evil Paragon, 7 Evil Storm, 8 Evil Wraith, 2 Evil Ironclad |  | Evil Davidski | 45 à 60 min |

- **Delta Siege** : la vague 18 (250 Seeker) est facultative : vous pouvez la passer pendant son compte à rebours, et elle ne paie rien
- **Omega Vault** : la vague 17 (250 Seeker) est facultative : vous pouvez la passer pendant son compte à rebours, et elle ne paie rien; les vagues 22 à 24 sont d’élite, avec ×1,5 de coque, de bouclier et de dégâts

<!-- solo-waves:end -->

### Les boss {#the-bosses}

Un boss est le vaisseau d’un alien agrandi, avec une coque, un bouclier et une salve à lui, qu’aucun réglage de la porte ni du monde ne change. Une phase commence quand la coque du boss tombe au chiffre du tableau : son bouclier peut être refixé, sa salve ou tous ses dégâts changent, et il peut lancer une attaque. Chaque attaque est annoncée : un cercle, un anneau ou une marque sur votre vaisseau la montre un instant avant qu’elle ne frappe. Les aliens qu’un boss appelle ne paient ni ne lâchent rien.

**Evil Davidski**, le boss de Davidski's Nightmare, pilote l’Ironclad de Davidski lui-même, dans un or plus sombre. Il tire des Dormant Lance, des roquettes guidées qui vous suivent sur une longue distance, et se bat avec des météores, un anneau et des vaisseaux Evil qu’il appelle. À mi-coque, il devient **DAVIDSKI FURIEUX** : son thème se joue, il frappe plus fort, et un **vaisseau doré de chaque vaisseau du jeu** apparaît autour de lui. Tant qu’un des vaisseaux dorés est en vie, il est invulnérable : vos lasers et vos roquettes ne peuvent pas le verrouiller et rien de ce que vous faites n’atteint sa coque ni son bouclier, donc vous vous frayez d’abord un chemin à travers eux. Quand le dernier tombe, la protection disparaît pour de bon. Il se moque de vous depuis sa propre fenêtre au début de chaque vague. Le tuer compte comme une élimination de Davidski pour les missions qui en demandent une, dans une porte comme dans les secteurs dangereux. Un jeu qui n’est pas à jour n’affiche pas la porte.

<!-- solo-bosses:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Boss | Porte | Coque | Bouclier | Salve laser |
| :--- | :--- | ---: | ---: | ---: |
| **Enhanced Phantasm** | Alpha Rift | 330 000 | 530 000 | 5 700–7 000 |
| **Enhanced Bulwark** | Beta Breach | 690 000 | 170 000 | 4 500–5 500 |
| **Elite Crystalys** | Gamma Foundry | 620 000 | 250 000 | 3 800–4 700 |
| **Siege Construct** | Delta Siege | 1 150 000 | 1 730 000 | 3 400–4 200 |
| **Omega Guardian** | Omega Vault | 1 340 000 | 840 000 | 2 600–3 200 |
| **Evil Davidski** | Davidski's Nightmare | 5 500 000 | 6 600 000 | 7 800–9 600 |

| Boss | Phase | Coque restante | Ce qu’il fait |
| :--- | :--- | :--- | :--- |
| **Enhanced Phantasm** | Enhanced Phantasm | 100 % à 0 % | Il ne fait que tirer. |
| **Enhanced Bulwark** | Shielded | 100 % à 50 % | Son bouclier est fixé à ×4 de celui du boss. |
|  | Second attack | 50 % à 0 % | Sa salve est ×1,3. Il vous tire 4 roquettes Dormant Lance, de 61 000 chacune, une toutes les 0,5 s, en une rafale toutes les 30 s. |
| **Elite Crystalys** | Elite | 100 % à 50 % | Il ne fait que tirer. |
|  | Reinforced | 50 % à 0 % | Son bouclier est fixé à ×2 de celui du boss. Toutes les 10 min, il appelle 10 Goombah, au plus 10 en vie ; ils ne paient ni ne lâchent rien. |
| **Siege Construct** | Siege Construct | 100 % à 0 % | Toutes les 1 min, il fait tomber 3 salves de 8 météores, de 5 500 chacun sur tout ce qui se trouve à moins de 420 unités de leur point de chute, 50 % d’entre eux visés sur vous ; chaque cercle s’affiche 3 s avant la chute. Il vous tire 6 roquettes Dormant Lance, de 9 000 chacune, une toutes les 0,5 s, en une rafale toutes les 1 min. |
| **Omega Guardian** | Shield Fortress | 100 % à 70 % | Son bouclier est fixé à ×1,5 de celui du boss. Toutes les 40 s, il appelle 6 Bulwark, au plus 12 en vie ; ils ne paient ni ne lâchent rien. |
|  | Swarm Protocol | 70 % à 35 % | Toutes les 25 s, il appelle 12 Phantasm, au plus 24 en vie ; ils ne paient ni ne lâchent rien. Toutes les 30 s, une explosion de 140 000 touche tout ce qui se trouve à moins de 700 unités du boss ; l’anneau s’affiche 2 s avant la chute. |
|  | Overload | 35 % à 0 % | Son bouclier est fixé à ×0,1 de celui du boss. Tous ses dégâts sont ×2,5. Après 2 min dans la phase, tous ses dégâts sont encore ×2. Toutes les 25 s, une explosion de 28 000 touche tout ce qui se trouve à moins de 700 unités du boss ; l’anneau s’affiche 2 s avant la chute. |
| **Evil Davidski** | Evil Davidski | 100 % à 50 % | Il vous tire 6 roquettes Dormant Lance, de 14 700 chacune, une toutes les 0,5 s, en une rafale toutes les 30 s. Toutes les 1 min, il fait tomber 2 salves de 8 météores, de 33 000 chacun sur tout ce qui se trouve à moins de 400 unités de leur point de chute, 50 % d’entre eux visés sur vous ; chaque cercle s’affiche 3 s avant la chute. Toutes les 40 s, il appelle 5 Evil Protos, au plus 10 en vie ; ils ne paient ni ne lâchent rien. |
|  | Angry | 50 % à 0 % | Son bouclier est fixé à ×0,5 de celui du boss. Tous ses dégâts sont ×1,5. Après 8 min dans la phase, tous ses dégâts sont encore ×2. Il vous tire 6 roquettes Dormant Lance, de 7 800 chacune, une toutes les 0,4 s, en une rafale toutes les 30 s. Toutes les 1 min, il fait tomber 3 salves de 8 météores, de 10 200 chacun sur tout ce qui se trouve à moins de 420 unités de leur point de chute, 50 % d’entre eux visés sur vous ; chaque cercle s’affiche 3 s avant la chute. Toutes les 45 s, une explosion de 105 000 touche tout ce qui se trouve à moins de 700 unités du boss ; l’anneau s’affiche 2 s avant la chute. Toutes les 40 s, il appelle 3 Evil Kitefin, au plus 6 en vie ; ils ne paient ni ne lâchent rien. |

<!-- solo-bosses:end -->

## Ce que paie une victoire {#what-a-clear-pays}

Une victoire paie son tableau **une fois**, d’un coup, à l’instant où le boss meurt : les Credits, le Thulium, l’expérience et l’honneur, le minerai, les plaques et les Power Cores, et les munitions. L’expérience et l’honneur comptent pour vos points PvE, comme ceux d’un donjon.

<!-- solo-pay:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Porte | Crédits | Thulium | XP | Honneur |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 450 000 | 5 000 | 70 000 | 1 000 |
| **Beta Breach** | 1 500 000 | 12 000 | 180 000 | 2 500 |
| **Gamma Foundry** | 4 000 000 | 25 000 | 400 000 | 5 500 |
| **Delta Siege** | 8 000 000 | 40 000 | 800 000 | 10 000 |
| **Omega Vault** | 15 000 000 | 60 000 | 1 500 000 | 20 000 |
| **Davidski's Nightmare** | 15 000 000 | 60 000 | 1 500 000 | 20 000 |

- **Alpha Rift** : Ship Fragment ×300, Nyxite ×300, Daraxium ×400, Echo Shard ×4, Lattice Shard ×6 ; munitions : Advanced Plasma ×15 000, Ultra Core ×3 750, Experimental Fusion Core ×15 000
- **Beta Breach** : Ship Fragment ×700, Nyxite ×750, Daraxium ×800, Cataclysite ×400, Quorvium ×100, Echo Shard ×9, Lattice Shard ×13 ; munitions : Advanced Plasma ×37 500, Ultra Core ×15 000, Experimental Fusion Core ×22 500
- **Gamma Foundry** : Ship Fragment ×1 150, Nyxite ×1 000, Cataclysite ×900, Quorvium ×400, Power Core ×15, Echo Shard ×18, Lattice Shard ×27 ; munitions : Advanced Plasma ×22 500, Ultra Core ×45 000, Experimental Fusion Core ×37 500
- **Delta Siege** : Ship Fragment ×2 000, Nyxite ×1 750, Cataclysite ×1 500, Quorvium ×1 000, Reinforced Hull Plate ×70, Power Core ×40, Ancient Control Unit ×3, Echo Shard ×29, Lattice Shard ×44 ; munitions : Advanced Plasma ×30 000, Ultra Core ×67 500, Experimental Fusion Core ×56 250
- **Omega Vault** : Ship Fragment ×3 250, Nyxite ×2 750, Cataclysite ×2 250, Quorvium ×1 600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10, Echo Shard ×34, Lattice Shard ×54 ; munitions : Advanced Plasma ×37 500, Ultra Core ×75 000, Experimental Fusion Core ×75 000
- **Davidski's Nightmare** : Ship Fragment ×3 250, Nyxite ×2 750, Cataclysite ×2 250, Quorvium ×1 600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10, Echo Shard ×34, Lattice Shard ×54 ; munitions : Advanced Plasma ×37 500, Ultra Core ×75 000, Experimental Fusion Core ×75 000
- **Heartshards** : 1 à la première réussite de chaque porte d’une saison, et 5 % de chances d’en obtenir 1 de plus à chaque réussite.

<!-- solo-pay:end -->

**Le Thulium est rogné à un plafond.** Les portes ne peuvent pas rendre plus d’une part du Thulium que vous avez dépensé en tirages, comptée sur toutes vos portes et tous vos tirages (la part est dans la liste du haut). Ce qu’une victoire et ses aliens paieraient au-delà est rogné, et l’écran de résultat dit combien. Les Credits, l’expérience, l’honneur, le minerai, les plaques et les munitions ne sont jamais rognés.

### Les aliens {#the-aliens}

Chaque alien que vous tuez dans une porte paie aux chiffres qu’il a dans Alpha, quel que soit le monde où vous volez : aucun multiplicateur de monde, aucun booster et aucun bonus Premium ne les change. Une vague paie ses aliens **une fois** par partie, autant de fois que vous partiez et reveniez. Le paiement arrive à la fin de chaque tronçon de la partie : quand vous partez, mourez, n’avez plus de vies, abandonnez ou gagnez. Les éliminations d’un tronçon ne restent impayées que lors de la réinitialisation et lors d’un redémarrage du serveur pendant que vous êtes dedans (votre partie reste ouverte, mais les éliminations de ce tronçon sont perdues). Les éliminations d’une porte comptent pour les [missions](/wiki/03-Mechanics/Quests.md#where-it-counts) qui ne nomment aucun secteur (comme les grandes chasses de la ligne des Défis), au moment où elles ont lieu (une vague compte pour elles **une fois** par partie, comme elle ne paie qu’une fois), et pour rien d’autre : ni pour les statistiques d’éliminations, ni pour les compteurs des succès, ni pour le fil des éliminations, ni pour l’expérience de vos drones et P.E.T.s. L’expérience et l’honneur qu’elles paient comptent en revanche pour vos points PvE, comme ceux d’une victoire. Le butin des aliens arrive avec le paiement, directement dans votre inventaire.

<!-- solo-kills:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Alien | Crédits | Thulium | XP | Honneur |
| :--- | ---: | ---: | ---: | ---: |
| **Seeker** | 1 000 | 4 | 100 | 2 |
| **Phantasm** | 3 000 | 12 | 300 | 6 |
| **Bulwark** | 5 000 | 25 | 800 | 10 |
| **Goombah** | 15 000 | 75 | 3 000 | 24 |
| **Crystalys** | 75 000 | 200 | 12 000 | 52 |
| **Boss Seeker** | 10 000 | 40 | 1 000 | 20 |
| **Seeker Slave** | 125 | 1 | 12 | 1 |
| **Boss Phantasm** | 39 000 | 195 | 7 800 | 62 |
| **Phantasm Guard** | 125 | 1 | 12 | 1 |
| **Boss Goombah** | 120 000 | 600 | 24 000 | 192 |
| **Goombah Guard** | 125 | 1 | 12 | 1 |
| **Boss Crystalys** | 393 750 | 1 050 | 63 000 | 273 |
| **Crystalys Guard** | 125 | 1 | 12 | 1 |
| **Evil Protos** | 4 250 | 17 | 725 | 6 |
| **Evil Kitefin** | 12 850 | 53 | 2 175 | 18 |
| **Evil Ostirion** | 34 350 | 141 | 5 800 | 48 |
| **Evil Nomad** | 59 600 | 245 | 10 060 | 84 |
| **Evil Paragon** | 68 700 | 283 | 11 600 | 97 |
| **Evil Storm** | 96 600 | 398 | 16 315 | 136 |
| **Evil Wraith** | 137 450 | 566 | 23 205 | 194 |
| **Evil Ironclad** | 268 450 | 1 105 | 45 330 | 379 |

| Porte | Crédits | Thulium | XP | Honneur |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 514 000 | 2 099 | 55 296 | 1 018 |
| **Beta Breach** | 1 298 500 | 5 939 | 187 744 | 2 470 |
| **Gamma Foundry** | 3 064 500 | 13 693 | 541 944 | 4 696 |
| **Delta Siege** | 5 239 625 | 22 338 | 882 676 | 7 850 |
| **Omega Vault** | 7 088 125 | 29 196 | 1 196 828 | 10 022 |
| **Davidski's Nightmare** | 7 081 950 | 29 124 | 1 196 445 | 9 968 |

<!-- solo-kills:end -->

## Défis et succès {#challenges-and-achievements}

Deux défis facultatifs peuvent être gagnés à chaque victoire, et ils paient chacun un succès et **aucun Thulium**. Une victoire **sans mort** est une victoire sans aucune mort dans toute la partie, sur toutes les fois où vous êtes entré. Un **speedrun** est une victoire dans le plus court temps prévu de la porte, compté par le temps que vous passez dans l’arène. Les six autres succès sont pour avoir vaincu chaque porte, et les cinq :

<!-- solo-achievements:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Faille refermée** (Commun) : Terminez seul l’Alpha Rift.
- **Brèche scellée** (Peu commun) : Terminez seul le Beta Breach.
- **Fonderie arrêtée** (Rare) : Terminez seul la Gamma Foundry.
- **Siège brisé** (Rare) : Brisez seul le Delta Siege.
- **Coffre-fort forcé** (Épique) : Forcez seul l’Omega Vault.
- **Gardien des portes** (Légendaire) : Terminez les cinq portes solo : Alpha, Beta, Gamma, Delta et Omega.
- **Intouchable** (Rare) : Terminez une porte solo sans perdre une vie.
- **Contre la montre** (Rare) : Terminez une porte solo dans son temps le plus court ou moins : 10, 15, 25, 35 ou 50 minutes, de l’Alpha à l’Omega.

<!-- solo-achievements:end -->

## Objets d’une porte {#items-from-a-gate}

Ce qu’une porte vous donne est **commercialisable** : le minerai, les plaques, les Power Cores, les munitions et le butin des aliens peuvent être mis en vente aux [Enchères](/wiki/03-Mechanics/Auction.md) comme un butin ou une récompense de quête, avec les mêmes exceptions que pour tout objet. Les lots d’un tirage sans pièce ne le sont pas : ils viennent d’un tirage, pas d’une porte.

## Les portes et la réinitialisation {#gates-and-the-wipe}

- **La réinitialisation met fin à toute partie ouverte** et vous rend ses pièces. Une partie ne se poursuit pas dans la saison suivante.
- **Conservé à travers la réinitialisation :** les pièces des cinq portes solo, le compteur de la garantie et le relevé de ce que vous avez dépensé en tirages et de ce que les portes ont rendu, si bien que le plafond du Thulium continue d’une saison à l’autre. Les succès sont à vous pour toujours.
- **Perdu à la réinitialisation :** les pièces du Chrono-Gate, comme avant. Vos tirages les rachètent.
- **Supprimer un compte** supprime les pièces, le compteur et le relevé.
