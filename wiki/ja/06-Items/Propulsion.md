<!-- wiki-i18n source: 201734b1f19e2346 -->
<!-- wiki-i18n title: 推進装置 -->
# 推進装置と速度 {#propulsion-speed}

推進装置は、艦の移動速度と機動性を決めます。

## 1分でわかる要点 {#in-one-minute}

- **エンジンは速度を生み、スラスターはその中に入って速度を上乗せします。** エンジンには1～3基のスラスターを装着でき（Engine I は1基、Engine II は2基、Engine III は3基）、アダプティブコアも同様です（ティアで基数が決まります）。
- **4ティアずつの2つの系統。** Impulse Thruster は固定の速度加算が最も大きく、Momentum Thruster は固定の加算が小さい代わりに速度への倍率が大きくなります。どちらの系統も、ティアが上がるごとに、両方の数値が1つ下のティアより高くなります。
- **どれをどこに。** 目安として、Momentum はスラスターを3基載せた Engine III に、Impulse はそれ以外のすべてに向きます。数値は[下の表](#which-thruster-where)にあります。最速の Engine III は両方を混ぜたもので、Impulse Thruster IV 1基と Momentum Thruster IV 2基で62.1になります。
- **入手方法。** 各系統のティアIは20,000クレジットで販売されています。ティアII～IVはアセンブリで、1つ下のティアから作ります。スラスターが系統を変えることはありません。

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## アイテムツリー {#item-tree}

アセンブリで作れるものは、先にその技術が必要です。アイテムにカーソルを合わせると、研究にかかる時間が分かります。技術ツリー、燃料、ブーストは [研究](/wiki/03-Mechanics/Research.md) を参照してください。

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | buy 2000 Thulium | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I -> Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## エンジン {#engines}

エンジンは艦の主な推進力です。**アビリティスロット**に入れたエンジンは、それ自体の推力を生まない代わりに、「特殊効果」列の **Afterburner** を使えるようにします。Afterburner は10秒間の加速で、エンジンを重ねるとさらに長くなります（[アビリティ](/wiki/03-Mechanics/Abilities.md)を参照）。

| 名前 | レアリティ | 基本速度 | 速度ボーナス% | シールドボーナス% | スロット | 特殊効果 | コスト |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | 粗悪 | +2 | +2% | -2% | 1 | Afterburner I | 20,000クレジット |
| **Engine II** | コモン | +4 | +4% | -8% | 2 | Afterburner II | 2,000 Thulium |
| **Engine III** | レア | +6 | +5% | -15% | 3 | Afterburner III | 製作専用 |

**Engine III** は、[アセンブリ](/wiki/06-Items/Overview.md#upgrading-modules)で Engine II から作ります。2,000 Thulium、Ship Fragment 60個、Power Core 3個、そして Dark Matter Plate 3枚（[Dark Matter と Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)）が必要です。消費したエンジンのエンチャント段階は引き継がれ、ボーナスは引き直されます（[アセンブリでの部品の強化](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)）。先に Engine II を艦から外してください（中のスラスターも取り出します）。装備されたままのエンジンや、スラスターが入ったままのエンジンは消費されません。

エンジンのシールドボーナスはアイテムデータに含まれていますが、ゲームで適用されたことは一度もありません。エンジンがシールドを弱めることはなく、アイテムカードにもこの値は表示されません。

---

## スラスター {#thrusters}

スラスターはエンジンまたはアダプティブコアの中に装着して、その速度を高めます。スラスターには、4ティアずつの2つの系統があります。**Impulse Thruster** は固定の速度加算が最も大きく、装着したエンジンの速度にもわずかな倍率をかけます。**Momentum Thruster** は固定の加算が小さい代わりに、その倍率がより大きくなります。どちらの系統も、ティアが上がるごとに、固定速度も倍率も1つ下のティアより高くなります。スラスターを載せたエンジン（またはアダプティブコア）が生み出す速度は、**自身の基本速度にスラスターの固定速度ブーストを足し、その全体にスラスターの速度倍率をすべて掛け合わせたもの**です（[速度の計算方法](/wiki/03-Mechanics/Speed.md)）。Momentum Thruster IV を3基載せた Engine III は (6 + 3 x 13.1) x 1.11 x 1.11 x 1.11 = 62.0、Impulse Thruster IV を3基載せると (6 + 3 x 16.5) x 1.035 x 1.035 x 1.035 = 61.5、Impulse Thruster IV を2基載せた Adaptive Core II は (0 + 2 x 16.5) x 1.035 x 1.035 = 35.4（Momentum Thruster IV 2基なら 32.3）になります。

| 名前 | レアリティ | 固定速度ブースト | 速度倍率 | コスト |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | 粗悪 | +5 | 1.02倍 | 20,000クレジット |
| **Impulse Thruster II** | コモン | +10 | 1.025倍 | 製作専用 |
| **Impulse Thruster III** | レア | +15 | 1.03倍 | 製作専用 |
| **Impulse Thruster IV** | エピック | +16.5 | 1.035倍 | 製作専用 |
| **Momentum Thruster I** | 粗悪 | +4.5 | 1.06倍 | 20,000クレジット |
| **Momentum Thruster II** | コモン | +9 | 1.07倍 | 製作専用 |
| **Momentum Thruster III** | レア | +12.5 | 1.09倍 | 製作専用 |
| **Momentum Thruster IV** | エピック | +13.1 | 1.11倍 | 製作専用 |

### どのスラスターをどこに {#which-thruster-where}

Impulse は固定の速度加算が大きく、Momentum は倍率が大きいので、どちらが速いかは、エンジンがもともと生み出している速度によって決まります。固定の加算が最も効くのは、掛け合わせる速度が少ない場所、つまりアダプティブコア（自前の速度を持ちません）と、スラスターが1～2基のエンジンです。倍率が最も効くのは、掛け合わせる速度が大きい、スラスターを3基載せた Engine III です。どの場所でも、すべてのスロットにティアIVのスラスターを入れたときの速度は次のとおりです。

| スラスターを載せる場所 | Impulse Thruster IV の場合 | Momentum Thruster IV の場合 | より速い方 |
| :--- | :---: | :---: | :--- |
| Engine I、スラスター1基 | 19.1 | 16.8 | Impulse |
| Engine II、スラスター2基 | 39.6 | 37.2 | Impulse |
| Engine III、スラスター1基 | 23.3 | 21.2 | Impulse |
| Engine III、スラスター2基 | 41.8 | 39.7 | Impulse |
| Engine III、スラスター3基 | 61.5 | 62.0 | Momentum |
| Adaptive Core II、スラスター2基 | 35.4 | 32.3 | Impulse |

- **低いティア。** ティアI～IIIも同じ傾向ですが、接戦になる場合が2つあります。Engine II にスラスターを2基載せた場合、ティアIとIIでは両系統がほぼ並びます（差は0.05以内）。Engine III に2基載せた場合は、ティアIとIIで Momentum が約0.2上回ります。ティアIII以降は、どちらも Impulse が1.4～2.4上回ります。スラスターを3基載せた Engine III では、どのティアでも Momentum が0.4～1.7上回ります。
- **Engine III では混ぜましょう。** 最速の Engine III は、Impulse Thruster IV 1基と Momentum Thruster IV 2基を載せたものです。(6 + 16.5 + 2 x 13.1) x 1.035 x 1.11 x 1.11 = 62.1で、Momentum 3基（62.0）や Impulse 3基（61.5）をわずかに上回ります。

[鍛冶場](/wiki/06-Items/Forge.md)でスラスターの速度倍率に付くボーナスは、1を超える部分を伸ばします（1.11倍に +15% のボーナスが付くと1.1265倍）。倍率が1.05倍以下の場合、鍛冶場はその倍率にボーナスを付けません。Impulse Thruster の1.02倍～1.035倍に付けても、増えるのは0.006未満です（1.035倍に +15% で1.040倍）。Impulse Thruster が持てるボーナスは1つ（固定の速度）、Momentum Thruster は2つです。

各系統のティアIは20,000クレジットで販売されています。ティアII～IVは[アセンブリ](/wiki/06-Items/Overview.md#upgrading-modules)で、同じ系統の1つ下のティアのスラスターから作ります（Impulse Thruster I から Impulse Thruster II、II から III、III から IV）。Thulium、ドロップ品、そしてプレートが必要です。ティアIIとIIIには Skylab で作る Velkonite Reinforced Plate（それぞれ2枚、4枚）、ティアIVには Dark Matter Plate 3枚です。スラスターが系統を変えることはありません。Impulse にするか Momentum にするかは、ティアIを買うときに選びます。いずれも、消費したスラスターのエンチャント段階は引き継がれ、ボーナスは引き直されます（[アセンブリでの部品の強化](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)）。スラスターは[アビリティスロット](/wiki/03-Mechanics/Abilities.md)には装着できません。エンジンとアダプティブコアの中に装着するものです。

### エイリアンを振り切る {#outrunning-aliens}

エイリアンの速度は、Seeker が120、Phantasm が160、Bulwark が175、Goombah が180、Crystalys が230です。Engine II 1基とスラスター2基を載せた Ostirion の速度は、Impulse Thruster I で223.1です。まだ Crystalys に届かないため、振り切るにはアセンブリで作ったスラスターが必要です（Impulse Thruster II で234.2、III で245.5、IV で249.2）。Momentum Thruster は、この艦では同じか少し低くなります（Momentum Thruster I で223.2、II から IV は234.2、243.8、246.7）。どちらの系統もティアIは Crystalys に届かず、アセンブリで作ったティアはすべて上回ります。
