<!-- wiki-i18n source: ce2f2e451bffe3b4 -->
<!-- wiki-i18n title: 激光 -->
# 激光与弹药 {#lasers-ammo}

<!-- wiki-search: arc amp; focus amp; pulse amp; prism amp; nova amp; apex amp; damage amp 1; crit amp 1; amps; penetration amp; shield penetration -->

武器是 SpaceCorps 中造成伤害的主要手段。

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## 物品树 {#item-tree}

装配站制造的东西要先有对应的科技；将指针悬停在物品上可看到研究所需的时间。科技树、燃料和加速见 [研究](/wiki/03-Mechanics/Research.md)。

```tree
Quantum Laser I | laser, shoddy | buy 8000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser II | laser, common | buy 80000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser III | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Quantum Laser II, 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-III | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser III, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-III, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp I | laser-amp, shoddy | buy 10000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp I | laser-amp, shoddy | buy 15000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp I | laser-amp, shoddy | buy 15000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Damage Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Crit Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Penetration Amp I, 20 Daraxium, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Damage Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Crit Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Penetration Amp II, 1 Power Core, 30 Nyxite, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Damage Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Crit Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp IV | laser-amp, epic | craft 1200 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Penetration Amp III, 1 Power Core, 30 Cataclysite, 40 Quorvium, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Standard Battery | ammo, common | buy 5 Credits | /wiki/06-Items/Lasers.md#laser-ammunition
Siphon Battery | ammo, rare | buy 0.25 Thulium | /wiki/06-Items/Lasers.md#siphon-battery
Advanced Plasma | ammo, rare | buy 0.5 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Ultra Core | ammo, rare | buy 1 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Experimental Fusion Core | ammo, epic | buy 2.2 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition

Quantum Laser I -> Quantum Laser II => Quantum Laser III => Starfire-III => Helios Beam
Damage Amp I => Damage Amp II => Damage Amp III => Damage Amp IV
Crit Amp I => Crit Amp II => Crit Amp III => Crit Amp IV
Penetration Amp I => Penetration Amp II => Penetration Amp III => Penetration Amp IV
Standard Battery -> Advanced Plasma -> Ultra Core -> Experimental Fusion Core
```
<!-- item-tree:end -->

## 激光 {#lasers}

把激光直接装备在舰船的激光槽位上，或装在无人机中，以提升你的进攻能力。

| 名称 | 稀有度 | 基础伤害 | 暴击率 | 射程 | 增幅器槽位 | 费用 |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Quantum Laser I** | 劣质 | 55 | – | 600 | 1 | 8,000 信用点 |
| **Quantum Laser II** | 普通 | 65 | – | 700 | 2 | 80,000 信用点 |
| **Quantum Laser III** | 稀有 | 80 | 10% | 800 | 3 | 仅可制造 |
| **Starfire-III** | 神话 | 135 | 15% | 850 | 3 | 仅可制造 |
| **Helios Beam** | 神话 | 185 | 25% | 900 | 3 | 仅可制造 |

“射程”一列是每把激光自己的射程。**你的舰船以所有激光射程的平均值开火**（无人机中的激光也计入），四舍五入取整，目标一进入这个距离，每把激光就会开火。一把 Starfire-III 加两把 Quantum Laser II，舰船的射程是 750，而不是 850；三把 Starfire-III 则保持 850，而全都相同的激光不会带来任何变化。锻造炉的射程加成会在取平均值之前先计入其所在的那把激光。没有激光时，机库不显示射程（只有一条短横线），激光无法开火，但你的火箭仍然可以，每枚各有自己的射程（见[火箭](/wiki/06-Items/Rockets.md)）。在机库中，当你的激光射程不一致时，对应的图块会写着“平均射程”，把鼠标悬停在上面会列出每把激光的射程。

