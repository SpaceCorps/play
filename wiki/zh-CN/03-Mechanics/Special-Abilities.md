<!-- wiki-i18n source: 0a2447734a603004 -->
<!-- wiki-i18n title: 特殊能力 -->
# 特殊能力 {#special-abilities}

<!-- wiki-search: special ability; special abilities; ability; abilities; mob; mobs; regenerate; mending; shield burst; hardened plating; plating; enrage; call reinforcements; reinforcements; clones; decoy; flee and return; flee; life drain; nova pulse; nova; rocket barrage; barrage; veil; sow mines; mines; split; fragments; boss steps; ladder; three steps; warning; tell; surprise; warlord; warden; leader; 特殊能力; 再生; 护盾爆发; 硬化装甲; 狂暴; 呼叫增援; 分身; 脱离并返回; 生命汲取; 新星脉冲; 火箭齐射; 隐幕; 布雷 -->

有些外星人带有一种**特殊能力**：当船体损失一半时，它们一生只会使用一次。再生、护盾爆发、逃离、呼叫增援。能力启动之前毫无迹象，所以每次狩猎都可能以一个意外收场。本页说明每种能力的作用以及如何应对。首领的运作方式不同：随着船体下降，它们会分三个阶段改变战斗方式；最后一个等级的小型外星人如果被过快摧毁，可能碎裂成残片。

## 运作方式 {#how-it-works}

<!-- mob-rules:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **只有一次。** 带有能力的外星人一生只会使用一次：在战斗中，它的船体（不是护盾）降到最大值的 50% 以下时。若一击从这条线之上把它击毁，它就永远没有机会发动；不在战斗中的外星人会等到战斗开始。
- **先有预警。** 能力从预警开始：一圈向舰船收拢的光环，以及它上方的一个词。下方条目写明立即开始的能力没有预警。预警期间外星人仍可被击毁；那样什么也不会发生，它照常支付奖励。轻型种类（Seeker 和 Phantasm）更快：它们的预警和效果只持续平时的 50%。
- **事先看不出任何迹象。** 带有能力的外星人在预警开始前，每个细节都和其他外星人一样。游戏里没有任何地方会告诉你是哪一个，[旅行者指南](/wiki/03-Mechanics/Travelers-Guide.md)也不会。
- **谁会带有。** 企业星区和危险星区中的一小部分外星人：等级越高，比例越大，虫群的头领（Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah 和 Boss Crystalys）比其余的更有可能带有。Deep Void、战队地下城和单人星门中的外星人从不带有，虫群的随从、Warden 的波次、Dormant Force 和 Tesseract 也不带有。
- **它和任何外星人一样支付奖励。** 使用能力的外星人和不使用的外星人在支付、掉落和计数上完全相同：能力不会给击杀增加任何东西，只会耗费时间。击杀仍属于持有它的飞行员：外星人逃跑、修复或躲藏时，这份归属不会失效。
- **召来的舰船和分身不算击杀。** 外星人召来的舰船和制造的分身不支付任何奖励，不掉落任何东西，也不计入任何任务、统计或排名。每个召唤者最多同时存在 6，一张地图上最多 24，地图自己的外星人仍会按时回来。
- **地图上的所有人都看得到。** 能力开始时，地图上的飞行员会收到通知：游戏会画出光环、那个词和效果，并播放音效。

<!-- mob-rules:end -->

## 十二种能力 {#the-twelve-abilities}

能力以一次**预警**开始，除非其条目注明它立即开始：一个向飞船收拢的光环，以及其上方的一个词。下面的时间和数值针对重型种类。数值有多个时，它们对应括号中所列的等级，即外星人名字前的希腊字母。

<!-- mob-abilities:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

### 再生 {#regenerate}

它停在原地，在 6 秒 内恢复船体和护盾的 15% / 20% / 25% / 30% (α / β / γ / δ)，期间不发射任何东西。累计达到船体和护盾总量 10% 的伤害会打断它，已恢复的部分保留。

- **预警**：1.5 秒
- **舰船上方的词**：修复中
- **携带者**：任何外星人
- **应对**：用火箭或一大群舰船把它打崩，或在预警期间击毁它。

### 护盾爆发 {#shield-burst}

一层相当于最大船体 15% / 20% / 30% / 40% (α / β / γ / δ) 的新护盾叠在护盾之上。它存在时会吸收每一点伤害；耗尽时或 10 秒 后消失。

