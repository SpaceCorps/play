<!-- wiki-i18n source: bbd76eb145ce6188 -->
<!-- wiki-i18n title: 虫群 -->
# 虫群 {#swarms}

**虫群**是在一个**头领**带领下游荡于银河某片区域的外星人群体：头领是一个 Boss，比周围任何外星人都强得多，有**随从**守卫它，其中两个虫群的随从还会为它治疗。虫群共有三个，每个都有自己的文章：

- [Seeker 虫群](/wiki/05-Swarms/Seeker-Swarm.md)：Boss Seeker 和它的 Seeker Slave，最小的虫群，出没在新手飞行员活动的星区。
- [Pirate 虫群](/wiki/05-Swarms/Pirate-Swarm.md)：Pirate Boss 和它的 Pirate Scout，需要小队长时间作战。
- [Dormant 虫群](/wiki/05-Swarms/Dormant-Swarm.md)：Dormant Force 和它的 Dormant Pulse，最强的虫群，掉落也最丰厚。

它们的舰船是**自成一类的外星人**：有自己的名字和自己的击杀计数，都不算作 Seeker、Phantasm 或任何其他外星人。虫群舰船的外形与它所基于的舰船相同，带有自己的色调，头顶显示名字；Boss Seeker 是一艘大得多的 Seeker。

## 三个虫群 {#the-three-swarms}

<!-- swarms-list:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| 虫群 | 位置 | 数量 | 头领 | 随从 | 回归 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**Pirate 虫群**](/wiki/05-Swarms/Pirate-Swarm.md) | 每个企业的 `x-2` 和 `x-3` 星区 | 每个星区 一个， 每个世界 共 6 个 | **Pirate Boss** | 最多 5 × Pirate Scout， 每 10 秒 出现 一个新的 | 头领 被击毁 2 分钟 后， 在同一星区 |
| [**Dormant 虫群**](/wiki/05-Swarms/Dormant-Swarm.md) | 危险星区 `DS-1`, `DS-2`, `DS-3`, `DS-4`， 在它们之间 飞行 | 每个世界一个 | **Dormant Force** | 2 × Dormant Pulse， 与头领 一同飞行 | 整个虫群 被击毁 1 小时 后， 在随机的 危险星区 |
| [**Seeker 虫群**](/wiki/05-Swarms/Seeker-Swarm.md) | 每个企业的 `x-1` 和 `x-2` 星区 | 每个星区 一个， 每个世界 共 6 个 | **Boss Seeker** | 最多 4 × Seeker Slave， 每 10 秒 出现 一个新的 | 头领 被击毁 2 分钟 后， 在同一星区 |

<!-- swarms-list:end -->

## 何时何地 {#when-and-where}

虫群从**初次接触**起开始出现，并一直留到重置（见[重置时间线](/wiki/03-Mechanics/Wipe-Timeline.md)；具体日期在下面规则的第一行）。**每个世界都有自己的虫群**，位置相同，所以 Alpha 的 Pirate Boss 和 Beta 的 Pirate Boss 是两艘不同的舰船，你在自己世界击毁的虫群，在别的世界里并未被击毁。被击毁的虫群会在上表给出的时间后回来。

## 每个虫群的规则 {#the-rules-of-every-swarm}

<!-- swarms-rules:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- 虫群从赛季第 4 天起出现，直到重置。
- 虫群舰船被击中时，其所在虫群中距它 1,500 单位以内的舰船会加入战斗，对付第一个击中它的飞行员。
- 头领出现的位置距离每个空间站和传送门环带的边缘至少 2,500 单位。
- 对 Boss 造成的伤害占比不低于 5% 的飞行员，会为这次击杀获得奖励。

<!-- swarms-rules:end -->

## 世界 {#the-worlds}

世界对虫群的强化与对所有外星人一样（[世界](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)）：虫群舰船的船体、护盾、护盾充能、激光伤害、火箭伤害和治疗量，都是 Alpha 的数值乘以下面的强度，击杀则按下面的奖励倍率支付。速度、射程和掉落在所有世界中相同。各篇文章给出了每艘舰船在三个世界中的数值。

<!-- swarms-world:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| 世界 | 强度 | 奖励倍率 |
| :--- | ---: | ---: |
| **Alpha** | ×1 | ×1 |
| **Beta** | ×1.5 | ×2 |
| **Gamma** | ×2 | ×3 |

<!-- swarms-world:end -->

## 飞行员会收到什么通知 {#what-the-pilots-are-told}

Seeker 虫群和 Pirate 虫群会在 Boss 出现和被击毁时，通知所在星区的飞行员。Dormant 虫群会通知整个世界，并在危险星区的地图和星系地图上标出，方便飞行员找到它。这些是系统行：它们显示在聊天的**系统**标签页中，带有未读计数，不会出现在**全球**或**本地**标签页里。击杀 Boss 还会在击杀播报中生成一行，写明获得这次击杀功劳的飞行员。各篇文章的*一览*列表说明了会通知谁。

