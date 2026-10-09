<!-- wiki-i18n source: a8a96edb9a5070f1 -->
<!-- wiki-i18n title: Dormant Swamp -->
# Dormant Swamp

<!-- wiki-search: swamp; dormant swamp; base; turret; turrets; nike turret; laser turret; inert mass; unwakened; the unwakened; slumbering void; void; dormant lance; ds-4; marais; tourelle; tourelles; canon; canons -->

Il y a très longtemps, une civilisation avancée a vécu au milieu de la galaxie. Elle bâtissait en cristal noir violacé, aux veines violettes qui luisent, et pour une raison que personne ne connaît, elle s’est effondrée. Le **Dormant Swamp** est son avant-poste, dans le coin supérieur gauche de `DS-4`. À partir du jour 11 de la saison, il s’agite : des canons au milieu tirent sur tout vaisseau qu’ils voient, des **Inert Masses** le gardent, et tout au milieu dort **l’Unwakened**. C’est un endroit que les pilotes **ne sont pas encore censés visiter**. Sous occultation, vous pouvez voler jusqu’à l’Unwakened, et rien d’autre ne peut y être fait pour l’instant : la base et ses canons ne peuvent être ni endommagés, ni pénétrés, ni abordés, ni utilisés pour commercer.

Le marais est aussi l’endroit où l’[Essaim Dormant](/wiki/05-Swarms/Dormant-Swarm.md) apparaît à partir du jour 11, et des **Slumbering Voids** patrouillent autour. Les mêmes Voids viennent par vagues aux [excavatrices géantes](/wiki/03-Mechanics/Giant-Excavator.md#the-slumbering-voids). Les secteurs sont dans [Secteurs dangereux](/wiki/01-General/Danger-Sectors.md).

## En un coup d’œil {#at-a-glance}

<!-- swamp-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Où** : Le coin supérieur gauche de `DS-4` : le milieu est en 5 000 / 5 000
- **Apparition** : Du jour 11 de la saison jusqu’à la réinitialisation
- **La zone** : 4 300 unités autour du milieu : la portée maximale des canons, et l’endroit que personne n’est encore censé visiter
- **L’avertissement** : Un vaisseau qui franchit l’anneau à 4 800 unités du milieu reçoit une ligne Système
- **Occultation** : Aucun canon ne voit jamais un vaisseau occulté, ni un vaisseau dans la fenêtre d’un EMP
- **Les aliens** : 5 Inert Masses restent à moins de 2 400 unités du milieu. L’Unwakened dort au milieu. 2 Slumbering Voids patrouillent entre 4 600 et 6 500 unités du milieu.
- **L’Essaim Dormant** : Il apparaît en 9 417 / 6 606, à 4 700 unités du milieu et hors de la zone
- **Roches** : Aucun astéroïde ne se trouve à moins de 4 900 unités du milieu

<!-- swamp-glance:end -->

## Les canons {#the-guns}

Les tourelles du marais tirent sur le **vaisseau le plus proche qu’elles peuvent voir** dans leur portée, et sur aucun autre : la zone est le cercle qu’atteint la plus lointaine d’entre elles. Ce ne sont des entités d’aucune sorte : elles n’ont pas de points de vie, on ne peut pas les cibler, et rien de ce que vous leur tirez dessus ne fait quoi que ce soit. Leurs tirs sont réels, et le monde met leurs dégâts à l’échelle comme il le fait pour l’arme de n’importe quel alien.

<!-- swamp-guns:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Dégâts d’un tir, dans chaque monde :

| Canon | Lieu | Tire toutes les | Portée (unités) | Alpha | Beta | Gamma |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| Tourelle de [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | 5 000 / 4 400 | 2 s | 3 640 | 75 000 | 112 500 | 150 000 |
| Tourelle de [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | 5 000 / 4 400 | 5 s | 1 080 | 50 000 | 75 000 | 100 000 |
| Tourelle laser × 2 | 3 600 / 5 200; 6 400 / 5 200 | 1 s | 2 500 | 45 000–55 000 | 67 500–82 500 | 90 000–110 000 |

- Une roquette est tirée à 90 % de sa portée, pour qu’elle arrive ; une tourelle laser tire une fois par seconde, et ses dégâts sont tirés au sort dans la plage indiquée.
- Un N.I.K.E. a 35 % de pénétration de bouclier, retranchée de l’absorption d’un bouclier.
- Un N.U.K.E. éclate sur un rayon de 900 unités, avec le plus de force au centre.

<!-- swamp-guns:end -->

- **Rien n’atteint l’extérieur de la zone,** et à l’intérieur un vaisseau est détruit en quelques secondes : plus il s’approche du milieu, plus de canons s’ajoutent, et même le Wraith le mieux protégé ne tient pas.
- **Une occultation vous fait entrer.** Aucune tourelle ne voit jamais un vaisseau occulté, ni un vaisseau dans la fenêtre d’un EMP, à aucune distance. Une explosion visant un vaisseau visible qui éclate près d’un vaisseau occulté le blesse quand même et met fin à son occultation.
- **Elles ne tirent que sur les pilotes,** jamais sur les aliens, les pilotes de corporation ni l’essaim, et la protection d’un vaisseau qui vient de revenir d’une destruction tient aussi contre elles.
- **L’anneau d’avertissement.** Un vaisseau qui franchit l’anneau en dehors de la zone reçoit une ligne Système : les tourelles tirent sur tout vaisseau qu’elles voient, et quelque chose dort au milieu. Il n’est prévenu de nouveau que lorsqu’il a quitté l’anneau et y est revenu.
- **En sortir.** Si vous êtes détruit là-bas et revenez sur place, ou si vous vous connectez dans la zone, vous êtes mis dehors. Un cap que vous cliquez est infléchi autour de la zone, et une alerte vous prévient quand l’endroit cliqué s’y trouve.

## Les aliens {#the-aliens}

Trois aliens de la civilisation perdue vivent ici, chacun avec ses propres chiffres. Ils sont payés comme le boss d’un essaim : **selon les dégâts infligés**, à chaque pilote qui en a fait au moins la part indiquée dans [Essaims](/wiki/05-Swarms/Swarms.md#the-rules-of-every-swarm), et la caisse va au pilote qui a infligé le plus de dégâts. Leurs éliminations s’ajoutent à vos points PvE de grade comme celles d’un vaisseau d’essaim, en proportion de leur gain ([Grades](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points)). Le bouclier de chacun absorbe 80 % de chaque coup tant qu’il tient ([Boucliers](/wiki/03-Mechanics/Shields.md)).

- **Slumbering Void.** Le chasseur élancé, l’alien le plus rapide du jeu (aussi rapide qu’un Storm avec Afterburner III). Certains patrouillent toujours aux abords du marais, et d’autres arrivent par vagues aux excavatrices. Il est agressif, traque le pilote le plus proche qu’il peut voir et ne voit jamais un vaisseau occulté.
- **Inert Mass.** Une carcasse morte aux fissures violettes, de la taille d’une petite station. Elles restent à une distance fixe du milieu du marais et ne le quittent pas pour l’instant. Elle tire des **Dormant Lances** : des roquettes guidées à très longue portée qui suivent un vaisseau jusqu’à ce qu’il s’occulte, ouvre une fenêtre d’EMP, entre dans un anneau sûr, saute ou meure. Elle est plus rapide que n’importe quel vaisseau, donc seules ces ruptures aident.
- **L’Unwakened.** Un monolithe qui dort au milieu du marais, la plus grande chose de toutes les cartes, si lent qu’il n’attrape jamais un vaisseau. Il ne tire rien, mais tout vaisseau dans son aura brûle, **occulté ou non**. Il est **immunisé** : les tirs et les roquettes touchent et ne font rien, la fenêtre de cible montre des barres pleines et le mot Immunisé. Un événement ultérieur permettra de le combattre ; ses récompenses ci-dessous sont écrites et ne peuvent pas encore être gagnées.

<!-- swamp-members:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

### Slumbering Void

2 Slumbering Voids patrouillent entre 4 600 et 6 500 unités du milieu du marais ; un qui est détruit revient 1 h plus tard. Les vagues d’une excavatrice amènent d’autres du même alien.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | 25 000 | 37 500 | 50 000 |
| Bouclier | 150 000 | 225 000 | 300 000 |
| Absorption du bouclier | 80 % | 80 % | 80 % |
| Dégâts des lasers (une salve par seconde) | 3 000 | 4 500 | 6 000 |
| Vitesse | 400 | 400 | 400 |
| Portée des lasers | 800 | 800 | 800 |
| Rayon d’aggro | 2 500 | 2 500 | 2 500 |
| Crédits | 23 000 | 46 000 | 69 000 |
| Thulium | 60 | 120 | 180 |
| Expérience (XP) | 3 600 | 7 200 | 10 800 |
| Honneur | 16 | 32 | 48 |
| Points PvE par élimination | 10 | 10 | 10 |

**Butin** : une caisse, pour le pilote qui a infligé le plus de dégâts.

| Objet | Chance | Quantité |
| :--- | ---: | ---: |
| L’un de Ultra Core et Experimental Fusion Core, tiré au hasard | 60 % | 30–60 |
| L’une des 4 [roquettes](/wiki/06-Items/Rockets.md) Épiques, tirée au hasard | 40 % | 1–3 |

### Inert Mass

5 Inert Masses se tiennent à moins de 2 400 unités du milieu ; une qui est détruite revient 1 h plus tard. Tire toutes les 6 s une [Dormant Lance](/wiki/06-Items/Rockets.md#the-craft-only-rockets) guidée sur le vaisseau le plus proche qu’elle peut voir : vitesse 750, un vol de 5 250 unités, 40 % de pénétration.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | 250 000 | 375 000 | 500 000 |
| Bouclier | 100 000 | 150 000 | 200 000 |
| Absorption du bouclier | 80 % | 80 % | 80 % |
| Dégâts de chaque Dormant Lance | 5 000–8 000 | 7 500–12 000 | 10 000–16 000 |
| Vitesse | 60 | 60 | 60 |
| Portée des roquettes | 5 000 | 5 000 | 5 000 |
| Rayon d’aggro | 5 000 | 5 000 | 5 000 |
| Crédits | 125 000 | 250 000 | 375 000 |
| Thulium | 335 | 670 | 1 005 |
| Expérience (XP) | 20 200 | 40 400 | 60 600 |
| Honneur | 88 | 176 | 264 |
| Points PvE par élimination | 15 | 15 | 15 |

**Butin** : une caisse, pour le pilote qui a infligé le plus de dégâts.

| Objet | Chance | Quantité |
| :--- | ---: | ---: |
| Ultra Core et Experimental Fusion Core, répartis à parts égales | 100 % | 400–800 en tout |
| L’une des 4 [roquettes](/wiki/06-Items/Rockets.md) Épiques, tirée au hasard | 100 % | 20–40 |
| N.I.K.E. | 5 % | 1–2 |
| Dark Matter | 5 % | 1–3 |
| Ancient Control Unit | 10 % | 1 |
| Power Core | 25 % | 1–2 |

### The Unwakened

Il y en a un, au milieu du marais et nulle part ailleurs ; il revient 24 h après sa destruction. Il est **immunisé** jusqu’à ce qu’une mission ultérieure désactive le drapeau : les tirs et les roquettes le touchent et ne font rien. Ses récompenses sont écrites et ne peuvent pas encore être gagnées.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | 10 000 000 | 15 000 000 | 20 000 000 |
| Bouclier | 10 000 000 | 15 000 000 | 20 000 000 |
| Absorption du bouclier | 80 % | 80 % | 80 % |
| Dégâts de l’aura par seconde, à tout vaisseau à l’intérieur | 75 000 | 112 500 | 150 000 |
| Rayon de l’aura | 700 | 700 | 700 |
| Vitesse | 10 | 10 | 10 |
| Rayon d’aggro | 3 000 | 3 000 | 3 000 |
| Crédits | 7 500 000 | 15 000 000 | 22 500 000 |
| Thulium | 20 000 | 40 000 | 60 000 |
| Expérience (XP) | 1 200 000 | 2 400 000 | 3 600 000 |
| Honneur | 5 200 | 10 400 | 15 600 |
| Points PvE par élimination | 112 | 112 | 112 |

**Butin** : une caisse, pour le pilote qui a infligé le plus de dégâts.

| Objet | Chance | Quantité |
| :--- | ---: | ---: |
| Ultra Core et Experimental Fusion Core, répartis à parts égales | 100 % | 10 000–15 000 en tout |
| L’une des 4 [roquettes](/wiki/06-Items/Rockets.md) Épiques, tirée au hasard | 100 % | 500–800 |
| N.I.K.E. | 100 % | 20–30 |
| N.U.K.E. | 100 % | 5–10 |
| Dark Matter | 100 % | 40–60 |
| Ancient Control Unit | 100 % | 10–20 |
| Power Core | 100 % | 100–200 |

<!-- swamp-members:end -->

## Que faire ici {#what-to-do-here}

- **Regarder, ne pas toucher.** Le marais est pour plus tard. Le seul contenu que vous pouvez atteindre sans occultation est hors de la zone : les Voids en patrouille, dans un anneau autour de la zone, sont la première ligne du marais et l’endroit où un groupe peut se battre sans les canons.
- **Combattez les Voids avec de la pénétration.** Le grand bouclier d’un Void absorbe 80 % d’un coup et compte presque pour rien : la coque derrière est petite. Plus vos lasers ont de pénétration de bouclier, plus vite il tombe ([Lasers et munitions](/wiki/06-Items/Lasers.md)).
- **Restez hors des Lances.** Une Inert Mass voit loin et on ne distance pas une Lance : rompez son emprise par une occultation, un EMP, un anneau sûr ou un saut, ou quittez sa portée. Une Mass est un long combat, même pour un grand groupe des vaisseaux les plus puissants.
- **L’Essaim Dormant** apparaît désormais juste hors de la zone, si bien qu’un groupe peut l’attendre sans les canons. Voir [Essaim Dormant](/wiki/05-Swarms/Dormant-Swarm.md).

## Pour en savoir plus {#where-to-read-more}

- [Secteurs dangereux](/wiki/01-General/Danger-Sectors.md) : ce qui a changé au jour 11.
- [Excavatrice géante](/wiki/03-Mechanics/Giant-Excavator.md) : les vagues de Slumbering Voids et ce qu’elles gardent.
- [Essaims](/wiki/05-Swarms/Swarms.md) et [Essaim Dormant](/wiki/05-Swarms/Dormant-Swarm.md) : comment paie l’élimination d’un boss.
- [Roquettes](/wiki/06-Items/Rockets.md#the-craft-only-rockets) : le N.I.K.E. et le N.U.K.E. que tire la tourelle.
- [Trou noir](/wiki/03-Mechanics/Black-Hole.md) : l’autre danger de `DS-4`.
- [Caisses de cargaison](/wiki/03-Mechanics/Cargo.md) : les caisses que lâchent les aliens.
