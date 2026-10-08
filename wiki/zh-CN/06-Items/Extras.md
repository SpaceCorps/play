<!-- wiki-i18n source: 93029f432757eb93 -->
<!-- wiki-i18n title: 附加装置 -->
# 附加装置 {#extras}

附加装置是装在舰船**附加槽位**中的各种小工具（Protos、Kitefin、Ostirion 和 Nomad，也就是你一开始拥有或购买的舰船，每套配置各有两个；Paragon、Ironclad、Wraith 和 Storm，也就是你自己制造的舰船，各有三个；装上 Extra Slots CPU 后再多 3、5 或 7 个）。你可以从快捷栏的“附加装置”选择器中启用它，或者通过你为它设置的快捷栏槽位启用。它们只在你当前驾驶的配置中生效：装在另一套配置里的，会等到你切换配置后才开始工作。

| 附加装置 | 效果 | 次数 | 价格 |
| :---- | :----------- | :--- | :---- |
| **Repair Drone I 至 IV** | 修复你的船体，每秒分别为最大值的 1.5%、2.25%、3.5% 和 5% | 无限 | 5,000 / 15,000 / 35,000 信用点，2,000 Thulium |
| **Cloaking CPU S** | 隐藏你的舰船 | 10 | 5,000 Thulium |
| **Cloaking CPU M** | 隐藏你的舰船 | 25 | 11,250 Thulium |
| **Cloaking CPU L** | 隐藏你的舰船 | 50 | 20,000 Thulium |
| **EMP Charge** | 3 秒内无人能将你选为目标，所有对你的锁定都会中断，你附近的所有隐形都会结束 | 1 | 500 Thulium |

Cloaking CPU 和 EMP Charge 只在商店出售。它们无法融合，也没有任何渠道会免费赠送。

新飞行员的**新手套装**已经在 Protos 的两个附加槽位里装好了两件附加装置：一个 **Base CPU I**（可用 10 次，传送到你所属企业的基地）和一个 **Repair Drone I**。想使用它们，请从快捷栏的“附加装置”选择器把它们拖到一个槽位上。只有新飞行员才会拿到这套装备：在 0.4.10 之前开始游戏的飞行员没有它。

另有七种 CPU 不出售：在 Skylab 的研究中心研究完成后，装配站就能制造它们（见[研究](/wiki/03-Mechanics/Research.md)）。它们是 Extra Slots CPU I、II、III，Jump CPU，Base CPU I、II，以及 Auto-Repair CPU；各自的作用见[最后一节](#research-cpus)。和 Cloaking CPU 一样，Jump CPU 和 Base CPU 也是留给平静时刻用的：在你开火或被击中后的 10 秒内，这三者都无法启动。两种传送 CPU，也就是 Jump CPU 和 Base CPU，在你携带任务物品时同样无法使用（“携带任务物品时无法使用传送 CPU。”）：见[任务物品](/wiki/03-Mechanics/Quests.md#quest-items)。

每个附加装置在快捷栏的槽位上都有一个简短标签：Repair Drone 是 **REP**，Cloaking CPU 是 **CLK**，EMP Charge 是 **EMP**，Auto-Repair CPU、Base CPU 和 Jump CPU 依次是 **ARP**、**BSE** 和 **JMP**。Extra Slots CPU 没有槽位：它们安装在你的 Skylab 里。把鼠标指向槽位，可以看到现在按下它会发生什么，或者为什么按了也没用。

![The Extras picker of the hotbar: Cloaking, Base and Jump CPUs to drag onto a slot](../../img/wiki-img/shots/cpu-hotbar.jpg)
![The Repair Drone of an extra slot docked to its ship and its wingmen](../../img/wiki-img/shots/repair-drones-extra.jpg)

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## 物品树 {#item-tree}

装配站制造的东西要先有对应的科技；将指针悬停在物品上可看到研究所需的时间。科技树、燃料和加速见 [研究](/wiki/03-Mechanics/Research.md)。

```tree
Cloaking CPU S | extra, common | buy 5000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Repair Drone I | extra, common | buy 5000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone II | extra, common | buy 15000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone III | extra, common | buy 35000 Credits | /wiki/06-Items/Extras.md#repair-drones
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
EMP Charge | extra, uncommon | buy 500 Thulium | /wiki/06-Items/Extras.md#emp-charge
Cloaking CPU M | extra, uncommon | buy 11250 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 2 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Extras.md#base-cpus
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu
Repair Drone IV | extra, rare | buy 2000 Thulium | /wiki/06-Items/Extras.md#repair-drones
Cloaking CPU L | extra, rare | buy 20000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 6 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu

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

## EMP Charge

在战斗中按下 EMP 槽位。**3 秒**内无人能锁定你，而且**所有已锁定你的人都会立刻失去锁定**，无论他们身在何处：飞行员、外星人和企业飞行员皆然。锁定被打断的飞行员会收到提示“锁定丢失：目标使用了 EMP”。在这 3 秒内试图锁定你的人会被拒绝。

- **它不是无敌。** 它能阻止需要锁定的东西：激光、制导火箭，以及直射单体火箭的碰撞（它会从你身上穿过）。**范围爆炸**不需要锁定，所以只要你在爆炸范围内，它仍会伤到你；而黑洞根本不是射击。
- **你仍然可以行动。** 开火不会结束它。你可以隐形（只要隐形自身的规则允许），也可以使用其他附加装置。
- **它会结束你附近的隐形。** 脉冲触发时，你周围 **1,500 单位**内每一艘处于隐形的舰船都会立刻现形，其 CPU 开始 60 秒的充能，无论它属于哪个企业，包括你自己的企业；你自己[小队](/wiki/03-Mechanics/Groups.md)的舰船是例外：它们会保持隐形。该飞行员会收到提示“隐形中断：附近有 EMP 被发射。”，看到舰船和任何解除隐形时一样伴着涟漪重新出现，槽位开始充能。你自己处于隐形时无法使用 EMP。
- **它不会隐藏任何东西。** 所有人仍然能看到你，这 3 秒内你周围还会有一层噼啪作响的电弧外壳。
- 在安全区保护你期间、隐形期间，或距上一次使用不足 **30 秒**时，**无法使用**。其他任何地方都能使用，包括赛季最初几天（和平协议）：那时外星人仍会追猎你。
- 你在这 3 秒内击中的外星人，要等这 3 秒结束后才会转而攻击你。你的击杀归属和首击规则不变。
- **你会看到什么。** 一道扭曲空间的脉冲从飞行员身上向外扩散，范围与脉冲结束隐形的距离相同（1,500 单位），范围内的所有人都能看到；在这 3 秒内，一层噼啪作响的电弧外壳包裹着舰船，你自己的舰船周围有一个圆环，屏幕顶部也有一个标签，两者都在计时。所有选中你的人，其目标圈会伴着一声短促的电击声碎裂。EMP 槽位显示你拥有的 EMP Charge 数量，外壳存在期间亮起蓝色，充能期间变暗。
- **一个 EMP Charge，一次使用。** 如果你拥有更多，槽位会从你的物品栏补充。**30 秒**的充能时间不会保存：退出登录或通过传送门跃迁会将其清零，下一次脉冲会消耗一个 EMP Charge。

## 研究中心的 CPU {#research-cpus}

其中两个 CPU 和每条升级链的最后一阶一样，需要 Dark Matter Plate：**Extra Slots CPU III** 需要 3 块（另需 6 块 Orvium Reinforced Plate），**Base CPU II** 需要 3 块（另需 2 块 Orvium Reinforced Plate），所以请先研究 Dark Matter Plate（[Dark Matter 与 Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)）。

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
