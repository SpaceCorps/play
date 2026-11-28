<!-- wiki-i18n source: 0a2447734a603004 -->
<!-- wiki-i18n title: Capacités spéciales -->
# Capacités spéciales {#special-abilities}

<!-- wiki-search: special ability; special abilities; ability; abilities; mob; mobs; regenerate; mending; shield burst; hardened plating; plating; enrage; call reinforcements; reinforcements; clones; decoy; flee and return; flee; life drain; nova pulse; nova; rocket barrage; barrage; veil; sow mines; mines; split; fragments; boss steps; ladder; three steps; warning; tell; surprise; warlord; warden; leader; capacités spéciales; régénération; sursaut de bouclier; blindage durci; fureur; appel de renforts; clones; fuite et retour; drain de vie; impulsion nova; salve de roquettes; voile; pose de mines -->

Certains aliens portent une **capacité spéciale** : une chose qu’ils font une seule fois dans leur vie, quand leur coque est à moitié détruite. Se régénérer, un sursaut de bouclier, une fuite, un appel à l’aide. Rien ne se voit avant qu’elle commence, si bien que chaque chasse peut finir par une surprise. Cette page dit ce que fait chaque capacité et comment y répondre. Les boss fonctionnent autrement : ils changent leur façon de combattre en trois étapes à mesure que leur coque baisse, et les petits aliens du dernier palier peuvent se briser en fragments quand on les détruit trop vite.

## Comment ça marche {#how-it-works}

<!-- mob-rules:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **Une fois.** Un alien qui porte une capacité l’utilise une seule fois dans sa vie : quand, au combat, sa coque (pas son bouclier) tombe sous 50 % de son maximum. Un coup qui le détruit depuis au-dessus de cette ligne ne le laisse jamais tirer, et un alien qui n’est pas au combat attend qu’un combat commence.
- **D’abord un avertissement.** La capacité commence par un avertissement : un anneau qui se referme sur le vaisseau et un mot au-dessus. Une capacité dont la rubrique ci-dessous dit qu’elle commence aussitôt n’a pas d’avertissement. L’alien peut encore être détruit pendant l’avertissement ; alors il ne se passe rien et il paie comme d’habitude. Les espèces légères (Seeker et Phantasm) sont plus rapides : leurs avertissements et leurs effets durent 50 % du temps normal.
- **Rien ne se voit avant.** Un alien qui porte une capacité ressemble à n’importe quel autre, dans le moindre détail, jusqu’au début de son avertissement. Rien dans le jeu ne dit lequel c’est, pas même le [Guide du voyageur](/wiki/03-Mechanics/Travelers-Guide.md).
- **Qui en porte une.** Une petite part des aliens des secteurs des compagnies et des Danger Sectors : plus le palier est fort, plus la part est grande, et les chefs des essaims (Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah et Boss Crystalys) en portent plus souvent que les autres. Les aliens de la Deep Void, des donjons de clan et des portes solo n’en portent jamais, ni les suivants d’un essaim, les vagues d’un Gardien, la Dormant Force ou le Tesseract.
- **Il paie ce que paie n’importe quel alien.** Un alien qui utilise une capacité paie, lâche du butin et compte exactement comme un qui n’en utilise pas : la capacité n’ajoute rien à l’élimination et lui prend du temps. L’élimination reste au pilote qui la détenait : tant que l’alien fuit, se régénère ou se cache, la revendication ne s’éteint pas.
- **Les vaisseaux appelés et les copies ne sont pas des éliminations.** Les vaisseaux qu’un alien appelle et les copies qu’il fait ne paient rien, ne lâchent rien et ne comptent pour aucune quête, statistique ni classement. Au plus 6 vivent pour un appelant et 24 sur une carte, et les aliens propres de la carte reviennent toujours à l’heure.
- **Tout le monde sur la carte le voit.** Les pilotes de la carte sont prévenus quand une capacité commence : le jeu dessine l’anneau, le mot et l’effet et joue un son.

<!-- mob-rules:end -->

## Les douze capacités {#the-twelve-abilities}

