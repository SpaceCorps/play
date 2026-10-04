<!-- wiki-i18n source: 1adce749be3cd1f3 -->
<!-- wiki-i18n title: シールド -->
# シールドと防御 {#shields-defense}

防御モジュールは、シールド容量を与え、ダメージを吸収し、防御をリチャージします。

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## アイテムツリー {#item-tree}

アセンブリで作れるものは、先にその技術が必要です。アイテムにカーソルを合わせると、研究にかかる時間が分かります。技術ツリー、燃料、ブーストは [研究](/wiki/03-Mechanics/Research.md) を参照してください。

```tree
Light Shield Core | shield, shoddy | buy 20000 Credits | /wiki/06-Items/Shields.md#shield-cores
Basic Shield Core | shield, common | buy 2000 Thulium | /wiki/06-Items/Shields.md#shield-cores
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cores
Adaptive Core I | hybrid-generator, shoddy | buy 100000 Credits | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core II | hybrid-generator, common | buy 4000 Thulium | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core III | hybrid-generator, rare | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Absorption Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells

Light Shield Core -> Basic Shield Core => Heavy Shield Core
Adaptive Core I -> Adaptive Core II -> Adaptive Core III
Absorption Shield Cell I => Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell I => Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```
<!-- item-tree:end -->

## シールドコア {#shield-cores}

シールドコアを艦のジェネレータースロットか[ドローン](/wiki/03-Mechanics/Drones.md)に装備すると、能動的な防御障壁を展開できます（ドローンのスロットは、コアスロットとして数えられます）。重いシールドは速度を下げるので注意してください。**アビリティスロット**に入れたシールドコアは、それ自体のシールドを加えない代わりに、「特殊効果」列の **Shield Surge** を使えるようにします。Shield Surge は10秒かけてシールドを回復する効果です（[アビリティ](/wiki/03-Mechanics/Abilities.md)を参照）。

| 名前 | レアリティ | シールド容量 | リチャージ速度 | 吸収率 | シールド% | 速度% | シールドセルスロット | 特殊効果 | コスト |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Light Shield Core** | 粗悪 | 10,000 | 333/秒 | 45% | +5% | -1% | 1 | Shield Surge I | 20,000クレジット |
| **Basic Shield Core** | コモン | 15,000 | 500/秒 | 48% | +10% | -3% | 2 | Shield Surge II | 2,000 Thulium |
| **Heavy Shield Core** | レア | 25,000 | 833/秒 | 50% | +20% | -5% | 3 | Shield Surge III | 製作専用 |

