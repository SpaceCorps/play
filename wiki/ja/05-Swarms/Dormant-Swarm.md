<!-- wiki-i18n source: fcba1b51b68a9123 -->
<!-- wiki-i18n title: Dormant の群れ -->
# Dormant の群れ {#dormant-swarm}

Dormant の群れは、**Dormant Force** とその **Dormant Pulse** からなります。自分から戦いを始めることはありませんが、目を覚ますと非常に強く攻撃してくる艦の集団です。各ワールドの危険セクターには1つだけいます（[Deep Void](/wiki/03-Mechanics/Deep-Void.md#the-dormant-swarms-visit)には、1日に1回の独自の訪問があります）。危険セクターを次々に渡り歩き、群れの中で最も厳しい戦いと最も豪華なドロップを持つ、最強の艦の大きなグループ向けの戦いです。シーズン11日目からは、`DS-4` の [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) から始まり、早く戻り、報酬は2倍になります（*概要*の一覧を参照）。

## ひと目で {#at-a-glance}

<!-- dormant-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **場所**：危険セクター `DS-1`, `DS-2`, `DS-3`, `DS-4`。それらの間を 飛び回る
- **数**：各ワールドに1つ
- **出現**：シーズン4日目からワイプまで（ベータとガンマ：シーズン1日目から）
- **リーダー**：Dormant Force
- **配下**：2 体の Dormant Pulse、 リーダーと 一緒に飛行
- **配下がとどまる範囲**：リーダーから700ユニット以内
- **リーダー撃破後**：Dormant Pulse がリーダーを引き継ぐ
- **リーダー撃破後**：リーダーが撃破されてから30秒後に配下は去ります。攻撃している最中でも同じです
- **移動**：1つのマップに8～15分とどまり、その後ほかの危険セクターのゲートへ飛びます。危険セクターの外へ出るゲートは使わず、ブラックホールのリングにも入りません
- **復活**：群れ全体撃破の {{guide:vitals.respawn@Dormant Force#1;Dormant Force#2;Dormant Force#3}} 後、 ランダムな 危険セクター
- **シーズン11日目から**：ランダムな危険セクターの代わりに、`DS-4` の [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) に現れ、群れ全体が撃破されてから30分後に戻り、どの艦も報酬が ×2になります（クレジット、Thulium、XP、名誉。ドロップは変わりません）
- **通知**：ワールド全体のパイロットは、群れが現れたときと撃破されたときに知らされます。これらはシステムの行です。チャットの**システム**タブに未読数付きで表示され、**全体**タブや**ローカル**タブには出ません。危険セクターのマップと銀河マップに印が付きます。キルフィードに、撃破の功績を得たパイロットの名前が出ます。

<!-- dormant-glance:end -->

## メンバー {#the-members}

- **Dormant Force**：全力の Wraith で、レーザーは典型的な装備の3倍の威力があります。群れを率い、攻撃されるまで非攻撃的で、最初に攻撃したパイロットに**直進ロケット**を撃ちます。
- **Dormant Pulse**：全力の Paragon で、同じ種類の重いレーザーを持ち、その1発ごとの威力は Force のレーザーの2倍です。専用のロケットも持ちます。Pulse は Force よりレーザーの数が少ないので、斉射全体は Force より大きいものの、2倍にはなりません（数値は下の表にあります）。Pulse は Force の近くを飛び、Force が撃破されるとそのうちの1隻がリーダーを引き継ぎます。

どれも非攻撃的で、自分からパイロットを襲うことはありません。1隻を攻撃すると、その近くにいるほかの艦が、最初に攻撃したパイロットに対して戦いに加わります。

## 戦いの流れ {#how-the-fight-goes}

- **見つけましょう。** 現れるとワールド全体に知らされ、危険セクターのマップと銀河マップに印が付きます。*ひと目で*の一覧の時間だけ1つのマップにとどまり、その後ほかの危険セクターのゲートへ飛んでジャンプします。危険セクターの外へ出るゲートは使わず、ブラックホールのリングにも入りません。最も遅い艦の速度で飛び、パイロットと同じく、攻撃を受けている間はジャンプを始めることも終えることもありません。シーズン11日目からは、まず [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) のゾーンのすぐ外に現れるので、グループは沼の砲台の届かない場所で待てます。その後 `DS-4` のゲートから飛び出していきます。
- **1人でも、少人数でも倒せません。** レベル 8 のパイロット8人が Paragon に乗り、x2 または x4 弾薬を使えば、Alpha でおよそ1分で撃破でき、失う艦は多くても1隻です。Paragon 1隻では撃破されてしまい、x2 弾薬では3隻や4隻でも同じです。Beta と Gamma の群れはより強いので（[ワールド](/wiki/05-Swarms/Swarms.md#the-worlds)）、それらのワールドではより大きなグループが必要です。
- **勝負を決めるのはレーザーです。** 合わせれば、ロケットがなくても1分足らずで Paragon を撃破でき、最良のシールドを持つ Paragon でも2分足らずです。持っている最良のシールドで、ダメージを素早く与えましょう。
- **1隻ずつ。** 各艦に独自の船体と独自の報酬があるので、Force と Pulse のどちらが先に撃破されることもあります。群れが入れ替わるのは、全体が撃破されたときだけで、*ひと目で*の一覧の時間がたってからです。

## リーダーの3つの段階 {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

その戦いには三つの段階があります([しくみ](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps))。それぞれ一度だけ起こります。

- **開始時**: Dormant Pulsesのうち一体でも生きている間、あらゆる攻撃の70%しか受けません。
- **三分の二を切ると**: Dormant Pulsesが15秒の間、2.5秒ごとにロケットを撃ちます。
- **三分の一を切ると**: Dormant Pulsesがすべて生きている間、6秒の間、毎秒、船体の5%ずつ回復させます。

<!-- mob-ladder:end -->

## 報酬とドロップ {#rewards-and-drops}

各艦は、受けたダメージに応じて個別に報酬を払い（[ボス撃破の報酬](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)）、それぞれがいちばんダメージを与えたパイロットのためにコンテナをドロップします。**Force のコンテナ**が賞品で、大量の x3 と x4 弾薬、1種類のエピックロケット、そして時々 N.I.K.E. か N.U.K.E. が入っています。**Pulse** は Ancient Control Unit、Power Core、Dark Matter をドロップすることがあります。この群れと戦う1分は、最も報酬の高いエイリアンである Crystalys と戦う1分より多く報酬を払います。シーズン11日目からは、どの艦も報酬が2倍になります（*概要*の一覧を参照）。コンテナは変わりません。

## 数値 {#the-numbers}

群れの艦の3つのワールドでの数値です（[ワールド](/wiki/05-Swarms/Swarms.md#the-worlds)）。表のクレジット、Thulium、XP、名誉は、シーズン11日目より前の報酬です。その日からは、撃破の報酬が2倍になります。

<!-- dormant-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Dormant Force

土台は Wraith で、船体はその100%、レーザーのダメージはその300%です。速度と射程は土台の艦のものです。5秒ごとに直進ロケットを1発撃ちます：[Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets)。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@Dormant Force#1}} | {{guide:vitals.hull@Dormant Force#2}} | {{guide:vitals.hull@Dormant Force#3}} |
| シールド | {{guide:vitals.shield@Dormant Force#1}} | {{guide:vitals.shield@Dormant Force#2}} | {{guide:vitals.shield@Dormant Force#3}} |
| レーザーのダメージ （毎秒1斉射） | {{guide:vitals.dps@Dormant Force#1}} | {{guide:vitals.dps@Dormant Force#2}} | {{guide:vitals.dps@Dormant Force#3}} |
| 速度 | {{guide:vitals.speed@Dormant Force#1}} | {{guide:vitals.speed@Dormant Force#2}} | {{guide:vitals.speed@Dormant Force#3}} |
| レーザーの射程 | 800 | 800 | 800 |
| 索敵範囲 | 攻撃時のみ | 攻撃時のみ | 攻撃時のみ |
| ロケットのダメージ （最大） | {{guide:behaviour.ability:rocket.damage@Dormant Force#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#3}} |
| クレジット | {{guide:spoils.pay.credits@Dormant Force#1}} | {{guide:spoils.pay.credits@Dormant Force#2}} | {{guide:spoils.pay.credits@Dormant Force#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Force#1}} | {{guide:spoils.pay.thulium@Dormant Force#2}} | {{guide:spoils.pay.thulium@Dormant Force#3}} |
| 経験値（XP） | {{guide:spoils.pay.experience@Dormant Force#1}} | {{guide:spoils.pay.experience@Dormant Force#2}} | {{guide:spoils.pay.experience@Dormant Force#3}} |
| 名誉 | {{guide:spoils.pay.honor@Dormant Force#1}} | {{guide:spoils.pay.honor@Dormant Force#2}} | {{guide:spoils.pay.honor@Dormant Force#3}} |
| 撃破1回あたりの PvE ポイント | 25 | 25 | 25 |

**ドロップ**：最もダメージを与えたパイロットのためのコンテナ1つ。

| アイテム |
| :--- |
| {{guide:spoils.box@Dormant Force#1;Dormant Force#2;Dormant Force#3}} |

### Dormant Pulse

土台は Paragon で、船体はその100%、レーザーのダメージはその600%です。速度と射程は土台の艦のものです。5秒ごとに直進ロケットを1発撃ちます：[Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets)。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@Dormant Pulse#1}} | {{guide:vitals.hull@Dormant Pulse#2}} | {{guide:vitals.hull@Dormant Pulse#3}} |
| シールド | {{guide:vitals.shield@Dormant Pulse#1}} | {{guide:vitals.shield@Dormant Pulse#2}} | {{guide:vitals.shield@Dormant Pulse#3}} |
| レーザーのダメージ （毎秒1斉射） | {{guide:vitals.dps@Dormant Pulse#1}} | {{guide:vitals.dps@Dormant Pulse#2}} | {{guide:vitals.dps@Dormant Pulse#3}} |
| 速度 | {{guide:vitals.speed@Dormant Pulse#1}} | {{guide:vitals.speed@Dormant Pulse#2}} | {{guide:vitals.speed@Dormant Pulse#3}} |
| レーザーの射程 | 800 | 800 | 800 |
| 索敵範囲 | 攻撃時のみ | 攻撃時のみ | 攻撃時のみ |
| ロケットのダメージ （最大） | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#3}} |
| クレジット | {{guide:spoils.pay.credits@Dormant Pulse#1}} | {{guide:spoils.pay.credits@Dormant Pulse#2}} | {{guide:spoils.pay.credits@Dormant Pulse#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Pulse#1}} | {{guide:spoils.pay.thulium@Dormant Pulse#2}} | {{guide:spoils.pay.thulium@Dormant Pulse#3}} |
| 経験値（XP） | {{guide:spoils.pay.experience@Dormant Pulse#1}} | {{guide:spoils.pay.experience@Dormant Pulse#2}} | {{guide:spoils.pay.experience@Dormant Pulse#3}} |
| 名誉 | {{guide:spoils.pay.honor@Dormant Pulse#1}} | {{guide:spoils.pay.honor@Dormant Pulse#2}} | {{guide:spoils.pay.honor@Dormant Pulse#3}} |
| 撃破1回あたりの PvE ポイント | 11 | 11 | 11 |

**ドロップ**：最もダメージを与えたパイロットのためのコンテナ1つ。

| アイテム |
| :--- |
| {{guide:spoils.box@Dormant Pulse#1;Dormant Pulse#2;Dormant Pulse#3}} |

<!-- dormant-members:end -->
