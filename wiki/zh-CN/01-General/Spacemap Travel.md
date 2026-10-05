<!-- wiki-i18n source: 6ad05a3dc7e0e2f6 -->
<!-- wiki-i18n title: 太空地图航行 -->
# 太空地图航行 {#spacemap-travel}

太空地图是你穿行 SpaceCorps 宇宙的导航界面。每个企业各自控制一片星区，这些星区按特定的拓扑结构排列，既便于安全探索，也会引出危险的 PvP 遭遇战。

![Galaxy Gates](../../img/wiki-img/shots/gates.jpg)
![Sector DS-1 as the game draws it](../../img/wiki-img/shots/sector-DS-1.jpg)
![Sector DS-2 as the game draws it](../../img/wiki-img/shots/sector-DS-2.jpg)
![Sector DS-3 as the game draws it](../../img/wiki-img/shots/sector-DS-3.jpg)
![Sector DS-4 as the game draws it](../../img/wiki-img/shots/sector-DS-4.jpg)
![Sector G-1 as the game draws it](../../img/wiki-img/shots/sector-G-1.jpg)
![Sector G-2 as the game draws it](../../img/wiki-img/shots/sector-G-2.jpg)
![Sector G-3 as the game draws it](../../img/wiki-img/shots/sector-G-3.jpg)
![Sector G-4 as the game draws it](../../img/wiki-img/shots/sector-G-4.jpg)
![Sector M-1 as the game draws it](../../img/wiki-img/shots/sector-M-1.jpg)
![Sector M-2 as the game draws it](../../img/wiki-img/shots/sector-M-2.jpg)
![Sector M-3 as the game draws it](../../img/wiki-img/shots/sector-M-3.jpg)
![Sector M-4 as the game draws it](../../img/wiki-img/shots/sector-M-4.jpg)
![Sector T-1 as the game draws it](../../img/wiki-img/shots/sector-T-1.jpg)
![Sector T-2 as the game draws it](../../img/wiki-img/shots/sector-T-2.jpg)
![Sector T-3 as the game draws it](../../img/wiki-img/shots/sector-T-3.jpg)
![Sector T-4 as the game draws it](../../img/wiki-img/shots/sector-T-4.jpg)
![The Star System map: the sectors, the PvP sectors, the gates and the company routes, with the portal ring that joins each company's x-4 sector to the next company's x-3 sector](../../img/wiki-img/shots/star-system.jpg)

## 宇宙结构 {#the-universe-structure}

宇宙由三个主要的企业星区（Mars、Terra、Galactic）和一个位于中央的 PvP 区域组成。

- **x-1（母星区）**：各企业的起始地图（M-1、T-1、G-1）。最安全的区域。
- **x-2 -> x-3**：外星人逐级变强的扩张区域。
- **x-4（边境星区）**：通往 PvP 星区的门户，也通往另一家企业的 `x-3`（见下文的星环）。
- **DS-x（危险星区）**：连接所有企业的中央 PvP 区域：DS-1 至 DS-4。

只有基地（母星区）设有空间站。**Mission Control** 就在那里打开，空间站的安全区覆盖其周围 1,600 单位。危险星区没有空间站，`DS-1` 也不例外：那里唯一的安全区，是跃迁门周围半径 660 单位的保护环，也无法打开 Mission Control；请飞回你的基地处理任务。

每个[世界](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)（Alpha、Beta、Gamma）都有一份这整张地图的独立副本，飞行员可以在哪些星区互相交战，取决于所在的世界：Alpha 中只有 `x-4` 和 `DS-x` 可以，Beta 中除 `x-1` 外处处可以，Gamma 中则处处可以。星系地图会按你所在世界的规则给各星区着色。

## 可视化 {#visualization}

下方的星系地图实时显示已知宇宙的布局。在游戏里，同一张地图就是**星系**窗口。

```spacemap

```

装备了 [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) 后，地图还能用来选择目的地：按下快捷栏里该 CPU 的槽位（**JMP**），星系窗口就会以选择模式打开。CPU 能带你去的星区会亮起，你自己所在的星区和危险星区则不亮。把鼠标指向亮起的星区可以看到价格，点击它，并在地图询问时确认跳跃（500 Thulium）。

## 如何航行 {#how-to-travel}

太空地图上的航行通过**传送门**（跃迁门）进行。[Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) 是另一条路：它不需要传送门（见本页末尾）。

1. **找到传送门**：传送门通常位于地图的角落或边缘。
2. **导航**：驾驶你的舰船飞近传送门主体。
3. **启动**：在距离传送门 500 单位以内按 **'J'** 开始跃迁。
4. **等待**：跃迁**需要 3 秒**。在此期间，快捷栏上方的进度条（“跃迁中…”）会逐渐填满，传送门也会随着充能而越来越亮；你跃迁时，其他飞行员也能在传送门上看到同样的充能效果。你的舰船仍可继续飞行，但在时间结束前必须一直留在传送门 500 单位范围内：飞出范围，跃迁就会被取消（“距离传送门太远，无法跃迁。”，进度条变红）。跃迁过程中再次按 **'J'** 不会有任何效果，只会给你一条提示。
5. **目的地**：你会抵达目标地图中对应的传送门。

### 遭受攻击时跃迁 {#jumping-under-fire}

