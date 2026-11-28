<!-- wiki-i18n source: 2eff9c368449da99 -->
<!-- wiki-i18n title: Phantasm 虫群 -->
# Phantasm 虫群 {#phantasm-swarm}

Phantasm 虫群由一个 **Boss Phantasm** 和它的 **Phantasm Guard** 组成：一只从不主动开战的巨型 [Phantasm](/wiki/04-Aliens/Phantasm.md)，以及待在它附近并为它治疗的较小个体。它出没在各企业的外围星区 `x-3` 和 `x-4`，适合一队中等等级的飞行员来战斗。

## 一览 {#at-a-glance}

<!-- phantasm-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **位置**：每个企业的 `x-3` 和 `x-4` 星区
- **数量**：每个星区 一个， 每个世界 共 6 个
- **出现**：从赛季第 4 天起，直到重置（Beta 和 Gamma：从赛季第 1 天起）
- **头领**：Boss Phantasm
- **随从**：最多 4 × Phantasm Guard， 每 10 秒 出现 一个新的
- **随从停留范围**：距头领不超过 500 单位
- **治疗**：距头领 600 单位以内的每个 Phantasm Guard 都会治疗它的船体，在 Alpha 中每秒 30 HP
- **头领被击毁后**：头领被击毁后 30 秒，随从会离开，除非它们正在攻击
- **回归**：头领 被击毁 {{guide:vitals.respawn@Boss Phantasm#1;Boss Phantasm#2;Boss Phantasm#3}} 后， 在同一星区
- **通知**：该星区的飞行员会被告知头领何时出现、何时被击毁。这些是系统行：它们显示在聊天的**系统**标签页中，带有未读计数，不会出现在**全球**或**本地**标签页里。击杀播报会写明获得这次击杀功劳的飞行员。

<!-- phantasm-glance:end -->

## 成员 {#the-members}

- **Boss Phantasm**: 一只更大的 Phantasm，带有虫群的色调，头顶显示名字，拥有自己的船体、护盾和激光齐射（数值见下）。它是被动的：一直游荡，直到有飞行员击中它，然后追上该飞行员并向其开火，附近的虫群舰船会加入战斗。它的武器射程和速度与 Phantasm 相同，也从不自己修复船体。它的[三个阶段](#the-leaders-three-steps)和[特殊能力](/wiki/03-Mechanics/Special-Abilities.md)可能改变这一点。
- **Phantasm Guard**: 一只带有虫群色调的较小 Phantasm。Guard 待在 Boss 附近，附近的虫群舰船被击中时就会加入战斗，每只靠近 Boss 的 Guard 都会为它的船体治疗。Guard 休息一段时间后会修复自己的船体，和 Phantasm 一样。

## 战斗过程 {#how-the-fight-goes}

- **带上一队人。** 三名 4–5 级、使用 x2 弹药的飞行员，在 Alpha 中大约一分半钟就能击毁它，至多损失一艘舰船；这个等级的飞行员单独一人会被击毁，两人只能险胜，而且只在伤害被分摊时才行。更好的舰船和 x4 弹药会快得多。
- **打 Boss，别打 Guard。** Guard 几秒钟就会倒下，但新的会按*一览*列表所说的频率到来，而 Guard 的治疗量只是一队人造成伤害的一小部分：放着它们不管只会多花一点时间，追着它们打则要多花更多时间。
- **Beta 和 Gamma 更难。** 这些世界的虫群更强（[世界](/wiki/05-Swarms/Swarms.md#the-worlds)），所以需要更多飞行员或更好的弹药。
- **留意星区。** `x-4` 在 Alpha 中是 PvP 星区，在 Beta 和 Gamma 中 `x-3` 和 `x-4` 都是（[世界](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)）：对手可能加入战斗，或等着拿货箱。让队里的一艘舰船放哨。
- **Boss 会回来**，在*一览*列表给出的时间之后，满状态，出现在同一个星区，它的 Guard 会一只接一只地到来。

## 首领的三个阶段 {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

这场战斗有三个阶段（[运作方式](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)）；每个只发生一次。

- **开始时**: 它的每个Phantasm Guards都会撑起一层相当于自身船体 10% 的护盾。
- **低于三分之二时**: 出现 3 个它的分身，真身带一圈光环。
- **低于三分之一时**: 闪现到离飞行员约 2,500 单位的地方，它的Phantasm Guards完好无损地回到它周围。

<!-- mob-ladder:end -->

## 奖励与掉落 {#rewards-and-drops}

Boss Phantasm 的奖励与这场战斗的分量相称：与它战斗一分钟的收益高于与 Goombah（这些星区报酬最高的外星人）战斗一分钟。奖励按伤害在与它战斗的飞行员之间分配（[Boss 击杀如何支付奖励](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)）。它的货箱归造成伤害最多的飞行员，里面有数倍于 Phantasm 的掉落（Ship Fragment、Daraxium 和 Nyxite），外加弹药和火箭。Guard 的奖励很少，也不掉落任何东西；击杀它们不算刷资源，因为它们会随 Boss 一起回来。

## 数值 {#the-numbers}

虫群舰船在三个世界中的数值（[世界](/wiki/05-Swarms/Swarms.md#the-worlds)）。

<!-- phantasm-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Phantasm

基于 Phantasm，拥有其 2,000% 的船体和 300% 的激光伤害；速度和射程与原舰船相同。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@Boss Phantasm#1}} | {{guide:vitals.hull@Boss Phantasm#2}} | {{guide:vitals.hull@Boss Phantasm#3}} |
| 护盾 | {{guide:vitals.shield@Boss Phantasm#1}} | {{guide:vitals.shield@Boss Phantasm#2}} | {{guide:vitals.shield@Boss Phantasm#3}} |
| 激光伤害 （每秒一轮齐射） | {{guide:vitals.dps@Boss Phantasm#1}} | {{guide:vitals.dps@Boss Phantasm#2}} | {{guide:vitals.dps@Boss Phantasm#3}} |
| 速度 | {{guide:vitals.speed@Boss Phantasm#1}} | {{guide:vitals.speed@Boss Phantasm#2}} | {{guide:vitals.speed@Boss Phantasm#3}} |
| 激光射程 | 700 | 700 | 700 |
| 仇恨范围 | 被攻击时 | 被攻击时 | 被攻击时 |
| 信用点 | {{guide:spoils.pay.credits@Boss Phantasm#1}} | {{guide:spoils.pay.credits@Boss Phantasm#2}} | {{guide:spoils.pay.credits@Boss Phantasm#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Phantasm#1}} | {{guide:spoils.pay.thulium@Boss Phantasm#2}} | {{guide:spoils.pay.thulium@Boss Phantasm#3}} |
| 经验值（XP） | {{guide:spoils.pay.experience@Boss Phantasm#1}} | {{guide:spoils.pay.experience@Boss Phantasm#2}} | {{guide:spoils.pay.experience@Boss Phantasm#3}} |
| 荣誉 | {{guide:spoils.pay.honor@Boss Phantasm#1}} | {{guide:spoils.pay.honor@Boss Phantasm#2}} | {{guide:spoils.pay.honor@Boss Phantasm#3}} |
| 每次击杀的 PvE 积分 | 8 | 8 | 8 |

**掉落**：一个货箱，归造成伤害最多的飞行员。

| 物品 |
| :--- |
| {{guide:spoils.box@Boss Phantasm#1;Boss Phantasm#2;Boss Phantasm#3}} |

### Phantasm Guard

基于 Phantasm，拥有其 50% 的船体、护盾和伤害；速度和射程与原舰船相同。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@Phantasm Guard#1}} | {{guide:vitals.hull@Phantasm Guard#2}} | {{guide:vitals.hull@Phantasm Guard#3}} |
| 护盾 | {{guide:vitals.shield@Phantasm Guard#1}} | {{guide:vitals.shield@Phantasm Guard#2}} | {{guide:vitals.shield@Phantasm Guard#3}} |
| 激光伤害 （每秒一轮齐射） | {{guide:vitals.dps@Phantasm Guard#1}} | {{guide:vitals.dps@Phantasm Guard#2}} | {{guide:vitals.dps@Phantasm Guard#3}} |
| 速度 | {{guide:vitals.speed@Phantasm Guard#1}} | {{guide:vitals.speed@Phantasm Guard#2}} | {{guide:vitals.speed@Phantasm Guard#3}} |
| 激光射程 | 700 | 700 | 700 |
| 仇恨范围 | 被攻击时 | 被攻击时 | 被攻击时 |
| 治疗头领 （每个，每秒，仅船体） | 30 | 45 | 60 |
| 信用点 | {{guide:spoils.pay.credits@Phantasm Guard#1}} | {{guide:spoils.pay.credits@Phantasm Guard#2}} | {{guide:spoils.pay.credits@Phantasm Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Phantasm Guard#1}} | {{guide:spoils.pay.thulium@Phantasm Guard#2}} | {{guide:spoils.pay.thulium@Phantasm Guard#3}} |
| 经验值（XP） | {{guide:spoils.pay.experience@Phantasm Guard#1}} | {{guide:spoils.pay.experience@Phantasm Guard#2}} | {{guide:spoils.pay.experience@Phantasm Guard#3}} |
| 荣誉 | {{guide:spoils.pay.honor@Phantasm Guard#1}} | {{guide:spoils.pay.honor@Phantasm Guard#2}} | {{guide:spoils.pay.honor@Phantasm Guard#3}} |
| 每次击杀的 PvE 积分 | 1 | 1 | 1 |

**掉落**：无。击杀只支付信用点、Thulium、经验值和荣誉。

<!-- phantasm-members:end -->
