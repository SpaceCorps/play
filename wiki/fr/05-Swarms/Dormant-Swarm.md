<!-- wiki-i18n source: fcba1b51b68a9123 -->
<!-- wiki-i18n title: Essaim Dormant -->
# Essaim Dormant {#dormant-swarm}

L’essaim Dormant est une **Dormant Force** avec ses **Dormant Pulses** : un groupe de vaisseaux qui ne commencent jamais un combat et frappent très fort une fois réveillés. Il n’y en a qu’un dans les secteurs dangereux de chaque monde (le [Deep Void](/wiki/03-Mechanics/Deep-Void.md#the-dormant-swarms-visit) a une visite à lui, une fois par jour). Il erre d’un secteur dangereux au suivant, et c’est le combat le plus dur et le butin le plus riche des essaims : un combat pour un grand groupe des vaisseaux les plus forts. Dès le jour 11 de la saison, il commence au [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) sur `DS-4`, revient plus tôt et paie le double (voir la liste *En un coup d’œil*).

## D’un coup d’œil {#at-a-glance}

<!-- dormant-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Où** : Les secteurs dangereux `DS-1`, `DS-2`, `DS-3`, `DS-4`, qu’il parcourt de l’un à l’autre
- **Combien** : Un dans chaque monde
- **Apparaît** : Du jour 4 de la saison jusqu’à la réinitialisation (Bêta et Gamma : dès le jour 1 de la saison)
- **Meneur** : Dormant Force
- **Suivants** : 2 × Dormant Pulse, qui volent avec le meneur
- **Les suivants restent** : à 700 unités au plus du meneur
- **Meneur détruit** : Dormant Pulse prend la tête
- **Meneur détruit** : Les suivants partent 30 s après la destruction du meneur, qu’ils attaquent ou non
- **Déplacements** : Reste 8 à 15 min sur une carte, puis vole vers le portail d’un autre secteur dangereux. Il ne prend jamais les portails qui sortent des secteurs dangereux et n’entre jamais dans l’anneau du trou noir
- **Revient** : {{guide:vitals.respawn@Dormant Force#1;Dormant Force#2;Dormant Force#3}} après la destruction de tout l’essaim, dans un secteur dangereux tiré au hasard
- **Dès le jour 11 de la saison** : Il apparaît au [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) de `DS-4` au lieu d’un secteur dangereux tiré au hasard, revient 30 min après la destruction de tout l’essaim, et chaque vaisseau paie ×2 (crédits, Thulium, XP et honneur ; le butin reste le même)
- **Annonces** : Les pilotes du monde entier sont prévenus quand l’essaim apparaît et quand il est détruit. Ce sont des lignes Système : elles apparaissent dans l’onglet **Système** du chat, avec un compteur de lignes non lues, et pas dans **Global** ni **Local**. Un marqueur le montre sur les cartes des secteurs dangereux et sur la carte de la galaxie. Le fil des éliminations nomme le pilote à qui l’élimination est créditée.

<!-- dormant-glance:end -->

## Les membres {#the-members}

- **Dormant Force** : un Wraith à pleine force, avec des lasers qui frappent trois fois plus fort que ceux d’un équipement typique. Elle mène l’essaim, est passive tant qu’on ne la touche pas, et tire des **roquettes droites** sur le premier pilote qui l’a touchée.
- **Dormant Pulse** : un Paragon à pleine force, avec des lasers lourds du même genre, dont chacun frappe deux fois plus fort qu’un laser de la Force, et ses propres roquettes. Une Pulse a moins de lasers que la Force, si bien que sa salve entière est plus grande que celle de la Force, sans être deux fois plus grande (les chiffres sont plus bas). Les Pulses volent près de la Force, et quand la Force est détruite, l’une d’elles prend la tête.

Ils sont passifs : ils n’attaquent jamais un pilote. Si l’un d’eux est touché, les autres proches de lui se joignent au combat contre le premier pilote qui l’a touché.

## Le déroulement du combat {#how-the-fight-goes}

- **Trouvez-le.** Le monde entier est prévenu quand il apparaît, et un marqueur le montre sur les cartes des secteurs dangereux et sur la carte de la galaxie. Il reste sur une carte le temps indiqué dans la liste *D’un coup d’œil*, puis vole vers la porte d’un autre secteur dangereux et saute ; il ne prend jamais une porte qui sort des secteurs dangereux et n’entre jamais dans l’anneau du trou noir. Il vole à la vitesse de son vaisseau le plus lent et, comme un pilote, ne commence ni ne termine un saut sous le feu. Dès le jour 11 de la saison, il apparaît d’abord juste en dehors de la zone du [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md), où un groupe peut l’attendre hors de portée des canons du marais, puis il sort en volant par une porte de `DS-4`.
- **On ne le bat pas seul, ni à quelques-uns.** Huit pilotes de niveau 8 en Paragon avec des munitions x2 ou x4 le détruisent en environ une minute dans Alpha, en perdant au plus un vaisseau ; un Paragon seul est détruit, et trois ou quatre avec des munitions x2 aussi. Les essaims de Beta et de Gamma sont plus forts ([Mondes](/wiki/05-Swarms/Swarms.md#the-worlds)), ces mondes demandent donc de plus grands groupes.
- **Ses lasers décident du combat.** Ensemble, ils peuvent détruire un Paragon en moins d’une minute, et même un Paragon aux meilleurs boucliers en moins de deux, roquettes ou non : amenez vos dégâts vite, avec les meilleurs boucliers que vous ayez.
- **Vaisseau par vaisseau.** Chaque vaisseau a sa propre coque et son propre gain, la Force ou une Pulse peut donc être détruite en premier. L’essaim n’est remplacé que lorsqu’il est entièrement détruit, après le délai de la liste *D’un coup d’œil*.

## Les trois étapes du chef {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Son combat a trois étapes ([comment elles marchent](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)) ; chacune a lieu une fois.

- **Au début**: Ne prend que 70 % de chaque coup tant que l’un de ses Dormant Pulses est en vie.
- **Sous les deux tiers**: Ses Dormant Pulses tirent une roquette toutes les 2,5 s pendant 15 s.
- **Sous un tiers**: Tant que tous ses Dormant Pulses sont en vie, ils le soignent de 5 % de sa coque par seconde pendant 6 s.

<!-- mob-ladder:end -->

## Récompenses et butin {#rewards-and-drops}

Chaque vaisseau paie pour lui-même, selon les dégâts qu’il a subis ([comment paie l’élimination d’un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)), et chacun laisse une caisse pour le pilote qui lui a infligé le plus de dégâts. La **caisse de la Force** est le gros lot : énormément de munitions x3 et x4, des roquettes Épiques d’une seule sorte et, de temps en temps, un N.I.K.E. ou un N.U.K.E. Les **Pulses** peuvent laisser une Ancient Control Unit, un Power Core ou de la Dark Matter. Une minute de combat contre l’essaim paie plus qu’une minute de combat contre le Crystalys, l’alien le mieux payé. Dès le jour 11 de la saison, chaque vaisseau paie le double (voir la liste *En un coup d’œil*) ; les caisses sont les mêmes.

## Les valeurs {#the-numbers}

Les valeurs des vaisseaux de l’essaim dans les trois mondes ([Mondes](/wiki/05-Swarms/Swarms.md#the-worlds)). Les crédits, le Thulium, l’XP et l’honneur des tableaux sont le gain d’avant le jour 11 de la saison ; à partir de ce jour, une élimination paie le double.

<!-- dormant-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Dormant Force

Base : Wraith, avec 100 % de sa coque et 300 % de ses dégâts laser ; la vitesse et la portée sont celles du vaisseau d’origine. Tire une roquette droite toutes les 5 s : [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | {{guide:vitals.hull@Dormant Force#1}} | {{guide:vitals.hull@Dormant Force#2}} | {{guide:vitals.hull@Dormant Force#3}} |
| Bouclier | {{guide:vitals.shield@Dormant Force#1}} | {{guide:vitals.shield@Dormant Force#2}} | {{guide:vitals.shield@Dormant Force#3}} |
| Dégâts des lasers (une salve par seconde) | {{guide:vitals.dps@Dormant Force#1}} | {{guide:vitals.dps@Dormant Force#2}} | {{guide:vitals.dps@Dormant Force#3}} |
| Vitesse | {{guide:vitals.speed@Dormant Force#1}} | {{guide:vitals.speed@Dormant Force#2}} | {{guide:vitals.speed@Dormant Force#3}} |
| Portée des lasers | 800 | 800 | 800 |
| Rayon d’aggro | seulement si attaqué | seulement si attaqué | seulement si attaqué |
| Dégâts des roquettes, au maximum | {{guide:behaviour.ability:rocket.damage@Dormant Force#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#3}} |
| Crédits | {{guide:spoils.pay.credits@Dormant Force#1}} | {{guide:spoils.pay.credits@Dormant Force#2}} | {{guide:spoils.pay.credits@Dormant Force#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Force#1}} | {{guide:spoils.pay.thulium@Dormant Force#2}} | {{guide:spoils.pay.thulium@Dormant Force#3}} |
| Expérience (XP) | {{guide:spoils.pay.experience@Dormant Force#1}} | {{guide:spoils.pay.experience@Dormant Force#2}} | {{guide:spoils.pay.experience@Dormant Force#3}} |
| Honneur | {{guide:spoils.pay.honor@Dormant Force#1}} | {{guide:spoils.pay.honor@Dormant Force#2}} | {{guide:spoils.pay.honor@Dormant Force#3}} |
| Points PvE par élimination | 25 | 25 | 25 |

**Butin** : une caisse, pour le pilote qui a infligé le plus de dégâts.

| Objet |
| :--- |
| {{guide:spoils.box@Dormant Force#1;Dormant Force#2;Dormant Force#3}} |

### Dormant Pulse

Base : Paragon, avec 100 % de sa coque et 600 % de ses dégâts laser ; la vitesse et la portée sont celles du vaisseau d’origine. Tire une roquette droite toutes les 5 s : [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | {{guide:vitals.hull@Dormant Pulse#1}} | {{guide:vitals.hull@Dormant Pulse#2}} | {{guide:vitals.hull@Dormant Pulse#3}} |
| Bouclier | {{guide:vitals.shield@Dormant Pulse#1}} | {{guide:vitals.shield@Dormant Pulse#2}} | {{guide:vitals.shield@Dormant Pulse#3}} |
| Dégâts des lasers (une salve par seconde) | {{guide:vitals.dps@Dormant Pulse#1}} | {{guide:vitals.dps@Dormant Pulse#2}} | {{guide:vitals.dps@Dormant Pulse#3}} |
| Vitesse | {{guide:vitals.speed@Dormant Pulse#1}} | {{guide:vitals.speed@Dormant Pulse#2}} | {{guide:vitals.speed@Dormant Pulse#3}} |
| Portée des lasers | 800 | 800 | 800 |
| Rayon d’aggro | seulement si attaqué | seulement si attaqué | seulement si attaqué |
| Dégâts des roquettes, au maximum | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#3}} |
| Crédits | {{guide:spoils.pay.credits@Dormant Pulse#1}} | {{guide:spoils.pay.credits@Dormant Pulse#2}} | {{guide:spoils.pay.credits@Dormant Pulse#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Pulse#1}} | {{guide:spoils.pay.thulium@Dormant Pulse#2}} | {{guide:spoils.pay.thulium@Dormant Pulse#3}} |
| Expérience (XP) | {{guide:spoils.pay.experience@Dormant Pulse#1}} | {{guide:spoils.pay.experience@Dormant Pulse#2}} | {{guide:spoils.pay.experience@Dormant Pulse#3}} |
| Honneur | {{guide:spoils.pay.honor@Dormant Pulse#1}} | {{guide:spoils.pay.honor@Dormant Pulse#2}} | {{guide:spoils.pay.honor@Dormant Pulse#3}} |
| Points PvE par élimination | 11 | 11 | 11 |

**Butin** : une caisse, pour le pilote qui a infligé le plus de dégâts.

| Objet |
| :--- |
| {{guide:spoils.box@Dormant Pulse#1;Dormant Pulse#2;Dormant Pulse#3}} |

<!-- dormant-members:end -->
