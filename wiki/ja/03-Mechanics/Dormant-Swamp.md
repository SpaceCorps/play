<!-- wiki-i18n source: 3c07d568f3af3aab -->
<!-- wiki-i18n title: Dormant Swamp -->
# Dormant Swamp

<!-- wiki-search: swamp; dormant swamp; base; turret; turrets; nike turret; laser turret; inert mass; unwakened; the unwakened; slumbering void; void; dormant lance; ds-4; 沼; 砲台 -->

はるか昔、銀河の中心には高度な文明がありました。紫がかった黒い結晶で築かれ、光る紫の脈が走り、理由は誰にも分からないまま崩壊しました。**Dormant Swamp** はその前哨基地で、`DS-4` の左上の隅にあります。シーズン11日目から、それは動き出します。中心の砲台が見えた艦船をすべて撃ち、**Inert Mass** が守り、真ん中では **Unwakened** が眠っています。ステルスなら Unwakened のところまで飛べます。[Deep Void](/wiki/03-Mechanics/Deep-Void.md) が開いてからは、砲台と Unwakened は破壊でき、シーズン最初に Unwakened が倒されると、そのワールドの Threshold が開きます。基地そのものには、入ることも、乗り込むことも、取引することもできません。

沼は、11日目から [Dormant の群れ](/wiki/05-Swarms/Dormant-Swarm.md)が現れる場所でもあり、**Slumbering Void** がその周りを巡回します。同じ Void が、ウェーブで[巨大掘削機](/wiki/03-Mechanics/Giant-Excavator.md#the-slumbering-voids)にも来ます。セクターは[危険セクター](/wiki/01-General/Danger-Sectors.md)にあります。

![Flying in towards the Dormant Swamp: the amber notice ring and, inside it, the red ring of the zone the guns reach](../../img/wiki-img/shots/swamp-rings.jpg)

## 概要 {#at-a-glance}

<!-- swamp-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **場所**：`DS-4` の左上の隅：中心は 5,000 / 5,000
- **出現**：シーズン11日目からワイプまで
- **ゾーン**：中心から4,300ユニット：砲台が届く最大距離
- **通告**：中心から4,800ユニットのリングを越えた艦には、システムの行が届きます
- **ステルス**：どの砲台も、ステルス中の艦や EMP の効果時間内の艦を見ません
- **エイリアン**：Inert Mass が5体、中心から2,400ユニット以内にとどまります。Unwakened は中心で眠っています。Slumbering Void が2体、中心から4,600～6,500ユニットのあいだを巡回します。
- **Dormant の群れ**：9,417 / 6,606 に現れます。中心から4,700ユニット離れた、ゾーンの外です
- **岩**：中心から4,900ユニット以内には小惑星がありません

<!-- swamp-glance:end -->

## 砲台 {#the-guns}

沼の砲台は、射程内で**見えている最も近い艦**を撃ち、ほかは撃ちません。ゾーンとは、その中で最も遠くまで届く砲台が届く円のことです。砲台は艦ではありませんが、Deep Void が開いてからはそれぞれに耐久値があります。砲台をクリックするとレーザーで撃てて、近くではじけたロケットもダメージを与えます。破壊された砲台は Unwakened が戻るまで止まったままです。ただし砲台の弾は本物で、ワールドは、どのエイリアンの武器にもするように、そのダメージを倍率で調整します。

<!-- swamp-guns:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

1発のダメージ（各ワールド）：

| 砲台 | 位置 | 発射間隔 | 射程（ユニット） | Alpha | Beta | Gamma |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) 砲台 | 5,000 / 4,400 | 2秒 | 3,640 | 75,000 | 112,500 | 150,000 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) 砲台 | 5,000 / 4,400 | 5秒 | 1,080 | 50,000 | 75,000 | 100,000 |
| レーザー砲台 × 2 | 3,600 / 5,200; 6,400 / 5,200 | 1秒 | 2,500 | 45,000–55,000 | 67,500–82,500 | 90,000–110,000 |

