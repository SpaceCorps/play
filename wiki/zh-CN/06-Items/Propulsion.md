<!-- wiki-i18n source: 201734b1f19e2346 -->
<!-- wiki-i18n title: 推进 -->
# 推进与速度 {#propulsion-speed}

推进系统决定你舰船的移动速度和机动性。

## 一分钟了解 {#in-one-minute}

- **引擎产生速度，推进器装在引擎里为它增加速度。** 一台引擎可装一到三个推进器（Engine I 一个，Engine II 两个，Engine III 三个），自适应核心也一样（它的等级决定数量）。
- **两个系列，每个四阶。** Impulse Thruster 提供最多的固定速度，Momentum Thruster 提供的固定速度较少，但对速度的倍率更大。两个系列中，每一阶在两项数值上都比下一阶更高。
- **哪个装哪里。** 一般来说，Momentum 适合装满三个推进器的 Engine III，其余各处都适合 Impulse：数字见[下面的表格](#which-thruster-where)。最快的 Engine III 把两者混装：一个 Impulse Thruster IV 加两个 Momentum Thruster IV，速度为 62.1。
- **如何获得。** 每个系列的 I 阶售价 20,000 信用点。II 到 IV 阶在装配站制造，每一阶用低一阶的推进器制成，推进器永远不会更换系列。

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## 物品树 {#item-tree}

装配站制造的东西要先有对应的科技；将指针悬停在物品上可看到研究所需的时间。科技树、燃料和加速见 [研究](/wiki/03-Mechanics/Research.md)。

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | buy 2000 Thulium | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I -> Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## 引擎 {#engines}

引擎是你舰船推力的主要来源。装在**技能槽位**中的引擎则会给你“特殊效果”列中的 **Afterburner**，它能在十秒内提供一阵爆发的速度（引擎越多持续越久），且自身不提供任何推力（见[技能](/wiki/03-Mechanics/Abilities.md)）。

| 名称 | 稀有度 | 基础速度 | 速度加成 % | 护盾加成 % | 槽位 | 特殊效果 | 费用 |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | 劣质 | +2 | +2% | -2% | 1 | Afterburner I | 20,000 信用点 |
| **Engine II** | 普通 | +4 | +4% | -8% | 2 | Afterburner II | 2,000 Thulium |
| **Engine III** | 稀有 | +6 | +5% | -15% | 3 | Afterburner III | 仅可制造 |

**Engine III** 在[装配站](/wiki/06-Items/Overview.md#upgrading-modules)中由一个 Engine II 制成，另需 2,000 Thulium、60 个 Ship Fragment、3 个 Power Core 和 3 块 Dark Matter Plate（[Dark Matter 与 Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)）。它沿用被消耗引擎的附魔等级，其加成会重新随机（[模块升级](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)）。请先把 Engine II 从你的舰船上取下（并把其中的推进器取出）：已装备或带有推进器的引擎不会被消耗。

引擎的护盾加成存在于物品数据中，但游戏从未应用过它：引擎不会削弱你的护盾，物品卡片也不显示它。

---

## 推进器 {#thrusters}

推进器嵌入在引擎或自适应核心中，以提升它们的速度输出。推进器分为两个系列，每个系列有四阶：**Impulse Thruster** 提供最多的固定速度，并以较小的倍率略微提升所装引擎的速度，**Momentum Thruster** 提供的固定速度较少，但倍率更大。两个系列中，每一阶的固定速度和倍率都比低一阶更高。装有推进器的引擎（或自适应核心）产生的速度是**它自身的基础速度加上推进器的固定速度提升，再把整体乘上所有推进器的速度倍率之积**（[速度如何计算](/wiki/03-Mechanics/Speed.md)）：装有三个 Momentum Thruster IV 的 Engine III 产生 (6 + 3 x 13.1) x 1.11 x 1.11 x 1.11 = 62.0，装有三个 Impulse Thruster IV 的产生 (6 + 3 x 16.5) x 1.035 x 1.035 x 1.035 = 61.5，装有两个 Impulse Thruster IV 的 Adaptive Core II 产生 (0 + 2 x 16.5) x 1.035 x 1.035 = 35.4（装两个 Momentum Thruster IV 则为 32.3）。

| 名称 | 稀有度 | 固定速度提升 | 速度倍率 | 费用 |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | 劣质 | +5 | 1.02x | 20,000 信用点 |
| **Impulse Thruster II** | 普通 | +10 | 1.025x | 仅可制造 |
| **Impulse Thruster III** | 稀有 | +15 | 1.03x | 仅可制造 |
| **Impulse Thruster IV** | 史诗 | +16.5 | 1.035x | 仅可制造 |
| **Momentum Thruster I** | 劣质 | +4.5 | 1.06x | 20,000 信用点 |
| **Momentum Thruster II** | 普通 | +9 | 1.07x | 仅可制造 |
| **Momentum Thruster III** | 稀有 | +12.5 | 1.09x | 仅可制造 |
| **Momentum Thruster IV** | 史诗 | +13.1 | 1.11x | 仅可制造 |

### 哪个推进器装哪里 {#which-thruster-where}

Impulse 提供更多固定速度，Momentum 的倍率更大，所以哪个更快，取决于引擎本来就产生多少速度。固定速度在可供相乘的速度很少的地方作用最大：自适应核心（它没有自身速度）以及装有一两个推进器的引擎。倍率则在可供相乘的速度很多的地方作用最大：装满三个推进器的 Engine III。每个槽位都装 IV 阶推进器时，各自产生的速度如下：

| 推进器装在哪里 | 装 Impulse Thruster IV | 装 Momentum Thruster IV | 更快的一方 |
| :--- | :---: | :---: | :--- |
| Engine I，1 个推进器 | 19.1 | 16.8 | Impulse |
| Engine II，2 个推进器 | 39.6 | 37.2 | Impulse |
| Engine III，1 个推进器 | 23.3 | 21.2 | Impulse |
| Engine III，2 个推进器 | 41.8 | 39.7 | Impulse |
| Engine III，3 个推进器 | 61.5 | 62.0 | Momentum |
| Adaptive Core II，2 个推进器 | 35.4 | 32.3 | Impulse |

- **较低的阶。** I 到 III 阶的规律相同，但有两处接近：Engine II 装两个推进器时，两个系列在 I 阶和 II 阶打平（相差不到 0.05）；Engine III 装两个时，Momentum 在 I 阶和 II 阶领先约 0.2。从 III 阶起，两种情况下都是 Impulse 领先，领先 1.4 到 2.4。装满三个推进器的 Engine III 里，Momentum 在每一阶都领先，领先 0.4 到 1.7。
- **在 Engine III 里混装。** 最快的 Engine III 装一个 Impulse Thruster IV 和两个 Momentum Thruster IV：(6 + 16.5 + 2 x 13.1) x 1.035 x 1.11 x 1.11 = 62.1，略高于三个 Momentum（62.0）或三个 Impulse（61.5）。

[锻造炉](/wiki/06-Items/Forge.md)为推进器速度倍率附加的加成，作用于超出 1 的部分（1.11x 加上 +15% 得到 1.1265x）；锻造炉不会给 1.05x 及以下的倍率附加加成：加在 Impulse Thruster 的 1.02x 到 1.035x 上，增加的不到 0.006（1.035x 加上 +15% 得到 1.040x）。Impulse Thruster 有一项加成（固定速度），Momentum Thruster 有两项。

每个系列的 I 阶以 20,000 信用点出售。II 至 IV 阶在[装配站](/wiki/06-Items/Overview.md#upgrading-modules)中制成，每一阶都由同系列低一阶的推进器升级而来（Impulse Thruster II 由一个 Impulse Thruster I 制成，III 由 II，IV 由 III），另需 Thulium、掉落物和板：II 阶或 III 阶需要来自你 Skylab 的 2 块或 4 块 Velkonite Reinforced Plate，IV 阶需要 3 块 Dark Matter Plate。推进器不会更换系列：Impulse 还是 Momentum，在购买 I 阶时选择。它们都沿用被消耗推进器的附魔等级，其加成会重新随机（[模块升级](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)）。推进器不能装进[技能槽位](/wiki/03-Mechanics/Abilities.md)；它们属于引擎和自适应核心的内部。

### 甩开外星人 {#outrunning-aliens}

外星人的飞行速度分别是 120（Seeker）、160（Phantasm）、175（Bulwark）、180（Goombah）和 230（Crystalys）。装了一个 Engine II 和两个推进器的 Ostirion，装 Impulse Thruster I 时速度为 223.1：仍然低于 Crystalys，所以要用装配站制成的推进器才能甩开它（Impulse Thruster II 为 234.2，III 为 245.5，IV 为 249.2）。Momentum Thruster 在这艘舰船上速度相同或稍低（Momentum Thruster I 为 223.2，II 至 IV 为 234.2、243.8、246.7）：两个系列的 I 阶都低于 Crystalys，在装配站制成的各阶则都高于它。