- **在危险星区之外**，无论被外星人还是其他飞行员攻击，都**不会**打断你的跃迁：跃迁会正常完成。
- **在危险星区（`DS-1` 至 `DS-4`）**中，受到攻击时无法跃迁离开。如果有飞行员或外星人在最近 **10 秒**内击中过你的舰船（护盾或船体），跃迁就无法开始（“你正遭受攻击：无法从危险星区跃迁离开。”），而在跃迁过程中被击中则会取消跃迁（进度条变红，游戏会告诉你原因）。黑洞辐射造成的伤害不算攻击，被安全区挡下的射击也不算。你在出发地图上受到的攻击不会跟着你穿过传送门：你抵达时记录是清白的。
- 你一次只能做一件事：跃迁期间无法拾取[货箱](/wiki/03-Mechanics/Cargo.md)，而开始跃迁会放弃你已经开始的拾取。
- 跃迁途中关闭游戏或返回基地都会取消跃迁：你不会抵达目的地。
- **CPU 的传送和传送门跳跃一样需要充能。** Jump CPU 充能 5 秒，Base CPU 充能 10 秒，快捷栏上方会出现一条进度条。你开火或被击中，不论在哪个星区，都会取消传送（不会扣费，也不会消耗任何东西），而且在开火或被击中后的 10 秒内，两种 CPU 都无法启动。再按一次该 CPU 的槽位，就可以自己取消。

### 跃迁连接 {#jump-links}

- **企业环线**：Mars、Terra 和 Galactic 的布局相同。连接关系为 `1 <-> 2 <-> 3`、`2 <-> 4` 和 `3 <-> 4`。这使次级地图（`x-2` 和 `x-3`）与边境地图（`x-4`）之间形成一个环，而 `x-1` 则是一条只与 `x-2` 相连的安全入口尾端：你的起始地图只有一个传送门。
- **危险星区入口门**：每个企业的边境地图（`x-4`）都直接连接到它自己的危险星区：
  - `M-4` 连接到 `DS-1`
  - `T-4` 连接到 `DS-2`
  - `G-4` 连接到 `DS-3`
- **星环**：每家企业的边境地图（`x-4`）还有一道传送门，通往**下一家企业**的 `x-3`，而每个 `x-3` 都有一道门通回来。这三条连接围着危险星区形成一个环，所以每家企业都有一条出路和一条入路：
  - `M-4` 连接到 Terra 的 `T-3`
  - `T-4` 连接到 Galactic 的 `G-3`
  - `G-4` 连接到 Mars 的 `M-3`

  星环向所有飞行员开放，无论他们为哪家企业效力：它是企业地图之间的第二条通路，不必穿过 PvP 区域。星环传送门立在所在地图自己的一个角落里，远离该地图的其他传送门，周围有照常的半径 660 单位的安全区，跃迁方式与任何传送门相同。你在对面会不会遭到攻击，和别处一样取决于你所在的世界：在 Alpha 中 `T-3` 不是 PvP 星区而 `T-4` 是，在 Beta 中两者都是，在 Gamma 中每个星区都是。
- **入侵路线（企业间航行）**：通过传送门进入另一家企业的领地有两条路。近的一条是星环：Mars 飞行员从 `M-4` 经星环传送门进入 Terra 的 `T-3`（从 Mars 基地出发三次跃迁，`M-1` → `M-2` → `M-4` → `T-3`），再前往 `T-4` 或 `T-2`；Galactic 的 `G-4` 同样通往 Mars 的 `M-3`，Terra 的 `T-4` 通往 Galactic 的 `G-3`。远的一条要穿过 PvP 区域：从 `M-4` 飞入危险星区 `DS-1`，穿过传送门前往 `DS-2`，再经由 `T-4` 进入 Terra 的星区；要前往 Galactic，则穿过传送门前往 `DS-3`，再经由 `G-4` 进入。
- **危险星区三角**：`DS-1`、`DS-2` 和 `DS-3` 彼此相连。它们各自有一个企业的传送门（Mars 在 `DS-1`，Terra 在 `DS-2`，Galactic 在 `DS-3`）；`DS-4` 没有。
- **核心中枢**：外围的三个危险星区（`DS-1`、`DS-2` 和 `DS-3`）都直接连接到中央地图 **`DS-4`**，它是宇宙中最危险、回报也最丰厚的 PvP 区域。一个**黑洞**就悬在它的正中央：传送门和它们之间的航道都远远避开黑洞，但飞进去的舰船会先感受到辐射，再感受到引力，最终在事件视界被摧毁。参见[黑洞](/wiki/03-Mechanics/Black-Hole.md)。

### Jump CPU {#the-jump-cpu}

[Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) 不需要传送门，每次跳跃 500 Thulium，就能把你的舰船送到你所在世界的任意企业星区，包括敌方的主星区。它永远不会通向危险星区，战斗中无法启动，而且你要先在 Skylab 的研究中心研究它（[研究](/wiki/03-Mechanics/Research.md)）。[Base CPU](/wiki/06-Items/Extras.md#base-cpus) 以同样的方式送你回基地。传送 CPU，也就是 Jump CPU 和 Base CPU，在你携带任务物品时无法使用（“携带任务物品时无法使用传送 CPU。”）：请从星门飞回家（[任务物品](/wiki/03-Mechanics/Quests.md#quest-items)）。
