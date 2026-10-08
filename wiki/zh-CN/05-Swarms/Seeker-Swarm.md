<!-- wiki-i18n source: fff5cfd69e987468 -->
<!-- wiki-i18n title: Seeker 虫群 -->
# Seeker 虫群 {#seeker-swarm}

Seeker 虫群是[虫群](/wiki/05-Swarms/Swarms.md)中最小的一个：一个 **Boss Seeker** 和守卫并治疗它的 **Seeker Slave**。它出没在新手飞行员开始飞行的星区，所以是大多数飞行员遇到的第一个虫群。Boss Seeker 从不主动开战，但只要你向它开火，它就比它所基于的 [Seeker](/wiki/04-Aliens/Seeker.md) 危险得多。

## 一览 {#at-a-glance}

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **位置**：每个企业的 `x-1` 和 `x-2` 星区
- **数量**：每个星区 一个， 每个世界 共 6 个
- **出现**：从赛季第 4 天起，直到重置
- **头领**：Boss Seeker
- **随从**：最多 4 × Seeker Slave， 每 10 秒 出现 一个新的
- **随从停留范围**：距头领不超过 500 单位
- **治疗**：距头领 600 单位以内的每个 Seeker Slave 都会治疗它的船体，在 Alpha 中每秒 50 HP
- **头领被击毁后**：头领被击毁后 30 秒，随从会离开，除非它们正在攻击
- **回归**：头领 被击毁 2 分钟 后， 在同一星区
- **通知**：该星区的飞行员会被告知头领何时出现、何时被击毁。这些是系统行：它们显示在聊天的**系统**标签页中，带有未读计数，不会出现在**全球**或**本地**标签页里。击杀播报会写明获得这次击杀功劳的飞行员。

<!-- seeker-glance:end -->

## 成员 {#the-members}

- **Boss Seeker**：一只大得多的 Seeker，带有虫群的色调，头顶显示名字，船体、护盾和伤害是 Seeker 的好几倍（数值见下）。它是被动的：一直游荡，直到有飞行员击中它，然后就地停下，向该飞行员开火，附近的虫群舰船会加入战斗。它的武器射程和速度与 Seeker 相同，也从不自己修复船体。
- **Seeker Slave**：带有虫群色调的普通 Seeker。Slave 待在 Boss 附近，附近的虫群舰船被击中时就会加入战斗，每只靠近 Boss 的 Slave 都会为它的船体治疗。Slave 休息一段时间后会修复自己的船体，和 Seeker 一样。

## 战斗过程 {#how-the-fight-goes}

- **在你的舰船扛得住之前别去招惹它。** Boss Seeker 的打击比飞行员的第一艘舰船能承受的更重：新手飞行员还没有护盾的 Protos，一旦被 Boss 和它的 Slave 缠上，几秒钟就会被击毁。
- **待在射程之外。** Boss 和它的 Slave 比 Protos 慢，武器射程也比 Quantum Laser II 短（见[激光与弹药](/wiki/06-Items/Lasers.md)）：装备这种激光并待在其射程之外的飞行员，在它们开火时不会受到伤害。装备 Quantum Laser I 的飞行员无法待在射程之外。
- **Slave 的治疗比孤身新手的输出更快。** 它们加在一起的治疗量超过一名用 x1 弹药的飞行员的激光所造成的伤害，所以带上搭档和 x2 弹药。两名装备 Quantum Laser II 并保持距离的飞行员，在 Alpha 中大约一分钟就能击败 Boss，用 x2 弹药则快得多。
- **Boss 会回来**，在*一览*列表给出的时间之后，满状态，出现在同一个星区，它的 Slave 会一只接一只地到来。

## 奖励与掉落 {#rewards-and-drops}

Boss Seeker 的奖励**恰好是十只 Seeker**：Seeker 的信用点、Thulium、经验值和荣誉的十倍，按伤害在与它战斗的飞行员之间分配（[Boss 击杀如何支付奖励](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)）。它的货箱里有十只 Seeker 的掉落，外加低于史诗级的弹药和火箭，归造成伤害最多的飞行员。Slave 的奖励很少，也不掉落任何东西；击杀它们不算刷资源，因为它们会随 Boss 一起回来。

## 数值 {#the-numbers}

虫群舰船在三个世界中的数值（[世界](/wiki/05-Swarms/Swarms.md#the-worlds)）。

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker

基于 Seeker，拥有其 400% 的船体、护盾和伤害；速度和射程与原舰船相同。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | 3,200 | 4,800 | 6,400 |
| 护盾 | 3,200 | 4,800 | 6,400 |
| 激光伤害 （每秒一轮齐射） | 720 | 1,080 | 1,440 |
| 速度 | 120 | 120 | 120 |
| 激光射程 | 600 | 600 | 600 |
| 仇恨范围 | 被攻击时 | 被攻击时 | 被攻击时 |
| 信用点 | 10,000 | 20,000 | 30,000 |
| Thulium | 40 | 80 | 120 |
| 经验值（XP） | 1,000 | 2,000 | 3,000 |
| 荣誉 | 20 | 40 | 60 |
| 每次击杀的 PvE 积分 | 5 | 5 | 5 |

**掉落**：一个货箱，归造成伤害最多的飞行员。

| 物品 | 几率 | 数量 |
| :--- | ---: | ---: |
| Ship Fragment | 10 次判定中每次 20% | 1 |
| Daraxium | 10 次判定中每次 50% | 1–2 |
| Standard Battery | 100% | 200–400 |
| Advanced Plasma | 100% | 10–20 |
| Ultra Core | 100% | 2–4 |
| 可用信用点购买的 8 种 [火箭](/wiki/06-Items/Rockets.md) 中随机一种 | 100% | 2–3 |

### Seeker Slave

基于 Seeker，拥有其 100% 的船体、护盾和伤害；速度和射程与原舰船相同。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | 800 | 1,200 | 1,600 |
| 护盾 | 800 | 1,200 | 1,600 |
| 激光伤害 （每秒一轮齐射） | 180 | 270 | 360 |
| 速度 | 120 | 120 | 120 |
| 激光射程 | 600 | 600 | 600 |
| 仇恨范围 | 被攻击时 | 被攻击时 | 被攻击时 |
| 治疗头领 （每个，每秒，仅船体） | 50 | 75 | 100 |
| 信用点 | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| 经验值（XP） | 12 | 24 | 36 |
| 荣誉 | 1 | 2 | 3 |
| 每次击杀的 PvE 积分 | 1 | 1 | 1 |

**掉落**：无。击杀只支付信用点、Thulium、经验值和荣誉。

<!-- seeker-members:end -->
