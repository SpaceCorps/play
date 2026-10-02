<!-- wiki-i18n source: cbf999e7c87f512e -->
<!-- wiki-i18n title: 激光 -->
# 激光与弹药 {#lasers-ammo}

武器是 SpaceCorps 中造成伤害的主要手段。

## 激光 {#lasers}

把激光直接装备在舰船的激光槽位上，或装在无人机中，以提升你的进攻能力。

| 名称 | 稀有度 | 基础伤害 | 暴击率 | 射程 | 增幅器槽位 | 费用 |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Quantum Laser 1** | 劣质 | 55 | – | 600 | 1 | 8,000 信用点 |
| **Quantum Laser 2** | 普通 | 65 | – | 700 | 2 | 80,000 信用点 |
| **Quantum Laser 3** | 稀有 | 80 | 10% | 800 | 3 | 仅可制造 |
| **Starfire-3** | 神话 | 135 | 15% | 850 | 3 | 仅可制造 |
| **Helios Beam** | 神话 | 185 | 25% | 900 | 3 | 仅可制造 |

“射程”一列是每把激光自己的射程。**你的舰船以所有激光射程的平均值开火**（无人机中的激光也计入），四舍五入取整，目标一进入这个距离，每把激光就会开火。一把 Starfire-3 加两把 Quantum Laser 2，舰船的射程是 750，而不是 850；三把 Starfire-3 则保持 850，而全都相同的激光不会带来任何变化。锻造炉的射程加成会在取平均值之前先计入其所在的那把激光。没有激光时，机库不显示射程（只有一条短横线），激光无法开火，但你的火箭仍然可以，每枚各有自己的射程（见[火箭](/wiki/05-Items/Rockets.md)）。在机库中，当你的激光射程不一致时，对应的图块会写着“平均射程”，把鼠标悬停在上面会列出每把激光的射程。

Quantum Laser 1 和 2 自身没有暴击率（“–”）：装在它们槽位中的伤害增幅器或暴击增幅器会带来暴击率。暴击在飘出的伤害数字中以不同的颜色显示（冰青色、更大，并带有“!”）。

### 制造顶级的三把激光 {#making-the-top-three-lasers}

**Quantum Laser 3**、**Starfire-3** 和 **Helios Beam** 只能在**装配站**制造。Quantum Laser 3 已不再在商店出售；已经拥有一把的飞行员可以继续保留。每个配方都需要来自 [Skylab](/wiki/03-Mechanics/Skylab.md) 锻造厂的强化板：

| 激光 | 制造时间 | 所需材料 |
| :--- | :---: | :--- |
| Quantum Laser 3 | 1 分钟 | 10 个 Ship Fragment、2 块 Velkonite Reinforced Plate、1,500 Thulium |
| Starfire-3 | 1 分钟 | 1 把 Quantum Laser 3、15 个 Ship Fragment、8 块 Velkonite Reinforced Plate、1 块 Reinforced Hull Plate、1,500 Thulium、100,000 信用点 |
| Helios Beam | 3 分钟 | 1 把 Starfire-3、50 个 Cataclysite、2 个 Power Core、18 块 Orvium Reinforced Plate、4 块 Reinforced Hull Plate、2,000 Thulium |

装配站页面会把你拥有的数量与配方所需的数量对照显示，“组装”按钮则会说明你缺少什么。

**Starfire-3 由一把 Quantum Laser 3 制成。** 你要先制造 Quantum Laser 3，Starfire-3 会把它消耗掉。Quantum Laser 3 已经花掉的东西不会再被要求一次，所以两者合计的花费，恰好等于 Starfire-3 此前单独制造时的花费：3,000 Thulium、100,000 信用点、25 个 Ship Fragment、10 块 Velkonite Reinforced Plate、1 块 Reinforced Hull Plate，以及 2 分钟。如果你已经有一把 Quantum Laser 3，只需支付 Starfire-3 自己的那一部分。规则与下面 Helios Beam 的相同：Starfire-3 沿用被它消耗的 Quantum Laser 3 的附魔等级（神圣·Quantum Laser 3 制成神圣·Starfire-3），其加成会重新随机；由你选择用哪一把 Quantum Laser 3，使用高于标准等级的一把之前，配方卡片会先询问，而且 Quantum Laser 3 必须是未使用状态：**请先把它从你的舰船上取下**（嵌入其中的增幅器会回到你的物品栏），并把它从运输储藏库中取出。当它装在舰船上时，“组装”按钮会显示“请先取下 Quantum Laser 3”。

