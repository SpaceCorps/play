<!-- wiki-i18n source: 2bd1925e336e25b6 -->
<!-- wiki-i18n title: 船体装甲 -->
# 船体装甲 {#hull-plating}

<!-- wiki-search: hull plate; hull plate slot; hull plate slots; plate slot; plate; armour; armor; hpl; 船体装甲; 装甲スロット; 装甲板 -->

Dormant の群れの研究で、装甲技術の進歩が明らかになりました。この技術を使って、艦は船体を強化できます。**船体装甲**は、製造した艦の船体プレートスロットに装着し、船体ポイントを加える装甲です。[ブースター](/wiki/06-Items/Boosters.md)のページにある Hull Plating **Booster** とは別物で、そちらは時間制のボーナスです。

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## アイテムツリー {#item-tree}

アセンブリで作れるものは、先にその技術が必要です。アイテムにカーソルを合わせると、研究にかかる時間が分かります。技術ツリー、燃料、ブーストは [研究](/wiki/03-Mechanics/Research.md) を参照してください。

```tree
Hull Plating I | hull-plating, uncommon | buy 5000 Thulium | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating II | hull-plating, rare | craft 2500 Thulium, 300 s | research 86400 s, 86400 science, 25 Dark Matter | 1 Hull Plating I, 150 Ship Fragment, 20 Reinforced Hull Plate, 6 Power Core, 5 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating III | hull-plating, epic | craft 4000 Thulium, 600 s | research 172800 s, 172800 science, 40 Dark Matter | 1 Hull Plating II, 300 Ship Fragment, 40 Reinforced Hull Plate, 12 Power Core, 1 Ancient Control Unit, 8 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings

Hull Plating I => Hull Plating II => Hull Plating III
```
<!-- item-tree:end -->

## 3つの装甲 {#the-three-platings}

| アイテム | 追加される船体 | 入手方法 |
| :--- | ---: | :--- |
| **Hull Plating I** | 5,000 | ショップ、5,000 Thulium |
| **Hull Plating II** | 10,000 | アセンブリ、Hull Plating I から |
| **Hull Plating III** | 15,000 | アセンブリ、Hull Plating II から |

Hull Plating I は購入します。**II と III は強化品です**。アセンブリは1つ下のティアの装甲（インベントリにそのままある1個）を消費し、Thulium、素材、そして **Dark Matter Plate** を要求します。II は5枚、III は8枚で、ほかの装備の最終ティアが要求する3枚より多くなっています。どちらもまず技術が必要で、[研究](/wiki/03-Mechanics/Research.md#tree-hull-plating)ページの Hull Plating ツリーにあります。II は1日と Dark Matter 25個、III は2日と Dark Matter 40個で、Dark Matter Plate 自体の技術に加えて必要です。上のツリーに価格、素材、時間が載っています。

[鍛冶場](/wiki/06-Items/Forge.md)はどの装甲も扱えます。強化すると、消費した装甲の鍛造の段階が引き継がれ、ボーナスは振り直されます。装甲のステータスは船体の1つだけなので、ボーナスも1つで、段階に応じて +2% から +15% です。「永遠」の Hull Plating III は最大で 17,250 を加えます。[オークション](/wiki/03-Mechanics/Auction.md)に出せるのは Hull Plating II と III で、ショップで売られている Hull Plating I は出品できません。

## 装甲スロット {#hull-plate-slots}

船体装甲は**装甲スロット**にしか入りません。これは、アセンブリで製作する4隻の艦が、レーザー、ジェネレーター、エクストラ、アビリティ、ドローンの各スロットに加えて持つ、専用の種類のスロットです。

| 艦 | 装甲スロット | Hull Plating III のフルセットで増える船体 |
| :--- | ---: | ---: |
| **Paragon** | 5 | 75,000 |
| **Storm** | 7 | 105,000 |
| **Ironclad** | 15 | 225,000 |
| **Wraith** | 9 | 135,000 |

- **最初はすべてロック。** スロットは、Skylab で研究すると開きます。スロット1つにつき技術が1つで、1時間と Dark Matter 10個、最初のものから順に進めます。[研究](/wiki/03-Mechanics/Research.md#ship-technologies)画面では、艦のスロットが1枚のカードにまとめて表示され、スロット1つにつき点が1つ付きます。
- **艦1隻ではなく、艦の種類ごと。** Paragon のために開いたスロットは、Paragon のすべてのデザインでも開いています（[艦のデザイン](/wiki/03-Mechanics/Ship-Designs.md)）。技術は永久にあなたのものです。ワイプでも残ります。
- **2つの構成で共有。** 装甲は艦に属します。構成を切り替えても付いたままで、ハンガーはどちらの構成でも同じ装甲を表示します。
- **自由な組み合わせ。** スロットにはどの船体装甲でも入り、同じものを2つ入れても構いません。
- **船体の割合は変わりません。** 装甲を付けても外しても、今ある船体の割合が保たれるので、装甲で回復することも、傷つくこともありません。
- **ほかの装備と同じく**、装甲の着脱はハンガーで、またはセーフゾーンの中からそのウィンドウで行います。フィールドでは行えません。研究していないスロットは装甲を受け付けません。

ハンガーでは、**船体装甲**カードにスロットが表示されます。開いているスロットには、ほかのスロットと同じようにドラッグ＆ドロップで装甲を入れます。ロックされたスロットには鍵が表示され、クリックすると Skylab の研究が開きます。ほかのステータスの隣のタイルには、装着中の装甲が与える合計が表示されます。

## 船体の合計の仕組み {#how-the-hull-adds-up}

装甲は艦自身の船体に自分の船体を足し、ハンガーと艦のウィンドウには大きいほうの数値が表示されます。艦の船体と装甲の合計は、これまでどおりの倍率を通ります。[Hull Plating Booster](/wiki/06-Items/Boosters.md)と、装着中の[ドローン編成](/wiki/03-Mechanics/Formations.md)です。船体を変えるデザイン（BUCKY は25%多い）は艦自身の船体を変えるもので、装甲はその上に加わります。

## Hull Plating か、Hull Plating Booster か {#hull-plating-or-booster}

同じ名前のものが2つあります。**船体装甲**（このページ）は装甲です。製作した艦の装甲スロットに入る板で、装着している間、その船体を加えます。**Hull Plating Booster** は[ブースター](/wiki/06-Items/Boosters.md)ページの時間制ボーナスで、操縦中の艦に10時間のあいだ最大ヒットポイント +10% を与え、装着するものはありません。両者は重なります。先に装甲が加わり、Booster の10%は合計に対してかかります。
