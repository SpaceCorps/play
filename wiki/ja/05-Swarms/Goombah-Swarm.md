<!-- wiki-i18n source: 38ffa8ba7cbf5000 -->
<!-- wiki-i18n title: Goombah の群れ -->
# Goombah の群れ {#goombah-swarm}

Goombah の群れは、**Boss Goombah** とその **Goombah Guard** からなります。自分から戦いを始めることのない巨大な[Goombah](/wiki/04-Aliens/Goombah.md)と、そのそばにとどまってそれを回復する小型の個体です。[Phantasm の群れ](/wiki/05-Swarms/Phantasm-Swarm.md)と同じセクター `x-3` と `x-4` にいて、企業セクターで最強のパイロットたちのグループ向けの戦いです。

## ひと目で {#at-a-glance}

<!-- goombah-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **場所**：各企業の `x-3` と `x-4` セクター
- **数**：各セクターに 1つ （各ワールドに 計6つ）
- **出現**：シーズン4日目からワイプまで（ベータとガンマ：シーズン1日目から）
- **リーダー**：Boss Goombah
- **配下**：最大 4 体の Goombah Guard、 10秒 ごとに 新しく1体
- **配下がとどまる範囲**：リーダーから500ユニット以内
- **回復**：リーダーから600ユニット以内にいる Goombah Guard は1体ごとにリーダーの船体を回復します（Alpha では毎秒 110 HP）
- **リーダー撃破後**：リーダーが撃破されてから30秒後に配下は去ります。ただし攻撃している間は残ります
- **復活**：リーダー撃破の {{guide:vitals.respawn@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} 後、 同じセクター
- **通知**：そのセクターのパイロットは、リーダーが現れたときと撃破されたときに知らされます。これらはシステムの行です。チャットの**システム**タブに未読数付きで表示され、**全体**タブや**ローカル**タブには出ません。キルフィードに、撃破の功績を得たパイロットの名前が出ます。

<!-- goombah-glance:end -->

## メンバー {#the-members}

- **Boss Goombah**: 群れの色合いを帯び、頭上に名前が表示される、より大きな Goombah で、独自の船体、シールド、レーザーの一斉射撃を持ちます（数値は下にあります）。非攻撃的で、パイロットに攻撃されるまでうろつき、攻撃されるとそのパイロットを追って発砲し、近くにいる群れの艦が戦いに加わります。武器の射程と速度は Goombah と同じで、自分で船体を修復することはありません。その[3つの段階](#the-leaders-three-steps)と[特殊能力](/wiki/03-Mechanics/Special-Abilities.md)は、これを変えることがあります。
- **Goombah Guard**: 群れの色合いを帯びた、より小さな Goombah です。Guard はボスのそばにとどまり、近くの群れの艦が攻撃されると戦いに加わり、ボスの近くにいる Guard は1体ごとにボスの船体を回復します。Guard は Goombah と同じように、しばらく休むと自分の船体を修復します。

## 戦いの流れ {#how-the-fight-goes}

- **最強の艦のグループで来ましょう。** x2 弾薬を持つレベル8のパイロット3人なら、Alpha ではおよそ75秒で倒せ、失う艦は多くても1隻です。うち2人は x4 弾薬が必要で、低いレベルのパイロットでは与えるダメージが足りず勝てません。
- **狙うのはボスで、Guard ではありません。** Guard は数秒で倒れますが、*ひと目で*の一覧にある間隔で新しいものが現れ、Guard が回復する量はグループが与えるダメージのごく一部です。放っておいても少し時間がかかるだけで、追いかけるともっとかかります。
- **Beta と Gamma はもっと手強いです。** これらのワールドの群れは強いので（[ワールド](/wiki/05-Swarms/Swarms.md#the-worlds)）、より多くのパイロットか、より良い弾薬が必要です。
- **セクターに気をつけましょう。** `x-4` は Alpha では PvP セクターで、Beta と Gamma では `x-3` と `x-4` がそうです（[ワールド](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)）。ライバルが戦いに加わったり、コンテナを待ち構えたりすることがあります。グループの1隻を見張りに残しましょう。
- **ボスは戻ってきます。** *ひと目で*の一覧の時間がたつと、同じセクターに全快の状態で現れ、Guard は1体ずつ順に現れます。

## リーダーの3つの段階 {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

その戦いには三つの段階があります([しくみ](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps))。それぞれ一度だけ起こります。

- **開始時**: 6秒の間、あらゆる攻撃の50%しか受けません。
- **三分の二を切ると**: 10秒の間、ダメージは×1.5、速度は×1.25になります。
- **三分の一を切ると**: 船体とシールドの25%を回復します(ダメージのバーストで中断されます)。その間、Goombah Guardsが×2の速さで回復させます。

<!-- mob-ladder:end -->

## 報酬とドロップ {#rewards-and-drops}

Boss Goombah の報酬は、その戦いの重さに見合っています。1分戦うと、このセクターで最も報酬の高いエイリアンである Goombah と1分戦うより多く支払われます。報酬は、戦ったパイロットの間でダメージに応じて分けられます（[ボス撃破の報酬](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)）。コンテナには Goombah のドロップが数倍になって（Cataclysite、Quorvium、Power Core、Reinforced Hull Plate、Ship Fragment）、弾薬とロケットとともに入っていて、最もダメージを与えたパイロットのものになります。Guard の報酬は少額でドロップもありません。ボスとともに戻ってくるので、倒しても稼ぎにはなりません。

## 数値 {#the-numbers}

群れの艦の3つのワールドでの数値です（[ワールド](/wiki/05-Swarms/Swarms.md#the-worlds)）。

<!-- goombah-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Goombah

土台は Goombah で、船体はその400%、レーザーのダメージはその100%です。速度と射程は土台の艦のものです。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@Boss Goombah#1}} | {{guide:vitals.hull@Boss Goombah#2}} | {{guide:vitals.hull@Boss Goombah#3}} |
| シールド | {{guide:vitals.shield@Boss Goombah#1}} | {{guide:vitals.shield@Boss Goombah#2}} | {{guide:vitals.shield@Boss Goombah#3}} |
| レーザーのダメージ （毎秒1斉射） | {{guide:vitals.dps@Boss Goombah#1}} | {{guide:vitals.dps@Boss Goombah#2}} | {{guide:vitals.dps@Boss Goombah#3}} |
| 速度 | {{guide:vitals.speed@Boss Goombah#1}} | {{guide:vitals.speed@Boss Goombah#2}} | {{guide:vitals.speed@Boss Goombah#3}} |
| レーザーの射程 | 800 | 800 | 800 |
| 索敵範囲 | 攻撃時のみ | 攻撃時のみ | 攻撃時のみ |
| クレジット | {{guide:spoils.pay.credits@Boss Goombah#1}} | {{guide:spoils.pay.credits@Boss Goombah#2}} | {{guide:spoils.pay.credits@Boss Goombah#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Goombah#1}} | {{guide:spoils.pay.thulium@Boss Goombah#2}} | {{guide:spoils.pay.thulium@Boss Goombah#3}} |
| 経験値（XP） | {{guide:spoils.pay.experience@Boss Goombah#1}} | {{guide:spoils.pay.experience@Boss Goombah#2}} | {{guide:spoils.pay.experience@Boss Goombah#3}} |
| 名誉 | {{guide:spoils.pay.honor@Boss Goombah#1}} | {{guide:spoils.pay.honor@Boss Goombah#2}} | {{guide:spoils.pay.honor@Boss Goombah#3}} |
| 撃破1回あたりの PvE ポイント | 14 | 14 | 14 |

**ドロップ**：最もダメージを与えたパイロットのためのコンテナ1つ。

| アイテム |
| :--- |
| {{guide:spoils.box@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} |

### Goombah Guard

土台は Goombah で、船体、シールド、ダメージはその20%です。速度と射程は土台の艦のものです。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@Goombah Guard#1}} | {{guide:vitals.hull@Goombah Guard#2}} | {{guide:vitals.hull@Goombah Guard#3}} |
| シールド | {{guide:vitals.shield@Goombah Guard#1}} | {{guide:vitals.shield@Goombah Guard#2}} | {{guide:vitals.shield@Goombah Guard#3}} |
| レーザーのダメージ （毎秒1斉射） | {{guide:vitals.dps@Goombah Guard#1}} | {{guide:vitals.dps@Goombah Guard#2}} | {{guide:vitals.dps@Goombah Guard#3}} |
| 速度 | {{guide:vitals.speed@Goombah Guard#1}} | {{guide:vitals.speed@Goombah Guard#2}} | {{guide:vitals.speed@Goombah Guard#3}} |
| レーザーの射程 | 800 | 800 | 800 |
| 索敵範囲 | 攻撃時のみ | 攻撃時のみ | 攻撃時のみ |
| リーダーを回復 （1体ごとに毎秒、 船体のみ） | 110 | 165 | 220 |
| クレジット | {{guide:spoils.pay.credits@Goombah Guard#1}} | {{guide:spoils.pay.credits@Goombah Guard#2}} | {{guide:spoils.pay.credits@Goombah Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Goombah Guard#1}} | {{guide:spoils.pay.thulium@Goombah Guard#2}} | {{guide:spoils.pay.thulium@Goombah Guard#3}} |
| 経験値（XP） | {{guide:spoils.pay.experience@Goombah Guard#1}} | {{guide:spoils.pay.experience@Goombah Guard#2}} | {{guide:spoils.pay.experience@Goombah Guard#3}} |
| 名誉 | {{guide:spoils.pay.honor@Goombah Guard#1}} | {{guide:spoils.pay.honor@Goombah Guard#2}} | {{guide:spoils.pay.honor@Goombah Guard#3}} |
| 撃破1回あたりの PvE ポイント | 3 | 3 | 3 |

**ドロップ**：なし。撃破で支払われるのはクレジット、Thulium、経験値、名誉だけです。

<!-- goombah-members:end -->
