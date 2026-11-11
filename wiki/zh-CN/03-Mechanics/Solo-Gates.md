<!-- wiki-i18n source: 4d2749864875137f -->
<!-- wiki-i18n title: 单人星门 -->
# 单人星门 {#solo-gates}

<!-- wiki-search: solo gates; solo gate; gate; gates; galaxy gates; rift; rifts; alpha rift; beta breach; gamma foundry; delta siege; omega vault; chrono gate; chrono-gate; materializer; energy materializer; scan; spin; gate part; gate parts; guarantee; pity; consolation; wave; waves; nuke wave; skip; boss; lives; resume; abandon; speedrun; no death; challenge; achievement; thulium cap; 单人星门; 星门; 星系之门; 部件; 星门部件; 能量具现器; 扫描; 保底; 波次; 生命; 继续; 放弃; 无死亡; 挑战; 成就; Thulium 上限 -->

**单人星门**是星系之门中由你独自飞入的五座星门：**Alpha Rift**、**Beta Breach**、**Gamma Foundry**、**Delta Siege** 和 **Omega Vault**。每一座都是一个空旷的专属竞技场，外星人的波次一波接一波地向你袭来，最后有一个 Boss 在等着。你用星门的**部件**建造它，部件通过用 Thulium 扫描能量具现器来寻找，通关会发放信用点、Thulium、经验值、荣誉、矿石、装甲板和弹药。

单人星门不是[战队地下城](/wiki/03-Mechanics/Dungeons.md)。地下城是战队为一个小队开启的迷宫，尽头有一名战争领主；单人星门是只有你一个人的竞技场，其他人无法与你一同进入。两者的规则、报酬和限制各自独立。星系之门页面里还有 **Chrono-Gate**，它不是用来飞入的地方，而是为重置打开你的[运输储藏库](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-)的星门：它的部件用同样的扫描来寻找。

## 概览 {#at-a-glance}

<!-- solo-glance:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **星门**：6：Chrono-Gate 和 5 座单人星门，Alpha Rift, Beta Breach, Gamma Foundry, Delta Siege 和 Omega Vault
- **扫描**：每次扫描 100 Thulium，一次最多 1, 5, 10或100 次扫描
- **部件几率**：每次扫描 13%。部件属于哪座星门是随机决定的，每座星门得到扫描的 2.17%。Chrono-Gate 完成后，它的份额退出转盘，单人星门各保持 2.17%
- **保底**：连续 24 次扫描没有部件后，几率会随每次扫描上升，在 47 次之后，下一次扫描必定找到一个。任何一座星门的部件都会让计数重新开始
- **生命**：每次尝试 3；每次死亡损失一条
- **倒计时**：每一波之前 5 秒，第一波和 Boss 那一波也一样。一波没有计时器，一局也没有
- **竞技场**：8,000 × 6,000 单位的开阔空间，没有岩石，里面只有你一个人。一个世界有 16 个这样的空间，全部被占用时你无法进入
- **同时存活的外星人**：同一时间一波最多有 60 个存活，可选波次为 250 个。其余的等待空位
- **Boss**：Boss 在切换阶段时 3 秒 内无法被伤害
- **Thulium 上限**：星门返还的数额不超过你在扫描上花费的 Thulium 的 50%。其余部分会被截断，结果会告诉你截断了多少

<!-- solo-glance:end -->

## 寻找星门部件 {#finding-gate-parts}