- ロケットは、確実に届くよう、パイロットが使う同じロケットの射程の82%の距離から発射されます。レーザー砲台は毎秒1発撃ち、ダメージは示された範囲でランダムに決まります。
- N.I.K.E. のシールド貫通は35%で、シールドの吸収率から差し引かれます。
- 砲台の N.I.K.E. は、あなたのものより25%速く、2倍の距離を飛びます。毎秒1,250ユニットで合計8,910ユニット飛ぶため、逃げる艦も遠くまで追われます。
- N.U.K.E. は半径1,013ユニットで炸裂し、中心が最も強力です。
- 砲台の N.U.K.E. は、あなたのものより25%速く、2倍の距離を飛びます。毎秒375ユニットで合計2,640ユニット飛ぶため、逃げる艦も遠くまで追われます。

<!-- swamp-guns:end -->

- **ゾーンの外からは何も撃ってきません。**中では艦が数秒で破壊されます。中心に近づくほど砲台が増え、最良のシールドを積んだ Wraith でももちません。 ただし、すでに飛んでいるロケットはそのまま飛び続けます。砲台のロケットはあなたのものより速く、遠くまで飛ぶので、まっすぐ逃げるだけでは振り切れません。
- **ステルスなら入れます。**どの砲台も、ステルス中の艦や EMP の効果時間内の艦を、どんな距離でも見ません。見えている艦を狙った爆発がステルス中の艦の近くで炸裂した場合は、それでも傷つけ、ステルスを解除します。
- **撃つのはパイロットだけです。**エイリアン、企業パイロット、群れは撃たず、破壊から復帰したばかりの艦の保護は、砲台に対しても有効です。
- **通告リング。**ゾーンの外のリングを越えた艦には、システムの行が届きます。砲台は見えた艦船をすべて撃ち、中心では何かが眠っている、と。リングを出て戻ったときだけ、また知らされます。
- **脱出。**そこで破壊されてもその場では復帰できず（危険セクターでは基地と最寄りのポータルだけが選べます）、ゾーン内でログインすると外に出されます。クリックした針路はゾーンを迂回するよう曲げられ、クリックした場所が内側にあるとトーストで警告されます。

## エイリアン {#the-aliens}

