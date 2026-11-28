<!-- wiki-i18n source: 33448f95d2520b3a -->
<!-- wiki-i18n title: Essaim Pirate -->
# Essaim Pirate {#pirate-swarm}

L’essaim Pirate est un **Pirate Boss** avec ses **Pirate Scouts** : un vaisseau énorme et lent qui n’attaque personne et répond par des roquettes, et une meute de vaisseaux plus rapides qui le protègent et le soignent. Il vit dans les secteurs entre la base d’une corporation et sa frontière, là où se jouent les niveaux intermédiaires du jeu, et c’est un long combat pour un groupe de pilotes, pas une élimination rapide.

## D’un coup d’œil {#at-a-glance}

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Où** : Les secteurs `x-2` et `x-3` de chaque corporation
- **Combien** : Un dans chacun de ces secteurs, 6 dans chaque monde
- **Apparaît** : Du jour 4 de la saison jusqu’à la réinitialisation (Bêta et Gamma : dès le jour 1 de la saison)
- **Meneur** : Pirate Boss
- **Suivants** : Jusqu’à 5 × Pirate Scout, un nouveau toutes les 10 s
- **Les suivants restent** : à 900 unités au plus du meneur
- **Soins** : Chaque Pirate Scout à moins de 600 unités du meneur soigne sa coque, 40 PV par seconde dans Alpha
- **Meneur détruit** : Les suivants partent 1 min après la destruction du meneur, sauf s’ils attaquent
- **Revient** : {{guide:vitals.respawn@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} après la destruction du meneur, dans le même secteur
- **Annonces** : Les pilotes du secteur sont prévenus quand le meneur apparaît et quand il est détruit. Ce sont des lignes Système : elles apparaissent dans l’onglet **Système** du chat, avec un compteur de lignes non lues, et pas dans **Global** ni **Local**. Le fil des éliminations nomme le pilote à qui l’élimination est créditée.

<!-- pirate-glance:end -->

## Les membres {#the-members}

- **Pirate Boss** : un vaisseau construit sur l’Ironclad, avec une part de sa force (les valeurs sont plus bas). Il est passif et ne tire **aucun laser** : sa seule arme est une **roquette droite** ([Roquettes](/wiki/06-Items/Rockets.md) ; laquelle dépend du secteur, voir le tableau), sur le pilote qui l’a attaqué, et il continue d’errer pendant qu’il tire. Il ne répare jamais sa coque de lui-même. Ses [trois étapes](#the-leaders-three-steps) et une [capacité spéciale](/wiki/03-Mechanics/Special-Abilities.md) peuvent changer cela.
- **Pirate Scout** : un vaisseau construit sur le Kitefin, avec une part de sa force. Les Scouts attaquent tout pilote qui s’approche d’eux, restent près du boss, et chacun qui est près du boss soigne sa coque.

## Le déroulement du combat {#how-the-fight-goes}

- **Tirez sur le boss, pas sur les Scouts.** Les Scouts soignent le boss, mais ce soin est faible à côté de sa coque, et un nouveau Scout arrive aussi souvent que le dit la liste *D’un coup d’œil* : un groupe qui élimine d’abord les Scouts ne prend jamais d’avance sur eux, et seul un très grand groupe peut les éliminer tous et met pourtant plus de temps à finir le boss que celui qui les a laissés tranquilles. Les Scouts vous coûtent du temps, ils ne décident pas du combat.
- **Éloignez les Scouts.** Un Scout ne soigne que tant qu’il est à portée du boss, donc un Scout qui vous suit hors de cette portée ne soigne rien, et un Ostirion est plus rapide qu’un Scout.
- **Restez en mouvement.** La roquette du boss est droite et non guidée : un vaisseau qui reste en mouvement l’esquive, un vaisseau immobile est touché.
- **Amenez un groupe.** Trois pilotes en Ostirion avec des munitions x2 l’emportent sur `x-2` sans perdre de vaisseau, mais de justesse, et sont détruits sur `x-3`, même tant que les coups se répartissent ; quatre l’abattent en environ trois minutes dans Alpha. Avec des munitions x4, trois l’abattent sur `x-3` en environ deux minutes. Cinq l’abattent en environ deux minutes et demie quand les coups se répartissent et en environ trois quand un pilote encaisse tout le feu, et perdent alors deux vaisseaux : un groupe qui laisse un pilote encaisser tout le feu en demande cinq. Dans Beta il faut cinq pilotes et dans Gamma sept, les coups étant répartis (le boss y est plus grand et ses Scouts soignent davantage). Dans Alpha, sur `x-3` avec des munitions x2, un Ostirion seul n’y arrive pas, un Paragon seul n’y arrive pas non plus, et deux Paragons y arrivent sans risque. Dans Beta et Gamma, sur `x-3`, un Paragon seul est détruit avec des munitions x2 comme avec des munitions x4. Le boss répond au premier pilote qui l’a touché, donc laissez le vaisseau le plus robuste commencer, et utilisez vos compétences (Emergency Repair, Shield Surge : [Compétences](/wiki/03-Mechanics/Abilities.md)) dans un combat aussi long. Les pilotes encore de niveau 2 ou 3 sont trop faibles pour lui, même là où ils volent : restez à l’écart jusqu’à être plus forts.
- **Le boss revient** après le délai de la liste *D’un coup d’œil*, dans le même secteur.

## Les trois étapes du chef {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Son combat a trois étapes ([comment elles marchent](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)) ; chacune a lieu une fois.

- **Au début**: Tire un éventail de 3 roquettes, espacées de 12 degrés, sur le premier pilote qui l’a touché.
- **Sous les deux tiers**: Appelle 5 Pirate Scouts de plus d’un coup, au plus 10 en vie. Ils ne paient rien et partent après 45 s.
- **Sous un tiers**: Vole à vitesse ×1,8 vers la porte la plus proche pendant 10 s, puis se retourne contre les pilotes.

<!-- mob-ladder:end -->

## Récompenses et butin {#rewards-and-drops}

Le Pirate Boss paie à la mesure du combat qu’il est : une minute de combat contre lui paie plus qu’une minute de combat contre un Goombah. Le gain est réparti selon les dégâts entre les pilotes qui l’ont combattu ([comment paie l’élimination d’un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Sa caisse est pour le pilote qui a infligé le plus de dégâts et peut contenir une **Reinforced Hull Plate**, des roquettes et des munitions. Sa caisse vaut un peu moins de la moitié de ce que paie l’élimination elle-même. Les Scouts paient peu et ne laissent rien.

## Les valeurs {#the-numbers}

Les valeurs des vaisseaux de l’essaim dans les trois mondes ([Mondes](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss

Base : Ironclad, avec 50 % de coque, de bouclier et de dégâts ; la vitesse et la portée sont celles du vaisseau d’origine. Tire une roquette droite toutes les 5 s : [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) dans `x-2`, [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) dans `x-3`.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | {{guide:vitals.hull@Pirate Boss#1}} | {{guide:vitals.hull@Pirate Boss#2}} | {{guide:vitals.hull@Pirate Boss#3}} |
| Bouclier | {{guide:vitals.shield@Pirate Boss#1}} | {{guide:vitals.shield@Pirate Boss#2}} | {{guide:vitals.shield@Pirate Boss#3}} |
| Dégâts des lasers (une salve par seconde) | aucun | aucun | aucun |
| Vitesse | {{guide:vitals.speed@Pirate Boss#1}} | {{guide:vitals.speed@Pirate Boss#2}} | {{guide:vitals.speed@Pirate Boss#3}} |
| Portée des lasers | – | – | – |
| Rayon d’aggro | seulement si attaqué | seulement si attaqué | seulement si attaqué |
| Dégâts des roquettes, au maximum | {{guide:behaviour.ability:rocket.damage@Pirate Boss#1}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#2}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#3}} |
| Crédits | {{guide:spoils.pay.credits@Pirate Boss#1}} | {{guide:spoils.pay.credits@Pirate Boss#2}} | {{guide:spoils.pay.credits@Pirate Boss#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Boss#1}} | {{guide:spoils.pay.thulium@Pirate Boss#2}} | {{guide:spoils.pay.thulium@Pirate Boss#3}} |
| Expérience (XP) | {{guide:spoils.pay.experience@Pirate Boss#1}} | {{guide:spoils.pay.experience@Pirate Boss#2}} | {{guide:spoils.pay.experience@Pirate Boss#3}} |
| Honneur | {{guide:spoils.pay.honor@Pirate Boss#1}} | {{guide:spoils.pay.honor@Pirate Boss#2}} | {{guide:spoils.pay.honor@Pirate Boss#3}} |
| Points PvE par élimination | 15 | 15 | 15 |

**Butin** : une caisse, pour le pilote qui a infligé le plus de dégâts.

| Objet |
| :--- |
| {{guide:spoils.box@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} |

### Pirate Scout

Base : Kitefin, avec 50 % de sa coque et 113 % de ses dégâts laser ; la vitesse et la portée sont celles du vaisseau d’origine.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | {{guide:vitals.hull@Pirate Scout#1}} | {{guide:vitals.hull@Pirate Scout#2}} | {{guide:vitals.hull@Pirate Scout#3}} |
| Bouclier | {{guide:vitals.shield@Pirate Scout#1}} | {{guide:vitals.shield@Pirate Scout#2}} | {{guide:vitals.shield@Pirate Scout#3}} |
| Dégâts des lasers (une salve par seconde) | {{guide:vitals.dps@Pirate Scout#1}} | {{guide:vitals.dps@Pirate Scout#2}} | {{guide:vitals.dps@Pirate Scout#3}} |
| Vitesse | {{guide:vitals.speed@Pirate Scout#1}} | {{guide:vitals.speed@Pirate Scout#2}} | {{guide:vitals.speed@Pirate Scout#3}} |
| Portée des lasers | 700 | 700 | 700 |
| Rayon d’aggro | {{guide:vitals.aggro@Pirate Scout#1}} | {{guide:vitals.aggro@Pirate Scout#2}} | {{guide:vitals.aggro@Pirate Scout#3}} |
| Soigne le meneur, chacun, par seconde (coque seulement) | 40 | 60 | 80 |
| Crédits | {{guide:spoils.pay.credits@Pirate Scout#1}} | {{guide:spoils.pay.credits@Pirate Scout#2}} | {{guide:spoils.pay.credits@Pirate Scout#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Scout#1}} | {{guide:spoils.pay.thulium@Pirate Scout#2}} | {{guide:spoils.pay.thulium@Pirate Scout#3}} |
| Expérience (XP) | {{guide:spoils.pay.experience@Pirate Scout#1}} | {{guide:spoils.pay.experience@Pirate Scout#2}} | {{guide:spoils.pay.experience@Pirate Scout#3}} |
| Honneur | {{guide:spoils.pay.honor@Pirate Scout#1}} | {{guide:spoils.pay.honor@Pirate Scout#2}} | {{guide:spoils.pay.honor@Pirate Scout#3}} |
| Points PvE par élimination | 4 | 4 | 4 |

**Butin** : aucun. L’élimination ne paie que ses crédits, son Thulium, son XP et son honneur.

<!-- pirate-members:end -->
