<!-- wiki-i18n source: fe17f46644fd6072 -->
<!-- wiki-i18n title: 推進装置 -->
# 推進装置と速度 {#propulsion-speed}

推進装置は、艦の移動速度と機動性を決めます。

## 1分でわかる要点 {#in-one-minute}

- **エンジンは速度を生み、スラスターはその中に入って速度を上乗せします。** エンジンには1～3基のスラスターを装着でき（Engine I は1基、Engine II は2基、Engine III は3基）、アダプティブコアも同様です（ティアで基数が決まります）。
- **4ティアずつの2つの系統。** Impulse Thruster は固定の速度加算が最も大きく、Momentum Thruster は固定の加算が小さい代わりに速度への倍率が大きくなります。どちらの系統も、ティアが上がるごとに、両方の数値が1つ下のティアより高くなります。
- **どれをどこに。** 目安として、スラスターを3基載せた Engine III には Momentum を、アダプティブコアには Impulse を入れます。小さいエンジンでは、ティアIとIIでは両者が近く、ティアIII以降は Impulse が上回ります。数値は[下の表](#which-thruster-where)にあります。最速の Engine III は Momentum Thruster IV を3基載せたもので、63.3になります。
- **入手方法。** 各系統のティアIは20,000クレジットで販売されています。ティアII～IVはアセンブリで、1つ下のティアから作ります。スラスターが系統を変えることはありません。

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## アイテムツリー {#item-tree}

アセンブリで作れるものは、先にその技術が必要です。アイテムにカーソルを合わせると、研究にかかる時間が分かります。技術ツリー、燃料、ブーストは [研究](/wiki/03-Mechanics/Research.md) を参照してください。

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Engine I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 4000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 80 Ship Fragment, 4 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 80 Ship Fragment, 4 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 4000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 4000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I => Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## エンジン {#engines}

エンジンは艦の主な推進力です。**アビリティスロット**に入れたエンジンは、それ自体の推力を生まない代わりに、「特殊効果」列の **Afterburner** を使えるようにします。Afterburner は15秒間の加速で、エンジンを重ねるとさらに長くなります（[アビリティ](/wiki/03-Mechanics/Abilities.md)を参照）。

| 名前 | レアリティ | 基本速度 | 速度ボーナス% | シールドボーナス% | スロット | 特殊効果 | コスト |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | 粗悪 | +5 | +2% | -2% | 1 | Afterburner I | 20,000クレジット |
| **Engine II** | コモン | +10 | +3% | -8% | 2 | Afterburner II | 製作専用 |
| **Engine III** | レア | +15 | +4% | -15% | 3 | Afterburner III | 製作専用 |

**Engine II** は、[アセンブリ](/wiki/06-Items/Overview.md#upgrading-modules)で Engine I から作ります。2,000 Thulium、Ship Fragment 60個、Power Core 1個、Velkonite Reinforced Plate 4枚が必要です。**Engine III** は、同じくアセンブリで Engine II から作ります。4,000 Thulium、Ship Fragment 110個、Power Core 5個、Ancient Control Unit 1個、そして Dark Matter Plate 4枚（[Dark Matter と Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)）が必要です。どちらも、消費したエンジンのエンチャント段階とボーナスが引き継がれます（[アセンブリでの部品の強化](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)）。先に、消費するエンジンを艦から外してください（中のスラスターも取り出します）。装備されたままのエンジンや、スラスターが入ったままのエンジンは消費されません。

エンジンのシールドボーナスはアイテムデータに含まれていますが、ゲームで適用されたことは一度もありません。エンジンがシールドを弱めることはなく、アイテムカードにもこの値は表示されません。

---

## スラスター {#thrusters}

スラスターはエンジンまたはアダプティブコアの中に装着して、その速度を高めます。スラスターには、4ティアずつの2つの系統があります。**Impulse Thruster** は固定の速度加算が最も大きく、装着したエンジンの速度にもわずかな倍率をかけます。**Momentum Thruster** は固定の加算が小さい代わりに、その倍率がより大きくなります。どちらの系統も、ティアが上がるごとに、固定速度も倍率も1つ下のティアより高くなります。スラスターを載せたエンジン（またはアダプティブコア）が生み出す速度は、**自身の基本速度にスラスターの固定速度ブーストを足し、その全体にスラスターの速度倍率をすべて掛け合わせたもの**です（[速度の計算方法](/wiki/03-Mechanics/Speed.md)）。Momentum Thruster IV を3基載せた Engine III は (15 + 3 x 11.135) x 1.0935 x 1.0935 x 1.0935 = 63.3、Impulse Thruster IV を3基載せると (15 + 3 x 14.025) x 1.02975 x 1.02975 x 1.02975 = 62.3、Impulse Thruster IV を2基載せた Adaptive Core II は (0 + 2 x 14.025) x 1.02975 x 1.02975 = 29.7（Momentum Thruster IV 2基なら 26.6）になります。

| 名前 | レアリティ | 固定速度ブースト | 速度倍率 | コスト |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | 粗悪 | +4.25 | 1.017倍 | 20,000クレジット |
| **Impulse Thruster II** | コモン | +8.5 | 1.02125倍 | 製作専用 |
| **Impulse Thruster III** | レア | +12.75 | 1.0255倍 | 製作専用 |
| **Impulse Thruster IV** | エピック | +14.025 | 1.02975倍 | 製作専用 |
| **Momentum Thruster I** | 粗悪 | +3.825 | 1.051倍 | 20,000クレジット |
| **Momentum Thruster II** | コモン | +7.65 | 1.0595倍 | 製作専用 |
| **Momentum Thruster III** | レア | +10.625 | 1.0765倍 | 製作専用 |
| **Momentum Thruster IV** | エピック | +11.135 | 1.0935倍 | 製作専用 |

### どのスラスターをどこに {#which-thruster-where}

Impulse は固定の速度加算が大きく、Momentum は倍率が大きいので、どちらが速いかは、エンジンがもともと生み出している速度によって決まります。固定の加算が最も効くのは、掛け合わせる速度が少ない場所、つまりアダプティブコア（自前の速度を持ちません）と、スラスターが1～2基のエンジンです。倍率が最も効くのは、掛け合わせる速度が大きい、スラスターを3基載せた Engine III で、そこではどのティアでも Momentum が勝ちます。どの場所でも、すべてのスロットにティアIVのスラスターを入れたときの速度は次のとおりです。

| スラスターを載せる場所 | Impulse Thruster IV の場合 | Momentum Thruster IV の場合 | より速い方 |
| :--- | :---: | :---: | :--- |
| Engine I、スラスター1基 | 19.6 | 17.6 | Impulse |
| Engine II、スラスター2基 | 40.3 | 38.6 | Impulse |
| Engine III、スラスター1基 | 29.9 | 28.6 | Impulse |
| Engine III、スラスター2基 | 45.6 | 44.6 | Impulse |
| Engine III、スラスター3基 | 62.3 | 63.3 | Momentum |
| Adaptive Core II、スラスター2基 | 29.7 | 26.6 | Impulse |

- **低いティア。** ティアIII以降は、スラスターを3基載せた Engine III を除くどの場所でも Impulse が0.6～3.1上回ります。ティアIとIIでは、3基載せた Engine III を除けば両系統の差は1ポイント未満です。Impulse が上回るのは Engine I とアダプティブコア I・II で、Momentum が上回る（または並ぶ）のはスラスター1～2基の Engine III と、2基の Engine II です。例外はスラスターを3基載せた Engine III で、ここではどのティアでも Momentum が1.0～2.0上回ります。
- **最速の Engine III。** Momentum Thruster IV を3基載せたものです。63.3で、Impulse 1基と Momentum Thruster IV 2基（63.2）や Impulse 3基（62.3）をわずかに上回ります。

[鍛冶場](/wiki/06-Items/Forge.md)でスラスターの速度倍率に付くボーナスは、1を超える部分を伸ばします（1.0935倍に +15% のボーナスが付くと1.1075倍）。倍率が1.05倍以下の場合、鍛冶場はその倍率にボーナスを付けません。Impulse Thruster の1.017倍～1.02975倍に付けても、増えるのは0.005未満です（1.02975倍に +15% で1.034倍）。Impulse Thruster が持てるボーナスは1つ（固定の速度）、Momentum Thruster は2つです。

各系統のティアIは20,000クレジットで販売されています。ティアII～IVは[アセンブリ](/wiki/06-Items/Overview.md#upgrading-modules)で、同じ系統の1つ下のティアのスラスターから作ります（Impulse Thruster I から Impulse Thruster II、II から III、III から IV）。Thulium、ドロップ品、そしてプレートが必要です。ティアIIとIIIには Skylab で作る Velkonite Reinforced Plate（どちらも4枚）、ティアIVには Dark Matter Plate 4枚と Ancient Control Unit 1個です。スラスターが系統を変えることはありません。Impulse にするか Momentum にするかは、ティアIを買うときに選びます。いずれも、消費したスラスターのエンチャント段階とボーナスが引き継がれます（[アセンブリでの部品の強化](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)）。スラスターは[アビリティスロット](/wiki/03-Mechanics/Abilities.md)には装着できません。エンジンとアダプティブコアの中に装着するものです。

### エイリアンを振り切る {#outrunning-aliens}

エイリアンの速度は、Seeker が120、Phantasm が160、Bulwark が175、Goombah が180、Crystalys が230です。Engine II 1基とスラスター2基を載せた Ostirion（基本速度220）の速度は、Impulse Thruster I で246.3、II で255.6、III で265.1、IV で268.2です。どのティアでも Crystalys を振り切れます。購入できるティアIでも同じです。Momentum Thruster の速度はそこから2以内に収まります（Momentum Thruster I で246.7、II から IV は255.9、263.9、266.3）。どちらの系統もすべてのティアが Crystalys を上回り、その差は最低でも16.3です。
