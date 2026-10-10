<!-- wiki-i18n source: 7a131032ce9f07fb -->
<!-- wiki-i18n title: 护盾 -->
# 护盾与防御 {#shields-defense}

防御模块提供护盾容量、吸收伤害，并为你的防御系统充能。

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## 物品树 {#item-tree}

装配站制造的东西要先有对应的科技；将指针悬停在物品上可看到研究所需的时间。科技树、燃料和加速见 [研究](/wiki/03-Mechanics/Research.md)。

```tree
Light Shield Core | shield, shoddy | buy 20000 Credits | /wiki/06-Items/Shields.md#shield-cores
Basic Shield Core | shield, common | buy 2000 Thulium | /wiki/06-Items/Shields.md#shield-cores
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cores
Adaptive Core I | hybrid-generator, shoddy | buy 100000 Credits | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core II | hybrid-generator, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Adaptive Core I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core III | hybrid-generator, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Adaptive Core II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Absorption Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells

Light Shield Core -> Basic Shield Core => Heavy Shield Core
Adaptive Core I => Adaptive Core II => Adaptive Core III
Absorption Shield Cell I => Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell I => Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```
<!-- item-tree:end -->

## 护盾核心 {#shield-cores}

装备护盾核心来生成主动防御屏障，可装在你舰船的发生器槽位中，也可装在你的[无人机](/wiki/03-Mechanics/Drones.md)上（无人机的槽位按核心槽位计算）。请注意，重型护盾会拖慢你的速度。装在**技能槽位**中的护盾核心则会给你“特殊效果”列中的 **Shield Surge**，即在十秒内修复护盾，且自身不提供任何护盾（见[技能](/wiki/03-Mechanics/Abilities.md)）。

| 名称 | 稀有度 | 容量 | 充能速率 | 吸收率 | 护盾加成 % | 速度加成 % | 电池槽位 | 特殊效果 | 费用 |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Light Shield Core** | 劣质 | 10,000 | 333/秒 | 45% | +5% | -1% | 1 | Shield Surge I | 20,000 信用点 |
| **Basic Shield Core** | 普通 | 15,000 | 500/秒 | 48% | +10% | -3% | 2 | Shield Surge II | 2,000 Thulium |
| **Heavy Shield Core** | 稀有 | 25,000 | 833/秒 | 50% | +20% | -5% | 3 | Shield Surge III | 仅可制造 |

