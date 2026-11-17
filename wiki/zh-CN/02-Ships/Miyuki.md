<!-- wiki-i18n source: 5ac83735773f6626 -->
<!-- wiki-i18n title: Miyuki -->
# Miyuki

Miyuki 是一艘分为五个等级的支援舰船。你在装配站像制造其他舰船一样制造 1 级，然后把同一艘舰船就地改装为 2、3、4、5 级：每一级都由低一级制造而来，舰船上装备的一切都会保留。每升一级就多一个激光槽位和一个装甲槽位，这些槽位都是需要研究的科技。

## 属性 {#stats}

- **生命值（HP）**：128,000
- **基础速度**：270
- **激光槽位**：5
- **附加槽位**：3
- **装甲槽位**: 5

### 发生器与支援槽位 {#generator-support-slots}

- **核心槽位（100% 效率）**：3
- **支援槽位（75% 效率）**：3
- **辅助槽位（50% 效率）**：2

---

## 价格 {#price}

- **信用点**：0（在装配站制造）
- **Thulium**：0

## 等级 {#levels}

上面的属性是 1 级的。高于第一级的等级，在装配站由低一级的 Miyuki 制造：还是同一艘舰船，就地改装，所以装备和配置都会保留。等级不能跳过，也不能购买。

| 等级 | 船体 | 基础速度 | 激光 | 装甲 | 核心 / 支援 / 辅助 | 护盾容量 | 护盾吸收率 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Miyuki** | 128,000 | 270 | 5 | 5 | 3 / 3 / 2 | – | – |
| **Miyuki II** | 134,400 | 270 | 6 | 6 | 3 / 3 / 2 | +5% | +2% |
| **Miyuki III** | 141,120 | 270 | 7 | 7 | 3 / 3 / 2 | +10.25% | +4.04% |
| **Miyuki IV** | 148,176 | 320 | 8 | 8 | 3 / 3 / 2 | +15.76% | +6.12% |
| **Miyuki V** | 155,585 | 320 | 9 | 9 | 4 / 4 / 4 | +21.55% | +8.24% |

护盾容量和护盾吸收率是相对于 1 级的加成。

在装配站制造一个等级所需的东西（低一级的 Miyuki 本身会被改装为新等级）：

| 等级 | 研究 | 制造时间 | Thulium | 材料 |
| :--- | :--- | ---: | ---: | :--- |
| **Miyuki** | 1 天、10 个 Dark Matter | 15分钟 | 6,000 | 160 Ship Fragment、25 Reinforced Hull Plate、10 Power Core、1 Ancient Control Unit |
| **Miyuki II** | 1 天、10 个 Dark Matter | 10分钟 | 20,000 | 80 Ship Fragment、8 Reinforced Hull Plate、4 Power Core、8 Dark Matter Plate |
| **Miyuki III** | 1 天、10 个 Dark Matter | 10分钟 | 35,000 | 120 Ship Fragment、10 Reinforced Hull Plate、6 Power Core、1 Ancient Control Unit、8 Dark Matter Plate |
| **Miyuki IV** | 2 天、10 个 Dark Matter | 15分钟 | 50,000 | 180 Ship Fragment、18 Reinforced Hull Plate、9 Power Core、2 Ancient Control Unit、8 Dark Matter Plate |
| **Miyuki V** | 2 天、10 个 Dark Matter | 15分钟 | 75,000 | 240 Ship Fragment、25 Reinforced Hull Plate、12 Power Core、3 Ancient Control Unit、8 Dark Matter Plate |

## 能力 {#abilities}

Miyuki 的能力属于舰船，而不是某件物品：不占用能力槽，也不需要装备任何东西。每个能力如何运作见[舰船能力](/wiki/03-Mechanics/Abilities.md#ship-abilities)；这张表说明每个等级拥有什么。

| 等级 | Heal Pod | Channel Heal | Channel Shield |
| :--- | :--- | :--- | :--- |
| **Miyuki** | 7.5 秒，20,000 + 2% | – | – |
| **Miyuki II** | 7.5 秒，20,000 + 2% | 每秒 50,000 船体（你 10,000），120 秒 | – |
| **Miyuki III** | 7.5 秒，30,000 + 3% | 每秒 50,000 船体（你 10,000），120 秒 | 每秒 75,000 护盾（你 15,000），120 秒 |
| **Miyuki IV** | 7.5 秒，30,000 + 3% | 每秒 75,000 船体（你 10,000），100 秒 | 每秒 75,000 护盾（你 15,000），120 秒 |
| **Miyuki V** | 7.5 秒，30,000 + 3% | 每秒 75,000 船体（你 10,000），100 秒 | 每秒 75,000 护盾（你 15,000），120 秒 |

连接持续 5 秒，可达你小队或企业中 1,200 单位内的舰船。Heal Pod 可达 600。

## 研究 {#research}

- **等级。** Miyuki II 至 V 是 Skylab 里各自独立的科技，每一级都排在低一级之后：II 和 III 需要 1 天，IV 和 V 需要 2 天，每项都需要 10 个 Dark Matter。在研究视图中，五个等级上下排列，每一级都有一个箭头指向下一级：II 在 I 之后研究，III 在 II 之后，IV 在 III 之后，V 在 IV 之后。
- **槽位。** 装甲槽位、第 6 个起的激光槽位和第 9 个起的发生器槽位，都是 Skylab 里独立的科技，每项需要 1 小时和 10 个 Dark Matter：装甲槽位 1 至 9 从第一个起依次研究，激光槽位 6 至 9（各排在对应等级之后），发生器槽位 9 至 12（各排在 5 级之后）。槽位一经研究就会在舰船上开启，无论它是几级；尚未研究的槽位在机库里显示为锁定。
- **装甲槽位。** Miyuki 在 1 级有 5 个、在 5 级有 9 个用于[船体装甲](/wiki/06-Items/Hull-Plating.md)的[装甲槽位](/wiki/06-Items/Hull-Plating.md#hull-plate-slots)，制造出来时全部锁定。9 个槽位全部装上 Hull Plating III，可增加 225,000 点船体。

<!-- research-ship:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **先研究。** 只有研究完这艘舰船的科技后，装配站才能制造它：研究时间 1 天，另需把 10 个 Dark Matter 放入研究中心。该科技位于[研究](/wiki/03-Mechanics/Research.md)页面的[舰船科技树](/wiki/03-Mechanics/Research.md#tree-ships)中。
- **更多附加槽位。** 安装在你的 Skylab 中的 Extra Slots CPU I、II、III，分别为这艘舰船增加 3、5、7 个附加槽位，加上它本来就有的 3 个，总共是 6、8、10 个。它们和其他物品一样先研究、再制造：见 [Extra Slots CPUs](/wiki/06-Items/Extras.md#extra-slots-cpus)。

<!-- research-ship:end -->

## 背景故事 {#lore}

Miyuki 诞生于 Skylab 的船坞，起因是一个问题：如果守护舰队的那艘舰船能和驾驶它的飞行员一起成长，会怎么样？每次改装都会保留装备和配置，并让它各方面都强一点。Miyuki V 就是飞行员在第一天出击的那艘舰船，成长到了旗舰的体量。
