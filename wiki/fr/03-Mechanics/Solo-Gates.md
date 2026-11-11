<!-- wiki-i18n source: 4d2749864875137f -->
<!-- wiki-i18n title: Portes solo -->
# Portes solo {#solo-gates}

<!-- wiki-search: solo gates; solo gate; gate; gates; galaxy gates; rift; rifts; alpha rift; beta breach; gamma foundry; delta siege; omega vault; chrono gate; chrono-gate; materializer; energy materializer; scan; spin; gate part; gate parts; guarantee; pity; consolation; wave; waves; nuke wave; skip; boss; lives; resume; abandon; speedrun; no death; challenge; achievement; thulium cap; portes solo; porte solo; portes galactiques; pièce; pièces; matérialiseur d’énergie; tirage; garantie; vague; vagues; vies; reprendre; abandonner; sans mourir; défi; succès; plafond de thulium -->

Les **portes solo** sont cinq portes des Portes galactiques que vous pilotez seul : **Alpha Rift**, **Beta Breach**, **Gamma Foundry**, **Delta Siege** et **Omega Vault**. Chacune est une arène vide à elle seule où des vagues d’aliens vous attaquent l’une après l’autre et où un boss attend à la fin. Vous construisez une porte avec ses **pièces**, que vous trouvez en lançant le Matérialiseur d’énergie avec du Thulium, et une victoire paie des Credits, du Thulium, de l’expérience, de l’honneur, du minerai, des plaques et des munitions.

Une porte solo n’est pas un [donjon de clan](/wiki/03-Mechanics/Dungeons.md). Un donjon est un labyrinthe qu’un clan ouvre pour un groupe, avec un Seigneur de guerre au bout ; une porte solo est une arène où vous seul êtes, et personne d’autre ne peut y entrer avec vous. Les deux ont des règles, des paiements et des limites séparés. La page des Portes galactiques a aussi le **Chrono-Gate**, qui n’est pas un lieu où voler mais la porte qui ouvre votre [Cache de transport](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) pour la réinitialisation : ses pièces se trouvent avec les mêmes tirages.

## En un coup d’œil {#at-a-glance}

<!-- solo-glance:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Portes** : 6 : le Chrono-Gate et 5 portes solo, Alpha Rift, Beta Breach, Gamma Foundry, Delta Siege et Omega Vault
- **Tirage** : 100 Thulium par tirage, et 1, 5, 10 ou 100 tirages à la fois
- **Chance d’une pièce** : 13 % par tirage. La porte dont la pièce fait partie est tirée au hasard, et chaque porte reçoit 2,17 % des tirages. Quand le Chrono-Gate est complet, sa part sort de la roue, et les portes solo gardent 2,17 % chacune
- **Garantie** : Après 24 tirages de suite sans pièce, la chance monte à chaque tirage, et après 47 le tirage suivant en trouve toujours une. Une pièce de n’importe quelle porte repart le compte
- **Vies** : 3 par tentative ; chaque mort en coûte une
- **Compte à rebours** : 5 s avant chaque vague, la première et celle du boss aussi. Une vague n’a pas de minuteur, ni une partie
- **Arène** : Un espace ouvert de 8 000 × 6 000 unités sans rochers, où vous êtes seul. Un monde en a 16, et quand toutes sont occupées vous ne pouvez pas entrer
- **Aliens à la fois** : Au plus 60 d’une vague sont en vie à la fois, et 250 dans une vague facultative. Les autres attendent de la place
- **Boss** : Un boss ne peut pas être blessé pendant 3 s quand il change de phase
- **Plafond de Thulium** : Une porte ne rend pas plus de 50 % du Thulium que vous avez dépensé en tirages. Le reste est rogné, et le résultat dit combien

<!-- solo-glance:end -->

## Trouver des pièces de porte {#finding-gate-parts}

