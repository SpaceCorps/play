<!-- wiki-i18n source: 9cb279aeecb3bbc8 -->
<!-- wiki-i18n title: 容器 -->
# 容器 {#containers}

<!-- wiki-search: 容器; container; containers; case; crate; lootbox; loot box; 盲盒; 概率; 爆率; 保底; pity; 转轮; 开启; 标本库; 铸造坩埚; 档案库; 勘测罐; 试剂架; odds; drop rate; vault; crucible; archive; canister; rack -->

**容器**是来自 Mission Control 的密封发现物。你开启一个容器时，服务器会从一张表中抽取一个奖励，这张表里每个奖励的概率都印在本页上。游戏中的容器页面显示的是同一张表。

> [!NOTE]
> **容器是在游戏中获得的随机奖励。它们从不出售，概率在这里公布。** 任何容器都不能购买、交易或赠送。

## 什么是容器 {#what-a-container-is}

- **靠获得。** 你在游戏中获得容器。它没有价格，也没有钥匙：商店不卖，其他地方也不卖。
- **只属于你。** 容器绑定在你的账号上。你不能交易它，不能送给朋友，也不能放到[拍卖行](/wiki/03-Mechanics/Auction.md)上；容器给出的任何东西同样不能放到那里。
- **对每位飞行员都一样。** 高级会员不会改变任何东西：不会增加开启次数，也不会提高概率。
- **重置后仍会保留。** 你没有开启的容器，在[重置](/wiki/03-Mechanics/Wipe-Timeline.md)到来时仍留在你的账号里。重置对奖励做了什么，见[重置](#the-wipe)。
- **在基地开启。** 你在停靠状态下，于容器页面开启容器。奖励由服务器在你按下“开启”时抽取，按下这个动作本身不会改变任何东西。真正起作用的内容见[奖励是怎样选出的](#how-a-prize-is-chosen)。

## 容器从哪里来 {#where-containers-come-from}

<!-- containers-sources:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

你可以通过以下方式获得容器：

- 来自游戏管理员
- 作为重置时军衔的奖励
- 在登录日历中
- 作为成就奖励

<!-- containers-sources:end -->

## 五种容器 {#the-five-containers}

<!-- containers-glance:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 容器 | 里面有什么 | 适合 | 重置时关闭 | 保底 | 最稀有的奖励 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **标本库 (Specimen Vault)** | 什么都有一点：信用点、Thulium、弹药、火箭、装备、板材、Dark Matter、增益和颜色 | 任何飞行员 | 从赛季第 30 天起 | 10 次开启内必出 稀有 或更高等级的奖励 | 60,000 Thulium; 12,000,000 信用点：各 0.100% |
| **铸造坩埚 (Foundry Crucible)** | 弹药、火箭、激光、增幅器、护盾电池、推进器和装备，以及 5 艘飞船 | 等级 5 及以上 | 从赛季第 30 天起 | 8 次开启内必出 稀有 或更高等级的奖励 | 飞船：Wraith：0.020% |
| **色彩档案库 (Chroma Archive)** | 只有外观：皮肤、颜色、尾焰效果和光环 | 任何飞行员 | 保持开放 | 12 次开启内必出 史诗 或更高等级的奖励 | Crystal Ice; Comet; Halo：各 0.667% |
| **勘测罐 (Survey Canister)** | Skylab 矿石、板材、Dark Matter、Cluster Chunks 和 Thulium | Skylab 核心 10 及以上 | 从赛季第 30 天起 | 8 次开启内必出 稀有 或更高等级的奖励 | 32 × Dark Matter Plate; 50,000 Thulium：各 0.150% |
| **试剂架 (Reagent Rack)** | 增益、EMP Charges、Energetic Walls 和弹药 | 等级 4 及以上 | 从赛季第 30 天起 | 10 次开启内必出 稀有 或更高等级的奖励 | **全光谱**; Cloaking CPU L：各 0.100% |

<!-- containers-glance:end -->

**适合**只是建议：游戏允许你在任何等级开启任何容器。

## 等级 {#grades}

每个奖励都有一个**等级**，是游戏稀有度用词中的一个。等级是抽取时最先决定的东西。在转轮上，它是奖励方块的边框，用颜色和形状表示，因此颜色永远不是唯一的标志。

| 等级 | 颜色 | 形状 |
| :--- | :--- | :--- |
| 普通 | 灰色 | 圆形 |
| 优秀 | 绿色 | 正方形 |
| 稀有 | 蓝色 | 菱形 |
| 史诗 | 紫色 | 六边形 |
| 神话 | 粉色 | 星形 |
| 传说 | 金色 | 王冠 |

每种容器对每个等级都有自己的概率，列在下面。你拥有什么，永远不会改变等级的概率。

## 标本库 (Specimen Vault) {#specimen-vault}

*Mission Control 的异星档案员会把所有无法归入单一领域的发现物封入编号库中，原封不动地送出。在飞行员打破封印之前，基地里没有人知道库里装着什么。*

### 各等级的概率 {#specimen-vault-grades}

<!-- containers-specimen-vault-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等级 | 概率 | 包含的奖励 |
| :--- | ---: | ---: |
| 普通 | 38.000% | 9 |
| 优秀 | 38.000% | 8 |
| 稀有 | 17.000% | 8 |
| 史诗 | 5.500% | 5 |
| 神话 | 1.300% | 4 |
| 传说 | 0.200% | 2 |

<!-- containers-specimen-vault-grades:end -->

### 所有奖励 {#specimen-vault-prizes}

<!-- containers-specimen-vault-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等级 | 奖励 | 概率 |
| :--- | :--- | ---: |
| 普通 | 50,000 信用点 | 5.000% |
| 普通 | 250 Thulium | 4.000% |
| 普通 | 10,000 × Standard Battery | 4.000% |
| 普通 | 500 × Advanced Plasma | 4.000% |
| 普通 | 250 × Ultra Core | 3.000% |
| 普通 | **火箭架 I**: 4 选 1，各 100 个，概率相同：Ember I, Lancet I, Rivet I, Scatter I | 6.000% |
| 普通 | **锻造粉尘**: 1,500 × Daraxium + 1,500 × Nyxite | 3.000% |
| 普通 | 4,000 × Ship Fragment | 3.000% |
| 普通 | 1 小时 Experience Booster | 6.000% |
| 优秀 | 150,000 信用点 | 6.000% |
| 优秀 | 750 Thulium | 6.000% |
| 优秀 | 750 × Ultra Core | 4.500% |
| 优秀 | 340 × Experimental Fusion Core | 4.000% |
| 优秀 | **火箭架 II**: 4 选 1，各 190 个，概率相同：Ember II, Lancet II, Rivet II, Scatter II | 6.000% |
| 优秀 | 10 × Velkonite Reinforced Plate | 4.000% |
| 优秀 | 1 小时 Laser Damage Booster I | 4.000% |
| 优秀 | **颜色样品**: 11 选 1，概率相同：Cobalt, Indigo, Violet, Magenta, Crimson, Ember, Sunset, Gold, Emerald, Jade, Teal | 3.500% |
| 稀有 | 400,000 信用点 | 2.500% |
| 稀有 | 2,000 Thulium | 2.500% |
| 稀有 | 10 × Dark Matter | 1.500% |
| 稀有 | **火箭架 III**: 4 选 1，各 400 个，概率相同：Ember III, Lancet III, Rivet III, Scatter III | 2.000% |
| 稀有 | 1,000 × Experimental Fusion Core | 1.500% |
| 稀有 | 9 × Orvium Reinforced Plate | 1.500% |
| 稀有 | 4 小时 Laser Damage Booster I | 1.500% |
| 稀有 | **一件 II 阶部件**: 4 选 1，概率相同：Absorption Shield Cell II, Capacity Shield Cell II, Impulse Thruster II, Momentum Thruster II | 4.000% |
| 史诗 | 1,200,000 信用点 | 1.200% |
| 史诗 | 6,000 Thulium | 1.200% |
| 史诗 | 30 × Dark Matter | 0.900% |
| 史诗 | 26 × Orvium Reinforced Plate | 0.900% |
| 史诗 | **一件 III 阶部件**: 5 选 1，概率相同：Absorption Shield Cell III, Capacity Shield Cell III, Impulse Thruster III, Momentum Thruster III, Starfire-III | 1.300% |
| 神话 | 18,000 Thulium | 0.400% |
| 神话 | 12 × Dark Matter Plate | 0.300% |
| 神话 | Helios Beam | 0.300% |
| 神话 | **一个 IV 阶增幅器**: 3 选 1，概率相同：Damage Amp IV, Crit Amp IV, Penetration Amp IV | 0.300% |
| 传说 | 60,000 Thulium | 0.100% |
| 传说 | 12,000,000 信用点 | 0.100% |

<!-- containers-specimen-vault-prizes:end -->

**颜色样品**会给出一种你尚未拥有的颜色。如果样品中的所有颜色你都已拥有，它会改为支付回收 Thulium（[重复与回收](#duplicates-and-salvage)）。

### 保底 {#specimen-vault-guarantee}

<!-- containers-specimen-vault-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **保底**：每 10 次开启内至少一次 稀有 或更高等级的奖励
- **没有保底时出 稀有 或更高等级奖励的概率**：24.000%
- **有保底时，多次开启的比例**：25.649%
- **由保底强制的开启**：2.170%
- **两次这样的奖励之间平均开启的次数**：3.899

<!-- containers-specimen-vault-guarantee:end -->

## 铸造坩埚 (Foundry Crucible) {#foundry-crucible}

*Dormant 的铸造厂冷却时，最后一炉还留在坩埚里：弹药、成品装备，以及在最深处的一具从未完工的船体。Mission Control 的工程师从废墟中切下坩埚，原封交给飞行员，因为没有人能说出哪一个里面有船体。*

### 各等级的概率 {#foundry-crucible-grades}

<!-- containers-foundry-crucible-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等级 | 概率 | 包含的奖励 |
| :--- | ---: | ---: |
| 普通 | 45.000% | 6 |
| 优秀 | 30.000% | 7 |
| 稀有 | 16.000% | 6 |
| 史诗 | 6.500% | 6 |
| 神话 | 2.200% | 5 |
| 传说 | 0.300% | 2 |

<!-- containers-foundry-crucible-grades:end -->

### 所有奖励 {#foundry-crucible-prizes}

<!-- containers-foundry-crucible-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等级 | 奖励 | 概率 |
| :--- | :--- | ---: |
| 普通 | 30,000 × Standard Battery | 7.000% |
| 普通 | 1,500 × Advanced Plasma | 7.000% |
| 普通 | 750 × Ultra Core | 7.000% |
| 普通 | 340 × Experimental Fusion Core | 5.000% |
| 普通 | **火箭架 I**: 4 选 1，各 300 个，概率相同：Ember I, Lancet I, Rivet I, Scatter I | 11.000% |
| 普通 | **激光套件**: Quantum Laser II + Damage Amp I + Crit Amp I + Penetration Amp I | 8.000% |
| 优秀 | 2,250 × Ultra Core | 4.500% |
| 优秀 | 1,020 × Experimental Fusion Core | 4.500% |
| 优秀 | **火箭架 II**: 4 选 1，各 560 个，概率相同：Ember II, Lancet II, Rivet II, Scatter II | 8.500% |
| 优秀 | Basic Shield Core | 4.500% |
| 优秀 | **II 阶增幅器三件套**: Damage Amp II + Crit Amp II + Penetration Amp II | 4.000% |
| 优秀 | Repair Drone IV | 3.900% |
| 优秀 | 飞船：Nomad | 0.100% |
| 稀有 | 1,800 × Experimental Fusion Core | 2.500% |
| 稀有 | **火箭架 III**: 4 选 1，各 500 个，概率相同：Ember III, Lancet III, Rivet III, Scatter III | 3.000% |
| 稀有 | Quantum Laser III | 2.400% |
| 稀有 | **一件 II 阶部件**: 4 选 1，概率相同：Absorption Shield Cell II, Capacity Shield Cell II, Impulse Thruster II, Momentum Thruster II | 4.500% |
| 稀有 | **一个 III 阶增幅器**: 3 选 1，概率相同：Damage Amp III, Crit Amp III, Penetration Amp III | 3.500% |
| 稀有 | 飞船：Paragon | 0.100% |
| 史诗 | **一个 III 阶电池或推进器**: 4 选 1，概率相同：Absorption Shield Cell III, Capacity Shield Cell III, Impulse Thruster III, Momentum Thruster III | 3.000% |
| 史诗 | Starfire-III | 1.200% |
| 史诗 | Heavy Shield Core | 1.200% |
| 史诗 | Cloaking CPU M | 1.000% |
| 史诗 | 飞船：Storm | 0.050% |
| 史诗 | 飞船：Ironclad | 0.050% |
| 神话 | Helios Beam | 0.600% |
| 神话 | **一个 IV 阶电池或推进器**: 4 选 1，概率相同：Absorption Shield Cell IV, Capacity Shield Cell IV, Impulse Thruster IV, Momentum Thruster IV | 0.700% |
| 神话 | **一个 IV 阶增幅器**: 3 选 1，概率相同：Damage Amp IV, Crit Amp IV, Penetration Amp IV | 0.480% |
| 神话 | Cloaking CPU L | 0.400% |
| 神话 | 飞船：Wraith | 0.020% |
| 传说 | **Helios 军械库**: Helios Beam + Damage Amp IV + Crit Amp IV + Penetration Amp IV | 0.150% |
| 传说 | 50,000 Thulium | 0.150% |

<!-- containers-foundry-crucible-prizes:end -->

表中列出了飞船及其基础概率。你已拥有的飞船永远不会出现，所以你自己的概率可能与这张表略有不同：见[飞船](#the-ships)。

### 保底 {#foundry-crucible-guarantee}

<!-- containers-foundry-crucible-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **保底**：每 8 次开启内至少一次 稀有 或更高等级的奖励
- **没有保底时出 稀有 或更高等级奖励的概率**：25.000%
- **有保底时，多次开启的比例**：27.781%
- **由保底强制的开启**：3.708%
- **两次这样的奖励之间平均开启的次数**：3.600

<!-- containers-foundry-crucible-guarantee:end -->

## 色彩档案库 (Chroma Archive) {#chroma-archive}

*Dormant 用带紫色纹路的紫黑色晶体建造，他们的档案员把色彩存放在薄玻璃片里，压到什么东西上就会把它重新涂色。每个色彩档案库都是一叠封好的玻璃片，由 Mission Control 的色彩师编入索引，在飞行员打开之前无人读过。*

色彩档案库先抽取等级，再从该等级中抽取一个你尚未拥有的外观，每个外观的概率相同。一个系列算一个奖励：它会给你该系列中你没有的所有皮肤。表中的概率适用于一个没有该等级任何外观的飞行员。随着你收集得越多，它会升高，因为留在抽取里的外观变少了。外观本身见[外观装饰](/wiki/06-Items/Cosmetics.md)。

### 各等级的概率 {#chroma-archive-grades}

<!-- containers-chroma-archive-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等级 | 概率 | 包含的外观 |
| :--- | ---: | ---: |
| 普通 | 6.000% | 1 |
| 优秀 | 50.000% | 14 |
| 稀有 | 30.000% | 8 |
| 史诗 | 12.000% | 12 |
| 神话 | 2.000% | 3 |
| 传说 | 0.000% | – |

<!-- containers-chroma-archive-grades:end -->

### 所有奖励 {#chroma-archive-prizes}

<!-- containers-chroma-archive-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等级 | 外观 | 你没有该等级任何外观时的概率 |
| :--- | :--- | ---: |
| 普通 | Glow（光环） | 6.000% |
| 优秀 | Company Supporter（系列） | 3.571% |
| 优秀 | Cobalt（颜色） | 3.571% |
| 优秀 | Indigo（颜色） | 3.571% |
| 优秀 | Violet（颜色） | 3.571% |
| 优秀 | Magenta（颜色） | 3.571% |
| 优秀 | Crimson（颜色） | 3.571% |
| 优秀 | Ember（颜色） | 3.571% |
| 优秀 | Sunset（颜色） | 3.571% |
| 优秀 | Gold（颜色） | 3.571% |
| 优秀 | Emerald（颜色） | 3.571% |
| 优秀 | Jade（颜色） | 3.571% |
| 优秀 | Teal（颜色） | 3.571% |
| 优秀 | Twin（尾焰效果） | 3.571% |
| 优秀 | Breath（光环） | 3.571% |
| 稀有 | Nature White（系列） | 3.750% |
| 稀有 | Sunrise Orbit（系列） | 3.750% |
| 稀有 | Seeker Burnt（颜色） | 3.750% |
| 稀有 | Pirate Brick（颜色） | 3.750% |
| 稀有 | Pulse（尾焰效果） | 3.750% |
| 稀有 | Helix（尾焰效果） | 3.750% |
| 稀有 | Motes（光环） | 3.750% |
| 稀有 | Shimmer（光环） | 3.750% |
| 史诗 | Midnight Gala（系列） | 1.000% |
| 史诗 | Blue Marble（系列） | 1.000% |
| 史诗 | Mimosa（系列） | 1.000% |
| 史诗 | Olive Branch（系列） | 1.000% |
| 史诗 | Steady Pulse（系列） | 1.000% |
| 史诗 | Hollow Night（系列） | 1.000% |
| 史诗 | Dormant Void（颜色） | 1.000% |
| 史诗 | Ancient Amethyst（颜色） | 1.000% |
| 史诗 | Embers（尾焰效果） | 1.000% |
| 史诗 | Gradient（尾焰效果） | 1.000% |
| 史诗 | Sparkle（光环） | 1.000% |
| 史诗 | Wreath（光环） | 1.000% |
| 神话 | Crystal Ice（颜色） | 0.667% |
| 神话 | Comet（尾焰效果） | 0.667% |
| 神话 | Halo（光环） | 0.667% |

<!-- containers-chroma-archive-prizes:end -->

### 保底 {#chroma-archive-guarantee}

<!-- containers-chroma-archive-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **保底**：每 12 次开启内至少一次 史诗 或更高等级的奖励
- **没有保底时出 史诗 或更高等级奖励的概率**：14.000%
- **有保底时，多次开启的比例**：16.740%
- **由保底强制的开启**：3.186%
- **两次这样的奖励之间平均开启的次数**：5.974

<!-- containers-chroma-archive-guarantee:end -->

## 勘测罐 (Survey Canister) {#survey-canister}

*勘测探针从 Skylab 飞入宇宙地图的迷雾，每一枚都带着一罐密封的岩芯样本返回。有来自无人测绘矿脉的矿石、异常现象，偶尔还有比地图更古老的某种东西的碎块：Mission Control 按单元归档这个罐子，把解读留给 Skylab 的主人。*

### 各等级的概率 {#survey-canister-grades}

<!-- containers-survey-canister-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等级 | 概率 | 包含的奖励 |
| :--- | ---: | ---: |
| 普通 | 45.000% | 8 |
| 优秀 | 30.000% | 7 |
| 稀有 | 16.000% | 6 |
| 史诗 | 6.500% | 5 |
| 神话 | 2.200% | 3 |
| 传说 | 0.300% | 2 |

<!-- containers-survey-canister-grades:end -->

### 所有奖励 {#survey-canister-prizes}

<!-- containers-survey-canister-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等级 | 奖励 | 概率 |
| :--- | :--- | ---: |
| 普通 | 240 × Velkonite（进入 Skylab） | 7.000% |
| 普通 | 160 × Orvium（进入 Skylab） | 7.000% |
| 普通 | 1,300 × Reinforced Hull Plate | 5.000% |
| 普通 | 9,000 × Ship Fragment | 6.000% |
| 普通 | **锻造晶体**: 4,000 × Cataclysite + 3,000 × Quorvium | 5.000% |
| 普通 | 450 × Power Core | 5.000% |
| 普通 | 450 Thulium | 5.000% |
| 普通 | 4 × Regular Cluster Chunk | 5.000% |
| 优秀 | 780 × Velkonite（进入 Skylab） | 5.000% |
| 优秀 | 510 × Orvium（进入 Skylab） | 5.000% |
| 优秀 | 19 × Velkonite Reinforced Plate | 4.000% |
| 优秀 | 7 × Dark Matter | 5.000% |
| 优秀 | 8 × Ancient Control Unit | 3.000% |
| 优秀 | 1,450 Thulium | 4.000% |
| 优秀 | 3 × Mythical Cluster Chunk | 4.000% |
| 稀有 | 17 × Dark Matter | 3.500% |
| 稀有 | 15 × Orvium Reinforced Plate | 3.000% |
| 稀有 | 1,900 × Velkonite（进入 Skylab） | 2.500% |
| 稀有 | 1,230 × Orvium（进入 Skylab） | 2.500% |
| 稀有 | 2 × Legendary Cluster Chunk | 1.500% |
| 稀有 | 3,500 Thulium | 3.000% |
| 史诗 | 45 × Dark Matter | 1.500% |
| 史诗 | 39 × Orvium Reinforced Plate | 1.200% |
| 史诗 | **混合板材箱**: 60 × Velkonite Reinforced Plate + 20 × Orvium Reinforced Plate | 1.200% |
| 史诗 | 9,000 Thulium | 1.500% |
| 史诗 | 6 × Dark Matter Plate | 1.100% |
| 神话 | 13 × Dark Matter Plate | 0.900% |
| 神话 | 20,000 Thulium | 0.800% |
| 神话 | 100 × Dark Matter | 0.500% |
| 传说 | 32 × Dark Matter Plate | 0.150% |
| 传说 | 50,000 Thulium | 0.150% |

<!-- containers-survey-canister-prizes:end -->

标有*（进入 Skylab）*的矿石会进入你的 Skylab 矿石库，数量以你的资源仓库所能容纳为限。其余的会作为同样的矿石进入你的背包。见 [Skylab](/wiki/03-Mechanics/Skylab.md)。

### 保底 {#survey-canister-guarantee}

<!-- containers-survey-canister-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **保底**：每 8 次开启内至少一次 稀有 或更高等级的奖励
- **没有保底时出 稀有 或更高等级奖励的概率**：25.000%
- **有保底时，多次开启的比例**：27.781%
- **由保底强制的开启**：3.708%
- **两次这样的奖励之间平均开启的次数**：3.600

<!-- containers-survey-canister-guarantee:end -->

## 试剂架 (Reagent Rack) {#reagent-rack}

*Skylab 的研究中心用试剂安瓿蒸馏出你飞行时用的增益，而试剂架就是一批被中途打断后剩下的东西：每种试剂一份定量，各装在自己的密封安瓿里。药量只在飞船飞行时才会变质，所以试剂架想在架子上放多久都行。*

### 各等级的概率 {#reagent-rack-grades}

<!-- containers-reagent-rack-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等级 | 概率 | 包含的奖励 |
| :--- | ---: | ---: |
| 普通 | 45.000% | 5 |
| 优秀 | 33.000% | 8 |
| 稀有 | 15.000% | 8 |
| 史诗 | 5.500% | 6 |
| 神话 | 1.300% | 2 |
| 传说 | 0.200% | 2 |

<!-- containers-reagent-rack-grades:end -->

### 所有奖励 {#reagent-rack-prizes}

<!-- containers-reagent-rack-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等级 | 奖励 | 概率 |
| :--- | :--- | ---: |
| 普通 | 1 小时 Experience Booster | 11.000% |
| 普通 | 1 小时 Honor Booster | 11.000% |
| 普通 | 1 小时 Shield Regen Booster | 9.000% |
| 普通 | Energetic Wall I | 8.000% |
| 普通 | 500 × Advanced Plasma | 6.000% |
| 优秀 | 1 小时 Laser Damage Booster I | 5.000% |
| 优秀 | 1 小时 Shield Wall Booster I | 5.000% |
| 优秀 | 1 小时 Hull Plating Booster I | 5.000% |
| 优秀 | 1 小时 Resource Magnet Booster | 3.500% |
| 优秀 | 2 小时 Experience Booster | 4.500% |
| 优秀 | 2 小时 Honor Booster | 3.500% |
| 优秀 | EMP Charge | 3.500% |
| 优秀 | 3 × Energetic Wall I | 3.000% |
| 稀有 | 2 小时 Laser Damage Booster I | 2.500% |
| 稀有 | 2 小时 Shield Wall Booster I | 2.000% |
| 稀有 | 2 小时 Hull Plating Booster I | 2.000% |
| 稀有 | 4 小时 Experience Booster | 2.000% |
| 稀有 | 4 小时 Honor Booster | 2.000% |
| 稀有 | 2 小时 Loot Luck Booster | 1.500% |
| 稀有 | 3 × EMP Charge | 2.000% |
| 稀有 | 2 小时 Resource Magnet Booster | 1.000% |
| 史诗 | 4 小时 Laser Damage Booster I | 1.200% |
| 史诗 | 4 小时 Shield Wall Booster I | 1.000% |
| 史诗 | 4 小时 Hull Plating Booster I | 1.000% |
| 史诗 | 4 小时 Resource Magnet Booster | 0.700% |
| 史诗 | 4 小时 Loot Luck Booster | 0.900% |
| 史诗 | 8 × EMP Charge | 0.700% |
| 神话 | **战斗架**: 4 小时 Laser Damage Booster I + 4 小时 Shield Wall Booster I + 4 小时 Hull Plating Booster I | 0.700% |
| 神话 | **学者架**: 4 小时 Experience Booster + 4 小时 Honor Booster + 4 小时 Resource Magnet Booster + 4 小时 Loot Luck Booster | 0.600% |
| 传说 | **全光谱**: 4 小时 Laser Damage Booster I + 4 小时 Shield Wall Booster I + 4 小时 Hull Plating Booster I + 4 小时 Shield Regen Booster + 4 小时 Experience Booster + 4 小时 Honor Booster + 4 小时 Resource Magnet Booster + 4 小时 Loot Luck Booster | 0.100% |
| 传说 | Cloaking CPU L | 0.100% |

<!-- containers-reagent-rack-prizes:end -->

增益时间会加到已在运行的同一个增益上，并且只在你飞行时才会倒计时。见[增益](/wiki/06-Items/Boosters.md)。

### 保底 {#reagent-rack-guarantee}

<!-- containers-reagent-rack-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **保底**：每 10 次开启内至少一次 稀有 或更高等级的奖励
- **没有保底时出 稀有 或更高等级奖励的概率**：22.000%
- **有保底时，多次开启的比例**：24.001%
- **由保底强制的开启**：2.565%
- **两次这样的奖励之间平均开启的次数**：4.167

<!-- containers-reagent-rack-guarantee:end -->

## 奖励是怎样选出的 {#how-a-prize-is-chosen}

你开启容器时，服务器分三步选择：

1. **等级。** 用一个随机数与各等级的概率对照。
2. **奖励。** 用第二个数与该等级中各奖励的概率对照。你已拥有的飞船不在其中（见[飞船](#the-ships)）。
3. **在相同概率中选择。** 写着*几选一*的奖励会给出其中一个，每个的概率相同。

这些数来自服务器操作系统的随机数生成器，并且在你的容器被取走之后才抽取。你发送的任何东西都无法改变它们：按钮、时间都不行。

此前的两样东西确实会起作用。保底计数器会从一次开启带到下一次，上面各容器的保底部分有说明。另外，你已拥有的东西（包括你在之前开启中赢得的）会改变抽取中还剩下哪些奖励：你已拥有的飞船不在其中，只要该等级里还有你没有的外观，你已拥有的外观就不会被抽到（见[重复与回收](#duplicates-and-salvage)和[飞船](#the-ships)）。你拥有什么，永远不会改变各等级的概率。

<!-- containers-draw:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- 每个概率都是 100,000 份中的整数份。1 份是 0.001%。

<!-- containers-draw:end -->

**每次开启都会被记录**，包括它的种子（服务器所用的随机数）、抽到的数、所抽取的表的哈希，以及你已拥有的东西从抽取中去掉的奖励。你可以在容器页面的**记录**里的**详情**下读到它们。

**你也可以自己核对一次。** 游戏源码中的工具 `scripts/containers-verify.py` 会读取表和一次开启的详情，并告诉你等级、奖励和选择是否由种子推出。方法很短：

```text
stream(seed, id): value i, for i = 0, 1, 2, ...
  = the first 8 bytes (big endian) of HMAC-SHA256(
      key     = seed,
      message = "sc-container-v1|" + id + "|" + i )
  where i is written as 4 bytes, big endian
below(n): take values until one is under 2^64 - (2^64 mod n),
  then use it modulo n (no modulo bias)
grade:    roll = below(total of the grades in play);
  the grade is the first whose running sum is above the roll
prize:    sub = below(total of the prizes left in that grade);
  the prize is the first whose running sum is above sub
choice:   a prize that is "one of N" gives the alternative
  number below(N)
seed = the 32 bytes shown under Details; id = the container's id.
When the guarantee forces an opening, only the guaranteed grade
and better are in play.
```

## 重复与回收 {#duplicates-and-salvage}

- 只要该等级里还有你没有的外观，你已拥有的**外观**就不会被抽到。当你拥有一个系列的所有皮肤时，该系列算作已拥有。
- 当你拥有该等级的所有外观时，奖励会改为支付**回收**：按等级计算的 Thulium。对保底来说，它算作该等级的奖励。
- **物品**永远不会被换成 Thulium：它们会叠加，或原样送达。
- **飞船**永远不会给两次，也不会作为回收支付（见[飞船](#the-ships)）。

<!-- containers-salvage:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等级 | Thulium |
| :--- | ---: |
| 普通 | 25 |
| 优秀 | 100 |
| 稀有 | 400 |
| 史诗 | 1,200 |
| 神话 | 4,000 |

<!-- containers-salvage:end -->

## 飞船 {#the-ships}

铸造坩埚可能装有一艘飞船。表中列出了这些飞船及其**基础概率**，即一个没有其中任何一艘的飞行员的概率。这些就是公布的概率。

你已拥有的飞船永远不会出现。它会从抽取中去掉，它的份额按各自的概率比例分给同一等级的其他奖励。所以你拥有什么会改变你自己的概率：该等级其他奖励的概率会略高一点。各等级的概率永远不变，保底也不变。用某艘飞船做成的设计，算作拥有这艘飞船：一艘 Paragon THUNDER 算作拥有 Paragon。

<!-- containers-ships:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 飞船 | 等级 | 概率 |
| :--- | :--- | ---: |
| Nomad | 优秀 | 0.100% |
| Paragon | 稀有 | 0.100% |
| Storm | 史诗 | 0.050% |
| Ironclad | 史诗 | 0.050% |
| Wraith | 神话 | 0.020% |
| **全部 5 艘** | | **0.320%** |

例子：你已拥有飞船 Nomad。优秀 等级的概率不变，但该等级 30,000 份中这艘飞船（Nomad）的 100 份会从抽取中去掉，因此 优秀 等级的其他奖励都是表中概率的 30,000 / 29,900 = 1.0033 倍。

下一张表适用于你拥有该等级全部飞船的情况。如果你只拥有其中一部分，只有这些飞船的份数会从抽取中去掉，倍数会更小。

| 等级 | 等级的份数 | 其全部飞船的份数 | 该等级其他奖励的概率提高的倍数 |
| :--- | ---: | ---: | ---: |
| 优秀 | 30,000 | 100 | ×1.0033 |
| 稀有 | 16,000 | 100 | ×1.0063 |
| 史诗 | 6,500 | 100 | ×1.0156 |
| 神话 | 2,200 | 20 | ×1.0092 |

例子：史诗 等级有 2 艘飞船。如果你只拥有飞船 Storm，该等级 6,500 份中只有它的 50 份会从抽取中去掉，因此 史诗 等级的其他奖励是表中概率的 6,500 / 6,450 = 1.0078 倍，而不是 1.0156 倍。

<!-- containers-ships:end -->

游戏中的容器页面会在你自己的概率与公布概率不同时，把它们并排显示。你已拥有的飞船仍留在列表中，显示为灰色，并带有一行“你已拥有这艘飞船，所以它不会从容器里出现。”

## 重置 {#the-wipe}

- **未开启的容器会保留。** 它们在重置后仍留在你的账号里。
- **容器给出的物品是普通物品。** 重置时，除非你放进运输储藏库带走，否则它们会丢失（[重置时间线](/wiki/03-Mechanics/Wipe-Timeline.md)）。
- **外观和飞船会留在你身边**，和任何外观、任何飞船一样。信用点、Thulium 和增益的剩余时间在重置时各按自己的规则处理。
- **容器给出的任何东西都不能放到拍卖行。**

<!-- containers-wipe:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **从赛季第 30 天起关闭**：标本库, 铸造坩埚, 勘测罐, 试剂架。里面的东西会在重置时丢失，所以在重置结束前无法开启。
- **横幅**：容器页面会从赛季第 28 天起提醒你。
- **保持开放**：色彩档案库。里面只有外观，而重置会保留外观。

<!-- containers-wipe:end -->

## 表的版本 {#version-of-the-table}

本页的每个概率都来自游戏服务器上的表。当某个概率改变时，表会获得新的版本和新的哈希，并且每次开启都会记录它所抽取的表的哈希。

<!-- containers-version:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **表的版本**：1
- **表的哈希（前 12 个字符）**：`23aa20f1a5ad`

更改内容：

- 版本 1：首次公布的表。

<!-- containers-version:end -->
