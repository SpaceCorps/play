<!-- wiki-i18n source: d73343b5c426be4e -->
<!-- wiki-i18n title: エクストラ -->
# エクストラ {#extras}

エクストラは、艦の**エクストラスロット**（Protos、Kitefin、Ostirion、Nomad（最初から持っているか購入する艦）は構成ごとに2つ、Paragon、Ironclad、Wraith、Storm（製作する艦）は3つ。Extra Slots CPU でさらに3、5、7つ増えます）に入れるガジェットです。ホットバーの「エクストラ」の選択画面から、またはエクストラを割り当てたホットバーのスロットから起動します。効果があるのは、飛行中の構成に装備したものだけです。もう一方の構成に装備したものは、構成を切り替えるまで待機します。

| エクストラ | 効果 | 使用回数 | 価格 |
| :---- | :----------- | :--- | :---- |
| **Repair Drone I～IV** | 船体を修理します。毎秒の回復量は最大値の1.5%、2.25%、3.5%、5%（I～IV の順） | 無制限 | 5,000 / 15,000 / 35,000クレジット、2,000 Thulium |
| **Cloaking CPU S** | 艦を隠します | 10 | 5,000 Thulium |
| **Cloaking CPU M** | 艦を隠します | 25 | 11,250 Thulium |
| **Cloaking CPU L** | 艦を隠します | 50 | 20,000 Thulium |
| **P.E.T. Station I～III** | ON の間、ドッキング中の2体、3体、5体の[P.E.T.](/wiki/03-Mechanics/Pets.md#the-station)が艦にブーストを与え、経験値を得て、働きます。OFF の間は、そのどれもしません | ON / OFF | アセンブリ：研究後（下のアイテムツリー） |

Cloaking CPU は、ショップでのみ販売されています。統合はできず、ドロップや報酬で入手することもできません。**EMP Charge** はもうエクストラではありません。0.4.21 からは消耗品で、ロケットと同じようにスタックで持ち運び、どのスロットにも装着しないため、エクストラスロットを使いません（[ロケット](/wiki/06-Items/Rockets.md#emp-charge)を参照）。2つの **Energetic Wall** もエクストラではなくなりました。0.4.22 からは同じく消耗品で、スタックで持ち運び、どのスロットにも装着しません（[Energetic Wall](#energetic-wall)を参照）。

新しいパイロットの**スターターキット**では、Protos の2つのエクストラスロットに、すでに2つのエクストラが装着されています。**Base CPU I**（10回使用でき、自分の企業の基地へテレポートします）と **Repair Drone I** です。使うには、ホットバーの「エクストラ」の選択画面からスロットにドラッグしてください。キットがもらえるのは新しいパイロットだけです。0.4.10より前に登録したパイロットには、ありません。

さらに7つの CPU は販売されていません。Skylab の研究センターが研究を終えると、アセンブリで製作できます（[研究](/wiki/03-Mechanics/Research.md)を参照）。Extra Slots CPU I・II・III、Jump CPU、Base CPU I・II、Auto-Repair CPU で、それぞれの働きは[最後のセクション](#research-cpus)にあります。Cloaking CPU と同じく、Jump CPU と Base CPU は落ち着いたときのためのものです。自分が撃ったり攻撃を受けたりしてから10秒以内は、この3つのどれも始動しません。2つのワープ CPU、つまり Jump CPU と Base CPU も、ミッションアイテムを運搬中は使えません（「ミッションアイテムを運搬中はワープ CPU を使えません。」）。[ミッションアイテム](/wiki/03-Mechanics/Quests.md#quest-items)を参照してください。

エクストラは、ホットバーのスロットに短い略称が付きます。Repair Drone は **REP**、Cloaking CPU は **CLK**、Auto-Repair CPU・Base CPU・Jump CPU は順に **ARP**、**BSE**、**JMP** です。消耗品にもそれぞれ略称があります。**EMP** と、Energetic Wall の **WAL** です。Extra Slots CPU にはスロットがなく、Skylab に取り付けられます。3つの **P.E.T. Station** のアイテムはほかのエクストラと同じで、略称は **PET** です。装備すると、そのスロットで Station を **ON** と **OFF** に切り替えられ（2回の押下の間は1秒）、どちらかが表示されます。ON の間はドッキング中の[P.E.T.](/wiki/03-Mechanics/Pets.md)が数えられ、OFF の間は数えられません。スロットにポインターを合わせると、今押すと何が起こるか、または押しても起こらない理由が読めます。

![The Extras picker of the hotbar: the Repair Drone, the Auto-Repair, Cloaking, Base and Jump CPUs and the P.E.T. Station you have fitted (REP, ARP, CLK, BSE, JMP, PET), to drag onto a slot](../../img/wiki-img/shots/cpu-hotbar.jpg)
![The Consumables picker of the hotbar: the EMP Charge and the Energetic Wall I and II (EMP, WAL) to drag onto a slot, with how many of each you hold](../../img/wiki-img/shots/emp-hotbar.jpg)
![The hotbar with extras on its slots: a Repair Drone, a Cloaking CPU with its uses left, the P.E.T. Station that says ON, the EMP Charge and the Energetic Wall I and II with the number of each you carry](../../img/wiki-img/shots/hotbar-slots.jpg)
![The Repair Drone of an extra slot docked to its ship and its wingmen](../../img/wiki-img/shots/repair-drones-extra.jpg)
![The Shop's Consumables category: the EMP Charge and the Energetic Wall I with their prices in Thulium, and the Energetic Wall II, which only Assembly makes](../../img/wiki-img/shots/shop-consumables.jpg)

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## アイテムツリー {#item-tree}

アセンブリで作れるものは、先にその技術が必要です。アイテムにカーソルを合わせると、研究にかかる時間が分かります。技術ツリー、燃料、ブーストは [研究](/wiki/03-Mechanics/Research.md) を参照してください。

```tree
P.E.T. Station I | extra, common | craft 100000 Credits, 2000 Thulium, 300 s | research 10800 s, 10800 science | 25 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md
Cloaking CPU S | extra, common | buy 5000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Repair Drone I | extra, common | buy 5000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone II | extra, common | buy 15000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone III | extra, common | buy 35000 Credits | /wiki/06-Items/Extras.md#repair-drones
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
P.E.T. Station II | extra, uncommon | craft 400000 Credits, 6000 Thulium, 600 s | research 36000 s, 36000 science | 60 Ship Fragment, 6 Reinforced Hull Plate, 4 Power Core, 8 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md
Cloaking CPU M | extra, uncommon | buy 11250 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 2 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Extras.md#base-cpus
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu
P.E.T. Station III | extra, rare | craft 1500000 Credits, 18000 Thulium, 900 s | research 86400 s, 86400 science | 120 Ship Fragment, 12 Reinforced Hull Plate, 8 Power Core, 2 Ancient Control Unit, 12 Velkonite Reinforced Plate, 4 Orvium Reinforced Plate | /wiki/06-Items/Extras.md
Repair Drone IV | extra, rare | buy 2000 Thulium | /wiki/06-Items/Extras.md#repair-drones
Cloaking CPU L | extra, rare | buy 20000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 6 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu

P.E.T. Station I -> P.E.T. Station II -> P.E.T. Station III
Cloaking CPU S -> Cloaking CPU M -> Cloaking CPU L
Repair Drone I -> Repair Drone II -> Repair Drone III -> Repair Drone IV
Extra Slots CPU I -> Extra Slots CPU II -> Extra Slots CPU III
Base CPU I -> Base CPU II
```
<!-- item-tree:end -->

## Repair Drone {#repair-drones}

Repair Drone を起動（REP）すると、船体が満タンになるまで修理します。作動するのは、被弾せずに10秒経ってからで、被弾すると停止します。複数装備している場合は、最も性能の高いものが働きます。[Auto-Repair CPU](#auto-repair-cpu) があれば、作動させ直してくれます。修理速度は[戦闘](/wiki/03-Mechanics/Combat.md)に載っています。修復している間は、小さな修復ドローンが艦から飛び出して周りを回り、船体にビームを当てます。Repair Drone I は1機、II は2機、III と IV は3機で、近くのパイロットにも見えます。修復が止まると、ドローンはドックに戻ります。

## Cloaking CPU

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
- **画面での見え方。**あなたの艦は透けて、紫の破線の輪郭になり、ドローンも一緒に薄くなります。画面上部のチップに「ステルス」と残りの使用回数が表示されます（秒数は出ません。タイマーがないためです）。CLK スロットには残りの使用回数が表示され、ステルス中は紫に光って ON と表示されます。ステルスが終わると（理由を問わず）、スロットは暗くなり、60秒の再充填をカウントします。サーバーに拒否された操作（再充填中、セーフゾーン、直近10秒以内の被弾または射撃）はスロットが赤く点滅し、メッセージで理由が知らされます。味方は、名前の前にゴーストマークがついた淡いゴーストとして表示され、近くでステルスになったパイロットは波紋とともに消えます。REP と同じように、ホットバーのエクストラから CLK をスロットにドラッグして使います。
- **使用回数**は CPU 自体に保存されます。ログアウト、撃破、ゲームの再起動で戻ることはなく、キャンセルした起動も消費済みのままです。パックの最後の1回を使い切ると、そのパックは消費され、同じ CPU の予備をインベントリに持っていれば、そのスロットに補充されます。
- 1つの構成に**複数の CPU** を装備しても、効果は合算されません。残りの使用回数が最も少ないものから先に使われます。

S、M、L の挙動はすべて同じです。大きいパックは、1回あたりの価格が安いだけです（500、450、400 Thulium）。

## Energetic Wall

WAL スロットを押すと、**カーソルの位置**に、艦からカーソルへの線に直角に**プラズマの壁**が立ちます。長さ360ユニット（艦のモデルおよそ3つ半）、幅10ユニットの帯です。中心は艦の中心から**450ユニット**以内で、カーソルがそれより遠ければ線上450ユニットの位置に、120ユニットより近ければ120ユニットの位置に出ます。スロットが使える間は、薄い点線とゴーストの輪郭で立つ場所が分かります。カーソルの位置がゲームに分からないときは、艦の中心から220ユニット前方に、進行方向に対して横向きに立ちます。Energetic Wall は、[EMP Charge](/wiki/06-Items/Rockets.md#emp-charge) と同じ**消耗品**です。インベントリのスタックで持ち、どの艦のスロットも使いません（0.4.22 まではエクストラでした）。使うには、ホットバーの消耗品からスロットにドラッグします。2つのレベルは別々の項目なので、1つのスロットには1つのレベルが入ります。壁は、後ろに隠れたり通路をふさいだりするためのもので、中に立つものではありません。

- **何を止めるか。** 壁を横切る弾は、誰が撃ったものでも、どちら側からでも、代わりに壁に当たります。レーザーの斉射、ロケット、エイリアンの斉射のすべてです。壁の後ろにいるものは何も受けず、壁の耐久値がダメージを負います。壁で炸裂したロケットの爆風は、手前側の艦には届きますが、後ろの艦には届きません。自分の弾も同じで、自分の壁越しに外へ撃つことはできません。N.I.K.E.とDormant Swampの砲台の弾は、小惑星と同じように壁の上を越えていきます。
- **何を燃やすか。** 船体が帯に触れた艦はすべて、まずシールドに**毎秒2,500のダメージ**を受けます。自分の艦も、エイリアンも企業パイロットも同じです。セーフゾーンにいる艦やリスポーン直後の保護中の艦は燃えず、1隻に帯が2本重なっても加算されません。
- **どれだけ持つか。** レベル1の壁は**耐久値30,000**、レベル2は**90,000**です。壁は何もしなくても毎秒その60分の1を失うので、誰にも撃たれない壁は**60秒**で消えます。射撃は寿命を縮めます。Helios Beam 12門に x4 弾の Wraith なら、レベル1の壁を約3.5秒で破壊します。
- **同時に1枚、1回につき1枚。** 新しい壁は古い壁の代わりになります。押したあと、アイテムは**90秒**再充填されます。待ち時間は艦ではなくパイロットのもので、死亡やログアウトでは短くなりません。押すと、**スロットに入っているレベルの壁を1つ**消費します。消費するのは壁が立ったときだけで、ゲームが拒否した操作（下記）は何も消費せず、待ち時間も始まりません。そのレベルが残っていないときは「Energetic Wall が残っていません。」と表示され、もう一方のレベルが代わりに使われることはありません。
- **使えない場所。** セーフゾーンやリスポーンの保護中、帯がセーフゾーンやゲートに触れる場所、ステルス中、帯の中心がマップの外に出る場所では使えません。どの場合かはゲームが教えてくれます。
- **撃破。** 壁に破壊された艦は放射線で死亡し、撃破は15秒以内に最後に命中させた敵パイロットのものになります（いれば）。壁を立てた本人は、自分で撃っていないものについては何も得られません。壁に破壊されたエイリアンは何も払い出しません。報酬も戦利品もありません。
- **エイリアンは迂回しない。** 壁を通り抜けて燃えるか、自分の側に立ったまま壁を撃ちます。
- **見た目。** 青白い光の帯に、明るい筋が走り、両端に光の柱が立ちます。弾が当たると光り、ほぼ尽きるとちらつきます。レベル2の壁は代わりに黄色く光り、芯が太く明るくなり、輝きも強くなりますが、帯の幅はレベル1の壁と同じ10ユニットです。そばの細い体力バーは短くなり、琥珀色、次に赤に変わります。スロットでは壁の残り寿命が弧、待ち時間が影で表示されます。立てた壁は光ってせり上がり、撃破された壁は火花になって崩れ、時間切れの壁は薄れて消えます。スロットの数字は、そのレベルの残りの壁の数も表します。
- **入手と持ち運び。** Energetic Wall I はショップで1枚 **250 Thulium** で、1つのスタックに最大 **20** まで持てます（[オークション](/wiki/03-Mechanics/Auction.md)に出品中の分も数えます）。Energetic Wall II は、研究センターで研究したあと、アセンブリで**1回の製作につき1枚**、**600 Thulium**、Ship Fragment 5個、Power Core 1個から作ります（通常速度で6時間：[研究](/wiki/03-Mechanics/Research.md)）。最大 **10** まで持てます。ロケットと同じく、持っている壁はシーズン終了で失われますが、トランスポートキャッシュに入れておけば残ります。キャッシュの中の壁は使えません。自分で作った Energetic Wall II はオークションで売れますが、ショップで売っている Energetic Wall I は売れません。

## 研究センターの CPU {#research-cpus}

CPU のうち2つは、各強化系統の最終ティアと同じく Dark Matter Plate を要求します。**Extra Slots CPU III** は4枚（と Ancient Control Unit 2個、Orvium Reinforced Plate 6枚）、**Base CPU II** は4枚（と Ancient Control Unit 1個、Orvium Reinforced Plate 2枚）です。先に Dark Matter Plate を研究してください（[Dark Matter と Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)）。

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | 研究時間 | 先に必要 | 製作に必要な Thulium | 製作時間 |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30分 | – | 12,000 | 5分 |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10時間 | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30,000 | 10分 |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1日 | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75,000 | 15分 |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3時間 | – | 8,000 | 5分 |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10時間 | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | 20,000 | 10分 |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1日 | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40,000 | 15分 |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6時間 | – | 15,000 | 10分 |
| [Energetic Wall II](/wiki/06-Items/Extras.md#energetic-wall) | 6時間 | – | 600 | 2分 |

どれもショップでは売っていません。技術を研究し、アセンブリで CPU を製作します。ツリーの CPU にカーソルを合わせると、アセンブリが何を必要とするか分かります。

### Extra Slots CPUs

- **働き。** Extra Slots CPU I・II・III は、すべての艦のエクストラスロットを 3、5、7 増やします。艦がもともと 3 持っていれば合計は 6、8、10、2 なら 5、7、9 です。上位の CPU は下位を置き換えます。II は I に加算されません。
- **装備ではなく導入。** Extra Slots CPU はアイテムではありません。アセンブリで受け取ると Skylab に導入され、両方の構成のすべての艦に効き、スロットは使いません。ワイプ後も残ります。
- **順番に。** 順に製作してください。II は I を導入済みのとき、III は II を導入済みのときだけ製作できます。それまでは、先に導入すべきものをアセンブリが教えてくれます。3つ合わせて 117,000 Thulium（12,000、30,000、75,000）です。

### Jump CPU

- **働き。** 艦を、あなたのワールドにある任意の企業のセクター（自企業のものも他企業のものも、拠点セクターも含む。`M`、`T`、`G` のセクター 1〜4）へ、1回につき **500 Thulium** でジャンプさせます。使用回数の上限はなく、払うのは Thulium だけです。危険セクター（`DS`）や中立セクター（`N`）へは行けません。
- **ジャンプ。** JMP スロットを押し、星系マップでセクターを選んで確定すると、艦が 5 秒チャージしたあと、そのセクターのゲートに到着します。到着直後は、ふつうのゲートジャンプのあとと同じ保護があります。到着後、CPU は 30 秒のクールダウンに入ります。
- **戦闘中は不可。** 発砲または被弾から 10 秒以内には開始できず、チャージ中の発砲や被弾でジャンプはキャンセルされます（その場合は何も支払いません）。ステルス中はジャンプできません。
- **中立セクターからは不可：** 中立セクターにいるパイロット、または企業に所属しないパイロットは使えません。
- 戦闘中でなければ、危険セクターから出ることはできます。

### Base CPUs

- **働き。** 艦を所属企業の拠点にある、ステーション周囲のセーフゾーンへテレポートさせます（`M-1`、`T-1`、`G-1`。Mission Control があるセクター）。Thulium はかかりません。ホットバーの BSE スロットから起動します。
- **戦闘中は不可。** チャージは 10 秒で、どちらも同じです。発砲または被弾から 10 秒以内、ステルス中、すでに拠点のセーフゾーン内にいるときは開始できず、チャージ中の発砲や被弾でキャンセルされます。

| CPU | 使用回数 | クールダウン |
| :--- | ---: | ---: |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 10 | 10分 |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 25 | 5分 |

- **使い切り、再チャージなし。** 使うたびに CPU の使用回数が1つ減り、使用回数がなくなった CPU は消えます。新しく製作してください。両方を装備している場合は、上位の II から使われます。

### Auto-Repair CPU

- **働き。** 手動で出撃させられる状況になるたびに、エクストラスロットに装備した Repair Drone を自動で出撃させます。船体が満タンでなく、ドローンがまだ出ておらず、最後の被弾から 10 秒が過ぎていることが条件です。船体の割合を設定する必要はありません。
- 専用のエクストラスロットを1つ使い、同じ構成のエクストラスロットに Repair Drone がなければ何もしません。アビリティスロットにある Repair Drone は出撃させません（それは Emergency Repair ボタンです）。
- **ドローンを手動で止めた場合、**船体が再び満タンになるか、自分でドローンを出撃させるまで、CPU は手を出しません。


<!-- research-cpus:end -->
