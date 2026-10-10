<!-- wiki-i18n source: 8005e2da2b482cd9 -->
<!-- wiki-i18n title: 小惑星採掘 -->
# 小惑星採掘 {#asteroid-mining}

**小惑星**は、企業のセクターと危険セクターの飛行平面にある大きな岩です。動くことも、撃ってくることもありません。**ロケット**か**レーザー**で壊すと、クレジット、Thulium、鉱石の小さな**破片**に砕け、[積荷](/wiki/03-Mechanics/Cargo.md)と同じように拾えます。向いているのはロケットです。レーザーも小惑星にダメージを与えますが、船に与えるダメージの5%だけで、ドローンは何もできません。

採掘は狩りとは別の仕事であり、その代わりになるものではありません。XP も名誉もランキングポイントも得られず、撃つロケットにはクレジットか Thulium がかかります。得られるのは、クレジットと Thulium、戦わずに[鍛冶場](/wiki/06-Items/Forge.md)や製作に使える鉱石、そして[グループ](/wiki/03-Mechanics/Groups.md)で分け合える仕事です。稼ぎは良好です。ゲーム自身のモデルでは、適した小惑星を適したロケットで採掘する1時間は、ロケット代を引いたうえで、自分のレベルで最良の狩りの1時間のおよそ2.6～6.8倍になります。[ワールド](#the-worlds)の1日の上限が歯止めになり、上限にはすぐ届きます。Alpha で良いセクターを着実に採掘すれば、Thulium の上限には2時間足らず、クレジットの上限には約2.7時間で届きます。

## 小惑星とは {#what-an-asteroid-is}

- **艦と同じ高さ。** 小惑星は飛行平面にあり、その上を通る艦、ロケット、破片のすべての後ろに描かれ、その場から動きません。艦とエイリアンは通り抜けますが、射撃は通り抜けられません（[遮蔽](#cover)を参照）。小惑星は本来の縦横比で描かれるため、Motherlode や Prism Cluster は平らにならず、高くそびえます。マップの遠く奥にある薄暗い岩は背景です。命中させることはできず、中身もありません。
- **種類とファミリー。** 小惑星はどれも[種類一覧](#the-kinds)の種類のどれかで、各種類は性質を表すファミリーに属します。小惑星の輝きは中身を表します。地面の**1重のリング**は普通の小惑星、**2重のリング**は装甲つき、**破線のリング**はもろい小惑星を示します。
- **ミニマップ。** セクターのすべての小惑星は、その種類の色の小さな六角形で、命中するまでは中が空で、命中後は塗りつぶされます。破片は小さな丸い点です。
- **ターゲット画面。** 小惑星をクリックすると選択できます。選択した小惑星の周りの円は、その周りを飛んでいても小惑星から離れません。何もない場所や小惑星のすぐ横をクリックすると艦が飛ぶだけで、Esc かターゲット画面の × ボタンで選択を解除します。画面には、名前、ファミリーとサイズ、船体、**装甲**・**爆発**のバッジ、手に持っているロケットでおよそ何発かかるかとレーザーの斉射でおよそ何回かかるか、あなたのワールドで壊すと何が出るか、誰がどれだけダメージを与えたかが表示されます。小惑星を選んでも、自分の艦やエイリアンのターゲットは変わらないので、レーザーのロックオンはそのままです。

## 小惑星を壊す {#breaking-one}

1. **狙う。** 小惑星をクリックして選択すると、ロケットはその小惑星に向かいます。直進ロケット（Rivet、Scatter）は、カーソルの下に小惑星があれば、代わりにそちらに向かいます（その下に艦やエイリアンもいる場合を除きます。小惑星の縁のすぐ外側や、ミニマップ上の六角形も有効です）。小惑星を選択していない場合、誘導ロケット（Lancet、Ember）は、艦やエイリアンを選択していないときに限り、カーソルの下の小惑星に向かいます。そのため、小惑星のそばで戦うハンターは、そのままエイリアンを撃ち続けられます。狙う小惑星がないロケットは普通のロケットですが、進路上の小惑星には止められます（[遮蔽](#cover)）。
2. **撃つ。** ショップの12種類の[ロケット](/wiki/06-Items/Rockets.md#the-twelve-rockets)のどれでも使えます。N.U.K.E. も使えます。誘導ロケットは小惑星がロックオン範囲内に、直進ロケットは射程内にある必要があり、どちらも小惑星の中心までの距離で測ります。どちらも中心に向かって飛ぶので、カーソルが小惑星のどこにあるかは関係ありません。[N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) は小惑星にダメージを与えられません。
3. **撃ち続ける。** すべてのロケットは1つのリチャージタイマーを共有し、ロケット1発ごとにかかるコストはそのままです。ロケットがこの仕事の元手です。

- **小惑星を狙って撃ったロケットは、その小惑星に向かって飛びます。** 途中の艦は通り抜け、進路上で最初に出会った別の小惑星が代わりに受け止めます（[遮蔽](#cover)）。範囲ロケットの爆発は、どこでもと同じく届く艦すべてにダメージを与えますが、その中の他の小惑星は何も受けません。
- **レーザーは少しだけ効き、ドローンは何もしません。** 小惑星を選択して、ダブルクリックするか、攻撃キーまたは弾薬スロットを押すと、小惑星の中心がレーザーの射程内にある間、レーザーが毎秒1回撃ち、艦に対してと同じように弾薬を消費します。ダブルクリックは常に小惑星を撃ちます。攻撃キーと弾薬スロットは、艦もエイリアンも選択していないときに小惑星を撃ちます。Siphon 弾薬はシールドを吸い取るだけで小惑星にはダメージを与えられないため、その命令は拒否されます。
- **ダメージ。** ロケットは、自身のロール値を小惑星の船体から引き、[ドローン編成](/wiki/03-Mechanics/Formations.md)のロケットボーナスは艦に対してと同じように効きます（Ballista の+55%も）。レーザー、アンプ、ブースター、弾薬はロケットのロール値を変えません。レーザーの斉射は、シールドのない艦に与えるダメージの5%を引き、アンプ、ブースター、弾薬、クリティカルヒット、編成も計算に含まれます。ボーナスが先で、**装甲つき**の小惑星はそのあとで命中ごとに装甲の値を引き、範囲爆発は**もろい**結晶の小惑星により大きなダメージを与えます（数値は「ルール」と「種類一覧」にあります）。小惑星にはシールドがなく、回復もしません。削った岩は、誰かが壊すまで削れたままです。
- **何発か。** 各種類は特定のロケット向けに作られており、「種類一覧」におよそ何発で壊れるかが書かれています。ターゲット画面とホバーカードには、手に持っているロケットの場合と、その横にレーザーの斉射でおよそ何回かかるかが表示されます。強いワールドほど船体が大きくなります（「ワールド」）。飛行中のあなたのロケットは、他の誰かが小惑星を壊した場合、普通のロケットとして飛び続け、無駄になります。

## 遮蔽 {#cover}

小惑星は遮蔽物になります。**射撃の進路上にある最初の小惑星が、その射撃を受け止めます。** パイロット、エイリアン、または別の小惑星に向けて撃たれたレーザーの斉射、ロケット、範囲ロケットの爆発は、撃った艦から標的までの直線上にある最初の小惑星に止められます。標的は何も受けず、小惑星が命中を受けます。そのため、小惑星の陰に隠れて、パイロットからもエイリアンからも身を守れます。ロックオンは射撃ではないので止められません。小惑星の陰にいるパイロットをロックオンすることはできますが、レーザーは小惑星に当たります。

- **内側から。** 中心が小惑星の内側にある艦は、どこを狙っても、すべての射撃がその小惑星に当たります。
- **止められるもの。** パイロット、エイリアン（群れの艦、Clan Warden、Slumbering Void）、企業パイロットのレーザーの斉射とロケットのすべてで、N.U.K.E. も含みます。小惑星の上を飛び越えるものは2つあります。[N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) と Dormant Swamp の砲です。Venom のようなアビリティやブラックホールは射撃ではありません。
- **小惑星が受けるもの。** ロケットはロケットが与えるだけのダメージを与え、レーザーの斉射は、レーザーが小惑星に与える分、つまり艦に与えるダメージの5%から小惑星の装甲を引いた分を与えます。ほかの小惑星へのダメージと同じように数えられるので、射撃で小惑星を壊したパイロットはその分の報酬を受け取ります（[破片を受け取る人](#who-gets-the-chunks)）。エイリアンの射撃は小惑星に何のダメージも与えません。報酬を受け取る人がいないからです。
- **進路。** 小惑星は、描かれたとおりの姿をちょうど囲む円で、ロケットは艦に触れるときと同じように、縁の数ユニット手前で触れます。小惑星の向こう側にいる標的、または中心が小惑星の内側にある標的は遮蔽され、縁のちょうど上にいる標的は遮蔽されません。進路の脇にある小惑星や、標的の後ろ、撃った艦の後ろにある小惑星は邪魔になりません。
- **消費はいつもどおり。** 小惑星に止められた射撃も、ほかの射撃と同じように弾薬、ロケット、タイマーを消費します。

## 壊すと残るもの {#what-a-break-leaves}

小惑星が壊れた時点では、何も支払われません。小惑星は瓦礫になって砕け、いくつかの**破片**を飛ばします。クレジットは小さな金の塊、Thulium はラベンダー色の結晶、鉱石は荒い石です。破片は瓦礫からただよい出て、ほかの[コンテナ](/wiki/03-Mechanics/Cargo.md)と同じように揺れます。1つをクリックすると艦がそこへ飛び、ほかのコンテナと同じく短いチャネルで回収します（[回収のしかた](/wiki/03-Mechanics/Cargo.md#collecting)）。鉱石はハンガーのインベントリに、クレジットと Thulium はアカウントに入り、入手した内容は通知で知らされます。

大きな小惑星ほど破片が多く残ります（「種類一覧」の「金銭の破片」列。クレジットと Thulium はその数に分かれ、鉱石はもう1つ加わります）。回収後は、近くにある自分が取れる小惑星の次の破片へ艦が自動で向かいます。自分の移動命令を出すと止まります。

## 破片を受け取る人 {#who-gets-the-chunks}

小惑星は共同作業です。ロケットでもレーザーでも何人でも攻撃でき、破片は最初に撃った人や最後に撃った人ではなく、各自が与えたダメージで決まります。ターゲット画面のダメージ欄に、誰がどれだけ与えたか、あなたが来る前に与えられた分が表示されます。壊れたときのクレジットと Thulium は1回だけ抽選され、ダメージに応じて分配されます。鉱石は与えたダメージが大きかったパイロットで分け合い、レアな獲得物は最も多く与えたパイロットのものになります。「ルール」の割合に届かなかったパイロットは何も受け取れず、ゲームログにその旨が出ます。破片は支払い対象のパイロットごとに置かれ、しばらくはそのパイロットとそのクランに取り置かれ、その後は誰でも取れます。

## ルール {#the-rules}

<!-- asteroids-rules:begin -->
<!-- Generated from server/Resources/Asteroids.json (and Rockets.json) by scripts/asteroids-wiki.sh: don't edit by hand. -->

- 小惑星に与えたダメージの 5% 以上を与えたパイロットは、与えたダメージに応じてその破片の取り分を受け取ります。誰も 5% に届かなかった場合は、最も多く与えたパイロットがすべて受け取ります。
- [グループ](/wiki/03-Mechanics/Groups.md#sharing-kills)は1人のパイロットとして数えられ、その取り分は、近くで撃っているグループメンバーの間でレベルに応じて分けられます。
- 壊れたときの破片は、置かれた相手のパイロットとそのクランに 30秒取り置かれます。その後はマップ上の誰でも取れます。誰も取らなかった破片は 3分後に消えます。
- 1つのマップに置ける破片は最大 36 個で、マップ全体の上限 64 個のコンテナの中に収まります。破片がエイリアンのコンテナを押し出すことはなく、エイリアンのコンテナが破片を押し出すこともありません。破片を置く余地がないときは、その破片を受け取るはずだったパイロットにすぐ支払われます。
- クレジットと Thulium は、小惑星が壊れたときではなく、破片を回収したときに支払われます。任意の 24時間のあいだにパイロットが受け取れるのは、最大で[ワールド](#the-worlds)の上限までです。上限を超える破片は消費されて、上限の残りの分だけ支払われ、ゲームログにその旨が出ます。
- 報酬はだれでも同じです。プレミアム特典、シーズンストアのブースト、クランのブースト、Loot Luck、ブースターのいずれも、クレジット、Thulium、獲得物を変えません。[Resource Magnet Booster](/wiki/06-Items/Boosters.md) は、ほかのコンテナと同じように、鉱石の破片を回収するときにその資源を増やします。
- 装甲は命中ごとに自分の値を引きますが、命中の 20% 以上は必ず通ります。
- 範囲爆発は、もろい小惑星にはほかの小惑星の 1.6 倍のダメージを与えます。
- 小惑星は、安全リングの縁から 1,500 ユニット以内、ブラックホールの中心から 4,200 ユニット以内、マップの端から 600 ユニット以内には存在せず、パイロットから 1,200 ユニット以内にも現れません。
- 壊れたあと、同じ種類の小惑星が、セクターの行にある時間がたつとマップの別の場所に育ちます。時間は前後 25% ほどずれます。
- Motherlode は、どのセクターでも 1時間後に戻ります。

<!-- asteroids-rules:end -->

## ワールド {#the-worlds}

Alpha、Beta、Gamma の各ワールドには、同じ場所にそれぞれ独自の小惑星があります（[ワールド](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)）。自分のワールドで壊した小惑星は、ほかのワールドでは壊れていません。大きいワールドほど船体が大きく、報酬も大きくなります。

<!-- asteroids-worlds:begin -->
<!-- Generated from server/Resources/Asteroids.json (and Rockets.json) by scripts/asteroids-wiki.sh: don't edit by hand. -->

| ワールド | 船体 | 報酬倍率 | Thulium の上限 | クレジットの上限 |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha** | ×1 | ×1 | 3,000 | 13,000,000 |
| **Beta** | ×1.5 | ×2 | 4,500 | 18,000,000 |
| **Gamma** | ×2 | ×3 | 6,000 | 21,000,000 |

下の表は Alpha の小惑星の数値です。**船体**は各小惑星の船体にかかるワールドの倍率、**報酬倍率**は壊したときのクレジットと Thulium にかかる倍率です。鉱石とレアな獲得物はどのワールドでも同じです。2つの上限は、任意の 24時間のあいだに1人のパイロットが破片で受け取れる最大量です。

<!-- asteroids-worlds:end -->

## ある場所 {#where-they-are}

3つの企業の本拠地セクターと危険セクターのすべてに小惑星があり、セクターごとに構成が違います。主にそのリングの種類で、1つ上か下のリングから1、2種類が加わります。ゲートが通じていない中立セクターにはありません。危険セクターの小惑星は、表にあるシーズン日から現れます。PvP が解禁される日です（[ファーストコンタクト](/wiki/03-Mechanics/Wipe-Timeline.md)）。ほかは初日からあります。壊れたあとは、そのセクターの行にある時間がたつと、同じ種類の新しい小惑星が育ちます。シーズン11日目からは、パルサー、巨大掘削機、Dormant Swamp の中心の近くに小惑星はなく（[危険セクター](/wiki/01-General/Danger-Sectors.md#where-everything-is)）、イベント2が始まったときにそこにあった岩は消えます。

<!-- asteroids-maps:begin -->
<!-- Generated from server/Resources/Asteroids.json (and Rockets.json) by scripts/asteroids-wiki.sh: don't edit by hand. -->

| セクター | 小惑星 | 開始日 | 復活 | 種類 |
| :--- | ---: | ---: | ---: | :--- |
| `M-1` | 12 | 1 | 2分 | 3 × Pebble, 3 × Cobble, 2 × Glimmer, 2 × Cache Pod, 2 × Ironhide |
| `T-1` | 12 | 1 | 2分 | 3 × Rime, 3 × Cache Pod, 2 × Cobble, 2 × Pebble, 2 × Dark Chondrite |
| `G-1` | 12 | 1 | 2分 | 4 × Glimmer, 2 × Pebble, 2 × Rime, 2 × Cobble, 2 × Nyx Geode |
| `M-2` | 14 | 1 | 3分 | 4 × Ironhide, 3 × Dark Chondrite, 3 × Scrap Hulk, 2 × Vein Rock, 1 × Cobble, 1 × Pebble |
| `T-2` | 14 | 1 | 3分 | 4 × Scrap Hulk, 3 × Dark Chondrite, 3 × Vein Rock, 2 × Nyx Geode, 2 × Rime |
| `G-2` | 14 | 1 | 3分 | 4 × Nyx Geode, 3 × Vein Rock, 3 × Dark Chondrite, 2 × Ironhide, 2 × Glimmer |
| `M-3` | 16 | 1 | 5分 | 3 × Plateback, 3 × Slag Block, 3 × Lode Rock, 3 × Cataclast, 2 × Derelict Hulk, 2 × Cataclysite Mass |
| `T-3` | 16 | 1 | 5分 | 3 × Derelict Hulk, 3 × Slag Block, 3 × Cataclast, 3 × Lode Rock, 2 × Thulium Geode, 2 × Derelict Cruiser |
| `G-3` | 16 | 1 | 5分 | 4 × Cataclast, 3 × Slag Block, 3 × Thulium Geode, 2 × Plateback, 2 × Lode Rock, 2 × Quorvium Boulder |
| `M-4` | 18 | 1 | 5分 | 4 × Anvil, 4 × Cataclysite Mass, 4 × Quorvium Boulder, 2 × Derelict Cruiser, 2 × Vault Rock, 2 × Plateback |
| `T-4` | 18 | 1 | 5分 | 4 × Derelict Cruiser, 4 × Quorvium Boulder, 4 × Cataclysite Mass, 2 × Thulium Cluster, 2 × Vault Rock, 2 × Thulium Geode |
| `G-4` | 18 | 1 | 5分 | 5 × Quorvium Boulder, 3 × Cataclysite Mass, 3 × Anvil, 3 × Lode Rock, 2 × Thulium Cluster, 2 × Vault Rock |
| `DS-1` | 24 | 4 | 5分 | 8 × Rich Lode, 6 × Prism Cluster, 4 × Ancient Husk, 3 × Star Crystal, 2 × Vault Rock, 1 × Motherlode |
| `DS-2` | 24 | 4 | 5分 | 7 × Rich Lode, 7 × Ancient Husk, 3 × Star Crystal, 3 × Anvil, 3 × Derelict Cruiser, 1 × Motherlode |
| `DS-3` | 24 | 4 | 5分 | 9 × Prism Cluster, 5 × Rich Lode, 4 × Star Crystal, 3 × Quorvium Boulder, 2 × Cataclysite Mass, 1 × Motherlode |
| `DS-4` | 24 | 4 | 5分 | 9 × Rich Lode, 5 × Prism Cluster, 4 × Ancient Husk, 3 × Cataclysite Mass, 2 × Derelict Cruiser, 1 × Motherlode |

<!-- asteroids-maps:end -->

## 種類一覧 {#the-kinds}

<!-- asteroids-kinds:begin -->
<!-- Generated from server/Resources/Asteroids.json (and Rockets.json) by scripts/asteroids-wiki.sh: don't edit by hand. -->

小惑星には 8 個のファミリーに分かれた 27 種類があります。**対応ロケット**は、その種類がバランスされているロケットと、Alpha で壊すのにおよそ何発かかるかです。**獲得物**は、壊れたときに抽選される鉱石とレアな獲得物で、その破片が分け合います。パーセントはその行の確率で、ほかの行は必ず手に入ります。クレジットと Thulium は、壊れたときの Alpha の量です。

### 岩石 {#stone}

ふつうの岩：装甲も弱点もありません。

| 種類 | 船体 | サイズ | 特性 | 金銭の破片 | 対応ロケット | クレジット | Thulium | 獲得物 | 出現場所 |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Pebble** | 8,500 | 極小 | – | 1 | [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約4⁠発 | 6,600–11,100 | 22%で3個 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3 (49%) | `M-1`, `T-1`, `G-1`, `M-2` |
| **Cobble** | 10,000 | 小 | – | 1 | [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約5⁠発 | 6,300–10,500 | 25%で3個 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–9 (89%) | `M-1`, `T-1`, `G-1`, `M-2` |
| **Dark Chondrite** | 12,000 | 小 | – | 1 | [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約3⁠発 | 7,050–11,850 | 65%で3個 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–12 (91%), [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (93%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `T-1`, `M-2`, `T-2`, `G-2` |
| **Vein Rock** | 18,000 | 小 | – | 1 | [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約4⁠発 | 13,350–22,200 | 50%で3–9個 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–6 (73%), [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (45%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `M-2`, `T-2`, `G-2` |
| **Slag Block** | 24,000 | 中 | – | 2 | [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約5⁠発 | 18,600–31,050 | 50%で3–9個 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (95%), [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 3–6 (84%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1.5%) | `M-3`, `T-3`, `G-3` |
| **Cataclast** | 36,000 | 中 | – | 2 | [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約8⁠発 | 22,350–37,200 | 50%で6–15個 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 9–18, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–24; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1.5%) | `M-3`, `T-3`, `G-3` |
| **Lode Rock** | 52,000 | 中 | – | 2 | [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約11⁠発 | 34,950–58,200 | 50%で18–39個 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 9–18, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–24; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1.5%) | `M-3`, `T-3`, `G-3`, `G-4` |
| **Cataclysite Mass** | 72,000 | 大 | – | 2 | [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約10⁠発 | 44,700–74,550 | 50%で21–45個 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 15–30, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 9–15; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `M-3`, `M-4`, `T-4`, `G-4`, `DS-3`, `DS-4` |
| **Rich Lode** | 80,000 | 大 | – | 3 | [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約11⁠発 | 61,800–103,050 | 50%で39–90個 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–24, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 6–12; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (8%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (5%) | `DS-1`, `DS-2`, `DS-3`, `DS-4` |

### 氷 {#ice}

凍った岩：装甲も弱点もありません。

| 種類 | 船体 | サイズ | 特性 | 金銭の破片 | 対応ロケット | クレジット | Thulium | 獲得物 | 出現場所 |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Rime** | 12,000 | 小 | – | 1 | [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約5⁠発 | 8,250–13,800 | 55%で3個 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–9 (77%) | `T-1`, `G-1`, `T-2` |

### 結晶 {#crystal}

もろい：範囲爆発は、結晶の小惑星に直撃より大きなダメージを与えます。

| 種類 | 船体 | サイズ | 特性 | 金銭の破片 | 対応ロケット | クレジット | Thulium | 獲得物 | 出現場所 |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Glimmer** | 9,000 | 極小 | 爆発 ×1.6 | 1 | [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約4⁠発 | 6,150–10,350 | 41%で3個 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–6 (77%) | `M-1`, `G-1`, `G-2` |
| **Nyx Geode** | 26,000 | 中 | 爆発 ×1.6 | 2 | [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約6⁠発 | 16,650–27,750 | 50%で9–21個 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 6–15, [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3–6 (96%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `G-1`, `T-2`, `G-2` |
| **Quorvium Boulder** | 48,000 | 中 | 爆発 ×1.6 | 2 | [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約7⁠発 | 29,850–49,650 | 50%で12–30個 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–21, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 3–15 (86%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `G-3`, `M-4`, `T-4`, `G-4`, `DS-3` |
| **Prism Cluster** | 100,000 | 大 | 爆発 ×1.6 | 3 | [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約14⁠発 | 71,700–119,550 | 50%で27–60個 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 24–42, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 12–21; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (8%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (5%) | `DS-1`, `DS-3`, `DS-4` |

### 残骸 {#salvage}

残骸とポッド：Ship Fragment を含みます。

| 種類 | 船体 | サイズ | 特性 | 金銭の破片 | 対応ロケット | クレジット | Thulium | 獲得物 | 出現場所 |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Cache Pod** | 14,000 | 極小 | – | 1 | [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約6⁠発 | 9,000–15,000 | 29%で3個 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–6 (83%), [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 3–9 (78%) | `M-1`, `T-1` |
| **Scrap Hulk** | 20,000 | 小 | – | 1 | [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約5⁠発 | 12,150–20,250 | 92%で3個 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–9 (95%), [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (77%), [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 6–12; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `M-2`, `T-2` |
| **Derelict Hulk** | 52,000 | 中 | – | 2 | [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約11⁠発 | 33,150–55,200 | 50%で9–18個 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 6–12, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 9–18, [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 30–54; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1.5%) | `M-3`, `T-3` |
| **Derelict Cruiser** | 72,000 | 大 | – | 2 | [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約10⁠発 | 46,200–76,950 | 50%で18–39個 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 9–15, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 3–9 (97%), [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 21–36; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `T-3`, `M-4`, `T-4`, `DS-2`, `DS-4` |

### 鉄 {#iron}

装甲つき：命中ごとに装甲の分だけダメージが減るため、船体から想像するより強いロケットが必要です。

| 種類 | 船体 | サイズ | 特性 | 金銭の破片 | 対応ロケット | クレジット | Thulium | 獲得物 | 出現場所 |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Ironhide** | 14,000 | 小 | 装甲 500 | 1 | [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約4⁠発 | 13,650–22,650 | 50%で3–9個 | [Daraxium](/wiki/06-Items/Resources.md#daraxium) 3–6 (74%), [Nyxite](/wiki/06-Items/Resources.md#nyxite) 3 (46%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (2%) | `M-1`, `M-2`, `G-2` |
| **Plateback** | 36,000 | 中 | 装甲 1,500 | 2 | [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約11⁠発 | 31,650–52,800 | 50%で9–18個 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 6–12, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 9–15, [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 27–51; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1.5%) | `M-3`, `G-3`, `M-4` |
| **Anvil** | 80,000 | 大 | 装甲 3,000 | 2 | [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約18⁠発 | 84,900–141,450 | 50%で30–72個 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 15–27, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 6–15, [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) 36–69; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `M-4`, `G-4`, `DS-2` |

### 財宝 {#treasure}

最高の支払い：どれも、そのリングの平均的な小惑星より多くのクレジットと Thulium を支払います。

| 種類 | 船体 | サイズ | 特性 | 金銭の破片 | 対応ロケット | クレジット | Thulium | 獲得物 | 出現場所 |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Thulium Geode** | 66,000 | 中 | 爆発 ×1.6 | 2 | [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約14⁠発 | 42,450–70,800 | 18–42 | [Nyxite](/wiki/06-Items/Resources.md#nyxite) 9–15, [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–21; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1 (4%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (1.5%) | `T-3`, `G-3`, `T-4` |
| **Thulium Cluster** | 100,000 | 大 | – | 2 | [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約14⁠発 | 62,100–103,500 | 42–99 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 12–21, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 3–15 (90%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `T-4`, `G-4` |
| **Vault Rock** | 130,000 | 大 | – | 3 | [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約18⁠発 | 101,400–169,050 | 50%で36–87個 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 9–18, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 3–12 (90%); [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (6%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (3%) | `M-4`, `T-4`, `G-4`, `DS-1` |
| **Star Crystal** | 150,000 | 大 | 爆発 ×1.6 | 3 | [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約21⁠発 | 109,650–182,700 | 60–141 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 18–33, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 9–15; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (8%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (5%) | `DS-1`, `DS-2`, `DS-3` |

### 遺物 {#relic}

死んだ群れの艦の殻：装甲があり、レアな獲得物が豊富です。

| 種類 | 船体 | サイズ | 特性 | 金銭の破片 | 対応ロケット | クレジット | Thulium | 獲得物 | 出現場所 |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Ancient Husk** | 120,000 | 大 | 装甲 2,000 | 3 | [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約22⁠発 | 114,300–190,350 | 50%で57–129個 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 24–45, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 12–24; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (16%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (10%) | `DS-1`, `DS-2`, `DS-4` |

### タイタン {#titan}

最大の小惑星。グループ向けの岩です。

| 種類 | 船体 | サイズ | 特性 | 金銭の破片 | 対応ロケット | クレジット | Thulium | 獲得物 | 出現場所 |
| :--- | ---: | :--- | :--- | ---: | :--- | ---: | ---: | :--- | :--- |
| **Motherlode** | 450,000 | 巨大 | – | 3 | [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets) 約61⁠発 | 348,900–581,400 | 165–381 | [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) 69–126, [Quorvium](/wiki/06-Items/Resources.md#quorvium) 36–66; [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) 1–2 (8%), [Power Core](/wiki/06-Items/Resources.md#power-core) 1 (5%) | `DS-1`, `DS-2`, `DS-3`, `DS-4` |

<!-- asteroids-kinds:end -->

## 得られないもの {#what-it-does-not-give}

小惑星はキルではありません。壊しても、XP、名誉、キル数、PvE や PvP のポイント、ランキング、[ワイプポイント](/wiki/03-Mechanics/Wipe-Timeline.md#earning-wipe-points)、ドローンの XP、[ミッション](/wiki/03-Mechanics/Quests.md)の進行は、各レベルの[小惑星ミッション](/wiki/03-Mechanics/Quests.md#levels)を除いて得られません。シーズンストアのブーストも効きません。得られるのは表にあるもの、つまりクレジット、Thulium、鉱石で、[資源](/wiki/06-Items/Resources.md)のページにエイリアンのドロップと並べて載っています。

## コツ {#tips}

- **その種類向けのロケットから始める。** 弱いロケットでも壊せますが、数もタイマーも余計にかかります。強いロケットは速いものの、残りの船体を超えたダメージは無駄になり、ロケットのコストは何に当てても同じです。
- **結晶には爆発、鉄には強さ。** もろい小惑星には Scatter や Ember が向いています。装甲つきは、命中ごとに装甲の分が引かれるため、船体から想像するより強いロケットが必要です。
- **ロケットの合間にレーザーを働かせましょう。** レーザーは毎秒1回撃ち、消費するのはロケットではなく弾薬ですが、1回の斉射が与えるのは艦に対するダメージの5%だけです。ロケットを補うもので、代わりにはなりません。
- **1日の上限に注意。** 1日にワールドの上限まで回収すると、破片はそれ以上支払われません。採掘は稼ぎが良いので、上限には数時間で届きます。上限は「ワールド」にあります。
- **大きいものは一緒に壊す。** 小惑星 Motherlode はグループ向けの岩です。グループは1人として数えられ、その取り分は、近くで撃っているグループメンバーの間でレベルに応じて分けられます。
- **セクターに気を配る。** 小惑星は反撃しませんが、周りのセクターにはエイリアンがいて、危険セクターでは他のパイロットもいます。
- **利用しつつ、気をつける。** 自分と相手やエイリアンの間にある小惑星は、お互いのレーザーを遠ざけます。採掘中の小惑星越しに撃ってくる相手はその小惑星にダメージを与え、ほかのパイロットと同じく与えたダメージに応じた報酬を受け取ります。
