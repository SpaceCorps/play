<!-- wiki-i18n source: b11d0d55c7d49e79 -->
<!-- wiki-i18n title: 锻造炉 -->
# 锻造炉 {#the-forge}

**锻造炉**是装配站页面的第二个标签页（飞行中的装配站窗口也是）。它能对你拥有的装备做两件事：花费信用点和外星人掉落物，**把一件物品提升一个等级**；或者**把一件物品的两件副本合并**成一件，保留两者中最好的部分。它取代了旧的融合室，后者需要五件相同的物品，结果还要靠一次 25% 的随机判定。

## 可锻造的物品 {#what-can-be-forged}

激光、激光增幅器、护盾核心、护盾电池、引擎、推进器、自适应核心和 Repair Drone：任何能够承载[附魔加成](/wiki/06-Items/Overview.md)的单件装备。它可以在你的物品栏中、在舰船上（它会留在原处，并立即以新的等级生效），或者嵌入在另一件物品中。无人机、舰船、弹药、资源和增益不能锻造，运输储藏库中的任何东西也不能：请先把它取出来。

## 升级 {#tier-up}

选择一件物品后，面板会显示它当前的等级、将要达到的等级、这会带来什么变化（能承载多少项加成、每项加成有多大），以及价格，并列出你拥有的每一种材料的数量：足够时显示绿色，不够时显示红色，并标出还差多少。凑齐一切后，点击**升级**会把物品恰好提升一个等级。不能跳级：要达到永恒，物品要依次经过腐化、神圣和裂变，每一级都有各自的价格。

| 阶段 | 成功率 | 信用点 | Thulium | 材料 |
| :--- | :---: | :---: | :---: | :--- |
| 标准升至腐化 | 100% | 10,000 | – | 5 个 Ship Fragment、15 个 Daraxium |
| 腐化升至神圣 | 90% | 50,000 | – | 30 个 Ship Fragment、45 个 Nyxite |
| 神圣升至裂变 | 75% | 200,000 | – | 20 块 Reinforced Hull Plate、120 个 Cataclysite、2 块 Dark Matter Plate |
| 裂变升至永恒 | 60% | 500,000 | 2,000 | 8 个 Power Core、240 个 Quorvium、2 块 Dark Matter Plate |