失われた文明の3体のエイリアンがここにいて、それぞれに専用の数値があります。群れのボスと同じように、**与えたダメージに応じて**報酬が支払われます。[群れ](/wiki/05-Swarms/Swarms.md#the-rules-of-every-swarm)にある割合以上を与えたパイロット全員が対象で、コンテナは最も多くのダメージを与えたパイロットに渡ります。撃破は、群れの艦と同じく、報酬に比例してあなたの PvE ランクポイントに加わります（[階級](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points)）。それぞれのシールドは、持つかぎり、命中の{{guide:vitals.absorbance@Slumbering Void;Inert Mass;The Unwakened}}を吸収します（[シールド](/wiki/03-Mechanics/Shields.md)）。

- **Slumbering Void。** 細身の狩人で、ゲームで最も速いエイリアンです（Afterburner III を使った Storm より速い）。数体は沼の周辺を常に巡回し、ほかはウェーブで掘削機に来ます。攻撃的で、見えている最も近いパイロットを狩り、ステルス中の艦は決して見ません。
- **Inert Mass。** 紫のひびが入った死んだ巨体で、小さなステーションほどの大きさです。沼の中心から決まった距離内にとどまり、今のところそこを離れません。**Dormant Lance** を撃ちます。射程が非常に長い誘導ロケットで、艦がステルスになる、EMP の効果時間を開く、安全リングに入る、ジャンプする、または死ぬまで追い続けます。どの艦より速いので、効くのはこれらの中断だけです。 Dormant Lance の進路にある小惑星はそれを止め、Lance は自身のダメージでその小惑星を傷つけます（それで報酬を受け取る人はいません）。そのため、岩が Inert Mass から身を守ってくれるのは数発のあいだだけです。
- **Unwakened。** 沼の中心で眠るモノリスで、どのマップでも最大の存在です。あまりに遅いので、艦を捕まえることはありません。何も撃ちませんが、オーラの中の艦はすべて、**ステルス中でもそうでなくても**焼かれます。[Deep Void](/wiki/03-Mechanics/Deep-Void.md) が開いてからは倒せます。与えたダメージに応じて報酬が支払われ、死んでから 1 日後に戻り、各ワールドでシーズン最初の撃破がそのワールドの Threshold を開きます。パイロットの**放射線技術**はこの焼かれる量を下げ、レベル100では0.40倍になります。

<!-- swamp-members:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

### Slumbering Void

Slumbering Void が2体、沼の中心から4,600～6,500ユニットのあいだを巡回します。撃破された個体は{{guide:vitals.respawn@Slumbering Void}}後に戻ります。掘削機のウェーブは、同じエイリアンをさらに連れてきます。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@Slumbering Void}} | {{guide:vitals.hull*1.5@Slumbering Void}} | {{guide:vitals.hull*2@Slumbering Void}} |
| シールド | {{guide:vitals.shield@Slumbering Void}} | {{guide:vitals.shield*1.5@Slumbering Void}} | {{guide:vitals.shield*2@Slumbering Void}} |
| シールド吸収率 | {{guide:vitals.absorbance@Slumbering Void}} | {{guide:vitals.absorbance@Slumbering Void}} | {{guide:vitals.absorbance@Slumbering Void}} |
| レーザーのダメージ （毎秒1斉射） | {{guide:vitals.dps@Slumbering Void}} | {{guide:vitals.dps*1.5@Slumbering Void}} | {{guide:vitals.dps*2@Slumbering Void}} |
| 速度 | {{guide:vitals.speed@Slumbering Void}} | {{guide:vitals.speed@Slumbering Void}} | {{guide:vitals.speed@Slumbering Void}} |
| レーザーの射程 | 800 | 800 | 800 |
| 索敵範囲 | {{guide:vitals.aggro@Slumbering Void}} | {{guide:vitals.aggro@Slumbering Void}} | {{guide:vitals.aggro@Slumbering Void}} |
| クレジット | {{guide:spoils.pay.credits@Slumbering Void}} | {{guide:spoils.pay.credits*2@Slumbering Void}} | {{guide:spoils.pay.credits*3@Slumbering Void}} |
| Thulium | {{guide:spoils.pay.thulium@Slumbering Void}} | {{guide:spoils.pay.thulium*2@Slumbering Void}} | {{guide:spoils.pay.thulium*3@Slumbering Void}} |
| 経験値（XP） | {{guide:spoils.pay.experience@Slumbering Void}} | {{guide:spoils.pay.experience*2@Slumbering Void}} | {{guide:spoils.pay.experience*3@Slumbering Void}} |
| 名誉 | {{guide:spoils.pay.honor@Slumbering Void}} | {{guide:spoils.pay.honor*2@Slumbering Void}} | {{guide:spoils.pay.honor*3@Slumbering Void}} |
| 撃破1回あたりの PvE ポイント | 10 | 10 | 10 |

**ドロップ**：最もダメージを与えたパイロットのためのコンテナ1つ。

| アイテム |
| :--- |
| {{guide:spoils.box@Slumbering Void}} |

### Inert Mass

