<!-- wiki-i18n source: 2b63df451b6a864e -->
<!-- wiki-i18n title: エクストラ -->
# エクストラ {#extras}

エクストラは、艦の**エクストラスロット**（どの艦でも、構成ごとに3つ。Extra Slots CPU でさらに増えます）に入れるガジェットです。ホットバーの「エクストラ」の選択画面から、またはエクストラを割り当てたホットバーのスロットから起動します。効果があるのは、飛行中の構成に装備したものだけです。もう一方の構成に装備したものは、構成を切り替えるまで待機します。

| エクストラ | 効果 | 使用回数 | 価格 |
| :---- | :----------- | :--- | :---- |
| **Repair Drone I～IV** | 船体を修理します。毎秒の回復量は最大値の1.5%、2.25%、3.5%、5%（I～IV の順） | 無制限 | 5,000 / 15,000 / 35,000クレジット、2,000 Thulium |
| **Cloaking CPU S** | 艦を隠します | 10 | 5,000 Thulium |
| **Cloaking CPU M** | 艦を隠します | 25 | 11,250 Thulium |
| **Cloaking CPU L** | 艦を隠します | 50 | 20,000 Thulium |
| **EMP Charge** | 3秒間、誰もあなたをロックオンできず、あなたへのロックオンはすべて解除され、近くのステルスもすべて解除されます | 1 | 500 Thulium |

Cloaking CPU と EMP Charge は、ショップでのみ販売されています。統合はできず、ドロップや報酬で入手することもできません。

