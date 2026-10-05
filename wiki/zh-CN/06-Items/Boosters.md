<!-- wiki-i18n source: 380267094f925178 -->
<!-- wiki-i18n title: 增益 -->
# 增益 {#boosters}

增益提供临时的属性加成，强化你舰船的战斗、防御、升级和资源收集能力。

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## 物品树 {#item-tree}

装配站制造的东西要先有对应的科技；将指针悬停在物品上可看到研究所需的时间。科技树、燃料和加速见 [研究](/wiki/03-Mechanics/Research.md)。

```tree
Experience Kit | booster, common | buy 8000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Honor Beacon | booster, common | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Damage Amp II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Regen | booster, rare | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Resource Magnet | booster, rare | buy 18000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Damage Amp | booster, rare | buy 20000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Loot Luck | booster, legendary | buy 30000 Thulium | /wiki/06-Items/Boosters.md#active-boosters

Shield Wall -> Shield Wall II
Hull Plating -> Hull Plating II
Damage Amp -> Damage Amp II
```
<!-- item-tree:end -->

## 叠加规则 {#stacking-rules}

增益采用加法叠加机制：
1. **加成百分比相加叠加**：如果你购买了两种不同的增益，且都提供 +10% 激光伤害，你将获得合计 **+20% 激光伤害** 的加成。
2. **持续时间按倍数叠加**：多次购买*同一种*增益会延长它的生效时间。*不同*增益的计时器则并行运行。
3. **计时查看**：生效中的增益显示在 HUD 的“增益”窗口中，列出按类别汇总的生效加成总和，以及下一个到期的时间点。

---

## 生效中的增益 {#active-boosters}

每个增益的基础持续时间都是 **10 小时**，购买、收到或领取后立即生效。三种 **II** 增益不出售：你要先在 Skylab 里研究它们的科技（[研究](/wiki/03-Mechanics/Research.md)），再到装配站制造；领取一个时，它的 10 小时会像购买时一样立刻开始。

| 名称 | 稀有度 | 基础效果（10 小时） | 价格（Thulium） |
| :--- | :--- | :--- | :--- |
| **Damage Amp** | 稀有 | +10% 激光伤害 | 20,000 |
| **Damage Amp II** | 稀有 | +10% 激光伤害 | 装配站：20,000 |
| **Shield Wall** | 稀有 | +25% 护盾容量（护盾点数上限） | 15,000 |
| **Shield Wall II** | 稀有 | +25% 护盾容量（护盾点数上限） | 装配站：15,000 |
| **Hull Plating** | 稀有 | +10% 最大生命值 | 15,000 |
| **Hull Plating II** | 稀有 | +10% 最大生命值 | 装配站：15,000 |
| **Shield Regen** | 稀有 | +25% 护盾充能速率（每秒恢复的护盾点数） | 10,000 |
| **Experience Kit** | 普通 | +20% 经验值获取 | 8,000 |
| **Honor Beacon** | 普通 | +20% 荣誉点数获取 | 10,000 |
| **Resource Magnet** | 稀有 | +25% 货箱产出 | 18,000 |
| **Loot Luck** | 传说 | +5% 来自 NPC 的稀有掉落率 | 30,000 |

---

## 护盾增益：三种类型 {#shield-boosts-three-kinds}

护盾有三项各自独立的属性，每一种护盾增益只会提升其中恰好一项。“增益”窗口把它们分开显示，每一项都有自己的图标和总值：

| 类型 | 含义 | 提升它的增益 |
| :--- | :--- | :--- |
| **护盾容量** | 你的护盾点数上限 | Shield Wall、Shield Wall II，以及永久加成 **Shield Capacity Boost**（赛季商店） |
| **护盾吸收率** | 每次攻击中由护盾承受的份额（其余落在船体上）；可以超过 100% | 永久加成 **Shield Absorbance Boost**（赛季商店）：每级 +0.1 点，每级需 25 重置点数，最多 +10 点。没有任何增益能提升它 |
| **护盾充能** | 每秒恢复的护盾点数 | Shield Regen。没有任何永久加成能提升它 |

同一类型的增益会相加，绝不会计入另一类型。永久加成在[跨赛季进度](/wiki/03-Mechanics/Wipe-Timeline.md)中介绍；各项属性本身在[护盾机制](/wiki/03-Mechanics/Shields.md)中介绍。
