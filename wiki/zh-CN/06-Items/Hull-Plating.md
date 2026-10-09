<!-- wiki-i18n source: 2bd1925e336e25b6 -->
<!-- wiki-i18n title: 船体装甲 -->
# 船体装甲 {#hull-plating}

<!-- wiki-search: hull plate; hull plate slot; hull plate slots; plate slot; plate; armour; armor; hpl; 船体装甲; 装甲槽位; 装甲板 -->

对 Dormant 虫群的研究显示出装甲技术的进步。借助这项技术，飞船可以强化自己的船体：**船体装甲**是装入已制造飞船船体装甲槽位、为其增加船体值的装甲。它不是[增益](/wiki/06-Items/Boosters.md)页面里的 Hull Plating **Booster**，后者是限时加成。

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## 物品树 {#item-tree}

装配站制造的东西要先有对应的科技；将指针悬停在物品上可看到研究所需的时间。科技树、燃料和加速见 [研究](/wiki/03-Mechanics/Research.md)。

```tree
Hull Plating I | hull-plating, uncommon | buy 5000 Thulium | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating II | hull-plating, rare | craft 2500 Thulium, 300 s | research 86400 s, 86400 science, 25 Dark Matter | 1 Hull Plating I, 150 Ship Fragment, 20 Reinforced Hull Plate, 6 Power Core, 5 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating III | hull-plating, epic | craft 4000 Thulium, 600 s | research 172800 s, 172800 science, 40 Dark Matter | 1 Hull Plating II, 300 Ship Fragment, 40 Reinforced Hull Plate, 12 Power Core, 1 Ancient Control Unit, 8 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings

Hull Plating I => Hull Plating II => Hull Plating III
```
<!-- item-tree:end -->

## 三种装甲 {#the-three-platings}

| 物品 | 增加的船体值 | 来源 |
| :--- | ---: | :--- |
| **Hull Plating I** | 5,000 | 商店，5,000 Thulium |
| **Hull Plating II** | 10,000 | 装配站，由 Hull Plating I 升级 |
| **Hull Plating III** | 15,000 | 装配站，由 Hull Plating II 升级 |

Hull Plating I 是买来的。**II 和 III 是升级**：装配站会消耗一块低一阶的装甲（要放在物品栏里，不能装在舰船上），并需要 Thulium、材料和 **Dark Matter Plate**，II 需要 5 块，III 需要 8 块，而任何其他装备的最后一阶只需要 3 块。每一块都要先有对应的科技，位于[研究](/wiki/03-Mechanics/Research.md#tree-hull-plating)页的 Hull Plating 科技树中：II 需要 1 天和 25 个 Dark Matter，III 需要 2 天和 40 个，另外还要有 Dark Matter Plate 本身的科技。上面的科技树列出了价格、材料和时间。

[锻造炉](/wiki/06-Items/Forge.md)可以处理每一种装甲，升级会保留被消耗装甲的锻造等级，并重新掷出它的加成。装甲只有一项属性，也就是船体，所以只带一条加成，按等级从 +2% 到 +15%：一块永恒等级的 Hull Plating III 最多可增加 17,250。[拍卖行](/wiki/03-Mechanics/Auction.md)可以上架 Hull Plating II 和 III，但不能上架商店出售的 Hull Plating I。

## 装甲槽位 {#hull-plate-slots}

船体装甲只能装进**装甲槽位**。这是你在装配站制造的四艘舰船除激光、发生器、附加、技能和无人机槽位之外另有的一种槽位：

| 舰船 | 装甲槽位 | 一整套 Hull Plating III 增加 |
| :--- | ---: | ---: |
| **Paragon** | 5 | 75,000 |
| **Storm** | 7 | 105,000 |
| **Ironclad** | 15 | 225,000 |
| **Wraith** | 9 | 135,000 |

- **起初全部锁定。** 槽位要在 Skylab 里研究后才会开启：每个槽位一项科技，需要 1 小时和 10 个 Dark Matter，从第一个起依次进行。[研究](/wiki/03-Mechanics/Research.md#ship-technologies)视图把一艘舰船的槽位显示为一张卡片，每个槽位一个圆点。
- **按舰船种类，而不是按单艘舰船。** 你为 Paragon 开启的槽位，在 Paragon 的每一种设计上也是开启的（[舰船设计](/wiki/03-Mechanics/Ship-Designs.md)）。科技永远属于你：重置也会保留。
- **两种配置共用。** 装甲属于舰船：切换配置时它们仍然装着，机库在两种配置里显示的是同样的装甲。
- **任意混搭。** 槽位可以装任何一种船体装甲，两块相同的也没问题。
- **你的船体比例不变。** 装上或卸下装甲，都会保持你现有的船体比例，所以装甲不会治疗你，也不会伤到你。
- **和所有装备一样**，装甲在机库里装卸，或者在安全区内通过机库窗口装卸，绝不能在野外进行。没有研究的槽位会拒绝装甲。

在机库里，**船体装甲**卡片显示这些槽位。空着的开启槽位像其他槽位一样，拖放即可装入装甲；锁定的槽位显示一把锁，点击会打开 Skylab 的研究。其他属性旁边的一个图块会把已装装甲提供的数值加起来。

## 船体如何叠加 {#how-the-hull-adds-up}

装甲把自己的船体加到舰船本身的船体上，机库和舰船窗口显示的是更大的数字。舰船的船体加上装甲，随后仍然经过原来的那些倍率：[Hull Plating Booster](/wiki/06-Items/Boosters.md) 和你所佩戴的[无人机编队](/wiki/03-Mechanics/Formations.md)。改变船体的设计（BUCKY 多 25%）改变的是舰船本身的船体，装甲再叠加在其上。

## Hull Plating 还是 Hull Plating Booster？ {#hull-plating-or-booster}

有两样东西同名。**船体装甲**（本页）是一种护甲：一块装进已制造舰船的装甲槽位的板，装着的时候就增加它的船体。**Hull Plating Booster** 是[增益](/wiki/06-Items/Boosters.md)页上的限时加成，在你驾驶的任何舰船上提供 10 小时的 +10% 最大生命值，没有东西可装。两者会叠加：先算装甲，Booster 的 10% 在总数上计算。
