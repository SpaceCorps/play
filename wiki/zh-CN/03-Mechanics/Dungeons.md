<!-- wiki-i18n source: a3ead40fe6402d78 -->
<!-- wiki-i18n title: 地下城 -->
# 地下城 {#dungeons}

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; 地下城; 迷宫之门; 战争领主; 迷宫; 阶段; 战利品区域; 卡牌 -->

**地下城**在游戏中叫作**迷宫之门**：一座封闭的迷宫，尽头有一名**战争领主**。[战队](/wiki/03-Mechanics/Clans.md)的副队长或队长用战队银行的资金开启一座，战队成员随后组成一个[小队](/wiki/03-Mechanics/Groups.md)一同飞入。他们杀穿迷宫里的外星人，开启战利品区域并从每个区域中选一张卡牌，然后击败战争领主。参与战斗的飞行员会在战争领主倒下时，按下方限制获得报酬。迷宫之门位于战队页面的**迷宫之门**标签页。

迷宫之门只与外星人作战：里面无法攻击任何人，包括战队成员。外星人不会支付任何东西。报酬只来自战争领主，所以想拿到报酬，唯一的办法是在它倒下时身处战斗之中。

## 概览 {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **开放**：从赛季第 4 天起
- **谁来开启门**：副队长或队长，费用从战队银行扣除
- **小队**：战队成员 4 至 10 名，编成一个小队
- **每日门数**：每个战队每个 UTC 日 3 座，同一时间只开一座
- **同时存在的门**：每个世界 6 座
- **地图**：Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **迷宫**：8 种；开启门时随机选一种
- **集合**：10 分钟 用于集合和开始。无人开始的门会关闭，费用退回战队银行
- **时间限制**：从开始起 阶段 1: 80 分钟, 阶段 2: 110 分钟, 阶段 3: 150 分钟。时间用完，门失败且不发放任何报酬
- **无人时**：门内 3 分钟 无人则失败
- **战争领主倒下后**：门会为门内的飞行员保持开启 2 分钟
- **返回**：离开或被击毁的飞行员可以飞回 3 次，每次间隔 20 秒

<!-- dungeons-glance:end -->

## 一局的流程 {#how-a-run-goes}