- **材料**取自你物品栏中未装备的堆叠：舰船上的物品和运输储藏库中的堆叠不会被使用。当缺少的材料在储藏库中时，面板会告诉你。
- **一步可能失败。** 物品保持原样，信用点会损失，一半的材料和一半的 Thulium 会返还（向下取整；两块 Dark Matter Plate 则返还一块）。面板会在你点击之前告诉你成功率和这一点。
- **成功时**，物品现有的每一项加成都会在新等级的范围内重新随机，并保留较好的数值。没有任何加成的物品一定会得到它的第一项加成；新等级开出的其他槽位各自以 **50% 的概率、分别单独判定**，在物品的其他属性上获得新加成，没填上的槽位可以在之后的升级中填上（见[各等级的加成](#buffs-by-tier)）。结果显示在面板上方；物品保持选中，所以它的下一步已经显示在屏幕上了。
- 提升等级是即时完成的。

### Dark Matter Plate {#dark-matter-plates}

最后两步除了其他材料之外，每步还需要 **2 块 Dark Matter Plate**。一块板在[装配站](/wiki/06-Items/Overview.md)中用 **5 个 Dark Matter、1 块 Velkonite Reinforced Plate 和 1 块 Orvium Reinforced Plate** 压制而成（250 Thulium，2 分钟），所以一步需要 10 个 Dark Matter、2 块 Velkonite 强化板和 2 块 Orvium 强化板。Dark Matter 来自[黑洞](/wiki/03-Mechanics/Black-Hole.md)：大约五枚 N.I.K.E. 火箭（见[火箭](/wiki/06-Items/Rockets.md)）可产出十个；途中遇到舰船的 N.I.K.E. 会改为击中那艘舰船，不产出任何 Dark Matter。这些板和其他材料一样取自你未装备的堆叠，如果不够，面板会指出缺少哪些。每条升级链的最后一阶也需要这种板，每件 3 块（[Dark Matter 与 Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)）。

### 各等级的加成 {#buffs-by-tier}

| 等级 | 最多承载的加成数 | 每项加成的幅度 |
| :--- | :---: | :---: |
| 腐化 | 1 | +2% 至 +5% |
| 神圣 | 2 | +4% 至 +8% |
| 裂变 | 3 | +6% 至 +11% |
| 永恒 | 4 | +9% 至 +15% |

在锻造炉出现之前制造的装备会保留当初随机出的加成，这些加成往往比表中的更小（当时的神圣装备可能只有 +2%）。没有任何东西会自动提高它们：升级会在新等级的范围内重新随机每一项加成并保留较好的数值，合并则会保留每项属性中较好的数值。

一件物品能承载的加成数量不会超过它拥有的属性数：护盾核心有四项，激光有三项（Quantum Laser I 和 II 有两项），引擎或自适应核心有两项，Momentum Thruster 有两项，Impulse Thruster 有一项（它的倍率 1.02 到 1.035 太小，不值得加成，锻造炉不会给 1.05 及以下的倍率附加加成，所以加成只能加在固定速度上），Crit Amp I 或 Repair Drone 有一项，更高级的暴击增幅器有两项，伤害增幅器和护盾电池有三项。当下一等级能承载的加成数不比物品所能承载的更多时，面板会这样提示：这一级就只会让加成更强。射程加成永远不会超过 +5%。Penetration Amp 只有一项属性，所以只带一条加成。

**一个等级最多能承载这么多项加成。** 每次升级一定会给物品第一项加成；新等级开出的其他槽位，只要物品有对应的属性，就各自以 **50% 的概率、分别单独判定**，没填上的槽位会在下一次升级时再试一次。所以神圣护盾核心有一半的概率有两项加成，另一半只有一项；永恒的大约三次有一次四项齐全（平均 3.1 项），有三项属性的激光三次有两次三项齐全，引擎则几乎总是两项都有。面板对下一等级会写“最多”，并显示新槽位多久填上一次。只有一项属性的物品，以及升到腐化的每一步，都不受影响，在这条规则之前制造的装备保留原有的加成。**合并**是填上升级时没填上的槽位的办法：它会保留两件副本中每项属性较好的加成，直到该等级的上限。由于有概率，一件部件只有一部分会带有下面说明的吸收率加成（永恒护盾核心 78%，永恒护盾电池 88%）：那里的数字适用于带有它的部件。

**护盾的吸收率加成**（以及护盾电池的吸收率提升）是按比例乘在该属性上的，所以它折合的[吸收率](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-)点数与它成正比：在 Heavy Shield Core 的 50% 上加 +5% 是 +2.5 点，而最佳套装（一个 Heavy Shield Core 加三个 Absorption Shield Cell IV，合计 80%）的每一件上加 +15%，则是 +12 点。永恒套装能增加 +7 到 +12 点，平均约 10 点；再加上赛季商店的 Shield Absorbance Boost（上限时 +10 点；全游戏的重置点数可买下它 100 级中的 34 级，即 +3.4 点），舰船可以达到 95%；要超过 100%，只有把该加成加到上限才行，而这项属性本来就允许超过 100%：攻击方的护盾穿透会从中扣除。神圣套装能增加 3 到 6 点。

引擎、推进器、自适应核心和 Repair Drone 靠百分比加成几乎提升不了多少（Engine II 提供 4 点速度，所以 +12% 只有半点）：想要等级时再锻造它们，不要为了属性。

**Penetration Amp 的加成**会成倍提高它的穿透：一条永恒级加成（+9% 至 +15%）会让 Penetration Amp IV 每个槽位达到 8.7 至 9.2 点，而不是 8 点。在最强的激光里（Fusion Core、Stiletto，以及每把激光上三个 Penetration Amp IV），10 + 16 + 24 已经达到激光命中的 50% 上限，所以那条加成在那里是浪费的；它适用于总和低于上限的地方（[激光与弹药](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)）。

### 材料从哪里掉落 {#where-the-materials-drop}

| 材料 | 掉落来源 |
| :--- | :--- |
| **Ship Fragment** | 每一种外星人 |
| **Daraxium** | [Seeker](/wiki/04-Aliens/Seeker.md)、[Phantasm](/wiki/04-Aliens/Phantasm.md) |
| **Nyxite** | [Phantasm](/wiki/04-Aliens/Phantasm.md)、[Bulwark](/wiki/04-Aliens/Bulwark.md) |
| **Reinforced Hull Plate** | [Bulwark](/wiki/04-Aliens/Bulwark.md)、[Goombah](/wiki/04-Aliens/Goombah.md) |
| **Cataclysite** | [Bulwark](/wiki/04-Aliens/Bulwark.md)、[Goombah](/wiki/04-Aliens/Goombah.md)、[Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Power Core** | [Goombah](/wiki/04-Aliens/Goombah.md)、[Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Quorvium** | [Goombah](/wiki/04-Aliens/Goombah.md)、[Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Dark Matter Plate** | 没有外星人掉落：装配站用 Dark Matter（来自[黑洞](/wiki/03-Mechanics/Black-Hole.md)）和 Skylab 的强化板压制而成 |

这些晶体的颜色与各个等级相对应：Daraxium 是蓝色，如同腐化；Nyxite 是黄色，如同神圣；Cataclysite 是橙色，如同裂变；Quorvium 是紫色，如同永恒。每一种来源及其几率和数量，都在[资源](/wiki/06-Items/Resources.md)页面和各外星人自己的页面上；Resource Magnet Booster 会让一个货箱的内容增加 25%。[小行星](/wiki/03-Mechanics/Asteroid-Mining.md#the-kinds)会在碎块里留下除 Dark Matter Plate 之外的所有东西。

## 合并 {#merge}

同一物品的两件副本（两个 Light Shield Core、两把 Quantum Laser II）会合成一件。切换到**合并**，点击你想保留的物品（**基础**），再点击第二件副本（**素材**）。确认之前，面板会先显示结果。

- **基础会被保留。** 它留在原位：它可以在舰船上，也可以嵌入在另一件物品中，而嵌入其中的模块会保留。**素材会被消耗。** 它必须是未使用状态（不在舰船上，也没有嵌入其他物品），嵌入其中的模块会回到你的物品栏。
- **结果取两者中较高的等级**，每项属性取**两者中较好的数值**。
- **加成数量永远不会超过其等级允许的上限。** 如果两件物品合计的加成多于结果等级所能承载的数量，最好的会被保留，其余的会被舍弃；表格会标出它们（加删除线，标注“超出上限”）。想承载更多加成，请先提升物品的等级。合并不会随机任何东西：预览显示的就是你得到的。
- **合并按所合成的等级收取信用点**：腐化 5,000，神圣 25,000，裂变 100,000，永恒 250,000。不需要材料。
- 不会带来任何变化的合并（结果不比基础更好）会被拒绝。
- 合并之后，结果保持选中，素材槽位为空：放入下一件素材，或者切换回升级。
- **标记**：合并后的物品只有在基础物品和捐献物品都可交易时，才是**可交易**的（可以在[拍卖行](/wiki/03-Mechanics/Auction.md#marketable-items)出售）。预览会显示这一点。

合并不会把物品成倍放大，但能填上升级时没填上的槽位：合并两个神圣护盾核心，加成平均比一个多出大约 3.5 点。它的用处在于挑选：得到一个属性正合你意的神圣核心，或者把等级转移到你舰船上的那件物品上，而不必把它取下来。

## 装配站中的模块升级 {#module-upgrades-in-the-assembly}

最顶级的三种激光、激光增幅器、II 至 IV 阶的护盾电池和推进器，以及 Heavy Shield Core 和 Engine III，都不在商店出售，而且只有在 Skylab 里研究出对应科技后，装配站才会制造它们（[研究](/wiki/03-Mechanics/Research.md)）。你要在装配站的**制造**标签页中，通过升级低一级的部件来制作它们：把 Damage Amp III 升级为 **Damage Amp IV**，把 Crit Amp III 升级为 **Crit Amp IV**，把 Capacity Shield Cell I 升级为 **Capacity Shield Cell II**（再到 III 和 IV；Absorption Shield Cell、Impulse Thruster 和 Momentum Thruster 也同样逐阶升级），把 Basic Shield Core 升级为 **Heavy Shield Core**，把 Engine II 升级为 **Engine III**，把 Quantum Laser II 升级为 **Quantum Laser III**，把 Quantum Laser III 升级为 **Starfire-III**，把 Starfire-III 升级为 **Helios Beam**。锻造炉与此的关系就在于等级。每个增幅器系列的第一阶（Damage Amp I、Crit Amp I 和 Penetration Amp I）在商店出售；每个系列的 II 至 IV 阶用同样的方式制作。

- **等级保留。** 升级会消耗该部件的一件副本，新物品沿用这件副本的等级：神圣·Damage Amp III 制成神圣·Damage Amp IV，标准等级的则制成标准·Damage Amp IV。你在锻造炉上花的钱不会白费。升级本身不会增加任何等级，所以标准等级的部件制成的永远是标准等级的成品。
- **加成会重新随机。** 新物品会获得适合其等级的全新加成：数量与你消耗的部件原有的相同（有两项加成的神圣·Damage Amp III 制成有两项的神圣·Damage Amp IV，只有一项的则制成只有一项的；高于标准等级时至少一项），但以该等级能承载的数量和新物品拥有的属性数为上限，每一项都落在上表中该等级的范围内，且位于 Damage Amp IV 拥有的属性上。除此之外，旧部件上的任何东西都不会被复制，所以新加成可能比原来的更好，也可能更差；平均而言是一样的。保留数量是为了不让升级填上锻造炉没填上的槽位，而且它从不拿走加成：在这条规则之前制造、槽位全满的部件会保留全部。加成在你把任务加入队列的那一刻就已随机确定，你领取到的就是当时随机出的结果：等待领取不会改变任何东西。原因在于升级是制造一件新物品，而锻造炉的骰子是掷在你手中那件物品上的。真正花钱的是等级：一件永恒部件相当于超过一百万信用点的锻造步骤，而一项加成只是某一项属性的几个百分点。
- **强化板。** 除了 Thulium 和外星人的掉落物之外，每次模块升级都需要板。最后一阶需要 **3 块 Dark Matter Plate**：IV 阶的增幅器、护盾电池或推进器，以及 Heavy Shield Core、Engine III 和 Helios Beam。更前面的几步需要 **Velkonite Reinforced Plate**：II 或 III 阶的增幅器需要 1 块或 2 块，II 或 III 阶的护盾电池或推进器需要 2 块或 4 块，Quantum Laser III 需要 2 块，Starfire-III 需要 8 块（Helios Beam 还需要 18 块 Orvium Reinforced Plate）。外星人不会掉落其中任何一种。你的 [Skylab](/wiki/03-Mechanics/Skylab.md) 锻造厂会用矿石制造 Velkonite 和 Orvium 强化板，锻造厂 1 级时每块 Velkonite 板需要 40 个矿石。1 级的 Velkonite 采集器每小时开采 10 个矿石，所以一个 III 阶增幅器的强化板需要 8 小时的开采，一个 III 阶护盾电池或推进器的则需要 16 小时（5 级采集器分别是 4 小时和 9 小时）。装配站在你研究了这块板的配方之后，用 5 个 Dark Matter、1 块 Velkonite Reinforced Plate、1 块 Orvium Reinforced Plate 和 250 Thulium 压制一块 [Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)。各种材料的来源见[资源](/wiki/06-Items/Resources.md)页面。锻造炉自己的步骤需要掉落物和信用点，其最高几步还需要 Dark Matter Plate（神圣升至裂变：20 块 Reinforced Hull Plate 和 2 块 Dark Matter Plate；裂变升至永恒：2 块 Dark Matter Plate），与模块升级最后一阶所用的是同一种板。
- **使用哪一件副本。** 由你选择。当你持有的副本各不相同（等级或加成不同）时，配方卡片会把它们显示成一排图块：点击要使用的那一件，图块下方的一行会显示它将变成什么（“神圣·Damage Amp III”，接着是“成品：神圣·Damage Amp IV”）。如果你没有选择，最普通的那件会被使用：先用等级最低的，同一等级的副本中先用最旧的，无论它们的加成如何。只要还有更普通的未使用副本，神圣或更高等级的副本就绝不会被使用。使用高于标准等级的副本时会先询问，并写明该物品的名称。
- **哪些副本可以使用。** 未使用的：舰船上的（技能槽位中的也算）、嵌入在另一件物品中的、自身带有电池或推进器的，或在[运输储藏库](/wiki/03-Mechanics/Cargo.md)中的副本都不能使用，装配站会告诉你这一点。请先把它取下或从储藏库中取出。同时开始的两次升级不能使用同一件副本。

- **Quantum Laser III 同样是一次升级。** 它由一把 **Quantum Laser II**（商店里的激光）制成（另需 1,500 Thulium、10 个 Ship Fragment 和 2 块 Velkonite Reinforced Plate：见[激光与弹药](/wiki/06-Items/Lasers.md)），以上所有规则都适用：神圣·Quantum Laser II 制成神圣·Quantum Laser III，带有新加成，由你选择副本，使用高于标准等级的副本前配方卡片会先询问，Quantum Laser II 必须是未使用状态：请先在机库中把它取下，在你取下之前，“组装”按钮会显示“请先取下 Quantum Laser II”。等级随后继续向上传递：神圣·Quantum Laser III 制成神圣·Starfire-III。

- **Starfire-III 同样是一次升级。** 它由一把 **Quantum Laser III** 制成（另需 1,500 Thulium、100,000 信用点、掉落物和 8 块 Velkonite Reinforced Plate：见[激光与弹药](/wiki/06-Items/Lasers.md)），以上所有规则都适用：神圣·Quantum Laser III 制成神圣·Starfire-III，带有新加成，由你选择副本，使用高于标准等级的副本前配方卡片会先询问，Quantum Laser III 必须是未使用状态：请先在机库中把它取下，在你取下之前，“组装”按钮会显示“请先取下 Quantum Laser III”。等级随后继续向上传递：神圣·Starfire-III 制成神圣·Helios Beam。

- **Helios Beam 同样是一次升级。** 它由一把 **Starfire-III** 制成（另需 2,000 Thulium、掉落物、18 块 Orvium Reinforced Plate 和 3 块 Dark Matter Plate：见[激光与弹药](/wiki/06-Items/Lasers.md)），以上所有规则都适用：神圣·Starfire-III 制成神圣·Helios Beam，带有新加成（数量与 Starfire-III 原有的相同，三项属性中最多两项），由你选择副本，使用高于标准等级的副本前配方卡片会先询问，Starfire-III 必须是未使用状态。激光通常装在舰船上并带着增幅器，所以往往不是未使用状态：请先在机库中把它取下（其中的增幅器会回到你的物品栏），在你取下之前，“组装”按钮会显示“请先取下 Starfire-III”。

配方、费用以及这条规则背后的数字，见[物品总览](/wiki/06-Items/Overview.md#upgrading-modules)；Quantum Laser III、Starfire-III 和 Helios Beam 的部分见[激光与弹药](/wiki/06-Items/Lasers.md)页面。

## 旧服务器 {#old-servers}

尚未更新到锻造炉的游戏服务器会在标签页的位置显示“此服务器上还没有锻造炉”；制造功能照常可用。锻造炉出现之前的游戏客户端在已更新的服务器上会显示旧的融合标签页，并被提示更新。