**Helios Beam 由一把 Starfire-3 制成。** 你要先制造 Starfire-3（连同它的 Quantum Laser 3 共 3,000 Thulium 和 100,000 信用点），Helios Beam 会把它消耗掉，就像 [Master Drone](/wiki/05-Items/Drones.md) 会消耗一台 Slave Drone 一样。Starfire-3 已经花掉的东西不会再被要求一次，所以两者合计的花费是 Helios Beam 单独制造时所需的 5,000 Thulium、Cataclysite、Power Core 和 Reinforced Hull Plate，以及 18 块 Orvium 强化板而不是 20 块（Starfire-3 的十块 Velkonite 强化板顶替了缺少的两块）；此外你还要付 Starfire-3 的 100,000 信用点和 25 个 Ship Fragment。规则与[模块升级](/wiki/05-Items/Forge.md#module-upgrades-in-the-assembly)相同：Helios Beam 沿用被它消耗的 Starfire-3 的附魔等级（神圣·Starfire-3 制成神圣·Helios Beam），其加成会重新随机；当你持有多把 Starfire-3 时，由你选择用哪一把，使用高于标准等级的一把之前，配方卡片会先询问。Starfire-3 必须是未使用状态：**请先把它从你的舰船上取下**（嵌入其中的增幅器会回到你的物品栏），并把它从运输储藏库中取出。当它装在舰船上时，“组装”按钮会显示“请先取下 Starfire-3”。

强化板从哪里来：

- **Velkonite Reinforced Plate**（Quantum Laser 3 和 Starfire-3 所需）由 Velkonite 锻造而成，锻造厂 1 级时每块板 40 个矿石。**Orvium Reinforced Plate**（Helios Beam 所需）由 Orvium 锻造而成，每块板 80 个矿石。
- 矿石只来自你 Skylab 的采集器。5 级的 Velkonite 采集器每小时大约开采 29 个 Velkonite，所以制造一把 Quantum Laser 3 的强化板需要大约 3 小时的开采，Starfire-3 的十块板（两块在它的 Quantum Laser 3 中，八块在它自己的一步中）则需要大约 14 小时。Helios Beam 是耗时最长的：它的 18 块板需要 1,440 个 Orvium，5 级 Orvium 采集器大约要开采 4 天。
- 资源仓库 1 级时每种矿石最多容纳 900 个，所以请边开采边锻造（锻造厂 1 级时一批是 10 块板），或者升级仓库。
- 锻造出的强化板会留在锻造厂中，等你在舰船降落时收取，收取后作为普通物品进入你的物品栏。

Ship Fragment、Cataclysite、Power Core 和 Reinforced Hull Plate 由外星人掉落；每种材料的全部来源和用途见[资源](/wiki/05-Items/Resources.md)页面；[Bulwark](/wiki/04-Aliens/Bulwark.md) 和 [Goombah](/wiki/04-Aliens/Goombah.md) 页面上的战利品列表则显示了具体数量。

---

## 激光增幅器（Amp） {#laser-amplifiers-amps-}

把它们直接装入激光的槽位，以增强激光的特性。共有两条路线，每条四级：**伤害系**增加固定数值的伤害，**暴击系**增加暴击率和固定暴击伤害。

| 名称 | 稀有度 | 基础伤害提升 | 暴击率提升 | 固定暴击伤害 | 费用 |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Damage Amp 1** | 劣质 | +10 | +5% | +5 | 10,000 信用点 |
| **Arc Amp** | 优秀 | +16 | +5% | +8 | 60,000 信用点 |
| **Pulse Amp** | 稀有 | +26 | +6% | +13 | 1,500 Thulium |
| **Nova Amp** | 史诗 | +38 | +7% | +20 | 仅可制造 |
| **Crit Amp 1** | 劣质 | +0 | +15% | +0 | 15,000 信用点 |
| **Focus Amp** | 优秀 | +0 | +20% | +14 | 60,000 信用点 |
| **Prism Amp** | 稀有 | +0 | +25% | +24 | 1,500 Thulium |
| **Apex Amp** | 史诗 | +0 | +25% | +44 | 仅可制造 |

Nova Amp 和 Apex Amp 在[装配站](/wiki/05-Items/Overview.md#upgrading-modules)中分别由 Pulse Amp 和 Prism Amp 制成，各自还需要 Thulium、掉落物和 3 块来自你 Skylab 的 Velkonite Reinforced Plate。它们沿用被消耗的增幅器的附魔等级，其加成会重新随机（[模块升级](/wiki/05-Items/Forge.md#module-upgrades-in-the-assembly)）。

### 哪种增幅器装在哪里 {#which-amp-goes-where}

伤害增幅器给任何激光增加的伤害都一样，所以装在 **Quantum 系列激光**上最划算。暴击增幅器放大的是激光本来的输出，所以激光打得越重，它就越值：在 **Starfire-3** 上它与伤害系持平，在 **Helios Beam** 上则领先约 3.5%。激光的暴击率上限是 100%：三个 Prism Amp 或 Apex Amp 恰好能把 Helios Beam 推到这个数字。

装上同样的增幅器时，一把激光总是比低一级的那把更强，所以更好的增幅器永远无法取代更好的激光：装了三个 Nova Amp 的 Quantum Laser 3，输出低于装了三个 Damage Amp 1 的 Helios Beam（前提是部件的附魔等级相同：锻造到神圣或更高的 Quantum Laser 3 和 Nova Amp，在随机到最佳数值时，可以超过装着 Damage Amp 1 的普通 Helios Beam，神圣等级时只是险胜）。

---

## 激光弹药 {#laser-ammunition}

可消耗的电池，成倍提升你激光齐射的伤害：

| 名称 | 稀有度 | 伤害倍率 | 护盾穿透 | 每发价格 |
| :--- | :--- | :---: | :---: | :--- |
| **Standard Battery** | 普通 | 1.0x | – | 10 信用点 |
| **Advanced Plasma** | 稀有 | 2.0x | – | 0.5 Thulium |
| **Ultra Core** | 稀有 | 3.0x | 5% | 1.0 Thulium |
| **Experimental Fusion Core** | 史诗 | 4.0x | 10% | 2.2 Thulium |
| **Siphon Battery** | 稀有 | 1.0x，仅作用于护盾 | – | 0.25 Thulium |

**护盾穿透**会在你齐射的每一次命中中，从目标的吸收率里扣除：护盾承受的是目标的吸收率减去穿透后的份额（见[护盾机制](/wiki/03-Mechanics/Shields.md#shield-penetration)）。对付吸收率为 80% 的舰船（最强的护盾配最强的电池），x4 弹药的 10% 会让护盾只承受 70% 的伤害，船体承受 30%。它对付船体相对护盾较小的舰船时最有价值；而一艘吸收率 80% 的超大型舰船，无论有没有穿透，撑住的程度都没有区别。外星人没有值得一提的吸收率属性（它们的护盾承受一次命中的 80%），穿透同样会从中扣除。

### Siphon Battery {#siphon-battery}

Siphon Battery 是用来偷取护盾而不是打穿船体的弹药。它对**目标的护盾直接造成 x1 伤害**，并把同样的数值加到**你自己的护盾**上，最高不超过你的护盾上限。像其他弹药一样，在快捷栏的弹药选择器中选择它（它是带有青绿色漩涡的那个图块）。它不会发射光束：一道纤细、微弱的青绿色探针射向目标，目标的护盾在探针命中处泛起青绿色闪光，而你吸走的护盾会化作发光的青绿色能量包，肉眼可见地流回你的舰船（三到十个，吸取量越大越多），在大约半秒内一个接一个地到达。每个到达的能量包都会让你的护盾脉动一下。视野内任何飞行员使用的 Siphon Battery 你都能看到同样的效果，无论它吸取的是谁：外星人、其他飞行员，还是企业飞行员的舰船。

- **仅作用于护盾**：船体绝不会受到影响，目标的吸收率不会对伤害进行分摊，Siphon Battery 永远无法摧毁任何东西。它的伤害以目标护盾剩余的量为上限。
- **无物可吸**：对付没有护盾的目标，它什么也吸不到，也什么都给不了你。这一轮齐射仍然会消耗弹药，每把激光一块电池，和所有弹药一样。你只会看到探针和船体上一道暗淡的闪烁，没有能量包。
- **获得**：你的护盾绝不会超过上限，而且吸入护盾不会推迟你自己的护盾再生。
- **外星人和飞行员**一样都有护盾可吸。从外星人身上吸走护盾，算作一次命中，计入[首击归属](/wiki/03-Mechanics/Combat.md)；没找到护盾的则不算。它也会像任何其他命中一样唤醒只会还击的 Seeker 或 Goombah。
- **暴击**同样有效：暴击的齐射吸取量是 1.5 倍，其数字会以暴击的样式显示。它的能量包更大更亮，目标的护盾闪光也更强烈。
- [企业飞行员](/wiki/03-Mechanics/Company-Pilots.md)使用标准 x1 弹药开火。
