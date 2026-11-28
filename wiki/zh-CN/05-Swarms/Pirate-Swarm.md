<!-- wiki-i18n source: 33448f95d2520b3a -->
<!-- wiki-i18n title: Pirate 虫群 -->
# Pirate 虫群 {#pirate-swarm}

Pirate 虫群由一个 **Pirate Boss** 和它的 **Pirate Scout** 组成：Pirate Boss 是一艘庞大而缓慢的舰船，不攻击任何人，用火箭回应；Pirate Scout 是一群更快的舰船，守卫并治疗它。它出没在企业基地与边境之间的星区，也就是游戏中段等级活动的地方，对飞行员小队来说是一场持久战，而不是速战速决的击杀。

## 一览 {#at-a-glance}

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **位置**：每个企业的 `x-2` 和 `x-3` 星区
- **数量**：每个星区 一个， 每个世界 共 6 个
- **出现**：从赛季第 4 天起，直到重置（Beta 和 Gamma：从赛季第 1 天起）
- **头领**：Pirate Boss
- **随从**：最多 5 × Pirate Scout， 每 10 秒 出现 一个新的
- **随从停留范围**：距头领不超过 900 单位
- **治疗**：距头领 600 单位以内的每个 Pirate Scout 都会治疗它的船体，在 Alpha 中每秒 40 HP
- **头领被击毁后**：头领被击毁后 1 分钟，随从会离开，除非它们正在攻击
- **回归**：头领 被击毁 {{guide:vitals.respawn@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} 后， 在同一星区
- **通知**：该星区的飞行员会被告知头领何时出现、何时被击毁。这些是系统行：它们显示在聊天的**系统**标签页中，带有未读计数，不会出现在**全球**或**本地**标签页里。击杀播报会写明获得这次击杀功劳的飞行员。

<!-- pirate-glance:end -->

## 成员 {#the-members}

- **Pirate Boss**：基于 Ironclad 的舰船，拥有它的一部分强度（数值见下）。它是被动的，**不发射激光**：它唯一的武器是**直线火箭**（[火箭](/wiki/06-Items/Rockets.md)；具体是哪种取决于星区，见表格），射向攻击它的飞行员，发射时它仍在游荡。它从不自己修复船体。它的[三个阶段](#the-leaders-three-steps)和[特殊能力](/wiki/03-Mechanics/Special-Abilities.md)可能改变这一点。
- **Pirate Scout**：基于 Kitefin 的舰船，拥有它的一部分强度。Scout 会攻击任何靠近的飞行员，待在 Boss 附近，每艘靠近 Boss 的 Scout 都会为它的船体治疗。

## 战斗过程 {#how-the-fight-goes}

- **打 Boss，不要打 Scout。** Scout 会治疗 Boss，但与 Boss 的船体相比，治疗量很小，而且新的 Scout 会按*一览*列表所说的频率出现：先击杀 Scout 的小队永远赶不上它们，只有非常庞大的小队才能清掉它们，而且仍比不去管它们的小队花更长时间击败 Boss。Scout 只会耗费你的时间，不会决定战斗。
- **把 Scout 引开。** Scout 只有在 Boss 的范围之内才会治疗，所以跟着你离开该范围的 Scout 什么也治疗不了，而 Ostirion 比 Scout 更快。
- **保持移动。** Boss 的火箭是直线的，不带制导：保持移动的舰船可以躲开，原地不动的舰船则会被击中。
- **带上小队。** 三名驾驶 Ostirion、使用 x2 弹药的飞行员，在 `x-2` 不损失一艘舰船就能赢，只是很勉强；在 `x-3` 则会被击毁，即使伤害被分摊也一样；四个人在 Alpha 中大约三分钟就能击败它。使用 x4 弹药时，在 `x-3` 三个人大约两分钟就能击败它。五个人在伤害被分摊时大约两分半钟就能击败它，由一名飞行员承受全部火力时要大约三分钟，并且会损失两艘舰船：让一名飞行员承受全部火力的小队需要五个人。在 Beta 中需要五名飞行员，在 Gamma 中需要七名，且伤害要被分摊（那里的 Boss 更大，它的 Scout 回复更多）。在 Alpha 的 `x-3` 使用 x2 弹药时，单独一艘 Ostirion 做不到，单独一艘 Paragon 也做不到，两艘 Paragon 可以稳稳拿下。在 Beta 和 Gamma 的 `x-3`，使用 x2 或 x4 弹药时，单独一艘 Paragon 都会被击毁。Boss 会应对第一个击中它的飞行员，所以让最结实的舰船先出手，并在这样的长战中使用你的技能（Emergency Repair、Shield Surge：[技能](/wiki/03-Mechanics/Abilities.md)）。仍是 2 级或 3 级的飞行员对它来说太弱，即使在他们活动的星区也是如此：变强之前请远离。
- **Boss 会回来**，在*一览*列表给出的时间之后，出现在同一个星区。

## 首领的三个阶段 {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

这场战斗有三个阶段（[运作方式](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)）；每个只发生一次。

- **开始时**: 向第一个击中它的飞行员发射一把扇形的 3 枚火箭，彼此相隔 12 度。
- **低于三分之二时**: 一次再召来 5 个Pirate Scouts，同时最多 10 个存活。它们不支付奖励，45 秒 后离开。
- **低于三分之一时**: 在 10 秒 内以 ×1.8 的速度飞向最近的星门，然后转身对付飞行员。

<!-- mob-ladder:end -->

## 奖励与掉落 {#rewards-and-drops}

Pirate Boss 的奖励与这场战斗相称：与它战斗一分钟的收益高于与 Goombah 战斗一分钟。奖励按伤害在与它战斗的飞行员之间分配（[Boss 击杀如何支付奖励](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)）。它的货箱归造成伤害最多的飞行员，里面可能有 **Reinforced Hull Plate**、火箭和弹药。它的货箱价值略低于击杀本身奖励的一半。Scout 的奖励很少，也不掉落任何东西。

## 数值 {#the-numbers}

虫群舰船在三个世界中的数值（[世界](/wiki/05-Swarms/Swarms.md#the-worlds)）。

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss

基于 Ironclad，拥有其 50% 的船体、护盾和伤害；速度和射程与原舰船相同。每 5 秒发射一枚直线火箭：`x-2`：[Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets), `x-3`：[Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets)。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@Pirate Boss#1}} | {{guide:vitals.hull@Pirate Boss#2}} | {{guide:vitals.hull@Pirate Boss#3}} |
| 护盾 | {{guide:vitals.shield@Pirate Boss#1}} | {{guide:vitals.shield@Pirate Boss#2}} | {{guide:vitals.shield@Pirate Boss#3}} |
| 激光伤害 （每秒一轮齐射） | 无 | 无 | 无 |
| 速度 | {{guide:vitals.speed@Pirate Boss#1}} | {{guide:vitals.speed@Pirate Boss#2}} | {{guide:vitals.speed@Pirate Boss#3}} |
| 激光射程 | – | – | – |
| 仇恨范围 | 被攻击时 | 被攻击时 | 被攻击时 |
| 火箭伤害 （最高） | {{guide:behaviour.ability:rocket.damage@Pirate Boss#1}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#2}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#3}} |
| 信用点 | {{guide:spoils.pay.credits@Pirate Boss#1}} | {{guide:spoils.pay.credits@Pirate Boss#2}} | {{guide:spoils.pay.credits@Pirate Boss#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Boss#1}} | {{guide:spoils.pay.thulium@Pirate Boss#2}} | {{guide:spoils.pay.thulium@Pirate Boss#3}} |
| 经验值（XP） | {{guide:spoils.pay.experience@Pirate Boss#1}} | {{guide:spoils.pay.experience@Pirate Boss#2}} | {{guide:spoils.pay.experience@Pirate Boss#3}} |
| 荣誉 | {{guide:spoils.pay.honor@Pirate Boss#1}} | {{guide:spoils.pay.honor@Pirate Boss#2}} | {{guide:spoils.pay.honor@Pirate Boss#3}} |
| 每次击杀的 PvE 积分 | 15 | 15 | 15 |

**掉落**：一个货箱，归造成伤害最多的飞行员。

| 物品 |
| :--- |
| {{guide:spoils.box@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} |

### Pirate Scout

基于 Kitefin，拥有其 50% 的船体和 113% 的激光伤害；速度和射程与原舰船相同。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@Pirate Scout#1}} | {{guide:vitals.hull@Pirate Scout#2}} | {{guide:vitals.hull@Pirate Scout#3}} |
| 护盾 | {{guide:vitals.shield@Pirate Scout#1}} | {{guide:vitals.shield@Pirate Scout#2}} | {{guide:vitals.shield@Pirate Scout#3}} |
| 激光伤害 （每秒一轮齐射） | {{guide:vitals.dps@Pirate Scout#1}} | {{guide:vitals.dps@Pirate Scout#2}} | {{guide:vitals.dps@Pirate Scout#3}} |
| 速度 | {{guide:vitals.speed@Pirate Scout#1}} | {{guide:vitals.speed@Pirate Scout#2}} | {{guide:vitals.speed@Pirate Scout#3}} |
| 激光射程 | 700 | 700 | 700 |
| 仇恨范围 | {{guide:vitals.aggro@Pirate Scout#1}} | {{guide:vitals.aggro@Pirate Scout#2}} | {{guide:vitals.aggro@Pirate Scout#3}} |
| 治疗头领 （每个，每秒，仅船体） | 40 | 60 | 80 |
| 信用点 | {{guide:spoils.pay.credits@Pirate Scout#1}} | {{guide:spoils.pay.credits@Pirate Scout#2}} | {{guide:spoils.pay.credits@Pirate Scout#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Scout#1}} | {{guide:spoils.pay.thulium@Pirate Scout#2}} | {{guide:spoils.pay.thulium@Pirate Scout#3}} |
| 经验值（XP） | {{guide:spoils.pay.experience@Pirate Scout#1}} | {{guide:spoils.pay.experience@Pirate Scout#2}} | {{guide:spoils.pay.experience@Pirate Scout#3}} |
| 荣誉 | {{guide:spoils.pay.honor@Pirate Scout#1}} | {{guide:spoils.pay.honor@Pirate Scout#2}} | {{guide:spoils.pay.honor@Pirate Scout#3}} |
| 每次击杀的 PvE 积分 | 4 | 4 | 4 |

**掉落**：无。击杀只支付信用点、Thulium、经验值和荣誉。

<!-- pirate-members:end -->