**Heavy Shield Core** は、[アセンブリ](/wiki/06-Items/Overview.md#upgrading-modules)で Basic Shield Core から作ります。2,000 Thulium、Cataclysite 20個、Reinforced Hull Plate 8枚、そして Skylab で作る Velkonite Reinforced Plate 6枚が必要です。消費したコアのエンチャント段階は引き継がれ、ボーナスは引き直されます（[アセンブリでの部品の強化](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)）。先に Basic Shield Core を艦から外してください（中のセルも取り出します）。装備されたままのコアや、セルが入ったままのコアは消費されません。

**吸収率**は、各攻撃のうちシールドが受ける割合で、残りは船体が受けます。シールド単体では**45～50%**で、残りはシールドセルが加えます。最高のシールドに最高のセルを組み合わせた場合（Heavy Shield Core に Absorption Shield Cell IV を3個）は**80%**で、これが艦が初期状態で持てる最大値です。さらに2つの永続的な強化が上乗せされます。シーズンストアの Shield Absorbance Boost（1レベルにつき +0.1ポイント、100レベル、各25ワイプポイント）と、鍛冶場の吸収率ボーナスです。現時点のワイプポイントの入手元は、上限まで集めて合計855ポイント（ワイプをまたいで持ち越されます。入手元は今後増える予定です）で、100レベルのうち34レベル（+3.4ポイント）を購入できます。これに鍛冶場で永遠まで鍛え上げた装備一式を合わせると、約**95%**になります。ただし、このステータスに100%の上限はありません。攻撃側の*シールド貫通*が差し引かれるため、艦が100%を超えて持つ分は、貫通に対する余裕になります。詳しくは[シールドの仕組み](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-)をご覧ください。

---

## ハイブリッドジェネレーター（アダプティブコア） {#hybrid-generators-adaptive-cores-}

アダプティブコアはハイブリッドジェネレーターとして働き、シールドと速度の両方の性能を兼ね備えます。スロットにはスラスターとシールドセルのどちらも装着できます（1スロットにつきモジュール1個で、どちらの種類でも構いません）。シールドボーナスと速度ボーナスは、シールドやエンジンと同じ扱いで加算されます（上位4個が対象で、スロットの割合が掛かります）。吸収率は持たないため、艦の吸収率は変わらず、中に入れたセルが加えるのは容量とリチャージだけです。攻撃の一部を受け持つのはシールドだけなので、アダプティブコアのセルを活かすには、艦にシールドも必要です。

| 名前 | レアリティ | シールドボーナス% | 速度ボーナス% | スロット | 特殊効果 | コスト |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **Adaptive Core I** | 粗悪 | +5% | +3% | 1 | — | 100,000クレジット |
| **Adaptive Core II** | コモン | +8% | +4% | 2 | — | 4,000 Thulium |
| **Adaptive Core III** | レア | +15% | +5% | 3 | — | 製作専用 |

---

## シールドセル {#shield-cells}

シールドセルは、シールドコアまたはアダプティブコアの中に（そのコアのスロット数まで）装着して、そのコアを強化します。シールドコアの中では吸収率もポイント単位で上げ、それに伴って、シールドが受ける各攻撃の割合も上がります。セルには、4ティアずつの2つの系統があります。**Capacity Shield Cell** はシールド容量とリチャージ速度を最も伸ばし、**Absorption Shield Cell** は吸収率を最も伸ばします（各ティアで、同じティアの Capacity の2倍の吸収率と、半分の容量・リチャージ速度）。シールドで勝負が決まる艦には Capacity、船体で勝負が決まる艦には Absorption が有効です。1種類のセルでスロットをすべて埋めたコアの吸収率は、ティアIの Capacity セルからティアIVの Absorption セルまでで、Light Shield Core（1スロット）が47～55%、Basic Shield Core（2スロット）が52～68%、Heavy Shield Core（3スロット）が56～80%です。コアを外したとき、またはコアが[鍛冶場](/wiki/06-Items/Forge.md)の統合で提供アイテムとして消費されたとき、装着していたセルはインベントリに戻ります。

| 名前 | レアリティ | 容量ブースト | リチャージブースト | 吸収率ブースト | コスト |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Capacity Shield Cell I** | 粗悪 | +3,000 | +250/秒 | +2% | 30,000クレジット |
| **Capacity Shield Cell II** | コモン | +6,000 | +500/秒 | +3% | 製作専用 |
| **Capacity Shield Cell III** | レア | +9,000 | +750/秒 | +4% | 製作専用 |
| **Capacity Shield Cell IV** | エピック | +12,000 | +1,000/秒 | +5% | 製作専用 |
| **Absorption Shield Cell I** | 粗悪 | +1,500 | +125/秒 | +4% | 30,000クレジット |
| **Absorption Shield Cell II** | コモン | +3,000 | +250/秒 | +6% | 製作専用 |
| **Absorption Shield Cell III** | レア | +4,500 | +375/秒 | +8% | 製作専用 |
| **Absorption Shield Cell IV** | エピック | +6,000 | +500/秒 | +10% | 製作専用 |

各系統のティアIは30,000クレジットで販売されています。ティアII～IVは[アセンブリ](/wiki/06-Items/Overview.md#upgrading-modules)で、同じ系統の1つ下のティアのセルから作ります（Capacity Shield Cell I から Capacity Shield Cell II、II から III、III から IV）。Thulium、ドロップ品、そして Skylab で作る Velkonite Reinforced Plate（2枚、4枚、6枚）が必要です。セルが系統を変えることはありません。Capacity にするか Absorption にするかは、ティアIを買うときに選びます。消費したセルのエンチャント段階は引き継がれ、ボーナスは引き直されます（[アセンブリでの部品の強化](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)）。セルは[アビリティスロット](/wiki/03-Mechanics/Abilities.md)には装着できません。シールドとアダプティブコアの中に装着するものです。