Inert Mass が5体、中心から2,400ユニット以内にいます。撃破された個体は{{guide:vitals.respawn@Inert Mass}}後に戻ります。6秒ごとに、見えている最も近い艦へ誘導式の [Dormant Lance](/wiki/06-Items/Rockets.md#the-craft-only-rockets) を撃ちます。速度750、飛翔距離5,250ユニット、貫通40%。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@Inert Mass}} | {{guide:vitals.hull*1.5@Inert Mass}} | {{guide:vitals.hull*2@Inert Mass}} |
| シールド | {{guide:vitals.shield@Inert Mass}} | {{guide:vitals.shield*1.5@Inert Mass}} | {{guide:vitals.shield*2@Inert Mass}} |
| シールド吸収率 | {{guide:vitals.absorbance@Inert Mass}} | {{guide:vitals.absorbance@Inert Mass}} | {{guide:vitals.absorbance@Inert Mass}} |
| Dormant Lance 1発のダメージ | {{guide:behaviour.ability:rocket.damageMin@Inert Mass}}–{{guide:behaviour.ability:rocket.damage@Inert Mass}} | {{guide:behaviour.ability:rocket.damageMin*1.5@Inert Mass}}–{{guide:behaviour.ability:rocket.damage*1.5@Inert Mass}} | {{guide:behaviour.ability:rocket.damageMin*2@Inert Mass}}–{{guide:behaviour.ability:rocket.damage*2@Inert Mass}} |
| 速度 | {{guide:vitals.speed@Inert Mass}} | {{guide:vitals.speed@Inert Mass}} | {{guide:vitals.speed@Inert Mass}} |
| ロケットの射程 | 5,000 | 5,000 | 5,000 |
| 索敵範囲 | {{guide:vitals.aggro@Inert Mass}} | {{guide:vitals.aggro@Inert Mass}} | {{guide:vitals.aggro@Inert Mass}} |
| クレジット | {{guide:spoils.pay.credits@Inert Mass}} | {{guide:spoils.pay.credits*2@Inert Mass}} | {{guide:spoils.pay.credits*3@Inert Mass}} |
| Thulium | {{guide:spoils.pay.thulium@Inert Mass}} | {{guide:spoils.pay.thulium*2@Inert Mass}} | {{guide:spoils.pay.thulium*3@Inert Mass}} |
| 経験値（XP） | {{guide:spoils.pay.experience@Inert Mass}} | {{guide:spoils.pay.experience*2@Inert Mass}} | {{guide:spoils.pay.experience*3@Inert Mass}} |
| 名誉 | {{guide:spoils.pay.honor@Inert Mass}} | {{guide:spoils.pay.honor*2@Inert Mass}} | {{guide:spoils.pay.honor*3@Inert Mass}} |
| 撃破1回あたりの PvE ポイント | 15 | 15 | 15 |

**ドロップ**：最もダメージを与えたパイロットのためのコンテナ1つ。

| アイテム |
| :--- |
| {{guide:spoils.box@Inert Mass}} |

### The Unwakened

沼の中心に1体だけおり、ほかにはいません。撃破された場合は{{guide:vitals.respawn@The Unwakened}}後に戻ります。Deep Void が開いてからは倒せるようになり、ここのほかのエイリアンと同じく与えたダメージに応じて報酬が支払われます。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@The Unwakened}} | {{guide:vitals.hull*1.5@The Unwakened}} | {{guide:vitals.hull*2@The Unwakened}} |
| シールド | {{guide:vitals.shield@The Unwakened}} | {{guide:vitals.shield*1.5@The Unwakened}} | {{guide:vitals.shield*2@The Unwakened}} |
| シールド吸収率 | {{guide:vitals.absorbance@The Unwakened}} | {{guide:vitals.absorbance@The Unwakened}} | {{guide:vitals.absorbance@The Unwakened}} |
| オーラの毎秒ダメージ（中のすべての艦に） | {{guide:behaviour.ability:aura.damagePerSecond@The Unwakened}} | {{guide:behaviour.ability:aura.damagePerSecond*1.5@The Unwakened}} | {{guide:behaviour.ability:aura.damagePerSecond*2@The Unwakened}} |
| オーラの半径 | 700 | 700 | 700 |
| 速度 | {{guide:vitals.speed@The Unwakened}} | {{guide:vitals.speed@The Unwakened}} | {{guide:vitals.speed@The Unwakened}} |
| 索敵範囲 | {{guide:vitals.aggro@The Unwakened}} | {{guide:vitals.aggro@The Unwakened}} | {{guide:vitals.aggro@The Unwakened}} |
| クレジット | {{guide:spoils.pay.credits@The Unwakened}} | {{guide:spoils.pay.credits*2@The Unwakened}} | {{guide:spoils.pay.credits*3@The Unwakened}} |
| Thulium | {{guide:spoils.pay.thulium@The Unwakened}} | {{guide:spoils.pay.thulium*2@The Unwakened}} | {{guide:spoils.pay.thulium*3@The Unwakened}} |
| 経験値（XP） | {{guide:spoils.pay.experience@The Unwakened}} | {{guide:spoils.pay.experience*2@The Unwakened}} | {{guide:spoils.pay.experience*3@The Unwakened}} |
| 名誉 | {{guide:spoils.pay.honor@The Unwakened}} | {{guide:spoils.pay.honor*2@The Unwakened}} | {{guide:spoils.pay.honor*3@The Unwakened}} |
| 撃破1回あたりの PvE ポイント | 112 | 112 | 112 |

