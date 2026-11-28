<!-- wiki-i18n source: 2b3edf7bcb1d9673 -->
<!-- wiki-i18n title: Crystalys の群れ -->
# Crystalys の群れ {#crystalys-swarm}

Crystalys の群れは、**Boss Crystalys** とその **Crystalys Guard** からなります。最も頑丈なエイリアンである[Crystalys](/wiki/04-Aliens/Crystalys.md)をさらに大きくしたもので、そのそばにとどまってそれを回復する護衛がつきます。[危険セクター](/wiki/01-General/Danger-Sectors.md)の `DS-1`、`DS-2`、`DS-3` に1体ずつおり、自分のセクターから出ることはありません。危険セクターは PvP セクターなので、戦いは最強のパイロットたちの大きなグループ向けで、そこで危険なのはボスだけではありません。

## ひと目で {#at-a-glance}

<!-- crystalys-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **場所**：危険セクター `DS-1`, `DS-2`, `DS-3`
- **数**：各セクターに 1つ （各ワールドに 計3つ）
- **出現**：シーズン4日目からワイプまで（ベータとガンマ：シーズン1日目から）
- **リーダー**：Boss Crystalys
- **配下**：最大 3 体の Crystalys Guard、 10秒 ごとに 新しく1体
- **配下がとどまる範囲**：リーダーから500ユニット以内
- **回復**：リーダーから600ユニット以内にいる Crystalys Guard は1体ごとにリーダーの船体を回復します（Alpha では毎秒 250 HP）
- **リーダー撃破後**：リーダーが撃破されてから30秒後に配下は去ります。ただし攻撃している間は残ります
- **復活**：リーダー撃破の {{guide:vitals.respawn@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} 後、 同じセクター
- **通知**：そのセクターのパイロットは、リーダーが現れたときと撃破されたときに知らされます。これらはシステムの行です。チャットの**システム**タブに未読数付きで表示され、**全体**タブや**ローカル**タブには出ません。キルフィードに、撃破の功績を得たパイロットの名前が出ます。

<!-- crystalys-glance:end -->

## メンバー {#the-members}

- **Boss Crystalys**: 群れの色合いを帯び、頭上に名前が表示される、より大きな Crystalys で、独自の船体、シールド、レーザーの一斉射撃を持ちます（数値は下にあります）。非攻撃的で、パイロットに攻撃されるまでうろつき、攻撃されるとそのパイロットを追って発砲し、近くにいる群れの艦が戦いに加わります。武器の射程と速度は Crystalys と同じで、自分で船体を修復することはありません。その[3つの段階](#the-leaders-three-steps)と[特殊能力](/wiki/03-Mechanics/Special-Abilities.md)は、これを変えることがあります。
- **Crystalys Guard**: 群れの色合いを帯びた、より小さな Crystalys です。Guard はボスのそばにとどまり、近くの群れの艦が攻撃されると戦いに加わり、ボスの近くにいる Guard は1体ごとにボスの船体を回復します。Guard は Crystalys と同じように、しばらく休むと自分の船体を修復します。

## 戦いの流れ {#how-the-fight-goes}

- **大きなグループで来ましょう。** Alpha では、x2 弾薬を持ち Paragon に乗ったレベル8のパイロットが、敵の攻撃が分散するなら6人、1人に集中するなら9人で足ります。x4 弾薬なら5人と6人です。人数が多いほど戦いは早く終わり、失う艦も減ります。パイロット1人では撃破されます。
- **狙うのはボスで、Guard ではありません。** Guard は数秒で倒れますが、*ひと目で*の一覧にある間隔で新しいものが現れ、Guard が回復する量はグループが与えるダメージのごく一部です。放っておいても少し時間がかかるだけで、追いかけるともっとかかります。
- **Beta と Gamma はもっと手強いです。** これらのワールドの群れは強いので（[ワールド](/wiki/05-Swarms/Swarms.md#the-worlds)）、より多くのパイロットか、より良い弾薬が必要です。
- **危険セクターは PvP です。** ライバルが戦いの最中にグループを攻撃し、コンテナを待ち構えることがあります。コンテナは30秒間は最もダメージを与えたパイロット（とそのクラン）のもので、その後は誰でも取れます（[積荷](/wiki/03-Mechanics/Cargo.md)）。仲間と一緒に行きましょう。
- **ボスは戻ってきます。** *ひと目で*の一覧の時間がたつと、同じセクターに全快の状態で現れ、Guard は1体ずつ順に現れます。

## リーダーの3つの段階 {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

その戦いには三つの段階があります([しくみ](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps))。それぞれ一度だけ起こります。

- **開始時**: 8秒の間、あらゆる攻撃の50%しか受けません。
- **三分の二を切ると**: 半径700ユニットのリングが、中にいるすべての艦をその一斉射撃の4で攻撃し、さらに4発のロケットを撃ちます。
- **三分の一を切ると**: 船体とシールドの20%を回復し(ダメージのバーストで中断されます)、Crystalys Guardsがさらに3体来ます。生存は最大6体まで。

<!-- mob-ladder:end -->

## 報酬とドロップ {#rewards-and-drops}

Boss Crystalys の報酬は、その戦いの重さに見合っています。1分戦うと、最も報酬の高いエイリアンである Crystalys と1分戦うより多く支払われます。報酬は、戦ったパイロットの間でダメージに応じて分けられます（[ボス撃破の報酬](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)）。コンテナには Cataclysite と Quorvium、ときどき Power Core、Ancient Control Unit、Dark Matter、x3 と x4 の弾薬、エピックのロケットが入っていて、最もダメージを与えたパイロットのものになります。Guard の報酬は少額でドロップもありません。ボスとともに戻ってくるので、倒しても稼ぎにはなりません。

## 数値 {#the-numbers}

群れの艦の3つのワールドでの数値です（[ワールド](/wiki/05-Swarms/Swarms.md#the-worlds)）。

<!-- crystalys-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Crystalys

土台は Crystalys で、船体はその350%、レーザーのダメージはその100%です。速度と射程は土台の艦のものです。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@Boss Crystalys#1}} | {{guide:vitals.hull@Boss Crystalys#2}} | {{guide:vitals.hull@Boss Crystalys#3}} |
| シールド | {{guide:vitals.shield@Boss Crystalys#1}} | {{guide:vitals.shield@Boss Crystalys#2}} | {{guide:vitals.shield@Boss Crystalys#3}} |
| レーザーのダメージ （毎秒1斉射） | {{guide:vitals.dps@Boss Crystalys#1}} | {{guide:vitals.dps@Boss Crystalys#2}} | {{guide:vitals.dps@Boss Crystalys#3}} |
| 速度 | {{guide:vitals.speed@Boss Crystalys#1}} | {{guide:vitals.speed@Boss Crystalys#2}} | {{guide:vitals.speed@Boss Crystalys#3}} |
| レーザーの射程 | 900 | 900 | 900 |
| 索敵範囲 | 攻撃時のみ | 攻撃時のみ | 攻撃時のみ |
| クレジット | {{guide:spoils.pay.credits@Boss Crystalys#1}} | {{guide:spoils.pay.credits@Boss Crystalys#2}} | {{guide:spoils.pay.credits@Boss Crystalys#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Crystalys#1}} | {{guide:spoils.pay.thulium@Boss Crystalys#2}} | {{guide:spoils.pay.thulium@Boss Crystalys#3}} |
| 経験値（XP） | {{guide:spoils.pay.experience@Boss Crystalys#1}} | {{guide:spoils.pay.experience@Boss Crystalys#2}} | {{guide:spoils.pay.experience@Boss Crystalys#3}} |
| 名誉 | {{guide:spoils.pay.honor@Boss Crystalys#1}} | {{guide:spoils.pay.honor@Boss Crystalys#2}} | {{guide:spoils.pay.honor@Boss Crystalys#3}} |
| 撃破1回あたりの PvE ポイント | 30 | 30 | 30 |

**ドロップ**：最もダメージを与えたパイロットのためのコンテナ1つ。

| アイテム |
| :--- |
| {{guide:spoils.box@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} |

### Crystalys Guard

土台は Crystalys で、船体、シールド、ダメージはその15%です。速度と射程は土台の艦のものです。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@Crystalys Guard#1}} | {{guide:vitals.hull@Crystalys Guard#2}} | {{guide:vitals.hull@Crystalys Guard#3}} |
| シールド | {{guide:vitals.shield@Crystalys Guard#1}} | {{guide:vitals.shield@Crystalys Guard#2}} | {{guide:vitals.shield@Crystalys Guard#3}} |
| レーザーのダメージ （毎秒1斉射） | {{guide:vitals.dps@Crystalys Guard#1}} | {{guide:vitals.dps@Crystalys Guard#2}} | {{guide:vitals.dps@Crystalys Guard#3}} |
| 速度 | {{guide:vitals.speed@Crystalys Guard#1}} | {{guide:vitals.speed@Crystalys Guard#2}} | {{guide:vitals.speed@Crystalys Guard#3}} |
| レーザーの射程 | 900 | 900 | 900 |
| 索敵範囲 | 攻撃時のみ | 攻撃時のみ | 攻撃時のみ |
| リーダーを回復 （1体ごとに毎秒、 船体のみ） | 250 | 375 | 500 |
| クレジット | {{guide:spoils.pay.credits@Crystalys Guard#1}} | {{guide:spoils.pay.credits@Crystalys Guard#2}} | {{guide:spoils.pay.credits@Crystalys Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Crystalys Guard#1}} | {{guide:spoils.pay.thulium@Crystalys Guard#2}} | {{guide:spoils.pay.thulium@Crystalys Guard#3}} |
| 経験値（XP） | {{guide:spoils.pay.experience@Crystalys Guard#1}} | {{guide:spoils.pay.experience@Crystalys Guard#2}} | {{guide:spoils.pay.experience@Crystalys Guard#3}} |
| 名誉 | {{guide:spoils.pay.honor@Crystalys Guard#1}} | {{guide:spoils.pay.honor@Crystalys Guard#2}} | {{guide:spoils.pay.honor@Crystalys Guard#3}} |
| 撃破1回あたりの PvE ポイント | 6 | 6 | 6 |

**ドロップ**：なし。撃破で支払われるのはクレジット、Thulium、経験値、名誉だけです。

<!-- crystalys-members:end -->
