<!-- wiki-i18n source: bbd76eb145ce6188 -->
<!-- wiki-i18n title: 群れ -->
# 群れ {#swarms}

**群れ**とは、**リーダー**のもとで銀河の一部をうろつくエイリアンの集団です。リーダーは周囲のどのエイリアンよりはるかに強いボスで、**配下**がそれを守り、2つの群れでは回復もします。群れは3つあり、それぞれに専用の記事があります。

- [Seeker の群れ](/wiki/05-Swarms/Seeker-Swarm.md)：Boss Seeker とその Seeker Slave。最も小さな群れで、新人パイロットが飛ぶセクターにいます。
- [Pirate の群れ](/wiki/05-Swarms/Pirate-Swarm.md)：Pirate Boss とその Pirate Scout。グループ向けの長い戦いです。
- [Dormant の群れ](/wiki/05-Swarms/Dormant-Swarm.md)：Dormant Force とその Dormant Pulse。最強の群れで、ドロップも最も豪華です。

群れの艦は**それぞれ独立した種類のエイリアン**です。独自の名前と独自の撃破数を持ち、Seeker や Phantasm、その他のエイリアンとしては数えられません。群れの艦は、土台になった艦の形をしていて、独自の色合いを帯び、頭上に名前が表示されます。Boss Seeker はずっと大きな Seeker です。

## 3つの群れ {#the-three-swarms}

<!-- swarms-list:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| 群れ | 場所 | 数 | リーダー | 配下 | 復活 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**Pirate の群れ**](/wiki/05-Swarms/Pirate-Swarm.md) | 各企業の `x-2` と `x-3` セクター | 各セクターに 1つ （各ワールドに 計6つ） | **Pirate Boss** | 最大 5 体の Pirate Scout、 10秒 ごとに 新しく1体 | リーダー撃破の 2分 後、 同じセクター |
| [**Dormant の群れ**](/wiki/05-Swarms/Dormant-Swarm.md) | 危険セクター `DS-1`, `DS-2`, `DS-3`, `DS-4`。それらの間を 飛び回る | 各ワールドに1つ | **Dormant Force** | 2 体の Dormant Pulse、 リーダーと 一緒に飛行 | 群れ全体撃破の 1時間 後、 ランダムな 危険セクター |
| [**Seeker の群れ**](/wiki/05-Swarms/Seeker-Swarm.md) | 各企業の `x-1` と `x-2` セクター | 各セクターに 1つ （各ワールドに 計6つ） | **Boss Seeker** | 最大 4 体の Seeker Slave、 10秒 ごとに 新しく1体 | リーダー撃破の 2分 後、 同じセクター |

<!-- swarms-list:end -->

## いつ、どこに {#when-and-where}

群れは**ファーストコンタクト**から現れ始め、ワイプまで残ります（[ワイプのタイムライン](/wiki/03-Mechanics/Wipe-Timeline.md)を参照。日付は下のルールの最初の行にあります）。**各ワールドにそれぞれの群れがいて**、場所は同じです。そのため Alpha の Pirate Boss と Beta の Pirate Boss は別々の艦で、自分のワールドで倒した群れがほかのワールドで倒されたことにはなりません。倒された群れは、上の表の時間がたつと戻ってきます。

## すべての群れのルール {#the-rules-of-every-swarm}

<!-- swarms-rules:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- 群れはシーズン4日目からワイプまで現れます。
- 群れの艦が攻撃されると、その艦から1,500ユニット以内にいる同じ群れの艦が、最初に攻撃したパイロットに対して戦いに加わります。
- リーダーは、すべてのステーションとゲートのリングの縁から少なくとも2,500ユニット離れた場所に現れます。
- ボスに与えられたダメージの5%以上を与えたパイロットが、その撃破の報酬を受け取ります。

<!-- swarms-rules:end -->

## ワールド {#the-worlds}

ワールドは、ほかのすべてのエイリアンと同じように群れを強化します（[ワールド](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)）。群れの艦の船体、シールド、シールドリチャージ、レーザーのダメージ、ロケットのダメージ、回復は、Alpha の数値に下の強さを掛けたもので、撃破の報酬には下の報酬倍率が掛かります。速度、射程、ドロップはどのワールドでも同じです。各記事に、3つのワールドそれぞれでの各艦の数値が載っています。

<!-- swarms-world:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| ワールド | 強さ | 報酬倍率 |
| :--- | ---: | ---: |
| **Alpha** | ×1 | ×1 |
| **Beta** | ×1.5 | ×2 |
| **Gamma** | ×2 | ×3 |

<!-- swarms-world:end -->

## パイロットへの通知 {#what-the-pilots-are-told}

Seeker の群れと Pirate の群れは、ボスが現れたときと倒されたときに、そのセクターのパイロットに知らせます。Dormant の群れはワールド全体に知らせ、危険セクターのマップと銀河マップに印が付くので、パイロットは見つけられます。これらはシステムの行です。チャットの**システム**タブに未読数付きで表示され、**全体**タブや**ローカル**タブには出ません。ボスの撃破は、撃破の功績を得たパイロットの名前を載せた行がキルフィードにも出ます。誰に知らされるかは、各記事の*ひと目で*の一覧に書かれています。

