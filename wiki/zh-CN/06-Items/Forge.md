<!-- wiki-i18n source: 1bd2092b2dd812be -->
<!-- wiki-i18n title: 锻造炉 -->
# 锻造炉 {#the-forge}

<!-- wiki-search: forge; 锻造炉; 锻造; 升级; 等级; sockets; 调谐; 重排; shard; shards; 碎片; echo; echo shard; lattice; lattice shard; heartshard; 完整度; 裂痕; 修复; 合并; 融合; tainted; godly; rupturing; eternal; 腐化; 神圣; 裂变; 永恒; awakened; resonant; radiant; ascendant; 觉醒; 共鸣; 辉耀; 升华; tinkerer's badge -->

**锻造炉**是装配站页面的第二个标签页（飞行中的装配站窗口也是）。它能对你拥有的装备做三件事：花费信用点和外星人掉落物，**把一件物品提升一个等级**；用 Shard **调谐它的插槽**（加成就从这里来）；或者**把一件物品的两件副本合并**成一件，保留两者中最好的部分。升级从不失败，锻造炉只有在你从候选里选定之后，才会往物品里放入新的加成。（0.5.7 之前，等级叫腐化、神圣、裂变和永恒，一步也可能失败；现在叫觉醒、共鸣、辉耀和升华。）它取代了旧的融合室，后者需要五件相同的物品，结果还要靠一次 25% 的随机判定。

## 可锻造的物品 {#what-can-be-forged}

激光、激光增幅器、护盾核心、护盾电池、引擎、推进器、自适应核心、Repair Drone 和[船体装甲](/wiki/06-Items/Hull-Plating.md)：任何能够承载[附魔加成](/wiki/06-Items/Overview.md)的单件装备。它可以在你的物品栏中、在舰船上（它会留在原处，并立即以新的等级生效），或者嵌入在另一件物品中。无人机、舰船、弹药、资源和增益不能锻造，运输储藏库中的、或装在你的 Skylab 引擎模块或防御模块里的任何东西也不能：请先把它取出来。

装备列表在其他筛选旁有一个**全部 / 已装备 / 物品栏**开关。**已装备**显示在飞船上或嵌在别的物品里的物品，**物品栏**显示散放的物品，标题下的一行会告诉你开关隐藏了多少件。在为合并选择素材时，“已装备”会暂停，因为素材必须是散放的。

类型筛选旁的**飞船**下拉菜单只显示你某一艘飞船上的部件（嵌在别的物品里的部件算在其宿主所在的飞船上）。在“物品栏”和为合并选择素材时，它会暂停。部件的悬停卡片、面板标题和合并的基础物品都会说明部件在哪里：*在 Kitefin 上，配置 1*（船体装甲：两个配置），以及它嵌在什么里。**Ctrl+F**（Mac 上是 Cmd+F）会把光标放进装配站标题栏里的搜索框；它会缩小当前标签页的列表（配方按产出和所需材料，装备按名称、类型和等级），按 Esc 清除。在*已唤醒的插槽*下面，面板会说明部件的某项属性是否太低、无法承载加成，这就是 Impulse Thruster 只有一项加成而 Momentum Thruster 有两项的原因。

## 升级 {#tier-up}

选择一件物品后，面板会显示它当前的等级、将要达到的等级、这会带来什么变化（能承载多少项加成、每项加成有多大），以及价格，并列出你拥有的每一种材料的数量：足够时显示绿色，不够时显示红色，并标出还差多少。凑齐一切后，点击**升级**会把物品恰好提升一个等级。不能跳级：要达到升华，物品要依次经过觉醒、共鸣和辉耀，每一级都有各自的价格。

| 阶段 | 信用点 | Thulium | 材料 |
| :--- | :---: | :---: | :--- |
| 标准升至觉醒 | 10,000 | – | 5 个 Ship Fragment、15 个 Daraxium |
| 觉醒升至共鸣 | 56,000 | – | 32 个 Ship Fragment、48 个 Nyxite |
| 共鸣升至辉耀 | 267,000 | – | 23 块 Reinforced Hull Plate、140 个 Cataclysite、2 块 Dark Matter Plate |
| 辉耀升至升华 | 833,000 | 2,667 | 11 个 Power Core、320 个 Quorvium、2 块 Dark Matter Plate |

