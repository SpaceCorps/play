<!-- wiki-i18n source: 13c9ac551cfd01fa -->
<!-- wiki-i18n title: 危険セクター -->
# 危険セクター {#danger-sectors}

<!-- wiki-search: ds; ds-1; ds-2; ds-3; ds-4; central pvp zone; pvp zone; pulsar; giant excavator; excavator; dormant swamp; swamp; event 2; tech surge; 危険セクター; 巨大掘削機; 掘削機; パルサー; 沼; テックサージ -->

**危険セクター**は、銀河の中心にある4つのセクター、`DS-1` から `DS-4` です。3つの企業がここで出会い、どのワールドでもパイロット同士が戦えます（[スペースマップ移動](/wiki/01-General/Spacemap%20Travel.md)）。`DS-1`、`DS-2`、`DS-3` にはそれぞれ1つの企業のゲートがあり、`DS-4` は中心部で、真ん中に[ブラックホール](/wiki/03-Mechanics/Black-Hole.md)があります。どのセクターにもステーションはありません。安全な場所は、ジャンプゲートの周りのリングだけです。

かつてここには古い銀河の文明があり、高度で、紫がかった黒をしていましたが、理由は誰にも分からないまま崩壊しました。その残骸は完全に死んではいませんでした。[Dormant の群れ](/wiki/05-Swarms/Dormant-Swarm.md)が最初の兆しです。**シーズン11日目**、イベント2（**テックサージ**、[ワイプのタイムライン](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule)を参照）の始まりから、さらに多くが目を覚まし、危険セクターは変わります。ワールドのすべてのパイロットが始まった日に知らされ、新しいものはワイプまで残ります。

![Flying in towards the Dormant Swamp: the amber notice ring and, inside it, the red ring of the zone the guns reach](../../img/wiki-img/shots/swamp-rings.jpg)

## 11日目からの新要素 {#what-is-new-from-day-11}

- **巨大掘削機。** `DS-1`、`DS-2`、`DS-3` にはシーズン初日からそれぞれパルサーが1つあります。空に浮かぶ光で、それ以上のものではありません。11日目からは、その隣に**巨大掘削機**が立ちます。掘削機のタンクに Dark Matter を入れ、資源を選ぶと、パルサーを採掘します。Thulium と希少な鉱石が、誰でも拾えるコンテナとなって周りに落ちます。危険セクターで奪い合う価値のあるもののうち最も豊かで、最も危険です。[巨大掘削機](/wiki/03-Mechanics/Giant-Excavator.md)を参照してください。
- **Slumbering Void。** 掘削機が採掘しているあいだ、**Slumbering Void** がマップの端からウェーブで飛来し、近くのパイロットを狩ります。ほかのものは沼を巡回します。[Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void)を参照してください。
- **Dormant Swamp。** `DS-4` の隅に、失われた文明の基地が立っています。見えた艦船をすべて撃つ砲台、それを守る Inert Mass、そして中心にいる Unwakened です。パイロットがまだ訪れることを想定されていない場所です。[Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md)を参照してください。
- **速く、豊かになった Dormant の群れ。** 群れは沼に現れるようになり、撃破後に早く戻り、報酬は2倍になります。[Dormant の群れ](/wiki/05-Swarms/Dormant-Swarm.md)を参照してください。
- **11日目より前**は、パルサーだけが輝きます。それ以外の危険セクターは[スペースマップ移動](/wiki/01-General/Spacemap%20Travel.md)が説明するとおりです。11日目以降のワールドには、すべてが一度に揃います。

## 何がどこにあるか {#where-everything-is}

どのワールドにも、すべてのコピーがそれぞれにあります。パルサーとその掘削機は、セクターの開けた3分の1、どのゲートリングからも離れた、マップの中央に面した側に立っています。距離はマップの単位で、セクターの大きさは 32,000 × 18,000 ユニットです。

<!-- danger-sites:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

| セクター | 企業のゲート | パルサー | 巨大掘削機 |
| :--- | :--- | :--- | :--- |
| `DS-1` | Mars | 8,000 / 5,000 | 8,805 / 5,402 |
| `DS-2` | Terra | 8,000 / 13,000 | 8,805 / 12,598 |
| `DS-3` | Galactic | 24,000 / 13,000 | 23,195 / 12,598 |

<!-- danger-sites:end -->

`DS-4` にはパルサーがありません。そこにはブラックホールがあります。その隅には代わりに Dormant Swamp があり、沼の数値は[Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#at-a-glance)にあります。

<!-- danger-rules:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- パルサーはシーズン初日から輝きます。それ以外の新しいものはすべてシーズン11日目に現れ、ワイプまで残ります。
- どのワールドにも専用のパルサー、掘削機、沼があり、あるワールドで起きたことはほかのワールドでは起きません。
- パルサーから2,600ユニット以内、巨大掘削機から2,200ユニット以内、Dormant Swamp の中心から4,900ユニット以内には小惑星がありません。

<!-- danger-rules:end -->

## 危険を避けるには {#keeping-out-of-trouble}

- **放射線。** 過熱した、または破壊された掘削機とそのパルサーは、円の中にとどまる艦船をすべて焼きます（[巨大掘削機](/wiki/03-Mechanics/Giant-Excavator.md#heat-and-radiation)）。ゲームは事前に警告し、円は飛行中は地面に、そしてミニマップに描かれます。
- **沼の砲台。** 沼の砲台は、艦船が行く価値のある何かを見る前に、見えた艦船を撃ちます（[Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#the-guns)）。クリックした針路は、ブラックホールのときと同じく砲台と放射線を迂回するよう曲げられ、クリックした場所が内側にあるとトーストで警告されます。
- **そこで破壊されたら、**復帰の選択肢**その場で復帰**は、ブラックホールのときと同じく、放射線の外かつ沼のゾーンの外の最も近い地点に置きます（[はじめに](/wiki/01-General/Getting-Started.md#dying-and-coming-back)）。
- **グループと退路。** 掘削機は Void もライバルも同じように引き寄せます。[グループ](/wiki/03-Mechanics/Groups.md)で行き、最も近いゲートを把握し、危険セクターでは攻撃されているあいだジャンプで離脱できないことを忘れないでください（[攻撃を受けているときのジャンプ](/wiki/01-General/Spacemap%20Travel.md#jumping-under-fire)）。
- **それ以外はいつもどおりの PvP です。** ここに安全な場所はありません。ライバルも含め、あなたのワールドの通常のルールが適用されます。

## 関連ページ {#where-to-read-more}

- [巨大掘削機](/wiki/03-Mechanics/Giant-Excavator.md)：制御パネル、燃料、何を採掘するか、Void、熱、放射線。
- [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md)：砲台、3体のエイリアン、群れの新しい居場所。
- [Dormant の群れ](/wiki/05-Swarms/Dormant-Swarm.md)と[群れ](/wiki/05-Swarms/Swarms.md)。
- [ブラックホール](/wiki/03-Mechanics/Black-Hole.md)と [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md)：燃料の入手先。
- [小惑星採掘](/wiki/03-Mechanics/Asteroid-Mining.md)：危険セクターの岩。
