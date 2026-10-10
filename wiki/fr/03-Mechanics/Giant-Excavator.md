<!-- wiki-i18n source: 6b964707b3b7ca22 -->
<!-- wiki-i18n title: Excavatrice géante -->
# Excavatrice géante {#giant-excavator}

<!-- wiki-search: excavator; giant excavator; pulsar; mining; fuel; excavator fuel; control panel; overheat; radiation; slumbering void; voids; wave; ds-1; ds-2; ds-3; excavatrice; excavatrice géante; carburant; panneau de commande; surchauffe; vague -->

Dès le premier jour de la saison, un **pulsar** brille dans chacun des secteurs dangereux `DS-1`, `DS-2` et `DS-3`, et à partir du jour 11 de la saison une **excavatrice géante** se dresse à côté. L’excavatrice exploite le pulsar pour du **Thulium et des minerais rares**, et elle brûle de la [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md) pour cela. N’importe qui peut la ravitailler, choisir ce qu’elle extrait et la lancer, et tout ce qu’elle dépose repose autour d’elle dans des caisses que n’importe qui peut prendre. Une série est pourtant bruyante : le monde entier est prévenu quand elle commence, des **Slumbering Voids** viennent la prendre pour cible par vagues, et une excavatrice qu’on pousse trop longtemps surchauffe et irradie toute la zone. Cette page explique comment se déroule une série, ce qu’elle dépose et comment la survivre. Les secteurs sont dans [Secteurs dangereux](/wiki/01-General/Danger-Sectors.md) ; les Voids dans [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).

![The giant excavator's sheet: the fuel tank, the heat, the resource to mine, the excavator's hull and the Voids of the next wave](../../img/wiki-img/shots/excavator-sheet.jpg)

## En un coup d’œil {#at-a-glance}

<!-- excavator-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Où** : Un pulsar avec une excavatrice géante dans chacun des secteurs `DS-1`, `DS-2` et `DS-3`, dans tous les mondes
- **Apparition** : Le pulsar dès le premier jour de la saison, l’excavatrice dès le jour 11 de la saison jusqu’à la réinitialisation
- **Carburant** : Dark Matter. Une brûle 10 min ; le réservoir en contient 3, soit 30 min d’extraction. N’importe qui peut en ajouter une à la fois, depuis sa propre cargaison
- **Panneau** : La fenêtre fonctionne à moins de 600 unités de l’excavatrice, et son étiquette s’affiche dès 1 400 unités. N’importe qui peut ravitailler, choisir et lancer ; le choix est verrouillé tant qu’elle tourne
- **Caisses** : Une caisse toutes les 20 s, entre 450 et 900 unités de l’excavatrice, libre pour n’importe qui dès l’instant où elle tombe. Elle reste 5 min, et 24 au plus reposent en même temps sur une carte
- **Chaleur** : 30 min d’extraction, en autant de séries qu’il faut, et l’excavatrice surchauffe pendant 1 h. La chaleur est conservée entre les séries et disparaît après le repos
- **Radiation** : Tant qu’elle est en surchauffe ou détruite, l’excavatrice (à moins de 1 100 unités) et son pulsar (à moins de 1 300 unités) brûlent tout vaisseau à l’intérieur : 10 % de ses PV totaux chaque seconde
- **Coque** : 200 000 PV en Alpha, 300 000 en Bêta et 400 000 en Gamma. Seuls les Slumbering Voids peuvent l’endommager, et seulement quand plus aucun pilote ne la défend
- **Voids** : 2 Slumbering Voids toutes les 2 min pendant qu’elle extrait, les premiers 1 min après le lancement ; 8 au plus en vie sur une carte
- **Annonces** : Les pilotes du monde entier sont prévenus quand une série commence, quand l’excavatrice surchauffe et quand elle est détruite ; le reste va aux pilotes de son secteur. Ce sont des lignes Système : elles apparaissent dans l’onglet **Système** du chat et dans le Journal de jeu, et pas dans **Global** ni **Local**.

<!-- excavator-glance:end -->

## Comment se déroule une série {#how-a-run-goes}