Quantum Laser I 和 II 自身没有暴击率（“–”）：装在它们槽位中的 Damage Amp 或 Crit Amp 会带来暴击率（Penetration Amp 不会）。暴击在飘出的伤害数字中以不同的颜色显示（冰青色、更大，并带有“!”；见[伤害与治疗数字](/wiki/03-Mechanics/Combat.md#damage-and-heal-numbers)）。

激光也能伤害[小行星](/wiki/03-Mechanics/Asteroid-Mining.md#breaking-one)，但只有一轮齐射对飞船伤害的 5%（你的增幅器、增益、弹药和暴击都会计入，之后再扣除小行星的装甲；Siphon Battery 无法伤害小行星）。击碎小行星要靠火箭。

### 制造顶级的三把激光 {#making-the-top-three-lasers}

**Quantum Laser III**、**Starfire-III** 和 **Helios Beam** 只能在**装配站**制造，每一把都由低一级的激光制成：商店里的 Quantum Laser II 变成 Quantum Laser III，再变成 Starfire-III，最后变成 Helios Beam。Quantum Laser III 已不再在商店出售；已经拥有一把的飞行员可以继续保留。每个配方都需要来自 [Skylab](/wiki/03-Mechanics/Skylab.md) 锻造厂的强化板，Helios Beam 还需要 3 块 Dark Matter Plate：

| 激光 | 制造时间 | 所需材料 |
| :--- | :---: | :--- |
| Quantum Laser III | 1 分钟 | 1 把 Quantum Laser II、10 个 Ship Fragment、2 块 Velkonite Reinforced Plate、1,500 Thulium |
| Starfire-III | 1 分钟 | 1 把 Quantum Laser III、15 个 Ship Fragment、8 块 Velkonite Reinforced Plate、1 块 Reinforced Hull Plate、1,500 Thulium、100,000 信用点 |
| Helios Beam | 3 分钟 | 1 把 Starfire-III、50 个 Cataclysite、2 个 Power Core、18 块 Orvium Reinforced Plate、3 块 Dark Matter Plate、4 块 Reinforced Hull Plate、2,000 Thulium |

装配站页面会把你拥有的数量与配方所需的数量对照显示，“组装”按钮则会说明你缺少什么。 把鼠标指向配方的图片或名称，或其中的某种材料，就会显示该物品的完整描述和属性。

**Quantum Laser III 由一把 Quantum Laser II 制成。** Quantum Laser II 是商店里的激光（80,000 信用点），Quantum Laser III 会把它消耗掉，所以配方里的 10 个 Ship Fragment、2 块 Velkonite Reinforced Plate 和 1,500 Thulium，要加在你在商店为 Quantum Laser II 付的钱之上。规则与下面 Starfire-III 的相同：Quantum Laser III 沿用被它消耗的 Quantum Laser II 的附魔等级（神圣·Quantum Laser II 制成神圣·Quantum Laser III），其加成会重新随机；由你选择用哪一把 Quantum Laser II，使用高于标准等级的一把之前，配方卡片会先询问，而且 Quantum Laser II 必须是未使用状态：**请先把它从你的舰船上取下**（嵌入其中的增幅器会回到你的物品栏），并把它从运输储藏库中取出。当它装在舰船上时，“组装”按钮会显示“请先取下 Quantum Laser II”。

**Starfire-III 由一把 Quantum Laser III 制成。** 你要先制造 Quantum Laser III，Starfire-III 会把它消耗掉。Quantum Laser III 已经花掉的东西不会再被要求一次，所以两者合计的花费，等于 Starfire-III 此前单独制造时的花费（3,000 Thulium、100,000 信用点、25 个 Ship Fragment、10 块 Velkonite Reinforced Plate、1 块 Reinforced Hull Plate，以及 2 分钟），再加上 Quantum Laser III 所消耗的那把 Quantum Laser II。如果你已经有一把 Quantum Laser III，只需支付 Starfire-III 自己的那一部分。规则与下面 Helios Beam 的相同：Starfire-III 沿用被它消耗的 Quantum Laser III 的附魔等级（神圣·Quantum Laser III 制成神圣·Starfire-III），其加成会重新随机；由你选择用哪一把 Quantum Laser III，使用高于标准等级的一把之前，配方卡片会先询问，而且 Quantum Laser III 必须是未使用状态：**请先把它从你的舰船上取下**（嵌入其中的增幅器会回到你的物品栏），并把它从运输储藏库中取出。当它装在舰船上时，“组装”按钮会显示“请先取下 Quantum Laser III”。

**Helios Beam 由一把 Starfire-III 制成。** 你要先制造 Starfire-III（连同它的 Quantum Laser III 共 3,000 Thulium 和 100,000 信用点，而 Quantum Laser III 又会消耗一把 Quantum Laser II），Helios Beam 会把它消耗掉，就像 [Master Drone](/wiki/06-Items/Drones.md) 会消耗一台 Slave Drone 一样。Starfire-III 已经花掉的东西不会再被要求一次，所以两者合计的花费是 Helios Beam 单独制造时所需的 5,000 Thulium、Cataclysite、Power Core 和 Reinforced Hull Plate，以及 18 块 Orvium 强化板而不是 20 块（Starfire-III 的十块 Velkonite 强化板顶替了缺少的两块），另外，由于 Helios Beam 是所在升级链的最后一阶，还要 3 块 Dark Matter Plate；此外你还要付 Starfire-III 的 100,000 信用点和 25 个 Ship Fragment，以及升级链最开头的那一把 Quantum Laser II。规则与[模块升级](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)相同：Helios Beam 沿用被它消耗的 Starfire-III 的附魔等级（神圣·Starfire-III 制成神圣·Helios Beam），其加成会重新随机；当你持有多把 Starfire-III 时，由你选择用哪一把，使用高于标准等级的一把之前，配方卡片会先询问。Starfire-III 必须是未使用状态：**请先把它从你的舰船上取下**（嵌入其中的增幅器会回到你的物品栏），并把它从运输储藏库中取出。当它装在舰船上时，“组装”按钮会显示“请先取下 Starfire-III”。

强化板从哪里来：

- **Velkonite Reinforced Plate**（Quantum Laser III 和 Starfire-III 所需）由 Velkonite 锻造而成，锻造厂 1 级时每块板 40 个矿石。**Orvium Reinforced Plate**（Helios Beam 所需）由 Orvium 锻造而成，每块板 80 个矿石。
- **Dark Matter Plate**（Helios Beam 需要 3 块）在研究了它的配方之后，由装配站用 5 个 Dark Matter、1 块 Velkonite Reinforced Plate、1 块 Orvium Reinforced Plate 和 250 Thulium 压制而成。3 块共需 15 个 Dark Matter，平均相当于 7.5 枚来自[黑洞](/wiki/03-Mechanics/Black-Hole.md)的 N.I.K.E. 火箭：整个流程见 [Dark Matter 与 Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)。
- 矿石只来自你 Skylab 的采集器。5 级的 Velkonite 采集器每小时开采 18 个 Velkonite，所以制造一把 Quantum Laser III 的强化板需要大约 4 小时的开采，Starfire-III 的十块板（两块在它的 Quantum Laser III 中，八块在它自己的一步中）则需要大约 22 小时。Helios Beam 是耗时最长的：它的 18 块板需要 1,440 个 Orvium，5 级 Orvium 采集器大约要开采 4 天，它的 3 块 Dark Matter Plate 里多出的 3 块 Orvium 板还要再加 240 个 Orvium，大约 17 小时。
- 资源仓库 1 级时每种矿石最多容纳 240 个：锻造厂 1 级时可做 6 块 Velkonite 板或 3 块 Orvium 板。所以请边开采边锻造（锻造厂 1 级时一批最多是 10 块板），或者升级仓库。
- 锻造出的强化板会留在锻造厂中，等你在舰船降落时收取，收取后作为普通物品进入你的物品栏。

Ship Fragment、Cataclysite、Power Core 和 Reinforced Hull Plate 由外星人掉落；每种材料的全部来源和用途见[资源](/wiki/06-Items/Resources.md)页面；[Bulwark](/wiki/04-Aliens/Bulwark.md) 和 [Goombah](/wiki/04-Aliens/Goombah.md) 页面上的战利品列表则显示了具体数量。

---

## 激光增幅器（Amp） {#laser-amplifiers-amps-}

把它们直接装入激光的槽位，以增强激光的特性。共有**三个系列，每个四阶**，命名方式和护盾电池一样：**Damage Amp** 增加固定数值的伤害，**Crit Amp** 增加暴击率和固定暴击伤害，**Penetration Amp** 则从目标的吸收率中扣除点数（[见下文](#shield-penetration-of-a-laser-hit)）。它们不是[增益](/wiki/06-Items/Boosters.md)：**Laser Damage Booster I** 和 **Laser Damage Booster II** 是有时限的增益（10 小时内 +10% 激光伤害），没有东西可装。

| 名称 | 稀有度 | 基础伤害提升 | 暴击率提升 | 固定暴击伤害 | 费用 |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Damage Amp I** | 劣质 | +10 | +5% | +5 | 10,000 信用点 |
| **Damage Amp II** | 优秀 | +16 | +5% | +8 | 仅可制造 |
| **Damage Amp III** | 稀有 | +26 | +6% | +13 | 仅可制造 |
| **Damage Amp IV** | 史诗 | +38 | +7% | +20 | 仅可制造 |
| **Crit Amp I** | 劣质 | +0 | +15% | +0 | 15,000 信用点 |
| **Crit Amp II** | 优秀 | +0 | +20% | +14 | 仅可制造 |
| **Crit Amp III** | 稀有 | +0 | +25% | +24 | 仅可制造 |
| **Crit Amp IV** | 史诗 | +0 | +25% | +44 | 仅可制造 |

| 名称 | 稀有度 | 护盾穿透 | 费用 |
| :--- | :--- | :---: | :--- |
| **Penetration Amp I** | 劣质 | +3% | 15,000 信用点 |
| **Penetration Amp II** | 优秀 | +6% | 仅可制造 |
| **Penetration Amp III** | 稀有 | +9% | 仅可制造 |
| **Penetration Amp IV** | 史诗 | +12% | 仅可制造 |

**每个系列只出售第一阶**，在商店购买。其余三阶在[装配站](/wiki/06-Items/Overview.md#upgrading-modules)中用低一阶的增幅器制作，前提是你已在 Skylab 研究了它们的科技（[研究](/wiki/03-Mechanics/Research.md)）。每一步需要 Thulium、外星人的掉落物和板（II、III 阶用来自你 Skylab 的 Velkonite Reinforced Plate，IV 阶用 3 块 Dark Matter Plate），新增幅器沿用被消耗增幅器的附魔等级，加成会重新随机（[模块升级](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)）。Penetration 的几步会加入晶体透镜。每个 IV 阶增幅器都需要 3 块 [Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)，和每条升级链的最后一阶一样，所以 IV 阶增幅器的科技要先研究那块板的科技。

| 步骤 | Thulium | 用时 | 除低一阶的增幅器外 |
| :--- | ---: | ---: | :--- |
| Damage Amp II / Crit Amp II | 250 | 60 秒 | 10 个 Cataclysite、1 块 Velkonite Reinforced Plate |
| Damage Amp III / Crit Amp III | 1,000 | 60 秒 | 20 个 Cataclysite、1 个 Power Core、2 块 Velkonite Reinforced Plate |
| Damage Amp IV / Crit Amp IV | 1,200 | 60 秒 | 30 个 Cataclysite、1 个 Power Core、3 块 Dark Matter Plate |
| Penetration Amp II | 250 | 60 秒 | 20 个 Daraxium、10 个 Cataclysite、1 块 Velkonite Reinforced Plate |
| Penetration Amp III | 1,000 | 60 秒 | 30 个 Nyxite、20 个 Cataclysite、1 个 Power Core、2 块 Velkonite Reinforced Plate |
| Penetration Amp IV | 1,200 | 90 秒 | 40 个 Quorvium、30 个 Cataclysite、1 个 Power Core、3 块 Dark Matter Plate |

一把带有 3 个 IV 阶增幅器的 Helios Beam 含有 4 件最后一阶的部件：12 块 Dark Matter Plate、60 个 Dark Matter，平均相当于 30 枚 N.I.K.E. 火箭。每个槽位都是最后一阶的 Wraith 含有 900 个 Dark Matter（[Dark Matter 与 Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md#what-the-last-tier-asks-for)）。

### 哪种增幅器装在哪里 {#which-amp-goes-where}

伤害增幅器给任何激光增加的伤害都一样，所以装在 **Quantum 系列激光**上最划算。暴击增幅器放大的是激光本来的输出，所以激光打得越重，它就越值：在 **Starfire-III** 上它与伤害系持平，在 **Helios Beam** 上则领先约 3.5%。激光的暴击率上限是 100%：三个 Crit Amp III 或 Crit Amp IV 恰好能把 Helios Beam 推到这个数字。Penetration Amp 既不增加伤害也不增加暴击率：它是给那些护盾本会承受你大部分命中的舰船用的（[见下文](#when-is-a-penetration-amp-worth-a-slot)）。

装上同样的增幅器时，一把激光总是比低一级的那把更强，所以更好的增幅器永远无法取代更好的激光：装了三个 Damage Amp IV 的 Quantum Laser III，输出低于装了三个 Damage Amp I 的 Helios Beam（前提是部件的附魔等级相同：锻造到神圣或更高的 Quantum Laser III 和 Damage Amp IV，在随机到最佳数值时，可以超过装着 Damage Amp I 的普通 Helios Beam，神圣等级时只是险胜）。


---

## 激光弹药 {#laser-ammunition}

可消耗的电池，成倍提升你激光齐射的伤害：

| 名称 | 稀有度 | 伤害倍率 | 护盾穿透 | 每发价格 |
| :--- | :--- | :---: | :---: | :--- |
| **Standard Battery** | 普通 | 1.0x | – | 5 信用点 |
| **Advanced Plasma** | 稀有 | 2.0x | – | 0.5 Thulium |
| **Ultra Core** | 稀有 | 3.0x | 5% | 1.0 Thulium |
| **Experimental Fusion Core** | 史诗 | 4.0x | 10% | 2.2 Thulium |
| **Siphon Battery** | 稀有 | 1.0x，仅作用于护盾 | – | 0.25 Thulium |

**护盾穿透**会在你齐射的每一次命中中，从目标的吸收率里扣除：护盾承受的是目标的吸收率减去穿透后的份额（见[护盾机制](/wiki/03-Mechanics/Shields.md#shield-penetration)）。你的 Penetration Amp 和无人机编队会加到弹药的穿透上，完整的总和在[本页下方](#shield-penetration-of-a-laser-hit)。对付吸收率为 80% 的舰船（最强的护盾配最强的电池），x4 弹药的 10% 会让护盾只承受 70% 的伤害，船体承受 30%。它对付船体相对护盾较小的舰船时最有价值；而一艘吸收率 80% 的超大型舰船，无论有没有穿透，撑住的程度都没有区别。外星人没有值得一提的吸收率属性（它们的护盾承受一次命中的 80%），穿透同样会从中扣除。

### Siphon Battery

Siphon Battery 是用来偷取护盾而不是打穿船体的弹药。它对**目标的护盾直接造成 x1 伤害**，并把同样的数值加到**你自己的护盾**上，最高不超过你的护盾上限。像其他弹药一样，在快捷栏的弹药选择器中选择它（它是带有青绿色漩涡的那个图块）。它不会发射光束：一道纤细、微弱的青绿色探针射向目标，目标的护盾在探针命中处泛起青绿色闪光，而你吸走的护盾会化作发光的青绿色能量包，肉眼可见地流回你的舰船（三到十个，吸取量越大越多），在大约半秒内一个接一个地到达。每个到达的能量包都会让你的护盾脉动一下。视野内任何飞行员使用的 Siphon Battery 你都能看到同样的效果，无论它吸取的是谁：外星人、其他飞行员，还是企业飞行员的舰船。

- **仅作用于护盾**：船体绝不会受到影响，目标的吸收率不会对伤害进行分摊，Siphon Battery 永远无法摧毁任何东西。它的伤害以目标护盾剩余的量为上限。
- **无物可吸**：对付没有护盾的目标，它什么也吸不到，也什么都给不了你。这一轮齐射仍然会消耗弹药，每把激光一块电池，和所有弹药一样。你只会看到探针和船体上一道暗淡的闪烁，没有能量包。
- **获得**：你的护盾绝不会超过上限，而且吸入护盾不会推迟你自己的护盾再生。
- **外星人和飞行员**一样都有护盾可吸。从外星人身上吸走护盾，算作一次命中，计入[首击归属](/wiki/03-Mechanics/Combat.md)；没找到护盾的则不算。它也会像任何其他命中一样唤醒只会还击的 Seeker 或 Goombah。
- **暴击**同样有效：暴击的齐射吸取量是 1.5 倍，其数字会以暴击的样式显示。它的能量包更大更亮，目标的护盾闪光也更强烈。
- [企业飞行员](/wiki/03-Mechanics/Company-Pilots.md)使用标准 x1 弹药开火。

---

## 激光命中的护盾穿透 {#shield-penetration-of-a-laser-hit}

每一次激光命中都会从目标的吸收率中扣除点数，来源最多三个，彼此相加：你的**弹药**（Ultra Core 5%，Experimental Fusion Core 10%）、你的 **Penetration Amp**，以及**无人机编队**（Gemini +9%，Stiletto +16%；[无人机编队](/wiki/03-Mechanics/Formations.md)）。**总和没有上限**（直接火箭也以同样的方式把自己的穿透和编队的穿透相加：[火箭](/wiki/06-Items/Rockets.md)）。然后护盾承受目标吸收率减去该次命中穿透后的份额，船体承受其余部分（[护盾机制](/wiki/03-Mechanics/Shields.md#shield-penetration)）。

- **你的增幅器按你所有激光的平均值计算。** 一次齐射就是一次命中，所以游戏会把每把激光上增幅器的穿透相加（无人机里的激光也计入），再对你所有的激光取平均，每把按其伤害加权，和暴击率的算法一样。每把激光上三个 Penetration Amp IV 是 36%；十二把激光里只有一把装一个 Penetration Amp IV 是 1%。Wraith 有 12 把激光和 36 个增幅槽位，要凑到 36% 必须把 36 个槽位全部装满。
- **机库会显示它。** 机库的战斗属性中，每艘飞船都有一个显示所示配置的激光增幅器数值的**穿透**图块（没有 Penetration Amp 时为 0.0%）；弹药和编队不计入其中。飞行中的**舰船**窗口在下方一行的末尾有一个**穿透**标签（为腾出位置，配置和速度标签只显示一个图标和一个数字），显示激光命中的总穿透：你的增幅器、所穿戴的编队和所用的弹药相加，一换就更新，它的悬停提示会列出这三部分。
- **最强的激光是 62%。** Experimental Fusion Core（10%）、Stiletto（16%）和每把激光上三个 Penetration Amp IV（36%）加起来是 62%。
- **Penetration Amp IV 上的锻造加成会计入。** Penetration Amp 和其他增幅器一样可以锻造，它唯一的一条加成会成倍提高穿透：一条永恒级加成（+9% 至 +15%）会让 Penetration Amp IV 达到 13.1 至 13.8 点，而不是 12 点。在最强的配置里，三个永恒级的加起来是 67.4%，每一点都会计入。

| 激光齐射 | 弹药 | 增幅器（3 个槽位） | 编队 | 合计 |
|---|---|---|---|---|
| 仅 Experimental Fusion Core | 10% | – | – | **10%** |
| Fusion Core + Gemini | 10% | – | 9% | **19%** |
| Fusion Core + Stiletto（Penetration Amp 出现之前的最强） | 10% | – | 16% | **26%** |
| Fusion Core + 3 Penetration Amp I | 10% | 9% | – | **19%** |
| Fusion Core + 3 Penetration Amp II | 10% | 18% | – | **28%** |
| Fusion Core + 3 Penetration Amp III | 10% | 27% | – | **37%** |
| Fusion Core + 3 Penetration Amp IV | 10% | 36% | – | **46%** |
| Fusion Core + 3 Penetration Amp IV + Gemini | 10% | 36% | 9% | **55%** |
| Ultra Core + 3 个 Penetration Amp IV + Stiletto（日常最强） | 5% | 36% | 16% | **57%** |
| Fusion Core + 3 个 Penetration Amp IV + Stiletto（最强的激光） | 10% | 36% | 16% | **62%** |

这对目标的护盾意味着什么：每个格子是一次命中中**护盾承受的份额 / 船体承受的份额**。

| 防守方（吸收率） | 无增幅器 | 仅 Fusion Core（10%） | 以前：Fusion Core + Stiletto（26%） | Fusion Core + 3 个 Penetration Amp IV（46%） | 最强的激光（62%） |
|---|---|---|---|---|---|
| Light Shield Core，无电池（45%） | 45 / 55 | 35 / 65 | 19 / 81 | 0 / 100 | 0 / 100 |
| Heavy Shield Core，无电池（50%） | 50 / 50 | 40 / 60 | 24 / 76 | 4 / 96 | 0 / 100 |
| Light Shield Core + Absorption Shield Cell IV（55%） | 55 / 45 | 45 / 55 | 29 / 71 | 9 / 91 | 0 / 100 |
| Heavy Shield Core + 3 个 Capacity Shield Cell IV（65%） | 65 / 35 | 55 / 45 | 39 / 61 | 19 / 81 | 3 / 97 |
| 出厂最好的护盾（80%） | 80 / 20 | 70 / 30 | 54 / 46 | 34 / 66 | 18 / 82 |
| 最好的护盾，永恒锻造（最高掷值）加 34 级赛季商店（95.4%） | 95 / 5 | 85 / 15 | 69 / 31 | 49 / 51 | 33 / 67 |
| 最好的护盾，永恒锻造（最高掷值）加赛季商店上限（102%） | 100 / 0 | 92 / 8 | 76 / 24 | 56 / 44 | 40 / 60 |
| 任何外星人（80%） | 80 / 20 | 70 / 30 | 54 / 46 | 34 / 66 | 18 / 82 |

最强的激光会打空没有电池的护盾核心，以及配了最好电池的 Light Shield Core（船体承受整次命中）；带三个 Capacity 电池的 Heavy Shield Core 会保留每次命中的 3%，最好的护盾保留其中的 18%（有加成时是 33%）。单独的火箭永远打不空护盾（最高 35%），但 Lancet III 或 Rivet III 配上 Stiletto（51%）就能打空。

### 什么时候值得为 Penetration Amp 腾一个槽位？ {#when-is-a-penetration-amp-worth-a-slot}

**Penetration Amp 能克制吸收率，吸收率越高越有用：面对船体较小的舰船，在约 95%（赛季商店、锻造炉和 Rampart 的配置）时，Penetration 配置击杀速度约为最好的普通配置的 1.8 倍；面对出厂最好的护盾（80%），三个 Penetration Amp 比三个同阶的 Crit Amp 约少用 11% 的时间。面对外星人几乎没有收益。**

- **它不提供伤害。** 在 Helios Beam 上，三个 Penetration Amp IV 每次齐射只有 187 点伤害（弹药 x1，随机波动和暴击的平均值），而三个 Damage Amp IV 是 356，三个 Crit Amp IV 是 369：大约一半。它夺回的是护盾的份额，所以只有在船体相对护盾较小、吸收率较高的时候才划算；面对船体庞大、本来就扛得住的 Wraith 或 Ironclad，普通的 Damage 或 Crit 组合速度差不多（一把激光里的一个 Penetration Amp 最多只多出 5%）。
- **外星人。** 它们的护盾承受命中的 80% 减去你的穿透，所以它对外星人也有效，但同阶的 Damage Amp 或 Crit Amp 杀得一样快或更快；例外是配合编队作战的 Phantasm 或 Goombah，此时一把激光里的一个 Penetration Amp 最多多出 5%。
- **代价。** 每个 Penetration Amp IV 需要 3 块 Dark Matter Plate（15 个 Dark Matter），每个 IV 阶增幅器都一样，所以装满 36 个槽位的 Wraith 需要 108 块板，共 540 个 Dark Matter。
