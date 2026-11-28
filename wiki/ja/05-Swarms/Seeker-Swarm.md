<!-- wiki-i18n source: 7c6bc3eaf70223f5 -->
<!-- wiki-i18n title: Seeker の群れ -->
# Seeker の群れ {#seeker-swarm}

Seeker の群れは[群れ](/wiki/05-Swarms/Swarms.md)の中で最も小さく、**Boss Seeker** と、それを守って回復する **Seeker Slave** からなります。新人パイロットが飛び始めるセクターにいるので、多くのパイロットが最初に出会う群れです。Boss Seeker は自分から戦いを始めることはありませんが、攻撃すると、土台になった[Seeker](/wiki/04-Aliens/Seeker.md)よりはるかに危険です。

## ひと目で {#at-a-glance}

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **場所**：各企業の `x-1` と `x-2` セクター
- **数**：各セクターに 1つ （各ワールドに 計6つ）
- **出現**：シーズン4日目からワイプまで（ベータとガンマ：シーズン1日目から）
- **リーダー**：Boss Seeker
- **配下**：最大 4 体の Seeker Slave、 10秒 ごとに 新しく1体
- **配下がとどまる範囲**：リーダーから500ユニット以内
- **回復**：リーダーから600ユニット以内にいる Seeker Slave は1体ごとにリーダーの船体を回復します（Alpha では毎秒 50 HP）
- **リーダー撃破後**：リーダーが撃破されてから30秒後に配下は去ります。ただし攻撃している間は残ります
- **復活**：リーダー撃破の {{guide:vitals.respawn@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} 後、 同じセクター
- **通知**：そのセクターのパイロットは、リーダーが現れたときと撃破されたときに知らされます。これらはシステムの行です。チャットの**システム**タブに未読数付きで表示され、**全体**タブや**ローカル**タブには出ません。キルフィードに、撃破の功績を得たパイロットの名前が出ます。

<!-- seeker-glance:end -->

## メンバー {#the-members}

- **Boss Seeker**：群れの色合いを帯び、頭上に名前が表示される、ずっと大きな Seeker で、船体、シールド、ダメージが Seeker の何倍もあります（数値は下にあります）。非攻撃的で、パイロットに攻撃されるまでうろつき、攻撃されるとその場に止まってそのパイロットに発砲し、近くにいる群れの艦が戦いに加わります。武器の射程と速度は Seeker と同じで、自分で船体を修復することはありません。その[3つの段階](#the-leaders-three-steps)と[特殊能力](/wiki/03-Mechanics/Special-Abilities.md)は、これを変えることがあります。
- **Seeker Slave**：群れの色合いを帯びた普通の Seeker です。Slave はボスのそばにとどまり、近くの群れの艦が攻撃されると戦いに加わり、ボスの近くにいる Slave は1体ごとにボスの船体を回復します。Slave は Seeker と同じように、しばらく休むと自分の船体を修復します。

## 戦いの流れ {#how-the-fight-goes}

- **自分の艦が耐えられるようになるまで放っておきましょう。** Boss Seeker は、パイロットの最初の艦では耐えきれないほど強く攻撃します。シールドのない新人パイロットの Protos は、ボスと Slave に取りつかれると数秒で撃破されます。
- **射程の外にいましょう。** ボスと Slave は Protos より遅く、武器の射程も Quantum Laser II より短いので（[レーザーと弾薬](/wiki/06-Items/Lasers.md)を参照）、そうしたレーザーを持ち、その射程の外にいるパイロットは、攻撃されてもダメージを受けません。Quantum Laser I のパイロットは射程の外にとどまれません。
- **Slave の回復は、新人パイロット1人の攻撃より速いです。** 全員合わせると、x1 弾薬のパイロット1人のレーザーが与えるダメージ以上を回復するので、仲間と x2 弾薬を用意しましょう。Quantum Laser II を持つ2人のパイロットが距離を保てば、Alpha ではおよそ1分でボスを倒せ、x2 弾薬ならずっと速くなります。
- **ボスは戻ってきます。** *ひと目で*の一覧の時間がたつと、同じセクターに全快の状態で現れ、Slave は1体ずつ順に現れます。

## リーダーの3つの段階 {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

その戦いには三つの段階があります([しくみ](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps))。それぞれ一度だけ起こります。

- **開始時**: Seeker Slavesが8秒の間、×2の速さで回復させます。
- **三分の二を切ると**: 2の分身が現れ、本物にはリングが付きます。
- **三分の一を切ると**: 4秒の間パイロットから逃げ、その後向き直ります。

<!-- mob-ladder:end -->

## 報酬とドロップ {#rewards-and-drops}

Boss Seeker の報酬は**ちょうど Seeker 10体分**です。Seeker のクレジット、Thulium、経験値、名誉の10倍が、戦ったパイロットの間でダメージに応じて分けられます（[ボス撃破の報酬](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)）。そのコンテナには Seeker 10体分のドロップに加えて、エピック未満の弾薬とロケットが入っていて、最もダメージを与えたパイロットのものになります。Slave の報酬は少額でドロップもありません。ボスとともに戻ってくるので、倒しても稼ぎにはなりません。

## 数値 {#the-numbers}

群れの艦の3つのワールドでの数値です（[ワールド](/wiki/05-Swarms/Swarms.md#the-worlds)）。

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker

土台は Seeker で、船体、シールド、ダメージはその400%です。速度と射程は土台の艦のものです。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@Boss Seeker#1}} | {{guide:vitals.hull@Boss Seeker#2}} | {{guide:vitals.hull@Boss Seeker#3}} |
| シールド | {{guide:vitals.shield@Boss Seeker#1}} | {{guide:vitals.shield@Boss Seeker#2}} | {{guide:vitals.shield@Boss Seeker#3}} |
| レーザーのダメージ （毎秒1斉射） | {{guide:vitals.dps@Boss Seeker#1}} | {{guide:vitals.dps@Boss Seeker#2}} | {{guide:vitals.dps@Boss Seeker#3}} |
| 速度 | {{guide:vitals.speed@Boss Seeker#1}} | {{guide:vitals.speed@Boss Seeker#2}} | {{guide:vitals.speed@Boss Seeker#3}} |
| レーザーの射程 | 600 | 600 | 600 |
| 索敵範囲 | 攻撃時のみ | 攻撃時のみ | 攻撃時のみ |
| クレジット | {{guide:spoils.pay.credits@Boss Seeker#1}} | {{guide:spoils.pay.credits@Boss Seeker#2}} | {{guide:spoils.pay.credits@Boss Seeker#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Seeker#1}} | {{guide:spoils.pay.thulium@Boss Seeker#2}} | {{guide:spoils.pay.thulium@Boss Seeker#3}} |
| 経験値（XP） | {{guide:spoils.pay.experience@Boss Seeker#1}} | {{guide:spoils.pay.experience@Boss Seeker#2}} | {{guide:spoils.pay.experience@Boss Seeker#3}} |
| 名誉 | {{guide:spoils.pay.honor@Boss Seeker#1}} | {{guide:spoils.pay.honor@Boss Seeker#2}} | {{guide:spoils.pay.honor@Boss Seeker#3}} |
| 撃破1回あたりの PvE ポイント | 5 | 5 | 5 |

**ドロップ**：最もダメージを与えたパイロットのためのコンテナ1つ。

| アイテム |
| :--- |
| {{guide:spoils.box@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} |

### Seeker Slave

土台は Seeker で、船体、シールド、ダメージはその100%です。速度と射程は土台の艦のものです。

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 船体 | {{guide:vitals.hull@Seeker Slave#1}} | {{guide:vitals.hull@Seeker Slave#2}} | {{guide:vitals.hull@Seeker Slave#3}} |
| シールド | {{guide:vitals.shield@Seeker Slave#1}} | {{guide:vitals.shield@Seeker Slave#2}} | {{guide:vitals.shield@Seeker Slave#3}} |
| レーザーのダメージ （毎秒1斉射） | {{guide:vitals.dps@Seeker Slave#1}} | {{guide:vitals.dps@Seeker Slave#2}} | {{guide:vitals.dps@Seeker Slave#3}} |
| 速度 | {{guide:vitals.speed@Seeker Slave#1}} | {{guide:vitals.speed@Seeker Slave#2}} | {{guide:vitals.speed@Seeker Slave#3}} |
| レーザーの射程 | 600 | 600 | 600 |
| 索敵範囲 | 攻撃時のみ | 攻撃時のみ | 攻撃時のみ |
| リーダーを回復 （1体ごとに毎秒、 船体のみ） | 50 | 75 | 100 |
| クレジット | {{guide:spoils.pay.credits@Seeker Slave#1}} | {{guide:spoils.pay.credits@Seeker Slave#2}} | {{guide:spoils.pay.credits@Seeker Slave#3}} |
| Thulium | {{guide:spoils.pay.thulium@Seeker Slave#1}} | {{guide:spoils.pay.thulium@Seeker Slave#2}} | {{guide:spoils.pay.thulium@Seeker Slave#3}} |
| 経験値（XP） | {{guide:spoils.pay.experience@Seeker Slave#1}} | {{guide:spoils.pay.experience@Seeker Slave#2}} | {{guide:spoils.pay.experience@Seeker Slave#3}} |
| 名誉 | {{guide:spoils.pay.honor@Seeker Slave#1}} | {{guide:spoils.pay.honor@Seeker Slave#2}} | {{guide:spoils.pay.honor@Seeker Slave#3}} |
| 撃破1回あたりの PvE ポイント | 1 | 1 | 1 |

**ドロップ**：なし。撃破で支払われるのはクレジット、Thulium、経験値、名誉だけです。

<!-- seeker-members:end -->