Ouvrez la page des **Portes galactiques** et lancez le Matérialiseur d’énergie. Chaque tirage se paie en Thulium et trouve au plus une pièce, et la pièce appartient à l’une des six portes, tirée au hasard. Il vous faut un certain nombre de pièces d’une porte pour la construire, et les pièces sont à vous jusqu’à ce que vous les utilisiez. Un tirage qui ne trouve aucune pièce n’est pas perdu : il paie un lot ([plus bas](#a-spin-without-a-part)). Chaque tirage est facturé, même avec un Chrono-Gate complet. Quand le Chrono-Gate est complet, sa part des tirages ne trouve rien, et les portes solo gardent leur propre chance : une pièce d’une porte solo coûte donc pareil avec ou sans lui.

Le tableau donne le coût de chaque porte en pièces et ce qu’elles coûtent en moyenne **avec la garantie** (un tirage est une loterie : un pilote chanceux paie moins et un malchanceux plus, jusqu’à la plus longue série de tirages que la garantie permet).

<!-- solo-parts:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Porte | Pièces pour la compléter | Chance d’une pièce par tirage | Tirages en moyenne | Thulium en moyenne |
| :--- | ---: | ---: | ---: | ---: |
| **Chrono-Gate** | 2 | 2,17 % | 91 | 9 093 |
| **Alpha Rift** | 11 | 2,17 % | 500 | 50 011 |
| **Beta Breach** | 26 | 2,17 % | 1 182 | 118 208 |
| **Gamma Foundry** | 54 | 2,17 % | 2 455 | 245 508 |
| **Delta Siege** | 87 | 2,17 % | 3 955 | 395 541 |
| **Omega Vault** | 108 | 2,17 % | 4 910 | 491 017 |

<!-- solo-parts:end -->

Les pièces du Chrono-Gate retombent à zéro à la réinitialisation, et vous les retrouvez à chaque saison. **Les pièces des portes solo restent**, de même que le compteur de la garantie et le relevé de ce que vous avez dépensé en tirages et de ce que les portes ont rendu ; la réinitialisation n’en prend aucun ([Les portes et la réinitialisation](#gates-and-the-wipe)).

### Un tirage sans pièce {#a-spin-without-a-part}

La plupart des tirages ne trouvent aucune pièce. Chacun d’eux paie un lot, tiré selon les chances ci-dessous : des munitions laser du deuxième multiplicateur ou mieux, un lot de roquettes du deuxième ou du troisième niveau et, de temps en temps, un [objet spécial](/wiki/06-Items/Special-Items.md) ou un [conteneur](/wiki/06-Items/Containers.md). Un lot qui ne peut pas être donné (vous avez déjà le maximum de cet objet spécial, par exemple) devient un lot de munitions ou de roquettes par le même tirage, si bien qu’un tirage ne paie jamais moins que son tableau. Le lot vaut nettement moins que ce que coûte le tirage : les portes sont un puits à Thulium.

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

Vous **construisez** une porte sur la page des Portes galactiques et vous y **sautez** par son portail. On construit depuis la station, vaisseau amarré : inutile d’être en vol. Il faut :

- les pièces de la porte : elles sont prises **une seule fois, à la construction**, et une construction refusée ne prend rien ;
- aucune autre partie solo ouverte : vous avez une partie à la fois, et une partie que vous avez quittée est reprise par son portail ou abandonnée avant que vous construisiez une autre porte ;
- le serveur principal (les serveurs régionaux n’ont pas de portes).

La porte construite se dresse dans votre **secteur d’origine** (`M-1`, `T-1` ou `G-1`, selon votre corporation) sous la forme d’un portail qui porte son nom, et la page des Portes galactiques dit où elle se trouve. **Décollez, volez jusqu’au portail et sautez** comme par n’importe quel portail. Une faille doit être libre dans votre monde quand vous entrez : chaque monde en a un certain nombre, et quand toutes sont occupées, vous attendez.

Vous atterrissez seul au milieu d’une arène vide. Personne ne peut vous y attaquer, et la Jump CPU et la Base CPU ne fonctionnent pas.

## Le déroulement d’une partie {#how-a-run-goes}

1. **Un compte à rebours précède chaque vague**, la première et celle du boss aussi. Une vague n’a pas de minuteur, ni la partie : elle dure le temps qu’il vous faut.
2. **Une vague** apparaît sur un anneau autour de vous et vous fonce dessus, au rythme de la porte. Seule une partie d’entre elle est en vie à la fois, et les autres attendent de la place. Elle se termine quand son dernier alien est mort.
3. **Votre progression est sauvegardée après chaque vague.** Si vous partez, une vague en cours recommence en entier à votre retour.
4. **Une vague facultative** est une énorme vague de Seeker, et Delta Siege et Omega Vault en ont une chacune. Pendant son compte à rebours, vous pouvez la passer : elle compte alors comme faite et ne paie **rien**. Si vous la combattez, ses éliminations paient comme celles de n’importe quelle vague.
5. **La dernière vague est le boss.** Il change de phase à mesure que sa coque tombe, et il ne peut pas être blessé un instant à chaque changement. Quand le boss meurt, la partie est gagnée, et la victoire est payée aussitôt.

**Vies.** Une mort coûte une vie et vous renvoie à votre base comme toute autre mort ; la partie vous attend, sans horloge qui tourne. Tant que la partie est ouverte et que vous êtes hors de l’arène, **le portail de votre porte se dresse dans votre secteur d’origine**, et un saut par lui vous ramène à la vague sauvegardée avec les vies qu’il vous reste, comme **Reprendre** ; il ne demande aucune nouvelle pièce. Quand votre dernière vie est perdue, la tentative se termine mais la partie reste ouverte à la dernière vague franchie, et y retourner vous rend vos vies. **Quitter**, une déconnexion ou un changement de monde met la partie en pause sans coûter de vie. Un redémarrage du serveur garde aussi votre partie ouverte. **Abandonner** renonce à la partie : ses pièces sont perdues, et les aliens que vous avez tués sont payés tels quels. **Reprendre** ne marche que depuis un vaisseau en vol : après une mort, son bouton sur l’écran de résultat attend, avec une ligne qui dit pourquoi, que vous ayez réapparu. Un vaisseau qui réapparaît revient avec une coque plafonnée ; quand votre coque est sous la moitié, l’écran de résultat vous prévient, et **Reprendre** vous remet quand même en jeu tel que vous êtes. Les vaisseaux de réparation de votre base vous réparent dans leur aura.

Chaque monde affronte la même porte : la force et le paiement des aliens ne dépendent pas du monde où vous volez.

### Les vagues {#the-waves}

Les aliens sont ceux du jeu (Seeker, Phantasm, Bulwark, Goombah et Crystalys), rendus plus durs ou plus tendres par la porte. Le temps prévu est ce que la porte est conçue pour prendre à un pilote au niveau de départ de la Technique laser ([Aptitudes de pilote](/wiki/03-Mechanics/Pilot-Skills.md)) ; un pilote qui a fait monter sa Technique laser finit plus tôt.

<!-- solo-waves:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Porte | Vagues, celle du boss comprise | Aliens dans les vagues | Boss | Temps prévu |
| :--- | ---: | :--- | :--- | :--- |
| **Alpha Rift** | 10 | 60 Seeker, 160 Phantasm | Enhanced Phantasm | 10 à 15 min |
| **Beta Breach** | 14 | 80 Seeker, 180 Phantasm, 80 Bulwark, 20 Goombah | Enhanced Bulwark | 15 à 25 min |
| **Gamma Foundry** | 18 | 100 Phantasm, 120 Bulwark, 100 Goombah, 8 Crystalys | Elite Crystalys | 25 à 35 min |
| **Delta Siege** | 22 | 250 Seeker, 200 Phantasm, 180 Bulwark, 140 Goombah, 15 Crystalys | Siege Construct | 35 à 45 min |
| **Omega Vault** | 26 | 250 Seeker, 250 Phantasm, 200 Bulwark, 200 Goombah, 25 Crystalys | Omega Guardian | 50 à 60 min |

- **Delta Siege** : la vague 18 (250 Seeker) est facultative : vous pouvez la passer pendant son compte à rebours, et elle ne paie rien
- **Omega Vault** : la vague 17 (250 Seeker) est facultative : vous pouvez la passer pendant son compte à rebours, et elle ne paie rien; les vagues 22 à 24 sont d’élite, avec ×1,5 de coque, de bouclier et de dégâts

<!-- solo-waves:end -->

### Les boss {#the-bosses}

Un boss est le vaisseau d’un alien agrandi, avec une coque, un bouclier et une salve à lui, qu’aucun réglage de la porte ni du monde ne change. Une phase commence quand la coque du boss tombe au chiffre du tableau : son bouclier peut être refixé, sa salve ou tous ses dégâts changent, et il peut lancer une attaque. Chaque attaque est annoncée : un cercle, un anneau ou une marque sur votre vaisseau la montre un instant avant qu’elle ne frappe. Les aliens qu’un boss appelle ne paient ni ne lâchent rien.

<!-- solo-bosses:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Boss | Porte | Coque | Bouclier | Salve laser |
| :--- | :--- | ---: | ---: | ---: |
| **Enhanced Phantasm** | Alpha Rift | 330 000 | 530 000 | 5 700–7 000 |
| **Enhanced Bulwark** | Beta Breach | 690 000 | 170 000 | 4 500–5 500 |
| **Elite Crystalys** | Gamma Foundry | 620 000 | 250 000 | 3 800–4 700 |
| **Siege Construct** | Delta Siege | 1 150 000 | 1 730 000 | 3 400–4 200 |
| **Omega Guardian** | Omega Vault | 1 340 000 | 840 000 | 2 600–3 200 |

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

<!-- solo-bosses:end -->

## Ce que paie une victoire {#what-a-clear-pays}

Une victoire paie son tableau **une fois**, d’un coup, à l’instant où le boss meurt : les Credits, le Thulium, l’expérience et l’honneur, le minerai, les plaques et les Power Cores, et les munitions. L’expérience compte pour vos points PvE, comme celle d’un donjon.

<!-- solo-pay:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Porte | Crédits | Thulium | XP | Honneur |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 450 000 | 5 000 | 70 000 | 1 000 |
| **Beta Breach** | 1 500 000 | 12 000 | 180 000 | 2 500 |
| **Gamma Foundry** | 4 000 000 | 25 000 | 400 000 | 5 500 |
| **Delta Siege** | 8 000 000 | 40 000 | 800 000 | 10 000 |
| **Omega Vault** | 15 000 000 | 60 000 | 1 500 000 | 20 000 |

- **Alpha Rift** : Ship Fragment ×300, Nyxite ×300, Daraxium ×400 ; munitions : Advanced Plasma ×20 000, Ultra Core ×5 000, Experimental Fusion Core ×20 000
- **Beta Breach** : Ship Fragment ×700, Nyxite ×750, Daraxium ×800, Cataclysite ×400, Quorvium ×100 ; munitions : Advanced Plasma ×50 000, Ultra Core ×20 000, Experimental Fusion Core ×30 000
- **Gamma Foundry** : Ship Fragment ×1 150, Nyxite ×1 000, Cataclysite ×900, Quorvium ×400, Power Core ×15 ; munitions : Advanced Plasma ×30 000, Ultra Core ×60 000, Experimental Fusion Core ×50 000
- **Delta Siege** : Ship Fragment ×2 000, Nyxite ×1 750, Cataclysite ×1 500, Quorvium ×1 000, Reinforced Hull Plate ×70, Power Core ×40, Ancient Control Unit ×3 ; munitions : Advanced Plasma ×40 000, Ultra Core ×90 000, Experimental Fusion Core ×75 000
- **Omega Vault** : Ship Fragment ×3 250, Nyxite ×2 750, Cataclysite ×2 250, Quorvium ×1 600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10 ; munitions : Advanced Plasma ×50 000, Ultra Core ×100 000, Experimental Fusion Core ×100 000

<!-- solo-pay:end -->

**Le Thulium est rogné à un plafond.** Les portes ne peuvent pas rendre plus d’une part du Thulium que vous avez dépensé en tirages, comptée sur toutes vos portes et tous vos tirages (la part est dans la liste du haut). Ce qu’une victoire et ses aliens paieraient au-delà est rogné, et l’écran de résultat dit combien. Les Credits, l’expérience, l’honneur, le minerai, les plaques et les munitions ne sont jamais rognés.

### Les aliens {#the-aliens}

Chaque alien que vous tuez dans une porte paie aux chiffres qu’il a dans Alpha, quel que soit le monde où vous volez : aucun multiplicateur de monde, aucun booster et aucun bonus Premium ne les change. Une vague paie ses aliens **une fois** par partie, autant de fois que vous partiez et reveniez. Le paiement arrive à la fin de chaque tronçon de la partie : quand vous partez, mourez, n’avez plus de vies, abandonnez ou gagnez. Les éliminations d’un tronçon ne restent impayées que lors de la réinitialisation et lors d’un redémarrage du serveur pendant que vous êtes dedans (votre partie reste ouverte, mais les éliminations de ce tronçon sont perdues). Les éliminations d’une porte ne comptent pour rien d’autre : ni pour les missions, ni pour les statistiques d’éliminations, ni pour les compteurs des succès, ni pour le fil des éliminations, ni pour l’expérience de vos drones et P.E.T.s. L’expérience qu’elles paient compte en revanche pour vos points PvE, comme celle d’une victoire. Le butin des aliens arrive avec le paiement, directement dans votre inventaire.

<!-- solo-kills:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Alien | Crédits | Thulium | XP | Honneur |
| :--- | ---: | ---: | ---: | ---: |
| **Seeker** | 1 000 | 4 | 100 | 2 |
| **Phantasm** | 3 000 | 12 | 300 | 6 |
| **Bulwark** | 5 000 | 25 | 800 | 10 |
| **Goombah** | 15 000 | 75 | 3 000 | 24 |
| **Crystalys** | 75 000 | 200 | 12 000 | 52 |

| Porte | Crédits | Thulium | XP | Honneur |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 540 000 | 2 160 | 54 000 | 1 080 |
| **Beta Breach** | 1 320 000 | 5 980 | 186 000 | 2 520 |
| **Gamma Foundry** | 3 000 000 | 13 300 | 522 000 | 4 616 |
| **Delta Siege** | 4 975 000 | 21 400 | 829 000 | 7 640 |
| **Omega Vault** | 6 875 000 | 29 000 | 1 160 000 | 10 100 |

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
