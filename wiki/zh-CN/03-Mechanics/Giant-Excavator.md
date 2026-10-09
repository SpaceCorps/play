<!-- wiki-i18n source: 5df6b18400b138dc -->
<!-- wiki-i18n title: 巨型挖掘机 -->
# 巨型挖掘机 {#giant-excavator}

<!-- wiki-search: excavator; giant excavator; pulsar; mining; fuel; excavator fuel; control panel; overheat; radiation; slumbering void; voids; wave; ds-1; ds-2; ds-3; 挖掘机; 巨型挖掘机; 脉冲星; 燃料; 控制面板; 过热; 辐射; 波 -->

从赛季第 11 天起，危险星区 `DS-1`、`DS-2`、`DS-3` 中各有一颗**脉冲星**在闪耀，旁边立着一台**巨型挖掘机**。挖掘机从脉冲星中开采 **Thulium 和稀有矿石**，为此要燃烧 [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md)。任何人都可以给它加燃料、选择它开采什么并启动它，它产出的东西装在货箱里落在周围，谁都可以拾取。不过一次运转动静很大：它启动时整个世界都会得到通知，**Slumbering Void** 会成波来攻击它，而被开太久的挖掘机会过热，并让整片区域受到辐射。本页说明一次运转如何进行、它能产出什么、以及如何熬过它。星区见[危险星区](/wiki/01-General/Danger-Sectors.md)；Void 见 [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void)。

## 概览 {#at-a-glance}

<!-- excavator-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **位置**：每个世界里，`DS-1`, `DS-2` 和 `DS-3` 各有一颗脉冲星和一台巨型挖掘机
- **出现**：从赛季第 11 天起，直到重置
- **燃料**：Dark Matter。1 个能烧 10 分钟；燃料箱可放 3 个，即 30 分钟 的开采。任何人都可以从自己的货舱一次放入 1 个
- **面板**：窗口在距挖掘机 600 单位内可用，标签从 1,400 单位处开始显示。任何人都可以加燃料、选择和启动；运转期间选择被锁定
- **货箱**：每 20 秒 一个货箱，落在距挖掘机 450 到 900 单位之间，从落下的那一刻起任何人都可以拾取。它会存在 5 分钟，地图上同时最多有 24 个
- **热量**：累计 30 分钟 的开采（分多少次运转都行），挖掘机就会过热 1 小时。热量在运转之间会保留，休息之后消失
- **辐射**：过热或被摧毁期间，挖掘机（1,100 单位内）和它的脉冲星（1,300 单位内）会烧伤里面的每艘飞船：每秒其总 HP 的 10%
- **船体**：Alpha 为 200,000 HP，Beta 为 300,000，Gamma 为 400,000。只有 Slumbering Void 能伤到它，而且只在没有飞行员保护它时
- **Void**：开采期间每 2 分钟 来 2 个 Slumbering Void，第一波在启动后 1 分钟；地图上最多同时存活 8 个
- **通知**：一次运转启动、挖掘机过热、被摧毁时，整个世界的飞行员都会得到通知；其余通知发给它所在星区的飞行员。这些是系统行：显示在聊天的**系统**标签页和游戏日志中，不会出现在**全球**或**本地**标签页里。

<!-- excavator-glance:end -->

## 一次运转如何进行 {#how-a-run-goes}

1. **找到一台。** 三个有脉冲星的危险星区各有一台挖掘机，每个世界都有。你靠近时，上方会悬着标签**挖掘机**，星系地图会显示你所在星区挖掘机的状态。
2. **打开面板。** 点击标签。只要你的飞船在挖掘机控制面板的范围内，**巨型挖掘机**窗口就能使用（范围见*概览*列表）。隐形的飞船也能使用，使用不会解除隐形。
3. **加燃料。** **添加 Dark Matter** 会把你货舱里的 1 个 Dark Matter 放进燃料箱。任何人都可以。燃料箱接收的量绝不会超过挖掘机在过热前能烧完的量，所以不会浪费燃料。
4. **选择开采什么，**从列表中选择，然后按**开始采矿**。需要燃料箱里至少有 1 个 Dark Matter，并且选好了资源。启动之前任何人都可以更改选择；一旦运转，资源就被锁定。启动会连同你的名字、星区和资源一起通知世界上的所有飞行员。
5. **守住它。** 开采期间，每隔几秒就有一个货箱落在挖掘机周围，启动后不久第一批 Slumbering Void 就会抵达。保护挖掘机，拾取货箱。
6. **留意热量。** 热量条在挖掘机开采时上升，在它等待时也永远不会下降。到达上限时挖掘机会过热。请提前离开：游戏会向地图发出两次警告。
7. **它休息。** 过热或被摧毁后，挖掘机和它的脉冲星会持续辐射，直到休息结束；然后它重新就绪，热量归零，船体回满。

