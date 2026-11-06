<!-- wiki-i18n source: 7859e3f6a7efac1e -->
<!-- wiki-i18n title: Goombah 虫群 -->
# Goombah 虫群 {#goombah-swarm}

Goombah 虫群由一个 **Boss Goombah** 和它的 **Goombah Guard** 组成：一只从不主动开战的巨型 [Goombah](/wiki/04-Aliens/Goombah.md)，以及待在它附近并为它治疗的较小个体。它与 [Phantasm 虫群](/wiki/05-Swarms/Phantasm-Swarm.md) 出没在同样的星区 `x-3` 和 `x-4`，适合一队企业星区中最强的飞行员来战斗。

## 一览 {#at-a-glance}

<!-- goombah-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **位置**：每个企业的 `x-3` 和 `x-4` 星区
- **数量**：每个星区 一个， 每个世界 共 6 个
- **出现**：从赛季第 4 天起，直到重置（Beta 和 Gamma：从赛季第 1 天起）
- **头领**：Boss Goombah
- **随从**：最多 4 × Goombah Guard， 每 10 秒 出现 一个新的
- **随从停留范围**：距头领不超过 500 单位
- **治疗**：距头领 600 单位以内的每个 Goombah Guard 都会治疗它的船体，在 Alpha 中每秒 110 HP
- **头领被击毁后**：头领被击毁后 30 秒，随从会离开，除非它们正在攻击
- **回归**：头领 被击毁 5 分钟 后， 在同一星区
- **通知**：该星区的飞行员会被告知头领何时出现、何时被击毁。这些是系统行：它们显示在聊天的**系统**标签页中，带有未读计数，不会出现在**全球**或**本地**标签页里。击杀播报会写明获得这次击杀功劳的飞行员。

<!-- goombah-glance:end -->

## 成员 {#the-members}

- **Boss Goombah**: 一只更大的 Goombah，带有虫群的色调，头顶显示名字，拥有自己的船体、护盾和激光齐射（数值见下）。它是被动的：一直游荡，直到有飞行员击中它，然后追上该飞行员并向其开火，附近的虫群舰船会加入战斗。它的武器射程和速度与 Goombah 相同，也从不自己修复船体。
- **Goombah Guard**: 一只带有虫群色调的较小 Goombah。Guard 待在 Boss 附近，附近的虫群舰船被击中时就会加入战斗，每只靠近 Boss 的 Guard 都会为它的船体治疗。Guard 休息一段时间后会修复自己的船体，和 Goombah 一样。

## 战斗过程 {#how-the-fight-goes}

- **带上一队最强舰船。** 三名 8 级、使用 x2 弹药的飞行员，在 Alpha 中大约 75 秒就能击毁它，至多损失一艘舰船；其中两人需要 x4 弹药，等级更低的飞行员造成的伤害不足以获胜。
- **打 Boss，别打 Guard。** Guard 几秒钟就会倒下，但新的会按*一览*列表所说的频率到来，而 Guard 的治疗量只是一队人造成伤害的一小部分：放着它们不管只会多花一点时间，追着它们打则要多花更多时间。
- **Beta 和 Gamma 更难。** 这些世界的虫群更强（[世界](/wiki/05-Swarms/Swarms.md#the-worlds)），所以需要更多飞行员或更好的弹药。
- **留意星区。** `x-4` 在 Alpha 中是 PvP 星区，在 Beta 和 Gamma 中 `x-3` 和 `x-4` 都是（[世界](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)）：对手可能加入战斗，或等着拿货箱。让队里的一艘舰船放哨。
- **Boss 会回来**，在*一览*列表给出的时间之后，满状态，出现在同一个星区，它的 Guard 会一只接一只地到来。

## 奖励与掉落 {#rewards-and-drops}

Boss Goombah 的奖励与这场战斗的分量相称：与它战斗一分钟的收益高于与 Goombah（这些星区报酬最高的外星人）战斗一分钟。奖励按伤害在与它战斗的飞行员之间分配（[Boss 击杀如何支付奖励](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)）。它的货箱归造成伤害最多的飞行员，里面有数倍于 Goombah 的掉落（Cataclysite、Quorvium、Power Core、Reinforced Hull Plate 和 Ship Fragment），外加弹药和火箭。Guard 的奖励很少，也不掉落任何东西；击杀它们不算刷资源，因为它们会随 Boss 一起回来。

## 数值 {#the-numbers}

虫群舰船在三个世界中的数值（[世界](/wiki/05-Swarms/Swarms.md#the-worlds)）。

<!-- goombah-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Goombah

基于 Goombah，拥有其 400% 的船体和 100% 的激光伤害；速度和射程与原舰船相同。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | 128,000 | 192,000 | 256,000 |
| 护盾 | 192,000 | 288,000 | 384,000 |
| 激光伤害 （每秒一轮齐射） | 3,000 | 4,500 | 6,000 |
| 速度 | 180 | 180 | 180 |
| 激光射程 | 800 | 800 | 800 |
| 仇恨范围 | 被攻击时 | 被攻击时 | 被攻击时 |
| 信用点 | 120,000 | 240,000 | 360,000 |
| Thulium | 600 | 1,200 | 1,800 |
| 经验值（XP） | 24,000 | 48,000 | 72,000 |
| 荣誉 | 192 | 384 | 576 |
| 每次击杀的 PvE 积分 | 14 | 14 | 14 |

**掉落**：一个货箱，归造成伤害最多的飞行员。

| 物品 | 几率 | 数量 |
| :--- | ---: | ---: |
| Ship Fragment | 8 次判定中每次 100% | 3 |
| Reinforced Hull Plate | 8 次判定中每次 60% | 1 |
| Power Core | 8 次判定中每次 25% | 1 |
| Cataclysite | 8 次判定中每次 100% | 4 |
| Quorvium | 8 次判定中每次 100% | 2–4 |
| Advanced Plasma | 100% | 100–200 |
| Ultra Core | 100% | 100–200 |
| 可用信用点购买的 8 种 [火箭](/wiki/06-Items/Rockets.md) 中随机一种 | 100% | 6–10 |

### Goombah Guard

基于 Goombah，拥有其 20% 的船体、护盾和伤害；速度和射程与原舰船相同。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | 6,400 | 9,600 | 12,800 |
| 护盾 | 9,600 | 14,400 | 19,200 |
| 激光伤害 （每秒一轮齐射） | 600 | 900 | 1,200 |
| 速度 | 180 | 180 | 180 |
| 激光射程 | 800 | 800 | 800 |
| 仇恨范围 | 被攻击时 | 被攻击时 | 被攻击时 |
| 治疗头领 （每个，每秒，仅船体） | 110 | 165 | 220 |
| 信用点 | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| 经验值（XP） | 12 | 24 | 36 |
| 荣誉 | 1 | 2 | 3 |
| 每次击杀的 PvE 积分 | 3 | 3 | 3 |

**掉落**：无。击杀只支付信用点、Thulium、经验值和荣誉。

<!-- goombah-members:end -->