1. **En trouver une.** À partir du jour 11 de la saison, chacun des trois secteurs dangereux qui ont un pulsar a une excavatrice, dans chaque monde. Une étiquette, **Excavatrice**, flotte au-dessus d’elle quand vous êtes proche, et la carte du Système stellaire marque chaque secteur dangereux qui en a une : la couleur de la marque est l’état de son excavatrice, et son infobulle indique le temps avant son prochain changement.
2. **Ouvrir le panneau.** Cliquez sur l’étiquette. La fenêtre **Excavatrice géante** fonctionne tant que votre vaisseau est à portée du panneau de l’excavatrice (la liste *En un coup d’œil* l’indique). Un vaisseau occulté peut l’utiliser, et l’utiliser ne met pas fin à l’occultation.
3. **La ravitailler.** **Ajouter de la Dark Matter** met une Dark Matter de votre cargaison dans le réservoir. N’importe qui peut le faire. Le réservoir n’en prend jamais plus que l’excavatrice ne peut en brûler avant de surchauffer, si bien qu’aucun carburant n’est gaspillé.
4. **Choisir ce qu’elle extrait** dans la liste, puis appuyer sur **Lancer l’extraction**. Il faut au moins une Dark Matter dans le réservoir et une ressource. N’importe qui peut changer le choix jusqu’au lancement ; une fois qu’elle tourne, la ressource est verrouillée. Le lancement est annoncé à tous les pilotes du monde, avec votre nom, le secteur et la ressource.
5. **La tenir.** Pendant qu’elle extrait, une caisse tombe autour de l’excavatrice toutes les quelques secondes, et les premiers Slumbering Voids arrivent peu après le lancement. Défendez l’excavatrice et prenez les caisses.
6. **Surveiller la chaleur.** La barre de Chaleur se remplit pendant que l’excavatrice extrait et ne se vide jamais pendant qu’elle attend. À sa limite, l’excavatrice surchauffe. Partez avant : le jeu avertit la carte deux fois.
7. **Elle se repose.** Surchauffée ou détruite, l’excavatrice et son pulsar sont irradiés jusqu’à la fin du repos ; puis elle est de nouveau prête, avec sa chaleur remise à zéro et sa coque pleine.

La fenêtre montre aussi le secteur, le réservoir (une cellule par Dark Matter, celle qui brûle dessinée en partie), la Dark Matter que vous transportez, la coque de l’excavatrice, ce que chaque ressource dépose par minute dans votre monde et, pendant qu’elle extrait, le temps avant la prochaine vague et les Voids en vie. Quand quelque chose est refusé, vous lisez la raison en rouge : vous êtes trop loin du panneau, vous n’avez pas de Dark Matter, le réservoir est plein, il n’y a pas encore de carburant ou de ressource choisie, la ressource est verrouillée tant qu’elle tourne, ou l’excavatrice est en surchauffe.

| État | Ce que c’est | Ce que vous pouvez faire |
| :--- | :--- | :--- |
| **Prête** | Sans carburant, ou avec du carburant et pas lancée. La chaleur accumulée est conservée. | Ajouter de la Dark Matter, choisir, lancer. |
| **En extraction** | Elle brûle de la Dark Matter et accumule de la chaleur ; la ressource est verrouillée. | Ajouter de la Dark Matter jusqu’à la place restante, combattre les Voids, prendre les caisses. |
| **Surchauffée** | La chaleur a atteint sa limite. Le réservoir est vidé ; les caisses déjà déposées restent. | Rien. La zone est irradiée : restez dehors. |
| **Détruite** | Les Voids ont amené la coque à zéro. Le carburant est perdu, la coque est de nouveau pleine aussitôt. | Rien. La zone est irradiée : restez dehors. |

Si le carburant s’épuise avant la limite, l’excavatrice revient à **Prête** avec sa chaleur conservée, et les Voids qui restent partent au bout d’un moment, sauf s’ils combattent.

## Ce qu’elle extrait {#what-it-mines}

Un réservoir plein dépose à peu près ce que gagneraient cinq pilotes en une demi-heure du meilleur farm de Thulium. Bêta et Gamma déposent davantage, comme ils paient davantage pour chaque élimination. Vous choisissez une ressource par série. Une caisse est la même pour tous, et une caisse de Thulium est de l’argent comptant qui est versé au ramassage, comme le Thulium des astéroïdes.

<!-- excavator-resources:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Un réservoir plein (3 Dark Matter, 30 min d’extraction) dépose les quantités ci-dessous, en 90 caisses.

