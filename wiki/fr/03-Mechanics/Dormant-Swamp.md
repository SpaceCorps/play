<!-- wiki-i18n source: 3c07d568f3af3aab -->
<!-- wiki-i18n title: Dormant Swamp -->
# Dormant Swamp

<!-- wiki-search: swamp; dormant swamp; base; turret; turrets; nike turret; laser turret; inert mass; unwakened; the unwakened; slumbering void; void; dormant lance; ds-4; marais; tourelle; tourelles; canon; canons -->

Il y a très longtemps, une civilisation avancée a vécu au milieu de la galaxie. Elle bâtissait en cristal noir violacé, aux veines violettes qui luisent, et pour une raison que personne ne connaît, elle s’est effondrée. Le **Dormant Swamp** est son avant-poste, dans le coin supérieur gauche de `DS-4`. À partir du jour 11 de la saison, il s’agite : des canons au milieu tirent sur tout vaisseau qu’ils voient, des **Inert Masses** le gardent, et tout au milieu dort **l’Unwakened**. Sous occultation, vous pouvez voler jusqu’à l’Unwakened. Depuis l’ouverture du [Deep Void](/wiki/03-Mechanics/Deep-Void.md), les canons et l’Unwakened peuvent être détruits, et la première mise à mort de l’Unwakened de la saison ouvre, dans chaque monde, le Threshold de ce monde. La base elle-même ne peut être ni pénétrée, ni abordée, ni utilisée pour commercer.