- **预警**：1 秒
- **舰船上方的词**：护盾展开
- **携带者**：任何外星人
- **应对**：穿透护盾的弹药和火箭更容易打穿它。或者去打另一个外星人，直到它消失。

### 硬化装甲 {#hardened-plating}

在 7 秒 / 8 秒 / 10 秒 (β / γ / δ) 内，它每次只承受 50% 的伤害，船体和护盾都一样：硬度翻倍。它继续战斗，而你的命中数字会变灰。

- **预警**：1.5 秒
- **舰船上方的词**：装甲硬化
- **携带者**：重型种类（Bulwark, Goombah 和 Crystalys）和重型虫群头领（Pirate Boss 和 Boss Phantasm），β 及以上
- **应对**：等它结束，期间去打另一个外星人，把你的爆发留到之后。

### 狂暴 {#enrage}

在 10 秒 内，它的伤害乘以 ×1.3 / ×1.4 / ×1.5 / ×1.75 (α / β / γ / δ)，速度乘以 ×1.25。

- **预警**：1 秒
- **舰船上方的词**：狂暴
- **携带者**：任何外星人
- **应对**：保持护盾开启，不停移动，待在它的射程之外。

### 呼叫增援 {#call-reinforcements}

4 / 6 (γ / δ) 个较小的外星人从地图最近的边缘进入，分 2 波，每波间隔 3 秒。来的种类是：Phantasm（由 Bulwark 和 Goombah 召来）; Bulwark（由 Crystalys 召来）。它们合计拥有它船体和护盾的 45% / 60% (γ / δ)，并发射它齐射的 50%。它们不支付奖励，不掉落东西，也不计入任何统计，在 45 秒 后或召唤者被击毁时离开。

- **预警**：2 秒
- **舰船上方的词**：呼叫中
- **携带者**：重型种类（Bulwark, Goombah 和 Crystalys）和重型虫群头领（Boss Phantasm 和 Boss Goombah），γ 及以上
- **应对**：击毁召唤者：它的舰船会随它一起消失。范围武器可以把它们清掉。

### 分身 {#clones}

它周围出现 3 (γ / δ) 个它的分身，名字和外观都与它相同。它们合计拥有它船体和护盾的 18% (γ / δ)；它们不发射任何东西，也不支付奖励，持续 15 秒，或直到真身被击毁。分身在场时，真身会带一圈细环，目标窗口把分身称为“诱饵”。

- **预警**：1 秒
- **舰船上方的词**：分身中
- **携带者**：任何外星人，γ 及以上
- **应对**：跟着真身的光环和移动的船体条，或使用范围武器。

### 脱离并返回 {#flee-and-return}

它以 ×2 的速度从攻击者身边飞开，持续 5 秒 / 6 秒 / 7 秒 / 8 秒 (α / β / γ / δ)，然后转身对付第一个击中它的飞行员。它不会离开地图，也不会进入安全区，全程都可以被击中，持有它击杀的飞行员保留这份归属。

- **预警**：0.5 秒
- **舰船上方的词**：逃离中
- **携带者**：任何外星人
- **应对**：追上它，或在它飞行时用火箭打它。

### 生命汲取 {#life-drain}

在 10 秒 内它不发射别的东西：每秒用一次无法躲避的完整齐射吸取射程内的每艘舰船，并恢复所造成伤害的 75% / 100% / 100% (β / γ / δ)，总共最多恢复船体的 20%。

- **预警**：1 秒
- **舰船上方的词**：汲取中
- **携带者**：重型种类（Bulwark, Goombah 和 Crystalys）和重型虫群头领（Pirate Boss, Boss Phantasm, Boss Goombah 和 Boss Crystalys），β 及以上
- **应对**：在射线上放一块岩石或一堵墙，进入隐形，或离开它的射程。

### 新星脉冲 {#nova-pulse}

预警期间，它周围的地面上有一圈光环在扩大。光环充满时，对其中的每艘舰船打击一次，威力为它齐射的 4 / 5 (γ / δ)。半径以单位计为 700 / 800 (γ / δ)。

- **预警**：2.5 秒
- **舰船上方的词**：新星
- **携带者**：重型种类（Bulwark, Goombah 和 Crystalys）和重型虫群头领（Pirate Boss, Boss Phantasm 和 Boss Goombah），γ 及以上
- **应对**：在光环充满之前飞出去：这是唯一能躲开的一次爆发。