**Heavy Shield Core** 在[装配站](/wiki/06-Items/Overview.md#upgrading-modules)中由一个 Basic Shield Core 制成，另需 2,000 Thulium、20 个 Cataclysite、8 块 Reinforced Hull Plate 和 3 块 Dark Matter Plate（[Dark Matter 与 Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)）。它沿用被消耗核心的附魔等级，其加成会重新随机（[模块升级](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)）。请先把 Basic Shield Core 从你的舰船上取下（并把其中的电池取出）：已装备或装有电池的核心不会被消耗。

**吸收率**是你的护盾承受每次攻击的份额，其余由船体承受。单靠护盾本身是 **45% 到 50%**，其余由它的电池补上：最强的护盾配最强的电池（一个 Heavy Shield Core 加三个 Absorption Shield Cell IV）是 **80%**，这是一艘舰船开箱即有的最高值。有两项永久提升可以在此基础上叠加：赛季商店的 Shield Absorbance Boost（每级 +0.1 点，共 100 级，每级 25 重置点数）和锻造炉的吸收率加成。目前的重置点数来源（达到各自上限时共 855 点，重置后保留；还计划增加更多来源）可以买下这 100 级中的 34 级（+3.4 点），配上完全锻造的永恒套装，约为 **95%**。不过这项属性并不以 100% 为上限：攻击方的*护盾穿透*会从中扣除，所以一艘舰船超出 100% 的部分，就是它抵御穿透的余量。见[护盾机制](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-)。

---

## 混合发生器（自适应核心） {#hybrid-generators-adaptive-cores-}

自适应核心是混合发生器，兼具护盾和速度能力。它们的槽位既能装推进器，也能装护盾电池（每个槽位一个模块，两种皆可）。它们的护盾加成和速度加成的计算方式与护盾或引擎相同（取最好的四个，再乘以槽位的效能比例）。它们没有吸收率：不会改变你舰船的吸收率，其中的电池只增加容量和充能。只有护盾会分担攻击，所以自适应核心中的电池还需要舰船上装有护盾。

| 名称 | 稀有度 | 护盾加成 % | 速度加成 % | 槽位 | 特殊效果 | 费用 |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **Adaptive Core I** | 劣质 | +4% | +2.4% | 1 | — | 100,000 信用点 |
| **Adaptive Core II** | 普通 | +6.4% | +3.2% | 2 | — | 仅可制造 |
| **Adaptive Core III** | 稀有 | +8% | +4% | 3 | — | 仅可制造 |

**Adaptive Core II** 在[装配站](/wiki/06-Items/Overview.md#upgrading-modules)中由一个 Adaptive Core I 制成，另需 1,000 Thulium、10 个 Ship Fragment、1 个 Power Core 和 2 块 Velkonite Reinforced Plate。**Adaptive Core III** 在装配站中由一个 Adaptive Core II 制成，另需 2,000 Thulium、60 个 Ship Fragment、3 个 Power Core 和 3 块 Dark Matter Plate（[Dark Matter 与 Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)）。两者都沿用被消耗核心的附魔等级，其加成会重新随机（[模块升级](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)）。请先把要消耗的核心从你的舰船上取下（并把其中的推进器和电池取出）：已装备或带有模块的核心不会被消耗。

---

## 护盾电池 {#shield-cells}

护盾电池安装在护盾核心或自适应核心内部（数量等于核心的槽位数），用来强化该核心。在护盾核心中，它们还会以点数提升其吸收率，从而提高你的护盾承受每次攻击的份额。电池分为两个系列，每个系列有四阶：**Capacity Shield Cell** 提供最多的护盾和充能，**Absorption Shield Cell** 提供最多的吸收率（每一阶都是同阶 Capacity 的两倍吸收率、一半护盾和充能）。Capacity 适合护盾决定胜负的舰船，Absorption 适合船体决定胜负的舰船。当一个核心的所有槽位都装满同一种电池时：Light Shield Core（1 个槽位）是 47% 到 55%，Basic Shield Core（2 个槽位）是 52% 到 68%，Heavy Shield Core（3 个槽位）是 56% 到 80%，范围从 I 阶 Capacity 电池到 IV 阶 Absorption 电池。卸下核心，或把它作为[锻造炉](/wiki/06-Items/Forge.md)合并的素材消耗掉，其中的电池会回到物品栏。

| 名称 | 稀有度 | 容量提升 | 充能提升 | 吸收率提升 | 费用 |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Capacity Shield Cell I** | 劣质 | +3,000 | +250/秒 | +2% | 30,000 信用点 |
| **Capacity Shield Cell II** | 普通 | +6,000 | +500/秒 | +3% | 仅可制造 |
| **Capacity Shield Cell III** | 稀有 | +9,000 | +750/秒 | +4% | 仅可制造 |
| **Capacity Shield Cell IV** | 史诗 | +12,000 | +1,000/秒 | +5% | 仅可制造 |
| **Absorption Shield Cell I** | 劣质 | +1,500 | +125/秒 | +4% | 30,000 信用点 |
| **Absorption Shield Cell II** | 普通 | +3,000 | +250/秒 | +6% | 仅可制造 |
| **Absorption Shield Cell III** | 稀有 | +4,500 | +375/秒 | +8% | 仅可制造 |
| **Absorption Shield Cell IV** | 史诗 | +6,000 | +500/秒 | +10% | 仅可制造 |

每个系列的 I 阶以 30,000 信用点出售。II 至 IV 阶在[装配站](/wiki/06-Items/Overview.md#upgrading-modules)中制成，每一阶都由同系列低一阶的电池升级而来（Capacity Shield Cell II 由一个 Capacity Shield Cell I 制成，III 由 II，IV 由 III），另需 Thulium、掉落物和板：II 阶或 III 阶需要来自你 Skylab 的 2 块或 4 块 Velkonite Reinforced Plate，IV 阶需要 3 块 Dark Matter Plate。电池不会更换系列：Capacity 还是 Absorption，在购买 I 阶时选择。新电池沿用被消耗电池的附魔等级，其加成会重新随机（[模块升级](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)）。电池不能装进[技能槽位](/wiki/03-Mechanics/Abilities.md)；它们属于护盾和自适应核心的内部。