Le marais est aussi l’endroit où l’[Essaim Dormant](/wiki/05-Swarms/Dormant-Swarm.md) apparaît à partir du jour 11, et des **Slumbering Voids** patrouillent autour. Les mêmes Voids viennent par vagues aux [excavatrices géantes](/wiki/03-Mechanics/Giant-Excavator.md#the-slumbering-voids). Les secteurs sont dans [Secteurs dangereux](/wiki/01-General/Danger-Sectors.md).

![Flying in towards the Dormant Swamp: the amber notice ring and, inside it, the red ring of the zone the guns reach](../../img/wiki-img/shots/swamp-rings.jpg)

## En un coup d’œil {#at-a-glance}

<!-- swamp-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Où** : Le coin supérieur gauche de `DS-4` : le milieu est en 5 000 / 5 000
- **Apparition** : Du jour 11 de la saison jusqu’à la réinitialisation
- **La zone** : 4 300 unités autour du milieu : la portée maximale des canons
- **L’avertissement** : Un vaisseau qui franchit l’anneau à 4 800 unités du milieu reçoit une ligne Système
- **Occultation** : Aucun canon ne voit jamais un vaisseau occulté, ni un vaisseau dans la fenêtre d’un EMP
- **Les aliens** : 5 Inert Masses restent à moins de 2 400 unités du milieu. L’Unwakened dort au milieu. 2 Slumbering Voids patrouillent entre 4 600 et 6 500 unités du milieu.
- **L’Essaim Dormant** : Il apparaît en 9 417 / 6 606, à 4 700 unités du milieu et hors de la zone
- **Roches** : Aucun astéroïde ne se trouve à moins de 4 900 unités du milieu

<!-- swamp-glance:end -->

## Les canons {#the-guns}

Les tourelles du marais tirent sur le **vaisseau le plus proche qu’elles peuvent voir** dans leur portée, et sur aucun autre : la zone est le cercle qu’atteint la plus lointaine d’entre elles. Ce ne sont pas des vaisseaux, mais depuis l’ouverture du Deep Void chacune a des points de vie : cliquez sur une tourelle pour tirer vos lasers dessus, et une roquette qui éclate près d’elle l’endommage aussi. Une tourelle détruite le reste jusqu’au retour de l’Unwakened. Leurs tirs sont réels, et le monde met leurs dégâts à l’échelle comme il le fait pour l’arme de n’importe quel alien.

<!-- swamp-guns:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Dégâts d’un tir, dans chaque monde :

| Canon | Lieu | Tire toutes les | Portée (unités) | Alpha | Beta | Gamma |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| Tourelle de [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | 5 000 / 4 400 | 2 s | 3 640 | 75 000 | 112 500 | 150 000 |
| Tourelle de [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | 5 000 / 4 400 | 5 s | 1 080 | 50 000 | 75 000 | 100 000 |
| Tourelle laser × 2 | 3 600 / 5 200; 6 400 / 5 200 | 1 s | 2 500 | 45 000–55 000 | 67 500–82 500 | 90 000–110 000 |

- Une roquette est tirée à 82 % de la portée que la même roquette a entre les mains d’un pilote, pour qu’elle arrive ; une tourelle laser tire une fois par seconde, et ses dégâts sont tirés au sort dans la plage indiquée.
- Un N.I.K.E. a 35 % de pénétration de bouclier, retranchée de l’absorption d’un bouclier.
- Le N.I.K.E. de la tourelle vole 25 % plus vite et 2× plus loin que le vôtre : 1 250 unités par seconde, 8 910 unités en tout, si bien qu’un vaisseau qui le fuit est poursuivi très loin.
- Un N.U.K.E. éclate sur un rayon de 1 013 unités, avec le plus de force au centre.
- Le N.U.K.E. de la tourelle vole 25 % plus vite et 2× plus loin que le vôtre : 375 unités par seconde, 2 640 unités en tout, si bien qu’un vaisseau qui le fuit est poursuivi très loin.

<!-- swamp-guns:end -->

- **Rien ne tire depuis l’extérieur de la zone,** et à l’intérieur un vaisseau est détruit en quelques secondes : plus il s’approche du milieu, plus de canons s’ajoutent, et même le Wraith le mieux protégé ne tient pas. Une roquette déjà en l’air continue sa route, cependant, et celles de la tourelle volent plus vite et plus loin que les vôtres : fuir droit devant l’une d’elles ne vous en débarrasse pas.
- **Une occultation vous fait entrer.** Aucune tourelle ne voit jamais un vaisseau occulté, ni un vaisseau dans la fenêtre d’un EMP, à aucune distance. Une explosion visant un vaisseau visible qui éclate près d’un vaisseau occulté le blesse quand même et met fin à son occultation.
- **Elles ne tirent que sur les pilotes,** jamais sur les aliens, les pilotes de corporation ni l’essaim, et la protection d’un vaisseau qui vient de revenir d’une destruction tient aussi contre elles.
- **L’anneau d’avertissement.** Un vaisseau qui franchit l’anneau en dehors de la zone reçoit une ligne Système : les tourelles tirent sur tout vaisseau qu’elles voient, et quelque chose dort au milieu. Il n’est prévenu de nouveau que lorsqu’il a quitté l’anneau et y est revenu.
- **En sortir.** Si vous êtes détruit là-bas, vous ne pouvez pas revenir sur place (un secteur dangereux ne propose que la base et le portail le plus proche), et si vous vous connectez dans la zone, vous êtes mis dehors. Un cap que vous cliquez est infléchi autour de la zone, et une alerte vous prévient quand l’endroit cliqué s’y trouve.

## Les aliens {#the-aliens}

Trois aliens de la civilisation perdue vivent ici, chacun avec ses propres chiffres. Ils sont payés comme le boss d’un essaim : **selon les dégâts infligés**, à chaque pilote qui en a fait au moins la part indiquée dans [Essaims](/wiki/05-Swarms/Swarms.md#the-rules-of-every-swarm), et la caisse va au pilote qui a infligé le plus de dégâts. Leurs éliminations s’ajoutent à vos points PvE de grade comme celles d’un vaisseau d’essaim, en proportion de leur gain ([Grades](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points)). Le bouclier de chacun absorbe {{guide:vitals.absorbance@Slumbering Void;Inert Mass;The Unwakened}} de chaque coup tant qu’il tient ([Boucliers](/wiki/03-Mechanics/Shields.md)).

- **Slumbering Void.** Le chasseur élancé, l’alien le plus rapide du jeu (plus rapide qu’un Storm avec Afterburner III). Certains patrouillent toujours aux abords du marais, et d’autres arrivent par vagues aux excavatrices. Il est agressif, traque le pilote le plus proche qu’il peut voir et ne voit jamais un vaisseau occulté.
- **Inert Mass.** Une carcasse morte aux fissures violettes, de la taille d’une petite station. Elles restent à une distance fixe du milieu du marais et ne le quittent pas pour l’instant. Elle tire des **Dormant Lances** : des roquettes guidées à très longue portée qui suivent un vaisseau jusqu’à ce qu’il s’occulte, ouvre une fenêtre d’EMP, entre dans un anneau sûr, saute ou meure. Elle est plus rapide que n’importe quel vaisseau, donc seules ces ruptures aident. Un astéroïde sur la trajectoire d’une Dormant Lance l’arrête, et la Lance l’endommage de son propre dégât (personne n’est payé pour cela) ; un rocher ne protège donc d’une Inert Mass que pour quelques coups.
- **L’Unwakened.** Un monolithe qui dort au milieu du marais, la plus grande chose de toutes les cartes, si lent qu’il n’attrape jamais un vaisseau. Il ne tire rien, mais tout vaisseau dans son aura brûle, **occulté ou non**. Depuis l’ouverture du [Deep Void](/wiki/03-Mechanics/Deep-Void.md), il peut être détruit : il paie selon les dégâts infligés, revient un jour après sa mort, et dans chaque monde la première mise à mort de la saison ouvre le Threshold de ce monde. La **Technique de radiation** d’un pilote réduit sa brûlure, jusqu’à 0,40 de celle-ci au niveau 100.

<!-- swamp-members:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

### Slumbering Void

2 Slumbering Voids patrouillent entre 4 600 et 6 500 unités du milieu du marais ; un qui est détruit revient {{guide:vitals.respawn@Slumbering Void}} plus tard. Les vagues d’une excavatrice amènent d’autres du même alien.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | {{guide:vitals.hull@Slumbering Void}} | {{guide:vitals.hull*1.5@Slumbering Void}} | {{guide:vitals.hull*2@Slumbering Void}} |
| Bouclier | {{guide:vitals.shield@Slumbering Void}} | {{guide:vitals.shield*1.5@Slumbering Void}} | {{guide:vitals.shield*2@Slumbering Void}} |
| Absorption du bouclier | {{guide:vitals.absorbance@Slumbering Void}} | {{guide:vitals.absorbance@Slumbering Void}} | {{guide:vitals.absorbance@Slumbering Void}} |
| Dégâts des lasers (une salve par seconde) | {{guide:vitals.dps@Slumbering Void}} | {{guide:vitals.dps*1.5@Slumbering Void}} | {{guide:vitals.dps*2@Slumbering Void}} |
| Vitesse | {{guide:vitals.speed@Slumbering Void}} | {{guide:vitals.speed@Slumbering Void}} | {{guide:vitals.speed@Slumbering Void}} |
| Portée des lasers | 800 | 800 | 800 |
| Rayon d’aggro | {{guide:vitals.aggro@Slumbering Void}} | {{guide:vitals.aggro@Slumbering Void}} | {{guide:vitals.aggro@Slumbering Void}} |
| Crédits | {{guide:spoils.pay.credits@Slumbering Void}} | {{guide:spoils.pay.credits*2@Slumbering Void}} | {{guide:spoils.pay.credits*3@Slumbering Void}} |
| Thulium | {{guide:spoils.pay.thulium@Slumbering Void}} | {{guide:spoils.pay.thulium*2@Slumbering Void}} | {{guide:spoils.pay.thulium*3@Slumbering Void}} |
| Expérience (XP) | {{guide:spoils.pay.experience@Slumbering Void}} | {{guide:spoils.pay.experience*2@Slumbering Void}} | {{guide:spoils.pay.experience*3@Slumbering Void}} |
| Honneur | {{guide:spoils.pay.honor@Slumbering Void}} | {{guide:spoils.pay.honor*2@Slumbering Void}} | {{guide:spoils.pay.honor*3@Slumbering Void}} |
| Points PvE par élimination | 10 | 10 | 10 |

**Butin** : une caisse, pour le pilote qui a infligé le plus de dégâts.

| Objet |
| :--- |
| {{guide:spoils.box@Slumbering Void}} |

### Inert Mass

5 Inert Masses se tiennent à moins de 2 400 unités du milieu ; une qui est détruite revient {{guide:vitals.respawn@Inert Mass}} plus tard. Tire toutes les 6 s une [Dormant Lance](/wiki/06-Items/Rockets.md#the-craft-only-rockets) guidée sur le vaisseau le plus proche qu’elle peut voir : vitesse 750, un vol de 5 250 unités, 40 % de pénétration.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | {{guide:vitals.hull@Inert Mass}} | {{guide:vitals.hull*1.5@Inert Mass}} | {{guide:vitals.hull*2@Inert Mass}} |
| Bouclier | {{guide:vitals.shield@Inert Mass}} | {{guide:vitals.shield*1.5@Inert Mass}} | {{guide:vitals.shield*2@Inert Mass}} |
| Absorption du bouclier | {{guide:vitals.absorbance@Inert Mass}} | {{guide:vitals.absorbance@Inert Mass}} | {{guide:vitals.absorbance@Inert Mass}} |
| Dégâts de chaque Dormant Lance | {{guide:behaviour.ability:rocket.damageMin@Inert Mass}}–{{guide:behaviour.ability:rocket.damage@Inert Mass}} | {{guide:behaviour.ability:rocket.damageMin*1.5@Inert Mass}}–{{guide:behaviour.ability:rocket.damage*1.5@Inert Mass}} | {{guide:behaviour.ability:rocket.damageMin*2@Inert Mass}}–{{guide:behaviour.ability:rocket.damage*2@Inert Mass}} |
| Vitesse | {{guide:vitals.speed@Inert Mass}} | {{guide:vitals.speed@Inert Mass}} | {{guide:vitals.speed@Inert Mass}} |
| Portée des roquettes | 5 000 | 5 000 | 5 000 |
| Rayon d’aggro | {{guide:vitals.aggro@Inert Mass}} | {{guide:vitals.aggro@Inert Mass}} | {{guide:vitals.aggro@Inert Mass}} |
| Crédits | {{guide:spoils.pay.credits@Inert Mass}} | {{guide:spoils.pay.credits*2@Inert Mass}} | {{guide:spoils.pay.credits*3@Inert Mass}} |
| Thulium | {{guide:spoils.pay.thulium@Inert Mass}} | {{guide:spoils.pay.thulium*2@Inert Mass}} | {{guide:spoils.pay.thulium*3@Inert Mass}} |
| Expérience (XP) | {{guide:spoils.pay.experience@Inert Mass}} | {{guide:spoils.pay.experience*2@Inert Mass}} | {{guide:spoils.pay.experience*3@Inert Mass}} |
| Honneur | {{guide:spoils.pay.honor@Inert Mass}} | {{guide:spoils.pay.honor*2@Inert Mass}} | {{guide:spoils.pay.honor*3@Inert Mass}} |
| Points PvE par élimination | 15 | 15 | 15 |

**Butin** : une caisse, pour le pilote qui a infligé le plus de dégâts.

| Objet |
| :--- |
| {{guide:spoils.box@Inert Mass}} |

### The Unwakened

Il y en a un, au milieu du marais et nulle part ailleurs ; il revient {{guide:vitals.respawn@The Unwakened}} après sa destruction. Depuis l’ouverture du Deep Void, il peut être détruit, et il paie selon les dégâts infligés comme les autres aliens d’ici.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | {{guide:vitals.hull@The Unwakened}} | {{guide:vitals.hull*1.5@The Unwakened}} | {{guide:vitals.hull*2@The Unwakened}} |
| Bouclier | {{guide:vitals.shield@The Unwakened}} | {{guide:vitals.shield*1.5@The Unwakened}} | {{guide:vitals.shield*2@The Unwakened}} |
| Absorption du bouclier | {{guide:vitals.absorbance@The Unwakened}} | {{guide:vitals.absorbance@The Unwakened}} | {{guide:vitals.absorbance@The Unwakened}} |
| Dégâts de l’aura par seconde, à tout vaisseau à l’intérieur | {{guide:behaviour.ability:aura.damagePerSecond@The Unwakened}} | {{guide:behaviour.ability:aura.damagePerSecond*1.5@The Unwakened}} | {{guide:behaviour.ability:aura.damagePerSecond*2@The Unwakened}} |
| Rayon de l’aura | 700 | 700 | 700 |
| Vitesse | {{guide:vitals.speed@The Unwakened}} | {{guide:vitals.speed@The Unwakened}} | {{guide:vitals.speed@The Unwakened}} |
| Rayon d’aggro | {{guide:vitals.aggro@The Unwakened}} | {{guide:vitals.aggro@The Unwakened}} | {{guide:vitals.aggro@The Unwakened}} |
| Crédits | {{guide:spoils.pay.credits@The Unwakened}} | {{guide:spoils.pay.credits*2@The Unwakened}} | {{guide:spoils.pay.credits*3@The Unwakened}} |
| Thulium | {{guide:spoils.pay.thulium@The Unwakened}} | {{guide:spoils.pay.thulium*2@The Unwakened}} | {{guide:spoils.pay.thulium*3@The Unwakened}} |
| Expérience (XP) | {{guide:spoils.pay.experience@The Unwakened}} | {{guide:spoils.pay.experience*2@The Unwakened}} | {{guide:spoils.pay.experience*3@The Unwakened}} |
| Honneur | {{guide:spoils.pay.honor@The Unwakened}} | {{guide:spoils.pay.honor*2@The Unwakened}} | {{guide:spoils.pay.honor*3@The Unwakened}} |
| Points PvE par élimination | 112 | 112 | 112 |

**Butin** : une caisse, pour le pilote qui a infligé le plus de dégâts.

| Objet |
| :--- |
| {{guide:spoils.box@The Unwakened}} |

<!-- swamp-members:end -->

## Avec le Deep Void {#with-the-deep-void}

Ce que le Deep Void a changé ici, en bref :

- **L’Unwakened peut être détruit.** Il n’est plus invulnérable : il paie selon les dégâts infligés, comme les autres aliens d’ici, et revient un jour après sa mort.
- **Les canons peuvent être détruits.** Chacun des trois canons (la tourelle de roquettes, qui tire à la fois la N.I.K.E. et la N.U.K.E., et les deux tourelles laser) a maintenant des points de vie, et les lasers comme les roquettes les endommagent. Un canon détruit le reste jusqu’au retour de l’Unwakened.
- **La première mise à mort ouvre le Threshold.** Dans chaque monde, la première mise à mort de l’Unwakened de la saison ouvre le Threshold de ce monde dans le coin opposé de `DS-4`, là où commence le [Deep Void](/wiki/03-Mechanics/Deep-Void.md).

## Que faire ici {#what-to-do-here}

- **La première mise à mort ouvre la voie.** La première mise à mort de l’Unwakened de la saison ouvre le Threshold de son monde et, avec lui, la voie vers le [Deep Void](/wiki/03-Mechanics/Deep-Void.md) ; dans la zone, les canons détruisent un vaisseau en quelques secondes. Hors de la zone, les Voids en patrouille, dans un anneau autour de la zone, sont la première ligne du marais et l’endroit où un groupe peut se battre sans les canons.
- **Combattez les Voids avec de la pénétration.** Le grand bouclier d’un Void absorbe {{guide:vitals.absorbance@Slumbering Void;Inert Mass;The Unwakened}} d’un coup et compte presque pour rien : la coque derrière est petite. Plus vos lasers ont de pénétration de bouclier, plus vite il tombe ([Lasers et munitions](/wiki/06-Items/Lasers.md)).
- **Restez hors des Lances.** Une Inert Mass voit loin et on ne distance pas une Lance : rompez son emprise par une occultation, un EMP, un anneau sûr ou un saut, ou quittez sa portée. Une Mass est un long combat, même pour un grand groupe des vaisseaux les plus puissants.
- **L’Essaim Dormant** apparaît désormais juste hors de la zone, si bien qu’un groupe peut l’attendre sans les canons. Voir [Essaim Dormant](/wiki/05-Swarms/Dormant-Swarm.md).

## Pour en savoir plus {#where-to-read-more}

- [Secteurs dangereux](/wiki/01-General/Danger-Sectors.md) : ce qui a changé au jour 11.
- [Excavatrice géante](/wiki/03-Mechanics/Giant-Excavator.md) : les vagues de Slumbering Voids et ce qu’elles gardent.
- [Essaims](/wiki/05-Swarms/Swarms.md) et [Essaim Dormant](/wiki/05-Swarms/Dormant-Swarm.md) : comment paie l’élimination d’un boss.
- [Roquettes](/wiki/06-Items/Rockets.md#the-craft-only-rockets) : le N.I.K.E. et le N.U.K.E. que tire la tourelle.
- [Trou noir](/wiki/03-Mechanics/Black-Hole.md) : l’autre danger de `DS-4`.
- [Caisses de cargaison](/wiki/03-Mechanics/Cargo.md) : les caisses que lâchent les aliens.
