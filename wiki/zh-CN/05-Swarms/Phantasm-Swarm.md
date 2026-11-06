<!-- wiki-i18n source: c21ae6d189180cd7 -->
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
- **回归**：头领 被击毁 2 分钟 后， 在同一星区
- **通知**：该星区的飞行员会被告知头领何时出现、何时被击毁。这些是系统行：它们显示在聊天的**系统**标签页中，带有未读计数，不会出现在**全球**或**本地**标签页里。击杀播报会写明获得这次击杀功劳的飞行员。

<!-- phantasm-glance:end -->

## 成员 {#the-members}

- **Boss Phantasm**: 一只更大的 Phantasm，带有虫群的色调，头顶显示名字，拥有自己的船体、护盾和激光齐射（数值见下）。它是被动的：一直游荡，直到有飞行员击中它，然后追上该飞行员并向其开火，附近的虫群舰船会加入战斗。它的武器射程和速度与 Phantasm 相同，也从不自己修复船体。
- **Phantasm Guard**: 一只带有虫群色调的较小 Phantasm。Guard 待在 Boss 附近，附近的虫群舰船被击中时就会加入战斗，每只靠近 Boss 的 Guard 都会为它的船体治疗。Guard 休息一段时间后会修复自己的船体，和 Phantasm 一样。

## 战斗过程 {#how-the-fight-goes}

- **带上一队人。** 三名 4–5 级、使用 x2 弹药的飞行员，在 Alpha 中大约一分半钟就能击毁它，至多损失一艘舰船；这个等级的飞行员单独一人会被击毁，两人也一样。更好的舰船和 x4 弹药会快得多。
- **打 Boss，别打 Guard。** Guard 几秒钟就会倒下，但新的会按*一览*列表所说的频率到来，而 Guard 的治疗量只是一队人造成伤害的一小部分：放着它们不管只会多花一点时间，追着它们打则要多花更多时间。
- **Beta 和 Gamma 更难。** 这些世界的虫群更强（[世界](/wiki/05-Swarms/Swarms.md#the-worlds)），所以需要更多飞行员或更好的弹药。
- **留意星区。** `x-4` 在 Alpha 中是 PvP 星区，在 Beta 和 Gamma 中 `x-3` 和 `x-4` 都是（[世界](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)）：对手可能加入战斗，或等着拿货箱。让队里的一艘舰船放哨。
- **Boss 会回来**，在*一览*列表给出的时间之后，满状态，出现在同一个星区，它的 Guard 会一只接一只地到来。

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
| 船体 | 40,000 | 60,000 | 80,000 |
| 护盾 | 64,000 | 96,000 | 128,000 |
| 激光伤害 （每秒一轮齐射） | 1,050 | 1,575 | 2,100 |
| 速度 | 160 | 160 | 160 |
| 激光射程 | 700 | 700 | 700 |
| 仇恨范围 | 被攻击时 | 被攻击时 | 被攻击时 |
| 信用点 | 39,000 | 78,000 | 117,000 |
| Thulium | 195 | 390 | 585 |
| 经验值（XP） | 7,800 | 15,600 | 23,400 |
| 荣誉 | 62 | 124 | 186 |
| 每次击杀的 PvE 积分 | 8 | 8 | 8 |

**掉落**：一个货箱，归造成伤害最多的飞行员。

| 物品 | 几率 | 数量 |
| :--- | ---: | ---: |
| Ship Fragment | 13 次判定中每次 100% | 1 |
| Daraxium | 13 次判定中每次 60% | 1–2 |
| Nyxite | 13 次判定中每次 60% | 1–2 |
| Standard Battery | 100% | 600–1,200 |
| Advanced Plasma | 100% | 60–100 |
| Ultra Core | 100% | 10–20 |
| 可用信用点购买的 8 种 [火箭](/wiki/06-Items/Rockets.md) 中随机一种 | 100% | 4–6 |

### Phantasm Guard

基于 Phantasm，拥有其 50% 的船体、护盾和伤害；速度和射程与原舰船相同。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | 1,000 | 1,500 | 2,000 |
| 护盾 | 1,600 | 2,400 | 3,200 |
| 激光伤害 （每秒一轮齐射） | 175 | 263 | 350 |
| 速度 | 160 | 160 | 160 |
| 激光射程 | 700 | 700 | 700 |
| 仇恨范围 | 被攻击时 | 被攻击时 | 被攻击时 |
| 治疗头领 （每个，每秒，仅船体） | 30 | 45 | 60 |
| 信用点 | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| 经验值（XP） | 12 | 24 | 36 |
| 荣誉 | 1 | 2 | 3 |
| 每次击杀的 PvE 积分 | 1 | 1 | 1 |

**掉落**：无。击杀只支付信用点、Thulium、经验值和荣誉。

<!-- phantasm-members:end -->
