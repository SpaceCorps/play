<!-- wiki-i18n source: 27056100dc9d4562 -->
<!-- wiki-i18n title: 拍卖行 -->
# 拍卖行 {#auction}

拍卖行是飞行员之间的市场，也是游戏自己每小时开出的拍品，都在空间站菜单的同一个页面里。和商店一样，它是空间站的页面：你在停靠时使用，飞行中不能用。它分为四个部分。**市场**是其他飞行员在卖的东西。**拍品**是游戏自己的出售，每小时一个。**我的挂单**是你自己在卖的东西。**记录**是你的出售、购买、你赢得的拍品，以及你的交易表现。

<!-- market-glance:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- 要使用拍卖行（挂单、购买和出价），需要 **5 级**。
- 挂单按每组定价，用整数信用点或整数 Thulium（二选一），且不能低于该物品的最低价。**没有最高价。**
- Thulium 定价至少是信用点最低价除以汇率（1,000）后向上取整的值，且只适用于最低价达到 1 Thulium 或以上的物品。汇率只起这一个作用：**1 Thulium = 1,000 信用点只是最低价的规则，不是兑换汇率。**不会换算任何东西，也不显示任何价值，信用点和 Thulium 永远不会相加。
- 共有 82 种物品可以挂单，其中 81 种还可以用 Thulium 定价。
- 挂单时长可在 24 / 72 / 168 小时中选择，每个等级的可选时长都一样。
- **押金**是价格的 1%，按挂单每 24 小时计，最低 50 信用点 或 1 Thulium。挂单时支付，永远不退还，取消挂单也不退。
- 从 10 级起，押金为 1.5%。
- **税**是价格的 5%。挂单售出时，从卖家所得中扣除。
- 押金和税都会被销毁：不会给任何人。
- 赛季第 28 天起直到重置，没有押金，也没有税。
- 赛季第 30 天起，拍卖行关闭，直到新赛季开始：不能挂单、购买或出价。你仍然可以取消自己的挂单。
- 每种货币各有自己的上限，限制你在 24 小时内能卖多少、能买多少（见下方等级表）。拍品得标不计入。
- 两名飞行员之间（一方向另一方购买），24 小时内最多只能流动 8,000,000 信用点 或 40,000 Thulium。

<!-- market-glance:end -->

## 可交易的物品 {#marketable-items}