## 群れとの戦い {#fighting-a-swarm}

- **リーダーは決して自分から戦いを始めません。** リーダーはパイロットに攻撃されるまでうろつき、攻撃されると反撃します。その近くにいる群れの艦は、最初に攻撃したパイロットに対して戦いに加わります（距離は上のルールにあります）。例外は Pirate Scout で、近づいてきたパイロットを誰でも攻撃します。リーダーは自分で船体を修復することがないので、与えたダメージは、配下が回復しない限りそのまま残ります。シールドはほかのエイリアンと同じように再充電されます。
- **群れの艦が戦うのはパイロットだけです。** エイリアンを撃たず、エイリアンからも撃たれません。[企業パイロット](/wiki/03-Mechanics/Company-Pilots.md)は群れの艦を無視し、狩ることも、あなたを助けに来ることもありません。
- **ロケット。** Pirate Boss と Dormant Force、Pulse は、自分を攻撃したパイロットに向けて**直進**ロケット、つまり[Rivet ロケット](/wiki/06-Items/Rockets.md)を撃ちます。動き続ける艦はかわせますが、止まっている艦には当たります。
- **戦いの規模。** Seeker の群れは2人向け、Pirate の群れは小さなグループ向け、Dormant の群れは最強の艦の大きなグループ向けです。上位のワールドほど、ほかのエイリアンと同じく、より多くのパイロットが必要です。

## 持っていくもの {#what-to-bring}

- **グループ。** [グループ](/wiki/03-Mechanics/Groups.md)で飛んでください。群れはグループ向けに調整されていて、レベルの低いパイロット1人ではすぐ撃破され、Pirate Boss を1人で倒せるのは最強クラスの艦だけです。Dormant の群れは誰にも1人では倒せません。群れは最初に攻撃したパイロットと戦うので（[エイリアンが戦う相手](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)）、グループでいちばん頑丈な艦に最初に攻撃させましょう。
- **より良い弾薬。** x2 以上の弾薬を持っていきましょう（[レーザーと弾薬](/wiki/06-Items/Lasers.md)を参照）。群れの配下の回復量は、小さなグループが x1 弾薬で与えるダメージを上回ることがあります。
- **シールドと修復**：長い戦いに備えます。自分の艦のアビリティ（[アビリティ](/wiki/03-Mechanics/Abilities.md)）は、数分かかる Pirate 戦で最も重要になります。
- **動く余地。** 自分のほうが射程で勝る武器の届かない位置にとどまり、ロケットに対しては動き続けましょう。

## ボス撃破の報酬 {#how-a-boss-kill-pays}

通常のエイリアンは、最初に攻撃したパイロットに報酬を払います（[戦闘](/wiki/03-Mechanics/Combat.md#kill-rewards-first-hit-claims)）。群れのリーダーと各 Dormant Pulse は、代わりに**与えたダメージに応じて**報酬を払います。

- **報酬はダメージに応じて分けられます。** 上のルールで示された割合以上のダメージを与えたパイロットが、与えたダメージに比例して報酬を受け取ります。撃破のクレジット、Thulium、経験値、名誉は、その人たちの間で分けられます。割合に届かなかったパイロットには何も支払われません。
- **積荷コンテナは最もダメージを与えたパイロットのものになります。** 通常のエイリアンと同じく、30秒間はそのパイロット（とそのクラン）のもので、その後は誰でも取れます（[積荷](/wiki/03-Mechanics/Cargo.md)）。Dormant の各艦には、それぞれ独自のダメージ集計と独自のコンテナがあります。
- **配下はいつもどおりに支払います。** Pirate Scout と Seeker Slave は最初に攻撃したパイロットに報酬を払い、その報酬はボスに比べて少額です。
- **ボスの報酬は、周囲のエイリアンを上回るように作られています。** Pirate Boss と戦う1分は、Goombah と戦う1分より多く報酬を払い、Dormant の群れはさらに多く払います。Boss Seeker の報酬は、ちょうど Seeker 10体分です。

撃破はすべて、その艦自身の名前でキルの統計に数えられ、ランキングに PvE ポイントを加えます。

<!-- swarms-points:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| 群れの艦 | 群れ | 撃破1回あたりの PvE ポイント |
| :--- | :--- | ---: |
| **Pirate Boss** | Pirate の群れ | 10 |
| **Pirate Scout** | Pirate の群れ | 1 |
| **Dormant Force** | Dormant の群れ | 25 |
| **Dormant Pulse** | Dormant の群れ | 10 |
| **Boss Seeker** | Seeker の群れ | 5 |
| **Seeker Slave** | Seeker の群れ | 1 |

<!-- swarms-points:end -->

群れの撃破はほかのエイリアンの撃破としては数えられません。Boss Seeker や Seeker Slave は、Seeker を求めるミッションでは Seeker になりませんし、ワイプポイントのマイルストーン（[ワイプのタイムライン](/wiki/03-Mechanics/Wipe-Timeline.md#earning-wipe-points)）も5種類のエイリアンのものだけです。
