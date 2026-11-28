<!-- wiki-i18n source: 2eff9c368449da99 -->
<!-- wiki-i18n title: Essaim Phantasm -->
# Essaim Phantasm {#phantasm-swarm}

L’essaim Phantasm est un **Boss Phantasm** avec ses **Phantasm Guards** : un [Phantasm](/wiki/04-Aliens/Phantasm.md) énorme qui ne commence jamais un combat, et de plus petits qui restent près de lui et le soignent. Il vit dans les secteurs extérieurs des corporations, `x-3` et `x-4`, et c’est un combat pour un groupe de pilotes de niveau intermédiaire.

## D’un coup d’œil {#at-a-glance}

<!-- phantasm-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Où** : Les secteurs `x-3` et `x-4` de chaque corporation
- **Combien** : Un dans chacun de ces secteurs, 6 dans chaque monde
- **Apparaît** : Du jour 4 de la saison jusqu’à la réinitialisation (Bêta et Gamma : dès le jour 1 de la saison)
- **Meneur** : Boss Phantasm
- **Suivants** : Jusqu’à 4 × Phantasm Guard, un nouveau toutes les 10 s
- **Les suivants restent** : à 500 unités au plus du meneur
- **Soins** : Chaque Phantasm Guard à moins de 600 unités du meneur soigne sa coque, 30 PV par seconde dans Alpha
- **Meneur détruit** : Les suivants partent 30 s après la destruction du meneur, sauf s’ils attaquent
- **Revient** : {{guide:vitals.respawn@Boss Phantasm#1;Boss Phantasm#2;Boss Phantasm#3}} après la destruction du meneur, dans le même secteur
- **Annonces** : Les pilotes du secteur sont prévenus quand le meneur apparaît et quand il est détruit. Ce sont des lignes Système : elles apparaissent dans l’onglet **Système** du chat, avec un compteur de lignes non lues, et pas dans **Global** ni **Local**. Le fil des éliminations nomme le pilote à qui l’élimination est créditée.

<!-- phantasm-glance:end -->

## Les membres {#the-members}

- **Boss Phantasm**: un Phantasm plus grand, à la teinte de l’essaim et avec son nom au-dessus, avec une coque, un bouclier et une salve laser qui lui sont propres (les valeurs sont plus bas). Il est passif : il erre jusqu’à ce qu’un pilote le touche, puis poursuit ce pilote et tire sur lui, et les vaisseaux de son essaim proches se joignent au combat. La portée de son arme et sa vitesse sont celles d’un Phantasm, et il ne répare jamais sa coque tout seul. Ses [trois étapes](#the-leaders-three-steps) et une [capacité spéciale](/wiki/03-Mechanics/Special-Abilities.md) peuvent changer cela.
- **Phantasm Guard**: un Phantasm plus petit à la teinte de l’essaim. Les Guards restent près du boss, se joignent au combat quand un vaisseau d’essaim proche est touché, et chacun qui est près du boss soigne sa coque. Un Guard répare sa propre coque après un repos, comme un Phantasm.

## Le déroulement du combat {#how-the-fight-goes}

- **Venez en groupe.** Trois pilotes de niveau 4–5 avec des munitions x2 le détruisent en environ une minute et demie dans Alpha, en perdant au plus un vaisseau ; un pilote de ce niveau seul est détruit, et deux ne gagnent que de justesse, et seulement tant que les coups se répartissent. De meilleurs vaisseaux et des munitions x4 le rendent bien plus rapide.
- **Tirez sur le boss, pas sur les Guards.** Un Guard tombe en quelques secondes, mais un nouveau arrive aussi souvent que la liste *D’un coup d’œil* l’indique, et ce que les Guards soignent est une petite part de ce qu’inflige un groupe : les laisser tranquilles coûte un peu de temps, leur donner la chasse en coûte davantage.
- **Beta et Gamma sont plus durs.** Les essaims de ces mondes sont plus forts ([Mondes](/wiki/05-Swarms/Swarms.md#the-worlds)), ils demandent donc plus de pilotes ou de meilleures munitions.
- **Surveillez le secteur.** `x-4` est un secteur PvP dans Alpha, et `x-3` et `x-4` le sont dans Beta et Gamma ([Mondes](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)) : un rival peut se joindre au combat ou attendre la caisse. Gardez un vaisseau du groupe en veille.
- **Le boss revient** après le délai de la liste *D’un coup d’œil*, en pleine force, dans le même secteur, et ses Guards arrivent l’un après l’autre.

## Les trois étapes du chef {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Son combat a trois étapes ([comment elles marchent](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)) ; chacune a lieu une fois.

- **Au début**: Chacun de ses Phantasm Guards dresse une couche de bouclier de 10 % de sa propre coque.
- **Sous les deux tiers**: 3 copies de lui apparaissent, et le vrai porte un anneau.
- **Sous un tiers**: Saute à environ 2 500 unités des pilotes, et ses Phantasm Guards reviennent intacts autour de lui.

<!-- mob-ladder:end -->

## Récompenses et butin {#rewards-and-drops}

Le Boss Phantasm paie pour le combat qu’il est : une minute à le combattre paie plus qu’une minute à combattre un Goombah, l’alien le mieux payé de ces secteurs. Le paiement est réparti selon les dégâts entre les pilotes qui l’ont combattu ([comment paie l’élimination d’un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Sa caisse revient au pilote qui a infligé le plus de dégâts et contient le butin propre d’un Phantasm plusieurs fois (Ship Fragments, Daraxium et Nyxite), avec des munitions et des roquettes. Les Guards paient peu et ne laissent rien ; les tuer n’est pas une façon de farmer, car ils reviennent avec le boss.

## Les valeurs {#the-numbers}

Les valeurs des vaisseaux de l’essaim dans les trois mondes ([Mondes](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- phantasm-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Phantasm

Base : Phantasm, avec 2 000 % de sa coque et 300 % de ses dégâts laser ; la vitesse et la portée sont celles du vaisseau d’origine.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | {{guide:vitals.hull@Boss Phantasm#1}} | {{guide:vitals.hull@Boss Phantasm#2}} | {{guide:vitals.hull@Boss Phantasm#3}} |
| Bouclier | {{guide:vitals.shield@Boss Phantasm#1}} | {{guide:vitals.shield@Boss Phantasm#2}} | {{guide:vitals.shield@Boss Phantasm#3}} |
| Dégâts des lasers (une salve par seconde) | {{guide:vitals.dps@Boss Phantasm#1}} | {{guide:vitals.dps@Boss Phantasm#2}} | {{guide:vitals.dps@Boss Phantasm#3}} |
| Vitesse | {{guide:vitals.speed@Boss Phantasm#1}} | {{guide:vitals.speed@Boss Phantasm#2}} | {{guide:vitals.speed@Boss Phantasm#3}} |
| Portée des lasers | 700 | 700 | 700 |
| Rayon d’aggro | seulement si attaqué | seulement si attaqué | seulement si attaqué |
| Crédits | {{guide:spoils.pay.credits@Boss Phantasm#1}} | {{guide:spoils.pay.credits@Boss Phantasm#2}} | {{guide:spoils.pay.credits@Boss Phantasm#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Phantasm#1}} | {{guide:spoils.pay.thulium@Boss Phantasm#2}} | {{guide:spoils.pay.thulium@Boss Phantasm#3}} |
| Expérience (XP) | {{guide:spoils.pay.experience@Boss Phantasm#1}} | {{guide:spoils.pay.experience@Boss Phantasm#2}} | {{guide:spoils.pay.experience@Boss Phantasm#3}} |
| Honneur | {{guide:spoils.pay.honor@Boss Phantasm#1}} | {{guide:spoils.pay.honor@Boss Phantasm#2}} | {{guide:spoils.pay.honor@Boss Phantasm#3}} |
| Points PvE par élimination | 8 | 8 | 8 |

**Butin** : une caisse, pour le pilote qui a infligé le plus de dégâts.

| Objet |
| :--- |
| {{guide:spoils.box@Boss Phantasm#1;Boss Phantasm#2;Boss Phantasm#3}} |

### Phantasm Guard

Base : Phantasm, avec 50 % de coque, de bouclier et de dégâts ; la vitesse et la portée sont celles du vaisseau d’origine.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | {{guide:vitals.hull@Phantasm Guard#1}} | {{guide:vitals.hull@Phantasm Guard#2}} | {{guide:vitals.hull@Phantasm Guard#3}} |
| Bouclier | {{guide:vitals.shield@Phantasm Guard#1}} | {{guide:vitals.shield@Phantasm Guard#2}} | {{guide:vitals.shield@Phantasm Guard#3}} |
| Dégâts des lasers (une salve par seconde) | {{guide:vitals.dps@Phantasm Guard#1}} | {{guide:vitals.dps@Phantasm Guard#2}} | {{guide:vitals.dps@Phantasm Guard#3}} |
| Vitesse | {{guide:vitals.speed@Phantasm Guard#1}} | {{guide:vitals.speed@Phantasm Guard#2}} | {{guide:vitals.speed@Phantasm Guard#3}} |
| Portée des lasers | 700 | 700 | 700 |
| Rayon d’aggro | seulement si attaqué | seulement si attaqué | seulement si attaqué |
| Soigne le meneur, chacun, par seconde (coque seulement) | 30 | 45 | 60 |
| Crédits | {{guide:spoils.pay.credits@Phantasm Guard#1}} | {{guide:spoils.pay.credits@Phantasm Guard#2}} | {{guide:spoils.pay.credits@Phantasm Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Phantasm Guard#1}} | {{guide:spoils.pay.thulium@Phantasm Guard#2}} | {{guide:spoils.pay.thulium@Phantasm Guard#3}} |
| Expérience (XP) | {{guide:spoils.pay.experience@Phantasm Guard#1}} | {{guide:spoils.pay.experience@Phantasm Guard#2}} | {{guide:spoils.pay.experience@Phantasm Guard#3}} |
| Honneur | {{guide:spoils.pay.honor@Phantasm Guard#1}} | {{guide:spoils.pay.honor@Phantasm Guard#2}} | {{guide:spoils.pay.honor@Phantasm Guard#3}} |
| Points PvE par élimination | 1 | 1 | 1 |

**Butin** : aucun. L’élimination ne paie que ses crédits, son Thulium, son XP et son honneur.

<!-- phantasm-members:end -->
