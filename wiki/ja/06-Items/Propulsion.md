<!-- wiki-i18n source: b04277deb1c5225f -->
<!-- wiki-i18n title: 推進装置 -->
# 推進装置と速度 {#propulsion-speed}

推進装置は、艦の移動速度と機動性を決めます。

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

スラスターはエンジンまたはアダプティブコアの中に装着して、その速度を高めます。スラスターには、4ティアずつの2つの系統があります。**Impulse Thruster** は固定の速度加算が最も大きく、装着したエンジンの速度にもわずかな倍率をかけます。**Momentum Thruster** は固定の加算が小さい代わりに、その倍率がより大きくなります。スラスターを載せたエンジン（またはアダプティブコア）が生み出す速度は、**自身の基本速度にスラスターの固定速度ブーストを足し、その全体にスラスターの速度倍率をすべて掛け合わせたもの**です（[速度の計算方法](/wiki/03-Mechanics/Speed.md)）。Momentum Thruster IV を3基載せた Engine III は (6 + 3 x 12) x 1.14 x 1.14 x 1.14 = 62.2、Impulse Thruster IV を3基載せると (6 + 3 x 17) x 1.02 x 1.02 x 1.02 = 60.5、Impulse Thruster IV を2基載せた Adaptive Core II は (0 + 2 x 17) x 1.02 x 1.02 = 35.4（Momentum Thruster IV 2基なら 31.2）になります。

| 名前 | レアリティ | 固定速度ブースト | 速度倍率 | コスト |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | 粗悪 | +5 | 1.02倍 | 20,000クレジット |
| **Impulse Thruster II** | コモン | +10 | 1.02倍 | 製作専用 |
| **Impulse Thruster III** | レア | +15 | 1.03倍 | 製作専用 |
| **Impulse Thruster IV** | エピック | +17 | 1.02倍 | 製作専用 |
| **Momentum Thruster I** | 粗悪 | +4 | 1.08倍 | 20,000クレジット |
| **Momentum Thruster II** | コモン | +8 | 1.10倍 | 製作専用 |
| **Momentum Thruster III** | レア | +11 | 1.13倍 | 製作専用 |
| **Momentum Thruster IV** | エピック | +12 | 1.14倍 | 製作専用 |

どちらの系統が速いかは、載せる場所で変わります。Impulse Thruster は、アダプティブコアと、スラスターが1基か2基のエンジンでより多くの速度を生み出します。同じティアの Momentum Thruster は、3つのスロットをすべて埋めた Engine III でより多くの速度を生み出します（ティアIVでは62.2対60.5。Impulse Thruster IV 1基と Momentum Thruster IV 2基の組み合わせ（62.3）が、Engine III で作れる最速です）。

[鍛冶場](/wiki/06-Items/Forge.md)でスラスターの速度倍率に付くボーナスは、1を超える部分を伸ばします（1.14倍に +15% のボーナスが付くと1.161倍）。倍率が1.05倍以下の場合、鍛冶場はその倍率にボーナスを付けません。Impulse Thruster の1.02倍や1.03倍に付けても、効果は1000分の1ほどです。Impulse Thruster が持てるボーナスは1つ（固定の速度）、Momentum Thruster は2つです。

各系統のティアIは20,000クレジットで販売されています。ティアII～IVは[アセンブリ](/wiki/06-Items/Overview.md#upgrading-modules)で、同じ系統の1つ下のティアのスラスターから作ります（Impulse Thruster I から Impulse Thruster II、II から III、III から IV）。Thulium、ドロップ品、そして Skylab で作る Velkonite Reinforced Plate（2枚、4枚、6枚）が必要です。スラスターが系統を変えることはありません。Impulse にするか Momentum にするかは、ティアIを買うときに選びます。いずれも、消費したスラスターのエンチャント段階は引き継がれ、ボーナスは引き直されます（[アセンブリでの部品の強化](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)）。スラスターは[アビリティスロット](/wiki/03-Mechanics/Abilities.md)には装着できません。エンジンとアダプティブコアの中に装着するものです。

### エイリアンを振り切る {#outrunning-aliens}

エイリアンの速度は、Seeker が120、Phantasm が160、Bulwark が175、Goombah が180、Crystalys が230です。Engine II 1基とスラスター2基を載せた Ostirion の速度は、Impulse Thruster I で223.1です。まだ Crystalys に届かないため、振り切るにはアセンブリで作ったスラスターが必要です（Impulse Thruster II で234.0、III で245.5、IV で249.1）。Momentum Thruster は、この艦では速度が少し低くなります（Momentum Thruster I で222.6、II から IV で233.2、242.5、245.8）。どちらの系統もティアIは Crystalys に届かず、アセンブリで作ったティアはすべて上回ります。