窗口还显示星区、燃料箱（每个 Dark Matter 一格，正在燃烧的那格只画一部分）、你携带的 Dark Matter 数量、挖掘机的船体、每种资源在你的世界里每分钟的产出，以及开采期间距下一波的时间和存活的 Void 数。当某个操作被拒绝时，你会看到红色的原因：离控制面板太远、没有 Dark Matter、燃料箱已满、还没有燃料或没选资源、运转期间资源被锁定，或者挖掘机很烫。

| 状态 | 含义 | 你能做什么 |
| :--- | :--- | :--- |
| **就绪** | 没有燃料，或有燃料但尚未启动。已有的热量会保留。 | 添加 Dark Matter、选择、启动。 |
| **采矿中** | 燃烧 Dark Matter 并积累热量；资源被锁定。 | 在剩余空间内继续添加 Dark Matter、与 Void 战斗、拾取货箱。 |
| **过热** | 热量达到上限。燃料箱被清空；已落下的货箱保留。 | 无。区域受到辐射：请远离。 |
| **已摧毁** | Void 把船体打到了零。燃料丢失，船体立刻回满。 | 无。区域受到辐射：请远离。 |

如果燃料在上限之前耗尽，挖掘机会带着保留的热量回到**就绪**，剩下的 Void 如果没在战斗，过一段时间就会离开。

## 它开采什么 {#what-it-mines}

满箱燃料的产出经过调整，大致等于两三名飞行员以最佳方式刷半小时 Thulium 的收入。Beta 和 Gamma 产出更多，就像它们每次击杀的奖励更高一样。每次运转你选一种资源。货箱对所有人都一样，Thulium 货箱是现金，拾取时才支付，和小行星的 Thulium 一样。

<!-- excavator-resources:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

满箱燃料（3 个 Dark Matter，开采 30 分钟）会产出下列数量，分装在 90 个货箱里。

