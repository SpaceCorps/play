<!-- wiki-i18n source: 3c07d568f3af3aab -->
<!-- wiki-i18n title: Dormant Swamp -->
# Dormant Swamp

<!-- wiki-search: swamp; dormant swamp; base; turret; turrets; nike turret; laser turret; inert mass; unwakened; the unwakened; slumbering void; void; dormant lance; ds-4; 沼泽; 炮塔; 炮台 -->

很久以前，银河中央住着一个先进的文明。它用泛着紫光脉络的紫黑色晶体建造，因为一个无人知晓的原因崩溃了。**Dormant Swamp** 是它的前哨，位于 `DS-4` 的左上角。从赛季第 11 天起它开始躁动：中央的炮台向看到的每艘飞船开火，**Inert Mass** 守卫着它，正中心沉睡着 **Unwakened**。隐形时你可以飞到 Unwakened 跟前。自 [Deep Void](/wiki/03-Mechanics/Deep-Void.md) 开启以来，炮台和 Unwakened 都可以被摧毁，每个世界本赛季第一次击杀 Unwakened 会打开该世界的 Threshold。基地本身无法进入、登上，也无法与之交易。

沼泽也是 [Dormant 虫群](/wiki/05-Swarms/Dormant-Swarm.md)从第 11 天起出现的地方，**Slumbering Void** 在它周围巡逻。同样的 Void 也会成波来到[巨型挖掘机](/wiki/03-Mechanics/Giant-Excavator.md#the-slumbering-voids)。星区见[危险星区](/wiki/01-General/Danger-Sectors.md)。

![Flying in towards the Dormant Swamp: the amber notice ring and, inside it, the red ring of the zone the guns reach](../../img/wiki-img/shots/swamp-rings.jpg)

## 概览 {#at-a-glance}

<!-- swamp-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **位置**：`DS-4` 的左上角：中心在 5,000 / 5,000
- **出现**：从赛季第 11 天起，直到重置
- **区域**：围绕中心 4,300 单位：炮台所能到达的最远处
- **提示**：越过距中心 4,800 单位的那个环的飞船会收到一条系统行
- **隐形**：任何炮台都不会看到隐形的飞船，也不会看到处于 EMP 生效期内的飞船
- **外星人**：5 个 Inert Mass 留在距中心 2,400 单位以内。Unwakened 沉睡在中心。2 个 Slumbering Void 在距中心 4,600 到 6,500 单位之间巡逻。
- **Dormant 虫群**：它出现在 9,417 / 6,606，距中心 4,700 单位，位于区域之外
- **岩石**：中心 4,900 单位内没有小行星

<!-- swamp-glance:end -->

## 炮台 {#the-guns}

沼泽的炮塔会向射程内**它们能看到的最近的飞船**开火，不会向其他飞船开火：区域就是其中射程最远的那座所能到达的圆。它们不是飞船，但自 Deep Void 开启以来，每座炮塔都有了生命值：点击炮塔即可用激光向它开火，在它附近爆炸的火箭也会伤害它。被摧毁的炮塔在 Unwakened 复活前一直失效。它们的射击是真实的，世界会像缩放任何外星人的武器那样缩放它们的伤害。

<!-- swamp-guns:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

一发的伤害（各世界）：

| 炮台 | 位置 | 发射间隔 | 射程（单位） | Alpha | Beta | Gamma |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) 炮塔 | 5,000 / 4,400 | 2 秒 | 3,640 | 75,000 | 112,500 | 150,000 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) 炮塔 | 5,000 / 4,400 | 5 秒 | 1,080 | 50,000 | 75,000 | 100,000 |
| 激光炮塔 × 2 | 3,600 / 5,200; 6,400 / 5,200 | 1 秒 | 2,500 | 45,000–55,000 | 67,500–82,500 | 90,000–110,000 |

- 火箭在同款火箭于飞行员手中射程的 82% 处发射，以保证命中；激光炮塔每秒开火一次，伤害在所示范围内随机。
- N.I.K.E. 的护盾穿透为 35%，会从护盾吸收率中扣除。
- 炮塔的 N.I.K.E. 比你的飞得快 25%，飞行距离是你的 2 倍：每秒 1,250 单位，总共 8,910 单位，因此逃跑的飞船会被追很远。
- N.U.K.E. 在半径 1,013 单位内爆炸，中心最强。
- 炮塔的 N.U.K.E. 比你的飞得快 25%，飞行距离是你的 2 倍：每秒 375 单位，总共 2,640 单位，因此逃跑的飞船会被追很远。

<!-- swamp-guns:end -->

