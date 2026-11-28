<!-- wiki-i18n source: 2b3edf7bcb1d9673 -->
<!-- wiki-i18n title: Essaim Crystalys -->
# Essaim Crystalys {#crystalys-swarm}

L’essaim Crystalys est un **Boss Crystalys** avec ses **Crystalys Guards** : le plus coriace des aliens, le [Crystalys](/wiki/04-Aliens/Crystalys.md), en plus grand, avec des gardes qui restent près de lui et le soignent. Il vit dans les [secteurs dangereux](/wiki/01-General/Danger-Sectors.md) `DS-1`, `DS-2` et `DS-3`, un dans chacun, et ne quitte jamais son secteur. Les secteurs dangereux sont des secteurs PvP : le combat est donc pour un grand groupe des pilotes les plus forts, et le boss n’y est pas le seul danger.

## D’un coup d’œil {#at-a-glance}

<!-- crystalys-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Où** : Les secteurs dangereux `DS-1`, `DS-2`, `DS-3`
- **Combien** : Un dans chacun de ces secteurs, 3 dans chaque monde
- **Apparaît** : Du jour 4 de la saison jusqu’à la réinitialisation (Bêta et Gamma : dès le jour 1 de la saison)
- **Meneur** : Boss Crystalys
- **Suivants** : Jusqu’à 3 × Crystalys Guard, un nouveau toutes les 10 s
- **Les suivants restent** : à 500 unités au plus du meneur
- **Soins** : Chaque Crystalys Guard à moins de 600 unités du meneur soigne sa coque, 250 PV par seconde dans Alpha
- **Meneur détruit** : Les suivants partent 30 s après la destruction du meneur, sauf s’ils attaquent
- **Revient** : {{guide:vitals.respawn@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} après la destruction du meneur, dans le même secteur
- **Annonces** : Les pilotes du secteur sont prévenus quand le meneur apparaît et quand il est détruit. Ce sont des lignes Système : elles apparaissent dans l’onglet **Système** du chat, avec un compteur de lignes non lues, et pas dans **Global** ni **Local**. Le fil des éliminations nomme le pilote à qui l’élimination est créditée.

<!-- crystalys-glance:end -->

## Les membres {#the-members}

- **Boss Crystalys**: un Crystalys plus grand, à la teinte de l’essaim et avec son nom au-dessus, avec une coque, un bouclier et une salve laser qui lui sont propres (les valeurs sont plus bas). Il est passif : il erre jusqu’à ce qu’un pilote le touche, puis poursuit ce pilote et tire sur lui, et les vaisseaux de son essaim proches se joignent au combat. La portée de son arme et sa vitesse sont celles d’un Crystalys, et il ne répare jamais sa coque tout seul. Ses [trois étapes](#the-leaders-three-steps) et une [capacité spéciale](/wiki/03-Mechanics/Special-Abilities.md) peuvent changer cela.
- **Crystalys Guard**: un Crystalys plus petit à la teinte de l’essaim. Les Guards restent près du boss, se joignent au combat quand un vaisseau d’essaim proche est touché, et chacun qui est près du boss soigne sa coque. Un Guard répare sa propre coque après un repos, comme un Crystalys.

## Le déroulement du combat {#how-the-fight-goes}

- **Venez en grand groupe.** Dans Alpha, six pilotes de niveau 8 en Paragon avec des munitions x2 suffisent si son tir se répartit entre eux, neuf s’il se concentre sur un seul pilote ; avec des munitions x4, cinq et six. Plus il y a de pilotes, plus le combat finit tôt et moins de vaisseaux sont perdus, et un pilote seul est détruit.
- **Tirez sur le boss, pas sur les Guards.** Un Guard tombe en quelques secondes, mais un nouveau arrive aussi souvent que la liste *D’un coup d’œil* l’indique, et ce que les Guards soignent est une petite part de ce qu’inflige un groupe : les laisser tranquilles coûte un peu de temps, leur donner la chasse en coûte davantage.
- **Beta et Gamma sont plus durs.** Les essaims de ces mondes sont plus forts ([Mondes](/wiki/05-Swarms/Swarms.md#the-worlds)), ils demandent donc plus de pilotes ou de meilleures munitions.
- **Les secteurs dangereux sont PvP.** Un rival peut attaquer le groupe en plein combat et attendre la caisse : elle est au pilote qui a infligé le plus de dégâts (et à son clan) pendant 30 secondes, puis à n’importe qui ([Cargaison](/wiki/03-Mechanics/Cargo.md)). Ne venez pas seul.
- **Le boss revient** après le délai de la liste *D’un coup d’œil*, en pleine force, dans le même secteur, et ses Guards arrivent l’un après l’autre.

## Les trois étapes du chef {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Son combat a trois étapes ([comment elles marchent](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)) ; chacune a lieu une fois.

- **Au début**: Ne prend que 50 % de chaque coup pendant 8 s.
- **Sous les deux tiers**: Un anneau de 700 unités frappe chaque vaisseau à l’intérieur avec 4 de ses salves, et il tire 4 roquettes.
- **Sous un tiers**: Se soigne de 20 % de sa coque et de son bouclier (une rafale de dégâts l’interrompt), et 3 Crystalys Guards de plus arrivent, au plus 6 en vie.

<!-- mob-ladder:end -->

## Récompenses et butin {#rewards-and-drops}

Le Boss Crystalys paie pour le combat qu’il est : une minute à le combattre paie plus qu’une minute à combattre un Crystalys, l’alien le mieux payé. Le paiement est réparti selon les dégâts entre les pilotes qui l’ont combattu ([comment paie l’élimination d’un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Sa caisse revient au pilote qui a infligé le plus de dégâts et contient de la Cataclysite et du Quorvium, de temps en temps un Power Core, une Ancient Control Unit ou de la Dark Matter, des munitions x3 et x4 et des roquettes Épiques. Les Guards paient peu et ne laissent rien ; les tuer n’est pas une façon de farmer, car ils reviennent avec le boss.

## Les valeurs {#the-numbers}

Les valeurs des vaisseaux de l’essaim dans les trois mondes ([Mondes](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- crystalys-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Crystalys

Base : Crystalys, avec 350 % de sa coque et 100 % de ses dégâts laser ; la vitesse et la portée sont celles du vaisseau d’origine.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | {{guide:vitals.hull@Boss Crystalys#1}} | {{guide:vitals.hull@Boss Crystalys#2}} | {{guide:vitals.hull@Boss Crystalys#3}} |
| Bouclier | {{guide:vitals.shield@Boss Crystalys#1}} | {{guide:vitals.shield@Boss Crystalys#2}} | {{guide:vitals.shield@Boss Crystalys#3}} |
| Dégâts des lasers (une salve par seconde) | {{guide:vitals.dps@Boss Crystalys#1}} | {{guide:vitals.dps@Boss Crystalys#2}} | {{guide:vitals.dps@Boss Crystalys#3}} |
| Vitesse | {{guide:vitals.speed@Boss Crystalys#1}} | {{guide:vitals.speed@Boss Crystalys#2}} | {{guide:vitals.speed@Boss Crystalys#3}} |
| Portée des lasers | 900 | 900 | 900 |
| Rayon d’aggro | seulement si attaqué | seulement si attaqué | seulement si attaqué |
| Crédits | {{guide:spoils.pay.credits@Boss Crystalys#1}} | {{guide:spoils.pay.credits@Boss Crystalys#2}} | {{guide:spoils.pay.credits@Boss Crystalys#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Crystalys#1}} | {{guide:spoils.pay.thulium@Boss Crystalys#2}} | {{guide:spoils.pay.thulium@Boss Crystalys#3}} |
| Expérience (XP) | {{guide:spoils.pay.experience@Boss Crystalys#1}} | {{guide:spoils.pay.experience@Boss Crystalys#2}} | {{guide:spoils.pay.experience@Boss Crystalys#3}} |
| Honneur | {{guide:spoils.pay.honor@Boss Crystalys#1}} | {{guide:spoils.pay.honor@Boss Crystalys#2}} | {{guide:spoils.pay.honor@Boss Crystalys#3}} |
| Points PvE par élimination | 30 | 30 | 30 |

**Butin** : une caisse, pour le pilote qui a infligé le plus de dégâts.

| Objet |
| :--- |
| {{guide:spoils.box@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} |

### Crystalys Guard

Base : Crystalys, avec 15 % de coque, de bouclier et de dégâts ; la vitesse et la portée sont celles du vaisseau d’origine.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | {{guide:vitals.hull@Crystalys Guard#1}} | {{guide:vitals.hull@Crystalys Guard#2}} | {{guide:vitals.hull@Crystalys Guard#3}} |
| Bouclier | {{guide:vitals.shield@Crystalys Guard#1}} | {{guide:vitals.shield@Crystalys Guard#2}} | {{guide:vitals.shield@Crystalys Guard#3}} |
| Dégâts des lasers (une salve par seconde) | {{guide:vitals.dps@Crystalys Guard#1}} | {{guide:vitals.dps@Crystalys Guard#2}} | {{guide:vitals.dps@Crystalys Guard#3}} |
| Vitesse | {{guide:vitals.speed@Crystalys Guard#1}} | {{guide:vitals.speed@Crystalys Guard#2}} | {{guide:vitals.speed@Crystalys Guard#3}} |
| Portée des lasers | 900 | 900 | 900 |
| Rayon d’aggro | seulement si attaqué | seulement si attaqué | seulement si attaqué |
| Soigne le meneur, chacun, par seconde (coque seulement) | 250 | 375 | 500 |
| Crédits | {{guide:spoils.pay.credits@Crystalys Guard#1}} | {{guide:spoils.pay.credits@Crystalys Guard#2}} | {{guide:spoils.pay.credits@Crystalys Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Crystalys Guard#1}} | {{guide:spoils.pay.thulium@Crystalys Guard#2}} | {{guide:spoils.pay.thulium@Crystalys Guard#3}} |
| Expérience (XP) | {{guide:spoils.pay.experience@Crystalys Guard#1}} | {{guide:spoils.pay.experience@Crystalys Guard#2}} | {{guide:spoils.pay.experience@Crystalys Guard#3}} |
| Honneur | {{guide:spoils.pay.honor@Crystalys Guard#1}} | {{guide:spoils.pay.honor@Crystalys Guard#2}} | {{guide:spoils.pay.honor@Crystalys Guard#3}} |
| Points PvE par élimination | 6 | 6 | 6 |

**Butin** : aucun. L’élimination ne paie que ses crédits, son Thulium, son XP et son honneur.

<!-- crystalys-members:end -->