さらに7つの CPU は販売されていません。Skylab の研究センターが研究を終えると、アセンブリで製作できます（[研究](/wiki/03-Mechanics/Research.md)を参照）。Extra Slots CPU I・II・III、Jump CPU、Base CPU I・II、Auto-Repair CPU で、それぞれの働きは[最後のセクション](#research-cpus)にあります。Cloaking CPU と同じく、Jump CPU と Base CPU は落ち着いたときのためのものです。自分が撃ったり攻撃を受けたりしてから10秒以内は、この3つのどれも始動しません。

エクストラは、ホットバーのスロットに短い略称が付きます。Repair Drone は **REP**、Cloaking CPU は **CLK**、EMP Charge は **EMP**、Auto-Repair CPU・Base CPU・Jump CPU は順に **ARP**、**BSE**、**JMP** です。Extra Slots CPU にはスロットがなく、Skylab に取り付けられます。スロットにポインターを合わせると、今押すと何が起こるか、または押しても起こらない理由が読めます。

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## アイテムツリー {#item-tree}

アセンブリで作れるものは、先にその技術が必要です。アイテムにカーソルを合わせると、研究にかかる時間が分かります。技術ツリー、燃料、ブーストは [研究](/wiki/03-Mechanics/Research.md) を参照してください。

```tree
Cloaking CPU S | extra, common | buy 5000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Repair Drone I | extra, common | buy 5000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone II | extra, common | buy 15000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone III | extra, common | buy 35000 Credits | /wiki/06-Items/Extras.md#repair-drones
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
EMP Charge | extra, uncommon | buy 500 Thulium | /wiki/06-Items/Extras.md#emp-charge
Cloaking CPU M | extra, uncommon | buy 11250 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 8 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu
Repair Drone IV | extra, rare | buy 2000 Thulium | /wiki/06-Items/Extras.md#repair-drones
Cloaking CPU L | extra, rare | buy 20000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 20 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu

Cloaking CPU S -> Cloaking CPU M -> Cloaking CPU L
Repair Drone I -> Repair Drone II -> Repair Drone III -> Repair Drone IV
Extra Slots CPU I -> Extra Slots CPU II -> Extra Slots CPU III
Base CPU I -> Base CPU II
```
<!-- item-tree:end -->

## Repair Drone {#repair-drones}

Repair Drone を起動（REP）すると、船体が満タンになるまで修理します。作動するのは、被弾せずに10秒経ってからで、被弾すると停止します。複数装備している場合は、最も性能の高いものが働きます。[Auto-Repair CPU](#auto-repair-cpu) があれば、作動させ直してくれます。修理速度は[戦闘](/wiki/03-Mechanics/Combat.md)に載っています。

## Cloaking CPU {#cloaking-cpu}

CLK スロットを押すと、ステルスになります。**1回押すと1回使用**したことになり、これはどのパックでも同じです。残りの使用回数は、スロットとハンガーで確認できます。ステルスに**時間制限はありません**。自分で解除するか、何かに破られるまで続きます。

- **あなたが見えない相手。**他企業のパイロットとエイリアンには、あなたの艦がまったく見えません。画面にもターゲット一覧にも現れず、誰もロックオンできません。他企業の企業パイロットも、あなたを無視します。
- **レーダーの点。**自分の企業を除く、マップ上のほかのパイロット全員には、あなたの位置にミニマップ上の無地の**赤い点**が見えます。そのため、誰かがステルス中だと分かります。この点には名前、艦、企業、ID がなく、クリックもターゲットもできません。カーソルを合わせると「ここに何かがステルス中」とだけ表示されます。点は丸く、輪に囲まれています（ミニマップ上の艦は四角です）。輪はゆっくりと脈打ち、「動きを減らす」を設定しているときは静止します。サーバーが点を更新するのは1秒に約2回で、その間の動きは、見ている側のゲームが滑らかに補います。分かるのは、誰かがそこにいることと、その場所だけで、誰なのかまでは分かりません。ステルスになるのを見たパイロットは点を追うことができ、点を狙った**ロケットの爆発**は、やはりあなたに届きます。
- **見える相手。**自分の艦は、薄く輪郭つきで見えます。自分の企業のパイロットには、淡いゴーストとして見えます。他企業のクランメンバーには見えません。クランは申請した人なら誰でも受け入れるためです。ゴーストをターゲットにすることは、自分の企業でもできません。
- セーフゾーン内、CPU の再充填中、被弾または射撃から**10秒以内**は、**ステルスになれません**。
- **解除される条件。**解除されるのは、もう一度スロットを押したとき、最初の斉射またはロケットを撃ったとき（命中した時点で姿が見えます）、セーフゾーンに入ったとき、CPU が飛行中の構成から外れたとき、**1,500ユニット以内で EMP が発動したとき**（誰が使ったものでも同じで、自分の企業のものも含みますが、グループのメンバーのものは含みません）、そしてあなたに当たるロケットの範囲爆発を受けたときです。時間の経過では解除されません。積荷の回収でも解除されません（取った積荷は全員から消えるため、その場所の手の届く範囲に何かがいたことは分かりますが、誰なのかまでは分かりません）。アビリティでも解除されず、ブラックホールの放射線はステルス中の艦にもダメージを与えますが、ステルスは解除しません。ログアウトまたは撃破されると解除されます。操縦されていない艦はステルスではないからです。
- **再充填。**ステルスが終わると、どのような理由で終わった場合でも、CPU は**60秒間**再充填されます。再充填は艦ではなくあなた自身に付いているため、ポータルでジャンプしても、ログアウトしても、撃破されても続きます。押すたびに使用回数は1回消費されます。
- あなたを追っていた**エイリアン**は、あなたを見失います。ステルスになると、あなたの撃破の権利は解除されます。
- **ロケット。**誘導ロケットをあなたにロックオンさせることはできず、直進の単体ロケットはあなたをすり抜けます。**範囲爆発**は、爆発が覆った艦にはやはりダメージを与えてステルスを解除し、その艦の位置が見えるパイロットには、ダメージの数字が出る前にその艦が表示されます。ロケットの発射は射撃にあたります。斉射と同じように自分のステルスが解除され（その後 CPU は上記の60秒間再充填されます）、ステルス中かどうかにかかわらず、発射後10秒間はステルスになれません。
- **ブラックホール**は、ステルス中の艦も他の艦と同じように飲み込み、マップ全体にそれが知らされます。
- **画面での見え方。**あなたの艦は透けて、紫の破線の輪郭になり、画面上部のチップに「ステルス」と残りの使用回数が表示されます（秒数は出ません。タイマーがないためです）。CLK スロットには残りの使用回数が表示され、ステルス中は紫に光って ON と表示されます。ステルスが終わると（理由を問わず）、スロットは暗くなり、60秒の再充填をカウントします。サーバーに拒否された操作（再充填中、セーフゾーン、直近10秒以内の被弾または射撃）はスロットが赤く点滅し、メッセージで理由が知らされます。味方は、名前の前にゴーストマークがついた淡いゴーストとして表示され、近くでステルスになったパイロットは波紋とともに消えます。REP と同じように、ホットバーのエクストラから CLK をスロットにドラッグして使います。
- **使用回数**は CPU 自体に保存されます。ログアウト、撃破、ゲームの再起動で戻ることはなく、キャンセルした起動も消費済みのままです。パックの最後の1回を使い切ると、そのパックは消費され、同じ CPU の予備をインベントリに持っていれば、そのスロットに補充されます。
- 1つの構成に**複数の CPU** を装備しても、効果は合算されません。残りの使用回数が最も少ないものから先に使われます。

S、M、L の挙動はすべて同じです。大きいパックは、1回あたりの価格が安いだけです（500、450、400 Thulium）。

## EMP Charge {#emp-charge}

戦闘中に EMP スロットを押します。**3秒間**、誰もあなたをロックオンできず、**あなたをロックオンしていた全員が**、どこにいても、ただちに**ロックを失います**。対象はパイロット、エイリアン、企業パイロットです。ロックが外れたパイロットには「ロックオン喪失：ターゲットが EMP を使用」と知らされます。この3秒の間にロックオンしようとした相手は、拒否されます。

- **無敵になるわけではありません。**止められるのは、ロックオンが必要なもの、つまりレーザー、誘導ロケット、そして直進の単体ロケットの接触（あなたをすり抜けます）です。**範囲爆発**はロックオンが不要なので、爆発の中にいればダメージを受けますし、ブラックホールはそもそも射撃ではありません。
- **行動は続けられます。**射撃しても EMP は終わりません。ステルスにもなれます（ステルス自体の条件を満たしていれば）。ほかのエクストラも使えます。
- **近くのステルスを解除します。**パルスが発動した時点で**1,500ユニット**以内にいるステルス中の艦はすべて、ただちに姿が見えるようになり、その CPU は60秒の再充填を始めます。所属する企業は問わず、自分の企業も含みます。例外は自分の[グループ](/wiki/03-Mechanics/Groups.md)の艦で、ステルスはそのまま続きます。該当するパイロットには「ステルス解除：近くで EMP が発動しました。」と知らされ、ほかのステルス解除と同じ波紋とともに艦が再び現れ、スロットは再充填を始めます。自分がステルス中は EMP を使えません。
- **何も隠しません。**あなたの姿はこれまでどおり全員に見え、3秒間、放電する電気のシェルをまといます。
- セーフゾーンに守られている間、ステルス中、前回の使用から**30秒以内**のときは、**使えません**。それ以外ではどこでも使えます。シーズン序盤の数日間（平和プロトコル中）も使えます。その間もエイリアンは襲ってくるからです。
- この3秒の間に攻撃したエイリアンは、3秒が過ぎるまであなたに反撃しません。撃破の権利と先制攻撃のルールは変わりません。
- **画面での見え方。**歪んだ空間のパルスが、パイロットから、ステルスを解除する範囲（1,500ユニット）の端まで広がり、範囲内の全員にそれが見えます。3秒間は、艦が放電する電気のシェルに包まれ、自分の艦の周りのリングと画面上部のチップが時間をカウントします。あなたを選択していた全員のターゲットリングは、短いバチッという音とともに砕け散ります。EMP スロットには所持しているチャージ数が表示され、シェルが出ている間は青く光り、再充填中は暗くなります。
- **チャージ1つで1回。** 2つ以上持っていれば、スロットにはインベントリから補充されます。**30秒**の再充填は保存されません。ログアウトやポータルでのジャンプでリセットされ、次のパルスでもチャージを1つ消費します。

## 研究センターの CPU {#research-cpus}

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | 研究時間 | 先に必要 | 製作に必要な Thulium | 製作時間 |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30分 | – | 12,000 | 5分 |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10時間 | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30,000 | 10分 |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1日 | [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75,000 | 15分 |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3時間 | – | 8,000 | 5分 |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10時間 | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 20,000 | 10分 |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1日 | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40,000 | 15分 |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6時間 | – | 15,000 | 10分 |

どれもショップでは売っていません。技術を研究し、アセンブリで CPU を製作します。ツリーの CPU にカーソルを合わせると、アセンブリが何を必要とするか分かります。

### Extra Slots CPUs {#extra-slots-cpus}

- **働き。** Extra Slots CPU I・II・III は、すべての艦のエクストラスロットを 3、5、7 増やします。艦がもともと持つ 3 を足すと、合計は 6、8、10 です。上位の CPU は下位を置き換えます。II は I に加算されません。
- **装備ではなく導入。** Extra Slots CPU はアイテムではありません。アセンブリで受け取ると Skylab に導入され、両方の構成のすべての艦に効き、スロットは使いません。ワイプ後も残ります。
- **順番に。** 順に製作してください。II は I を導入済みのとき、III は II を導入済みのときだけ製作できます。それまでは、先に導入すべきものをアセンブリが教えてくれます。3つ合わせて 117,000 Thulium（12,000、30,000、75,000）です。

### Jump CPU {#jump-cpu}

- **働き。** 艦を、あなたのワールドにある任意の企業のセクター（自企業のものも他企業のものも、拠点セクターも含む。`M`、`T`、`G` のセクター 1〜4）へ、1回につき **500 Thulium** でジャンプさせます。使用回数の上限はなく、払うのは Thulium だけです。危険セクター（`DS`）や中立セクター（`N`）へは行けません。
- **ジャンプ。** JMP スロットを押し、星系マップでセクターを選んで確定すると、艦が 5 秒チャージしたあと、そのセクターのゲートに到着します。到着直後は、ふつうのゲートジャンプのあとと同じ保護があります。到着後、CPU は 30 秒のクールダウンに入ります。
- **戦闘中は不可。** 発砲または被弾から 10 秒以内には開始できず、チャージ中の発砲や被弾でジャンプはキャンセルされます（その場合は何も支払いません）。ステルス中はジャンプできません。
- **中立セクターからは不可：** 中立セクターにいるパイロット、または企業に所属しないパイロットは使えません。
- 戦闘中でなければ、危険セクターから出ることはできます。

### Base CPUs {#base-cpus}

- **働き。** 艦を所属企業の拠点にある、ステーション周囲のセーフゾーンへテレポートさせます（`M-1`、`T-1`、`G-1`。Mission Control があるセクター）。Thulium はかかりません。ホットバーの BSE スロットから起動します。
- **戦闘中は不可。** チャージは 10 秒で、どちらも同じです。発砲または被弾から 10 秒以内、ステルス中、すでに拠点のセーフゾーン内にいるときは開始できず、チャージ中の発砲や被弾でキャンセルされます。

| CPU | 使用回数 | クールダウン |
| :--- | ---: | ---: |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 10 | 10分 |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 25 | 5分 |

- **使い切り、再チャージなし。** 使うたびに CPU の使用回数が1つ減り、使用回数がなくなった CPU は消えます。新しく製作してください。両方を装備している場合は、上位の II から使われます。

### Auto-Repair CPU {#auto-repair-cpu}

- **働き。** 手動で出撃させられる状況になるたびに、エクストラスロットに装備した Repair Drone を自動で出撃させます。船体が満タンでなく、ドローンがまだ出ておらず、最後の被弾から 10 秒が過ぎていることが条件です。船体の割合を設定する必要はありません。
- 専用のエクストラスロットを1つ使い、同じ構成のエクストラスロットに Repair Drone がなければ何もしません。アビリティスロットにある Repair Drone は出撃させません（それは Emergency Repair ボタンです）。
- **ドローンを手動で止めた場合、**船体が再び満タンになるか、自分でドローンを出撃させるまで、CPU は手を出しません。


<!-- research-cpus:end -->