- **区域之外没有任何东西开火，**区域内飞船会在几秒内被摧毁：越靠近中心，参与的炮台越多，连护盾最好的 Wraith 也撑不住。不过，已经在空中的火箭会继续飞行，而且炮台的火箭比你的飞得更快、更远：沿直线逃跑甩不掉它。
- **隐形能让你进去。** 任何炮塔都不会看到隐形的飞船，也不会看到处于 EMP 生效期内的飞船，无论多远。瞄准一艘可见飞船的爆炸如果在隐形飞船旁炸开，仍会伤到它并解除它的隐形。
- **它们只向飞行员开火，**从不向外星人、企业飞行员或虫群开火，刚从被摧毁中回来的飞船的保护对它们同样有效。
- **提示环。** 越过区域之外那个环的飞船会收到一条系统行：炮塔会向看到的每艘飞船开火，中央有什么东西在沉睡。只有它离开环再回来时才会再次通知。
- **离开。** 如果你在那里被摧毁，不能就地复活（危险星区只提供基地和最近的传送门）；如果在区域内登录，你会被放到外面。你点击的航线会绕开区域，点击的地点若在其中，会弹出提示警告你。

## 外星人 {#the-aliens}

失落文明的三种外星人住在这里，各有各的数字。它们像虫群首领一样**按造成的伤害**支付奖励：给予者是造成伤害至少达到[虫群](/wiki/05-Swarms/Swarms.md#the-rules-of-every-swarm)中所列比例的每名飞行员，货箱则归造成伤害最多的飞行员。击杀它们会像击杀虫群飞船一样，按奖励的比例增加你的 PvE 军衔积分（[军衔](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points)）。每个外星人的护盾在持续期间会吸收每次命中的 {{guide:vitals.absorbance@Slumbering Void;Inert Mass;The Unwakened}}（[护盾](/wiki/03-Mechanics/Shields.md)）。

- **Slumbering Void。** 修长的猎手，游戏中最快的外星人（比装了 Afterburner III 的 Storm 更快）。一些总在沼泽周围巡逻，另一些成波来到挖掘机。它具有攻击性，追猎它能看到的最近的飞行员，并且永远看不到隐形的飞船。
- **Inert Mass。** 带紫色裂纹的死寂巨体，有一座小空间站那么大。它们待在距沼泽中心固定的距离内，目前不会离开。它发射 **Dormant Lance**：射程极远的制导火箭，会一直追着飞船，直到它隐形、打开 EMP 窗口、进入安全环、跳跃或死亡。它比任何飞船都快，所以只有这些中断才管用。 挡在 Dormant Lance 路径上的小行星会拦下它，而 Lance 会用自身的伤害损伤该小行星（没有人为此获得报酬），因此岩石只能让你在几次命中之内免受 Inert Mass 的伤害。
- **Unwakened。** 沉睡在沼泽中央的巨碑，是任何地图上最大的东西，慢到永远追不上飞船。它什么也不发射，但它光环内的每艘飞船都会被烧伤，**无论是否隐形**。自 [Deep Void](/wiki/03-Mechanics/Deep-Void.md) 开启以来，它可以被摧毁了：按造成的伤害支付报酬，死亡一天后复活，每个世界本赛季的第一次击杀会打开该世界的 Threshold。飞行员的**辐射技术**会降低它的灼烧，100 级时降到 0.40 倍。

<!-- swamp-members:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

### Slumbering Void

2 个 Slumbering Void 在距沼泽中心 4,600 到 6,500 单位之间巡逻；被击毁的会在 {{guide:vitals.respawn@Slumbering Void}} 后回来。挖掘机的波次会带来更多同样的外星人。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@Slumbering Void}} | {{guide:vitals.hull*1.5@Slumbering Void}} | {{guide:vitals.hull*2@Slumbering Void}} |
| 护盾 | {{guide:vitals.shield@Slumbering Void}} | {{guide:vitals.shield*1.5@Slumbering Void}} | {{guide:vitals.shield*2@Slumbering Void}} |
| 护盾吸收率 | {{guide:vitals.absorbance@Slumbering Void}} | {{guide:vitals.absorbance@Slumbering Void}} | {{guide:vitals.absorbance@Slumbering Void}} |
| 激光伤害 （每秒一轮齐射） | {{guide:vitals.dps@Slumbering Void}} | {{guide:vitals.dps*1.5@Slumbering Void}} | {{guide:vitals.dps*2@Slumbering Void}} |
| 速度 | {{guide:vitals.speed@Slumbering Void}} | {{guide:vitals.speed@Slumbering Void}} | {{guide:vitals.speed@Slumbering Void}} |
| 激光射程 | 800 | 800 | 800 |
| 仇恨范围 | {{guide:vitals.aggro@Slumbering Void}} | {{guide:vitals.aggro@Slumbering Void}} | {{guide:vitals.aggro@Slumbering Void}} |
| 信用点 | {{guide:spoils.pay.credits@Slumbering Void}} | {{guide:spoils.pay.credits*2@Slumbering Void}} | {{guide:spoils.pay.credits*3@Slumbering Void}} |
| Thulium | {{guide:spoils.pay.thulium@Slumbering Void}} | {{guide:spoils.pay.thulium*2@Slumbering Void}} | {{guide:spoils.pay.thulium*3@Slumbering Void}} |
| 经验值（XP） | {{guide:spoils.pay.experience@Slumbering Void}} | {{guide:spoils.pay.experience*2@Slumbering Void}} | {{guide:spoils.pay.experience*3@Slumbering Void}} |
| 荣誉 | {{guide:spoils.pay.honor@Slumbering Void}} | {{guide:spoils.pay.honor*2@Slumbering Void}} | {{guide:spoils.pay.honor*3@Slumbering Void}} |
| 每次击杀的 PvE 积分 | 10 | 10 | 10 |

