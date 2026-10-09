<!-- wiki-i18n source: a8a96edb9a5070f1 -->
<!-- wiki-i18n title: Dormant Swamp -->
# Dormant Swamp

<!-- wiki-search: swamp; dormant swamp; base; turret; turrets; nike turret; laser turret; inert mass; unwakened; the unwakened; slumbering void; void; dormant lance; ds-4; 沼泽; 炮塔; 炮台 -->

很久以前，银河中央住着一个先进的文明。它用泛着紫光脉络的紫黑色晶体建造，因为一个无人知晓的原因崩溃了。**Dormant Swamp** 是它的前哨，位于 `DS-4` 的左上角。从赛季第 11 天起它开始躁动：中央的炮台向看到的每艘飞船开火，**Inert Mass** 守卫着它，正中心沉睡着 **Unwakened**。这是飞行员**暂时还不该去**的地方。隐形时你可以飞到 Unwakened 跟前，而目前在那里别的什么都做不了：基地和它的炮台无法被破坏、进入、登上或与之交易。

沼泽也是 [Dormant 虫群](/wiki/05-Swarms/Dormant-Swarm.md)从第 11 天起出现的地方，**Slumbering Void** 在它周围巡逻。同样的 Void 也会成波来到[巨型挖掘机](/wiki/03-Mechanics/Giant-Excavator.md#the-slumbering-voids)。星区见[危险星区](/wiki/01-General/Danger-Sectors.md)。

## 概览 {#at-a-glance}

<!-- swamp-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **位置**：`DS-4` 的左上角：中心在 5,000 / 5,000
- **出现**：从赛季第 11 天起，直到重置
- **区域**：围绕中心 4,300 单位：炮台所能到达的最远处，也是暂时还没人该去的地方
- **提示**：越过距中心 4,800 单位的那个环的飞船会收到一条系统行
- **隐形**：任何炮台都不会看到隐形的飞船，也不会看到处于 EMP 生效期内的飞船
- **外星人**：5 个 Inert Mass 留在距中心 2,400 单位以内。Unwakened 沉睡在中心。2 个 Slumbering Void 在距中心 4,600 到 6,500 单位之间巡逻。
- **Dormant 虫群**：它出现在 9,417 / 6,606，距中心 4,700 单位，位于区域之外
- **岩石**：中心 4,900 单位内没有小行星

<!-- swamp-glance:end -->

## 炮台 {#the-guns}

沼泽的炮塔会向射程内**它们能看到的最近的飞船**开火，不会向其他飞船开火：区域就是其中射程最远的那座所能到达的圆。它们不是任何意义上的实体：没有生命值，无法被锁定，你对它们开的火不会产生任何效果。它们的射击是真实的，世界会像缩放任何外星人的武器那样缩放它们的伤害。

<!-- swamp-guns:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

一发的伤害（各世界）：

| 炮台 | 位置 | 发射间隔 | 射程（单位） | Alpha | Beta | Gamma |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) 炮塔 | 5,000 / 4,400 | 2 秒 | 3,640 | 75,000 | 112,500 | 150,000 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) 炮塔 | 5,000 / 4,400 | 5 秒 | 1,080 | 50,000 | 75,000 | 100,000 |
| 激光炮塔 × 2 | 3,600 / 5,200; 6,400 / 5,200 | 1 秒 | 2,500 | 45,000–55,000 | 67,500–82,500 | 90,000–110,000 |

- 火箭在其射程的 90% 处发射，以保证命中；激光炮塔每秒开火一次，伤害在所示范围内随机。
- N.I.K.E. 的护盾穿透为 35%，会从护盾吸收率中扣除。
- N.U.K.E. 在半径 900 单位内爆炸，中心最强。

<!-- swamp-guns:end -->

- **区域之外什么也到不了，**区域内飞船会在几秒内被摧毁：越靠近中心，参与的炮台越多，连护盾最好的 Wraith 也撑不住。
- **隐形能让你进去。** 任何炮塔都不会看到隐形的飞船，也不会看到处于 EMP 生效期内的飞船，无论多远。瞄准一艘可见飞船的爆炸如果在隐形飞船旁炸开，仍会伤到它并解除它的隐形。
- **它们只向飞行员开火，**从不向外星人、企业飞行员或虫群开火，刚从被摧毁中回来的飞船的保护对它们同样有效。
- **提示环。** 越过区域之外那个环的飞船会收到一条系统行：炮塔会向看到的每艘飞船开火，中央有什么东西在沉睡。只有它离开环再回来时才会再次通知。
- **离开。** 如果你在那里被摧毁并选择就地复活，或在区域内登录，你会被放到外面。你点击的航线会绕开区域，点击的地点若在其中，会弹出提示警告你。