**ドロップ**：最もダメージを与えたパイロットのためのコンテナ1つ。

| アイテム |
| :--- |
| {{guide:spoils.box@The Unwakened}} |

<!-- swamp-members:end -->

## Deep Void の開放後 {#with-the-deep-void}

Deep Void でここが変わった点のまとめです。

- **Unwakened は倒せます。** もう無敵ではありません。ここのほかのエイリアンと同じく与えたダメージに応じて報酬が支払われ、死んでから 1 日後に戻ってきます。
- **砲台は破壊できます。** 3 基の砲台（N.I.K.E. と N.U.K.E. の両方を撃つロケット砲台と、2 基のレーザー砲台）にはそれぞれ耐久値があり、レーザーとロケットでダメージを与えられます。破壊された砲台は Unwakened が戻るまで止まったままです。
- **最初の撃破で Threshold が開きます。** 各ワールドでシーズン最初に Unwakened が倒されると、`DS-4` の反対側の隅にそのワールドの Threshold が開きます。そこから [Deep Void](/wiki/03-Mechanics/Deep-Void.md) が始まります。

## ここでできること {#what-to-do-here}

- **最初の撃破が道を開きます。**シーズン最初の Unwakened の撃破で、そのワールドの Threshold が開き、[Deep Void](/wiki/03-Mechanics/Deep-Void.md) への道が開きます。ゾーン内では砲台が艦船を数秒で破壊します。ゾーンの外では、ゾーンを囲むリングを巡回する Void が沼の最前線で、砲台なしでグループが戦える場所です。
- **Void には貫通で戦いましょう。**Void の大きなシールドは命中の{{guide:vitals.absorbance@Slumbering Void;Inert Mass;The Unwakened}}を吸収しますが、ほとんど意味がありません。その奥の船体は小さいからです。レーザーのシールド貫通が高いほど、早く倒れます（[レーザーと弾薬](/wiki/06-Items/Lasers.md)）。
- **Lance から離れましょう。**Inert Mass は遠くまで見え、Lance からは逃げ切れません。ステルス、EMP、安全リング、ジャンプで追尾を断つか、射程から出てください。Mass は、最強の艦の大きなグループにとっても長い戦いです。
- **Dormant の群れ**は今ではゾーンのすぐ外に現れるので、グループは砲台なしで待ち構えられます。[Dormant の群れ](/wiki/05-Swarms/Dormant-Swarm.md)を参照してください。

## 関連ページ {#where-to-read-more}

- [危険セクター](/wiki/01-General/Danger-Sectors.md)：11日目に何が変わったか。
- [巨大掘削機](/wiki/03-Mechanics/Giant-Excavator.md)：Slumbering Void のウェーブと、それが守るもの。
- [群れ](/wiki/05-Swarms/Swarms.md)と [Dormant の群れ](/wiki/05-Swarms/Dormant-Swarm.md)：ボス撃破の報酬の仕組み。
- [ロケット](/wiki/06-Items/Rockets.md#the-craft-only-rockets)：砲台が撃つ N.I.K.E. と N.U.K.E.。
- [ブラックホール](/wiki/03-Mechanics/Black-Hole.md)：`DS-4` のもう1つの危険。
- [積荷](/wiki/03-Mechanics/Cargo.md)：エイリアンが落とすコンテナ。