Une capacité commence par un **avertissement**, sauf si sa rubrique dit qu’elle commence aussitôt : un anneau qui se referme sur le vaisseau et un mot au-dessus. Les durées et les chiffres ci-dessous sont ceux des espèces lourdes. Quand un chiffre a plusieurs valeurs, ce sont celles des paliers nommés entre parenthèses, la lettre grecque devant le nom d’un alien.

<!-- mob-abilities:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

### Régénération {#regenerate}

Il reste immobile et restaure 15 % / 20 % / 25 % / 30 % (α / β / γ / δ) de sa coque et de son bouclier en 6 s, sans rien tirer pendant ce temps. Des dégâts qui totalisent 10 % de sa coque et de son bouclier ensemble l’interrompent, et il garde ce qu’il a déjà restauré.

- **Avertissement** : 1,5 s
- **Le mot au-dessus du vaisseau** : RÉGÉNÈRE
- **Portée par** : n’importe quel alien
- **Réponse** : Faites-le éclater avec des roquettes ou une foule de vaisseaux, ou détruisez-le pendant l’avertissement.

### Sursaut de bouclier {#shield-burst}

Une nouvelle couche de bouclier de 15 % / 20 % / 30 % / 40 % (α / β / γ / δ) de sa coque maximale vient s’ajouter à son bouclier. Tant qu’elle tient, elle prend chaque point d’un coup ; elle disparaît quand elle est épuisée ou après 10 s.

- **Avertissement** : 1 s
- **Le mot au-dessus du vaisseau** : BOUCLIER
- **Portée par** : n’importe quel alien
- **Réponse** : Les munitions et les roquettes qui percent les boucliers la traversent mieux. Ou tirez sur un autre alien jusqu’à ce qu’elle disparaisse.

### Blindage durci {#hardened-plating}

Pendant 7 s / 8 s / 10 s (β / γ / δ) il ne prend que 50 % de chaque coup, coque et bouclier confondus : deux fois plus résistant. Il continue de se battre, et les chiffres de vos coups deviennent gris.

- **Avertissement** : 1,5 s
- **Le mot au-dessus du vaisseau** : BLINDAGE
- **Portée par** : les espèces lourdes (Bulwark, Goombah et Crystalys) et les chefs d’essaim lourds (Pirate Boss et Boss Phantasm), à partir de β
- **Réponse** : Attendez que cela passe, frappez un autre alien en attendant et gardez vos rafales pour après.

### Fureur {#enrage}

Pendant 10 s, ses dégâts sont multipliés par ×1,3 / ×1,4 / ×1,5 / ×1,75 (α / β / γ / δ) et sa vitesse par ×1,25.

- **Avertissement** : 1 s
- **Le mot au-dessus du vaisseau** : FURIEUX
- **Portée par** : n’importe quel alien
- **Réponse** : Gardez votre bouclier levé, restez en mouvement et hors de sa portée.

### Appel de renforts {#call-reinforcements}

4 / 6 (γ / δ) aliens plus petits arrivent par le bord de la carte le plus proche, en 2 vagues espacées de 3 s. L’espèce qui vient : Phantasm (appelé par Bulwark et Goombah); Bulwark (appelé par Crystalys). Ensemble ils ont 45 % / 60 % (γ / δ) de sa coque et de son bouclier et tirent 50 % de sa salve. Ils ne paient rien, ne lâchent rien et ne comptent pour rien, et ils partent après 45 s, ou quand l’appelant est détruit.

- **Avertissement** : 2 s
- **Le mot au-dessus du vaisseau** : APPELLE
- **Portée par** : les espèces lourdes (Bulwark, Goombah et Crystalys) et les chefs d’essaim lourds (Boss Phantasm et Boss Goombah), à partir de γ
- **Réponse** : Détruisez l’appelant : ses vaisseaux partent avec lui. Une arme à effet de zone les balaie.

### Clones

3 (γ / δ) copies de lui apparaissent autour de lui, avec son nom et son apparence. Ensemble elles ont 18 % (γ / δ) de sa coque et de son bouclier ; elles ne tirent rien et ne paient rien, et elles durent 15 s ou jusqu’à la destruction du vrai. Le vrai porte un anneau fin tant que les copies sont là, et la fenêtre de cible appelle une copie Leurre.