## 与虫群作战 {#fighting-a-swarm}

- **头领从不主动开战。** 头领会一直游荡，直到有飞行员击中它，然后还击，它附近的虫群舰船会加入战斗，对付第一个击中它的飞行员（距离见上面的规则）。Pirate Scout 是例外：它们会攻击任何靠近的飞行员。头领从不自己修复船体，所以你造成的伤害会留在它身上，除非它的随从为它治疗；它的护盾和任何外星人一样会重新充能。
- **虫群舰船只与飞行员作战。** 它们不向外星人开火，外星人也不向它们开火，[企业飞行员](/wiki/03-Mechanics/Company-Pilots.md)会无视它们：既不猎杀虫群舰船，也不会前来帮你对付它。
- **火箭。** Pirate Boss、Dormant Force 和 Pulse 会向攻击它们的飞行员发射**直线**火箭，即 [Rivet 火箭](/wiki/06-Items/Rockets.md)。保持移动的舰船可以躲开，原地不动的舰船则会被击中。
- **战斗的规模。** Seeker 虫群适合两名飞行员，Pirate 虫群适合小规模小队，Dormant 虫群适合由最强舰船组成的大型小队；更高的世界需要更多飞行员，和任何外星人一样。

## 该带什么 {#what-to-bring}

- **一支小队。** 组成[小队](/wiki/03-Mechanics/Groups.md)飞行：虫群是按小队来平衡的，低等级的单人飞行员很快就会被击毁，只有最强的舰船才能单独击败 Pirate Boss。没有人能单独击败 Dormant 虫群。虫群会与第一个击中它的飞行员作战（[外星人与谁作战](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)），所以让小队里最结实的舰船先出手。
- **更好的弹药。** 带上 x2 或更好的弹药（见[激光与弹药](/wiki/06-Items/Lasers.md)）。虫群随从的治疗量可能超过小队用 x1 弹药造成的伤害。
- **护盾和修理**，为一场长战做准备：你舰船的技能（[技能](/wiki/03-Mechanics/Abilities.md)）在要打上几分钟的 Pirate 战斗中最为重要。
- **移动的空间。** 待在你射程占优的武器够不到的地方，面对火箭时保持移动。

## Boss 击杀如何支付奖励 {#how-a-boss-kill-pays}

普通外星人把奖励付给第一个击中它的飞行员（[战斗](/wiki/03-Mechanics/Combat.md#kill-rewards-first-hit-claims)）。虫群的头领和每个 Dormant Pulse 则改为**按造成的伤害**支付：

- **奖励按伤害分配。** 每个造成了不低于上面规则所给比例的伤害的飞行员都会获得奖励，与其造成的伤害成比例：这次击杀的信用点、Thulium、经验值和荣誉在他们之间分配。低于该比例的飞行员什么都得不到。
- **货箱归造成伤害最多的飞行员。** 和任何外星人一样，它在 30 秒内属于该飞行员（及其战队），之后任何人都可以拾取（[货箱](/wiki/03-Mechanics/Cargo.md)）。Dormant 的每艘舰船都有自己的伤害统计和自己的货箱。
- **随从照常支付**：Pirate Scout 和 Seeker Slave 把奖励付给第一个击中它们的飞行员，它们的奖励与 Boss 相比很少。
- **Boss 的奖励被设计得高于它周围的外星人。** 与 Pirate Boss 战斗一分钟的收益高于与 Goombah 战斗一分钟，Dormant 虫群还要更高；Boss Seeker 的奖励恰好是十只 Seeker。

每次击杀都以舰船自己的名字计入你的击杀统计，并为你的排名增加 PvE 积分：

<!-- swarms-points:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| 虫群舰船 | 虫群 | 每次击杀的 PvE 积分 |
| :--- | :--- | ---: |
| **Pirate Boss** | Pirate 虫群 | 10 |
| **Pirate Scout** | Pirate 虫群 | 1 |
| **Dormant Force** | Dormant 虫群 | 25 |
| **Dormant Pulse** | Dormant 虫群 | 10 |
| **Boss Seeker** | Seeker 虫群 | 5 |
| **Seeker Slave** | Seeker 虫群 | 1 |

<!-- swarms-points:end -->

虫群击杀不算作任何其他外星人的击杀：Boss Seeker 或 Seeker Slave 对于要求击杀 Seeker 的任务来说不是 Seeker，重置点数的里程碑（[重置时间线](/wiki/03-Mechanics/Wipe-Timeline.md#earning-wipe-points)）也只针对那五种外星人。