| 资源 | Alpha | Beta | Gamma | 每分钟，Alpha | 每箱，Alpha |
| :--- | ---: | ---: | ---: | ---: | ---: |
| [Thulium](/wiki/06-Items/Resources.md#thulium) | 4,821 | 7,714 | 9,643 | 160.7 | 53.6 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | 1,157 | 1,851 | 2,314 | 38.6 | 12.9 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | 514 | 823 | 1,029 | 17.1 | 5.7 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | 320 | 320 | 320 | 10.7 | 3.6 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | 160 | 160 | 160 | 5.3 | 1.8 |

- Velkonite 或 Orvium 的一次运转，在每个世界里最多产出 20 级 [Skylab](/wiki/03-Mechanics/Skylab.md) 采集器 4 小时的该矿石（Velkonite 320、Orvium 160）：它们是 Skylab 的矿石，一次运转加快其节奏的幅度绝不会超过这个量。
- 一个货箱大约装有最后一列的数量，上下浮动 15%。Thulium 货箱是现金：拾取时支付。矿石货箱装的是物品。

<!-- excavator-resources:end -->

飞行员自己的增益器和对待其他货物一样起作用：Resource Magnet Booster 的加成会增加矿石货箱。货箱没有每日上限：限制一次运转的是燃料和时间。

**矿石的用途。** 货箱里的矿石像任何物品一样进入你的货舱。Cataclysite 和 Quorvium 用于装配站和锻造炉（[资源](/wiki/06-Items/Resources.md)）。Skylab 的锻造炉只从资源仓库取矿石，而资源仓库由采集器填充；所以货箱里的 Velkonite 和 Orvium 是[研究中心](/wiki/03-Mechanics/Research.md#fuel)的燃料，而不是锻造炉的。

## Slumbering Void {#the-slumbering-voids}

一次运转会引来 **Slumbering Void**，它们是失落文明的猎手，从地图边缘飞来，保护脉冲星不被想掏空它的人夺走。它们追猎挖掘机附近的飞行员，一旦没有可追猎的目标，就转而攻击挖掘机。Void 的数字和奖励见 [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void)。

<!-- excavator-voids:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **波次。** 每 2 分钟 来 2 个 Slumbering Void；第一波在启动后 1 分钟，运转的最后 1 分钟 不再来。地图上同时最多存活 8 个：遇到地图已满的一波会被跳过。
- **来袭。** 一波出现在地图边缘向内 900 单位、距每个传送门环至少 2,500 单位处，约 20 秒 飞到挖掘机。消息会写明它来自地图的哪一侧。
- **追猎。** Void 追猎 2,500 单位内它能看到的最近的飞行员，并留在距挖掘机 7,000 单位以内。
- **围攻。** 当 15 秒 内距挖掘机 7,000 单位以内没有它们能看到的飞行员时，Void 会攻击挖掘机，每道激光造成平时伤害的 25%。降到零时挖掘机被摧毁：燃料丢失，船体立刻回满，并休息 1 小时。
- **撤离。** 一次运转结束时，剩下的 Void 再停留 90 秒，若被攻击就继续战斗；然后离开。

<!-- excavator-voids:end -->

- **Void 是玻璃大炮。** 它的护盾很大，但会吸收一次命中的 80%，所以后面的船体只要受到自身数倍的伤害就会消失，有护盾穿透时则快得多。两三名装备良好的飞行员就能在 Alpha 守住一次运转；Beta 和 Gamma 需要更大的小队，和对付任何外星人一样。
- **隐形不能保卫现场。** Void 看不到隐形的飞船，所以躲起来的飞行员无法让它们远离挖掘机；躲进传送门环的飞行员无法被攻击到，也不算数。
- **每个 Void 都会支付奖励，**按你对它造成的伤害，并掉落一个货箱（[击杀首领如何支付](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)）。击杀它们会像击杀虫群飞船一样增加你的 PvE 军衔积分。

## 热量与辐射 {#heat-and-radiation}

采矿每秒都在增加热量。热量会**累积，并且在挖掘机等待期间永不冷却**：提前结束的一次运转会给下一名飞行员留下更短的一次。达到上限时，挖掘机**过热**；船体被打到零时，它**被摧毁**；两种情况下，挖掘机和它的脉冲星都会辐射，直到休息结束。

<!-- excavator-radiation:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

| 圆圈 | 半径 | 每秒总 HP | 满状态的飞船能撑 |
| :--- | ---: | ---: | ---: |
| 巨型挖掘机 | 1,100 | 10% | 10 秒 |
| 脉冲星 | 1,300 | 10% | 10 秒 |

- **剂量。** 每秒飞船总最大 HP（船体加护盾）的 10%，所以满状态的飞船无论什么级别都能撑 10 秒。护盾先承受，它的吸收率不起作用。
- **对象。** 圆圈内的每艘飞船，包括隐形的；外星人不受影响。它算作受到的伤害：维修无人机会停止，护盾不会回复，和黑洞一样。
- **功劳。** 被烧死的飞行员，功劳记在之前 15 秒 内最后击中他的敌人身上。
- **警告。** 过热前 1 分钟 和 15 秒 时，地图会得到通知。

<!-- excavator-radiation:end -->

- **警告。** 过热之前两次（时间见上面的列表）地图会得到通知，圆圈内的飞船会看到警告，圆圈会画在星系地图和小地图上。辐射时圆圈是红色的，辐射计显示剂量。
- **离开。** 所有标准飞船都能从面板边缘，或从仍在的最远货箱处离开，只有缓慢的 Ironclad 例外：它要在警告期间离开，否则就离不开。热量耗尽时不要站在货箱上。
- **圆圈中的战利品。** 过热前落下的货箱会留在辐射中：辐射开始时还在那里的货箱，要付出剂量的代价才能拾取。
- **服务器重启**会暂停一次运转：燃料和热量按原样恢复，休息按时钟继续，重启后的第一波在一分钟后到来。

## 争夺一次运转 {#fighting-over-a-run}

挖掘机**没有特殊的环**：适用你所在世界的常规规则，所以对手可能前来，向你开火并拿走货箱（货箱从落下的那一刻起对任何人开放）。偷窃和伏击是活动的一部分。需要预先考虑的几点：

- **加燃料的人不一定是赢家。** 任何人都可以加燃料、选择并启动；对手可以在你按下开始之前更改资源。按下之前先确认选择。
- **燃料有风险。** 挖掘机被摧毁时，燃料箱里的 Dark Matter 会丢失，没有人能拿回。最多损失的就是一满箱。
- **带上小队，**商量好谁留在挖掘机附近、谁去拾取货箱，并留意热量：拾取最后几个货箱的飞行员，正是辐射会抓住的人。
- **Void 是冲着挖掘机来的，不是冲着货箱。** 守住挖掘机的小队会拖住 Void；离开的小队则把它留给围攻。

## 世界会得到什么通知 {#what-the-world-is-told}

这些是系统行（显示在聊天的**系统**标签页和游戏日志中，不会出现在**全球**或**本地**标签页里）。前三条发给整个世界；最后一条发给挖掘机所在星区的飞行员。

- 活动 2 开始的那天：危险星区发生了变化。
- 一名飞行员**启动**挖掘机，写明星区、资源和燃料的分钟数。
- 挖掘机**过热**，或**被摧毁**。
- 燃料耗尽；挖掘机即将过热（两次）；一波 Void **正在袭来**，写明编号和来向；没有飞行员留下，所以 Void 攻击挖掘机。

控制面板的每个操作和每次警告都有各自轻柔的声音，使用音效音量。

## 延伸阅读 {#where-to-read-more}

- [危险星区](/wiki/01-General/Danger-Sectors.md)：脉冲星在哪里，还有哪些新内容。
- [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md)：Slumbering Void、Inert Mass 和 Unwakened。
- [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md)和[黑洞](/wiki/03-Mechanics/Black-Hole.md)：燃料从哪里来。
- [资源](/wiki/06-Items/Resources.md)：挖掘机产出的矿石。
- [货箱](/wiki/03-Mechanics/Cargo.md)：货箱、拾取和 Resource Magnet Booster。
- [军衔](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points)：Void 的 PvE 积分。