| Ressource | Alpha | Beta | Gamma | Une minute, en Alpha | Une caisse, en Alpha |
| :--- | ---: | ---: | ---: | ---: | ---: |
| [Thulium](/wiki/06-Items/Resources.md#thulium) | 9 643 | 15 429 | 19 286 | 321,4 | 107,1 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | 2 314 | 3 703 | 4 629 | 77,1 | 25,7 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | 1 029 | 1 646 | 2 057 | 34,3 | 11,4 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | 640 | 640 | 640 | 21,3 | 7,1 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | 320 | 320 | 320 | 10,7 | 3,6 |

- Une série de Velkonite ou de Orvium dépose au plus 8 heures d’un collecteur de niveau 20 du [Skylab](/wiki/03-Mechanics/Skylab.md) pour ce minerai (640 Velkonite, 320 Orvium), dans tous les mondes : ce sont les minerais du Skylab, et une série n’accélère jamais son rythme de plus que cela.
- Une caisse contient à peu près la quantité de la dernière colonne, à 15 % près. Une caisse de Thulium est de l’argent comptant : le ramassage la verse. Une caisse de minerai contient l’objet.

<!-- excavator-resources:end -->

Les boosters du pilote agissent comme pour toute cargaison : le bonus du Resource Magnet Booster augmente une caisse de minerai. Il n’y a pas de limite quotidienne sur les caisses : le carburant et l’horloge limitent une série.

**À quoi sert le minerai.** Le minerai d’une caisse va dans votre cargaison comme n’importe quel objet. La Cataclysite et la Quorvium servent à l’Assemblage et à la Forge ([Ressources](/wiki/06-Items/Resources.md)). La Fonderie et le Centre de recherche du Skylab ne prennent la Velkonite et l’Orvium que dans l’Entrepôt de ressources, que remplissent les collecteurs ; le minerai d’une caisse ne sert donc à rien dans votre cargaison : posez votre vaisseau, et la [Baie à minerai](/wiki/03-Mechanics/Skylab.md#ore-bay) de votre Skylab (Noyau au niveau 10) le verse dans l’entrepôt, dans la limite de son quota par heure, d’où la Fonderie et le [Centre de recherche](/wiki/03-Mechanics/Research.md#fuel) le prennent.

## Les Slumbering Voids {#the-slumbering-voids}

Une série attire des **Slumbering Voids**, des chasseurs de la civilisation perdue qui arrivent en volant du bord de la carte pour protéger le pulsar de quiconque voudrait le vider. Ils traquent les pilotes près de l’excavatrice, et quand il n’y a plus personne à traquer, ils s’en prennent à l’excavatrice. Les chiffres du Void et son gain sont dans [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).

<!-- excavator-voids:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Vagues.** 2 Slumbering Voids toutes les 2 min ; les premiers 1 min après le lancement, et aucun dans les 1 min finales d’une série. 8 au plus sont en vie en même temps sur une carte : une vague qui trouve la carte pleine est sautée.
- **Arrivée.** Une vague apparaît au bord de la carte, à 900 unités vers l’intérieur et à au moins 2 500 unités de tout anneau de porte, et vole jusqu’à l’excavatrice en 20 s environ. Le message nomme le côté de la carte d’où elle vient.
- **Chasse.** Un Void traque le pilote le plus proche qu’il peut voir à moins de 2 500 unités, et reste à moins de 7 000 unités de l’excavatrice.
- **Siège.** Quand aucun pilote visible ne se trouve à moins de 7 000 unités de l’excavatrice pendant 15 s, les Voids attaquent l’excavatrice, et chaque laser inflige 25 % de ses dégâts habituels. À zéro, l’excavatrice est détruite : son carburant est perdu, sa coque est de nouveau pleine aussitôt, et elle se repose 1 h.
- **Départ.** Quand une série se termine, les Voids restants demeurent 90 s de plus et combattent encore si on les combat ; puis ils s’en vont.

<!-- excavator-voids:end -->

- **Un Void est un canon de verre.** Son bouclier est grand mais absorbe 80 % d’un coup, si bien que la coque derrière lui est partie après quelques fois sa taille en dégâts, et bien plus tôt avec de la pénétration de bouclier. Deux ou trois pilotes bien équipés tiennent une série en Alpha ; Bêta et Gamma demandent de plus grands groupes, comme pour tout alien.
- **Une occultation ne défend pas le site.** Les Voids ne voient pas les vaisseaux occultés, donc un pilote qui se cache ne les éloigne pas de l’excavatrice ; et un pilote qui s’abrite dans un anneau de porte ne peut pas être atteint et ne compte pas non plus.
- **Chaque Void paie,** selon les dégâts que vous lui avez infligés, et lâche une caisse ([comment paie l’élimination d’un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Leurs éliminations s’ajoutent à vos points PvE de grade comme celles d’un vaisseau d’essaim.

## Chaleur et radiation {#heat-and-radiation}

L’extraction ajoute de la chaleur seconde après seconde. La chaleur est **cumulative et ne refroidit jamais tant que l’excavatrice attend** : une série qui s’arrête tôt laisse au pilote suivant une série plus courte. Quand elle atteint la limite, l’excavatrice **surchauffe**, et quand sa coque est ramenée à zéro, elle est **détruite** ; dans les deux cas l’excavatrice et son pulsar irradient jusqu’à la fin du repos.

<!-- excavator-radiation:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

| Cercle | Rayon | PV totaux par seconde | Un vaisseau plein tient |
| :--- | ---: | ---: | ---: |
| L’excavatrice géante | 1 100 | 10 % | 10 s |
| Le pulsar | 1 300 | 10 % | 10 s |

- **La dose.** 10 % des PV maximum totaux d’un vaisseau (coque plus bouclier) chaque seconde, donc un vaisseau plein tient 10 s, quelle que soit sa classe. Le bouclier la reçoit en premier et son absorption ne compte pas.
- **Qui.** Tout vaisseau dans les cercles, occultés compris ; aucun alien. C’est du dégât subi : un Drone de réparation s’arrête et le bouclier ne se recharge pas, comme au trou noir.
- **Crédit.** Un pilote qui meurt brûlé est crédité au dernier ennemi qui l’a touché dans les 15 s précédentes.
- **Avertissements.** La carte est prévenue 1 min et 15 s avant la surchauffe.

<!-- excavator-radiation:end -->

- **L’avertissement.** Deux fois avant la surchauffe (les durées sont dans la liste ci-dessus), la carte est prévenue, un vaisseau dans les cercles voit un avertissement, et les cercles sont dessinés au sol en vol et sur la minicarte. Quand ils irradient, les cercles sont rouges et la jauge de Radiation montre la dose.
- **Partir.** Tout vaisseau de série peut sortir depuis le bord du panneau ou depuis la caisse la plus éloignée encore là, sauf l’Ironclad, qui est lent : il part pendant l’avertissement, ou il ne part pas. Ne restez pas sur une caisse quand la chaleur arrive à sa limite.
- **Le butin dans les cercles.** Les caisses déposées avant la surchauffe restent, dans la radiation : une caisse qui s’y trouve quand elle commence se prend au prix de la dose.
- **Le redémarrage du serveur** met une série en pause : le carburant et la chaleur reviennent comme ils étaient, le repos continue selon l’horloge, et la première vague après le redémarrage arrive une minute plus tard.

## Se battre pour une série {#fighting-over-a-run}

L’excavatrice n’a **aucun anneau spécial** : les règles normales de votre monde s’appliquent, donc des rivaux peuvent venir, vous tirer dessus et prendre les caisses (une caisse est libre pour n’importe qui dès l’instant où elle tombe). Voler et tendre des embuscades fait partie de l’événement. Quelques points à prévoir :

- **Qui ravitaille n’est pas qui gagne.** N’importe qui peut ravitailler, choisir et lancer ; un rival peut changer la ressource avant que vous appuyiez sur Lancer. Vérifiez le choix avant d’appuyer.
- **Le carburant est en danger.** Si l’excavatrice est détruite, la Dark Matter de son réservoir est perdue, et personne ne la récupère. Le plus que l’on puisse perdre est le réservoir plein.
- **Venez en groupe** et décidez qui reste près de l’excavatrice et qui prend les caisses, et gardez un œil sur la chaleur : les pilotes qui prennent les dernières caisses sont ceux que la radiation attrape.
- **Les Voids viennent à l’excavatrice, pas aux caisses.** Un groupe qui tient l’excavatrice occupe les Voids ; celui qui s’éloigne la laisse au siège.

## Ce que le monde apprend {#what-the-world-is-told}

Ce sont des lignes Système (elles s’affichent dans l’onglet **Système** du chat et dans le Journal de jeu, et pas dans **Global** ni **Local**). Les trois premières vont au monde entier ; la dernière aux pilotes du secteur de l’excavatrice.

- Le jour où l’événement 2 commence : les secteurs dangereux ont changé.
- Un pilote **lance** une excavatrice, avec le secteur, la ressource et les minutes de carburant.
- L’excavatrice **surchauffe**, ou est **détruite**.
- Le carburant s’épuise ; l’excavatrice va surchauffer (deux avertissements) ; une **vague** de Voids arrive, avec son numéro et le côté de la carte d’où elle vient ; plus aucun pilote ne reste, alors les Voids attaquent l’excavatrice.

Chaque action du panneau et chaque avertissement a un son discret bien à lui, au volume des effets.

## Pour en savoir plus {#where-to-read-more}

- [Secteurs dangereux](/wiki/01-General/Danger-Sectors.md) : où se trouvent les pulsars et ce qu’il y a d’autre de nouveau.
- [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) : le Slumbering Void, l’Inert Mass et l’Unwakened.
- [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md) et [Le trou noir](/wiki/03-Mechanics/Black-Hole.md) : d’où vient le carburant.
- [Ressources](/wiki/06-Items/Resources.md) : les minerais que dépose l’excavatrice.
- [Caisses de cargaison](/wiki/03-Mechanics/Cargo.md) : caisses, ramassage et le Resource Magnet Booster.
- [Grades](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points) : les points PvE d’un Void.