打开**星系之门**页面，扫描能量具现器。每次扫描用 Thulium 支付，至多找到一个部件，部件属于六座星门之一，随机决定。建造一座星门需要它的一定数量的部件，部件在你使用之前一直属于你。没有找到部件的扫描不会白费：它会发放一份奖品（[见下](#a-spin-without-a-part)）。每次扫描都要付费，Chrono-Gate 已完成时也一样。Chrono-Gate 完成后，它在扫描中的份额什么也找不到，而单人星门保持自己的几率，所以单人星门的部件无论有没有它，花费都一样。

表格给出每座星门所需的部件数，以及**含保底**时它们的平均花费（一次扫描就是一次抽奖，所以运气好的飞行员花得少，运气差的花得多，最多到保底所允许的最长连续扫描次数）。

<!-- solo-parts:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| 星门 | 完成所需部件 | 每次扫描的部件几率 | 平均扫描次数 | 平均 Thulium |
| :--- | ---: | ---: | ---: | ---: |
| **Chrono-Gate** | 2 | 2.17% | 91 | 9,093 |
| **Alpha Rift** | 11 | 2.17% | 500 | 50,011 |
| **Beta Breach** | 26 | 2.17% | 1,182 | 118,208 |
| **Gamma Foundry** | 54 | 2.17% | 2,455 | 245,508 |
| **Delta Siege** | 87 | 2.17% | 3,955 | 395,541 |
| **Omega Vault** | 108 | 2.17% | 4,910 | 491,017 |

<!-- solo-parts:end -->

Chrono-Gate 的部件会在重置时归零，你每个赛季都要重新找。**单人星门的部件会保留**，保底的计数以及你在扫描上的花费和星门返还金额的记录也会保留；重置不会带走其中任何一项（[星门与重置](#gates-and-the-wipe)）。

### 没有部件的扫描 {#a-spin-without-a-part}

大多数扫描找不到部件。每一次都会发放一份奖品，按下面的几率抽取：第二档倍率或更高的激光弹药、第二档或第三档的火箭堆，以及偶尔出现的[特殊物品](/wiki/06-Items/Special-Items.md)或[容器](/wiki/06-Items/Containers.md)。无法发放的奖品（比如你已经持有该特殊物品的上限）会在同一次抽取中变成一堆弹药或火箭，所以一次扫描绝不会比它的表格少发。奖品的价值明显低于一次扫描的花费：星门是 Thulium 的消耗口。

<!-- solo-prizes:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| 奖励 | 每次扫描的几率 |
| :--- | ---: |
| 一个容器：Chroma Archive | 0.01% |
| 一件特殊物品：Magic Hammer | 0.2% |
| 一件特殊物品：Schematics | 0.2% |
| 一件特殊物品：Philosopher's Stone | 0.2% |
| 一件特殊物品：Forger's Seal | 0.2% |
| 一件特殊物品：Workforce Contract | 0.2% |
| 一件特殊物品：Tinkerer's Badge | 0.1% |
| 激光弹药：Advanced Plasma ×75 | 12.88% |
| 激光弹药：Antimatter Battery I ×62 | 8.59% |
| 激光弹药：Ultra Core ×40 | 8.59% |
| 激光弹药：Antimatter Battery II ×29 | 4.29% |
| 激光弹药：Dark Matter Ammo I ×31 | 4.29% |
| 激光弹药：Experimental Fusion Core ×17 | 2.15% |
| 激光弹药：Dark Matter Ammo II ×17 | 2.15% |
| 火箭：Lancet II ×4 | 8.59% |
| 火箭：Rivet II ×4 | 8.59% |
| 火箭：Ember II ×4 | 8.59% |
| 火箭：Scatter II ×4 | 8.59% |
| 火箭：Lancet III ×1 | 2.15% |
| 火箭：Rivet III ×1 | 2.15% |
| 火箭：Ember III ×1 | 2.15% |
| 火箭：Scatter III ×1 | 2.15% |

<!-- solo-prizes:end -->

## 进入 {#going-in}

你在星系之门页面**建造**星门，再通过它的传送门**跃迁进入**。建造在空间站里进行，飞船停靠即可，不需要在飞行中。需要：

- 星门的部件：它们在**你建造时一次性**扣除，被拒绝的建造不会扣除任何东西；
- 没有其他未结束的单人对局：同一时间只能有一局，离开的对局要先通过传送门重新进入或放弃，才能建造另一座星门；
- 你在主服务器上（区域服务器没有星门）。

建好的星门以一个以它命名的传送门的形式立在你的**主星区**（`M-1`、`T-1` 或 `G-1`，取决于你的企业），星系之门页面会告诉你它在哪里。**出击，飞到传送门并跃迁**，和穿过任何传送门一样。进入时你的世界里必须有空闲的裂隙：每个世界有一定数量的裂隙，全部被占用时你需要等待。

你独自降落在一个空旷竞技场的中央。里面没有人能攻击你，Jump CPU 和 Base CPU 也无法使用。

## 一局如何进行 {#how-a-run-goes}

1. **每一波之前都有倒计时**，第一波和 Boss 那一波也一样。一波没有计时器，一局也没有：需要多久就多久。
2. **一波**会出现在你周围的圆环上，并以星门的节奏向你飞来。同一时间只有一定数量存活，其余的等待空位。它的最后一个外星人死亡时结束。
3. **你的进度会在每一波之后保存。**如果你离开，正在进行的一波会在你回来时整波重新开始。
4. **可选波次**是一大波 Seeker，Delta Siege 和 Omega Vault 各有一个。倒计时期间你可以跳过它：跳过后算作已完成，**不发放任何东西**。如果你打这一波，它的击杀与任何一波的击杀一样发放。
5. **最后一波是 Boss。**它随着船体下降而切换阶段，并且每次切换时有片刻无法被伤害。Boss 死亡后这一局即通关，奖励立即发放。

**生命。**一次死亡损失一条生命，并和其他死亡一样把你送回基地；这一局会等你，计时不会走。只要这一局开启而你在竞技场之外，**你星门的传送门就立在你的主星区**，通过它跃迁会像**继续**一样带着你剩下的生命回到保存的那一波，并且不需要新的部件。你的最后一条生命用完时，这次尝试结束，但这一局会停在最后通过的那一波保持开启，重新进入会补满你的生命。**离开**、下线或切换世界会暂停这一局，且不损失生命。服务器重启也会让你的这一局保持开启。**放弃**会放弃这一局：它的部件作废，你已击杀的外星人按当前情况发放。**继续**只能从飞行中的舰船使用：死亡之后，结果界面上的继续按钮会等待，并附一行说明原因，直到你重生。重生的舰船以受限的船体返回，所以当你的船体低于一半时，结果界面会提醒你；**继续**仍会让你以当前状态返回。你基地的维修舰会在其光环范围内为你修复。

每个世界面对的都是同一座星门：外星人的强度和报酬不取决于你所在的世界。

### 波次 {#the-waves}

外星人就是游戏里的那些（Seeker、Phantasm、Bulwark、Goombah 和 Crystalys），由星门调得更硬或更软。预计时间是星门为处于激光技术起始等级的飞行员设计的耗时（[飞行员专长](/wiki/03-Mechanics/Pilot-Skills.md)）；把激光技术升上去的飞行员会更快完成。

<!-- solo-waves:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| 星门 | 波次数（含 Boss 那一波） | 各波中的外星人 | Boss | 预计时间 |
| :--- | ---: | :--- | :--- | :--- |
| **Alpha Rift** | 10 | 60 Seeker, 160 Phantasm | Enhanced Phantasm | 10 到 15 分钟 |
| **Beta Breach** | 14 | 80 Seeker, 180 Phantasm, 80 Bulwark, 20 Goombah | Enhanced Bulwark | 15 到 25 分钟 |
| **Gamma Foundry** | 18 | 100 Phantasm, 120 Bulwark, 100 Goombah, 8 Crystalys | Elite Crystalys | 25 到 35 分钟 |
| **Delta Siege** | 22 | 250 Seeker, 200 Phantasm, 180 Bulwark, 140 Goombah, 15 Crystalys | Siege Construct | 35 到 45 分钟 |
| **Omega Vault** | 26 | 250 Seeker, 250 Phantasm, 200 Bulwark, 200 Goombah, 25 Crystalys | Omega Guardian | 50 到 60 分钟 |

- **Delta Siege**：第 18 波（250 Seeker）是可选的：倒计时期间你可以跳过它，它不发放任何东西
- **Omega Vault**：第 17 波（250 Seeker）是可选的：倒计时期间你可以跳过它，它不发放任何东西; 第 22 到 24 波是精英波，船体、护盾和伤害为 ×1.5

<!-- solo-waves:end -->

### Boss {#the-bosses}

Boss 是放大了的外星人飞船，有自己的船体、护盾和齐射，星门或世界的任何设置都不会改变它们。当 Boss 的船体降到表格中的数值时，一个阶段开始：它的护盾可能被重新设定，它的齐射或全部伤害会改变，并且它可能发动一个招式。每个招式都会预告：一个圆圈、一个圆环或你飞船上的标记会在落下前片刻显示。Boss 召唤的外星人不发放也不掉落任何东西。

<!-- solo-bosses:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Boss | 星门 | 船体 | 护盾 | 激光齐射 |
| :--- | :--- | ---: | ---: | ---: |
| **Enhanced Phantasm** | Alpha Rift | 330,000 | 530,000 | 5,700–7,000 |
| **Enhanced Bulwark** | Beta Breach | 690,000 | 170,000 | 4,500–5,500 |
| **Elite Crystalys** | Gamma Foundry | 620,000 | 250,000 | 3,800–4,700 |
| **Siege Construct** | Delta Siege | 1,150,000 | 1,730,000 | 3,400–4,200 |
| **Omega Guardian** | Omega Vault | 1,340,000 | 840,000 | 2,600–3,200 |

| Boss | 阶段 | 剩余船体 | 它会做什么 |
| :--- | :--- | :--- | :--- |
| **Enhanced Phantasm** | Enhanced Phantasm | 100% 到 0% | 它只开火。 |
| **Enhanced Bulwark** | Shielded | 100% 到 50% | 它的护盾被设为 Boss 自身护盾的 ×4。 |
|  | Second attack | 50% 到 0% | 它的齐射为 ×1.3。它向你发射 4 枚 Dormant Lance 火箭，每枚 61,000，每隔 0.5 秒 一枚，每 30 秒 一轮齐射。 |
| **Elite Crystalys** | Elite | 100% 到 50% | 它只开火。 |
|  | Reinforced | 50% 到 0% | 它的护盾被设为 Boss 自身护盾的 ×2。每 10 分钟 召唤 10 个 Goombah，最多同时存活 10 个；它们不发放也不掉落任何东西。 |
| **Siege Construct** | Siege Construct | 100% 到 0% | 每 1 分钟 降下 3 轮、每轮 8 颗的陨石，每颗对落点 420 单位内的一切造成 5,500，其中 50% 瞄准你；每个圆圈在落下前 3 秒 显示。它向你发射 6 枚 Dormant Lance 火箭，每枚 9,000，每隔 0.5 秒 一枚，每 1 分钟 一轮齐射。 |
| **Omega Guardian** | Shield Fortress | 100% 到 70% | 它的护盾被设为 Boss 自身护盾的 ×1.5。每 40 秒 召唤 6 个 Bulwark，最多同时存活 12 个；它们不发放也不掉落任何东西。 |
|  | Swarm Protocol | 70% 到 35% | 每 25 秒 召唤 12 个 Phantasm，最多同时存活 24 个；它们不发放也不掉落任何东西。每 30 秒，一次 140,000 的爆炸会击中 Boss 周围 700 单位内的一切；圆环在落下前 2 秒 显示。 |
|  | Overload | 35% 到 0% | 它的护盾被设为 Boss 自身护盾的 ×0.1。它的全部伤害为 ×2.5。在该阶段持续 2 分钟 之后，它的全部伤害再 ×2。每 25 秒，一次 28,000 的爆炸会击中 Boss 周围 700 单位内的一切；圆环在落下前 2 秒 显示。 |

<!-- solo-bosses:end -->

## 通关发放什么 {#what-a-clear-pays}

通关会在 Boss 死亡的那一刻**一次性**发放它的表格：信用点、Thulium、经验值和荣誉、矿石、装甲板和 Power Core，以及弹药。经验值会像地下城的一样计入你的 PvE 排名积分。

<!-- solo-pay:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| 星门 | 信用点 | Thulium | 经验值 | 荣誉 |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 450,000 | 5,000 | 70,000 | 1,000 |
| **Beta Breach** | 1,500,000 | 12,000 | 180,000 | 2,500 |
| **Gamma Foundry** | 4,000,000 | 25,000 | 400,000 | 5,500 |
| **Delta Siege** | 8,000,000 | 40,000 | 800,000 | 10,000 |
| **Omega Vault** | 15,000,000 | 60,000 | 1,500,000 | 20,000 |

- **Alpha Rift**：Ship Fragment ×300, Nyxite ×300, Daraxium ×400；弹药：Advanced Plasma ×20,000, Ultra Core ×5,000, Experimental Fusion Core ×20,000
- **Beta Breach**：Ship Fragment ×700, Nyxite ×750, Daraxium ×800, Cataclysite ×400, Quorvium ×100；弹药：Advanced Plasma ×50,000, Ultra Core ×20,000, Experimental Fusion Core ×30,000
- **Gamma Foundry**：Ship Fragment ×1,150, Nyxite ×1,000, Cataclysite ×900, Quorvium ×400, Power Core ×15；弹药：Advanced Plasma ×30,000, Ultra Core ×60,000, Experimental Fusion Core ×50,000
- **Delta Siege**：Ship Fragment ×2,000, Nyxite ×1,750, Cataclysite ×1,500, Quorvium ×1,000, Reinforced Hull Plate ×70, Power Core ×40, Ancient Control Unit ×3；弹药：Advanced Plasma ×40,000, Ultra Core ×90,000, Experimental Fusion Core ×75,000
- **Omega Vault**：Ship Fragment ×3,250, Nyxite ×2,750, Cataclysite ×2,250, Quorvium ×1,600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10；弹药：Advanced Plasma ×50,000, Ultra Core ×100,000, Experimental Fusion Core ×100,000

<!-- solo-pay:end -->

**Thulium 会被截断到一个上限。**星门返还的数额不得超过你在扫描上花费的 Thulium 的一定份额，按你所有的星门和所有的扫描合计（该份额见最上方的列表）。通关及其外星人超出该份额而本应发放的部分会被截断，结果界面会告诉你截断了多少。信用点、经验值、荣誉、矿石、装甲板和弹药永远不会被截断。

### 外星人 {#the-aliens}

你在星门中击杀的每个外星人，无论你在哪个世界飞行，都按它在 Alpha 的数字发放：世界倍率、增益和高级会员加成都不会改变它们。一波对它的外星人每局**只发放一次**，不管你离开再回来多少次。奖励在这一局每一段结束时到账：当你离开、死亡、生命用尽、放弃或通关时。只有重置，以及你在星门内时服务器重启，才会让一段中的击杀得不到发放（这一局仍保持开启，但那一段的击杀会丢失）。星门中的击杀不计入其他任何东西：不计入任务、击杀统计、成就计数器、击杀播报，也不计入你的无人机和 P.E.T. 的经验值。不过它们发放的经验值会像通关的经验值一样计入你的 PvE 排名积分。外星人的战利品随奖励一起直接进入你的背包。

<!-- solo-kills:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| 外星人 | 信用点 | Thulium | 经验值 | 荣誉 |
| :--- | ---: | ---: | ---: | ---: |
| **Seeker** | 1,000 | 4 | 100 | 2 |
| **Phantasm** | 3,000 | 12 | 300 | 6 |
| **Bulwark** | 5,000 | 25 | 800 | 10 |
| **Goombah** | 15,000 | 75 | 3,000 | 24 |
| **Crystalys** | 75,000 | 200 | 12,000 | 52 |

| 星门 | 信用点 | Thulium | 经验值 | 荣誉 |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 540,000 | 2,160 | 54,000 | 1,080 |
| **Beta Breach** | 1,320,000 | 5,980 | 186,000 | 2,520 |
| **Gamma Foundry** | 3,000,000 | 13,300 | 522,000 | 4,616 |
| **Delta Siege** | 4,975,000 | 21,400 | 829,000 | 7,640 |
| **Omega Vault** | 6,875,000 | 29,000 | 1,160,000 | 10,100 |

<!-- solo-kills:end -->

## 挑战与成就 {#challenges-and-achievements}

有两个可选挑战，任何一次通关都可以完成，每个发放一项成就，**不发放 Thulium**。**无死亡**通关是指在整局中、在你每一次进入加起来的范围内，一次也没有死亡的通关。**速通**是在星门最短的预计时间内通关，按你在竞技场内度过的时间计算。其余六项成就分别是通关每一座星门，以及五座全部通关：

<!-- solo-achievements:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **裂隙关闭**（普通）：单人通关 Alpha Rift。
- **缺口封堵**（优秀）：单人通关 Beta Breach。
- **铸造厂停工**（稀有）：单人通关 Gamma Foundry。
- **围攻告破**（稀有）：单人攻破 Delta Siege。
- **金库破解**（史诗）：单人破解 Omega Vault。
- **星门守护者**（传说）：通关全部五座单人星门：Alpha、Beta、Gamma、Delta 和 Omega。
- **毫发无伤**（稀有）：不损失任何一条生命，通关一座单人星门。
- **与时间赛跑**（稀有）：在最短时间内通关一座单人星门：从 Alpha 到 Omega 依次为 10、15、25、35 或 50 分钟。

<!-- solo-achievements:end -->

## 来自星门的物品 {#items-from-a-gate}

星门给你的东西是**可交易**的：矿石、装甲板、Power Core、弹药和外星人的战利品，可以像掉落物或任务奖励一样在[拍卖行](/wiki/03-Mechanics/Auction.md)挂单，例外情况与任何物品相同。没有部件的扫描所发放的奖品则不行：它们来自扫描，而不是来自星门。

## 星门与重置 {#gates-and-the-wipe}

- **重置会结束任何未结束的对局**，并把它的部件还给你。对局不会延续到下个赛季。
- **重置后保留：**五座单人星门的部件、保底的计数，以及你在扫描上的花费和星门返还金额的记录，所以 Thulium 的上限会跨赛季延续。成就永远属于你。
- **重置时丢失：**Chrono-Gate 的部件，和以前一样。你的扫描会把它们重新买回来。
- **删除账号**会删除部件、计数和记录。
