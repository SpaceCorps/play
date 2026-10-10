<!-- wiki-i18n source: 0f9ae19e1c5f8f9d -->
<!-- wiki-i18n title: Combat -->
# Mécaniques de combat {#combat-mechanics}

Cette section explique comment les dégâts sont calculés, appliqués et réparés pendant les combats dans SpaceCorps.

![The death screen: respawn at the nearest portal or on the spot, each with its lock](../../img/wiki-img/shots/death.jpg)
![The flight screen in a fight: ship and pilot windows, the target, the hotbar, the chat, the log and the minimap](../../img/wiki-img/shots/hud-fight.jpg)
![The Target window: the alien, its distance, hull and shield](../../img/wiki-img/shots/hud-target.jpg)

## Calcul des dégâts {#damage-calculation}

Quand un vaisseau tire avec ses lasers, le serveur calcule les dégâts infligés selon la séquence suivante :

### 1. Dégâts de base et variation aléatoire {#1-base-damage-random-variance}

Les dégâts de base de tous les lasers équipés (y compris les lasers des drones) et de leurs amplis laser installés sont additionnés.
- **Tirage aléatoire** : les dégâts réels d’une salve sont tirés au hasard entre **80 %** et **100 %** du total des dégâts de base.
  - Formule : `Roll = (0.8 + (Random * 0.2)) * BaseDamage`

### 2. Coups critiques {#2-critical-hits}

