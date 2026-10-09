<!-- wiki-i18n source: bc32fd762bb7742c -->
<!-- wiki-i18n title: 小行星采矿 -->
# 小行星采矿 {#asteroid-mining}

**小行星**是躺在企业星区和危险星区飞行平面上的大块岩石。它们从不移动，也从不开火。用**火箭**或**激光**击碎一颗，它就会炸成含有信用点、Thulium 和矿石的小**碎块**，你可以像拾取[货物](/wiki/03-Mechanics/Cargo.md)一样捡起它们。火箭才是干这件事的工具：激光也能伤害小行星，但只有对飞船伤害的 5%，无人机则对它毫无作用。

采矿和狩猎是两种不同的工作，前者替代不了后者：它不给经验值、荣誉或排名点数，而且你发射的火箭要花费信用点或 Thulium。它给你的是信用点和 Thulium、不用战斗就能得到的[锻造炉](/wiki/06-Items/Forge.md)和制造所需的矿石，以及一份[小队](/wiki/03-Mechanics/Groups.md)可以分着做的工作。它报酬丰厚：按游戏自己的模型，在合适的小行星上用合适的火箭采一小时，扣除火箭成本后，大约相当于你等级上最佳狩猎一小时的 2.6 到 6.8 倍。每日上限（见[世界](#the-worlds)）给它封了顶，而且你很快就会碰到：在 Alpha，稳定采矿的飞行员在好星区不到 2 小时就能达到 Thulium 上限，大约 2.7 小时就能达到信用点上限。

## 什么是小行星 {#what-an-asteroid-is}

- **与舰船同高。** 小行星躺在飞行平面上，画在每艘从上方飞过的舰船、火箭和碎块后面，并留在原地。没有任何东西会与它碰撞：舰船、外星人和火箭都会穿过它。每颗小行星都按真实比例绘制，所以 Motherlode 和 Prism Cluster 是高高耸立的，而不是被压扁的。地图远处后方暗淡的岩石只是背景：打不到它们，里面也什么都没有。
- **一个种类和一个系列。** 每颗小行星都是[种类](#the-kinds)中的一种，每个种类属于一个说明它性质的系列。小行星的光芒说明它里面有什么。地面上的**单环**标记普通小行星，**双环**标记有装甲的，**虚线环**标记易碎的。
- **在小地图上。** 星区里的每颗小行星都是一个与其种类同色的小六边形，被击中前是空心的，之后变成实心；碎块是小圆点。
- **目标窗口。** 点击一颗小行星即可选中它。选中小行星上的圆圈会在你绕着它飞行时一直留在它身上：点击空白处或紧挨着小行星的地方，只会让你的舰船飞过去，按 Esc 或目标窗口里的叉号则会松开它。窗口显示它的名称、系列和大小、船体、**装甲**和**爆炸**徽章、你手中这种火箭大约需要多少枚以及你的激光大约需要多少轮齐射、它在你的世界里碎裂后会留下什么，以及谁造成了多少伤害。选中小行星不会改变你舰船或外星人的目标，所以你的激光保持锁定。

## 击碎一颗小行星 {#breaking-one}

1. **瞄准它。** 点击小行星将其选中：你的火箭随后会飞向它。直射火箭（Rivet、Scatter）则改为飞向光标下的小行星，前提是光标下没有同时也有舰船或外星人（小行星边缘外一小段也算，小地图上它的六边形同样算）。没有选中小行星时，制导火箭（Lancet、Ember）只有在你没有选中舰船或外星人时，才会飞向光标下的小行星，所以在小行星旁战斗的猎手会继续朝外星人开火。没有小行星可飞的火箭就是普通火箭，会穿过所有小行星。
2. **发射。** 商店的十二种[火箭](/wiki/06-Items/Rockets.md#the-twelve-rockets)都可以用，N.U.K.E. 也可以。制导火箭需要小行星位于其锁定范围内，直射火箭需要位于其飞行射程内，都量到小行星的中心。两者都飞向中心，所以光标落在小行星的哪个位置都没有关系。[N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) 无法伤害小行星。
3. **继续发射。** 所有火箭共用同一个重新装填计时器，每枚火箭花多少就是多少：火箭就是这份工作的成本。

- **火箭只命中它所瞄准的那颗小行星。** 它会穿过路上其他所有小行星和舰船，而没有瞄准小行星发射的火箭会穿过所有小行星。当你的一枚火箭在一颗它没有瞄准的小行星旁结束时，游戏会告诉你原因。范围火箭的爆炸仍会像在别处一样伤害它波及的每艘舰船；爆炸范围内的其他小行星不受影响。
- **激光只能造成少量伤害，无人机毫无作用。** 选中小行星后，双击它，或按攻击键，或按弹药槽位：只要它的中心在你的激光射程内，你的激光就会每秒向它开火一次，并像对飞船开火那样消耗弹药。双击总是向小行星开火；攻击键和弹药槽位则在没有选中飞船或外星人时才这样做。Siphon 弹药只会吸取护盾，所以无法伤害小行星，这样的命令会被拒绝。
- **伤害。** 火箭从小行星的船体上扣除它自己的随机值，你的[无人机编队](/wiki/03-Mechanics/Formations.md)的火箭加成与对飞船时一样计入（Ballista 的 +55% 也一样）；你的激光、增幅器、增益道具和弹药不会改变火箭的随机值。一轮激光齐射扣除它对没有护盾的飞船所造成伤害的 5%，并计入你的增幅器、增益道具、弹药、暴击和编队。加成先算：**有装甲**的小行星随后每次命中都会扣除装甲的点数，范围爆炸对**易碎**的水晶小行星伤害更大（数字见“规则”和“种类”）。小行星没有护盾，也不会自愈：你打伤的岩石会一直带着伤，直到有人把它击碎。
- **需要几枚。** 每个种类都是为某一种火箭设计的，“种类”会写出大约需要多少枚才能击碎；目标窗口和悬停卡片会按你手中的火箭告诉你，并在旁边告诉你大约需要多少轮激光齐射。更强的世界意味着更大的船体（“世界”）。当别人击碎小行星时，你正在飞行中的火箭会作为普通火箭继续飞行，白白浪费。

## 击碎之后留下什么 {#what-a-break-leaves}

小行星碎裂的那一刻不会支付任何东西。它炸成碎屑，抛出几块**碎块**：信用点是小金块，Thulium 是薰衣草色的水晶，矿石是粗糙的石头。它们从碎屑里漂出来，像任何[货箱](/wiki/03-Mechanics/Cargo.md)一样上下浮动：点击一块，你的舰船就会飞过去，拾取要走它短短的一段读条，和任何货箱一样（[拾取](/wiki/03-Mechanics/Cargo.md#collecting)）。矿石进入你的机库物品栏，信用点和 Thulium 进入你的账户，弹出的提示会告诉你得到了什么。

更大的小行星会留下更多块（“种类”里的“钱币碎块”一列：信用点和 Thulium 会分成这么多块，矿石再多一块）。拾取之后，你的舰船会自己前往附近小行星上你可以拿的下一块碎块；你下达任何移动命令都会让它停下。

## 谁拿到碎块 {#who-gets-the-chunks}

小行星是共同的工作：任意数量的飞行员都可以用火箭或激光击打它，碎块按每个人造成的伤害分配，而不是看谁先开火或最后开火。目标窗口的伤害栏会显示谁造成了多少，以及你到来之前已经造成了多少。一次击碎的信用点和 Thulium 只抽取一次，按伤害分配；矿石由造成伤害最多的几名飞行员分，稀有产出归造成伤害最多的那一位。造成的伤害不到“规则”里那个比例的飞行员什么也拿不到，游戏日志会这样告诉他。碎块会为每位获得报酬的飞行员各放一份，在一段时间内为他和他的战队保留，之后对所有人开放。

## 规则 {#the-rules}

<!-- asteroids-rules:begin -->
<!-- Generated from server/Resources/Asteroids.json (and Rockets.json) by scripts/asteroids-wiki.sh: don't edit by hand. -->

- 对一颗小行星造成了至少 5% 伤害的飞行员，按造成的伤害比例分得它的碎块。若无人达到 5%，造成伤害最多的飞行员拿走全部。
- [小队](/wiki/03-Mechanics/Groups.md#sharing-kills)算作一名飞行员，它的份额按等级分给附近正在开火的队友。
- 一次击碎产生的碎块会为放置它们的那位飞行员和他的战队保留 30 秒。之后地图上的任何人都可以拿。无人拾取的碎块在 3 分钟后消失。
- 一张地图最多容纳 36 块碎块，包含在它能容纳的 64 个货箱之内：碎块不会挤走外星人的货箱，那些货箱也不会挤走碎块。当地图上没有地方放碎块时，它原本属于的那位飞行员会立刻拿到报酬。
- 信用点和 Thulium 在拾取碎块时支付，而不是在小行星碎裂时。在任意 24 小时内，一名飞行员最多拿到[世界](#the-worlds)里的上限：超出上限的碎块会被用掉，只支付上限之下剩下的部分，游戏日志会这样告诉你。
- 报酬对所有人都一样：没有任何高级会员加成、赛季商店增益、战队增益、Loot Luck 或增益道具会改变信用点、Thulium 或产出。[Resource Magnet Booster](/wiki/06-Items/Boosters.md) 会在你拾取矿石碎块时增加其中的资源，和对任何货箱一样。
- 装甲会从每次命中中扣掉它的点数，但一次命中至少有 20% 总会穿过。
- 范围爆炸对易碎的小行星造成的伤害是对其他小行星的 1.6 倍。
- 小行星从不出现在离安全环边缘 1,500 单位、离黑洞中心 4,200 单位或离地图边缘 600 单位以内的地方，也从不出现在离任何飞行员 1,200 单位以内的地方。
- 击碎之后，同种类的小行星会在地图上的另一处，经过该星区那一行所写的时间后重新长出来，前后浮动 25%。
- Motherlode 无论在哪个星区，都会在 1 小时后回来。

<!-- asteroids-rules:end -->

## 世界 {#the-worlds}

每个世界，Alpha、Beta 和 Gamma，在相同的位置都有各自的小行星（[世界](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)），所以你在自己世界里击碎的小行星，在别的世界里并没有被击碎。更大的世界意味着更大的船体和更高的报酬。

<!-- asteroids-worlds:begin -->
<!-- Generated from server/Resources/Asteroids.json (and Rockets.json) by scripts/asteroids-wiki.sh: don't edit by hand. -->

| 世界 | 船体 | 奖励倍率 | Thulium 上限 | 信用点上限 |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha** | ×1 | ×1 | 3,000 | 13,000,000 |
| **Beta** | ×1.5 | ×2 | 4,500 | 18,000,000 |
| **Gamma** | ×2 | ×3 | 6,000 | 21,000,000 |

下面的表给出的是 Alpha 小行星的数字。**船体**是世界对每颗小行星船体的倍率，**奖励倍率**是它对一次击碎的信用点和 Thulium 的倍率；矿石和稀有产出在每个世界里都一样。两个上限是一名飞行员在任意 24 小时内通过碎块最多能拿到的数量。

<!-- asteroids-worlds:end -->

## 它们在哪里 {#where-they-are}

三个企业的所有母星区和危险星区都有小行星，各有自己的组合：主要是它所在环的种类，再加上一两种来自上一环或下一环的“客人”。没有传送门通往的中立星区没有小行星。危险星区的小行星从表中的赛季日开始出现，也就是 PvP 开启的那一天（[初次接触](/wiki/03-Mechanics/Wipe-Timeline.md)），其余的从第一天起就有。击碎之后，同种类的新小行星会在该星区那一行所写的时间后重新长出来。从赛季第 11 天起，脉冲星、巨型挖掘机和 Dormant Swamp 中心附近没有小行星（[危险星区](/wiki/01-General/Danger-Sectors.md#where-everything-is)），活动 2 开始时在那里的岩石会消失。

<!-- asteroids-maps:begin -->
<!-- Generated from server/Resources/Asteroids.json (and Rockets.json) by scripts/asteroids-wiki.sh: don't edit by hand. -->

| 星区 | 小行星 | 起始日 | 回归 | 种类 |
| :--- | ---: | ---: | ---: | :--- |
| `M-1` | 12 | 1 | 2 分钟 | 3 × Pebble, 3 × Cobble, 2 × Glimmer, 2 × Cache Pod, 2 × Ironhide |
| `T-1` | 12 | 1 | 2 分钟 | 3 × Rime, 3 × Cache Pod, 2 × Cobble, 2 × Pebble, 2 × Dark Chondrite |
| `G-1` | 12 | 1 | 2 分钟 | 4 × Glimmer, 2 × Pebble, 2 × Rime, 2 × Cobble, 2 × Nyx Geode |
| `M-2` | 14 | 1 | 3 分钟 | 4 × Ironhide, 3 × Dark Chondrite, 3 × Scrap Hulk, 2 × Vein Rock, 1 × Cobble, 1 × Pebble |
| `T-2` | 14 | 1 | 3 分钟 | 4 × Scrap Hulk, 3 × Dark Chondrite, 3 × Vein Rock, 2 × Nyx Geode, 2 × Rime |
| `G-2` | 14 | 1 | 3 分钟 | 4 × Nyx Geode, 3 × Vein Rock, 3 × Dark Chondrite, 2 × Ironhide, 2 × Glimmer |
| `M-3` | 16 | 1 | 5 分钟 | 3 × Plateback, 3 × Slag Block, 3 × Lode Rock, 3 × Cataclast, 2 × Derelict Hulk, 2 × Cataclysite Mass |
| `T-3` | 16 | 1 | 5 分钟 | 3 × Derelict Hulk, 3 × Slag Block, 3 × Cataclast, 3 × Lode Rock, 2 × Thulium Geode, 2 × Derelict Cruiser |
| `G-3` | 16 | 1 | 5 分钟 | 4 × Cataclast, 3 × Slag Block, 3 × Thulium Geode, 2 × Plateback, 2 × Lode Rock, 2 × Quorvium Boulder |
| `M-4` | 18 | 1 | 5 分钟 | 4 × Anvil, 4 × Cataclysite Mass, 4 × Quorvium Boulder, 2 × Derelict Cruiser, 2 × Vault Rock, 2 × Plateback |
| `T-4` | 18 | 1 | 5 分钟 | 4 × Derelict Cruiser, 4 × Quorvium Boulder, 4 × Cataclysite Mass, 2 × Thulium Cluster, 2 × Vault Rock, 2 × Thulium Geode |
| `G-4` | 18 | 1 | 5 分钟 | 5 × Quorvium Boulder, 3 × Cataclysite Mass, 3 × Anvil, 3 × Lode Rock, 2 × Thulium Cluster, 2 × Vault Rock |
| `DS-1` | 24 | 4 | 5 分钟 | 8 × Rich Lode, 6 × Prism Cluster, 4 × Ancient Husk, 3 × Star Crystal, 2 × Vault Rock, 1 × Motherlode |
| `DS-2` | 24 | 4 | 5 分钟 | 7 × Rich Lode, 7 × Ancient Husk, 3 × Star Crystal, 3 × Anvil, 3 × Derelict Cruiser, 1 × Motherlode |
| `DS-3` | 24 | 4 | 5 分钟 | 9 × Prism Cluster, 5 × Rich Lode, 4 × Star Crystal, 3 × Quorvium Boulder, 2 × Cataclysite Mass, 1 × Motherlode |
| `DS-4` | 24 | 4 | 5 分钟 | 9 × Rich Lode, 5 × Prism Cluster, 4 × Ancient Husk, 3 × Cataclysite Mass, 2 × Derelict Cruiser, 1 × Motherlode |

<!-- asteroids-maps:end -->

## 种类 {#the-kinds}

<!-- asteroids-kinds:begin -->
<!-- Generated from server/Resources/Asteroids.json (and Rockets.json) by scripts/asteroids-wiki.sh: don't edit by hand. -->

小行星共有 27 种，分属 8 个系列。**针对火箭**写出该种类是按哪种火箭平衡的，以及在 Alpha 里大约需要多少枚才能击碎。**产出**是一次击碎抽取出的矿石和稀有产出，由它的碎块分着拿：百分比是那一行的几率，其他行一定会出。信用点和 Thulium 是一次击碎的 Alpha 数额。

### 岩石 {#stone}

普通岩石：没有装甲，也没有弱点。

| 种类 | 船体 | 大小 | 特性 | 钱币碎块 | 针对火箭 | 信用点 | Thulium | 产出 | 出现位置 |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Pebble** | 8,500 | 极小 | – | 1 | 约 4 ⁠枚 [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 6,600–11,100 | 22%：3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3 (49%) | `M-1`, `T-1`, `G-1`, `M-2` |
| **Cobble** | 10,000 | 小型 | – | 1 | 约 5 ⁠枚 [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 6,300–10,500 | 25%：3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–9 (89%) | `M-1`, `T-1`, `G-1`, `M-2` |
| **Dark Chondrite** | 12,000 | 小型 | – | 1 | 约 3 ⁠枚 [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 7,050–11,850 | 65%：3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–12 (91%), [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (93%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `T-1`, `M-2`, `T-2`, `G-2` |
| **Vein Rock** | 18,000 | 小型 | – | 1 | 约 4 ⁠枚 [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 13,350–22,200 | 50%：3–9 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–6 (73%), [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (45%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `M-2`, `T-2`, `G-2` |
| **Slag Block** | 24,000 | 中型 | – | 2 | 约 5 ⁠枚 [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 18,600–31,050 | 50%：3–9 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (95%), [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 3–6 (84%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1.5%) | `M-3`, `T-3`, `G-3` |
| **Cataclast** | 36,000 | 中型 | – | 2 | 约 8 ⁠枚 [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 22,350–37,200 | 50%：6–15 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 9–18, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–24; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1.5%) | `M-3`, `T-3`, `G-3` |
| **Lode Rock** | 52,000 | 中型 | – | 2 | 约 11 ⁠枚 [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 34,950–58,200 | 50%：18–39 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 9–18, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–24; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1.5%) | `M-3`, `T-3`, `G-3`, `G-4` |
| **Cataclysite Mass** | 72,000 | 大型 | – | 2 | 约 10 ⁠枚 [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 44,700–74,550 | 50%：21–45 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 15–30, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 9–15; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `M-3`, `M-4`, `T-4`, `G-4`, `DS-3`, `DS-4` |
| **Rich Lode** | 80,000 | 大型 | – | 3 | 约 11 ⁠枚 [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 61,800–103,050 | 50%：39–90 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–24, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 6–12; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (8%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (5%) | `DS-1`, `DS-2`, `DS-3`, `DS-4` |

### 冰 {#ice}

冻结的岩石：没有装甲，也没有弱点。

| 种类 | 船体 | 大小 | 特性 | 钱币碎块 | 针对火箭 | 信用点 | Thulium | 产出 | 出现位置 |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Rime** | 12,000 | 小型 | – | 1 | 约 5 ⁠枚 [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 8,250–13,800 | 55%：3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–9 (77%) | `T-1`, `G-1`, `T-2` |

### 水晶 {#crystal}

易碎：范围爆炸对水晶小行星造成的伤害比直接命中更大。

| 种类 | 船体 | 大小 | 特性 | 钱币碎块 | 针对火箭 | 信用点 | Thulium | 产出 | 出现位置 |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Glimmer** | 9,000 | 极小 | 爆炸 ×1.6 | 1 | 约 4 ⁠枚 [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 6,150–10,350 | 41%：3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–6 (77%) | `M-1`, `G-1`, `G-2` |
| **Nyx Geode** | 26,000 | 中型 | 爆炸 ×1.6 | 2 | 约 6 ⁠枚 [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 16,650–27,750 | 50%：9–21 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 6–15, [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3–6 (96%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `G-1`, `T-2`, `G-2` |
| **Quorvium Boulder** | 48,000 | 中型 | 爆炸 ×1.6 | 2 | 约 7 ⁠枚 [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 29,850–49,650 | 50%：12–30 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–21, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 3–15 (86%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `G-3`, `M-4`, `T-4`, `G-4`, `DS-3` |
| **Prism Cluster** | 100,000 | 大型 | 爆炸 ×1.6 | 3 | 约 14 ⁠枚 [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 71,700–119,550 | 50%：27–60 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 24–42, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 12–21; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (8%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (5%) | `DS-1`, `DS-3`, `DS-4` |

### 残骸 {#salvage}

残骸和吊舱：里面有 Ship Fragment。

| 种类 | 船体 | 大小 | 特性 | 钱币碎块 | 针对火箭 | 信用点 | Thulium | 产出 | 出现位置 |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Cache Pod** | 14,000 | 极小 | – | 1 | 约 6 ⁠枚 [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 9,000–15,000 | 29%：3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–6 (83%), [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 3–9 (78%) | `M-1`, `T-1` |
| **Scrap Hulk** | 20,000 | 小型 | – | 1 | 约 5 ⁠枚 [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 12,150–20,250 | 92%：3 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–9 (95%), [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (77%), [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 6–12; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `M-2`, `T-2` |
| **Derelict Hulk** | 52,000 | 中型 | – | 2 | 约 11 ⁠枚 [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 33,150–55,200 | 50%：9–18 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 6–12, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 9–18, [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 30–54; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1.5%) | `M-3`, `T-3` |
| **Derelict Cruiser** | 72,000 | 大型 | – | 2 | 约 10 ⁠枚 [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 46,200–76,950 | 50%：18–39 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 9–15, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 3–9 (97%), [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 21–36; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `T-3`, `M-4`, `T-4`, `DS-2`, `DS-4` |

### 铁 {#iron}

有装甲：每次命中都会因装甲损失点数，所以它们需要比船体所暗示的更强的火箭。

| 种类 | 船体 | 大小 | 特性 | 钱币碎块 | 针对火箭 | 信用点 | Thulium | 产出 | 出现位置 |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Ironhide** | 14,000 | 小型 | 装甲 500 | 1 | 约 4 ⁠枚 [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 13,650–22,650 | 50%：3–9 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–6 (74%), [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (46%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `M-1`, `M-2`, `G-2` |
| **Plateback** | 36,000 | 中型 | 装甲 1,500 | 2 | 约 11 ⁠枚 [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 31,650–52,800 | 50%：9–18 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 6–12, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 9–15, [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 27–51; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1.5%) | `M-3`, `G-3`, `M-4` |
| **Anvil** | 80,000 | 大型 | 装甲 3,000 | 2 | 约 18 ⁠枚 [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 84,900–141,450 | 50%：30–72 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 15–27, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 6–15, [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 36–69; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `M-4`, `G-4`, `DS-2` |

### 宝藏 {#treasure}

出手最大方的：每一种支付的信用点和 Thulium 都比它所在环的平均小行星更多。

| 种类 | 船体 | 大小 | 特性 | 钱币碎块 | 针对火箭 | 信用点 | Thulium | 产出 | 出现位置 |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Thulium Geode** | 66,000 | 中型 | 爆炸 ×1.6 | 2 | 约 14 ⁠枚 [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 42,450–70,800 | 18–42 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 9–15, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–21; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1.5%) | `T-3`, `G-3`, `T-4` |
| **Thulium Cluster** | 100,000 | 大型 | – | 2 | 约 14 ⁠枚 [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 62,100–103,500 | 42–99 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–21, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 3–15 (90%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `T-4`, `G-4` |
| **Vault Rock** | 130,000 | 大型 | – | 3 | 约 18 ⁠枚 [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 101,400–169,050 | 50%：36–87 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 9–18, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 3–12 (90%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `M-4`, `T-4`, `G-4`, `DS-1` |
| **Star Crystal** | 150,000 | 大型 | 爆炸 ×1.6 | 3 | 约 21 ⁠枚 [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 109,650–182,700 | 60–141 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 18–33, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 9–15; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (8%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (5%) | `DS-1`, `DS-2`, `DS-3` |

### 遗物 {#relic}

一艘死去的虫群舰船的外壳：有装甲，稀有产出丰富。

| 种类 | 船体 | 大小 | 特性 | 钱币碎块 | 针对火箭 | 信用点 | Thulium | 产出 | 出现位置 |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Ancient Husk** | 120,000 | 大型 | 装甲 2,000 | 3 | 约 22 ⁠枚 [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 114,300–190,350 | 50%：57–129 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 24–45, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 12–24; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (16%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (10%) | `DS-1`, `DS-2`, `DS-4` |

### 泰坦 {#titan}

最大的一种，给小队打的岩石。

| 种类 | 船体 | 大小 | 特性 | 钱币碎块 | 针对火箭 | 信用点 | Thulium | 产出 | 出现位置 |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Motherlode** | 450,000 | 巨型 | – | 3 | 约 61 ⁠枚 [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) | 348,900–581,400 | 165–381 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 69–126, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 36–66; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (8%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (5%) | `DS-1`, `DS-2`, `DS-3`, `DS-4` |

<!-- asteroids-kinds:end -->

## 它不给什么 {#what-it-does-not-give}

小行星不算击杀。击碎它不会给经验值、荣誉、击杀数、PvE 或 PvP 点数、排名、[重置点数](/wiki/03-Mechanics/Wipe-Timeline.md#earning-wipe-points)、无人机经验值，也不推进任何[任务](/wiki/03-Mechanics/Quests.md)，每个等级的[小行星任务](/wiki/03-Mechanics/Quests.md#levels)除外。赛季商店的增益也对它无效。它给的是表里写的东西：信用点、Thulium 和矿石，[资源](/wiki/06-Items/Resources.md)页面把它们和外星人的掉落一起列了出来。

## 小贴士 {#tips}

- **先用这个种类所针对的火箭。** 较弱的火箭也能击碎小行星，但需要更多火箭和更多计时器时间。更强的更快，但一次命中超出剩余船体的那部分伤害会浪费，而且无论打中什么，一枚火箭的花费都一样。
- **水晶用爆炸，铁用力量。** Scatter 或 Ember 是对付易碎小行星的火箭，有装甲的则需要比它船体所暗示的更强的火箭，因为装甲会从每次命中中扣掉它的点数。
- **让激光在两发火箭之间工作。** 它们每秒开火一次，消耗的是弹药而不是火箭，但一轮齐射只有对飞船伤害的 5%：它们是对火箭的补充，而不是替代。
- **留意每日上限。** 一天内你拾取的量达到你所在世界的上限后，碎块就不再支付；采矿报酬很高，几个小时就能碰到上限；上限见“世界”。
- **大的一起打。** 小行星 Motherlode 是给小队打的岩石：小队算作一名飞行员，它的份额按等级分给附近正在开火的队友。
- **留意星区。** 小行星不会还击，但它们周围的星区里仍有外星人，危险星区里还有其他飞行员。
