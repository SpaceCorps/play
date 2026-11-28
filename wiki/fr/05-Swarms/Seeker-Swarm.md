<!-- wiki-i18n source: 7c6bc3eaf70223f5 -->
<!-- wiki-i18n title: Essaim Seeker -->
# Essaim Seeker {#seeker-swarm}

L’essaim Seeker est le plus petit des [essaims](/wiki/05-Swarms/Swarms.md) : un **Boss Seeker** et les **Seeker Slaves** qui le protègent et le soignent. Il vit dans les secteurs où les nouveaux pilotes commencent à voler, c’est donc le premier essaim que la plupart rencontrent. Le Boss Seeker ne commence jamais un combat, mais dès que vous lui tirez dessus, il est bien plus dangereux que le [Seeker](/wiki/04-Aliens/Seeker.md) sur lequel il est construit.

## D’un coup d’œil {#at-a-glance}

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Où** : Les secteurs `x-1` et `x-2` de chaque corporation
- **Combien** : Un dans chacun de ces secteurs, 6 dans chaque monde
- **Apparaît** : Du jour 4 de la saison jusqu’à la réinitialisation (Bêta et Gamma : dès le jour 1 de la saison)
- **Meneur** : Boss Seeker
- **Suivants** : Jusqu’à 4 × Seeker Slave, un nouveau toutes les 10 s
- **Les suivants restent** : à 500 unités au plus du meneur
- **Soins** : Chaque Seeker Slave à moins de 600 unités du meneur soigne sa coque, 50 PV par seconde dans Alpha
- **Meneur détruit** : Les suivants partent 30 s après la destruction du meneur, sauf s’ils attaquent
- **Revient** : {{guide:vitals.respawn@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} après la destruction du meneur, dans le même secteur
- **Annonces** : Les pilotes du secteur sont prévenus quand le meneur apparaît et quand il est détruit. Ce sont des lignes Système : elles apparaissent dans l’onglet **Système** du chat, avec un compteur de lignes non lues, et pas dans **Global** ni **Local**. Le fil des éliminations nomme le pilote à qui l’élimination est créditée.

<!-- seeker-glance:end -->

## Les membres {#the-members}

- **Boss Seeker** : un Seeker bien plus grand, à la teinte de l’essaim et avec son nom au-dessus, avec plusieurs fois la coque, le bouclier et les dégâts d’un Seeker (les valeurs sont plus bas). Il est passif : il erre jusqu’à ce qu’un pilote le touche, puis s’arrête là où il est et tire sur ce pilote, et les vaisseaux de son essaim proches se joignent au combat. La portée de son arme et sa vitesse sont celles d’un Seeker, et il ne répare jamais sa coque de lui-même. Ses [trois étapes](#the-leaders-three-steps) et une [capacité spéciale](/wiki/03-Mechanics/Special-Abilities.md) peuvent changer cela.
- **Seeker Slave** : un Seeker ordinaire à la teinte de l’essaim. Les Slaves restent près du boss, se joignent au combat quand un vaisseau d’essaim proche est touché, et chacun qui est près du boss soigne sa coque. Un Slave répare sa propre coque après un repos, comme un Seeker.

## Le déroulement du combat {#how-the-fight-goes}

- **Laissez-le tranquille tant que votre vaisseau ne peut pas l’affronter.** Un Boss Seeker frappe plus fort que ce que supporte le premier vaisseau d’un pilote : le Protos d’un nouveau pilote, encore sans bouclier, est détruit en quelques secondes dès que le boss et ses Slaves sont sur lui.
- **Restez hors de portée.** Le boss et ses Slaves sont plus lents qu’un Protos, et leurs armes portent moins loin qu’un Quantum Laser II (voir [Lasers et munitions](/wiki/06-Items/Lasers.md)) : un pilote qui a de tels lasers et reste au-delà de leur portée ne subit aucun dégât pendant qu’ils tirent. Un pilote avec des Quantum Laser I ne peut pas rester hors de portée.
- **Les Slaves soignent plus vite qu’un pilote débutant seul ne frappe.** Ensemble, ils soignent plus que ce qu’infligent les lasers d’un pilote avec des munitions x1 ; amenez donc un partenaire et des munitions x2. Deux pilotes avec des Quantum Laser II qui gardent leurs distances abattent le boss en environ une minute dans Alpha, et bien plus vite avec des munitions x2.
- **Le boss revient** après le délai de la liste *D’un coup d’œil*, en pleine force, dans le même secteur, et ses Slaves arrivent l’un après l’autre.

## Les trois étapes du chef {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Son combat a trois étapes ([comment elles marchent](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)) ; chacune a lieu une fois.

- **Au début**: Ses Seeker Slaves le soignent ×2 plus vite pendant 8 s.
- **Sous les deux tiers**: 2 copies de lui apparaissent, et le vrai porte un anneau.
- **Sous un tiers**: S’éloigne des pilotes pendant 4 s, puis se retourne.

<!-- mob-ladder:end -->

## Récompenses et butin {#rewards-and-drops}

Le Boss Seeker paie **exactement dix Seekers** : dix fois les crédits, le Thulium, l’XP et l’honneur d’un Seeker, répartis selon les dégâts entre les pilotes qui l’ont combattu ([comment paie l’élimination d’un boss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Sa caisse contient le butin de dix Seekers et, en plus, des munitions et des roquettes en dessous d’Épique, pour le pilote qui a infligé le plus de dégâts. Les Slaves paient peu et ne laissent rien ; les abattre n’est pas un bon farm, puisqu’ils reviennent avec le boss.

## Les valeurs {#the-numbers}

Les valeurs des vaisseaux de l’essaim dans les trois mondes ([Mondes](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker

Base : Seeker, avec 400 % de coque, de bouclier et de dégâts ; la vitesse et la portée sont celles du vaisseau d’origine.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | {{guide:vitals.hull@Boss Seeker#1}} | {{guide:vitals.hull@Boss Seeker#2}} | {{guide:vitals.hull@Boss Seeker#3}} |
| Bouclier | {{guide:vitals.shield@Boss Seeker#1}} | {{guide:vitals.shield@Boss Seeker#2}} | {{guide:vitals.shield@Boss Seeker#3}} |
| Dégâts des lasers (une salve par seconde) | {{guide:vitals.dps@Boss Seeker#1}} | {{guide:vitals.dps@Boss Seeker#2}} | {{guide:vitals.dps@Boss Seeker#3}} |
| Vitesse | {{guide:vitals.speed@Boss Seeker#1}} | {{guide:vitals.speed@Boss Seeker#2}} | {{guide:vitals.speed@Boss Seeker#3}} |
| Portée des lasers | 600 | 600 | 600 |
| Rayon d’aggro | seulement si attaqué | seulement si attaqué | seulement si attaqué |
| Crédits | {{guide:spoils.pay.credits@Boss Seeker#1}} | {{guide:spoils.pay.credits@Boss Seeker#2}} | {{guide:spoils.pay.credits@Boss Seeker#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Seeker#1}} | {{guide:spoils.pay.thulium@Boss Seeker#2}} | {{guide:spoils.pay.thulium@Boss Seeker#3}} |
| Expérience (XP) | {{guide:spoils.pay.experience@Boss Seeker#1}} | {{guide:spoils.pay.experience@Boss Seeker#2}} | {{guide:spoils.pay.experience@Boss Seeker#3}} |
| Honneur | {{guide:spoils.pay.honor@Boss Seeker#1}} | {{guide:spoils.pay.honor@Boss Seeker#2}} | {{guide:spoils.pay.honor@Boss Seeker#3}} |
| Points PvE par élimination | 5 | 5 | 5 |

**Butin** : une caisse, pour le pilote qui a infligé le plus de dégâts.

| Objet |
| :--- |
| {{guide:spoils.box@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} |

### Seeker Slave

Base : Seeker, avec 100 % de coque, de bouclier et de dégâts ; la vitesse et la portée sont celles du vaisseau d’origine.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Coque | {{guide:vitals.hull@Seeker Slave#1}} | {{guide:vitals.hull@Seeker Slave#2}} | {{guide:vitals.hull@Seeker Slave#3}} |
| Bouclier | {{guide:vitals.shield@Seeker Slave#1}} | {{guide:vitals.shield@Seeker Slave#2}} | {{guide:vitals.shield@Seeker Slave#3}} |
| Dégâts des lasers (une salve par seconde) | {{guide:vitals.dps@Seeker Slave#1}} | {{guide:vitals.dps@Seeker Slave#2}} | {{guide:vitals.dps@Seeker Slave#3}} |
| Vitesse | {{guide:vitals.speed@Seeker Slave#1}} | {{guide:vitals.speed@Seeker Slave#2}} | {{guide:vitals.speed@Seeker Slave#3}} |
| Portée des lasers | 600 | 600 | 600 |
| Rayon d’aggro | seulement si attaqué | seulement si attaqué | seulement si attaqué |
| Soigne le meneur, chacun, par seconde (coque seulement) | 50 | 75 | 100 |
| Crédits | {{guide:spoils.pay.credits@Seeker Slave#1}} | {{guide:spoils.pay.credits@Seeker Slave#2}} | {{guide:spoils.pay.credits@Seeker Slave#3}} |
| Thulium | {{guide:spoils.pay.thulium@Seeker Slave#1}} | {{guide:spoils.pay.thulium@Seeker Slave#2}} | {{guide:spoils.pay.thulium@Seeker Slave#3}} |
| Expérience (XP) | {{guide:spoils.pay.experience@Seeker Slave#1}} | {{guide:spoils.pay.experience@Seeker Slave#2}} | {{guide:spoils.pay.experience@Seeker Slave#3}} |
| Honneur | {{guide:spoils.pay.honor@Seeker Slave#1}} | {{guide:spoils.pay.honor@Seeker Slave#2}} | {{guide:spoils.pay.honor@Seeker Slave#3}} |
| Points PvE par élimination | 1 | 1 | 1 |

**Butin** : aucun. L’élimination ne paie que ses crédits, son Thulium, son XP et son honneur.

<!-- seeker-members:end -->