**掉落**：一个货箱，归造成伤害最多的飞行员。

| 物品 |
| :--- |
| {{guide:spoils.box@Slumbering Void}} |

### Inert Mass

5 个 Inert Mass 站在距中心 2,400 单位以内；被击毁的会在 {{guide:vitals.respawn@Inert Mass}} 后回来。每 6 秒 向它能看到的最近飞船发射一枚制导的 [Dormant Lance](/wiki/06-Items/Rockets.md#the-craft-only-rockets)：速度 750，飞行距离 5,250 单位，穿透 40%。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@Inert Mass}} | {{guide:vitals.hull*1.5@Inert Mass}} | {{guide:vitals.hull*2@Inert Mass}} |
| 护盾 | {{guide:vitals.shield@Inert Mass}} | {{guide:vitals.shield*1.5@Inert Mass}} | {{guide:vitals.shield*2@Inert Mass}} |
| 护盾吸收率 | {{guide:vitals.absorbance@Inert Mass}} | {{guide:vitals.absorbance@Inert Mass}} | {{guide:vitals.absorbance@Inert Mass}} |
| 每枚 Dormant Lance 的伤害 | {{guide:behaviour.ability:rocket.damageMin@Inert Mass}}–{{guide:behaviour.ability:rocket.damage@Inert Mass}} | {{guide:behaviour.ability:rocket.damageMin*1.5@Inert Mass}}–{{guide:behaviour.ability:rocket.damage*1.5@Inert Mass}} | {{guide:behaviour.ability:rocket.damageMin*2@Inert Mass}}–{{guide:behaviour.ability:rocket.damage*2@Inert Mass}} |
| 速度 | {{guide:vitals.speed@Inert Mass}} | {{guide:vitals.speed@Inert Mass}} | {{guide:vitals.speed@Inert Mass}} |
| 火箭射程 | 5,000 | 5,000 | 5,000 |
| 仇恨范围 | {{guide:vitals.aggro@Inert Mass}} | {{guide:vitals.aggro@Inert Mass}} | {{guide:vitals.aggro@Inert Mass}} |
| 信用点 | {{guide:spoils.pay.credits@Inert Mass}} | {{guide:spoils.pay.credits*2@Inert Mass}} | {{guide:spoils.pay.credits*3@Inert Mass}} |
| Thulium | {{guide:spoils.pay.thulium@Inert Mass}} | {{guide:spoils.pay.thulium*2@Inert Mass}} | {{guide:spoils.pay.thulium*3@Inert Mass}} |
| 经验值（XP） | {{guide:spoils.pay.experience@Inert Mass}} | {{guide:spoils.pay.experience*2@Inert Mass}} | {{guide:spoils.pay.experience*3@Inert Mass}} |
| 荣誉 | {{guide:spoils.pay.honor@Inert Mass}} | {{guide:spoils.pay.honor*2@Inert Mass}} | {{guide:spoils.pay.honor*3@Inert Mass}} |
| 每次击杀的 PvE 积分 | 15 | 15 | 15 |

**掉落**：一个货箱，归造成伤害最多的飞行员。

| 物品 |
| :--- |
| {{guide:spoils.box@Inert Mass}} |

### The Unwakened

只有一个，在沼泽中央，别处没有；被击毁后 {{guide:vitals.respawn@The Unwakened}} 回来。自 Deep Void 开启以来，它可以被摧毁了，并和这里的其他外星人一样按造成的伤害支付报酬。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@The Unwakened}} | {{guide:vitals.hull*1.5@The Unwakened}} | {{guide:vitals.hull*2@The Unwakened}} |
| 护盾 | {{guide:vitals.shield@The Unwakened}} | {{guide:vitals.shield*1.5@The Unwakened}} | {{guide:vitals.shield*2@The Unwakened}} |
| 护盾吸收率 | {{guide:vitals.absorbance@The Unwakened}} | {{guide:vitals.absorbance@The Unwakened}} | {{guide:vitals.absorbance@The Unwakened}} |
| 光环每秒对内部每艘飞船的伤害 | {{guide:behaviour.ability:aura.damagePerSecond@The Unwakened}} | {{guide:behaviour.ability:aura.damagePerSecond*1.5@The Unwakened}} | {{guide:behaviour.ability:aura.damagePerSecond*2@The Unwakened}} |
| 光环半径 | 700 | 700 | 700 |
| 速度 | {{guide:vitals.speed@The Unwakened}} | {{guide:vitals.speed@The Unwakened}} | {{guide:vitals.speed@The Unwakened}} |
| 仇恨范围 | {{guide:vitals.aggro@The Unwakened}} | {{guide:vitals.aggro@The Unwakened}} | {{guide:vitals.aggro@The Unwakened}} |
| 信用点 | {{guide:spoils.pay.credits@The Unwakened}} | {{guide:spoils.pay.credits*2@The Unwakened}} | {{guide:spoils.pay.credits*3@The Unwakened}} |
| Thulium | {{guide:spoils.pay.thulium@The Unwakened}} | {{guide:spoils.pay.thulium*2@The Unwakened}} | {{guide:spoils.pay.thulium*3@The Unwakened}} |
| 经验值（XP） | {{guide:spoils.pay.experience@The Unwakened}} | {{guide:spoils.pay.experience*2@The Unwakened}} | {{guide:spoils.pay.experience*3@The Unwakened}} |
| 荣誉 | {{guide:spoils.pay.honor@The Unwakened}} | {{guide:spoils.pay.honor*2@The Unwakened}} | {{guide:spoils.pay.honor*3@The Unwakened}} |
| 每次击杀的 PvE 积分 | 112 | 112 | 112 |