Chaque salve a une chance d’être un coup critique.
- **Taux critique** : le taux critique moyen des lasers équipés, plus la somme des taux critiques de tous les amplis laser équipés.
- **Multiplicateur critique** : si un tir est critique, le tirage de dégâts est multiplié par **1,5**. Le nombre de dégâts d’une salve critique s’affiche en cyan glacé, plus grand, avec un « ! » (voir [Nombres de dégâts et de soins](#damage-and-heal-numbers)).
- Les Quantum Laser I et II n’ont pas de taux critique propre : ce sont leurs amplis qui le leur donnent.
- **Dégâts critiques fixes** : les dégâts critiques fixes des amplis laser s’ajoutent après le multiplicateur.
  - Formule : `CritDamage = (Roll * 1.5) + FixedCritDamage`

### 3. Multiplicateurs globaux {#3-global-multipliers}

Enfin, les multiplicateurs globaux (comme les boosters actifs, par exemple les +10 % d’un Laser Damage Booster, ou les multiplicateurs des munitions laser x2, x3, x4) sont appliqués pour obtenir les dégâts finaux :
- Formule : `FinalDamage = Damage * AmmoMultiplier * (1.0 + BoosterDamagePercent)`
- Une [formation de drones](/wiki/03-Mechanics/Formations.md) portée peut encore multiplier le résultat : par exemple Auger +21 % de dégâts laser, Gyre −11 % et, contre les aliens, Culler +12 % (un facteur à part, qui ne fait pas partie du pourcentage des boosters).
- Les munitions **Siphon Battery** ont le multiplicateur x1 mais une autre cible : leurs dégâts sont pris sur le seul bouclier de la cible (jamais sur la coque, quelle que soit l’absorption) et vont dans votre propre bouclier, jusqu’à votre maximum. Voir [Lasers et munitions](/wiki/06-Items/Lasers.md).

### 3b. Roquettes {#3b-rockets}

Une [roquette](/wiki/06-Items/Rockets.md) a ses propres dégâts (de 1 700 à 2 100 pour une Lancet I, de 5 200 à 6 200 pour une Lancet III, de 45 000 à 50 000 pour une N.U.K.E.), déterminés une fois par un jet au moment du tir et les mêmes pour tous les vaisseaux : vos lasers, amplis, boosters et munitions ne les changent pas, et elle ne fait pas de coup critique. Toutes les roquettes partagent un même délai de **3 secondes**. Une roquette à cible unique a une **pénétration de bouclier** : elle est retranchée de l’absorption de votre cible (voir Subir des dégâts, plus bas) ; une explosion blesse tous les vaisseaux dans son rayon, le nombre entier au centre et la moitié au bord. Rien ne plafonne ce qu’une roquette retire au vaisseau d’un pilote : le bouclier d’abord, puis la coque. Les roquettes ne blessent jamais votre propre corporation ni votre propre [groupe](/wiki/03-Mechanics/Groups.md), quelles que soient les corporations qui le composent. Une [formation de drones](/wiki/03-Mechanics/Formations.md) portée est la seule chose qui change les deux : une formation de roquettes augmente les dégâts de chaque roquette (jusqu’à +55 %), et quelques-unes allongent ou raccourcissent le minuteur. Les [astéroïdes](/wiki/03-Mechanics/Asteroid-Mining.md) subissent les dégâts des roquettes et ceux des lasers à 5 % de ce qu’une salve inflige à un vaisseau (vos amplis, boosters, munitions et coups critiques comptent, puis le blindage de l’astéroïde se retranche) ; les drones ne leur font rien, et un astéroïde sur la trajectoire d’un tir prend le coup à la place du vaisseau qui se trouve derrière ([Abri](/wiki/03-Mechanics/Asteroid-Mining.md#cover)).

### 4. Face à la cible {#4-facing-the-target}

Un vaisseau ou un alien qui a verrouillé sa cible et tire se tourne vers elle, quelle que soit sa direction de vol (en tournant autour, en reculant ou à l’arrêt), et reprend son cap quand il cesse de tirer.

### 5. Portée {#5-range}

Un vaisseau tire une salve par seconde tant que sa cible est dans sa **portée**, et suspend le tir tant que la cible est plus loin : le tir cesse de consommer des munitions jusqu’à ce que la cible soit de nouveau assez proche, et le panneau de la cible indique « Hors de portée ». La portée est **la moyenne des portées de tous vos lasers** (ceux de vos drones compris), arrondie à l’unité la plus proche, et c’est un seul nombre pour tout le vaisseau : en deçà, tous les lasers tirent ; au-delà, aucun. Un laser à longue portée à côté de lasers plus courts n’allonge donc pas votre portée : un Starfire-III (850) et deux Quantum Laser II (700) donnent 750. Un bonus de portée de la Forge compte sur son propre laser, avant la moyenne. Un vaisseau sans laser ne peut pas tirer au laser, et le hangar n’affiche aucune portée pour lui (un tiret) ; ses roquettes tirent toujours, chacune avec sa propre portée (voir [Roquettes](/wiki/06-Items/Rockets.md)). Voir [Lasers et munitions](/wiki/06-Items/Lasers.md) pour la portée propre de chaque laser.

## Nombres de dégâts et de soins {#damage-and-heal-numbers}

Un coup s’affiche comme un nombre qui flotte au-dessus du vaisseau qu’il touche. **Vos propres nombres** s’affichent toujours : les dégâts que vous infligez, ceux que vous subissez et vos propres réparations. **Le vaisseau sous votre cercle de verrouillage** en montre davantage : chaque coup et chaque soin qu’il reçoit, **de n’importe quelle source**. Cela comprend les lasers, roquettes et drones des autres pilotes, les aliens, les Clan Wardens, ainsi que les réparations et la régénération de bouclier du vaisseau lui-même. Quand quelqu’un d’autre tire sur votre cible, vous voyez ses dégâts.

- **Couleurs.** Or : dégâts sur un alien ou sur un pilote ennemi. Rouge avec un moins : dégâts sur un vaisseau que vous protégez (un pilote de votre propre corporation ou de votre groupe) et dégâts que vous subissez vous-même. Vert avec un plus : un soin, comme une Emergency Repair, un Repair Drone ou un bouclier qui revient. « Miss » en argent pâle : un coup direct que l’esquive d’une formation a dévié. Une salve critique est plus grande et se termine par un « ! » (cyan glacé quand elle touche un alien ou un ennemi).
- **Les vôtres restent plus lumineux.** Les nombres des autres sur votre cible sont un peu plus petits et plus pâles, et se tiennent dans une colonne à droite du vaisseau, pour ne jamais couvrir les vôtres.
- **Un nombre pour une foule.** Les coups qui arrivent ensemble sont additionnés en un seul nombre suivi d’un compte (`×35`). Quarante pilotes qui tirent sur un vaisseau font environ deux nombres par seconde, et jamais plus de sept. Les soins s’affichent une fois par seconde.
- **Seulement le vaisseau sous le cercle.** Tout autre vaisseau ne montre que vos propres coups et les coups que vous recevez. Les radiations du trou noir et le drain de bouclier d’une formation n’ont pas de nombres : ils se voient sur les barres.
- **Le réglage.** Paramètres › Interface › **Afficher les dégâts des autres sur ma cible**, activé par défaut. Désactivé, vous ne voyez que vos propres nombres. **Réduire les animations** garde tous les nombres immobiles : aucun n’apparaît d’un bond ni ne monte.

---

## Récompenses d’élimination : le premier coup revendique {#kill-rewards-first-hit-claims}

Les récompenses d’un alien vont au pilote qui l’a touché en premier, pas à celui qui porte le dernier coup.

- **Revendication** : le premier pilote dont un tir endommage un alien le revendique. Chacun de vos coups renouvelle votre revendication.
- **La perdre** : si vous ne touchez pas l’alien pendant **10 secondes**, votre revendication expire et le prochain pilote qui le touche le revendique. Votre revendication prend aussi fin quand votre vaisseau est détruit ou que vous quittez la carte (par un portail ou en vous déconnectant), et revenir dans les 10 secondes ne vous la rend pas.
- **L’élimination** : quand l’alien est détruit, le pilote qui détient sa revendication reçoit tout : crédits, Thulium, XP, honneur, l’élimination pour les quêtes et les points de réinitialisation, et la caisse de [cargaison](/wiki/03-Mechanics/Cargo.md). Un pilote qui achève un alien revendiqué par quelqu’un d’autre ne reçoit rien, et le Journal de jeu le lui dit. Quand votre revendication paie et qu’un autre pilote porte le dernier coup, le Journal de jeu nomme ce pilote et indique que votre revendication vous rapporte.
- **Points de classement** : l’élimination ajoute aussi des points PvE au classement du pilote qui détient la revendication, d’autant plus que l’alien est coriace : 1 pour un Seeker, 2 pour un Phantasm, 4 pour un Bulwark, 7 pour un Goombah et 16 pour un Crystalys (l’article de chaque alien donne le sien). Ils n’appartiennent qu’à ce pilote : le partage des récompenses d’un groupe ne les comprend pas.
- **Le voir** : quand vous sélectionnez un alien qu’un autre pilote a revendiqué, la fenêtre Cible affiche *Revendiqué par* ce pilote et *Aucune récompense*.
- Les [pilotes de corporation](/wiki/03-Mechanics/Company-Pilots.md) ne revendiquent jamais un alien, et un alien qu’ils achèvent paie quand même le pilote qui détient sa revendication.
- Un pilote en [groupe](/wiki/03-Mechanics/Groups.md) partage ce que sa revendication rapporte avec les membres du groupe qui sont proches et qui tirent ; la revendication elle-même n’appartient qu’à lui.
- **Les meneurs des [essaims](/wiki/05-Swarms/Swarms.md), les Dormant Pulses et les [Clan Wardens](/wiki/03-Mechanics/Clans.md#warden-pay-and-loot) font exception** : un boss d’essaim, chaque Dormant Pulse et chaque Clan Warden paient selon les dégâts que chaque pilote leur a infligés, pas selon le premier coup, et leur caisse de cargaison va au pilote qui a infligé le plus de dégâts ([comment paie l’élimination d’un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Les autres suivants, les Pirate Scouts et les Seeker Slaves, paient selon la revendication, comme tout alien. Les points PvE d’un vaisseau d’essaim sont sur la page Essaims.

---

## Les aliens qui ne font que riposter {#aliens-that-only-fight-back}

Le Seeker et le Goombah ne commencent jamais un combat. Chacun se retourne contre un pilote qui le touche (un coup qui inflige des dégâts ; le tir d’un autre alien ne le provoque jamais), combat celui que décrit la section [Contre qui un alien se bat](#who-an-alien-fights) et lâche prise **10 secondes** après le dernier coup reçu, de qui que ce soit. S’il est laissé tranquille pendant **30 secondes**, sa coque se répare de 2 % de son maximum par seconde. Les autres aliens (Phantasm, Bulwark, Crystalys) s’en prennent à tout pilote non protégé qui entre dans leur rayon d’aggro (700, 700 et 900 unités) et ne réparent jamais leur coque ; le bouclier de chaque alien se recharge à partir de 15 secondes après le dernier coup reçu.

---

## Contre qui un alien se bat {#who-an-alien-fights}

Un alien continue de combattre **le premier pilote qui lui a tiré dessus**, tant qu’il peut encore poursuivre ce pilote : celui-ci est sur la carte, n’est pas dans une zone sûre, n’est ni occulté ni dans la fenêtre de son EMP, est en vie et a touché l’alien au cours des **10 dernières secondes** (chaque coup relance les 10 secondes, qu’il s’agisse d’une salve de laser, d’une roquette ou du bord d’une explosion). Tant que cela tient, les tirs des autres pilotes ne le détournent jamais, si proches soient-ils et même s’ils touchent souvent, si bien qu’un pilote peut retenir un alien pendant que d’autres lui tirent dessus.

Quand le premier pilote décroche (il quitte la carte, atteint une zone sûre, s’occulte ou déclenche son EMP, est détruit, ou cesse de toucher l’alien pendant 10 secondes), l’alien se retourne contre le pilote **suivant** qui s’est joint au combat, dans l’ordre de leur premier tir sur lui, et non contre celui qui l’a touché en dernier. Un pilote qui a décroché puis lui tire de nouveau dessus se range tout au bout de la file. Un alien garde la trace des **32** premiers pilotes qui lui ont tiré dessus ; un 33e tireur ne compte pas dans la file tant que l’un d’eux n’a pas décroché, et, quelle que soit la taille de la foule, l’alien reste sur le premier.

Les [pilotes de corporation](/wiki/03-Mechanics/Company-Pilots.md) passent après tous les joueurs : un alien ne combat un pilote de corporation que tant qu’aucun joueur qu’il peut encore poursuivre ne lui a tiré dessus, un joueur qui tire sur un alien que combat un pilote de corporation le lui prend, et un pilote de corporation ne détourne jamais un alien d’un joueur. Rien de tout cela ne change qui reçoit les récompenses de l’alien : c’est la revendication qui en décide ([Récompenses d’élimination](#kill-rewards-first-hit-claims)).

---

## Les aliens se désintéressent {#aliens-lose-interest}

Aucun alien ne vous suit à travers toute la carte. Mais un alien que vous **touchez** ne se désintéresse pas de vous, il vous combat : pendant **10 secondes** après votre dernier coup (chaque coup relance les 10 secondes, qu’il s’agisse d’une salve de laser, d’une roquette ou du bord d’une explosion), il fonce sur vous, à sa propre vitesse, chaque fois que vous êtes au-delà de sa portée d’attaque (Seeker 600, Phantasm et Bulwark 700, Goombah 800, Crystalys 900), et continue d’approcher et de tirer jusqu’à ce que vous soyez à portée. Tant que vous continuez à le toucher, la distance sur laquelle il vous suit n’a pas de limite. Un laser qui porte plus loin que l’arme de l’alien (un Starfire-III porte à 850 unités, un Helios Beam à 900) ne vous permet pas de le toucher depuis un endroit où il ne peut pas répondre, et un vaisseau plus rapide ne le garde derrière vous que tant que vous continuez à tirer. Il vous lâche quand même aussitôt si vous atteignez une zone sûre, si vous vous occultez ou si vous quittez la carte.

Quand plusieurs pilotes touchent le même alien, il s’en tient au premier qui lui a tiré dessus (voir [Contre qui un alien se bat](#who-an-alien-fights)) : il fonce sur ce pilote et tire, si bien qu’un groupe posté autour de lui juste hors de sa portée ne peut pas le faire courir de l’un à l’autre sans qu’il riposte jamais.

Un alien qui vous a pris pour cible (un Phantasm, un Bulwark ou un Crystalys dont vous vous êtes approché, ou n’importe quel alien sur lequel vous avez tiré) et que vous n’avez pas touché depuis 10 secondes lâche prise dès que l’une de ces conditions est remplie :

- **Vous ne lui avez jamais tiré dessus :** vous êtes à plus de **1 200 unités** de lui, ou il a parcouru **2 000 unités** depuis l’endroit où la poursuite a commencé.
- **Vous lui avez tiré dessus dans la dernière minute :** vous êtes à plus de **2 500 unités** de lui, ou il a parcouru **3 000 unités** depuis l’endroit où la poursuite a commencé. Un combat que vous avez commencé reste équitable.

Un alien qui lâche prise reprend sa ronde depuis l’endroit où il se trouve, jamais vers l’endroit où il vous a vu pour la dernière fois (pas même quand vous vous occultez ou déclenchez une EMP), et ne vous reprend pas pour cible pendant **8 secondes**, sauf si vous lui tirez dessus. Chaque alien décide pour lui-même, si bien qu’une meute mixte s’éclaircit à mesure que vous vous éloignez. Les aliens ne vous suivent jamais dans une zone sûre ni à travers un portail, et ceux qui vous ont perdu près de l’une ou de l’autre s’en éloignent, chacun dans sa propre direction, pour ne pas attendre en tas. L’intérêt d’un alien ne descend jamais en dessous de sa portée d’attaque et de son rayon d’aggro, plus 100 unités.

Les aliens ne se repoussent pas entre eux : une meute aux trousses d’un pilote approche sans garder d’espace entre ses vaisseaux, et une meute qui a perdu son pilote ne se disperse que lorsque chaque alien choisit sa propre route. Un alien reste en revanche à distance d’un **vaisseau** : il ne se retrouve jamais dans la coque d’un pilote, et un pilote qui se gare sur l’un le pousse devant lui.

Voler plus vite ne vous aide que jusqu’à un certain point : un Protos (160) n’est pas plus rapide que les aliens qui chassent (Phantasm 160, Bulwark 175, Crystalys 230), donc c’est la laisse, et non votre vitesse, qui met fin à la poursuite.

---

## Subir des dégâts et zones sûres {#taking-damage-safe-zones}

Quand votre vaisseau est touché par un ennemi ou un PNJ, les dégâts sont traités ainsi :

### 1. Absorption du bouclier {#1-shield-absorption}

Les dégâts reçus sont répartis entre boucliers et points de vie selon l’**absorption moyenne** de votre vaisseau : la moyenne de l’absorption de vos boucliers, chacun avec celle de ses cellules de bouclier, plus le Shield Absorbance Boost de la Boutique de saison (voir [Mécaniques des boucliers](/wiki/03-Mechanics/Shields.md)). Elle n’est **pas plafonnée à 100 %** : la part d’un tir que prennent les boucliers est votre absorption **moins la pénétration de bouclier de l’attaquant**, entre 0 % et 100 %.
- L’**absorption** (par ex. 80 % pour le meilleur bouclier avec les meilleures cellules, 56 % pour un Basic Shield Core avec deux Absorption Shield Cell I) de chaque tir est prise par les boucliers, moins la pénétration du tir : les 35 % d’une Lancet III laissent 45 % sur les boucliers d’un vaisseau à 80 %, et le reste (ici 55 %) frappe directement les PV.
- La **pénétration de bouclier** vient des roquettes directes (10 à 35 %) et des munitions laser x3 et x4 (5 % et 10 %) ; les aliens n’en ont pas. Un vaisseau au-delà de 100 % (disons 112 %) garde un tir entier sur ses boucliers face à une pénétration allant jusqu’à la différence (ici 12 %). Les Penetration Amps des lasers du tireur (+3 % à +12 % par emplacement) et une formation de drones s’y ajoutent, et rien ne plafonne le total.
- Un bouclier trop faible pour sa part reporte la différence sur les PV ; si les boucliers sont entièrement vides, **100 %** des dégâts restants frappent les PV.
- Les aliens n’ont pas de statistique d’absorption : leurs boucliers prennent 80 % de chaque tir (moins la pénétration du tir), leur coque le reste.
- **Formations de drones.** Rampart augmente votre absorption de 17 % (Shrike la réduit de 6 %), et Asterism donne à chaque coup direct reçu 7 % de chances de ne faire aucun dégât (un « Raté » flottant s’affiche), et les coups qui arrivent se partagent entre bouclier et coque comme d’habitude. Gemini (+9 points) et Stiletto (+16) ajoutent de la pénétration à vos propres munitions et aux roquettes directes, sans plafond ([Formations de drones](/wiki/03-Mechanics/Formations.md)). Pour un laser, ses amplis comptent aussi.

### 2. Immunité en zone sûre {#2-safe-zone-immunity}

La base d’origine de chaque faction (cartes X-1) contient des zones sûres.
- Entrer dans une zone sûre rend votre vaisseau totalement insensible aux dégâts.
- **Rupture de l’immunité** : attaquer un ennemi vous retire immédiatement l’immunité de la zone sûre, même si vous vous trouvez physiquement à l’intérieur.
- Un anneau autour de chaque station et de chaque portail vous protège dès que 5 secondes se sont écoulées depuis le dernier coup reçu et 15 depuis votre dernier tir. Tant qu’il vous protège et que vous êtes hors combat, la fenêtre du hangar vous permet de changer de vaisseau sans quitter le jeu : voir [Le hangar en vol](/wiki/03-Mechanics/Hangar.md).
- Les stations n’existent que dans les bases d’origine (`x-1`). Les secteurs dangereux (`DS-1` à `DS-4`) n’en ont aucune : les anneaux autour des portails y sont les seules zones sûres.

### 3. Sous le feu dans un secteur dangereux {#3-under-attack-in-a-danger-sector}

Un saut par un portail dure 3 secondes (voir [Navigation sur la carte spatiale](/wiki/01-General/Spacemap%20Travel.md)). Dans les secteurs dangereux (`DS-1` à `DS-4`), un pilote dont le vaisseau a été touché par un autre pilote ou par un alien dans les **10 dernières secondes** ne peut pas en lancer un, et un coup reçu annule un saut en cours. Partout ailleurs, les attaques n’interrompent jamais un saut, et rien n’interrompt la récupération d’une caisse de [cargaison](/wiki/03-Mechanics/Cargo.md).

---

## Récupération et réparation {#recovery-repair}

Pour se remettre d’un combat, les pilotes peuvent compter sur la régénération passive et sur des robots utilitaires actifs :

### 1. Régénération passive du bouclier {#1-shield-passive-regeneration}

- **Fonctionnement** : restaure chaque seconde autant de points de bouclier que la vitesse de recharge de votre bouclier.
- **Délai** : interrompue par le combat ; la régénération passive ne reprend qu’après **15 secondes** sans subir de dégâts.
- **Formations de drones** : Adamant et Redoubt rendent du bouclier chaque seconde, même en combat (voir [Formations de drones](/wiki/03-Mechanics/Formations.md)).

### 1b. Siphon Battery

Les munitions [Siphon Battery](/wiki/06-Items/Lasers.md) ajoutent aussitôt au vôtre le bouclier qu’elles drainent d’une cible, jusqu’à votre maximum. Gagner du bouclier n’est pas subir des dégâts : cela ne retarde donc pas votre régénération passive.

### 2. Drones de réparation (réparation de la coque) {#2-repair-drones-hull-repair-}

- **Fonctionnement** : si vous équipez un Repair Drone (dans les extras du hangar), vous l’activez depuis la barre rapide (faites-le glisser depuis le sélecteur Extras sur un emplacement) et il répare votre coque (PV). Le moindre coup reçu le désactive, et il s’arrête quand la coque est pleine. Avec un [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) installé, vous n’avez pas à le réactiver : il le lance tout seul dès que le délai indiqué plus bas est écoulé, sauf si vous l’avez arrêté à la main.
- **Taux de réparation** : restaure chaque seconde un pourcentage de vos points de vie maximum (seul le meilleur drone installé compte, ils ne s’additionnent pas) :
  - **Repair Drone I** : 1,5 % des PV max / s
  - **Repair Drone II** : 2,25 % des PV max / s
  - **Repair Drone III** : 3,5 % des PV max / s
  - **Repair Drone IV** : 5 % des PV max / s
- **Délai** : les drones de réparation ne commencent à réparer la coque qu’après **10 secondes** sans subir de dégâts.
- **Dans un emplacement de compétence**, un Repair Drone ne répare pas tout seul : il vous donne **Emergency Repair**, un bouton qui rend une part de vos points de vie maximum en dix secondes, même sous le feu (voir [Compétences](/wiki/03-Mechanics/Abilities.md)).

---

## L’occultation et l’EMP {#cloaking-and-the-emp}

Un tir nécessite un verrouillage. Deux [extras](/wiki/06-Items/Extras.md) empêchent de vous verrouiller :

- **Cloaking CPU** : tant que vous êtes occulté (sans limite de temps), les pilotes des autres corporations, les aliens et les pilotes de corporation ne voient pas votre vaisseau et ne peuvent pas le verrouiller ; ils voient un simple point rouge sur la mini-carte, là où vous êtes. Votre première salve met fin à l’occultation, et vous ne pouvez pas vous occulter de nouveau pendant une minute, ni dans les 10 secondes qui suivent un coup reçu ou un tir.
- **EMP Charge** : pendant 3 secondes, personne ne peut vous verrouiller, et tout verrouillage déjà posé sur vous se brise aussitôt. Elle met fin à toute occultation à moins de 1 500 unités du pilote qui la déclenche, sauf celles des membres de son propre groupe. Elle ne vous cache pas et ne vous rend pas invulnérable : elle arrête ce qui nécessite un verrouillage.

Une roquette est aussi un tir : elle met fin à votre propre occultation, et l’explosion de zone de la roquette d’un autre pilote blesse quand même un vaisseau occulté et met fin à son occultation, car une explosion n’a pas besoin de verrouillage (voir [Roquettes](/wiki/06-Items/Rockets.md)). L’EMP arrête les lasers verrouillés et les roquettes guidées, pas une explosion.

Ni l’un ni l’autre ne change la revendication d’une élimination : une revendication est l’historique de qui a touché un alien, pas un verrouillage, et l’occultation libère la vôtre.
