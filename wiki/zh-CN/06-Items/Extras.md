<!-- wiki-i18n source: b961ad7c5408494d -->
<!-- wiki-i18n title: 附加装置 -->
# 附加装置 {#extras}

附加装置是装在舰船**附加槽位**中的各种小工具（Protos、Kitefin、Ostirion 和 Nomad，也就是你一开始拥有或购买的舰船，每套配置各有两个；Paragon、Ironclad、Wraith 和 Storm，也就是你自己制造的舰船，各有三个；装上 Extra Slots CPU 后再多 3、5 或 7 个）。你可以从快捷栏的“附加装置”选择器中启用它，或者通过你为它设置的快捷栏槽位启用。它们只在你当前驾驶的配置中生效：装在另一套配置里的，会等到你切换配置后才开始工作。

| 附加装置 | 效果 | 次数 | 价格 |
| :---- | :----------- | :--- | :---- |
| **Repair Drone I 至 IV** | 修复你的船体，每秒分别为最大值的 1.5%、2.25%、3.5% 和 5% | 无限 | 5,000 / 15,000 / 35,000 信用点，2,000 Thulium |
| **Cloaking CPU S** | 隐藏你的舰船 | 10 | 5,000 Thulium |
| **Cloaking CPU M** | 隐藏你的舰船 | 25 | 11,250 Thulium |
| **Cloaking CPU L** | 隐藏你的舰船 | 50 | 20,000 Thulium |
| **P.E.T. Station I 至 III** | 开启时，2、3 或 5 只已对接的 [P.E.T.](/wiki/03-Mechanics/Pets.md#the-station) 为你的飞船提供加成、获得经验并工作；关闭时，它们什么都不做 | 开 / 关 | 装配站，研究后（见下面的物品树） |
| **Auto-Rocket CPU** | 开启时，自动向战斗目标发射你的当前火箭 | 开 / 关 | 装配站，研究后（见下面的物品树） |

Cloaking CPU 只在商店出售。它们无法融合，也没有任何渠道会免费赠送。**EMP Charge** 不再是附加装置：从 0.4.21 起它是消耗品，像火箭一样以堆叠方式携带，不装在任何槽位里，所以不占用你的附加槽位（见[火箭](/wiki/06-Items/Rockets.md#emp-charge)）。两道 **Energetic Wall** 也不再是附加装置：从 0.4.22 起它们同样是消耗品，以堆叠方式携带，不装在任何槽位里（见 [Energetic Wall](#energetic-wall)）。

新飞行员的**新手套装**已经在 Protos 的两个附加槽位里装好了两件附加装置：一个 **Base CPU I**（可用 10 次，传送到你所属企业的基地）和一个 **Repair Drone I**。想使用它们，请从快捷栏的“附加装置”选择器把它们拖到一个槽位上。只有新飞行员才会拿到这套装备：在 0.4.10 之前开始游戏的飞行员没有它。

另有八种 CPU 不出售：在 Skylab 的研究中心研究完成后，装配站就能制造它们（见[研究](/wiki/03-Mechanics/Research.md)）。它们是 Extra Slots CPU I、II、III，Jump CPU，Base CPU I、II、Auto-Repair CPU，以及 Auto-Rocket CPU；各自的作用见[最后一节](#research-cpus)。和 Cloaking CPU 一样，Jump CPU 和 Base CPU 也是留给平静时刻用的：在你开火或被击中后的 10 秒内，这三者都无法启动。两种传送 CPU，也就是 Jump CPU 和 Base CPU，在你携带任务物品时同样无法使用（“携带任务物品时无法使用传送 CPU。”）：见[任务物品](/wiki/03-Mechanics/Quests.md#quest-items)。

每个附加装置在快捷栏的槽位上都有一个简短标签：Repair Drone 是 **REP**，Cloaking CPU 是 **CLK**，Auto-Repair CPU、Auto-Rocket CPU、Base CPU 和 Jump CPU 依次是 **ARP**、**ARL**、**BSE** 和 **JMP**。消耗品有各自的标签：**EMP**，以及 Energetic Wall 的 **WAL**。Extra Slots CPU 没有槽位：它们安装在你的 Skylab 里。三个 **P.E.T. Station** 物品和其他附加装置一样，标签是 **PET**：装备一个，它的槽位就会把 Station 在**开启**和**关闭**之间切换（两次按下之间相隔一秒），并显示当前是哪一个。开启时，已对接的 [P.E.T.](/wiki/03-Mechanics/Pets.md) 计入，关闭时不计入。**Auto-Rocket CPU** 的切换方式相同：开启或关闭。把鼠标指向槽位，可以看到现在按下它会发生什么，或者为什么按了也没用。

![The Extras picker of the hotbar: the Repair Drone, the Auto-Repair, Cloaking, Base and Jump CPUs and the P.E.T. Station you have fitted (REP, ARP, CLK, BSE, JMP, PET), to drag onto a slot](../../img/wiki-img/shots/cpu-hotbar.jpg)
![The Consumables picker of the hotbar: the EMP Charge and the Energetic Wall I and II (EMP, WAL) to drag onto a slot, with how many of each you hold](../../img/wiki-img/shots/emp-hotbar.jpg)
![The hotbar with extras on its slots: a Repair Drone, a Cloaking CPU with its uses left, the P.E.T. Station that says ON, the EMP Charge and the Energetic Wall I and II with the number of each you carry](../../img/wiki-img/shots/hotbar-slots.jpg)
![The Repair Drone of an extra slot docked to its ship and its wingmen](../../img/wiki-img/shots/repair-drones-extra.jpg)
![The Shop's Consumables category: the EMP Charge and the Energetic Wall I with their prices in Thulium, and the Energetic Wall II, which only Assembly makes](../../img/wiki-img/shots/shop-consumables.jpg)

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## 物品树 {#item-tree}

装配站制造的东西要先有对应的科技；将指针悬停在物品上可看到研究所需的时间。科技树、燃料和加速见 [研究](/wiki/03-Mechanics/Research.md)。

```tree
P.E.T. Station I | extra, common | craft 100000 Credits, 2000 Thulium, 300 s | research 10800 s, 10800 science | 25 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md
Cloaking CPU S | extra, common | buy 5000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Repair Drone I | extra, common | buy 5000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone II | extra, common | buy 15000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone III | extra, common | buy 35000 Credits | /wiki/06-Items/Extras.md#repair-drones
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
P.E.T. Station II | extra, uncommon | craft 400000 Credits, 6000 Thulium, 600 s | research 36000 s, 36000 science | 60 Ship Fragment, 6 Reinforced Hull Plate, 4 Power Core, 8 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md
Cloaking CPU M | extra, uncommon | buy 11250 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 2 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Extras.md#base-cpus
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu
P.E.T. Station III | extra, rare | craft 1500000 Credits, 18000 Thulium, 900 s | research 86400 s, 86400 science | 120 Ship Fragment, 12 Reinforced Hull Plate, 8 Power Core, 2 Ancient Control Unit, 12 Velkonite Reinforced Plate, 4 Orvium Reinforced Plate | /wiki/06-Items/Extras.md
Auto-Rocket CPU | extra, rare | craft 20000 Thulium, 900 s | research 36000 s, 36000 science | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 1 Ancient Control Unit, 8 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-rocket-cpu
Repair Drone IV | extra, rare | buy 2000 Thulium | /wiki/06-Items/Extras.md#repair-drones
Cloaking CPU L | extra, rare | buy 20000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 6 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu

P.E.T. Station I -> P.E.T. Station II -> P.E.T. Station III
Cloaking CPU S -> Cloaking CPU M -> Cloaking CPU L
Repair Drone I -> Repair Drone II -> Repair Drone III -> Repair Drone IV
Extra Slots CPU I -> Extra Slots CPU II -> Extra Slots CPU III
Base CPU I -> Base CPU II
```
<!-- item-tree:end -->

## Repair Drone {#repair-drones}

启用 Repair Drone（REP）后，它会修复船体直到修满。只有在 10 秒内没有被击中之后才会开始，任何一次被击中都会将其关闭。装备了多台时，只有最好的那一台生效。[Auto-Repair CPU](#auto-repair-cpu) 会替你再次启用它。修复速率见[战斗](/wiki/03-Mechanics/Combat.md)。修复期间，小型维修无人机会从舰船飞出，环绕舰船并向船体照射光束：Repair Drone I 一台，II 两台，III 或 IV 三台，附近的飞行员也能看到；修复停止后，它们会重新对接。

## Cloaking CPU

按下 CLK 槽位即可隐形。**一次按下就是一次使用**，无论是哪个型号，剩余次数会显示在槽位上和机库中。隐形**没有时间限制**：它会一直保持，直到你关闭它或有什么东西打断它。

- **谁看不到你。** 其他企业的飞行员和外星人完全看不到你的舰船：它不在他们的画面上，也不在他们的目标列表中，没有人能锁定它。其他企业的企业飞行员同样会无视它。
- **雷达光点。** 地图上除你所在企业之外的其他每名飞行员，都会在小地图上你所在的位置看到一个普通的**红点**，让他们知道附近有人隐形。这个红点没有名字、舰船、企业或编号，无法点击或选为目标；把鼠标悬停在上面，只会显示“这里有东西处于隐形状态”。它是圆形的，位于一个圆环之内（小地图上的舰船是方块），圆环会缓慢地一明一暗，如果你开启了“减弱动态效果”，则保持静止。服务器每秒刷新它大约两次，你的游戏会在两次刷新之间让它平滑移动。它只说明那里有人以及在哪里，不说明是谁：看到你隐形的飞行员可以跟着这个红点走，对准它的**火箭爆炸**仍然能找到你。
- **谁能看到你。** 你能看到自己的舰船，它很淡，带有轮廓。你所在企业的飞行员会把你看作一个淡淡的幽灵；其他企业的战队成员则看不到，因为战队会接纳任何提出申请的人。没有人能把幽灵选为目标，你所在企业的人也不行。
- 在安全区内、CPU 充能期间，或在被击中或开火后的 **10 秒**内，**无法隐形**。
- **什么会结束隐形。** 再次按下槽位；你的第一轮齐射或第一枚火箭（命中时你就会被看到）；进入安全区；CPU 离开了你正在驾驶的配置；你周围 **1,500 单位内有 EMP 触发**，无论是谁发射的（你所在企业的也算，但同小队队友的不算）；以及命中你的火箭的范围爆炸。时间不会结束隐形，拾取货物不会（你拿走的货箱对所有人而言都消失了，所以他们只会得知有东西曾在那个位置的拾取范围内，而不知道是谁），技能不会，黑洞的辐射会伤害隐形的舰船，但不会结束它的隐形。退出登录或舰船被摧毁会结束隐形，因为没人驾驶的舰船不算隐形。
- **充能。** 隐形结束后，无论以何种方式结束，CPU 都会充能 **60 秒**。充能属于你本人，而不属于舰船：即使你通过传送门跃迁、退出登录或舰船被摧毁，它也会继续。每次按下仍然消耗一次使用次数。
- 正在追你的**外星人**会丢失目标。你隐形时，你的击杀归属会被释放。
- **火箭。** 没有人能把制导火箭锁定在你身上，直射单体火箭会从你身上穿过。**范围爆炸**仍然会伤害它所覆盖的舰船并结束其隐形，而能看到该舰船所在位置的飞行员，会在伤害数字出现之前先看到这艘舰船。发射火箭算作一次射击：它会像齐射一样结束你自己的隐形（CPU 随后按上面所说的 60 秒充能），而且无论你是否隐形，发射后的 10 秒内你都无法隐形。
- **黑洞**会像吞噬其他舰船一样吞噬隐形的舰船，整张地图都会得知。
- **你会看到什么。** 你的舰船变得半透明，带有紫色虚线轮廓，它的无人机也随之淡出，屏幕顶部会出现一个标签，写着“隐形”和剩余使用次数（没有秒数：因为没有计时）。CLK 槽位显示剩余次数；隐形期间它会泛起紫色光芒并显示“开”，隐形结束后（无论以何种方式结束），它会变暗并倒数 60 秒的充能时间。服务器拒绝的按下（充能中、在安全区内、最近 10 秒内被击中或开火）会让槽位闪红，并弹出消息告诉你原因。盟友显示为淡淡的幽灵，名字前带有幽灵标记，而在你附近隐形的飞行员会在一圈涟漪中消失。像 REP 一样，把 CLK 从快捷栏的“附加装置”拖到槽位上即可使用。
- **使用次数**随 CPU 一并保存。退出登录、舰船被摧毁或重启游戏都不会返还次数，被你取消的启动也照样消耗。当一个 CPU 的最后一次使用次数用完时，它就被耗尽，如果你的物品栏里有同一种 CPU 的备用件，它的槽位会由备用件补上。
- 同一套配置中的**多个 CPU** 不会叠加。剩余次数最少的那个会先被使用。

S、M、L 型号的行为完全相同：更大的型号只是每次使用更便宜（分别为 500、450 和 400 Thulium）。

## Energetic Wall

按下 WAL 槽位，一道**等离子墙**就会立在**你的光标处**，与飞船到光标的连线垂直：一条长 360 单位（约三个半舰船模型）、宽 10 单位的带状区域。它的中心距舰船中心最远 **450 单位**：光标更远时，它立在连线上 450 单位处；光标近于 120 单位时，它被推到 120 单位处。槽位就绪时，一条淡淡的点线和一个幽灵轮廓会显示它将立在哪里。如果游戏不知道光标在哪里，它会立在舰船中心前方 220 单位处，横在航向上。Energetic Wall 是**消耗品**，与 [EMP Charge](/wiki/06-Items/Rockets.md#emp-charge) 一样：物品栏里的一个堆叠，**不占用任何舰船的槽位**（0.4.22 之前它是附加装置）。要使用它，把它从快捷栏的“消耗品”拖到槽位上；两个等级是两个条目，所以一个槽位放一个等级。它是用来躲在后面、封住一条通路的，不是用来站在里面的。

- **它挡住什么。** 穿过它的每一发射击都会改为击中墙体，不论是谁打的、从哪一侧打来：激光齐射、火箭、外星人的齐射。墙后的东西毫发无损，伤害由墙的耐久承担。在墙上爆炸的火箭，爆炸波只会波及近侧的舰船，不会波及墙后的舰船。你自己的射击也一样：你不能隔着自己的墙向外射击。 N.I.K.E. 和 Dormant Swamp 的炮塔会从墙上方飞越，就像飞越小行星一样。
- **它灼烧什么。** 船体碰到墙带的任何舰船每秒受到 **2,500 点伤害**，先扣护盾，你自己的舰船也一样，外星人和企业飞行员同样如此。在安全区内或处于重生保护中的舰船不会被灼烧，同一艘舰船上的两条墙带也不会叠加。
- **它能维持多久。** 1 级墙有 **30,000 点耐久**，2 级墙有 **90,000**。墙自己每秒会损失六十分之一，所以没人攻击的墙会在 **60 秒**后消失。射击会缩短这个时间：一艘装有十二把 Helios Beam、使用 x4 弹药的 Wraith 大约 3.5 秒就能击毁一道 1 级墙。
- **一次一道，每次按下一道。** 新墙会取代你的旧墙。按下之后，该物品需要 **90 秒**充能；等待时间属于你本人而不是舰船，死亡或下线都不会缩短它。每次按下消耗**槽位所放等级的一道墙**，而且只在墙立起来时才消耗：游戏拒绝的按下（见下）什么也不消耗，也不开始等待。该等级一道也不剩时，会提示“没有剩余的 Energetic Wall。”，也绝不会用另一个等级代替。
- **哪里不行。** 安全区或重生保护期间不行；墙带会碰到安全区或星系之门的地方不行；隐形时不行；墙带的中心会落在地图之外的地方也不行。游戏会告诉你是哪种情况。
- **击杀。** 被墙摧毁的舰船死于辐射，击杀记在 15 秒内最后击中它的敌方飞行员头上（如果有的话）。立墙的人不会因为并非自己射出的伤害而得到击杀记录。被墙摧毁的外星人不产出任何东西：没有奖励，也没有战利品。
- **外星人不会绕开它。** 它们要么穿过去被灼烧，要么待在自己一侧朝墙射击。
- **你看到的样子。** 一条蓝白色的光带，上面有明亮的线条沿着它跑动，两端各有一根光柱；射击命中的地方会闪光，快耗尽时会闪烁。2 级墙则发出黄色的光，核心更粗更亮，光晕也更强，但它的光带和 1 级墙一样宽，都是 10 单位。旁边一条细细的生命条会变短，并变成琥珀色，再变成红色；你的槽位用弧线显示墙的剩余寿命，用阴影显示等待时间。刚立起的墙会闪光亮起，被击毁的墙会化作火花崩塌，时间耗尽的墙会逐渐消散。槽位上的数字也是该等级剩余的墙数。
- **怎么得到和携带。** Energetic Wall I 在商店里每道售价 **250 Thulium**，一个堆叠最多携带 **20** 道（你在[拍卖行](/wiki/03-Mechanics/Auction.md)挂出的也算在内）。Energetic Wall II 在研究中心研究完成后，在装配站制造，**每次制造一道**，需要 **600 Thulium**、5 个 Ship Fragment 和 1 个 Power Core（正常速度下 6 小时：[研究](/wiki/03-Mechanics/Research.md)），最多携带 **10** 道。与火箭一样，携带的墙会随赛季丢失，除非放进运输储藏库；储藏库里的墙无法使用。你自己制造的 Energetic Wall II 可以在拍卖行出售；商店出售的 Energetic Wall I 则永远不能。

## 研究中心的 CPU {#research-cpus}

其中两个 CPU 和每条升级链的最后一阶一样，需要 Dark Matter Plate：**Extra Slots CPU III** 需要 4 块（另需 2 个 Ancient Control Unit 和 6 块 Orvium Reinforced Plate），**Base CPU II** 需要 4 块（另需 1 个 Ancient Control Unit 和 2 块 Orvium Reinforced Plate），所以请先研究 Dark Matter Plate（[Dark Matter 与 Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)）。

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
| [Energetic Wall II](/wiki/06-Items/Extras.md#energetic-wall) | 6 小时 | – | 600 | 2 分钟 |
| [Auto-Rocket CPU](/wiki/06-Items/Extras.md#auto-rocket-cpu) | 10 小时 | – | 20,000 | 15 分钟 |

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

### Auto-Rocket CPU

- **作用。** 开启期间，当你处于战斗中（你的激光瞄准外星人或敌方飞行员）时，只要按下“发射火箭”键本可以发射，它就会自动向该目标发射你上一次发射的当前火箭：火箭的计时已就绪，且你还剩一枚。服务器会像检查你的发射一样检查每一次发射。
- **开关。** 装备在附加装置槽位中，按下它的 ARL 槽位即可开启或关闭。默认关闭，并保持你上次的设置，重新登录后也一样。槽位会显示开启或关闭，CPU 发射时会亮起。
- **它从不做的事。** 它从不自己选目标，不攻击小行星，不在安全区内或隐形时发射，也从不发射 N.U.K.E. 或 N.I.K.E.。你自己发射的火箭总是有效。如果 3 分钟内没有按键、点击或移动鼠标，它会等你有所操作。
- **火箭用完。** 它只会提醒你一次，等你有了更多火箭就会重新发射。


<!-- research-cpus:end -->