**掉落**：一个货箱，归造成伤害最多的飞行员。

| 物品 |
| :--- |
| {{guide:spoils.box@The Unwakened}} |

<!-- swamp-members:end -->

## Deep Void 开启之后 {#with-the-deep-void}

Deep Void 在这里带来的变化，简要如下：

- **Unwakened 可以被摧毁了。** 它不再无敌：和这里的其他外星人一样按造成的伤害支付报酬，并在死亡一天后复活。
- **炮台可以被摧毁了。** 三座炮台（同时发射 N.I.K.E. 和 N.U.K.E. 的火箭炮塔，以及两座激光炮塔）现在都有耐久，激光和火箭都能伤害它们。被摧毁的炮台在 Unwakened 复活前一直失效。
- **第一次击杀会打开 Threshold。** 每个世界本赛季第一次击杀 Unwakened 时，会在 `DS-4` 的另一角打开该世界的 Threshold，[Deep Void](/wiki/03-Mechanics/Deep-Void.md) 就从那里开始。

## 在这里该做什么 {#what-to-do-here}

- **第一次击杀会打开通路。** 本赛季第一次击杀 Unwakened 会打开该世界的 Threshold，也就打开了通往 [Deep Void](/wiki/03-Mechanics/Deep-Void.md) 的路；区域内炮台几秒钟就能摧毁一艘飞船。区域之外，围绕区域一圈巡逻的 Void 是沼泽的第一道防线，也是小队可以不受炮台影响战斗的地方。
- **用穿透对付 Void。** Void 的大护盾会吸收一次命中的 {{guide:vitals.absorbance@Slumbering Void;Inert Mass;The Unwakened}}，却几乎无关紧要：后面的船体很小。你的激光护盾穿透越高，它倒得越快（[激光与弹药](/wiki/06-Items/Lasers.md)）。
- **远离 Lance。** Inert Mass 看得很远，而 Lance 是甩不掉的：用隐形、EMP、安全环或跳跃打断它的锁定，或者离开它的射程。即使对一支由最强飞船组成的大型小队来说，一只 Mass 也是一场漫长的战斗。
- **Dormant 虫群**现在出现在区域刚好之外，所以小队可以在炮台之外等它。见 [Dormant 虫群](/wiki/05-Swarms/Dormant-Swarm.md)。

## 延伸阅读 {#where-to-read-more}

- [危险星区](/wiki/01-General/Danger-Sectors.md)：第 11 天改变了什么。
- [巨型挖掘机](/wiki/03-Mechanics/Giant-Excavator.md)：Slumbering Void 的波次和它们守护的东西。
- [虫群](/wiki/05-Swarms/Swarms.md)和 [Dormant 虫群](/wiki/05-Swarms/Dormant-Swarm.md)：击杀首领如何支付。
- [火箭](/wiki/06-Items/Rockets.md#the-craft-only-rockets)：炮塔发射的 N.I.K.E. 和 N.U.K.E.。
- [黑洞](/wiki/03-Mechanics/Black-Hole.md)：`DS-4` 的另一个危险。
- [货箱](/wiki/03-Mechanics/Cargo.md)：外星人掉落的货箱。