只有你**赚来的**物品才能出售。你赚到的一切在[机库](/wiki/03-Mechanics/Inventory.md#marketable-items)里都带有一个小小的**可交易**标记：你在太空中拾取的东西（外星人、虫群、Warden 和黑洞的掉落：[货箱](/wiki/03-Mechanics/Cargo.md)）、任务发放的东西（[任务](/wiki/03-Mechanics/Quests.md#rewards)），以及装配站和锻造炉制作的一切。你在商店**购买**的、在拍品中赢得的、在市场上买到的、通过奖励码、邀请礼包或新手套装获得的、或作为退款拿回的东西都不可交易，也永远不能再次出售，所以没有什么东西是为了转手而买的。Skylab 锻造厂制作的板材同样不可交易；任务发放的 Reinforced Plate 则可以交易。Skylab 弹药打印机和火箭工厂制造的弹药和火箭同样不可交易。

标记是单位数量，不是开关：一叠弹药里可以既有买来的也有赚来的，卡片上会写“可交易（3/5）”。当你用掉一叠中的一部分（射击、制作）时，普通单位先用掉，所以可交易的单位留得最久。在[锻造炉](/wiki/06-Items/Forge.md#merge)里合并两件物品时，只有两件都带标记，标记才会保留，预览会显示这一点；失败的锻造炉步骤会把材料以普通单位退还。

机库里的**仅可交易**按钮只显示你能卖的东西，带标记物品的垃圾桶旁的**拍卖槌**会为它打开拍卖行的出售窗口。在装配站里，结果可交易的配方会这样标明，缺少的材料旁有一个链接，会用它的名字打开拍卖行的搜索。

拍卖行上线时（0.4.12），你已有的商店不卖的装备以及资源，被一次性加上了标记。下面这些没有加标记，因为商店曾经卖过它们，或者因为你持有的东西里买来的和赚来的混在一起：Quantum Laser III、Absorption Shield Cell II 和 III、Engine II、Adaptive Core II、Impulse Thruster II 和 III、两种 Reinforced Plate，以及每位飞行员最旧的 Base CPU I（新手套装里的那个）。你之后新赚到或制作的这些物品是带标记的。

## 可以出售什么 {#what-can-be-sold}

<!-- market-kinds:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| 类型 | 可出售的物品 | 数量 |
| :--- | :--- | ---: |
| **激光** | Quantum Laser I, Quantum Laser II, Quantum Laser III, Starfire-III, Helios Beam | 5 |
| **激光增幅器** | Damage Amp I, Crit Amp I, Penetration Amp I, Damage Amp II, Crit Amp II, Penetration Amp II, Damage Amp III, Crit Amp III, Penetration Amp III, Damage Amp IV, Crit Amp IV, Penetration Amp IV | 12 |
| **护盾核心** | Light Shield Core, Basic Shield Core, Heavy Shield Core | 3 |
| **引擎** | Engine I, Engine II, Engine III | 3 |
| **Adaptive Core** | Adaptive Core I, Adaptive Core II, Adaptive Core III | 3 |
| **护盾电池** | Absorption Shield Cell I, Capacity Shield Cell I, Absorption Shield Cell II, Capacity Shield Cell II, Absorption Shield Cell III, Capacity Shield Cell III, Absorption Shield Cell IV, Capacity Shield Cell IV | 8 |
| **推进器** | Impulse Thruster I, Momentum Thruster I, Impulse Thruster II, Momentum Thruster II, Impulse Thruster III, Momentum Thruster III, Impulse Thruster IV, Momentum Thruster IV | 8 |
| **激光弹药** | Standard Battery（每组 100 个）, Siphon Battery（每组 10 个）, Advanced Plasma（每组 10 个）, Ultra Core（每组 10 个）, Experimental Fusion Core | 5 |
| **火箭** | Ember I, Lancet I, Rivet I, Scatter I, Ember II, Lancet II, Rivet II, Scatter II, Ember III, Lancet III, Rivet III, Scatter III | 12 |
| **附加装置** | Repair Drone I, Repair Drone II, Repair Drone III, EMP Charge, Repair Drone IV, Cloaking CPU S, Base CPU I, Cloaking CPU M, Auto-Repair CPU, Cloaking CPU L, Base CPU II | 11 |
| **船体装甲** | Hull Plating II, Hull Plating III | 2 |
| **资源** | Cataclysite（每组 100 个）, Ship Fragment（每组 100 个）, Daraxium（每组 100 个）, Nyxite（每组 100 个）, Quorvium（每组 10 个）, Reinforced Hull Plate（每组 10 个）, Power Core, Velkonite Reinforced Plate, Dark Matter, Orvium Reinforced Plate | 10 |

<!-- market-kinds:end -->

飞船、无人机、无人机阵型、增益道具和订阅永远不能出售，Ancient Control Unit、矿石 Velkonite 和 Orvium、Dark Matter Plate、Jump CPU、Extra Slots CPU、N.U.K.E. 和 N.I.K.E. 也不能。Dark Matter Plate 根本不在拍卖行里，既不作为商品，也不作为价格。已装备的、嵌入另一件物品的、里面有模块的，或放在[运输储藏库](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-)里的物品不能挂单，用过的 Cloaking CPU、EMP Charge 或 Base CPU 也不能。弹药和火箭从空间站出售：请先让你的飞船降落。

## 出售 {#selling}

按下**出售物品**（或机库里的拍卖槌），选择你赚来的东西（分类下拉菜单可以缩小列表，分类与市场相同），选择信用点或 Thulium，设定每组的价格和挂单时长：1 天、3 天或 7 天。窗口会显示最低价、三个自动填价的按钮（**最低价**；**快速出售**，比当前最便宜的挂单低一点；**公允价**，即上一次成交价），以及挂单前就能看到的押金、税和你的所得。价格下方的**相似挂单**会用图表显示同一物品、同一附魔此刻的挂单价格，使用你选择的货币：你的价格是图上的一条线，最低价、上一次成交价和商店价格都有标记，一行文字说明你的价格会排在哪里，下面还列出最便宜的三个挂单。一件物品就是一组；弹药和部分资源按 10 或 100 一组出售，你出售的是整数组。你挂出的东西会离开你的物品栏，由服务器保管，直到售出、你取消或到期；之后它带着标记回来。你随时可以取消，赛季最后几天也一样。挂单是一张快照：要改价格，就取消挂单再重新挂出（押金要再付一次）。

每种物品都有**最低价**，而且**没有最高价**：想要多少就要多少。下表是几种物品的最低价。

<!-- market-bands:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| 物品 | 每组数量 | 最低价，信用点 | 最低价，Thulium |
| :--- | ---: | ---: | ---: |
| Quantum Laser II | 1 | 32,000 | 32 |
| Quantum Laser III | 1 | 210,000 | 210 |
| Helios Beam | 1 | 1,600,000 | 1,600 |
| Absorption Shield Cell IV | 1 | 1,100,000 | 1,100 |
| Heavy Shield Core | 1 | 870,000 | 870 |
| Impulse Thruster IV | 1 | 980,000 | 980 |
| EMP Charge | 1 | 40,000 | 40 |
| Cloaking CPU S | 1 | 400,000 | 400 |
| Ultra Core | 10 | 800 | 1 |
| Lancet I | 1 | 200 | 1 |
| Ship Fragment | 100 | 600 | 1 |
| Dark Matter | 1 | 33,000 | 33 |

<!-- market-bands:end -->

Thulium 定价只有一条规则：信用点最低价除以汇率，向上取整。汇率不是游戏给 Thulium 定的价值，它只是用来算出 Thulium 最低价的办法，所以对持有 Thulium 的飞行员来说，Thulium 挂单可能很便宜。大多数卖家会要信用点。除 **Quorvium** 外，每一种物品都可以用 Thulium 定价，便宜的也可以（弹药、火箭、普通资源）：它们的最低价就是 1 Thulium，也就是最小的一步。只有 Quorvium 仅限信用点定价，因为 1 Thulium 比一组 Quorvium 还要值钱。

你的**开放挂单**（以及被管理员搁置的挂单）会占用挂单位。等级提高后，挂单位会增加，直到上限，每天可以卖和买的也更多。挂单能持续多久，在每个等级都一样。

<!-- market-limits:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| 等级 | 在挂单数 | 最长挂单时间 | 每日，信用点 | 每日，Thulium | 每 24 小时押金 |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 5 | 20 | 168 小时 | 4,500,000 | 22,500 | 1% |
| 6 | 40 | 168 小时 | 6,000,000 | 30,000 | 1% |
| 7 | 70 | 168 小时 | 7,500,000 | 37,500 | 1% |
| 8 | 100 | 168 小时 | 8,500,000 | 42,500 | 1% |
| 9 | 100 | 168 小时 | 10,000,000 | 50,000 | 1% |
| 10 | 100 | 168 小时 | 15,000,000 | 75,000 | 1.5% |
| 11 | 100 | 168 小时 | 15,000,000 | 75,000 | 1.5% |
| 12 | 100 | 168 小时 | 15,000,000 | 75,000 | 1.5% |
| 13 | 100 | 168 小时 | 20,000,000 | 100,000 | 1.5% |
| 14 | 100 | 168 小时 | 20,000,000 | 100,000 | 1.5% |
| 15 | 100 | 168 小时 | 20,000,000 | 100,000 | 1.5% |
| 16 | 100 | 168 小时 | 20,000,000 | 100,000 | 1.5% |
| 17 | 100 | 168 小时 | 20,000,000 | 100,000 | 1.5% |
| 18 | 100 | 168 小时 | 20,000,000 | 100,000 | 1.5% |
| 19 | 100 | 168 小时 | 20,000,000 | 100,000 | 1.5% |
| 20 级及以上 | 100 | 168 小时 | 20,000,000 | 100,000 | 1.5% |

<!-- market-limits:end -->

## 费用 {#fees}

挂单要付**押金**，挂单时支付，永不退还；成交要付**税**，从卖家所得中扣除。两者都用挂单的货币支付并被**销毁**：它们不会给任何人，所以没有人能靠自己和自己交易获利。在赛季的最后两天没有押金，也没有税。

<!-- market-fees:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| 挂单 | 价格 | 押金 | 税 | 卖家所得 |
| :--- | ---: | ---: | ---: | ---: |
| Quantum Laser III：6 级，24 小时 | 210,000 信用点 | 2,100 信用点 | 10,500 信用点 | 199,500 信用点 |
| Quantum Laser III：10 级，72 小时 | 210 Thulium | 10 Thulium | 10 Thulium | 200 Thulium |
| Helios Beam：12 级，168 小时 | 2,500,000 信用点 | 262,500 信用点 | 125,000 信用点 | 2,375,000 信用点 |
| Helios Beam：12 级，168 小时，赛季最后几天 | 2,500,000 信用点 | 0 信用点 | 0 信用点 | 2,500,000 信用点 |

<!-- market-fees:end -->

## 购买 {#buying}

**市场**显示其他飞行员在卖的东西。可以用**分类标签**缩小列表（每种物品类型一个，标出其中的挂单数量），再按名称搜索，按附魔和货币筛选，按价格、最先结束或最新排序。选一个挂单，可以看到它是什么、谁在卖、还剩多久，以及它的价格与上一次成交价、当前最低价和商店价格相比如何。一叠按整数组购买。大额购买会再让你确认一次。卖家立刻收到款项（扣除税）；你不用付押金，也不用付税。你买到的东西**不可交易**：页面会在**购买**按钮旁写上“你得到的：不可交易”，因为只有你赚来的东西才能出售。你不能买自己的挂单。你正在看的挂单如果被别人买走，会提示“该上架物品已不存在。”

## 上限 {#limits}

每种货币各有自己的每日上限，限制你能卖多少、能买多少，按最近 24 小时计算；还有一个限制两名飞行员之间能流动多少，所以开小号并不是快速转移巨额财富的办法。信用点和 Thulium 永远不会相加：用 Thulium 卖东西的人只会用掉他的 Thulium 上限，别的都不会动。当一次出售会超过你的每日出售上限时，出售窗口会提醒你；当一次购买会超过你的每日购买上限时，市场会这样提示，并让**购买**按钮保持不可用。上限随等级增长，高级会员不会改变其中任何一项。拍品得标不计入。

挂单中的火箭、你领先的拍品中的火箭，以及你携带的火箭，都计入你最多能携带的某种火箭数量：不能通过挂单带上超过商店堆叠上限的火箭。

## 我的挂单与记录 {#my-listings-and-history}

**我的挂单**显示你的挂单位和每个挂单的状态（开放、已售出、已取消、已到期、已退回或已冻结），有**取消**按钮，已结束的挂单有**重新挂单**，当同一物品的其他挂单要价更低时会出现**被压价**标记。到期的挂单会自动回到你的物品栏。**记录**以你最近 30 天的交易开头：你的出售和购买、收入和支出、你付出的费用与税、净结果、最佳成交、平均成交价和交易最多的物品，外加两张折线图：每日收入和累计结果（信用点和 Thulium 一次显示一种）。下面是你卖出、买入和赢得的东西的列表（含税）。游戏会把拍卖行的账本保存 90 天。

有东西卖出时你会得到通知：一条提示、拍卖行的声音和新的余额，页面关闭时拍卖行的入口上还有一个角标。连续的成交只算一条提示。拍卖行有自己轻柔的声音，你在那里做的或发生在你身上的每件事（挂单、结束、成交、出价、被超过、得标）各有一个，并且跟随界面音量。

## 每小时的拍品 {#the-hourly-lots}

拍品是游戏自己的出售：弹药、火箭和 EMP Charge，每小时一次，供人出价。它们是以低于商店的价格买到弹药的办法，也是一个销毁渠道：得标出价会被销毁。只有下面一日表里的拍品才会开出（绝不会是 x1 或 x4 弹药、Siphon Battery 或特殊火箭），使用商店的货币。无论你已经携带了什么，都可以对任何拍品出价：赢得的拍品完整归你，即使它会让你超过商店允许你购买的堆叠上限。

<!-- market-lots:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- 每个 UTC 整点开启一个新拍品，开放 4 小时，所以同时开放 4 个。
- 起拍价是商品商店价格的 20%。之后的每次出价必须比最高出价至少高 5%，并且至少多 100 信用点 或 1 Thulium。
- 你的出价会立即支付并被冻结。如果有人出价更高，会立即退还给你。
- 在拍品结束前最后 2 分钟 内出价，会把结束时间推迟到出价后 2 分钟，最多 5 次。
- 赢得的东西是用来飞行的，不是用来交易的：永远不可交易。得标出价会被销毁。无人出价的拍品不会售出，也不会让任何人花钱。
- 拍品的大小取决于最近 3 天内看过拍卖行的 5 级及以上飞行员人数：没有人时是表中大小的 10%，达到 30 人及以上则是完整大小，步长为弹药 500、火箭 50、EMP Charge 1。
- 赛季最后 6 小时内不再生成拍品。重置会取消仍在开放的拍品，所有出价都会退还。

<!-- market-lots:end -->

<!-- market-day:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| UTC 整点 | 拍品 | 完整大小 | 支付货币 | 完整大小时的起拍价 |
| :--- | :--- | ---: | :--- | ---: |
| 00:00 | Scatter III | 1,250 | Thulium | 1,250 Thulium |
| 01:00 | Advanced Plasma | 25,000 | Thulium | 2,500 Thulium |
| 02:00 | Lancet I | 12,500 | 信用点 | 1,250,000 信用点 |
| 03:00 | EMP Charge | 5 | Thulium | 500 Thulium |
| 04:00 | Ultra Core | 25,000 | Thulium | 5,000 Thulium |
| 05:00 | Rivet II | 5,000 | 信用点 | 800,000 信用点 |
| 06:00 | Advanced Plasma | 10,000 | Thulium | 1,000 Thulium |
| 07:00 | Advanced Plasma | 50,000 | Thulium | 5,000 Thulium |
| 08:00 | Ember I | 12,500 | 信用点 | 1,250,000 信用点 |
| 09:00 | Ultra Core | 50,000 | Thulium | 10,000 Thulium |
| 10:00 | Scatter II | 5,000 | 信用点 | 800,000 信用点 |
| 11:00 | EMP Charge | 5 | Thulium | 500 Thulium |
| 12:00 | Advanced Plasma | 50,000 | Thulium | 5,000 Thulium |
| 13:00 | Lancet III | 1,250 | Thulium | 1,250 Thulium |
| 14:00 | Ultra Core | 10,000 | Thulium | 2,000 Thulium |
| 15:00 | Advanced Plasma | 25,000 | Thulium | 2,500 Thulium |
| 16:00 | Ultra Core | 50,000 | Thulium | 10,000 Thulium |
| 17:00 | Rivet I | 12,500 | 信用点 | 1,250,000 信用点 |
| 18:00 | Advanced Plasma | 50,000 | Thulium | 5,000 Thulium |
| 19:00 | Ember II | 5,000 | 信用点 | 800,000 信用点 |
| 20:00 | Ultra Core | 25,000 | Thulium | 5,000 Thulium |
| 21:00 | Advanced Plasma | 25,000 | Thulium | 2,500 Thulium |
| 22:00 | Advanced Plasma | 10,000 | Thulium | 1,000 Thulium |
| 23:00 | EMP Charge | 5 | Thulium | 500 Thulium |

<!-- market-day:end -->

使用拍卖行的飞行员很少时，拍品也很小，这样一小撮飞行员就不会每小时都看到成千上万发弹药；随着看的人变多，拍品会变大。

**用出价上限来出价。** 在出价窗口里打开“自动出价，直到出价上限”，然后输入你最多愿意付的数额。这样拍卖行就会替你出价：它先按拍品接受的最低出价出价，每当有人压过你，它就再出价，每次只比最高价高出最小加价幅度，直到你的出价上限，不会更高。你领先时的出价是刚好压过次高出价上限的最低价，而不是你的出价上限：在以 100 起拍的拍品上，上限分别为 500 和 800 信用点时，上限高的一方以 600 领先，而不是 800。两个上限相同，先设定的获胜。你的出价上限在设定时就会从钱包里全额冻结，所以自动出价不会因为钱不够而失败；拍品结束时你只付得标出价，其余退回；如果有人超过你的上限，全额会立刻退回，并且你会收到通知。在你领先的拍品上，“出价上限”按钮可以随时提高你的上限，也可以把它降到你当前的出价为止。设定出价上限不算出价，但延长规则会把每一次出价都算进去，拍卖行替你做的出价也一样。设定出价上限有自己轻柔的声音，跟随音效音量。

## 赛季与重置 {#the-season-and-the-wipe}

拍卖行跟随赛季（见[重置时间线](/wiki/03-Mechanics/Wipe-Timeline.md)）。最后两天没有费用。从第 30 天起，也就是重置的五分钟倒计时开始时，它关闭：不能挂单、购买或出价，当时结束的拍品会被取消并退还出价，你仍然可以取消自己的挂单。挂单不会持续到赛季结束之后。

重置时，**每个开放的挂单都会回到卖家手中**，成为散件，然后重置会像删除其他散件一样把它们删除（只有你放进[运输储藏库](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-)的东西会留下）：所以想留下的东西，要么卖掉，要么取消后放进储藏库。仍在开放的拍品会被取消，出价会退还。信用点和 Thulium 不会被重置。

## 拍卖行不能给你的 {#what-the-auction-does-not-give-you}

拍卖行是用来交易你赚来的东西的，它对自己的局限很坦率。

- **卖掉落物不是刷钱的办法。**外星人的原始掉落只有资源，价值只有同一个 5 级狩猎小时击杀所得的 0.4% 到 0.9%。市场给新飞行员的，是他的任务发放而他又用不上的装备（只有一次）、挑战任务的资源、虫群首领的箱子，以及他自己制作的东西。
- **没有经销商。**飞行员写明想买什么、出多少钱的求购单，这个版本里没有。在有之前，仅有的商人是手工匠（买材料，在装配站制作装备再卖掉）和仓库飞行员（把库存放在运输储藏库里度过重置）。
- **商店的装备不是用来转卖的。**你在商店买的装备不能再次出售：这包括 Quantum Laser I 和 II、Light 和 Basic Shield Core、Engine I 和 II、电池和推进器的第一阶、商店出售的增幅器，以及买来的弹药。一位飞行员手里唯一可交易的 Quantum Laser II，就是任务发放一次的那一个。
- **板材来自任务。**市场上的 Velkonite 和 Orvium Reinforced Plate 是挑战任务发放的那些。锻造厂的板材不在其中，否则它们会成为市场上最大的商品。

如果某个挂单看起来不对，请按通常的方式举报：游戏管理员可以搁置挂单、退回挂单、暂停拍卖行，或禁止某位飞行员使用它，每一次这样的操作都会被记录。