- **Avertissement** : 1 s
- **Le mot au-dessus du vaisseau** : CLONAGE
- **Portée par** : n’importe quel alien, à partir de γ
- **Réponse** : Suivez l’anneau et la barre de coque qui bouge du vrai, ou utilisez une arme à effet de zone.

### Fuite et retour {#flee-and-return}

Il s’éloigne de ses attaquants à vitesse ×2 pendant 5 s / 6 s / 7 s / 8 s (α / β / γ / δ), puis se retourne contre le premier pilote qui l’a touché. Il ne quitte jamais la carte ni n’entre dans une zone sûre, il peut être touché tout le temps, et le pilote qui détenait son élimination la garde.

- **Avertissement** : 0,5 s
- **Le mot au-dessus du vaisseau** : FUITE
- **Portée par** : n’importe quel alien
- **Réponse** : Poursuivez-le, ou touchez-le avec des roquettes pendant qu’il vole.

### Drain de vie {#life-drain}

Pendant 10 s il ne tire rien d’autre : une fois par seconde il draine chaque vaisseau à sa portée avec une salve complète que rien n’esquive, et il se soigne de 75 % / 100 % / 100 % (β / γ / δ) des dégâts qu’il inflige, au plus 20 % de sa coque en tout.

- **Avertissement** : 1 s
- **Le mot au-dessus du vaisseau** : DRAINE
- **Portée par** : les espèces lourdes (Bulwark, Goombah et Crystalys) et les chefs d’essaim lourds (Pirate Boss, Boss Phantasm, Boss Goombah et Boss Crystalys), à partir de β
- **Réponse** : Mettez un rocher ou un mur dans la ligne, passez en furtif ou quittez sa portée.

### Impulsion nova {#nova-pulse}

Un anneau grandit au sol autour de lui pendant l’avertissement. Quand l’anneau est plein, il frappe une fois chaque vaisseau à l’intérieur, avec 4 / 5 (γ / δ) de ses salves. Son rayon, en unités, est 700 / 800 (γ / δ).

- **Avertissement** : 2,5 s
- **Le mot au-dessus du vaisseau** : NOVA
- **Portée par** : les espèces lourdes (Bulwark, Goombah et Crystalys) et les chefs d’essaim lourds (Pirate Boss, Boss Phantasm et Boss Goombah), à partir de γ
- **Réponse** : Sortez de l’anneau avant qu’il se remplisse : c’est le seul coup que vous pouvez esquiver.

### Salve de roquettes {#rocket-barrage}

