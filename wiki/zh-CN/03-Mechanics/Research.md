<!-- wiki-i18n source: 0e8dd778c7574921 -->
<!-- wiki-i18n title: 研究 -->
# 研究 {#research}

**研究中心**是你的 [Skylab](/wiki/03-Mechanics/Skylab.md) 的实验室。你向它投入资源，它把资源变成**科研点**，科研点则用来研究**科技**。在[装配站](/wiki/06-Items/Overview.md#upgrading-modules)里制造任何东西，都要先有对应的科技：舰船、激光、推进器和 CPU，在研究完成之前都无法制造。

本页汇集了完整的科技树及每项科技所需的时间、每种资源提供的科研点、Thulium 加速、Dark Matter 规则和新的 CPU。所有数字都直接读取自游戏自身的数据，因此始终与游戏中一致。

![The Research view with a technology that needs Dark Matter picked: its Dark Matter row, the Add and Take back buttons, where Dark Matter comes from and the Wiki button](../../img/wiki-img/shots/research-dark-matter.jpg)
![The Research view filtered to the Defence tree: the shield and hull formations, each a technology with its Dark Matter](../../img/wiki-img/shots/research-formations.jpg)
![The Research view of the Skylab with the pointer on Impulse Thruster III: its kind and tier, what it does, its numbers, the four tiers of its family and what Assembly asks to craft it](../../img/wiki-img/shots/research-hover.jpg)

## 研究中心 {#the-research-centre}

<!-- research-centre:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **核心 10 级解锁。** 研究中心是你 [Skylab](/wiki/03-Mechanics/Skylab.md) 的一个模块，建造方式与其他模块相同：从物品栏扣除 25 个 Ship Fragment（舰船须已降落）、25,000 信用点和 500 Thulium。它的界面是 Skylab 页面的**研究**视图。
- **1 到 10 级。** 等级越高，储罐越大，耗电也越多。它不会让研究变快：一项科技在每个等级都花同样的时间。
- **储罐。** 研究中心把科研点存在储罐里，储罐在 1 级可容纳 12 小时 的研究量，每升一级多 25%（见下表）。
- **燃料变成科研点。** 你投入的资源立刻变成科研点，如燃料表所示。研究在其研究时间的每一秒消耗 1 科研点；储罐空了就暂停，等你再次向研究中心投入资源后继续。
- **免费的第一个小时。** 新的研究中心储罐里一开始就有 3,600 科研点，相当于 1 小时 的研究量。
- **一次一项。** 研究中心一次只研究一项科技，但你可以用“加入队列”按钮在它后面再排最多 5 项。前一项完成的那一刻，下一项就会自动开始，你不在线也一样。加入队列不花任何东西：科技在开始时才扣除 Dark Matter，队列里的科技可以免费移除。
- **你不在线时。** 研究按服务器的时钟进行，所以你下线后它仍会继续，直到完成或储罐变空。电力不足或研究中心升级都不会让它停下。
- **电力。** 研究中心在 1 级耗电 25，每升一级多 15%，并且无法关闭。
- **重置后一切保留：** 你的科技、储罐里的科研点、已放入的 Dark Matter、进行中的研究和加速。
- **你已拥有的就是你的。** 研究加入游戏时，每位飞行员都获得了自己当时已拥有的每件物品的科技，以及这些物品所需的科技。之后才到你手上的物品（礼物、兑换码、奖励）不会解锁它的科技。
- **核心低于 10 级时**无法研究，所以在装配站里还不能制造任何新东西。空间站任务会带你把核心升上去。

<!-- research-centre:end -->

**激光增幅器与最后一阶。** II 至 IV 阶的 Damage Amp、Crit Amp 和 Penetration Amp 与其他可制造的东西一样需要研究。增幅器系列推出时持有或排队制作了增幅器的飞行员，获得了这些增幅器各自的科技，以及更低阶的科技。有十二项科技需要另一棵树中的科技，即资源树中 Dark Matter Plate 的科技，因为每条升级链的最后一阶需要三块板：IV 阶的 Damage Amp、Crit Amp 和 Penetration Amp，IV 阶的 Absorption Shield Cell 和 Capacity Shield Cell，IV 阶的 Impulse Thruster 和 Momentum Thruster，以及 Heavy Shield Core、Engine III、Helios Beam、Extra Slots CPU III 和 Base CPU II。以前研究过其中某一项的飞行员会保留它，但要制作它所需的板，需要先研究这块板的科技。下面的树没有为它画箭头，但表格列出了它，游戏里的卡片也会写出它的名字（[Dark Matter 与 Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)）。

在你 Skylab 的**研究**视图里，一项科技告诉你的比下面树中的方框更多。将指针悬停在一项科技上，会弹出一张卡片，写着研究时间和消耗的科研点，下面是该物品**是什么、有什么用**：它的类型和在所属系列中的等级（例如四个 Impulse Thruster 中的第三个）、描述、与机库和商店所示相同的数值（激光的伤害、暴击率和射程，护盾的护盾容量、充能速率和吸收率，推进器的速度提升和速度倍率，火箭的伤害、爆炸半径和射程，无人机编队给予什么、要付出什么代价）、所属系列各等级的小表格，以及研究完成后装配站制造它所需的东西：时间、信用点和 Thulium，以及材料。这样你在研究之前就能看到某个等级能带来什么。点击科技即可选中它：树旁边的卡片会在**开始研究**按钮下方完整显示同样的内容。 有研究在进行时，**加入队列**会取代开始按钮的位置：已排队的科技在树上显示顺序编号，正在进行的研究下方的队列卡片会把它们全部列出，每一项都有一个叉号可以移除。如果下一项无法开始（它所需的 Dark Matter 不在研究中心里，或者储罐已空），队列会等待并说明原因，直到你解决问题并点击**开始队列**。

### 各等级的储罐 {#the-tank-at-every-level}

<!-- research-tank:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| 等级 | 储罐（科研点） | 可容纳的研究量 | … 加速时 | 电力 |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 43,200 | 12 小时 | 6 小时 | 25 |
| 2 | 54,000 | 15 小时 | 7.5 小时 | 28.7 |
| 3 | 67,500 | 18.8 小时 | 9.4 小时 | 33.1 |
| 4 | 84,375 | 23.4 小时 | 11.7 小时 | 38 |
| 5 | 105,469 | 29.3 小时 | 14.6 小时 | 43.7 |
| 6 | 131,836 | 36.6 小时 | 18.3 小时 | 50.3 |
| 7 | 164,795 | 45.8 小时 | 22.9 小时 | 57.8 |
| 8 | 205,994 | 57.2 小时 | 28.6 小时 | 66.5 |
| 9 | 257,492 | 71.5 小时 | 35.8 小时 | 76.5 |
| 10 | 321,865 | 89.4 小时 | 44.7 小时 | 87.9 |

<!-- research-tank:end -->

## 燃料 {#fuel}

你向研究中心投入资源，每个单位立刻变成科研点。获得一个单位越费功夫，它提供的科研点就越多：数值依据的是获得的难度，而不是稀有度标签。矿石是例外：一个单位提供的科研点比采集器开采它所花的秒数更多，所以处于等级中段的采集器一小时产出的矿石大约够两小时的研究。矿石来自你 [Skylab](/wiki/03-Mechanics/Skylab.md#resource-storage) 的资源仓库；其他资源都来自你的物品栏，并且舰船必须已降落。Velkonite Reinforced Plate、Orvium Reinforced Plate、Dark Matter Plate、Dark Matter、信用点和 Thulium 不能当作燃料烧掉；Reinforced Hull Plate 可以。

<!-- research-fuel:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| 资源 | 稀有度 | 取自 | 每单位科研点 | 1 小时所需数量 |
| :--- | :--- | :--- | ---: | ---: |
| [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) | 普通 | 你的物品栏 | 5 | 720 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | 普通 | 你的物品栏 | 5 | 720 |
| [Daraxium](/wiki/06-Items/Resources.md#daraxium) | 普通 | 你的物品栏 | 7 | 515 |
| [Nyxite](/wiki/06-Items/Resources.md#nyxite) | 普通 | 你的物品栏 | 7 | 515 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | 普通 | 你的物品栏 | 8 | 450 |
| [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) | 普通 | 你的物品栏 | 33 | 110 |
| [Power Core](/wiki/06-Items/Resources.md#power-core) | 优秀 | 你的物品栏 | 100 | 36 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | 优秀 | 资源仓库 | 210 | 18 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | 稀有 | 资源仓库 | 321 | 12 |
| [Ancient Control Unit](/wiki/06-Items/Resources.md#ancient-control-unit) | 稀有 | 你的物品栏 | 650 | 6 |

最后一列是不加速时维持 1 小时研究所需的单位数（向上取整）；加速时需要 2 倍。

<!-- research-fuel:end -->

## Thulium 加速 {#the-thulium-boost}

<!-- research-boost:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **5,000 Thulium** 可买一次加速：研究中心将在 **24 小时内以 2 倍速度**研究。
- 它还会让**科研点以 2 倍速度消耗**，所以加速买到的是时间而不是燃料：一项科技无论是否加速，消耗的科研点都一样。
- 加速在你买下的那一刻开始，并按时钟走，不论储罐里有没有燃料，所以请在研究进行时购买。没有任何研究时，研究中心会拒绝购买。
- 加速可以叠加：在另一次加速进行时再买一次，会把它的结束时间延后 24 小时，最多向后叠加到 72 小时。加速属于你的研究中心，而不属于某一项研究。

从研究一开始就加速时，加速对研究时间的影响：

| 研究时间 | 加速后 | 覆盖全程所需加速次数 | Thulium |
| :--- | :--- | ---: | ---: |
| 30 分钟 | 15 分钟 | 1 | 5,000 |
| 3 小时 | 1 小时 30 分钟 | 1 | 5,000 |
| 6 小时 | 3 小时 | 1 | 5,000 |
| 10 小时 | 5 小时 | 1 | 5,000 |
| 1 天 | 12 小时 | 1 | 5,000 |
| 2 天 | 1 天 | 1 | 5,000 |

<!-- research-boost:end -->

## Dark Matter

科技树顶端的科技还需要 Dark Matter。它来自[黑洞](/wiki/03-Mechanics/Black-Hole.md#dark-matter)：抵达黑洞的 N.I.K.E. 火箭会留下一些；偶尔也会从 [Dormant 虫群](/wiki/05-Swarms/Dormant-Swarm.md)的 Dormant Pulse 身上得到。

<!-- research-dark-matter:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- 下表中的 16 项科技，每项除科研点外还需要 **10 个 Dark Matter**：开始前把它放入研究中心（取自物品栏，舰船须已降落），研究开始时会取走它。
- **规则：** 稀有度达到 史诗 或更高、且研究耗时 10 小时 或更久的物品。用来产出 Dark Matter 的 N.I.K.E. 永远不需要它。
- **无人机编队**不适用此规则：每项编队研究都需要 Dark Matter，按强度为 5、13 或 20，如下表所示。
- **取消研究时，**为它放入的 Dark Matter 会退回研究中心。进度和已经消耗的科研点则不会退回。
- 全部加起来共需 349 个 Dark Matter。

| 科技 | 稀有度 | 研究时间 | Dark Matter |
| :--- | :--- | :--- | ---: |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | 史诗 | 10 小时 | 10 |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | 史诗 | 10 小时 | 10 |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | 史诗 | 10 小时 | 10 |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | 史诗 | 10 小时 | 10 |
| [Starfire-III](/wiki/06-Items/Lasers.md#lasers) | 神话 | 1 天 | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | 神话 | 1 天 | 10 |
| [Damage Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | 史诗 | 10 小时 | 10 |
| [Crit Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | 史诗 | 10 小时 | 10 |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | 史诗 | 1 天 | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | 史诗 | 1 天 | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | 神话 | 2 天 | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | 神话 | 1 天 | 10 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | 传说 | 1 天 | 10 |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 史诗 | 1 天 | 10 |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 史诗 | 1 天 | 10 |
| [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 史诗 | 10 小时 | 5 |
| [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 史诗 | 1 天 | 13 |
| [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 史诗 | 10 小时 | 5 |
| [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 神话 | 2 天 | 20 |
| [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 史诗 | 10 小时 | 5 |
| [Ballista Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 史诗 | 1 天 | 13 |
| [Stiletto Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 神话 | 2 天 | 20 |
| [Rampart Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 神话 | 2 天 | 20 |
| [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 史诗 | 1 天 | 13 |
| [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 史诗 | 10 小时 | 5 |
| [Culler Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 史诗 | 1 天 | 13 |
| [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 史诗 | 1 天 | 13 |
| [Auger Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 史诗 | 1 天 | 13 |
| [Cordon Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 史诗 | 1 天 | 13 |
| [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 史诗 | 10 小时 | 5 |
| [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 史诗 | 1 天 | 13 |
| [Penetration Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | 史诗 | 10 小时 | 10 |

<!-- research-dark-matter:end -->

## 科技树 {#the-technology-tree}

每个方框是一项科技：它让你能制造的物品，名字下方是研究时间（时钟），需要 Dark Matter 的还会有 Dark Matter 徽章。箭头从一项科技指向需要它的科技，你要先研究箭头起点的那一项；没有箭头的方框可以立即研究。将指针悬停在方框上，可以看到研究时间、消耗的科研点，以及研究完成后装配站对该物品的要求；点击方框可打开该物品的页面。这些树直接依据游戏自身的数据绘制。其中两棵树 **防御** 和 **打击与机动** 收录了十六种[无人机编队](/wiki/03-Mechanics/Formations.md)。

<!-- research-tree:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

### 推进与速度 {#tree-propulsion}

```tree research
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines

Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```

### 护盾与防御 {#tree-shields}

```tree research
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cores

Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```

### 激光与弹药 {#tree-lasers}

```tree research
Quantum Laser III | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Quantum Laser II, 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-III | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser III, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-III, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Damage Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Crit Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Damage Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Damage Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Crit Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Crit Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Penetration Amp I, 20 Daraxium, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Penetration Amp II, 1 Power Core, 30 Nyxite, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp IV | laser-amp, epic | craft 1200 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Penetration Amp III, 1 Power Core, 30 Cataclysite, 40 Quorvium, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-

Quantum Laser III => Starfire-III => Helios Beam
Damage Amp II => Damage Amp III => Damage Amp IV
Crit Amp II => Crit Amp III => Crit Amp IV
Penetration Amp II => Penetration Amp III => Penetration Amp IV
```

### 增益 {#tree-boosters}

```tree research
Laser Damage Booster II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
```

### 无人机 {#tree-drones}

```tree research
Master Drone | drone, rare | craft 40000 Thulium, 60 s | research 36000 s, 36000 science | 1 Slave Drone, 100 Ship Fragment | /wiki/06-Items/Drones.md#available-drones
```

### 舰船 {#tree-ships}

```tree research
Paragon | ship, rare | craft 1500 Thulium, 900 s | research 21600 s, 21600 science | 120 Ship Fragment, 20 Reinforced Hull Plate, 5 Power Core | /wiki/02-Ships/Paragon.md
Ironclad | ship, epic | craft 10500 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit | /wiki/02-Ships/Ironclad.md
Storm | ship, epic | craft 15000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit | /wiki/02-Ships/Storm.md
Wraith | ship, mythical | craft 20000 Thulium, 900 s | research 172800 s, 172800 science, 10 Dark Matter | 300 Ship Fragment, 50 Reinforced Hull Plate, 15 Power Core, 3 Ancient Control Unit | /wiki/02-Ships/Wraith.md
```

### 资源 {#tree-resources}

```tree research
Dark Matter Plate | resource, mythical | craft 250 Thulium, 120 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Velkonite Reinforced Plate, 1 Orvium Reinforced Plate, 5 Dark Matter | /wiki/06-Items/Resources.md#dark-matter-plate
```

### 火箭 {#tree-rockets}

```tree research
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
```

### CPU {#tree-cpus}

```tree research
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 6 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 2 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Extras.md#base-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu

Extra Slots CPU I => Extra Slots CPU II => Extra Slots CPU III
Base CPU I => Base CPU II => Jump CPU
```

### 防御 {#tree-defence}

```tree research
Testudo Formation | formation, epic | craft 7500 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Adamant Formation | formation, epic | craft 9000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Rampart Formation | formation, mythical | craft 38500 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Sanctum Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Redoubt Formation | formation, epic | craft 21000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Cordon Formation | formation, epic | craft 21500 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations

Testudo Formation => Sanctum Formation => Rampart Formation
Adamant Formation => Redoubt Formation => Cordon Formation
```

### 打击与机动 {#tree-strike-mobility}

```tree research
Bodkin Formation | formation, epic | craft 21000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Asterism Formation | formation, epic | craft 7000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Gemini Formation | formation, mythical | craft 38000 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Ballista Formation | formation, epic | craft 24000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Stiletto Formation | formation, mythical | craft 46000 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Shrike Formation | formation, epic | craft 8500 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Culler Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Auger Formation | formation, epic | craft 20500 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Centurion Formation | formation, epic | craft 8000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Gyre Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations

Asterism Formation => Bodkin Formation => Ballista Formation
Gemini Formation => Stiletto Formation
Centurion Formation => Shrike Formation => Culler Formation
Gyre Formation => Auger Formation
```


<!-- research-tree:end -->

## 全部科技 {#all-the-technologies}

<!-- research-technologies:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| 科技 | 需先研究 | 类别 | 研究时间 | 科研点 | Dark Matter |
| :--- | :--- | :--- | ---: | ---: | ---: |
| [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 分钟 | 1,800 | – |
| [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 小时 | 10,800 | – |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 小时 | 36,000 | 10 |
| [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 分钟 | 1,800 | – |
| [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 小时 | 10,800 | – |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 小时 | 36,000 | 10 |
| [Engine III](/wiki/06-Items/Propulsion.md#engines) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | B | 3 小时 | 10,800 | – |
| [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 分钟 | 1,800 | – |
| [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 小时 | 10,800 | – |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10 小时 | 36,000 | 10 |
| [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 分钟 | 1,800 | – |
| [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 小时 | 10,800 | – |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10 小时 | 36,000 | 10 |
| [Heavy Shield Core](/wiki/06-Items/Shields.md#shield-cores) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | B | 3 小时 | 10,800 | – |
| [Quantum Laser III](/wiki/06-Items/Lasers.md#lasers) | – | B | 3 小时 | 10,800 | – |
| [Starfire-III](/wiki/06-Items/Lasers.md#lasers) | [Quantum Laser III](/wiki/06-Items/Lasers.md#lasers) | D | 1 天 | 86,400 | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Starfire-III](/wiki/06-Items/Lasers.md#lasers) | D | 1 天 | 86,400 | 10 |
| [Damage Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Damage Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10 小时 | 36,000 | 10 |
| [Crit Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Crit Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10 小时 | 36,000 | 10 |
| [Laser Damage Booster II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 小时 | 10,800 | – |
| [Shield Wall Booster II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 小时 | 10,800 | – |
| [Hull Plating Booster II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 小时 | 10,800 | – |
| [Master Drone](/wiki/06-Items/Drones.md#available-drones) | – | C | 10 小时 | 36,000 | – |
| [Paragon](/wiki/02-Ships/Paragon.md) | – | B | 6 小时 | 21,600 | – |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | – | D | 1 天 | 86,400 | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | – | D | 1 天 | 86,400 | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | – | D | 2 天 | 172,800 | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | – | D | 1 天 | 86,400 | 10 |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | B | 3 小时 | 10,800 | – |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | D | 1 天 | 86,400 | 10 |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | – | A | 30 分钟 | 1,800 | – |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | C | 10 小时 | 36,000 | – |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | D | 1 天 | 86,400 | 10 |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | – | B | 3 小时 | 10,800 | – |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10 小时 | 36,000 | – |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | D | 1 天 | 86,400 | 10 |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | – | B | 6 小时 | 21,600 | – |
| [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 小时 | 36,000 | 5 |
| [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 天 | 86,400 | 13 |
| [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 小时 | 36,000 | 5 |
| [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | D | 2 天 | 172,800 | 20 |
| [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 小时 | 36,000 | 5 |
| [Ballista Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 天 | 86,400 | 13 |
| [Stiletto Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 2 天 | 172,800 | 20 |
| [Rampart Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 2 天 | 172,800 | 20 |
| [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 天 | 86,400 | 13 |
| [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | C | 10 小时 | 36,000 | 5 |
| [Culler Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 天 | 86,400 | 13 |
| [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 天 | 86,400 | 13 |
| [Auger Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 天 | 86,400 | 13 |
| [Cordon Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1 天 | 86,400 | 13 |
| [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10 小时 | 36,000 | 5 |
| [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | D | 1 天 | 86,400 | 13 |
| [Damage Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30 分钟 | 1,800 | – |
| [Damage Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Damage Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3 小时 | 10,800 | – |
| [Crit Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30 分钟 | 1,800 | – |
| [Crit Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Crit Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3 小时 | 10,800 | – |
| [Penetration Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30 分钟 | 1,800 | – |
| [Penetration Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Penetration Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3 小时 | 10,800 | – |
| [Penetration Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Penetration Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10 小时 | 36,000 | 10 |

按研究时间划分的类别：

| 类别 | 研究时间 | 科技数 | 逐项研究合计 | 科研点 | Dark Matter |
| :--- | :--- | ---: | ---: | ---: | ---: |
| A | 30 分钟 | 8 | 4 小时 | 14,400 | 0 |
| B | 3 小时 至 6 小时 | 17 | 2 天 9 小时 | 205,200 | 0 |
| C | 10 小时 | 15 | 6 天 6 小时 | 540,000 | 95 |
| D | 1 天 至 2 天 | 20 | 24 天 | 2,073,600 | 254 |
| 全部 |  | 60 | 32 天 19 小时 | 2,833,200 | 349 |

逐项依次研究，整棵科技树共需 32 天 19 小时。若全程开着加速，需要 16 天 9 小时 30 分钟，即 17 次加速和 85,000 Thulium；消耗的科研点相同。

<!-- research-technologies:end -->

## CPU {#the-cpus}

新的 CPU 也在这里研究，然后在装配站制造。同样的表格和说明也在[附加装置](/wiki/06-Items/Extras.md#research-cpus)页面上。

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | 研究时间 | 需先研究 | 制造所需 Thulium | 制造时间 |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 分钟 | – | 12,000 | 5 分钟 |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10 小时 | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30,000 | 10 分钟 |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1 天 | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75,000 | 15 分钟 |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3 小时 | – | 8,000 | 5 分钟 |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10 小时 | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | 20,000 | 10 分钟 |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1 天 | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40,000 | 15 分钟 |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6 小时 | – | 15,000 | 10 分钟 |

它们都不在商店出售：先研究科技，再在装配站制造 CPU。将指针悬停在物品树中的 CPU 上，可查看装配站制造它需要什么。

### Extra Slots CPUs

- **作用。** Extra Slots CPU I、II、III 分别为每艘舰船增加 3、5、7 个附加槽位：本来有 3 个的舰船总共是 6、8、10 个，本来有 2 个的舰船总共是 5、7、9 个。更高级的 CPU 会取代前一级：II 不会叠加在 I 之上。
- **安装，而非携带。** Extra Slots CPU 不是物品：你在装配站领取后，它会自动安装到你的 Skylab，对两套配置下的每艘舰船都生效，并且不占用槽位。重置之后它仍然保留。
- **按顺序。** 请依次制造：I 安装后才能制造 II，II 安装后才能制造 III；在此之前，装配站会告诉你应先安装哪一个。三个总共需要 117,000 Thulium：12,000、30,000 和 75,000。

### Jump CPU

- **作用。** 把你的舰船跳跃到你所在世界的任意企业星区，无论是你自己企业的还是其他企业的，包括它们的主星区（`M`、`T` 和 `G`，星区 1 到 4），每次跳跃需要 **500 Thulium**。使用次数没有上限：你只需支付 Thulium。它永远不会通向危险星区（`DS`）或中立星区（`N`）。
- **跳跃。** 按下 JMP 槽位，在星系地图上选择星区并确认，舰船充能 5 秒，然后抵达该星区的一座星门，并像经过任何星门跳跃后一样受到保护。你抵达后，CPU 冷却 30 秒。
- **战斗中不可用。** 开火或被击中后 10 秒内无法启动，充能期间开火或被击中会取消跳跃；这时不会扣费。隐形时不能跳跃。
- **不能从中立星区出发：** 身处中立星区或没有企业的飞行员无法使用。
- 只要你不在战斗中，就可以从危险星区离开。

### Base CPUs

- **作用。** 把你的舰船传送到你所属企业的基地，落在空间站周围的安全区内（`M-1`、`T-1` 或 `G-1`，设有 Mission Control 的星区），不需要 Thulium。你从快捷栏的 BSE 槽位启动它们。
- **战斗中不可用。** 充能 10 秒，两者相同。开火或被击中后 10 秒内、隐形时、或已经在基地的安全区内时都无法启动，充能期间开火或被击中会取消它。

| CPU | 使用次数 | 冷却 |
| :--- | ---: | ---: |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 10 | 10 分钟 |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 25 | 5 分钟 |

- **用完即止，不会重新充能。** 每次使用会消耗该 CPU 的一次使用次数，次数用完的 CPU 就消失了：请制造新的。两个都装备时，更好的那个（II）先被使用。

### Auto-Repair CPU

- **作用。** 只要你本可以手动放出附加槽位里装备的 Repair Drone，它就会自动放出：船体没有满、无人机还没放出，并且距上次被击中已过 10 秒。无需设置任何船体比例。
- 它占用一个自己的附加槽位，如果同一配置的附加槽位里没有 Repair Drone，它什么也不做。它从不放出技能槽位里的 Repair Drone（那是 Emergency Repair 按钮）。
- **如果你手动停下无人机，**CPU 就不再理会它，直到你的船体重新满血，或你自己再次放出无人机。


<!-- research-cpus:end -->
