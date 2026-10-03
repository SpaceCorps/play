<!-- wiki-i18n source: f06b4c7b561b1789 -->
<!-- wiki-i18n title: Pirate 虫群 -->
# Pirate 虫群 {#pirate-swarm}

Pirate 虫群由一个 **Pirate Boss** 和它的 **Pirate Scout** 组成：Pirate Boss 是一艘庞大而缓慢的舰船，不攻击任何人，用火箭回应；Pirate Scout 是一群更快的舰船，守卫并治疗它。它出没在企业基地与边境之间的星区，也就是游戏中段等级活动的地方，对飞行员小队来说是一场持久战，而不是速战速决的击杀。

## 一览 {#at-a-glance}

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **位置**：每个企业的 `x-2` 和 `x-3` 星区
- **数量**：每个星区 一个， 每个世界 共 6 个
- **出现**：从赛季第 4 天起，直到重置
- **头领**：Pirate Boss
- **随从**：最多 5 × Pirate Scout， 每 10 秒 出现 一个新的
- **随从停留范围**：距头领不超过 900 单位
- **治疗**：距头领 600 单位以内的每个 Pirate Scout 都会治疗它的船体，在 Alpha 中每秒 40 HP
- **头领被击毁后**：头领被击毁后 1 分钟，随从会离开，除非它们正在攻击
- **回归**：头领 被击毁 2 分钟 后， 在同一星区
- **通知**：星区聊天会通知头领何时出现、何时被击毁。 击杀播报会写明获得这次击杀功劳的飞行员。

<!-- pirate-glance:end -->

## 成员 {#the-members}

- **Pirate Boss**：基于 Ironclad 的舰船，拥有它的一部分强度（数值见下）。它是被动的，**不发射激光**：它唯一的武器是**直线火箭**（[火箭](/wiki/06-Items/Rockets.md)；具体是哪种取决于星区，见表格），射向攻击它的飞行员，发射时它仍在游荡。它从不自己修复船体。
- **Pirate Scout**：基于 Kitefin 的舰船，拥有它的一部分强度。Scout 会攻击任何靠近的飞行员，待在 Boss 附近，每艘靠近 Boss 的 Scout 都会为它的船体治疗。

## 战斗过程 {#how-the-fight-goes}

- **打 Boss，不要打 Scout。** Scout 会治疗 Boss，但与 Boss 的船体相比，治疗量很小，而且新的 Scout 会按*一览*列表所说的频率出现：先击杀 Scout 的小队永远赶不上它们，只有非常庞大的小队才能清掉它们，而且仍比不去管它们的小队花更长时间击败 Boss。Scout 只会耗费你的时间，不会决定战斗。
- **把 Scout 引开。** Scout 只有在 Boss 的范围之内才会治疗，所以跟着你离开该范围的 Scout 什么也治疗不了，而 Ostirion 比 Scout 更快。
- **保持移动。** Boss 的火箭是直线的，不带制导：保持移动的舰船可以躲开，原地不动的舰船则会被击中。
- **带上小队。** 三名驾驶 Ostirion、使用 x2 弹药的飞行员，在 Alpha 中大约五分钟就能击败它；单独一艘 Ostirion 做不到，单独一艘 Paragon 可以。Boss 会应对第一个击中它的飞行员，所以让最结实的舰船先出手，并在这样的长战中使用你的技能（Emergency Repair、Shield Surge：[技能](/wiki/03-Mechanics/Abilities.md)）。仍是 2 级或 3 级的飞行员对它来说太弱，即使在他们活动的星区也是如此：变强之前请远离。
- **Boss 会回来**，在*一览*列表给出的时间之后，出现在同一个星区。

## 奖励与掉落 {#rewards-and-drops}

Pirate Boss 的奖励与这场战斗相称：与它战斗一分钟的收益高于与 Goombah 战斗一分钟。奖励按伤害在与它战斗的飞行员之间分配（[Boss 击杀如何支付奖励](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)）。它的货箱归造成伤害最多的飞行员，里面可能有 **Reinforced Hull Plate**、火箭和弹药。Scout 的奖励很少，也不掉落任何东西。

## 数值 {#the-numbers}

虫群舰船在三个世界中的数值（[世界](/wiki/05-Swarms/Swarms.md#the-worlds)）。

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss {#pirate-boss}

基于 Ironclad，拥有其 50% 的船体、护盾和伤害；速度和射程与原舰船相同。 每 5 秒发射一枚直线火箭：`x-2`：[Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets), `x-3`：[Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets)。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | 300,000 | 450,000 | 600,000 |
| 护盾 | 50,100 | 75,150 | 100,200 |
| 激光伤害 （每秒一轮齐射） | 无 | 无 | 无 |
| 速度 | 92 | 92 | 92 |
| 激光射程 | – | – | – |
| 仇恨范围 | 被攻击时 | 被攻击时 | 被攻击时 |
| 火箭伤害 （最高） | 2,500 (Rivet I) / 5,000 (Rivet II) | 3,750 (Rivet I) / 7,500 (Rivet II) | 5,000 (Rivet I) / 10,000 (Rivet II) |
| 信用点 | 116,000 | 232,000 | 348,000 |
| Thulium | 725 | 1,450 | 2,175 |
| 经验值（XP） | 29,000 | 58,000 | 87,000 |
| 荣誉 | 232 | 464 | 696 |
| 每次击杀的 PvE 积分 | 10 | 10 | 10 |

**掉落**：一个货箱，归造成伤害最多的飞行员。

| 物品 | 几率 | 数量 |
| :--- | ---: | ---: |
| Reinforced Hull Plate | 50% | 1 |
| 可用信用点购买的 8 种 [火箭](/wiki/06-Items/Rockets.md) 中随机一种 | 100% | 5–10 |
| Advanced Plasma 和 Siphon Battery 中随机一种 | 100% | 500–1,000 |

### Pirate Scout {#pirate-scout}

基于 Kitefin，拥有其 50% 的船体、护盾和伤害；速度和射程与原舰船相同。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | 12,000 | 18,000 | 24,000 |
| 护盾 | 9,818 | 14,727 | 19,636 |
| 激光伤害 （每秒一轮齐射） | 98 | 147 | 196 |
| 速度 | 175 | 175 | 175 |
| 激光射程 | 700 | 700 | 700 |
| 仇恨范围 | 700 | 700 | 700 |
| 治疗头领 （每个，每秒，仅船体） | 40 | 60 | 80 |
| 信用点 | 800 | 1,600 | 2,400 |
| Thulium | 4 | 8 | 12 |
| 经验值（XP） | 100 | 200 | 300 |
| 荣誉 | 2 | 4 | 6 |
| 每次击杀的 PvE 积分 | 1 | 1 | 1 |

**掉落**：无。击杀只支付信用点、Thulium、经验值和荣誉。

<!-- pirate-members:end -->