### 火箭齐射 {#rocket-barrage}

在 3 秒 内它向目标发射 4 / 6 / 8 (β / γ / δ) 枚 [Rivet 火箭](/wiki/06-Items/Rockets.md#the-twelve-rockets)：Rivet I / II / II (β / γ / δ)。它们直线飞行，没有制导。

- **预警**：1.5 秒
- **舰船上方的词**：齐射
- **携带者**：重型种类（Bulwark, Goombah 和 Crystalys）和重型虫群头领（Boss Phantasm 和 Boss Goombah），β 及以上
- **应对**：不停移动：火箭是直线飞行的。路上的一块岩石会挡住它们。

### 隐幕 {#veil}

在 6 秒 / 8 秒 (γ / δ) 内，距它超过 700 单位的舰船无法锁定它，已有的锁定也会丢失。比这更近则照常可见。它继续战斗，爆炸仍会伤到它。

- **预警**：无，立即开始。
- **舰船上方的词**：隐匿中
- **携带者**：重型种类（Bulwark, Goombah 和 Crystalys）和重型虫群头领（Pirate Boss, Boss Phantasm, Boss Goombah 和 Boss Crystalys），γ 及以上
- **应对**：靠近到 700 单位以内。

### 布雷 {#sow-mines}

它在目标所站位置周围 500 单位的圆环上布下 4 / 6 / 8 (β / γ / δ) 颗地雷。地雷落地 3 秒 后启动，持续 30 秒，在第一艘飞过其上的飞行员舰船下爆炸一次，威力为该外星人齐射的 2 / 3 / 3 (β / γ / δ)。地雷从不伤害外星人。

- **预警**：1.5 秒
- **舰船上方的词**：布雷中
- **携带者**：重型种类（Bulwark, Goombah 和 Crystalys）和重型虫群头领（Pirate Boss, Boss Phantasm, Boss Goombah 和 Boss Crystalys），β 及以上
- **应对**：绕开它们：它们画在地面上，启动较晚。


<!-- mob-abilities:end -->

## 分裂 {#splitting}

<!-- mob-split:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

最后一级的小型外星人如果被击毁得太快，也会分裂。它只属于 δ 级的 Seeker, Phantasm, Bulwark, Goombah 和 Crystalys，其他外星人都没有，也不是上面的能力之一：一个外星人可以两者兼有。

- **何时**：飞行员在它受到第一次伤害后的 5 秒 内将其击毁。并不是每个死得这么快的外星人都会分裂。
- **会出现什么**：3 个同种类、同等级的外星人，大小为它的 70%，各自拥有船体和护盾的 25% 以及一次完整齐射，出现在它被击毁的位置周围。它们扑向击毁它的飞行员，180 秒 后离开。
- **它们是普通外星人**：每个都按其种类支付奖励、掉落同样的东西，并计入任务和统计。它们不带能力，也不会再分裂。
- **上限**：一张地图上最多同时存在 60 个碎片，它们不会挤掉地图自己的外星人。
- **这意味着什么**：能把外星人击毁得足够快的小队，从一个外星人身上最多可以得到 4 次击杀。做不到的小队什么也得不到。

<!-- mob-split:end -->

## 首领的三个阶段 {#the-bosses-three-steps}

每个首领都会分三个阶段改变战斗方式：战斗开始时、船体降到三分之二以下时、降到三分之一以下时。一个阶段只发生一次，不会倒退，除非首领按下文所述从头再来。

<!-- mob-ladders:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **每个阶段有一次暂停。** 在第一阶段之后，每当有事可做的阶段开始时，首领在 1.5 秒 内不会受伤（Dungeon Warlord 和单人星门首领为 3 秒）。
- **还有一种特殊能力。** Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah 和 Boss Crystalys也可能带有一种特殊能力（Dormant Force 和 Tesseract绝不会）：它出现在第二和第三阶段之间；如果两者本该同时开始，后者最多等待 3 秒。头领自己的阶段所用的能力绝不会被选中。
- **从头再来。** Tesseract完全修复后会从头开始它的阶段。

### 虫群头领 {#the-swarm-leaders}

| 头领 | 开始时 | 低于三分之二时 | 低于三分之一时 |
| :--- | :--- | :--- | :--- |
| **Pirate Boss** | 向第一个击中它的飞行员发射一把扇形的 3 枚火箭，彼此相隔 12 度。 | 一次再召来 5 个Pirate Scouts，同时最多 10 个存活。它们不支付奖励，45 秒 后离开。 | 在 10 秒 内以 ×1.8 的速度飞向最近的星门，然后转身对付飞行员。 |
| **Boss Seeker** | 它的Seeker Slaves在 8 秒 内以 ×2 的速度为它修复。 | 出现 2 个它的分身，真身带一圈光环。 | 在 4 秒 内从飞行员身边飞开，然后转回来。 |
| **Boss Phantasm** | 它的每个Phantasm Guards都会撑起一层相当于自身船体 10% 的护盾。 | 出现 3 个它的分身，真身带一圈光环。 | 闪现到离飞行员约 2,500 单位的地方，它的Phantasm Guards完好无损地回到它周围。 |
| **Boss Goombah** | 在 6 秒 内每次只承受 50% 的伤害。 | 在 10 秒 内，它的伤害乘以 ×1.5，速度乘以 ×1.25。 | 恢复船体和护盾的 25%（一次伤害爆发会打断它），期间它的Goombah Guards以 ×2 的速度为它修复。 |
| **Boss Crystalys** | 在 8 秒 内每次只承受 50% 的伤害。 | 一圈 700 单位的光环打击其中的每艘舰船，威力为它齐射的 4，同时它发射 4 枚火箭。 | 恢复船体和护盾的 20%（一次伤害爆发会打断它），再来 3 个Crystalys Guards，同时最多 6 个存活。 |
| **Dormant Force** | 只要它的某个Dormant Pulses还活着，它每次只承受 70% 的伤害。 | 它的Dormant Pulses在 15 秒 内每隔 2.5 秒 发射一枚火箭。 | 只要它的Dormant Pulses全部存活，它们就在 6 秒 内每秒为它修复船体的 5%。 |
| **Tesseract** | – | 在通常数量之外，一次再来 20 个Facets。 | – |

### 战队 Warden {#the-clan-wardens}

| Warden | 开始时 | 低于三分之二时 | 低于三分之一时 |
| :--- | :--- | :--- | :--- |
| **Brood Warden** (I, II, III) | 全部 4 架无人机同时来到它身边。 | 它的无人机在 15 秒 内以 ×1.5 的速度为它修复。 | 在通常数量之外，再来 2 架无人机，持续 30 秒。它们不支付奖励。 |
| **Siege Warden** (I, II, III) | – | 在 20 秒 内以 ×2 的频率发射火箭。 | 恢复船体和护盾的 15%（一次伤害爆发会打断它）。 |
| **Wrath Warden** (I, II, III) | – | 它的激光威力为 ×1.25。 | 它的激光威力合计为 ×1.5，不是叠加在前一阶段之上。 |

### Dungeon Warlord {#the-dungeon-warlord}

- **低于三分之二时**: 它的能力之间的间隔降到 4 秒，等待时间降到 ×0.75。
- **低于三分之一时**: 间隔降到 2 秒，等待时间降到 ×0.5，伤害升到 ×1.25；它会施放一次免费的 Meteor 齐射，它的 Swarm 回归的间隔绝不短于 120 秒。
- **每个阶段有一次暂停。** 阶段开始时，Warlord 在 3 秒 内不会受伤。

### 单人星门首领 {#the-solo-gate-bosses}

单人星门的六个首领同样有三个阶段，也就是它们的相位：它们在《单人星门》一文中[首领](/wiki/03-Mechanics/Solo-Gates.md#the-bosses)的表格里。

<!-- mob-ladders:end -->

## 延伸阅读 {#where-to-read-more}

- [战斗](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)：外星人与谁交战，谁获得击杀。
- [虫群](/wiki/05-Swarms/Swarms.md)：首领及其阶段，每个虫群各有一篇文章。
- [战队 Warden](/wiki/03-Mechanics/Clans.md#fighting-a-warden)、[地下城 Warlord](/wiki/03-Mechanics/Dungeons.md#the-warlord)和[单人星门的首领](/wiki/03-Mechanics/Solo-Gates.md#the-bosses)。
- [旅行者指南](/wiki/03-Mechanics/Travelers-Guide.md)：你对某个外星人了解到的内容。它从不说明哪一个带有能力。
