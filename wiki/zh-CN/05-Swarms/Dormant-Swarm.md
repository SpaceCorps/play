<!-- wiki-i18n source: 7b6c7a0bdcd6cfbd -->
<!-- wiki-i18n title: Dormant 虫群 -->
# Dormant 虫群 {#dormant-swarm}

Dormant 虫群由一个 **Dormant Force** 和它的 **Dormant Pulse** 组成：一群从不主动开战、一旦被唤醒就出手极重的舰船。每个世界只有一个。它在各个危险星区之间游荡，是所有虫群中最难的战斗、最丰厚的掉落：这是一场需要由最强舰船组成的大型小队来打的战斗。

## 一览 {#at-a-glance}

<!-- dormant-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **位置**：危险星区 `DS-1`, `DS-2`, `DS-3`, `DS-4`， 在它们之间 飞行
- **数量**：每个世界一个
- **出现**：从赛季第 4 天起，直到重置
- **头领**：Dormant Force
- **随从**：2 × Dormant Pulse， 与头领 一同飞行
- **随从停留范围**：距头领不超过 700 单位
- **头领被击毁后**：Dormant Pulse 接任头领
- **移动**：在一张地图上停留 8 至 15 分钟，然后飞向另一个危险星区的传送门。它从不使用通往危险星区之外的传送门，也从不进入黑洞的环带
- **回归**：整个虫群 被击毁 1 小时 后， 在随机的 危险星区
- **通知**：整个世界的飞行员会被告知虫群何时出现、何时被击毁。这些是系统行：它们显示在聊天的**系统**标签页中，带有未读计数，不会出现在**全球**或**本地**标签页里。危险星区的地图和星系地图上会标出它。击杀播报会写明获得这次击杀功劳的飞行员。

<!-- dormant-glance:end -->

## 成员 {#the-members}

- **Dormant Force**：满强度的 Wraith，激光的威力是典型配置的三倍。它带领虫群，被击中之前是被动的，会向第一个击中它的飞行员发射**直线火箭**。
- **Dormant Pulse**：满强度的 Paragon，拥有同类的重型激光，每道激光的威力是 Force 激光的两倍，另有自己的火箭。Pulse 的激光比 Force 少，所以它的整轮齐射比 Force 的大，但不是两倍（具体数值见下方）。Pulse 飞在 Force 附近，Force 被击毁后，其中一艘接任头领。

它们都是被动的：从不主动攻击飞行员。其中一艘被击中时，附近的其他成员会加入战斗，对付第一个击中它的飞行员。

## 战斗过程 {#how-the-fight-goes}

- **找到它。** 它出现时整个世界都会收到通知，并在危险星区的地图和星系地图上标出。它会在一张地图上停留*一览*列表给出的时间，然后飞向另一个危险星区的传送门并跃迁；它从不使用通往危险星区之外的传送门，也从不进入黑洞的环带。它以最慢那艘舰船的速度飞行，并且和飞行员一样，在受到攻击时不会开始或结束跃迁。
- **一个人或少数几个人打不赢它。** 八名 8 级飞行员驾驶 Paragon、使用 x2 或 x4 弹药，在 Alpha 中大约一分钟就能将它击毁，最多损失一艘舰船；单独一艘 Paragon 会被击毁，使用 x2 弹药的三艘或四艘也一样。Beta 和 Gamma 的虫群更强（[世界](/wiki/05-Swarms/Swarms.md#the-worlds)），所以那些世界需要更大的小队。
- **它的激光决定战斗。** 它们加在一起，不到一分钟就能击毁一艘 Paragon，装备最好护盾的也不到两分钟，不用火箭也一样：用你拥有的最好的护盾，尽快打出伤害。
- **一艘接一艘。** 每艘舰船都有自己的船体和自己的奖励，所以 Force 或某个 Pulse 可能先被击毁。只有整个虫群都被击毁之后，才会在*一览*列表给出的时间后重新出现。

## 奖励与掉落 {#rewards-and-drops}

每艘舰船都单独支付奖励，按它所受的伤害计算（[Boss 击杀如何支付奖励](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)），并各自为对它造成伤害最多的飞行员掉落一个货箱。**Force 的货箱**是大奖：大量 x3 和 x4 弹药、同一种史诗级火箭，偶尔还有一枚 N.I.K.E. 或 N.U.K.E.。**Pulse** 可能掉落 Ancient Control Unit、Power Core 或 Dark Matter。与这个虫群战斗一分钟的收益高于与 Crystalys（报酬最高的外星人）战斗一分钟。

## 数值 {#the-numbers}

虫群舰船在三个世界中的数值（[世界](/wiki/05-Swarms/Swarms.md#the-worlds)）。

<!-- dormant-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Dormant Force

基于 Wraith，拥有其 100% 的船体和 300% 的激光伤害；速度和射程与原舰船相同。每 5 秒发射一枚直线火箭：[Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets)。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | 324,000 | 486,000 | 648,000 |
| 护盾 | 83,400 | 125,100 | 166,800 |
| 激光伤害 （每秒一轮齐射） | 2,880 | 4,320 | 5,760 |
| 速度 | 220 | 220 | 220 |
| 激光射程 | 800 | 800 | 800 |
| 仇恨范围 | 被攻击时 | 被攻击时 | 被攻击时 |
| 火箭伤害 （最高） | 7,500 | 11,250 | 15,000 |
| 信用点 | 200,000 | 400,000 | 600,000 |
| Thulium | 535 | 1,070 | 1,605 |
| 经验值（XP） | 32,100 | 64,200 | 96,300 |
| 荣誉 | 139 | 278 | 417 |
| 每次击杀的 PvE 积分 | 25 | 25 | 25 |

**掉落**：一个货箱，归造成伤害最多的飞行员。

| 物品 | 几率 | 数量 |
| :--- | ---: | ---: |
| Ultra Core 和 Experimental Fusion Core， 平均分配 | 100% | 共 2,000–3,000 |
| 4 种史诗级 [火箭](/wiki/06-Items/Rockets.md) 中随机一种 | 100% | 30–50 |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) 和 [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) 中随机一种 | 50% | 1 |

### Dormant Pulse

基于 Paragon，拥有其 100% 的船体和 600% 的激光伤害；速度和射程与原舰船相同。每 5 秒发射一枚直线火箭：[Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets)。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | 128,000 | 192,000 | 256,000 |
| 护盾 | 64,570 | 96,855 | 129,140 |
| 激光伤害 （每秒一轮齐射） | 3,840 | 5,760 | 7,680 |
| 速度 | 210 | 210 | 210 |
| 激光射程 | 800 | 800 | 800 |
| 仇恨范围 | 被攻击时 | 被攻击时 | 被攻击时 |
| 火箭伤害 （最高） | 5,000 | 7,500 | 10,000 |
| 信用点 | 95,000 | 190,000 | 285,000 |
| Thulium | 255 | 510 | 765 |
| 经验值（XP） | 15,200 | 30,400 | 45,600 |
| 荣誉 | 66 | 132 | 198 |
| 每次击杀的 PvE 积分 | 11 | 11 | 11 |

**掉落**：一个货箱，归造成伤害最多的飞行员。

| 物品 | 几率 | 数量 |
| :--- | ---: | ---: |
| Ancient Control Unit | 20% | 1 |
| Power Core | 20% | 1 |
| Dark Matter | 20% | 1–5 |

<!-- dormant-members:end -->
