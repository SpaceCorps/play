<!-- wiki-i18n source: 0dfda8fd6d9be79d -->
<!-- wiki-i18n title: 无人机 -->
# 无人机 {#drones}

无人机是可购买或可制造的支援单位。你最多可同时启用 **8 台无人机**，Slave Drone 和 Master Drone 合计。

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## 物品树 {#item-tree}

装配站制造的东西要先有对应的科技；将指针悬停在物品上可看到研究所需的时间。科技树、燃料和加速见 [研究](/wiki/03-Mechanics/Research.md)。

```tree
Slave Drone | drone, common | buy 100000 Credits | /wiki/06-Items/Drones.md#available-drones
Master Drone | drone, rare | craft 40000 Thulium, 60 s | research 36000 s, 36000 science | 1 Slave Drone, 100 Ship Fragment | /wiki/06-Items/Drones.md#available-drones

Slave Drone => Master Drone
```
<!-- item-tree:end -->

## 可用的无人机 {#available-drones}

| 名称 | 稀有度 | 槽位 | 说明 | 费用 |
| :--- | :--- | :--- | :--- | :--- |
| **Slave Drone** | 普通 | 1 | 只有一个装备槽位的基础无人机。它会随着你消灭外星人而成长，共 8 个等级。 | 100,000 信用点起（见下文） |
| **Master Drone** | 稀有 | 2 | 在装配站由 Slave Drone 升级而来。它以金色飞行，保留自己的编号和所携带的装备，获得第二个装备槽位，并从 1 级重新开始。 | 升级一台 Slave Drone：40,000 Thulium 和 100 个 Ship Fragment |

Slave Drone 一开始是一颗小球体，到 8 级时会成长为一艘装甲炮艇。每当你消灭一个外星人，你拥有的每台无人机都会获得同样的经验值，而更高的等级会为其槽位中的激光增加少量伤害（8 级时最高 +7%）。各个等级以及每一级所需的经验值，见“游戏机制”分类下的无人机机制页面。制造 Master Drone 不会消耗一台无人机：它会就地升级你所选的那台 Slave Drone，升级完成时**它的等级和经验值会重置为 0**（装配站会提示这一点，并要求你确认）。作为补偿，这台无人机会拥有**两个装备槽位**，而不是一个：它原来携带的装备留在第一个槽位，第二个槽位为空。你的无人机连同等级和经验值，会在赛季重置后保留。

## Slave Drone 价格 {#slave-drone-prices}

你每买一台 Slave Drone，价格都比上一台更高。价格取决于你购买时持有的无人机数量（一台 Master Drone 算作一台），商店始终显示你下一台的价格。前三台只需信用点；从第四台起，还要加上 Thulium。

| 无人机 | 信用点 | Thulium |
| :---- | :--------- | :------ |
| 第 1 台 | 100,000 | – |
| 第 2 台 | 200,000 | – |
| 第 3 台 | 400,000 | – |
| 第 4 台 | 800,000 | 10,000 |
| 第 5 台 | 1,600,000 | 20,000 |
| 第 6 台 | 3,200,000 | 30,000 |
| 第 7 台 | 6,400,000 | 40,000 |
| 第 8 台 | 12,800,000 | 50,000 |

八台合计需要 25,500,000 信用点和 150,000 Thulium。你的无人机会在赛季重置后保留，所以价格会从你已持有的数量继续往后算：持有三台时，你的下一台永远是第 4 台；持有八台时，就没有可买的了。

## 使用方法 {#usage}

1. 在商店**购买** Slave Drone。想要金色的那台时，在装配站把其中一台**升级**为 Master Drone（它的等级和经验值会重新开始）。
2. 在机库的“无人机”标签页中**装备**它们。
3. 为它们**装上**激光或护盾来增强你的实力：Slave Drone 有一个槽位，Master Drone 有两个。激光与你的舰船一同开火；护盾则按装在核心槽位中的护盾计算，其全部属性都会生效。
4. 通过消灭外星人为它们**升级**：机库会显示每台无人机的等级，以及下一级还需要多少经验值。