- **材料**取自你物品栏中未装备的堆叠：舰船上的物品和运输储藏库中的堆叠不会被使用。当缺少的材料在储藏库中时，面板会告诉你。
- **每一步必定成功。** 价格相当于锻造炉还没有插槽时一步的平均花费，并会唤醒物品上的一个插槽（见[各等级的加成](#buffs-by-tier)）。
- **Commerce 专长**在 100 级时最多可把一步所需的信用点和 Thulium、以及一次合并所需的信用点降低 15%（[飞行员专长](/wiki/03-Mechanics/Pilot-Skills.md)）。表格里是 1 级时的价格，面板里是你实际支付的价格；材料不变。
- **物品已有的每项加成**会在新等级的范围内重新随机，并保留较好的数值。结果显示在面板上方；物品保持选中，所以它的下一步已经在屏幕上。
- 提升等级是即时完成的。
- **插槽就在这一步的下方。** 升级和[插槽](#sockets)是同一个视图，**强化**，升级在前：一步所唤醒的插槽就在按钮正下方的列表里，它的“调谐”按钮也在那里，用它不必切换到别处。
- **Tinkerer's Badge**（一种[特殊物品](/wiki/06-Items/Special-Items.md#tinkerers-badge)）不用信用点、不花 Thulium、也不要材料，就把一件装备提升一个等级，从标准等级起就能用。这是一步不花钱的升级：和付费的一步一样会唤醒一个插槽，并重新随机装备已有的加成。

### Dark Matter Plate {#dark-matter-plates}

最后两步除了其他材料之外，每步还需要 **2 块 Dark Matter Plate**。一块板在[装配站](/wiki/06-Items/Overview.md)中用 **5 个 Dark Matter、1 块 Velkonite Reinforced Plate 和 1 块 Orvium Reinforced Plate** 压制而成（250 Thulium，2 分钟），所以一步需要 10 个 Dark Matter、2 块 Velkonite 强化板和 2 块 Orvium 强化板。Dark Matter 来自[黑洞](/wiki/03-Mechanics/Black-Hole.md)：大约五枚 N.I.K.E. 火箭（见[火箭](/wiki/06-Items/Rockets.md)）可产出十个；途中遇到舰船的 N.I.K.E. 会改为击中那艘舰船，不产出任何 Dark Matter。这些板和其他材料一样取自你未装备的堆叠，如果不够，面板会指出缺少哪些。每条升级链的最后一阶也需要这种板，每件 4 块（[Dark Matter 与 Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)）。

### 各等级的加成 {#buffs-by-tier}

| 等级 | 最多承载的加成数 | 每项加成的幅度 | 该步的晶体 |
| :--- | :---: | :---: | :--- |
| 觉醒 | 1 | +2% 至 +5% | Daraxium |
| 共鸣 | 2 | +4% 至 +8% | Nyxite |
| 辉耀 | 3 | +6% 至 +11% | Cataclysite |
| 升华 | 4 | +9% 至 +15% | Quorvium |

在锻造炉出现之前制造的装备会保留当初随机出的加成，这些加成往往比表中的更小（当时的共鸣装备可能只有 +2%）。没有任何东西会自动提高它们：升级会在新等级的范围内重新随机每一项加成并保留较好的数值，合并则会保留每项属性中较好的数值。

一件物品能承载的加成数量不会超过它拥有的属性数：护盾核心有四项，激光有三项，引擎或自适应核心有两项，Momentum Thruster 有两项，Impulse Thruster 有一项（它的倍率 1.017 到 1.03 太小，不值得加成，锻造炉不会给 1.05 及以下的倍率附加加成，所以加成只能加在固定速度上），Crit Amp I、Repair Drone 或船体装甲（它的船体）有一项，更高级的暴击增幅器有两项，伤害增幅器和护盾电池有三项。当下一等级能承载的加成数不比物品所能承载的更多时，面板会这样提示：这一级就只会让加成更强。射程加成永远不会超过 +5%。Penetration Amp 只有一项属性，所以只带一条加成。

**一个等级最多容纳这么多项加成。** 每升一级，物品上会唤醒一个插槽，就是与该步晶体对应的那一个：Daraxium 唤醒第一个，Nyxite 第二个，Cataclysite 第三个，Quorvium 第四个。物品的插槽数以该等级能容纳的、且物品有对应属性的为限：共鸣等级的护盾核心有两个，升华等级的则四个全有，而只有两项属性的引擎没有可唤醒的第三个插槽。用 Echo Shard 调谐插槽并从候选里选定之后，加成才会放进去。**合并**会保留两件副本中每项属性最好的加成，以该等级的上限为准。

**护盾的吸收率加成**（以及护盾电池的吸收率提升）是按比例乘在该属性上的，所以它折合的[吸收率](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-)点数与它成正比：在 Heavy Shield Core 的 55% 上加 +5% 是 +2.75 点，而最佳套装（一个 Heavy Shield Core 加三个 Absorption Shield Cell IV，合计 91%）的每一件上加 +15%，则是 +13.65 点。升华套装能增加 +8.2 到 +13.65 点，平均约 11 点；再加上赛季商店的 Shield Absorbance Boost（上限时 +10 点；一次重置的重置点数可买下它 100 级中的 44 级，即 +4.4 点），舰船可以达到约 106%；再加上飞行员研究 Field Theory（最多 +10 点），则可远超 100%，而这项属性本来就允许超过 100%：攻击方的护盾穿透会从中扣除。共鸣套装能增加 3.6 到 7.3 点。这些是没有任何裂痕的加成的数值（[完整度与裂痕](#integrity-and-fractures)）。

引擎、推进器、自适应核心和 Repair Drone 靠百分比加成几乎提升不了多少（Engine II 提供 10 点速度，所以 +12% 是 1.2 点）：想要等级时再锻造它们，不要为了属性。

**Penetration Amp 的加成**会成倍提高它的穿透：一条升华级加成（+9% 至 +15%）会让 Penetration Amp IV 每个槽位达到 21.8 至 23 点，而不是 20 点。穿透没有上限，所以每一点都有用：在最强的激光里（Fusion Core、Gemini，以及每把激光上三个 Penetration Amp IV），10 + 15 + 60 合计 85%，三条升华级加成最多可以把它提高到 94%（[激光与弹药](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)）。

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

这些晶体的颜色与各个等级相对应：Daraxium 是蓝色，如同觉醒；Nyxite 是黄色，如同共鸣；Cataclysite 是橙色，如同辉耀；Quorvium 是紫色，如同升华。每一种来源及其几率和数量，都在[资源](/wiki/06-Items/Resources.md)页面和各外星人自己的页面上；Resource Magnet Booster 会让一个货箱的内容增加 25%。[小行星](/wiki/03-Mechanics/Asteroid-Mining.md#the-kinds)会在碎块里留下除 Dark Matter Plate 之外的所有东西。

## 插槽 {#sockets}

锻造炉**强化**视图中升级下方的**插槽**部分，是加成进入物品的地方。选中一件装备，这一部分会列出它的插槽、完整度和你持有的 Shard。插槽在升级唤醒它之前是**锁定**的（它那一行会写明在哪个等级、用哪种晶体的那一步），唤醒后是**空**的，装上加成后就是**已调谐**。升级部分会统计数量：*已唤醒的插槽 1 → 2 / 4*。

- 用 **Echo Shard** **调谐**空插槽：一件装备的第一个插槽要 10 个，之后依次是 20、40、80 个，所以每调谐一个插槽，价格就上涨（后面每个空插槽上淡色的价格会告诉你它要花多少）。按下“调谐”时 Shard 就被消耗，锻造炉随后给出一份**候选**：从仍然空闲的属性中随机抽出的两项，每项附带它会给出的加成。**选择**其中一项：你得到的就是候选里显示的。如果只剩一项属性空闲，两行就都是这项属性的抽取结果，可能抽成相同的数值。
- 调谐或重排时可以加上一枚 **Heartshard**：先打开*在下一次调谐或重排时使用 Heartshard*，候选就会改为列出这件装备所有空闲的属性，每项都在其范围的上半段掷出，所以属性由你来选。
- 想在已调谐的插槽里换成别的属性时，用 **Lattice Shard** **重排**。一件装备的第一次重排需要 2 个 Lattice Shard，之后是 3、4、4、5、7……（2 乘以 1.25，之前每重排一次乘一次，向上取整），还要花掉装备的一部分完整度：6 点，制造等级高时更少（[完整度与裂痕](#integrity-and-fractures)）。无论你选哪一项，Shard 和完整度都会被消耗，所以会先弹出确认面板。候选的生成方式和调谐一样，来自空闲的属性和插槽现有的属性，每项重新抽取，并在整个宽度上有一个**保留当前**按钮，用于它们都不如插槽现有加成的情况。
- **你选定之前，装备会一直等着。**未处理的候选会锁住这件装备：它上面其他操作都无法进行，面板会这样告知。关闭游戏不会损失任何东西，你回来时候选还在。无人回应的候选会在 7 天后、锻造炉下次碰到这件装备时（在那里选中它就够了）替你决定：调谐取候选的第一项，重排保留当前加成。拍卖行和装配站的模块升级从不决定候选，在锻造炉决定之前它们会拒绝这件装备，所以请先在锻造炉里打开这件装备。
- **修理**用下一次重排所需 Lattice Shard 的两倍，恢复 12 点完整度。它不会减少重排次数，所以下一次重排的价格不变。
- **仪表**显示完整度，并在每一道新裂痕出现的位置画有刻度（第一道裂痕在失去第一点时出现），鼠标悬停时会说明每道裂痕削掉了哪项属性。加成因裂痕而损失点数的已调谐插槽会同时显示两个数字（+9% 的加成带两道裂痕：*裂痕 −4%（掷出 +9%）*），降到零的插槽则显示*被裂痕完全抵消：没有剩余加成*。插槽仍是已调谐状态，加成为 +0%。
- **只有未装备的堆叠会被消耗。** 运输储藏库中的 Shard 不会，缺少的 Shard 在那里时面板会告诉你。Shard 不能购买、出售，也不能挂到拍卖行，运气和 Resource Magnet Booster 都不会增加它们。

### Shard 从哪里来 {#where-the-shards-come-from}

调谐一件装备的全部四个插槽需要 150 个 Echo Shard（10 + 20 + 40 + 80），它的前 16 次重排需要 283 个 Lattice Shard。它们来自[单人星门](/wiki/03-Mechanics/Solo-Gates.md)和[地下城](/wiki/03-Mechanics/Dungeons.md)，是在这两处其他奖励之外额外给的，外星人也会掉落少量 Echo Shard：

| 来源 | Echo Shard | Lattice Shard |
| :--- | :---: | :---: |
| 单人星门：Alpha Rift | 4 | 6 |
| 单人星门：Beta Breach | 9 | 13 |
| 单人星门：Gamma Foundry | 18 | 27 |
| 单人星门：Delta Siege | 29 | 44 |
| 单人星门：Omega Vault | 34 | 54 |
| 战队地下城：第 1 阶段 | 12 | 5 |
| 战队地下城：第 2 阶段 | 8 | 6 |
| 战队地下城：第 3 阶段 | 8 | 7 |

- **单人星门**每次通关都发放它们的 Shard，**战队地下城**则在每次获得奖励的阶段通关时发放。
- **Heartshard** 在本赛季每个星门和每个地下城阶段首次通关时获得（1 个），之后每次通关有 5% 的几率再获得 1 个。稀有 NPC 也会掉落：每击杀一次，Davidski 10%，Dormant Force 和 Tesseract 5%。其余内容见[资源](/wiki/06-Items/Resources.md#heartshard)页面。
- **外星人**只掉落 Echo Shard，而且很少：每击杀一次，从 Seeker 的 0.8% 到 Crystalys 的 40%（[Echo Shard](/wiki/06-Items/Resources.md#echo-shard)）。

## 合并 {#merge}

同一物品的两件副本（两个 Light Shield Core、两把 Quantum Laser II）会合成一件。切换到**合并**，点击你想保留的物品（**基础**），再点击第二件副本（**素材**）。确认之前，面板会先显示结果。

- **基础会被保留。** 它留在原位：它可以在舰船上，也可以嵌入在另一件物品中，而嵌入其中的模块会保留。**素材会被消耗。** 它必须是未使用状态（不在舰船上，也没有嵌入其他物品），嵌入其中的模块会回到你的物品栏。
- **结果取两者中较高的等级**，每项属性取**两者中较好的数值**。
- **加成数量永远不会超过其等级允许的上限。** 如果两件物品合计的加成多于结果等级所能承载的数量，最好的会被保留，其余的会被舍弃；表格会标出它们（加删除线，标注“超出上限”）。想承载更多加成，请先提升物品的等级。合并不会随机任何东西：预览显示的就是你得到的。
- **合并按所合成的等级收取信用点**：觉醒 5,000，共鸣 25,000，辉耀 100,000，升华 250,000。不需要材料。Commerce 专长也会像对一步那样降低这笔信用点。
- 不会带来任何变化的合并（结果不比基础更好）会被拒绝。仅仅完整度更高并不算：合并不是修理。
- **完整度。**结果的完整度是两件装备完整度的平均值（向下取整）减去 6，最低为 0，重排次数取两者中较高的一个：两件完好的装备合并后得到完整度 94 的装备。结果保留作为基础的那件装备的裂痕顺序：最先受损的是同一项属性。参见[完整度与裂痕](#integrity-and-fractures)。
- 合并之后，结果保持选中，素材槽位为空：放入下一件素材，或者切换回强化。
- **标记**：合并后的物品只有在基础物品和捐献物品都可交易时，才是**可交易**的（可以在[拍卖行](/wiki/03-Mechanics/Auction.md#marketable-items)出售）。预览会显示这一点。

合并不会让物品变多。它的用处在于挑选：得到带有你想要属性的共鸣核心，或者把某个等级转移到你飞船上的物品上而不必把它拆下来。

## 完整度与裂痕 {#integrity-and-fractures}

每件装备都有 0 到 100 的**完整度**。没人动过的装备是 100。你在装配站制造出来或作为战利品得到的装备（来自外星人、虫群或 Warden 的箱子，或者作为战队地下城的装备卡），会从 70 到 100 之间的某个值开始；你购买或获赠的，以及 0.5.7 之前你拥有的一切，都是完好的。重排一个插槽（需要一个 Lattice Shard）要消耗完整度：6 点，制造达到 29 级后是 5 点，84 级后是 4 点（[飞行员专长](/wiki/03-Mechanics/Pilot-Skills.md)）；剩余完整度不超过这个数的装备无法再重排。一次修复会返还 12 点（见[插槽](#sockets)）。

完整度每低于 100 达 12 点就多一道**裂痕**，不满 12 点的部分也算一道：完整度 99 到 88 有 1 道，87 到 76 有 2 道，依此类推，最多 8 道。一道裂痕让某一项属性的加成减少 2 个百分点：一个 +9% 的加成带两道裂痕就是 +5%。裂痕轮流落在物品的各项属性上，顺序对每件装备是固定的：第一道裂痕落在一项属性上，第二道落在下一项，每项都有了一道之后，新的一轮再从头开始。没有加成的属性也会被击中：它的裂痕会等着，在你往里调谐加成的那一刻开始计算。加成不会低于 +0%，所以裂痕不会让装备比原始物品更差。只有一项可加成属性的物品（Hull Plating、Repair Drone、Crit Amp I、Penetration Amp、Impulse Thruster）会把所有裂痕都落在这一项上：8 道裂痕，也就是 16 点，连 +15% 的加成也不会剩下。

对一件受损的装备，物品栏、机库、拍卖行和锻造炉显示的是它**实际飞行时使用**的数值：裂痕已经扣除，旁边列出各项裂痕。升级等级和模块升级都不改变完整度；[合并](#merge)会把它设为两件装备的平均值减去 6。

## 赛季重置 {#the-season-wipe}

[重置](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-)保留下来的装备（装在保留装备的飞船上的、装在你的 Skylab 里的，或放在运输储藏库里的），会保留锻造炉对它所做的一切：等级、已调谐的插槽及其加成、完整度、重排次数，以及仍然开着的候选。重置不会修复任何东西，也不会损坏任何东西。Shard 是和矿石一样的资源：重置会销毁未装备的那些，而你放进运输储藏库的会被保留（每个 1 kg）。

## 装配站中的模块升级 {#module-upgrades-in-the-assembly}

最顶级的三种激光、激光增幅器、II 至 IV 阶的护盾电池和推进器，II 至 III 阶的引擎和自适应核心，以及 Heavy Shield Core，都不在商店出售，而且只有在 Skylab 里研究出对应科技后，装配站才会制造它们（[研究](/wiki/03-Mechanics/Research.md)）。你要在装配站的**制造**标签页中，通过升级低一级的部件来制作它们：把 Damage Amp III 升级为 **Damage Amp IV**，把 Crit Amp III 升级为 **Crit Amp IV**，把 Capacity Shield Cell I 升级为 **Capacity Shield Cell II**（再到 III 和 IV；Absorption Shield Cell、Impulse Thruster 和 Momentum Thruster 也同样逐阶升级），把 Basic Shield Core 升级为 **Heavy Shield Core**，把 Engine I 升级为 **Engine II**（再到 **Engine III**），把 Adaptive Core I 升级为 **Adaptive Core II**（再到 **Adaptive Core III**），把 Quantum Laser II 升级为 **Quantum Laser III**，把 Quantum Laser III 升级为 **Starfire-III**，把 Starfire-III 升级为 **Helios Beam**。锻造炉与此的关系就在于等级。每个增幅器系列的第一阶（Damage Amp I、Crit Amp I 和 Penetration Amp I）在商店出售；每个系列的 II 至 IV 阶用同样的方式制作。

- **等级保留。** 升级会消耗该部件的一件副本，新物品沿用这件副本的等级：共鸣·Damage Amp III 制成共鸣·Damage Amp IV，标准等级的则制成标准·Damage Amp IV。你在锻造炉上花的钱不会白费。升级本身不会增加任何等级，所以标准等级的部件制成的永远是标准等级的成品。
- **加成保持不变。** 新物品沿用你消耗的部件的加成：属性相同、数值相同，不会重新随机（有两项加成的共鸣·Damage Amp III 制成带有这两项加成的共鸣·Damage Amp IV，只有一项的则制成带有这一项的）。部件的每一项属性在升级后的物品上也有，所以每一项加成都有位置，升级既不会为空插槽调谐，也不会拿走任何加成。加成在你把任务加入队列的那一刻就已确定，你领取到的就是当时确定的结果：等待领取不会改变任何东西；如果取消任务，退回的就是完全相同的部件，等级和加成都和原来一样。在这条规则之前加入队列的任务保留它当时随机出的加成。真正花钱的是锻造炉为部件做的事：一件升华部件相当于超过一百万信用点的锻造步骤，而升级会保留它的全部。**装备的完整度和重排次数也会一并保留**：升级不是修复，也不会抹掉任何一道裂痕。
- **强化板。** 除了 Thulium 和外星人的掉落物之外，每次模块升级都需要板。最后一阶需要 **4 块 Dark Matter Plate** 和至少 1 个 Ancient Control Unit：IV 阶的增幅器、护盾电池或推进器，以及 Heavy Shield Core、Engine III、Adaptive Core III 和 Helios Beam。更前面的几步需要 **Velkonite Reinforced Plate**：II 或 III 阶的增幅器需要 2 块，II 或 III 阶的护盾电池或推进器需要 4 块，Quantum Laser III 需要 3 块，Engine II 或 Adaptive Core II 需要 4 块，Starfire-III 需要 8 块（Helios Beam 还需要 18 块 Orvium Reinforced Plate）。外星人不会掉落其中任何一种。你的 [Skylab](/wiki/03-Mechanics/Skylab.md) 锻造厂会用矿石制造 Velkonite 和 Orvium 强化板，锻造厂 1 级时每块 Velkonite 板需要 40 个矿石。1 级的 Velkonite 采集器每小时开采 10 个矿石，所以一个 III 阶增幅器的强化板需要 8 小时的开采，一个 III 阶护盾电池或推进器的则需要 16 小时（5 级采集器分别是 4 小时和 9 小时）。装配站在你研究了这块板的配方之后，用 5 个 Dark Matter、1 块 Velkonite Reinforced Plate、1 块 Orvium Reinforced Plate 和 250 Thulium 压制一块 [Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)。各种材料的来源见[资源](/wiki/06-Items/Resources.md)页面。锻造炉自己的步骤需要掉落物和信用点，其最高几步还需要 Dark Matter Plate（共鸣升至辉耀：23 块 Reinforced Hull Plate 和 2 块 Dark Matter Plate；辉耀升至升华：2 块 Dark Matter Plate），与模块升级最后一阶所用的是同一种板。
- **使用哪一件副本。** 由你选择。当你持有的副本各不相同（等级或加成不同）时，配方卡片会把它们显示成一排图块：点击要使用的那一件，图块下方的一行会显示它将变成什么（“共鸣·Damage Amp III”，接着是“成品：共鸣·Damage Amp IV”）。如果你没有选择，最普通的那件会被使用：先用等级最低的，同一等级的副本中先用最旧的，无论它们的加成如何。只要还有更普通的未使用副本，共鸣或更高等级的副本就绝不会被使用。使用高于标准等级的副本时会先询问，并写明该物品的名称。
- **哪些副本可以使用。** 未使用的：舰船上的（技能槽位中的也算）、嵌入在另一件物品中的、装在你的 Skylab 引擎模块或防御模块里的、自身带有电池或推进器的，或在[运输储藏库](/wiki/03-Mechanics/Cargo.md)中的副本都不能使用，装配站会告诉你这一点。请先把它取下或从储藏库中取出。同时开始的两次升级不能使用同一件副本。

- **Quantum Laser III 同样是一次升级。** 它由一把 **Quantum Laser II**（商店里的激光）制成（另需 1,500 Thulium、10 个 Ship Fragment 和 3 块 Velkonite Reinforced Plate：见[激光与弹药](/wiki/06-Items/Lasers.md)），以上所有规则都适用：共鸣·Quantum Laser II 制成共鸣·Quantum Laser III，带有相同的加成，由你选择副本，使用高于标准等级的副本前配方卡片会先询问，Quantum Laser II 必须是未使用状态：请先在机库中把它取下，在你取下之前，“组装”按钮会显示“请先取下 Quantum Laser II”。等级随后继续向上传递：共鸣·Quantum Laser III 制成共鸣·Starfire-III。

- **Starfire-III 同样是一次升级。** 它由一把 **Quantum Laser III** 制成（另需 1,500 Thulium、100,000 信用点、掉落物和 8 块 Velkonite Reinforced Plate：见[激光与弹药](/wiki/06-Items/Lasers.md)），以上所有规则都适用：共鸣·Quantum Laser III 制成共鸣·Starfire-III，带有相同的加成，由你选择副本，使用高于标准等级的副本前配方卡片会先询问，Quantum Laser III 必须是未使用状态：请先在机库中把它取下，在你取下之前，“组装”按钮会显示“请先取下 Quantum Laser III”。等级随后继续向上传递：共鸣·Starfire-III 制成共鸣·Helios Beam。

- **Helios Beam 同样是一次升级。** 它由一把 **Starfire-III** 制成（另需 2,000 Thulium、掉落物、18 块 Orvium Reinforced Plate、4 块 Dark Matter Plate 和 1 个 Ancient Control Unit：见[激光与弹药](/wiki/06-Items/Lasers.md)），以上所有规则都适用：共鸣·Starfire-III 制成共鸣·Helios Beam，带有 Starfire-III 的加成，由你选择副本，使用高于标准等级的副本前配方卡片会先询问，Starfire-III 必须是未使用状态。激光通常装在舰船上并带着增幅器，所以往往不是未使用状态：请先在机库中把它取下（其中的增幅器会回到你的物品栏），在你取下之前，“组装”按钮会显示“请先取下 Starfire-III”。

配方、费用以及这条规则背后的数字，见[物品总览](/wiki/06-Items/Overview.md#upgrading-modules)；Quantum Laser III、Starfire-III 和 Helios Beam 的部分见[激光与弹药](/wiki/06-Items/Lasers.md)页面。

## 旧服务器 {#old-servers}

尚未更新到锻造炉的游戏服务器会在标签页的位置显示“此服务器上还没有锻造炉”；制造功能照常可用。锻造炉出现之前的游戏客户端在已更新的服务器上会显示旧的融合标签页，并被提示更新。0.5.7 之前的服务器没有插槽部分；0.5.7 之前的游戏仍然可以打开并阅读锻造炉，但已更新的服务器会拒绝它请求的每一次改动（升级、合并、调谐、重排、修复、Tinkerer's Badge），并提示“请更新游戏以使用此功能。”