Pendant 3 s il tire 4 / 6 / 8 (β / γ / δ) [roquettes Rivet](/wiki/06-Items/Rockets.md#the-twelve-rockets) sur sa cible : Rivet I / II / II (β / γ / δ). Elles volent droit et ne sont pas guidées.

- **Avertissement** : 1,5 s
- **Le mot au-dessus du vaisseau** : SALVE
- **Portée par** : les espèces lourdes (Bulwark, Goombah et Crystalys) et les chefs d’essaim lourds (Boss Phantasm et Boss Goombah), à partir de β
- **Réponse** : Restez en mouvement : les roquettes vont droit. Un rocher sur le chemin les arrête.

### Voile {#veil}

Pendant 6 s / 8 s (γ / δ), un vaisseau à plus de 700 unités de lui ne peut pas le verrouiller, et un verrouillage tenu est perdu. Plus près, on le voit comme d’habitude. Il continue de se battre, et une explosion le blesse quand même.

- **Avertissement** : aucun, elle commence aussitôt.
- **Le mot au-dessus du vaisseau** : SE VOILE
- **Portée par** : les espèces lourdes (Bulwark, Goombah et Crystalys) et les chefs d’essaim lourds (Pirate Boss, Boss Phantasm, Boss Goombah et Boss Crystalys), à partir de γ
- **Réponse** : Approchez-vous à moins de 700 unités.

### Pose de mines {#sow-mines}

Il pose 4 / 6 / 8 (β / γ / δ) mines sur un anneau de 500 unités autour de l’endroit où se tenait sa cible. Une mine s’arme 3 s après être tombée, dure 30 s et explose une fois, sous le premier vaisseau de pilote qui passe dessus, pour 2 / 3 / 3 (β / γ / δ) des salves de l’alien. Une mine ne blesse jamais un alien.

- **Avertissement** : 1,5 s
- **Le mot au-dessus du vaisseau** : POSE DES MINES
- **Portée par** : les espèces lourdes (Bulwark, Goombah et Crystalys) et les chefs d’essaim lourds (Pirate Boss, Boss Phantasm, Boss Goombah et Boss Crystalys), à partir de β
- **Réponse** : Contournez-les : elles sont dessinées au sol, et elles s’arment tard.


<!-- mob-abilities:end -->

## Fragmentation {#splitting}

<!-- mob-split:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Les petits aliens du dernier palier peuvent se briser quand on les détruit trop vite. Cela concerne Seeker, Phantasm, Bulwark, Goombah et Crystalys du palier δ et aucun autre alien, et ce n’est pas l’une des capacités ci-dessus : un alien peut avoir les deux.

- **Quand** : un pilote le détruit dans les 5 s qui suivent le premier dégât qu’il a subi. Tous les aliens qui meurent aussi vite ne se brisent pas.
- **Ce qui en sort** : 3 aliens de la même espèce et du même palier, à 70 % de sa taille, chacun avec 25 % de sa coque et de son bouclier et une salve complète, autour de l’endroit où il a été détruit. Ils s’en prennent au pilote qui l’a détruit et partent après 180 s.
- **Ce sont des aliens ordinaires** : chacun paie ce que paie son espèce, lâche ce qu’elle lâche et compte pour les quêtes et les statistiques. Ils ne portent aucune capacité et ne se brisent jamais.
- **Limites** : au plus 60 fragments vivent sur une carte, et ils ne retardent pas les aliens propres de la carte.
- **Ce que cela signifie** : un équipage qui détruit ses aliens assez vite peut tirer jusqu’à 4 éliminations d’un seul alien. Un équipage qui n’y arrive pas n’en retire rien.

<!-- mob-split:end -->

## Les trois étapes des boss {#the-bosses-three-steps}

Chaque boss change sa façon de combattre en trois étapes : quand le combat commence, quand sa coque tombe sous les deux tiers et quand elle tombe sous un tiers. Une étape a lieu une fois et ne revient jamais en arrière, sauf si le boss recommence, comme dit plus bas.

<!-- mob-ladders:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **Une pause à chaque étape.** Quand une étape qui a quelque chose à faire commence après la première, le boss ne peut pas être blessé pendant 1,5 s (3 s pour le Seigneur de guerre du donjon et les boss des portes solo).
- **Et une capacité spéciale.** Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah et Boss Crystalys peuvent aussi porter une capacité spéciale (Dormant Force et Tesseract jamais) : elle vient entre la deuxième et la troisième étape ; si les deux devaient commencer ensemble, la plus tardive attend 3 s au plus. Ce n’est jamais une capacité que les propres étapes du chef utilisent.
- **Tout recommencer.** Le Tesseract recommence ses étapes dès qu’il s’est entièrement soigné.

### Les chefs d’essaim {#the-swarm-leaders}

| Chef | Au début | Sous les deux tiers | Sous un tiers |
| :--- | :--- | :--- | :--- |
| **Pirate Boss** | Tire un éventail de 3 roquettes, espacées de 12 degrés, sur le premier pilote qui l’a touché. | Appelle 5 Pirate Scouts de plus d’un coup, au plus 10 en vie. Ils ne paient rien et partent après 45 s. | Vole à vitesse ×1,8 vers la porte la plus proche pendant 10 s, puis se retourne contre les pilotes. |
| **Boss Seeker** | Ses Seeker Slaves le soignent ×2 plus vite pendant 8 s. | 2 copies de lui apparaissent, et le vrai porte un anneau. | S’éloigne des pilotes pendant 4 s, puis se retourne. |
| **Boss Phantasm** | Chacun de ses Phantasm Guards dresse une couche de bouclier de 10 % de sa propre coque. | 3 copies de lui apparaissent, et le vrai porte un anneau. | Saute à environ 2 500 unités des pilotes, et ses Phantasm Guards reviennent intacts autour de lui. |
| **Boss Goombah** | Ne prend que 50 % de chaque coup pendant 6 s. | Ses dégâts sont multipliés par ×1,5 et sa vitesse par ×1,25 pendant 10 s. | Se soigne de 25 % de sa coque et de son bouclier (une rafale de dégâts l’interrompt), et ses Goombah Guards le soignent ×2 plus vite pendant ce temps. |
| **Boss Crystalys** | Ne prend que 50 % de chaque coup pendant 8 s. | Un anneau de 700 unités frappe chaque vaisseau à l’intérieur avec 4 de ses salves, et il tire 4 roquettes. | Se soigne de 20 % de sa coque et de son bouclier (une rafale de dégâts l’interrompt), et 3 Crystalys Guards de plus arrivent, au plus 6 en vie. |
| **Dormant Force** | Ne prend que 70 % de chaque coup tant que l’un de ses Dormant Pulses est en vie. | Ses Dormant Pulses tirent une roquette toutes les 2,5 s pendant 15 s. | Tant que tous ses Dormant Pulses sont en vie, ils le soignent de 5 % de sa coque par seconde pendant 6 s. |
| **Tesseract** | – | 20 Facets de plus arrivent d’un coup, au-dessus de leur nombre habituel. | – |

### Les Gardiens de clan {#the-clan-wardens}

| Gardien | Au début | Sous les deux tiers | Sous un tiers |
| :--- | :--- | :--- | :--- |
| **Brood Warden** (I, II, III) | Les 4 drones viennent tous à son côté d’un coup. | Ses drones le soignent ×1,5 plus vite pendant 15 s. | 2 drones de plus arrivent, au-dessus de leur nombre habituel, pendant 30 s. Ils ne paient rien. |
| **Siege Warden** (I, II, III) | – | Tire sa roquette ×2 plus souvent pendant 20 s. | Se soigne de 15 % de sa coque et de son bouclier (une rafale de dégâts l’interrompt). |
| **Wrath Warden** (I, II, III) | – | Ses lasers frappent ×1,25 plus fort. | Ses lasers frappent ×1,5 plus fort en tout, sans s’ajouter à l’étape d’avant. |

### Le Seigneur de guerre du donjon {#the-dungeon-warlord}

- **Sous les deux tiers**: La pause entre ses capacités tombe à 4 s et leurs attentes à ×0,75.
- **Sous un tiers**: La pause tombe à 2 s, leurs attentes à ×0,5 et ses dégâts montent à ×1,25 ; il lance une salve de Meteor gratuite, et son Swarm ne revient jamais plus vite que toutes les 120 s.
- **Une pause à chaque étape.** Quand une étape commence, le Seigneur de guerre ne peut pas être blessé pendant 3 s.

### Les boss des portes solo {#the-solo-gate-bosses}

Les six boss des portes solo ont aussi trois étapes, leurs phases : elles sont dans le tableau [des boss](/wiki/03-Mechanics/Solo-Gates.md#the-bosses) de l’article des portes solo.

<!-- mob-ladders:end -->

## Pour aller plus loin {#where-to-read-more}

- [Combat](/wiki/03-Mechanics/Combat.md#who-an-alien-fights) : qui un alien combat, et qui obtient sa destruction.
- [Essaims](/wiki/05-Swarms/Swarms.md) : les chefs et leurs étapes, un article par essaim.
- [Warden de clan](/wiki/03-Mechanics/Clans.md#fighting-a-warden), le [Warlord du donjon](/wiki/03-Mechanics/Dungeons.md#the-warlord) et les [boss des portes solo](/wiki/03-Mechanics/Solo-Gates.md#the-bosses).
- [Guide du voyageur](/wiki/03-Mechanics/Travelers-Guide.md) : ce que vous avez appris d’un alien. Il ne dit jamais lequel porte une capacité.
