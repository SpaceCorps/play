<!-- wiki-i18n source: 7fa3db40f02537c2 -->
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

**Engine III** は、[アセンブリ](/wiki/05-Items/Overview.md#upgrading-modules)で Engine II から作ります。2,000 Thulium、Ship Fragment 60個、Power Core 3個、そして Skylab で作る Velkonite Reinforced Plate 6枚が必要です。消費したエンジンのエンチャント段階は引き継がれ、ボーナスは引き直されます（[アセンブリでの部品の強化](/wiki/05-Items/Forge.md#module-upgrades-in-the-assembly)）。先に Engine II を艦から外してください（中のスラスターも取り出します）。装備されたままのエンジンや、スラスターが入ったままのエンジンは消費されません。

エンジンのシールドボーナスはアイテムデータに含まれていますが、ゲームで適用されたことは一度もありません。エンジンがシールドを弱めることはなく、アイテムカードにもこの値は表示されません。

---

## スラスター {#thrusters}

スラスターはエンジンまたはアダプティブコアの中に装着して、その速度を高めます。

| 名前 | レアリティ | 固定速度ブースト | 速度倍率 | コスト |
| :--- | :--- | :---: | :---: | :--- |
| **Thruster I** | 粗悪 | +5 | 1.00倍 | 20,000クレジット |
| **Vector Thruster** | アンコモン | +7 | 1.02倍 | 80,000クレジット |
| **Thruster II** | コモン | +10 | 1.05倍 | 2,000 Thulium |
| **Ion Thruster** | レア | +13 | 1.08倍 | 3,000 Thulium |
| **Thruster III** | レア | +15 | 1.10倍 | 製作専用 |
| **Plasma Thruster** | エピック | +18 | 1.12倍 | 製作専用 |

Plasma Thruster は、[アセンブリ](/wiki/05-Items/Overview.md#upgrading-modules)で Ion Thruster から作ります。Thulium、ドロップ品、そして Skylab で作る Velkonite Reinforced Plate 6枚が必要です。**Thruster III** は Thruster II から作り、1,500 Thulium、Ship Fragment 30個、Power Core 2個、Velkonite Reinforced Plate 4枚が必要です。どちらも、消費したスラスターのエンチャント段階は引き継がれ、ボーナスは引き直されます（[アセンブリでの部品の強化](/wiki/05-Items/Forge.md#module-upgrades-in-the-assembly)）。スラスターは[アビリティスロット](/wiki/03-Mechanics/Abilities.md)には装着できません。エンジンとアダプティブコアの中に装着するものです。

### エイリアンを振り切る {#outrunning-aliens}

エイリアンの速度は、Seeker が120、Phantasm が160、Bulwark が175、Goombah が180、Crystalys が230です。Engine II 1基とスラスター2基を載せた Ostirion の速度は、Thruster I で222.6、Vector Thruster で226.9です。いずれもまだ Crystalys に届かないため、Crystalys を振り切れるのは、Thulium 系のスラスターと、それから作ったスラスターだけです（Thruster II で233.4、Ion Thruster で239.9、Thruster III で244.2、Plasma Thruster で250.7）。
