<!-- wiki-i18n source: fcba1b51b68a9123 -->
<!-- wiki-i18n title: Dormant 虫群 -->
# Dormant 虫群 {#dormant-swarm}

Dormant 虫群由一个 **Dormant Force** 和它的 **Dormant Pulse** 组成：一群从不主动开战、一旦被唤醒就出手极重的舰船。每个世界的危险星区里只有一个（[Deep Void](/wiki/03-Mechanics/Deep-Void.md#the-dormant-swarms-visit) 另有每天一次的独立来访）。它在各个危险星区之间游荡，是所有虫群中最难的战斗、最丰厚的掉落：这是一场需要由最强舰船组成的大型小队来打的战斗。从赛季第 11 天起，它从 `DS-4` 的 [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) 开始，回归更早，奖励翻倍（见*概览*列表）。

## 一览 {#at-a-glance}

<!-- dormant-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **位置**：危险星区 `DS-1`, `DS-2`, `DS-3`, `DS-4`， 在它们之间 飞行
- **数量**：每个世界一个
- **出现**：从赛季第 4 天起，直到重置（Beta 和 Gamma：从赛季第 1 天起）
- **头领**：Dormant Force
- **随从**：2 × Dormant Pulse， 与头领 一同飞行
- **随从停留范围**：距头领不超过 700 单位
- **头领被击毁后**：Dormant Pulse 接任头领
- **头领被击毁后**：头领被击毁后 30 秒，随从会离开，即使它们正在攻击
- **移动**：在一张地图上停留 8 至 15 分钟，然后飞向另一个危险星区的传送门。它从不使用通往危险星区之外的传送门，也从不进入黑洞的环带
- **回归**：整个虫群 被击毁 {{guide:vitals.respawn@Dormant Force#1;Dormant Force#2;Dormant Force#3}} 后， 在随机的 危险星区
- **从赛季第 11 天起**：它出现在 `DS-4` 的 [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md)，而不是随机的危险星区；整个虫群被击毁 30 分钟 后回归；每艘飞船的奖励为 ×2（信用点、Thulium、XP 和荣誉；掉落不变）
- **通知**：整个世界的飞行员会被告知虫群何时出现、何时被击毁。这些是系统行：它们显示在聊天的**系统**标签页中，带有未读计数，不会出现在**全球**或**本地**标签页里。危险星区的地图和星系地图上会标出它。击杀播报会写明获得这次击杀功劳的飞行员。

<!-- dormant-glance:end -->

## 成员 {#the-members}

- **Dormant Force**：满强度的 Wraith，激光的威力是典型配置的三倍。它带领虫群，被击中之前是被动的，会向第一个击中它的飞行员发射**直线火箭**。
- **Dormant Pulse**：满强度的 Paragon，拥有同类的重型激光，每道激光的威力是 Force 激光的两倍，另有自己的火箭。Pulse 的激光比 Force 少，所以它的整轮齐射比 Force 的大，但不是两倍（具体数值见下方）。Pulse 飞在 Force 附近，Force 被击毁后，其中一艘接任头领。

它们都是被动的：从不主动攻击飞行员。其中一艘被击中时，附近的其他成员会加入战斗，对付第一个击中它的飞行员。

## 战斗过程 {#how-the-fight-goes}

- **找到它。** 它出现时整个世界都会收到通知，并在危险星区的地图和星系地图上标出。它会在一张地图上停留*一览*列表给出的时间，然后飞向另一个危险星区的传送门并跃迁；它从不使用通往危险星区之外的传送门，也从不进入黑洞的环带。它以最慢那艘舰船的速度飞行，并且和飞行员一样，在受到攻击时不会开始或结束跃迁。从赛季第 11 天起，它先出现在 [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) 区域的外面，小队可以在沼泽炮台打不到的地方等它，然后它从 `DS-4` 的一个传送门飞出。
- **一个人或少数几个人打不赢它。** 八名 8 级飞行员驾驶 Paragon、使用 x2 或 x4 弹药，在 Alpha 中大约一分钟就能将它击毁，最多损失一艘舰船；单独一艘 Paragon 会被击毁，使用 x2 弹药的三艘或四艘也一样。Beta 和 Gamma 的虫群更强（[世界](/wiki/05-Swarms/Swarms.md#the-worlds)），所以那些世界需要更大的小队。
- **它的激光决定战斗。** 它们加在一起，不到一分钟就能击毁一艘 Paragon，装备最好护盾的也不到两分钟，不用火箭也一样：用你拥有的最好的护盾，尽快打出伤害。
- **一艘接一艘。** 每艘舰船都有自己的船体和自己的奖励，所以 Force 或某个 Pulse 可能先被击毁。只有整个虫群都被击毁之后，才会在*一览*列表给出的时间后重新出现。

## 首领的三个阶段 {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

这场战斗有三个阶段（[运作方式](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)）；每个只发生一次。

- **开始时**: 只要它的某个Dormant Pulses还活着，它每次只承受 70% 的伤害。
- **低于三分之二时**: 它的Dormant Pulses在 15 秒 内每隔 2.5 秒 发射一枚火箭。
- **低于三分之一时**: 只要它的Dormant Pulses全部存活，它们就在 6 秒 内每秒为它修复船体的 5%。

<!-- mob-ladder:end -->

## 奖励与掉落 {#rewards-and-drops}

每艘舰船都单独支付奖励，按它所受的伤害计算（[Boss 击杀如何支付奖励](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)），并各自为对它造成伤害最多的飞行员掉落一个货箱。**Force 的货箱**是大奖：大量 x3 和 x4 弹药、同一种史诗级火箭，偶尔还有一枚 N.I.K.E. 或 N.U.K.E.。**Pulse** 可能掉落 Ancient Control Unit、Power Core 或 Dark Matter。与这个虫群战斗一分钟的收益高于与 Crystalys（报酬最高的外星人）战斗一分钟。从赛季第 11 天起，每艘飞船的奖励翻倍（见*概览*列表）；货箱不变。

## 数值 {#the-numbers}

虫群舰船在三个世界中的数值（[世界](/wiki/05-Swarms/Swarms.md#the-worlds)）。表中的信用点、Thulium、XP 和荣誉是赛季第 11 天之前的奖励；从那天起，一次击杀的奖励翻倍。

<!-- dormant-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Dormant Force

基于 Wraith，拥有其 100% 的船体和 300% 的激光伤害；速度和射程与原舰船相同。每 5 秒发射一枚直线火箭：[Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets)。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@Dormant Force#1}} | {{guide:vitals.hull@Dormant Force#2}} | {{guide:vitals.hull@Dormant Force#3}} |
| 护盾 | {{guide:vitals.shield@Dormant Force#1}} | {{guide:vitals.shield@Dormant Force#2}} | {{guide:vitals.shield@Dormant Force#3}} |
| 激光伤害 （每秒一轮齐射） | {{guide:vitals.dps@Dormant Force#1}} | {{guide:vitals.dps@Dormant Force#2}} | {{guide:vitals.dps@Dormant Force#3}} |
| 速度 | {{guide:vitals.speed@Dormant Force#1}} | {{guide:vitals.speed@Dormant Force#2}} | {{guide:vitals.speed@Dormant Force#3}} |
| 激光射程 | 800 | 800 | 800 |
| 仇恨范围 | 被攻击时 | 被攻击时 | 被攻击时 |
| 火箭伤害 （最高） | {{guide:behaviour.ability:rocket.damage@Dormant Force#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#3}} |
| 信用点 | {{guide:spoils.pay.credits@Dormant Force#1}} | {{guide:spoils.pay.credits@Dormant Force#2}} | {{guide:spoils.pay.credits@Dormant Force#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Force#1}} | {{guide:spoils.pay.thulium@Dormant Force#2}} | {{guide:spoils.pay.thulium@Dormant Force#3}} |
| 经验值（XP） | {{guide:spoils.pay.experience@Dormant Force#1}} | {{guide:spoils.pay.experience@Dormant Force#2}} | {{guide:spoils.pay.experience@Dormant Force#3}} |
| 荣誉 | {{guide:spoils.pay.honor@Dormant Force#1}} | {{guide:spoils.pay.honor@Dormant Force#2}} | {{guide:spoils.pay.honor@Dormant Force#3}} |
| 每次击杀的 PvE 积分 | 25 | 25 | 25 |

**掉落**：一个货箱，归造成伤害最多的飞行员。

| 物品 |
| :--- |
| {{guide:spoils.box@Dormant Force#1;Dormant Force#2;Dormant Force#3}} |

### Dormant Pulse

基于 Paragon，拥有其 100% 的船体和 600% 的激光伤害；速度和射程与原舰船相同。每 5 秒发射一枚直线火箭：[Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets)。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@Dormant Pulse#1}} | {{guide:vitals.hull@Dormant Pulse#2}} | {{guide:vitals.hull@Dormant Pulse#3}} |
| 护盾 | {{guide:vitals.shield@Dormant Pulse#1}} | {{guide:vitals.shield@Dormant Pulse#2}} | {{guide:vitals.shield@Dormant Pulse#3}} |
| 激光伤害 （每秒一轮齐射） | {{guide:vitals.dps@Dormant Pulse#1}} | {{guide:vitals.dps@Dormant Pulse#2}} | {{guide:vitals.dps@Dormant Pulse#3}} |
| 速度 | {{guide:vitals.speed@Dormant Pulse#1}} | {{guide:vitals.speed@Dormant Pulse#2}} | {{guide:vitals.speed@Dormant Pulse#3}} |
| 激光射程 | 800 | 800 | 800 |
| 仇恨范围 | 被攻击时 | 被攻击时 | 被攻击时 |
| 火箭伤害 （最高） | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#3}} |
| 信用点 | {{guide:spoils.pay.credits@Dormant Pulse#1}} | {{guide:spoils.pay.credits@Dormant Pulse#2}} | {{guide:spoils.pay.credits@Dormant Pulse#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Pulse#1}} | {{guide:spoils.pay.thulium@Dormant Pulse#2}} | {{guide:spoils.pay.thulium@Dormant Pulse#3}} |
| 经验值（XP） | {{guide:spoils.pay.experience@Dormant Pulse#1}} | {{guide:spoils.pay.experience@Dormant Pulse#2}} | {{guide:spoils.pay.experience@Dormant Pulse#3}} |
| 荣誉 | {{guide:spoils.pay.honor@Dormant Pulse#1}} | {{guide:spoils.pay.honor@Dormant Pulse#2}} | {{guide:spoils.pay.honor@Dormant Pulse#3}} |
| 每次击杀的 PvE 积分 | 11 | 11 | 11 |

**掉落**：一个货箱，归造成伤害最多的飞行员。

| 物品 |
| :--- |
| {{guide:spoils.box@Dormant Pulse#1;Dormant Pulse#2;Dormant Pulse#3}} |

<!-- dormant-members:end -->
