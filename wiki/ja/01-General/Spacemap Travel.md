<!-- wiki-i18n source: 6ad05a3dc7e0e2f6 -->
<!-- wiki-i18n title: スペースマップ移動 -->
# スペースマップでの移動 {#spacemap-travel}

スペースマップは、SpaceCorps の宇宙を移動するためのナビゲーションインターフェースです。各企業は宇宙のセクターを1つ支配しており、そのセクターは、安全な探索と危険な PvP の遭遇の両方を可能にする特定の配置（トポロジー）で並んでいます。

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

## 宇宙の構造 {#the-universe-structure}

宇宙は、3つの主要な企業セクター（Mars、Terra、Galactic）と、中央の PvP ゾーンで構成されています。

- **x-1（本拠地）**：各企業の開始マップ（M-1、T-1、G-1）。もっとも安全なゾーンです。
- **x-2 -> x-3**：拡張ゾーン。進むほど手強いエイリアンが現れます。
- **x-4（境界）**：PvP セクターへの入り口であり、別の企業の `x-3` への入り口でもあります（下の「リング」）。
- **DS-x（危険セクター）**：すべての企業をつなぐ中央の PvP ゾーン。DS-1～DS-4 です。

ステーションがあるのは本拠地だけです。**Mission Control** はそこで開き、セーフゾーンはステーションの周囲 1,600ユニットまで広がっています。危険セクターには、`DS-1` も含めてステーションがありません。そこにあるセーフゾーンは、ジャンプゲートの周りの半径 660ユニットのリングだけで、Mission Control は開けません。ミッションのためには本拠地まで飛んで戻ってください。

各[ワールド](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)（Alpha、Beta、Gamma）には、このマップ全体がそれぞれ別に存在し、パイロット同士が戦える場所はワールドごとに異なります。Alpha では `x-4` と `DS-x` のみ、Beta では `x-1` 以外のすべての場所、Gamma ではどこでも戦えます。銀河マップは、自分のワールドのルールに従ってセクターを色分けします。

## マップ表示 {#visualization}

下の銀河マップは、既知の宇宙の配置をリアルタイムで表示します。ゲーム内では、この同じマップが**星系**ウィンドウです。

```spacemap

```

[Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) を装備していると、このマップで行き先も選べます。ホットバーの CPU のスロット（**JMP**）を押すと、星系ウィンドウが選択モードで開きます。CPU で行けるセクターは明るく表示され、自分のいるセクターと危険セクターは暗く表示されます。明るいセクターにポインターを合わせると料金が読め、クリックして、マップから確認されたらジャンプを確定します（500 Thulium）。

## 移動のしかた {#how-to-travel}

スペースマップ上の移動は、**ジャンプゲート**（ポータル）を通じて行います。[Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) はもうひとつの方法で、ゲートを必要としません（このページの最後を参照）。

1. **ポータルを探す**：ポータルは通常、マップの角や端にあります。
2. **接近**：艦をポータルの構造物の近くまで飛ばします。
3. **起動**：ポータルから500ユニット以内で **「J」** を押すと、ジャンプが始まります。
4. **待つ**：ジャンプには**3秒かかります**。その間、ホットバーの上のバー（「ジャンプ中…」）が伸びていき、ポータルはチャージが進むにつれて明るく輝きます。あなたがジャンプしているときは、ほかのパイロットにも同じチャージの輝きがポータルに見えます。艦は飛び続けられますが、時間が終わるまでポータルから500ユニット以内にとどまる必要があります。範囲外へ出るとジャンプは中止されます（「ポータルが遠すぎてジャンプできません。」と表示され、バーが赤くなります）。ジャンプ中にもう一度 **「J」** を押しても、その旨が表示されるだけで何も起こりません。
5. **到着**：目的のマップにある、対応するポータルに到着します。

### 攻撃を受けながらのジャンプ {#jumping-under-fire}

- **危険セクターの外**では、エイリアンやほかのパイロットに攻撃されてもジャンプは**中断されません**。最後まで完了します。
- **危険セクター（`DS-1`～`DS-4`）** では、攻撃を受けている間はジャンプで脱出できません。パイロットまたはエイリアンが直近**10秒**以内にあなたの艦（シールドまたは船体）へ攻撃を当てていると、ジャンプは開始できず（「攻撃を受けています：危険セクターからはジャンプで脱出できません。」）、ジャンプ中に被弾するとジャンプは中止されます（バーが赤くなり、理由がゲームから通知されます）。ブラックホールの放射線で受けるダメージは攻撃には含まれず、セーフゾーンに防がれた射撃も含まれません。ジャンプ元のマップで受けた被弾が、ポータルを越えて持ち越されることはありません。到着時は被弾の記録がリセットされています。
- 同時に行えるのは1つの行動だけです。ジャンプ中は[積荷コンテナ](/wiki/03-Mechanics/Cargo.md)を回収できず、ジャンプを開始すると、始めていた回収は中止されます。
- ジャンプの途中でゲームを閉じたり基地に戻ったりすると、ジャンプは中止され、到着しません。
- **CPU のワープは、ポータルジャンプと同じように充填されます。** Jump CPU は5秒、Base CPU は10秒かかり、ホットバーの上にバーが表示されます。自分が撃ったときや攻撃を受けたときは、どのセクターでもワープが中止され（何も支払われず、何も消費されません）、撃ったり攻撃を受けたりしてから10秒以内は、どちらの CPU も始動しません。CPU のスロットをもう一度押すと、自分で中止できます。

