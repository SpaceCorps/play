<!-- wiki-i18n source: 969bfa836749a15e -->
<!-- wiki-i18n title: 推進装置 -->
# 推進装置と速度 {#propulsion-speed}

推進装置は、艦の移動速度と機動性を決めます。

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## アイテムツリー {#item-tree}

アセンブリで作れるものは、先にその技術が必要です。アイテムにカーソルを合わせると、研究にかかる時間が分かります。技術ツリー、燃料、ブーストは [研究](/wiki/03-Mechanics/Research.md) を参照してください。

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | buy 2000 Thulium | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters

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

**Engine III** は、[アセンブリ](/wiki/06-Items/Overview.md#upgrading-modules)で Engine II から作ります。2,000 Thulium、Ship Fragment 60個、Power Core 3個、そして Skylab で作る Velkonite Reinforced Plate 6枚が必要です。消費したエンジンのエンチャント段階は引き継がれ、ボーナスは引き直されます（[アセンブリでの部品の強化](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)）。先に Engine II を艦から外してください（中のスラスターも取り出します）。装備されたままのエンジンや、スラスターが入ったままのエンジンは消費されません。

エンジンのシールドボーナスはアイテムデータに含まれていますが、ゲームで適用されたことは一度もありません。エンジンがシールドを弱めることはなく、アイテムカードにもこの値は表示されません。

---

## スラスター {#thrusters}

スラスターはエンジンまたはアダプティブコアの中に装着して、その速度を高めます。スラスターには、4ティアずつの2つの系統があります。**Impulse Thruster** は固定の速度加算が最も大きく、装着したエンジンの速度にもわずかな倍率をかけます。**Momentum Thruster** は固定の加算が小さい代わりに、その倍率がより大きくなります。スラスターを載せたエンジン（またはアダプティブコア）が生み出す速度は、**自身の基本速度にスラスターの固定速度ブーストを足し、その全体にスラスターの速度倍率をすべて掛け合わせたもの**です（[速度の計算方法](/wiki/03-Mechanics/Speed.md)）。Momentum Thruster IV を3基載せた Engine III は (6 + 3 x 12) x 1.11 x 1.11 x 1.11 = 57.4、Impulse Thruster IV を3基載せると (6 + 3 x 17) x 1.02 x 1.02 x 1.02 = 60.5、Impulse Thruster IV を2基載せた Adaptive Core II は (0 + 2 x 17) x 1.02 x 1.02 = 35.4（Momentum Thruster IV 2基なら 29.6）になります。

| 名前 | レアリティ | 固定速度ブースト | 速度倍率 | コスト |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | 粗悪 | +5 | 1.02倍 | 20,000クレジット |
| **Impulse Thruster II** | コモン | +10 | 1.02倍 | 製作専用 |
| **Impulse Thruster III** | レア | +15 | 1.03倍 | 製作専用 |
| **Impulse Thruster IV** | エピック | +17 | 1.02倍 | 製作専用 |
| **Momentum Thruster I** | 粗悪 | +4 | 1.06倍 | 20,000クレジット |
| **Momentum Thruster II** | コモン | +8 | 1.07倍 | 製作専用 |
| **Momentum Thruster III** | レア | +11 | 1.09倍 | 製作専用 |
| **Momentum Thruster IV** | エピック | +12 | 1.11倍 | 製作専用 |

どのティアでも、Impulse Thruster は同じティアの Momentum Thruster より多くの速度を生み出します。アダプティブコアでも、スラスターを1基、2基、3基入れたエンジンでも同じです（Engine III にティアIVを3基入れると60.5対57.4で、Impulse Thruster IV を3基入れたものが Engine III で作れる最速です）。Momentum Thruster が勝っているのは、2つ目のボーナスです（下記）。

[鍛冶場](/wiki/06-Items/Forge.md)でスラスターの速度倍率に付くボーナスは、1を超える部分を伸ばします（1.11倍に +15% のボーナスが付くと1.1265倍）。倍率が1.05倍以下の場合、鍛冶場はその倍率にボーナスを付けません。Impulse Thruster の1.02倍や1.03倍に付けても、効果は1000分の1ほどです。Impulse Thruster が持てるボーナスは1つ（固定の速度）、Momentum Thruster は2つです。

各系統のティアIは20,000クレジットで販売されています。ティアII～IVは[アセンブリ](/wiki/06-Items/Overview.md#upgrading-modules)で、同じ系統の1つ下のティアのスラスターから作ります（Impulse Thruster I から Impulse Thruster II、II から III、III から IV）。Thulium、ドロップ品、そして Skylab で作る Velkonite Reinforced Plate（2枚、4枚、6枚）が必要です。スラスターが系統を変えることはありません。Impulse にするか Momentum にするかは、ティアIを買うときに選びます。いずれも、消費したスラスターのエンチャント段階は引き継がれ、ボーナスは引き直されます（[アセンブリでの部品の強化](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)）。スラスターは[アビリティスロット](/wiki/03-Mechanics/Abilities.md)には装着できません。エンジンとアダプティブコアの中に装着するものです。

### エイリアンを振り切る {#outrunning-aliens}

エイリアンの速度は、Seeker が120、Phantasm が160、Bulwark が175、Goombah が180、Crystalys が230です。Engine II 1基とスラスター2基を載せた Ostirion の速度は、Impulse Thruster I で223.1です。まだ Crystalys に届かないため、振り切るにはアセンブリで作ったスラスターが必要です（Impulse Thruster II で234.0、III で245.5、IV で249.1）。Momentum Thruster は、この艦では速度が少し低くなります（Momentum Thruster I で222.0、II から IV で231.8、240.1、243.9）。どちらの系統もティアIは Crystalys に届かず、アセンブリで作ったティアはすべて上回ります。
