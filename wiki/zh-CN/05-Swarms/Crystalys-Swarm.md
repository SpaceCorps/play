<!-- wiki-i18n source: 5f873edc2b653495 -->
<!-- wiki-i18n title: Crystalys 虫群 -->
# Crystalys 虫群 {#crystalys-swarm}

Crystalys 虫群由一个 **Boss Crystalys** 和它的 **Crystalys Guard** 组成：最坚韧的外星人 [Crystalys](/wiki/04-Aliens/Crystalys.md) 的放大版，带着待在它附近并为它治疗的守卫。它出没在[危险星区](/wiki/01-General/Danger-Sectors.md) `DS-1`、`DS-2` 和 `DS-3`，每个星区一只，从不离开自己的星区。危险星区是 PvP 星区，所以这场战斗适合一支由最强飞行员组成的大队，而且那里的危险不只是 Boss。

## 一览 {#at-a-glance}

<!-- crystalys-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **位置**：危险星区 `DS-1`, `DS-2`, `DS-3`
- **数量**：每个星区 一个， 每个世界 共 3 个
- **出现**：从赛季第 4 天起，直到重置（Beta 和 Gamma：从赛季第 1 天起）
- **头领**：Boss Crystalys
- **随从**：最多 3 × Crystalys Guard， 每 10 秒 出现 一个新的
- **随从停留范围**：距头领不超过 500 单位
- **治疗**：距头领 600 单位以内的每个 Crystalys Guard 都会治疗它的船体，在 Alpha 中每秒 250 HP
- **头领被击毁后**：头领被击毁后 30 秒，随从会离开，除非它们正在攻击
- **回归**：头领 被击毁 30 分钟 后， 在同一星区
- **通知**：该星区的飞行员会被告知头领何时出现、何时被击毁。这些是系统行：它们显示在聊天的**系统**标签页中，带有未读计数，不会出现在**全球**或**本地**标签页里。击杀播报会写明获得这次击杀功劳的飞行员。

<!-- crystalys-glance:end -->

## 成员 {#the-members}

- **Boss Crystalys**: 一只更大的 Crystalys，带有虫群的色调，头顶显示名字，拥有自己的船体、护盾和激光齐射（数值见下）。它是被动的：一直游荡，直到有飞行员击中它，然后追上该飞行员并向其开火，附近的虫群舰船会加入战斗。它的武器射程和速度与 Crystalys 相同，也从不自己修复船体。
- **Crystalys Guard**: 一只带有虫群色调的较小 Crystalys。Guard 待在 Boss 附近，附近的虫群舰船被击中时就会加入战斗，每只靠近 Boss 的 Guard 都会为它的船体治疗。Guard 休息一段时间后会修复自己的船体，和 Crystalys 一样。

## 战斗过程 {#how-the-fight-goes}

- **带上一支大队。** 在 Alpha 中，驾驶 Paragon 并使用 x2 弹药的 8 级飞行员，若其火力分散到各人身上，六人即可；若全部集中在一名飞行员身上，则需要九人；使用 x4 弹药则分别为五人和六人。人数越多，战斗结束得越早，损失的舰船也越少；单独一名飞行员会被击毁。
- **打 Boss，别打 Guard。** Guard 几秒钟就会倒下，但新的会按*一览*列表所说的频率到来，而 Guard 的治疗量只是一队人造成伤害的一小部分：放着它们不管只会多花一点时间，追着它们打则要多花更多时间。
- **Beta 和 Gamma 更难。** 这些世界的虫群更强（[世界](/wiki/05-Swarms/Swarms.md#the-worlds)），所以需要更多飞行员或更好的弹药。
- **危险星区是 PvP。** 对手可能在战斗中途攻击你们的队伍，并等着拿货箱：货箱在 30 秒内属于造成伤害最多的飞行员（及其战队），之后任何人都可以拾取（[货箱](/wiki/03-Mechanics/Cargo.md)）。别一个人去。
- **Boss 会回来**，在*一览*列表给出的时间之后，满状态，出现在同一个星区，它的 Guard 会一只接一只地到来。

## 奖励与掉落 {#rewards-and-drops}

Boss Crystalys 的奖励与这场战斗的分量相称：与它战斗一分钟的收益高于与 Crystalys（报酬最高的外星人）战斗一分钟。奖励按伤害在与它战斗的飞行员之间分配（[Boss 击杀如何支付奖励](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)）。它的货箱归造成伤害最多的飞行员，里面有 Cataclysite 和 Quorvium，偶尔还有 Power Core、Ancient Control Unit 或 Dark Matter，以及 x3 和 x4 弹药和史诗级火箭。Guard 的奖励很少，也不掉落任何东西；击杀它们不算刷资源，因为它们会随 Boss 一起回来。

## 数值 {#the-numbers}

虫群舰船在三个世界中的数值（[世界](/wiki/05-Swarms/Swarms.md#the-worlds)）。

<!-- crystalys-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Crystalys

基于 Crystalys，拥有其 350% 的船体和 100% 的激光伤害；速度和射程与原舰船相同。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | 896,000 | 1,344,000 | 1,792,000 |
| 护盾 | 560,000 | 840,000 | 1,120,000 |
| 激光伤害 （每秒一轮齐射） | 10,000 | 15,000 | 20,000 |
| 速度 | 230 | 230 | 230 |
| 激光射程 | 900 | 900 | 900 |
| 仇恨范围 | 被攻击时 | 被攻击时 | 被攻击时 |
| 信用点 | 393,750 | 787,500 | 1,181,250 |
| Thulium | 1,050 | 2,100 | 3,150 |
| 经验值（XP） | 63,000 | 126,000 | 189,000 |
| 荣誉 | 273 | 546 | 819 |
| 每次击杀的 PvE 积分 | 30 | 30 | 30 |

**掉落**：一个货箱，归造成伤害最多的飞行员。

| 物品 | 几率 | 数量 |
| :--- | ---: | ---: |
| Cataclysite | 2 次判定中每次 100% | 8 |
| Quorvium | 2 次判定中每次 100% | 6–10 |
| Power Core | 30% | 1 |
| Ancient Control Unit | 15% | 1 |
| Dark Matter | 4% | 1 |
| Ultra Core 和 Experimental Fusion Core， 平均分配 | 100% | 共 600–1,000 |
| 4 种史诗级 [火箭](/wiki/06-Items/Rockets.md) 中随机一种 | 100% | 8–15 |

### Crystalys Guard

基于 Crystalys，拥有其 15% 的船体、护盾和伤害；速度和射程与原舰船相同。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | 38,400 | 57,600 | 76,800 |
| 护盾 | 24,000 | 36,000 | 48,000 |
| 激光伤害 （每秒一轮齐射） | 1,500 | 2,250 | 3,000 |
| 速度 | 230 | 230 | 230 |
| 激光射程 | 900 | 900 | 900 |
| 仇恨范围 | 被攻击时 | 被攻击时 | 被攻击时 |
| 治疗头领 （每个，每秒，仅船体） | 250 | 375 | 500 |
| 信用点 | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| 经验值（XP） | 12 | 24 | 36 |
| 荣誉 | 1 | 2 | 3 |
| 每次击杀的 PvE 积分 | 6 | 6 | 6 |

**掉落**：无。击杀只支付信用点、Thulium、经验值和荣誉。

<!-- crystalys-members:end -->