1. **召唤。** 在迷宫之门标签页，[副队长或队长](/wiki/03-Mechanics/Clans.md#hierarchy-roles)选择一个阶段并按下**召唤**。费用从[战队银行](/wiki/03-Mechanics/Clans.md#clan-economy-taxation)扣除，这座门会分到上面列表中的一张地图。无人开始的门会关闭，费用退回银行。
2. **进入。** 战队成员在飞行时于战队窗口按下**进入**。里面的飞行员就是这座门的小队。
3. **开始。** 开启这座门的飞行员或一名干部在里面人数足够时按下**开始**。此后只有原本已在里面的飞行员可以回来。
4. **杀穿迷宫。** 你从迷宫的一端进入，战争领主在另一端等候。外星人睡在各自的房间里，小队靠近时成群醒来。
5. **开启战利品区域。** 迷宫中的圆环标记出这些区域。守住一个，小队就会为一张卡牌投票，这张卡牌会与战争领主的报酬一起发放。
6. **击败战争领主。** 打破它的护盾和船体，并应对它的技能。它倒下时，这座门就通关了。
7. **领取报酬。** 报酬在战争领主倒下的那一刻发放。这座门会为里面的飞行员再开放一小会儿，然后关闭。

## 进入 {#entering}

要进入一座门，你需要一艘**飞行中的飞船**，所以先起飞，再打开战队窗口，还需要一个里面有足够多战队成员的[小队](/wiki/03-Mechanics/Groups.md)。你还需要达到该阶段要求的**等级**，并且不能已经身处另一座门里。门的小队有人数上限：满员后，其他人无法再进入。

由副队长或队长开启门，战队同一时间只能开一座，且每天不超过规定的次数。战队银行必须有足够的费用。战队只有在通关前一个阶段之后，才能开启下一个阶段。

在门里无法更换世界，Jump CPU 和 Base CPU 也无法使用。门的状态栏上的**离开**按钮会在你确认后送你出去。离开或被摧毁的飞行员可以再飞回来几次，每次之间有一小段等待时间。

## 阶段 {#the-stages}

每座门都有一个阶段，阶段就是它的难度。阶段越高，外星人越坚固、攻击越狠，报酬也越高。表中的倍率适用于每一个外星人和战争领主。伤害指激光、火箭和战争领主的技能。表中还列出了每个阶段与第一阶段相比派出多少外星人。**价格**在开启门时从战队银行扣除。

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| 阶段 | 需求 | 外星人的船体和护盾 | 外星人数量 | 外星人的伤害 | 门的价格（信用点，由战队银行支付） |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **阶段 1** | 6 级起 | ×1 | ×1 | ×1 | 500,000 |
| **阶段 2** | 7 级起 | ×1.5 | ×1 | ×1.25 | 1,000,000 |
| **阶段 3** | 8 级起 | ×2.5 | ×1 | ×1.5 | 2,000,000 |

<!-- dungeons-stages:end -->

## 迷宫 {#the-maze}

每座门都是一座封闭的迷宫，位于它自己的地图上，地图是上面列表中的一张，而迷宫是几种布局中的一种。迷宫是由房间和走廊组成的网格，墙壁坚固。飞船无法穿过墙壁，墙壁还会挡住射击，所以墙壁可以当掩体。陨石从上方落下，墙壁挡不住它。

## 外星人 {#the-aliens}

四种外星人守卫着迷宫。它们睡在自己的房间里，飞行员靠近时会醒来。门同一时间只会让一定数量的外星人在空中活动，这个数量随小队人数增长，所以你消灭一群，下一群才会进来。小队越大，遇到的外星人按比例越多，越小则越少，而且每种外星人的数量都不会低于一。

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| 外星人，按 5 人小队计 | 阶段 1 | 阶段 2 | 阶段 3 |
| :--- | ---: | ---: | ---: |
| Gate Goombah | 130 | 130 | 130 |
| Gate Pirate | 28 | 28 | 28 |
| Gate Crystalys | 28 | 28 | 28 |
| Gate Crystalys Twin | 9 | 9 | 9 |
| 合计 | 195 | 195 | 195 |
| 战利品区域的一波 | 10 × Gate Goombah 和 1 × Gate Crystalys | 10 × Gate Goombah 和 1 × Gate Crystalys | 10 × Gate Goombah 和 1 × Gate Crystalys |

- **同时存活**：小队中每名飞行员最多 10 个，总共最多 70 个

<!-- dungeons-population:end -->

下面逐种列出。船体和护盾是常规数值乘以该列阶段的倍率。

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Gate Goombah

- **外观**：Goombah
- **成群飞行，每群**：6

|  | 阶段 1 | 阶段 2 | 阶段 3 |
| :--- | ---: | ---: | ---: |
| 船体 | 32,000 | 48,000 | 80,000 |
| 护盾 | 48,000 | 72,000 | 120,000 |
| 激光伤害 （每秒一轮齐射） | 3,000 | 3,750 | 4,500 |
| 速度 | 180 | 180 | 180 |
| 激光射程 | 800 | 800 | 800 |
| 仇恨范围 | 1,800 | 1,800 | 1,800 |

### Gate Pirate

- **外观**：Pirate Boss
- **成群飞行，每群**：2
- **火箭**：每 5 秒 一枚直射火箭，射程 970 单位

|  | 阶段 1 | 阶段 2 | 阶段 3 |
| :--- | ---: | ---: | ---: |
| 船体 | 300,000 | 450,000 | 750,000 |
| 护盾 | 50,100 | 75,150 | 125,250 |
| 激光伤害 （每秒一轮齐射） | 200 | 250 | 300 |
| 火箭伤害 | 5,000 | 6,250 | 7,500 |
| 速度 | 92 | 92 | 92 |
| 激光射程 | 700 | 700 | 700 |
| 仇恨范围 | 1,800 | 1,800 | 1,800 |

### Gate Crystalys

- **外观**：Crystalys
- **成群飞行，每群**：2

|  | 阶段 1 | 阶段 2 | 阶段 3 |
| :--- | ---: | ---: | ---: |
| 船体 | 256,000 | 384,000 | 640,000 |
| 护盾 | 160,000 | 240,000 | 400,000 |
| 激光伤害 （每秒一轮齐射） | 10,000 | 12,500 | 15,000 |
| 速度 | 230 | 230 | 230 |
| 激光射程 | 900 | 900 | 900 |
| 仇恨范围 | 2,400 | 2,400 | 2,400 |

### Gate Crystalys Twin

- **外观**：Crystalys，体型 1.4 倍
- **成群飞行，每群**：1

|  | 阶段 1 | 阶段 2 | 阶段 3 |
| :--- | ---: | ---: | ---: |
| 船体 | 512,000 | 768,000 | 1,280,000 |
| 护盾 | 320,000 | 480,000 | 800,000 |
| 激光伤害 （每秒一轮齐射） | 20,000 | 25,000 | 30,000 |
| 速度 | 230 | 230 | 230 |
| 激光射程 | 900 | 900 | 900 |
| 仇恨范围 | 2,400 | 2,400 | 2,400 |

<!-- dungeons-enemies:end -->

## 战争领主 {#the-warlord}

战争领主在迷宫远端的房间里等候，它是门里唯一会支付报酬的存在。它是一只长得极其巨大的 Crystalys。它的船体和护盾随小队人数增长：进入的飞行员越多，它就越坚固，成比例增长。它留在自己的房间里，以随机顺序一次使用一个技能，每个技能都有自己的冷却。

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **外观**：Crystalys，体型 3 倍
- **护盾回复**：每秒 3,000，在 15 秒 未受伤后

|  | 阶段 1 | 阶段 2 | 阶段 3 |
| :--- | ---: | ---: | ---: |
| 船体 | 10,000,000 | 15,000,000 | 25,000,000 |
| 护盾 | 8,000,000 | 12,000,000 | 20,000,000 |
| 激光伤害 （每秒一轮齐射） | 8,000 | 10,000 | 12,000 |
| 速度 | 120 | 120 | 120 |
| 激光射程 | 1,100 | 1,100 | 1,100 |

上面的船体和护盾按 5 人小队计。它们随小队人数增长：这是战争领主的船体与护盾之和，取决于门开始时小队中的飞行员人数。

| 小队中的飞行员 | 阶段 1 | 阶段 2 | 阶段 3 |
| :--- | ---: | ---: | ---: |
| 4 | 14,400,000 | 21,600,000 | 36,000,000 |
| 5 | 18,000,000 | 27,000,000 | 45,000,000 |
| 6 | 21,600,000 | 32,400,000 | 54,000,000 |
| 7 | 25,200,000 | 37,800,000 | 63,000,000 |
| 8 | 28,800,000 | 43,200,000 | 72,000,000 |
| 9 | 32,400,000 | 48,600,000 | 81,000,000 |
| 10 | 36,000,000 | 54,000,000 | 90,000,000 |

<!-- dungeons-boss:end -->

### 它的技能 {#its-abilities}

- 生命窃取光环的**红色圆环**会伤害里面的每一名飞行员，并用这些伤害治疗战争领主。护盾吸收也有一个红色圆环：它会抽干里面飞行员的护盾，并给战争领主的护盾充能。两种情况下，都要离开圆环，或者躲到墙后。
- 陨石坠落的**琥珀色圆环**显示片刻之后陨石将落在哪里。保持移动，在落下前离开圆环。
- **集火治疗者**会让战争领主转向治疗其他飞行员的人，并对那名飞行员打得更狠。把治疗分散开。
- **火箭齐射**会向随机的飞行员发射追踪火箭。EMP Charge 或隐形可以甩掉它们。

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| 技能 | 预备 | 持续时间 | 冷却 | 圆环半径（单位） | 战争领主最多回复 |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **生命窃取光环** | 2 秒 | 15 秒 | 2 分钟 | 900 | 船体和护盾的 8% |
| **陨石坠落** | 1.5 秒 | 3 轮，间隔 4 秒 | 2 分钟 | 420 | – |
| **集火治疗者** | 1 秒 | 45 秒 | 2 分钟 | – | – |
| **火箭齐射** | 1.5 秒 | 45 秒 | 2 分钟 | – | – |
| **护盾吸收** | 2 秒 | 15 秒 | 2 分钟 | 900 | 护盾的 6% |

| 技能 | 阶段 1 | 阶段 2 | 阶段 3 |
| :--- | :--- | :--- | :--- |
| **生命窃取光环** | 每秒 8,000 | 每秒 10,000 | 每秒 12,000 |
| **陨石坠落** | 每轮 6 颗陨石，每颗 40,000 | 每轮 8 颗陨石，每颗 50,000 | 每轮 10 颗陨石，每颗 60,000 |
| **集火治疗者** | 它的激光对其盯上的飞行员伤害为 ×1.5 | 它的激光对其盯上的飞行员伤害为 ×1.5 | 它的激光对其盯上的飞行员伤害为 ×1.5 |
| **火箭齐射** | 每枚火箭 6,500，每 15 秒 一枚 | 每枚火箭 8,125，每 15 秒 一枚 | 每枚火箭 9,750，每 15 秒 一枚 |
| **护盾吸收** | 每秒 10,000 护盾 | 每秒 12,500 护盾 | 每秒 15,000 护盾 |

<!-- dungeons-abilities:end -->

## 战利品区域 {#loot-zones}

小队找到战利品区域后，迷宫地面上的一个圆环会标记出它。在里面站一会儿，区域就会苏醒，一波外星人会朝它涌来。接着小队必须**守住**这个区域：让一名飞行员留在里面，直到进度条满。圆环里有外星人时进度条会停住，里面没人时则会倒退，所以先清掉这一波。区域开启时，小队会看到三张不同的卡牌，并为其中一张**投票**。一个区域只开启一次，它的那一波也不会再来。

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **战利品区域**：每座迷宫 4 个
- **半径**：450 单位
- **唤醒**：在圆环内站立 2 秒
- **守住**：让一名飞行员在圆环内停留 30 秒。圆环内有 3 个或更多外星人时进度条停止，里面没人时进度条倒退
- **选择**：小队有 45 秒 投票。所有在场飞行员都投票，或某张卡牌获得过半选票时，投票会提前结束

<!-- dungeons-zones:end -->

### 卡牌 {#the-cards}

卡牌从下面的卡池里逐张抽取。几率是一张卡牌在一次抽取中的几率。有多份的卡牌会发给每一名获得报酬的飞行员，只有一份的装备卡牌则发给小队中的一名飞行员。没有获得报酬的飞行员也拿不到卡牌，在失败的门里开启的区域不会支付任何东西。

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| 卡牌 | 阶段 1 | 阶段 2 | 阶段 3 | 几率 | 发给谁 |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2,000 | 3,000 | 5,000 | 21% | 每名获得报酬的飞行员 |
| Velkonite Reinforced Plate | 10 | 15 | 25 | 12% | 每名获得报酬的飞行员 |
| Orvium Reinforced Plate | 10 | 15 | 25 | 12% | 每名获得报酬的飞行员 |
| Velkonite | 200 | 300 | 500 | 12% | 每名获得报酬的飞行员 |
| Orvium | 200 | 300 | 500 | 12% | 每名获得报酬的飞行员 |
| Ultra Core | 5,000 | 7,500 | 12,500 | 10% | 每名获得报酬的飞行员 |
| Experimental Fusion Core | 3,000 | 4,500 | 7,500 | 8% | 每名获得报酬的飞行员 |
| Dark Matter | 5 | 8 | 12 | 8% | 每名获得报酬的飞行员 |
| Dark Matter Plate | 1 | 1 | 2 | 4% | 每名获得报酬的飞行员 |
| Engine III | 1 | 1 | 1 | 0.25% | 小队中的一名飞行员 |
| Heavy Shield Core | 1 | 1 | 1 | 0.25% | 小队中的一名飞行员 |
| Adaptive Core III | 1 | 1 | 1 | 0.25% | 小队中的一名飞行员 |
| Starfire-III | 1 | 1 | 1 | 0.25% | 小队中的一名飞行员 |

- **装备**：只有一份的卡牌是装备：合计占全部卡牌的 1%

<!-- dungeons-cards:end -->

## 报酬 {#pay}

战争领主倒下时，每名应得报酬的飞行员都会就这次通关获得一次报酬。小队选出的卡牌会加在该阶段的报酬之上。没有世界倍率：每个世界的报酬都相同。

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| 阶段 | 荣誉 | 经验值 | 信用点 | Thulium | x4 弹药 | PvE 积分 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| **阶段 1** | 25,000 | 600,000 | 5,000,000 | 4,000 | 4,000 | 600 |
| **阶段 2** | 50,000 | 1,500,000 | 10,000,000 | 9,000 | 9,000 | 1,500 |
| **阶段 3** | 100,000 | 2,400,000 | 17,500,000 | 15,000 | 15,000 | 2,400 |

<!-- dungeons-pay:end -->

### 谁能获得报酬 {#who-is-paid}

外星人从不支付报酬。即使没有任何报酬，一局也会完整打完，结果画面会告诉你原因。你不会因为已经拿过某个阶段的报酬而被拒绝入场：那一局只是不支付东西而已。

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **一天**：每个阶段每个 UTC 日向飞行员支付一次：以战争领主倒下的那一天为准
- **一周**：每个 UTC 周（周一至周日），飞行员最多可就 10 次阶段通关获得报酬
- **门内时间**：累计至少 2 分钟
- **战斗参与**：至少满足其一：对战争领主的船体和护盾造成了 2%; 击毁了门内的 10 个外星人; 在对战争领主的战斗中为其他飞行员治疗了 50,000

<!-- dungeons-rules:end -->

### 一天和一周的价值 {#what-a-day-and-a-week-are-worth}

一名飞行员一天能拿到的报酬，以及在限制允许的最佳一周里能拿到的报酬。最后一列是报酬为你的 [PvE 积分](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points)增加的数值。

<!-- dungeons-totals:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| 每名飞行员的报酬 | 荣誉 | 经验值 | 信用点 | Thulium | x4 弹药 | PvE 积分 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 一天，每个阶段各一次 | 175,000 | 4,500,000 | 32,500,000 | 28,000 | 28,000 | 4,500 |
| 最佳的一周：7 × 阶段 3 和 3 × 阶段 2 | 850,000 | 21,300,000 | 152,500,000 | 132,000 | 132,000 | 21,300 |

获得报酬的通关所得的经验值会计入你的 PvE 积分：每 1,000 点经验值得 1 分。

<!-- dungeons-totals:end -->

## 战队银行的奖励 {#clan-bank-reward}

战队在一个赛季里首次通关某个阶段时，战队银行也会获得报酬，是信用点而不是 Thulium。战队必须足够老，并且那一局必须有足够多的飞行员获得报酬。银行在一个赛季里每个阶段获得一次报酬。

<!-- dungeons-clan:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| 阶段 | 战队银行获得的信用点 |
| :--- | ---: |
| **阶段 1** | 10,000,000 |
| **阶段 2** | 20,000,000 |
| **阶段 3** | 30,000,000 |

- **战队年龄**：至少 3 天
- **获得报酬的飞行员**：门内至少 3 人

<!-- dungeons-clan:end -->

## 小贴士 {#tips}

- 先清掉区域的那一波，再去守这个区域；外星人冲进来时，就在圆环里战斗。
- 利用墙壁：激光穿不过去，战争领主的圆环也会在墙边停住。
- 为火箭齐射留一个 EMP Charge。
- 留意门的状态栏上的时钟。时间用完时，门会失败，也不会支付任何东西。
