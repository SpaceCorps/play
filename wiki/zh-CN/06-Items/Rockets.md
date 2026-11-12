<!-- wiki-i18n source: bd68fa87d7243d6f -->
<!-- wiki-i18n title: 火箭 -->
# 火箭 {#rockets}

火箭是激光之外的第二种武器：每隔几秒发射一枚，威力远超一轮激光齐射。十二种**普通火箭**分为四种类型、每种三个档次，共用**一个 3 秒装填计时器**，由飞船的火箭发射器决定。十二种**特殊火箭**不只是造成伤害，它们共用**自己的一个 5 秒计时器**，每种还要等待自己的计时器。只有四种普通火箭、Flares 和 Ricochet 可以用**信用点**购买；其他火箭都在装配站制造。[无人机编队](/wiki/03-Mechanics/Formations.md)可以提高火箭的伤害，也能让普通计时器变长或变短（见[无人机编队与火箭](#drone-formations-and-rockets)）。

## 一分钟了解 {#in-one-minute}

- **十二种普通火箭。** 四种类型（Lancet、Rivet、Ember、Scatter），每种三个档次。只出售第 I 档，500 信用点；第 II、III 档在装配站用下一档的 100 枚火箭制造。
- **每枚火箭发射时随机决定伤害。** 发射时，游戏会在这枚火箭的最低伤害和最高伤害之间选出一个数值（Lancet I 为 1,700 到 2,100）。你的舰船、激光、增幅器和增益都不会改变它，只有无人机编队和你的**火箭技术**（飞行员技能）会。外星人发射的火箭不会随机，它们造成固定数值的伤害（见[对付外星人](#against-the-aliens)）。
- **爆炸中心最强。** Ember 和 Scatter 火箭会爆裂，伤害圆环内的每一艘舰船：中心处是完整数值，边缘处是 66%（N.U.K.E. 的爆炸降到一半）。
- **两种计时器。** 普通火箭共用一个：任何一次发射后等 3 秒；有**火箭发射器 II 至 V** 时，则是间隔 0.15 秒连发 2 至 5 枚，然后等 5 秒（见[发射](#firing)）。特殊火箭共用另一个 5 秒计时器，任何发射器都不会改变它，每种还要等待自己的计时器，从 3 秒到 2 分钟不等（见[特殊火箭](#special-rockets)）。
- **十二种特殊火箭。** 它们能冻结、干扰、毒害或标记飞船，击碎护盾或锁定，治疗友军，跳向第二艘飞船，或在光标处开启一个小黑洞。N.U.K.E. 和 N.I.K.E. 是其中两种。
- **制导或直射。** 制导火箭（Lancet、Ember）需要你选中的目标。直射火箭（Rivet、Scatter）飞向你的光标。
- **还有几样东西像火箭一样携带。** **EMP Charge** 是消耗品：物品栏里的一个堆叠，从快捷栏使用，不占槽位（[EMP Charge](#emp-charge)）。两道 **Energetic Wall** 也是（[Energetic Wall](/wiki/06-Items/Extras.md#energetic-wall)）。

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## 物品树 {#item-tree}

装配站制造的东西要先有对应的科技；将指针悬停在物品上可看到研究所需的时间。科技树、燃料和加速见 [研究](/wiki/03-Mechanics/Research.md)。

```tree
Lancet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet II | rocket, rare | craft 50000 Credits, 200 Thulium, 120 s, x100 | research 1800 s, 1800 science | 100 Lancet I, 5 Ship Fragment, 10 Nyxite | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet II | rocket, rare | craft 50000 Credits, 200 Thulium, 120 s, x100 | research 1800 s, 1800 science | 100 Rivet I, 5 Ship Fragment, 10 Daraxium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember II | rocket, rare | craft 50000 Credits, 200 Thulium, 120 s, x100 | research 1800 s, 1800 science | 100 Ember I, 5 Ship Fragment, 10 Cataclysite | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter II | rocket, rare | craft 50000 Credits, 200 Thulium, 120 s, x100 | research 1800 s, 1800 science | 100 Scatter I, 5 Ship Fragment, 10 Quorvium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ricochet | rocket, rare | buy 4000 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Flares | rocket, rare | buy 25000 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet III | rocket, epic | craft 150000 Credits, 800 Thulium, 300 s, x100 | research 10800 s, 10800 science | 100 Lancet II, 15 Ship Fragment, 2 Reinforced Hull Plate, 20 Nyxite | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet III | rocket, epic | craft 150000 Credits, 800 Thulium, 300 s, x100 | research 10800 s, 10800 science | 100 Rivet II, 15 Ship Fragment, 2 Reinforced Hull Plate, 20 Daraxium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember III | rocket, epic | craft 150000 Credits, 800 Thulium, 300 s, x100 | research 10800 s, 10800 science | 100 Ember II, 15 Ship Fragment, 2 Reinforced Hull Plate, 20 Cataclysite | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter III | rocket, epic | craft 150000 Credits, 800 Thulium, 300 s, x100 | research 10800 s, 10800 science | 100 Scatter II, 15 Ship Fragment, 2 Reinforced Hull Plate, 20 Quorvium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Freeze Rocket | rocket, epic | craft 50000 Credits, 1000 Thulium, 300 s, x5 | research 14400 s, 14400 science | 10 Ship Fragment, 1 Power Core, 30 Cataclysite | /wiki/06-Items/Rockets.md#the-twelve-rockets
EMP Rocket | rocket, epic | craft 60000 Credits, 1200 Thulium, 300 s, x5 | research 14400 s, 14400 science | 10 Ship Fragment, 2 Power Core, 20 Quorvium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Shield Breaker | rocket, epic | craft 80000 Credits, 1500 Thulium, 300 s, x5 | research 21600 s, 21600 science | 15 Ship Fragment, 3 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-twelve-rockets
Toxic Rocket | rocket, epic | craft 60000 Credits, 1000 Thulium, 300 s, x5 | research 14400 s, 14400 science | 10 Ship Fragment, 30 Nyxite, 10 Quorvium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Marking Rocket | rocket, epic | craft 50000 Credits, 800 Thulium, 300 s, x5 | research 14400 s, 14400 science | 10 Ship Fragment, 30 Daraxium, 10 Nyxite | /wiki/06-Items/Rockets.md#the-twelve-rockets
Support Rocket | rocket, epic | craft 90000 Credits, 2000 Thulium, 600 s, x3 | research 21600 s, 21600 science | 20 Ship Fragment, 2 Power Core, 40 Nyxite, 20 Quorvium | /wiki/06-Items/Rockets.md#the-twelve-rockets
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
Gravitational N.U.K.E. | rocket, mythical | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 1 N.U.K.E., 4 Power Core, 2 Ancient Control Unit, 40 Quorvium | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
Cooldown Rocket | rocket, legendary | craft 100000 Credits, 2500 Thulium, 600 s, x3 | research 28800 s, 28800 science | 20 Ship Fragment, 3 Power Core, 1 Ancient Control Unit, 40 Quorvium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Mine I | consumable, uncommon | buy 100 Thulium | /wiki/06-Items/Extras.md#mine
EMP Charge | consumable, uncommon | buy 500 Thulium | /wiki/06-Items/Rockets.md#emp-charge
Energetic Wall I | consumable, uncommon | buy 10000 Credits | /wiki/06-Items/Extras.md#energetic-wall
Energetic Wall II | consumable, rare | craft 600 Thulium, 120 s | research 21600 s, 21600 science | 5 Ship Fragment, 1 Power Core | /wiki/06-Items/Extras.md#energetic-wall
Mine II | consumable, rare | craft 200 Thulium, 120 s | research 10800 s, 10800 science | 2 Mine I, 3 Ship Fragment, 1 Power Core | /wiki/06-Items/Extras.md#mine
Mine III | consumable, epic | craft 400 Thulium, 300 s | research 21600 s, 21600 science | 2 Mine II, 8 Ship Fragment, 1 Reinforced Hull Plate, 2 Power Core | /wiki/06-Items/Extras.md#mine

Lancet I => Lancet II => Lancet III
Rivet I => Rivet II => Rivet III
Ember I => Ember II => Ember III
Scatter I => Scatter II => Scatter III => N.U.K.E. => Gravitational N.U.K.E.
Mine I => Mine II => Mine III
Energetic Wall I -> Energetic Wall II
```
<!-- item-tree:end -->

## 四种类型 {#the-four-kinds}

| | 单体：只命中一艘舰船 | 范围爆炸：爆裂，伤害附近的一切 |
| :--- | :--- | :--- |
| **制导**：锁定你选中的目标并紧追不放 | Lancet I、Lancet II、Lancet III | Ember I、Ember II、Ember III |
| **直射**：飞向你的光标 | Rivet I、Rivet II、Rivet III | Scatter I、Scatter II、Scatter III |

每种类型是一个以其普通火箭命名的**系列**，档次用罗马数字表示：**Lancet I**、**Lancet II** 和 **Lancet III** 分别是普通、稀有和史诗的制导单体火箭，Rivet、Ember 和 Scatter 系列也是如此。火箭在选择器和机库中的图块上的代码，是其系列的三个字母加上数字（LNC II、RVT III、EMB I、SCT II）；只能在装配站制造的两种火箭保留各自的名称和代码（N.U.K.E.，NUK；N.I.K.E.，NIK）。

- **制导**火箭在离开时，需要有一个位于其**锁定范围**内的已选中目标。它们以有限的转向速率追踪目标，所以远处的快速舰船可以甩开一枚廉价火箭。如果目标死亡、离开或进入安全区，火箭会继续直线飞行，不会另选目标。
- **直射**火箭不需要目标，并且会忽略你已选中的目标：它们总是飞向你的**光标**，即飞行视图中光标下方的那个点。**点击直射火箭的槽位使其待发**（槽位会出现白色边框和准星，你的鼠标光标在太空中会变成准星），然后**在太空中点击**：火箭飞向你点击的那个点，而你的舰船留在原地。按 Esc、点击右键或再次点击同一个槽位可以放弃。如果火箭还在装填，点击只会提示你这一点，火箭仍保持待发状态。数字键和**发射火箭**会立即朝光标在飞行视图中最后停留过的那个点发射；如果光标还没有到过飞行视图，火箭就朝你舰船的**朝向**飞行。它们笔直飞行，所以高速横穿的舰船可以侧身躲开。
- **单体**火箭会命中它所能命中的第一艘舰船（制导火箭只命中它的目标）。**范围爆炸**火箭会在遇到的第一艘舰船旁、你瞄准的点上，或飞行结束的位置爆裂，并伤害其**爆炸半径**内的每一艘舰船：中心处是全额伤害，边缘处是 66%（N.U.K.E. 为一半）。爆炸在地图上画出的圆环就是它的精确作用范围。
- **小行星。** 朝[小行星](/wiki/03-Mechanics/Asteroid-Mining.md)发射的制导火箭会飞向那颗小行星；直射火箭和对付任何目标时一样飞向光标，光标落在小行星上时会击碎它。任何火箭路上的第一颗小行星都会拦住它，代替后面的飞船承受命中（见[掩体](/wiki/03-Mechanics/Asteroid-Mining.md#cover)）。[Energetic Wall](/wiki/06-Items/Extras.md#energetic-wall) 也会同样拦住火箭；N.I.K.E. 会从它上方飞过。商店的十二种火箭和 N.U.K.E. 都能击碎小行星；N.I.K.E. 不能朝小行星发射，而是从它们上方飞过。激光同样能伤害小行星，但只有对飞船伤害的 5%：击碎小行星要靠火箭。

## 十二种火箭 {#the-twelve-rockets}

每枚火箭都有**自己的伤害，在发射时随机决定**：在它的最低数值和最高数值之间的任意位置，表格里列出了最低值、最高值和平均值。它与你的舰船、你的激光及其增幅器、你的增益、你的弹药或你的无人机都无关，火箭也永远不会暴击。只有**无人机编队**和**火箭技术**能改变它，这里的表格给出的是没有编队、也未计入火箭技术时的伤害（见[无人机编队与火箭](#drone-formations-and-rockets)和[火箭技术](#rocket-tech)）。单体火箭对它命中的舰船造成这次掷出的伤害；爆炸只掷一次，并对**范围内的每一艘舰船**造成同样的伤害，中心处是完整数值，边缘处是 66%（N.U.K.E. 为一半）。*护盾穿透*会在这次命中中，从目标的吸收率里扣除（舰船的吸收率是它的护盾承受每次攻击的份额，见[护盾机制](/wiki/03-Mechanics/Shields.md#shield-penetration)）：Lancet III 的 35% 会让一艘吸收率 80% 的舰船，其护盾只承受 45% 的伤害，其余 55% 落在船体上。爆炸没有护盾穿透。

| 名称 | 类型 | 稀有度 | 伤害 | 平均 | 护盾穿透 | 爆炸半径 | 锁定范围 | 射程 | 速度 | 价格 | 最多携带 |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **Lancet I** | 制导 · 单体 | 普通 | 3,500–4,200 | 3,850 | 25% | – | 1,000 | 1,584 | 660 | 500 信用点 | 5,000 |
| **Lancet II** | 制导 · 单体 | 稀有 | 5,200–6,200 | 5,700 | 35% | – | 1,300 | 2,296 | 820 | 用 100 枚 Lancet I 制造 | 2,000 |
| **Lancet III** | 制导 · 单体 | 史诗 | 7,300–8,700 | 8,000 | 35% | – | 1,300 | 2,296 | 820 | 用 100 枚 Lancet II 制造 | 500 |
| **Rivet I** | 直射 · 单体 | 普通 | 4,500–5,250 | 4,875 | 25% | – | – | 1,120 | 700 | 500 信用点 | 5,000 |
| **Rivet II** | 直射 · 单体 | 稀有 | 7,000–8,000 | 7,500 | 35% | – | – | 1,100 | 500 | 用 100 枚 Rivet I 制造 | 2,000 |
| **Rivet III** | 直射 · 单体 | 史诗 | 9,800–11,200 | 10,500 | 35% | – | – | 1,100 | 500 | 用 100 枚 Rivet II 制造 | 500 |
| **Ember I** | 制导 · 范围爆炸 | 普通 | 2,400–2,900 | 2,650 | – | 345 | 920 | 1,500 | 600 | 500 信用点 | 5,000 |
| **Ember II** | 制导 · 范围爆炸 | 稀有 | 3,500–4,500 | 4,000 | – | 450 | 1,150 | 2,030 | 700 | 用 100 枚 Ember I 制造 | 2,000 |
| **Ember III** | 制导 · 范围爆炸 | 史诗 | 4,900–6,300 | 5,600 | – | 495 | 1,150 | 2,030 | 700 | 用 100 枚 Ember II 制造 | 500 |
| **Scatter I** | 直射 · 范围爆炸 | 普通 | 3,000–3,500 | 3,250 | – | 435 | – | 1,080 | 540 | 500 信用点 | 5,000 |
| **Scatter II** | 直射 · 范围爆炸 | 稀有 | 4,500–5,500 | 5,000 | – | 600 | – | 1,092 | 420 | 用 100 枚 Scatter I 制造 | 2,000 |
| **Scatter III** | 直射 · 范围爆炸 | 史诗 | 6,300–7,700 | 7,000 | – | 660 | – | 1,092 | 420 | 用 100 枚 Scatter II 制造 | 500 |

档次越贵，火箭的威力越大，射得越远，护盾穿透越高，能携带的数量也越少；贵的火箭按其价格计算，提供的伤害也最多。同样的价格下，直射火箭比同档次、同类型的制导火箭平均多造成 23% 到 32% 的伤害（大约四分之一到三分之一），因为你得自己瞄准。范围爆炸火箭的伤害约为同档次、同系列单体火箭的三分之二（平均 66% 到 70%：Ember 对比 Lancet，Scatter 对比 Rivet），但会作用于它覆盖的每一艘舰船。爆炸的伤害在中心处是满额，并沿直线下降，到**边缘处是 66%**（N.U.K.E. 为一半）：船体位于中心与边缘正中的舰船承受 83%，船体在圆环之外的舰船则不承受任何伤害。一次发射平均造成其范围的中间值，即最高数值的 89% 到 94%，下文统计火箭数量的表格用的就是这个平均值。

## 火箭的花费 {#what-they-cost}

普通（第 I 档）火箭在商店里每枚 500 信用点，各类型都一样。稀有（第 II 档）和史诗（第 III 档）火箭不出售：由装配站用下一档的 100 枚火箭制造，每次 100 枚（一批稀有火箭另需 50,000 信用点和 200 Thulium，一批史诗火箭另需 150,000 信用点和 800 Thulium，外加少量材料；其余信息由商店和装配站告诉你）。按每个计时器都发射，一枚普通火箭相当于每分钟 10,000 信用点，而 Ostirion 的三门激光在 x1 弹药下每分钟只消耗 900 信用点。一整叠是 5,000 枚普通火箭（2,500,000 信用点）、2,000 枚稀有火箭或 500 枚史诗火箭： 在此之内你想买多少就买多少，火箭的*最多携带*数量是你能持有数量的唯一限制。重置时，十二种火箭每种最多 1,000 枚无需任何操作就会保留；超出的部分，以及每一枚 N.U.K.E. 和 N.I.K.E.，只有放进运输储藏库才能保留，库中一枚火箭重 1 kg（N.U.K.E. 或 N.I.K.E. 为 250 kg）：见[重置](/wiki/03-Mechanics/Wipe-Timeline.md#ammo-and-rockets)。每 3 秒一枚，一分钟只有二十枚，所以火箭是叠加在激光之上的爆发手段：便宜的用来对付弱小的外星人，贵的留给大战。你在[拍卖行](/wiki/03-Mechanics/Auction.md#limits)挂出的火箭，以及你领先的拍品中的火箭，在你购买或出价时也计入这个上限。 这些是基础数值：飞行员研究 Sealed Backdoor（[研究](/wiki/03-Mechanics/Research.md#pilot-technologies)）会为你提高每种火箭的携带上限，合计提高 25%、50%、100%、150% 或 200%（向下取整），所以 5,000 在 I 级变成 6,250，在 V 级变成 15,000。

商店出售四种普通火箭，按类型逐一列出，之后是 Flares 和 Ricochet；机库、运输储藏库和火箭选择器以同样的方式列出十二种普通火箭，每种类型列在自己的名字下，普通的在前、史诗的在后，之后是特殊火箭。

## 对付外星人 {#against-the-aliens}

击杀一个外星人所需的火箭数量，每次只用一种火箭，每枚火箭都按其范围的平均值计算（Alpha 世界的数值；Beta 和 Gamma 的外星人分别强 1.5 倍和 2 倍）。爆炸按它在其旁边爆裂的那艘舰船所承受的伤害计算，比中心处略少一点（中心伤害的 95% 到 97%）。外星人的护盾承受一次命中的 80%，再减去火箭的护盾穿透。掷出最低值时，击杀所需的火箭最多比表中多 15%（对 Goombah，Lancet I 需要 48 枚而不是 43 枚），掷出最高值时最多少 13%（39 枚）。Rivet II、Lancet III 和 Rivet III 无论怎么掷都能一击杀死一架 Phantasm；Rivet I 在掷出 2,600 或更高时需要两击，低于这个值需要三击。

| 击杀所需火箭数 | Seeker（1,600） | Phantasm（5,200） | Bulwark（26,000） | Goombah（80,000） | Crystalys（416,000） |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Lancet I** | 1 | 2 | 7 | 19 | 109 |
| **Lancet II** | 1 | 1 | 5 | 11 | 73 |
| **Lancet III** | 1 | 1 | 4 | 8 | 52 |
| **Rivet I** | 1 | 1 | 6 | 15 | 86 |
| **Rivet II** | 1 | 1 | 4 | 8 | 56 |
| **Rivet III** | 1 | 1 | 3 | 6 | 40 |
| **Ember I** | 1 | 3 | 11 | 32 | 166 |
| **Ember II** | 1 | 2 | 7 | 21 | 109 |
| **Ember III** | 1 | 1 | 5 | 15 | 78 |
| **Scatter I** | 1 | 2 | 9 | 26 | 134 |
| **Scatter II** | 1 | 2 | 6 | 17 | 87 |
| **Scatter III** | 1 | 1 | 4 | 12 | 62 |

- **普通**单体火箭无论怎么掷都是一击杀死一架 Seeker，三击杀死一架 Phantasm（Lancet I 掷出最低值时需要第四击）；它们是最初几个星区里的日常火箭。**稀有**火箭用来对付 Bulwark 和 Goombah：七枚 Lancet II 就能在大约 20 秒的计时内击杀一架 Bulwark。**史诗**单体火箭用八枚（Rivet III）到十一枚（Lancet III）杀死一架 Goombah。当多个外星人聚在一起时，范围爆炸火箭物有所值：一枚 Scatter III 在一群五架 Phantasm（都在你所瞄准目标的 250 单位内）上空爆裂，一次发射就能对整群共造成约 33,000 点伤害。
- 只靠火箭击杀是一笔实打实的开销，不是发财之道：普通单体火箭的花费是该击杀所得的 9%（Rivet I 打 Phantasm）到 47%（Lancet I 打 Crystalys）（信用点，以及按每个 Thulium 折合 200 信用点计的 Thulium），而用稀有范围爆炸火箭打最强的外星人，花费比击杀所得还多（Ember II 打 Crystalys：133%）。只用一种火箭击杀 **Crystalys** 需要 40 到 166 枚火箭，要两到八分钟的计时；一整堆 500 枚史诗火箭足够击杀其中的六到十二架。最强的外星人需要一个计划：你的激光用 x2 弹药，从第一秒起每 3 秒一枚中档火箭，再用下文的大型火箭作为爆发。
- 无论用什么方式击杀，奖励都是一样的（最大的奖励见 [Crystalys](/wiki/04-Aliens/Crystalys.md)），所以火箭击杀只有在节省时间、且花费低于奖励时才值得。
- **外星人也会发射火箭。** [虫群](/wiki/05-Swarms/Swarms.md)的 Pirate Boss、Dormant Force 和 Pulse，以及[战队](/wiki/03-Mechanics/Clans.md#clan-wardens)的 Siege Warden，会以各自的计时（虫群 5 秒，Siege Warden 8 到 24 秒，不受你的编队影响）向攻击它们的飞行员发射直线 Rivet 火箭。**外星人的火箭不会随机，也不使用上面的范围**：它造成固定的 2,500（Rivet I）、5,000（Rivet II）或 7,500（Rivet III）伤害，在外星人分别强 1.5 倍和 2 倍的 Beta 和 Gamma 里更高（Clan Warden 的火箭在每个世界都一样）。保持移动的舰船可以躲开。虫群的 Boss 也会在货箱中掉落火箭。

## 仅可制造的火箭 {#the-craft-only-rockets}

有两种火箭不在商店出售。**装配站**制造它们，它们遵循下文的所有规则（共用计时器、安全区、PvP 规则）。两者都是直射火箭：和所有直射火箭一样，飞向你光标下方的那个点（无论你选中了什么，游戏都会发送光标的方向；只有不发送方向的旧版 0.4.3 客户端，服务器才会让火箭飞向选中的目标，没有选中目标则飞向其光标下的点，再没有则朝舰船的朝向飞行）。它们的伤害在其最高数值的 **90% 到 100%** 之间随机决定，范围比那十二种更窄，所以下文说的一击摧毁，掷出最低值时同样成立。

| 名称 | 类型 | 稀有度 | 伤害 | 护盾穿透 | 爆炸半径 | 射程 | 速度 | 最多携带 | 制作材料 |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **N.U.K.E.** | 直射 · 范围爆炸 | 传说 | 45,000–50,000 | – | 1,350 | 1,200 | 300 | 10 | 每次制造 1 枚：150,000 信用点、3,000 Thulium、6 枚 Scatter III、4 个 Power Core、10 块 Reinforced Hull Plate、40 个 Ship Fragment、80 个 Cataclysite |
| **N.I.K.E.** | 直射 · 单体 | 神话 | 67,500–75,000 | 35% | – | 4,050 | 900 | 20 | 每次制造 5 枚：100,000 信用点、1,500 Thulium、20 个 Ship Fragment、4 块 Reinforced Hull Plate、40 个 Cataclysite |

- **N.U.K.E.**：游戏中最大的爆炸。爆炸半径 1,350 单位，是 Scatter III 的 600 单位的两倍多，面积是它的五倍：对其中的每艘舰船在中心处造成 45,000 到 50,000 点伤害，到边缘降至一半，即 22,500 到 25,000。它飞得很慢（在空中四秒）。一枚 N.U.K.E. 能消灭整个爆炸范围内的每一架 Seeker 和 Phantasm，以及爆点 1,210 单位内（掷出最高值时为 1,366）的一架 Bulwark，也就是几乎整个爆炸范围；它能削去一架 Goombah 一半以上的生命值和一架 Crystalys 九分之一的生命值。对付飞行员，它是最重的一击：见下文的规则。地图上的圆环就是它的精确作用范围。
- **N.I.K.E.**：和 Rivet I 一样的单体火箭，伤害 67,500 到 75,000，护盾穿透 35%：**它会命中接触到的第一艘舰船，并在其上耗尽。**它也是能产出 [Dark Matter](/wiki/03-Mechanics/Black-Hole.md) 的火箭：朝危险星区 4 中央的黑洞发射时，它在越过事件视界时被吞没，黑洞会回馈 Dark Matter。它在 4.5 秒内飞行 4,050 单位：从辐射区边缘到距中心 4,380 单位之间的任何位置发射都可以。从更远处发射，它会射程不足而被浪费。五枚 N.I.K.E. 大约产出十个 Dark Matter。
- **要注意的一点。** 如果一枚 N.I.K.E. 在途中遇到一艘舰船、一个守在弹道上的对手，或任何它可以伤害的东西，它就会对其造成 67,500 到 75,000 点伤害并消失：黑洞什么也得不到，你也一样。黑洞圆环之内没有别的东西会游荡，让它误中（外星人和企业飞行员都不会进入）：只有为了 Dark Matter 而进去的飞行员，或在边缘等着你的飞行员。它会从你自己的小队、安全区内的舰船，以及你暂时还不能伤害的舰船身上穿过；在 PvP 开启的地方，它会像击中其他舰船一样击中你自己企业的舰船。如果你在发射后离开了地图，它会继续飞行，不伤害任何人，仍然会为你产出 Dark Matter。
- 如果一次制造会让你持有的某种火箭超过其*最多携带*数量（算上你已排队的），装配站不会开始这次制造。 Sealed Backdoor 同样会提高它们的上限（I 级时 10 变成 12、20 变成 25，V 级时是 30 和 60）。

## 特殊火箭 {#special-rockets}

特殊火箭做的是伤害数字说不清的事。它们彼此共用**一个 5 秒计时器**（任何发射器都不会改变它），每种还要等待**自己的计时器**，从 3 秒到 2 分钟；普通火箭的计时器是分开的，所以普通火箭和特殊火箭可以一起发射。它们由装配站制造，只有 Flares 和 Ricochet 由商店出售（上面的物品树有所有配方）。上面的 N.U.K.E. 和 N.I.K.E. 也是特殊火箭，N.U.K.E. 没有自己的计时器。自动火箭 CPU 和火箭发射器只发射普通火箭。

| 名称 | 类型 | 效果 | 自有计时 | 最多携带 |
| :--- | :--- | :--- | :---: | :---: |
| **Freeze Rocket** | 制导 · 单体 | 不造成伤害的制导火箭：被击中的飞船会被冻结，四秒内飞行速度降低 60%。 | 30 秒 | 50 |
| **EMP Rocket** | 制导 · 单体 | 不造成伤害的制导火箭：被击中的飞船会承受三秒的 EMP 充能效果。 | 30 秒 | 50 |
| **Shield Breaker** | 直射 · 单体 | 专为护盾设计的高速非制导火箭：对护盾造成 25,000 点、对船体造成 5,000 点伤害，但只要还有护盾，就只击中护盾。 | 15 秒 | 50 |
| **Toxic Rocket** | 制导 · 单体 | 自身不造成伤害的制导火箭：被击中的飞船会中毒五秒，每秒损失有效生命值（船体与护盾合计）的百分之零点五，从船体扣除。 | 20 秒 | 50 |
| **Marking Rocket** | 制导 · 单体 | 不造成伤害的制导火箭：被击中的飞船会被标记五秒，受到的所有伤害增加 20%。 | 30 秒 | 50 |
| **Cooldown Rocket** | 制导 · 单体 | 不造成伤害的制导火箭：八秒内，被击中飞船的计时物品以一半的速度冷却。 | 60 秒 | 20 |
| **Gravitational N.U.K.E.** | 直射 · 范围爆炸 | 围绕坍缩核心重新制造的 N.U.K.E.。放置在光标处，开启一个持续十五秒的小型黑洞，吸引飞船和制导火箭。每张地图只能存在一个。只能在装配站制造，且永远不能在拍卖行出售。 | 120 秒 | 5 |
| **Support Rocket** | 制导 · 单体 | 不造成伤害的制导火箭：为被击中的那一艘友方飞船恢复恰好 100,000 点船体（不会超过上限），与飞船大小无关。友方指你的小队和你的企业，只能向友方发射。 | 120 秒 | 20 |
| **Flares** | 直射 · 单体 | 从自己的飞船发射：使所有锁定你的制导火箭失去锁定。 | 60 秒 | 20 |
| **Ricochet** | 直射 · 单体 | 命中如 Rivet II 的高速非制导火箭，首次命中后会以 75% 的伤害弹向第二艘飞船。 | 3 秒 | 500 |

- 同类的第二次命中会刷新冻结、干扰、中毒、标记或冷却减缓，而不会与第一次叠加。Toxic Rocket 的伤害算射手的，所以因中毒而被击毁也算他的击杀。
- 重力 N.U.K.E. **放置在光标处**：它飞向光标下的那一点，或飞到射程尽头，任何飞船的引信都不会引爆它。一张地图上只能存在一个引力井：第二次发射会被拒绝，且不消耗任何东西。引力井中央有一个黑洞在旋转，引力不仅拉走飞行中的飞船，也会拉走静止不动的飞船：停泊的飞船连同它的目的地一起被带到中心。
- **Support Rocket** 只修复友方：你小队或你企业的飞船，包括企业的飞行员。它恰好恢复 100,000 点船体（不会超过上限），不恢复护盾。不能对自己使用：未选中任何目标时，发射会像任何制导火箭一样被拒绝；选中敌人、外星人、小行星或你自己的飞船时，会以“不是友方”被拒绝；都不消耗任何东西。对船体已满的友方发射会被拒绝，且不消耗任何东西。修复不算命中：不会打断 Repair Drone。

## 发射 {#firing}

1. 在商店（**火箭**分类）用信用点购买普通火箭，每种买到*最多携带*数量；稀有和史诗火箭在装配站用下一档的 100 枚制造。
2. 打开快捷栏上方的**火箭**，把你想要的火箭拖到槽位上。选择器为每种类型显示一列、每个档次显示一行，并标出你携带的数量。它们下方是**特殊火箭**，每行四种（没有携带的仅制造火箭会标上一个小锤子）。
3. 按下槽位的按键。点击**制导**火箭的槽位会朝你选中的目标发射；点击**直射**火箭的槽位会使其待发，你接下来在太空中的点击会朝那里发射。**发射火箭**按键（默认为 `R`，可在“设置 › 操作”中重新绑定）会发射你上一次发射的火箭，或快捷栏上的第一枚。
4. 每个火箭槽位上都会扫过一个扇形倒计时，对应该火箭所等待的计时器，中间显示剩余秒数：普通火箭 3 秒（有火箭发射器时 5 秒），特殊火箭则取 5 秒和自己计时器中较长的一个。在此之前按下只会提示你火箭正在装填（最后十分之一秒内的按下仍会发射）。无人机编队可以把普通计时器变成 2.19 到 4.05 秒之间（见下文）。

把鼠标悬停在火箭槽位上可以看到它的数值（伤害是最低值到最高值；商店和机库显示的相同），并在游戏世界中看到它的锁定圈（选中的目标在范围内时为绿色），或它的弹道线和爆炸圈。锁定**你**的火箭会让你的屏幕边缘闪红。

**火箭发射器。** 火箭发射器 II 至 V 像自动火箭 CPU 一样存放在机库中，不占槽位，在任何飞船上都有效（以你拥有的最好的一个为准）。按一次普通火箭，就会从叠中以 0.15 秒的间隔发射 2、3、4 或 5 枚，之后普通火箭等待 5 秒。装配站在研究完成后制造它们（8 至 24 小时，需要 150,000 至 2,000,000 Thulium 和材料；[附加装置](/wiki/06-Items/Extras.md)的物品树列出了它们）。

**N.U.K.E.** 在你发射之前就会在地图上画出它的爆炸范围（瞄准点处半径 1,350 单位的圆），引爆时，视野中会闪过一道白光，一个圆环在大约一秒内扩张到精确的作用范围并再停留两秒，一团蘑菇状升起的烟云，以及一阵镜头震动，离得越近震动越强。**减弱屏幕震动**会去掉震动，**减弱动态效果**会把闪光缩短到三分之一秒、亮度不到一半（两者都在“设置 › 图形”中）；较低的粒子质量会让烟云变稀疏并去掉火花，但绝不会去掉闪光和圆环。**N.I.K.E.** 的瞄准方式与 Rivet I 相同，沿着从你舰船到光标的连线；游戏绝不会因为距离黑洞太远或所在地图没有黑洞而拒绝发射：它飞向哪里，由你自己判断。它的卡片在伤害旁写着**黑洞：产出 Dark Matter**。它会拖出一道紫色的尾迹，火花环绕其间；它遇到的舰船会像被任何火箭击中一样受到打击，而当它越过视界时，黑洞会闪耀一下。

## 无人机编队与火箭 {#drone-formations-and-rockets}

正在使用的[无人机编队](/wiki/03-Mechanics/Formations.md)是你的舰船上唯一能改变火箭的东西，另一样是你自己的[火箭技术](#rocket-tech)。本页所有伤害数字都是没有编队、也未计入火箭技术的舰船的数值。

- **伤害。** Ballista（+55%）、Bodkin（+29%）和 Asterism（+24%）的火箭加成会乘到全部 14 种火箭的伤害上，包括 N.U.K.E. 和 N.I.K.E.。Testudo 对所有伤害的代价同样作用于火箭，Culler 对外星人的伤害则作用于击中外星人的火箭。同一枚火箭上的所有系数加起来最高为 ×1.59。这个加成对[小行星](/wiki/03-Mechanics/Asteroid-Mining.md#breaking-one)和对飞船一样有效，小行星的装甲在它之后才扣除。
- **装填。** Asterism 让普通火箭的计时器变长 35%（4.05 秒），Cordon 变长 11%（3.33 秒），Redoubt 变短 27%（2.19 秒），但绝不会短于火箭的飞行时间再加一瞬。在 Redoubt 下，快速火箭（Lancet I、Rivet I 和 II、Ember I、Scatter I 和 II）等 2.19 秒，Rivet III 等 2.3 秒，Lancet III 等 2.9 秒，Ember III 则等满 3 秒。等待时间在发射时就已确定，所以之后更换编队不会缩短它，火箭槽位上的倒计时也随它变化。特殊火箭的计时器不受任何编队影响。
- **两枚大型火箭的上限只对编队而言依然成立。** 用最好的编队，N.I.K.E. 最高造成 116,250 的伤害，完好的 Paragon（128,000）能扛住；N.U.K.E. 最高 77,500，Goombah（80,000）能扛住。[火箭技术](#rocket-tech)没有上限，会同时提高两者：100 级、装备 Ballista 时，N.I.K.E. 最高造成 151,125 的伤害，超过完好的 Paragon 的 128,000；N.U.K.E. 在爆炸中心最高 100,750，无论掷出多少都足以摧毁一只 Goombah。
- **闪避。** Asterism 的 7% 闪避让击中你的直接命中火箭有 7% 的几率完全不造成伤害，你的飞船上方会浮现“未命中”；范围爆炸没有瞄准，永远不会被闪避。
- **穿透。** Gemini 把自己的 15 点、Stiletto 把自己的 35 点火箭穿透，加到直接命中火箭的护盾穿透上（爆炸没有穿透），没有上限：Lancet III 加上 Stiletto 是 70%，加上 Gemini 是 50%。激光命中也以同样的方式把 Gemini 的点数加到弹药和增幅器的穿透上，但得不到 Stiletto 的任何点数（[激光与弹药](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)）。

## 火箭技术 {#rocket-tech}

**火箭技术**是一项飞行员技能：你发射火箭并用它们击中舰船时它会升级，它的等级在每艘舰船上都属于你。它从两个方面改变你发射的每一枚火箭。

- **伤害。** 火箭在 1 级造成其伤害的 1.00 倍，随等级呈直线上升，到 100 级为 1.30 倍：游戏在发射时随机决定的数值会乘上它，所以命中、爆炸、小行星和 Energetic Wall 都会受到这个数值。编队的 ×1.59 上限只作用于编队的加成，因此这项技能没有任何上限：100 级配上 Ballista，火箭造成其数值的 2.015 倍，N.U.K.E. 在爆炸中心可达 100,750，比 Goombah 的 80,000 还多。
- **哑火。** 你向敌人发射的火箭可能哑火，概率在 1 级为 10%，随等级呈直线下降，到 100 级为 1%，不会降到零。哑火和任何发射一样会耗掉那枚火箭、那一次射击和等待时间，但它哪里也不会飞去：所有看得到你舰船的人都会看到炮口冒出几点微弱的火花和一团灰烟，听到的不是发射声，而是沉闷的一声“噗”和一声闷响；你会收到提示："你的火箭哑火了。" Support Rocket 和 Flares 从不哑火。

## 规则 {#rules}

- 发射火箭**不需要装备激光**，而且你的激光不会改变火箭造成的伤害，也不会改变它能飞多远：制导火箭会锁定其自身锁定范围内的目标，直射火箭飞出它自己的射程。没有装备激光时，机库的射程图块显示一条短横线，只有你的火箭能开火。
- 每次发射消耗一枚火箭，无论是否命中。
- 火箭遵循激光的规则：**安全区**内的任何东西都不会受伤，在**和平协议**结束之前或星区禁止 PvP 的地方，没有飞行员会受伤，而**你自己的小队永远不会被你的火箭伤到**，无论是直接命中还是爆炸。**你自己的企业不受保护**：在 PvP 开启的地方，火箭会像激光一样伤害同企业的飞行员（锁定、挡在路径上的直射火箭、爆炸），摧毁一名会损失 **100 荣誉**。Beta 和 Gamma 没有和平协议，PvP 从第 1 天起就开启。
- 发射火箭会立即结束你自己的安全区保护。它算作一次射击：也会结束你自己的**隐形**，随后 Cloaking CPU 充能一分钟，和任何一次隐形结束后一样。无论是否隐形，发射之后的 10 秒内你都无法隐形（见[附加装置](/wiki/06-Items/Extras.md)）。
- 处于**隐形**状态或 **EMP 的 3 秒**内的舰船无法被锁定：制导火箭会被拒绝发射，已经朝它飞去的火箭会失去锁定并继续笔直飞行。直射单体火箭会从这样的舰船身上穿过。**范围爆炸**不需要锁定，所以无论是否隐形，它都会伤害其覆盖的舰船，并结束隐形（见[附加装置](/wiki/06-Items/Extras.md)）。
- **火箭对飞行员造成的伤害没有任何上限。**另一名飞行员的舰船会承受全额伤害：先是护盾（按其吸收率减去火箭的护盾穿透），然后是船体。小型舰船撑不住。在原装护盾核心（Light，吸收率 45%）下，无论掷出多少，一枚 N.I.K.E. 一击就能摧毁一艘全新的 Protos 或 Kitefin。全新的 Ostirion（64,000 船体）在最低掷值时会损失约 95% 的船体，在掷值的上半区间才会被摧毁；若用 Heavy 护盾核心（吸收率 55%），一击损失 84% 到 94%，永远无法一击摧毁；护盾被打光时，则无论掷出多少都会被摧毁。Paragon 会损失 47% 到 53% 的船体，Wraith 损失 24% 到 26%。一枚 N.U.K.E. 能摧毁爆炸范围内任何位置的 Protos、爆点约 80 单位内（掷出最高值时为 340）的 Kitefin，一次爆炸摧毁不了更大的舰船。两枚 Lancet III 或两枚 Rivet III 无论掷出多少都能摧毁一艘 Protos；摧毁一艘 Wraith 需要其中的 36 到 55 枚。挡在飞行员与火箭之间的，是和平协议、安全区、禁止 PvP 的星区和你的小队。这些数字是没有编队、也未计入[火箭技术](#rocket-tech)的舰船的数值，火箭技术在 1 级时把它们乘以 1.00，100 级时乘以 1.30；火箭编队最多能把它们提高 55%（见[无人机编队与火箭](#drone-formations-and-rockets)）。
- 只有火箭的**直接命中**才能取得外星人的归属（见[战斗](/wiki/03-Mechanics/Combat.md)）；爆炸的边缘可以伤到已有归属的外星人，却不会抢走它。爆炸伤到的每个外星人，包括沉睡的，都会转而攻击你，就像被激光命中一样（只会还击的 Seeker 或 Goombah 也包括在内）；爆炸没波及的则继续沉睡。
- 计时器属于你本人：它在跃迁、重新连接、更换舰船和舰船被摧毁之后依然保留。

只有第一张表里的普通火箭、Flares 和 Ricochet 可以购买（用信用点）；其他火箭都在装配站制造。

另见：[激光与弹药](/wiki/06-Items/Lasers.md)、[战斗](/wiki/03-Mechanics/Combat.md)、[黑洞](/wiki/03-Mechanics/Black-Hole.md)。

## EMP Charge

**EMP Charge** 像火箭一样携带，但它不是火箭，而是**消耗品**。你在商店以每次充能 **500 Thulium** 购买，一个堆叠最多携带 **20** 个（你在[拍卖行](/wiki/03-Mechanics/Auction.md)挂出的也算在内），快捷栏的“消耗品”选择器会显示你携带的数量。它**不占用任何舰船的槽位**；0.4.21 之前它是[附加装置](/wiki/06-Items/Extras.md)，每个 EMP Charge 都占一个附加槽位。一个 EMP Charge 在运输储藏库中的重量是 250。

在战斗中按下 EMP 槽位。**3 秒**内无人能锁定你，而且**所有已锁定你的人都会立刻失去锁定**，无论他们身在何处：飞行员、外星人和企业飞行员皆然。锁定被打断的飞行员会收到提示“锁定丢失：目标使用了 EMP”。在这 3 秒内试图锁定你的人会被拒绝。

- **它不是无敌。** 它能阻止需要锁定的东西：激光、制导火箭，以及直射单体火箭的碰撞（它会从你身上穿过）。**范围爆炸**不需要锁定，所以只要你在爆炸范围内，它仍会伤到你；而黑洞根本不是射击。
- **你仍然可以行动。** 开火不会结束它。你可以隐形（只要隐形自身的规则允许），也可以使用其他附加装置。
- **它会结束你附近的隐形。** 脉冲触发时，你周围 **1,500 单位**内每一艘处于隐形的舰船都会立刻现形，其 CPU 开始 60 秒的充能，无论它属于哪个企业，包括你自己的企业；你自己[小队](/wiki/03-Mechanics/Groups.md)的舰船是例外：它们会保持隐形。该飞行员会收到提示“隐形中断：附近有 EMP 被发射。”，看到舰船和任何解除隐形时一样伴着涟漪重新出现，槽位开始充能。你自己处于隐形时无法使用 EMP。
- **它不会隐藏任何东西。** 所有人仍然能看到你，这 3 秒内你周围还会有一层噼啪作响的电弧外壳。
- 在安全区保护你期间、隐形期间，或距上一次使用不足 **30 秒**时，**无法使用**。其他任何地方都能使用，包括赛季最初几天（和平协议）：那时外星人仍会追猎你。
- 你在这 3 秒内击中的外星人，要等这 3 秒结束后才会转而攻击你。你的击杀归属和首击规则不变。
- **你会看到什么。** 一道扭曲空间的脉冲从飞行员身上向外扩散，范围与脉冲结束隐形的距离相同（1,500 单位），范围内的所有人都能看到；在这 3 秒内，一层噼啪作响的电弧外壳包裹着舰船，你自己的舰船周围有一个圆环，屏幕顶部也有一个标签，两者都在计时。所有选中你的人，其目标圈会伴着一声短促的电击声碎裂。EMP 槽位显示你拥有的 EMP Charge 数量，外壳存在期间亮起蓝色，充能期间变暗。
- **按一次，用一个 EMP Charge。** 按一次会从你的堆叠中消耗一个 EMP Charge；一个也没有时会被拒绝（“没有剩余的 EMP Charge。”）。运输储藏库中的 EMP Charge 属于下一个赛季，无法使用。与每种有 1,000 枚会自动保留的十二种火箭不同，你携带的 EMP Charge 会随赛季一起丢失，除非你把它们放进运输储藏库。**30 秒**的充能时间不会保存：退出登录或通过传送门跃迁会将其清零，下一次脉冲会消耗一个 EMP Charge。