## 外星人 {#the-aliens}

失落文明的三种外星人住在这里，各有各的数字。它们像虫群首领一样**按造成的伤害**支付奖励：给予者是造成伤害至少达到[虫群](/wiki/05-Swarms/Swarms.md#the-rules-of-every-swarm)中所列比例的每名飞行员，货箱则归造成伤害最多的飞行员。击杀它们会像击杀虫群飞船一样，按奖励的比例增加你的 PvE 军衔积分（[军衔](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points)）。每个外星人的护盾在持续期间会吸收每次命中的 80%（[护盾](/wiki/03-Mechanics/Shields.md)）。

- **Slumbering Void。** 修长的猎手，游戏中最快的外星人（和装了 Afterburner III 的 Storm 一样快）。一些总在沼泽周围巡逻，另一些成波来到挖掘机。它具有攻击性，追猎它能看到的最近的飞行员，并且永远看不到隐形的飞船。
- **Inert Mass。** 带紫色裂纹的死寂巨体，有一座小空间站那么大。它们待在距沼泽中心固定的距离内，目前不会离开。它发射 **Dormant Lance**：射程极远的制导火箭，会一直追着飞船，直到它隐形、打开 EMP 窗口、进入安全环、跳跃或死亡。它比任何飞船都快，所以只有这些中断才管用。
- **Unwakened。** 沉睡在沼泽中央的巨碑，是任何地图上最大的东西，慢到永远追不上飞船。它什么也不发射，但它光环内的每艘飞船都会被烧伤，**无论是否隐形**。它**免疫**：射击和火箭会命中却毫无作用，目标窗口显示满格条和“免疫”一词。之后的活动会让它可以被战斗；下面它的奖励只是写下来了，现在还无法获得。

<!-- swamp-members:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

### Slumbering Void

2 个 Slumbering Void 在距沼泽中心 4,600 到 6,500 单位之间巡逻；被击毁的会在 1 小时 后回来。挖掘机的波次会带来更多同样的外星人。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | 25,000 | 37,500 | 50,000 |
| 护盾 | 150,000 | 225,000 | 300,000 |
| 护盾吸收率 | 80% | 80% | 80% |
| 激光伤害 （每秒一轮齐射） | 3,000 | 4,500 | 6,000 |
| 速度 | 400 | 400 | 400 |
| 激光射程 | 800 | 800 | 800 |
| 仇恨范围 | 2,500 | 2,500 | 2,500 |
| 信用点 | 23,000 | 46,000 | 69,000 |
| Thulium | 60 | 120 | 180 |
| 经验值（XP） | 3,600 | 7,200 | 10,800 |
| 荣誉 | 16 | 32 | 48 |
| 每次击杀的 PvE 积分 | 10 | 10 | 10 |

**掉落**：一个货箱，归造成伤害最多的飞行员。

| 物品 | 几率 | 数量 |
| :--- | ---: | ---: |
| Ultra Core 和 Experimental Fusion Core 中随机一种 | 60% | 30–60 |
| 4 种史诗级 [火箭](/wiki/06-Items/Rockets.md) 中随机一种 | 40% | 1–3 |

### Inert Mass

5 个 Inert Mass 站在距中心 2,400 单位以内；被击毁的会在 1 小时 后回来。每 6 秒 向它能看到的最近飞船发射一枚制导的 [Dormant Lance](/wiki/06-Items/Rockets.md#the-craft-only-rockets)：速度 750，飞行距离 5,250 单位，穿透 40%。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | 250,000 | 375,000 | 500,000 |
| 护盾 | 100,000 | 150,000 | 200,000 |
| 护盾吸收率 | 80% | 80% | 80% |
| 每枚 Dormant Lance 的伤害 | 5,000–8,000 | 7,500–12,000 | 10,000–16,000 |
| 速度 | 60 | 60 | 60 |
| 火箭射程 | 5,000 | 5,000 | 5,000 |
| 仇恨范围 | 5,000 | 5,000 | 5,000 |
| 信用点 | 125,000 | 250,000 | 375,000 |
| Thulium | 335 | 670 | 1,005 |
| 经验值（XP） | 20,200 | 40,400 | 60,600 |
| 荣誉 | 88 | 176 | 264 |
| 每次击杀的 PvE 积分 | 15 | 15 | 15 |

**掉落**：一个货箱，归造成伤害最多的飞行员。

| 物品 | 几率 | 数量 |
| :--- | ---: | ---: |
| Ultra Core 和 Experimental Fusion Core， 平均分配 | 100% | 共 400–800 |
| 4 种史诗级 [火箭](/wiki/06-Items/Rockets.md) 中随机一种 | 100% | 20–40 |
| N.I.K.E. | 5% | 1–2 |
| Dark Matter | 5% | 1–3 |
| Ancient Control Unit | 10% | 1 |
| Power Core | 25% | 1–2 |

### The Unwakened

只有一个，在沼泽中央，别处没有；被击毁后 24 小时 回来。在之后的任务关掉标记之前，它**免疫**：射击和火箭会命中却毫无作用。它的奖励只是写了下来，现在还无法获得。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | 10,000,000 | 15,000,000 | 20,000,000 |
| 护盾 | 10,000,000 | 15,000,000 | 20,000,000 |
| 护盾吸收率 | 80% | 80% | 80% |
| 光环每秒对内部每艘飞船的伤害 | 75,000 | 112,500 | 150,000 |
| 光环半径 | 700 | 700 | 700 |
| 速度 | 10 | 10 | 10 |
| 仇恨范围 | 3,000 | 3,000 | 3,000 |
| 信用点 | 7,500,000 | 15,000,000 | 22,500,000 |
| Thulium | 20,000 | 40,000 | 60,000 |
| 经验值（XP） | 1,200,000 | 2,400,000 | 3,600,000 |
| 荣誉 | 5,200 | 10,400 | 15,600 |
| 每次击杀的 PvE 积分 | 112 | 112 | 112 |

**掉落**：一个货箱，归造成伤害最多的飞行员。

| 物品 | 几率 | 数量 |
| :--- | ---: | ---: |
| Ultra Core 和 Experimental Fusion Core， 平均分配 | 100% | 共 10,000–15,000 |
| 4 种史诗级 [火箭](/wiki/06-Items/Rockets.md) 中随机一种 | 100% | 500–800 |
| N.I.K.E. | 100% | 20–30 |
| N.U.K.E. | 100% | 5–10 |
| Dark Matter | 100% | 40–60 |
| Ancient Control Unit | 100% | 10–20 |
| Power Core | 100% | 100–200 |

<!-- swamp-members:end -->

## 在这里该做什么 {#what-to-do-here}

- **只看，别碰。** 沼泽是留给以后的。不隐形时你能触及的唯一内容在区域之外：区域外围一圈巡逻的 Void 是沼泽的第一道防线，也是小队可以不受炮台影响战斗的地方。
- **用穿透对付 Void。** Void 的大护盾会吸收一次命中的 80%，却几乎无关紧要：后面的船体很小。你的激光护盾穿透越高，它倒得越快（[激光与弹药](/wiki/06-Items/Lasers.md)）。
- **远离 Lance。** Inert Mass 看得很远，而 Lance 是甩不掉的：用隐形、EMP、安全环或跳跃打断它的锁定，或者离开它的射程。即使对一支由最强飞船组成的大型小队来说，一只 Mass 也是一场漫长的战斗。
- **Dormant 虫群**现在出现在区域刚好之外，所以小队可以在炮台之外等它。见 [Dormant 虫群](/wiki/05-Swarms/Dormant-Swarm.md)。

## 延伸阅读 {#where-to-read-more}

- [危险星区](/wiki/01-General/Danger-Sectors.md)：第 11 天改变了什么。
- [巨型挖掘机](/wiki/03-Mechanics/Giant-Excavator.md)：Slumbering Void 的波次和它们守护的东西。
- [虫群](/wiki/05-Swarms/Swarms.md)和 [Dormant 虫群](/wiki/05-Swarms/Dormant-Swarm.md)：击杀首领如何支付。
- [火箭](/wiki/06-Items/Rockets.md#the-craft-only-rockets)：炮塔发射的 N.I.K.E. 和 N.U.K.E.。
- [黑洞](/wiki/03-Mechanics/Black-Hole.md)：`DS-4` 的另一个危险。
- [货箱](/wiki/03-Mechanics/Cargo.md)：外星人掉落的货箱。