### ジャンプの接続 {#jump-links}

- **企業ループ**：Mars、Terra、Galactic はどれも同じ配置です。接続は `1 <-> 2 <-> 3`、`2 <-> 4`、`3 <-> 4` の形で流れます。これにより、二次マップ（`x-2` と `x-3`）と境界マップ（`x-4`）の間でループが形成され、`x-1` は `x-2` にだけつながる安全な入口の行き止まりとして機能します。開始マップにあるポータルは1つだけです。
- **危険セクターへのアクセスゲート**：各企業の境界マップ（`x-4`）は、自企業の危険セクターに直接つながっています。
  - `M-4` は `DS-1` につながります
  - `T-4` は `DS-2` につながります
  - `G-4` は `DS-3` につながります
- **リング**：各企業の境界マップ（`x-4`）にはもう1つゲートがあり、**次の企業**の `x-3` につながっています。どの `x-3` にも戻りのゲートがあります。この3つの接続は危険セクターを囲むリングを作るので、どの企業にも出口が1つ、入口が1つあります。
  - `M-4` は Terra の `T-3` につながります
  - `T-4` は Galactic の `G-3` につながります
  - `G-4` は Mars の `M-3` につながります

  リングは、どの企業に所属していても、すべてのパイロットに開かれています。PvP ゾーンを通らずに企業のマップ間を移動できる、2つ目のルートです。リングのゲートは、そのマップのほかのゲートから離れた専用の隅にあり、周囲にはいつもの半径 660ユニットのセーフゾーンがあって、ジャンプは通常のゲートと同じように行えます。向こう側で攻撃を受けるかどうかは、ほかの場所と同じくワールドによって決まります。Alpha では `T-3` は PvP セクターではありませんが `T-4` は PvP セクターで、Beta ではどちらも PvP セクター、Gamma ではすべてのセクターが PvP セクターです。
- **侵攻ルート（企業間の移動）**：ゲートを通って別の企業の領域に入る方法は2つあります。近道はリングです。Mars のパイロットは `M-4` からリングのゲートを抜けて Terra の `T-3` に入り（Mars の本拠地から3回のジャンプ、`M-1` → `M-2` → `M-4` → `T-3`）、そこから `T-4` や `T-2` へ進みます。Galactic の `G-4` は同じように Mars の `M-3` に、Terra の `T-4` は Galactic の `G-3` につながります。遠回りの道は PvP ゾーンを通ります。`M-4` から危険セクター `DS-1` に入り、ジャンプゲートで `DS-2` へ渡り、`T-4` を通って Terra 領域に入ります。Galactic に向かうには、ジャンプゲートで `DS-3` へ渡り、`G-4` から入ります。
- **危険セクターの三角形**：`DS-1`、`DS-2`、`DS-3` は互いにすべてつながっています。それぞれに企業のゲートが1つずつあり（`DS-1` は Mars、`DS-2` は Terra、`DS-3` は Galactic）、`DS-4` にはありません。
- **コアセンター**：外側の3つの危険セクター（`DS-1`、`DS-2`、`DS-3`）は、いずれも中央のマップ **`DS-4`** に直接つながっています。ここは宇宙でもっとも危険で、もっとも見返りの大きい PvP ゾーンです。その真ん中には**ブラックホール**が浮かんでいます。ポータルとそれらを結ぶ航路は十分に離れていますが、飛び込んだ艦はまず放射線を受け、次に引力を受け、事象の地平線で破壊されます。[ブラックホール](/wiki/03-Mechanics/Black-Hole.md)を参照してください。

### Jump CPU {#the-jump-cpu}

[Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) は、ゲートを使わずに、あなたのワールドの任意の企業のセクターへ艦を運びます。1回のジャンプにつき 500 Thulium で、敵の本拠地セクターも含みます。危険セクターには行けず、戦闘中は開始できません。先に Skylab の研究センターで研究しておく必要があります（[研究](/wiki/03-Mechanics/Research.md)）。[Base CPU](/wiki/06-Items/Extras.md#base-cpus) は同じように艦を拠点へ戻します。ワープ CPU、つまり Jump CPU と Base CPU は、ミッションアイテムを運搬中は使えません（「ミッションアイテムを運搬中はワープ CPU を使えません。」）。ゲートを通って帰りましょう（[ミッションアイテム](/wiki/03-Mechanics/Quests.md#quest-items)）。
