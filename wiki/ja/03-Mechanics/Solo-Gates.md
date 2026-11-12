<!-- wiki-i18n source: 9b254c924e79c7e8 -->
<!-- wiki-i18n title: ソロゲート -->
# ソロゲート {#solo-gates}

<!-- wiki-search: solo gates; solo gate; gate; gates; galaxy gates; rift; rifts; alpha rift; beta breach; gamma foundry; delta siege; omega vault; chrono gate; chrono-gate; materializer; energy materializer; scan; spin; gate part; gate parts; guarantee; pity; consolation; wave; waves; nuke wave; skip; boss; lives; resume; abandon; speedrun; no death; challenge; achievement; thulium cap; ソロゲート; ゲート; ギャラクシーゲート; パーツ; ゲートパーツ; エネルギーマテリアライザー; スピン; 保証; ウェーブ; ライフ; 再開; 放棄; ノーデス; チャレンジ; 実績; Thulium上限 -->

**ソロゲート**は、ギャラクシーゲートのうち単独で飛ぶ5つのゲートです。**Alpha Rift**、**Beta Breach**、**Gamma Foundry**、**Delta Siege**、**Omega Vault**があります。それぞれが専用の空っぽのアリーナで、エイリアンのウェーブが次々に襲いかかり、最後にボスが待っています。ゲートは**パーツ**で建設し、パーツはThuliumでエネルギーマテリアライザーをスピンして見つけます。クリアするとクレジット、Thulium、経験値、名誉、鉱石、プレート、弾薬が支払われます。

ソロゲートは[クランのダンジョン](/wiki/03-Mechanics/Dungeons.md)ではありません。ダンジョンはクランがグループのために開く迷路で、最奥にウォーロードがいます。ソロゲートはあなた1人だけが入るアリーナで、ほかの誰も一緒に入れません。両者のルール、報酬、制限は別々です。ギャラクシーゲートのページには**Chrono-Gate**もあります。これは飛ぶ場所ではなく、ワイプに向けてあなたの[トランスポートキャッシュ](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-)を開くゲートで、そのパーツも同じスピンで見つかります。

## 概要 {#at-a-glance}

<!-- solo-glance:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **ゲート**：6：Chrono-Gateと5のソロゲート（Alpha Rift, Beta Breach, Gamma Foundry, Delta Siege と Omega Vault）
- **スピン**：1スピンあたり100 Thulium、一度に1, 5, 10または100スピンまで
- **パーツの確率**：1スピンあたり13%。パーツが属するゲートはランダムに決まり、各ゲートがスピンの2.17%を受け持ちます。Chrono-Gateが完成すると、その分はホイールから外れ、ソロゲートはそれぞれ2.17%のままです
- **保証**：パーツなしのスピンが24回続くと、スピンごとに確率が上がり、47回続くと次のスピンは必ずパーツを見つけます。どのゲートのパーツでもカウントは最初に戻ります
- **ライフ**：挑戦1回につき3。死亡するたびに1つ減ります
- **カウントダウン**：すべてのウェーブの前に5秒。最初のウェーブとボスのウェーブも同じです。ウェーブにタイマーはなく、ランにもありません
- **アリーナ**：岩のない8,000×6,000ユニットの開けた空間で、中にいるのはあなただけです。ワールドには16あり、すべて使用中のときは入れません
- **同時のエイリアン**：ウェーブの同時生存数は最大60、任意ウェーブでは250です。残りは空きを待ちます
- **ボス**：ボスはフェーズが変わるとき、3秒ダメージを受けません
- **Thulium上限**：ゲートが払い戻すのは、スピンに使ったThuliumの50%までです。残りは削られ、結果画面に削られた額が表示されます

<!-- solo-glance:end -->

## ゲートパーツを見つける {#finding-gate-parts}

**ギャラクシーゲート**のページを開き、エネルギーマテリアライザーをスピンします。スピンは1回ごとにThuliumで支払い、見つかるパーツは多くても1つで、そのパーツは6つのゲートのどれかに属し、ランダムに決まります。ゲートを建設するにはそのゲートのパーツが一定数必要で、パーツは使うまであなたのものです。パーツが見つからなかったスピンは無駄になりません。賞品が支払われます（[下](#a-spin-without-a-part)）。スピンは毎回課金され、Chrono-Gateが完成していても同じです。Chrono-Gateが完成すると、そのスピンの取り分は何も見つけず、ソロゲートは自分の確率を保つので、ソロゲートのパーツのコストはChrono-Gateの有無にかかわらず同じです。

表は、各ゲートに必要なパーツ数と、**保証を含めた**平均コストを示します（スピンは抽選なので、運のいいパイロットは安く、運の悪いパイロットは高くつき、保証が許す最長のスピン連続までです）。

<!-- solo-parts:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| ゲート | 完成に必要なパーツ | 1スピンあたりのパーツ確率 | 平均スピン数 | 平均Thulium |
| :--- | ---: | ---: | ---: | ---: |
| **Chrono-Gate** | 2 | 2.17% | 91 | 9,093 |
| **Alpha Rift** | 11 | 2.17% | 500 | 50,011 |
| **Beta Breach** | 26 | 2.17% | 1,182 | 118,208 |
| **Gamma Foundry** | 54 | 2.17% | 2,455 | 245,508 |
| **Delta Siege** | 87 | 2.17% | 3,955 | 395,541 |
| **Omega Vault** | 108 | 2.17% | 4,910 | 491,017 |

<!-- solo-parts:end -->

Chrono-Gateのパーツはワイプでゼロに戻り、毎シーズン見つけ直します。**ソロゲートのパーツは残ります**。保証のカウントと、スピンに使った額とゲートが払い戻した額の記録も残ります。ワイプはどれも奪いません（[ゲートとワイプ](#gates-and-the-wipe)）。

### パーツのないスピン {#a-spin-without-a-part}

ほとんどのスピンはパーツを見つけません。それぞれが賞品を1つ支払い、下の確率で選ばれます。2段階目以上の倍率のレーザー弾薬、2段階目か3段階目のロケットのスタック、そして時々[スペシャルアイテム](/wiki/06-Items/Special-Items.md)や[コンテナ](/wiki/06-Items/Containers.md)です。渡せない賞品（そのスペシャルアイテムをすでに上限まで持っている場合など）は、同じ抽選で弾薬かロケットのスタックになるので、スピンが表より少なく支払うことはありません。賞品の価値はスピンの費用よりはっきり低く、ゲートはThuliumの吸い込み口です。

<!-- solo-prizes:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| 報酬 | 1スピンあたりの確率 |
| :--- | ---: |
| コンテナ：Chroma Archive | 0.01% |
| スペシャルアイテム：Magic Hammer | 0.2% |
| スペシャルアイテム：Schematics | 0.2% |
| スペシャルアイテム：Philosopher's Stone | 0.2% |
| スペシャルアイテム：Forger's Seal | 0.2% |
| スペシャルアイテム：Workforce Contract | 0.2% |
| スペシャルアイテム：Tinkerer's Badge | 0.1% |
| レーザー弾薬：Advanced Plasma ×75 | 12.88% |
| レーザー弾薬：Antimatter Battery I ×62 | 8.59% |
| レーザー弾薬：Ultra Core ×40 | 8.59% |
| レーザー弾薬：Antimatter Battery II ×29 | 4.29% |
| レーザー弾薬：Dark Matter Ammo I ×31 | 4.29% |
| レーザー弾薬：Experimental Fusion Core ×17 | 2.15% |
| レーザー弾薬：Dark Matter Ammo II ×17 | 2.15% |
| ロケット：Lancet II ×4 | 8.59% |
| ロケット：Rivet II ×4 | 8.59% |
| ロケット：Ember II ×4 | 8.59% |
| ロケット：Scatter II ×4 | 8.59% |
| ロケット：Lancet III ×1 | 2.15% |
| ロケット：Rivet III ×1 | 2.15% |
| ロケット：Ember III ×1 | 2.15% |
| ロケット：Scatter III ×1 | 2.15% |

<!-- solo-prizes:end -->

## 入る {#going-in}

ゲートはギャラクシーゲートのページで**建設**し、そのポータルから**ジャンプして入ります**。建設はステーションから、船をドッキングしたままできるほか、飛行中にもできます。ツールバーのゲートのボタンで開く**ギャラクシーゲートのウィンドウ**で、ページと同じようにスピン、建設、目的地の選択ができます。必要なのは次のものです。

- ゲートのパーツ：パーツは**建設するときに1度だけ**取られ、拒否された建設では何も取られません。
- ほかのソロのランが開いていないこと：同時に持てるランは1つで、離れたランは、別のゲートを建設する前にポータルから入り直すか放棄します。
- ホームサーバー（地域サーバーにはゲートがありません）。

建設したゲートは、あなたの**基地セクター**（企業に応じて`M-1`、`T-1`、`G-1`のいずれか）に、ゲート名のついたポータルとして立ちます。どこにあるかはギャラクシーゲートのページに表示されます。**出撃してポータルまで飛び、ジャンプ**して通ります。ほかのポータルと同じです。入るときはワールドにリフトが空いている必要があります。各ワールドには一定数のリフトがあり、すべて使用中のときは待ちます。

**地域サーバーで（Singapore、US East）。**ゲート自体はホームサーバーに残ります。地域サーバーでは、建設も、プレイも、支払いも行われません。ただし、建設したゲートはそこでも忘れられません。到着したときにそのことが知らされ、ゲートのポータルはそこでもあなたの基地セクターに立ちます。そのポータルにジャンプするとホームサーバーに戻され、上記のとおりゲートへ出撃できます。

空っぽのアリーナの中央に、1人で降り立ちます。中ではほかの誰もあなたを攻撃できず、Jump CPUとBase CPUは動きません。

## ランの流れ {#how-a-run-goes}

1. **ウェーブの前には必ずカウントダウンがあります**。最初のウェーブとボスのウェーブも同じです。ウェーブにタイマーはなく、ランにもありません。必要なだけ時間をかけられます。
2. **ウェーブ**はあなたの周りのリングに現れ、ゲートのペースで迫ってきます。同時に生きているのは一定数までで、残りは空きを待ちます。最後のエイリアンが倒れると終わります。
3. **進行状況は各ウェーブのあとに保存されます。**離れた場合、進行中だったウェーブは、戻ったときに最初からやり直しになります。
4. **任意ウェーブ**はSeekerの巨大なウェーブで、Delta SiegeとOmega Vaultにそれぞれ1つあります。カウントダウン中にスキップでき、スキップすると完了扱いになり、**何も**支払われません。戦えば、その撃破はほかのウェーブと同じように支払われます。
5. **最後のウェーブはボスです。**船体が減るとフェーズが変わり、変わるたびに一瞬だけダメージを受けなくなります。ボスを倒すとランはクリアになり、クリア報酬はすぐに支払われます。

**ライフ。**死亡するとライフを1つ失い、ほかの死亡と同じく基地に送られます。ランはあなたを待ち、時計は進みません。ランが開いていてアリーナの外にいる間は、**ゲートのポータルが基地セクターに立っています**。そこをジャンプで通ると、**再開**と同じように、保存されたウェーブに残りライフで戻ります。新しいパーツは要求されません。最後のライフがなくなると挑戦は終わりますが、ランは最後にクリアしたウェーブで開いたままで、入り直すとライフが満タンになります。**退出**、ログオフ、ワールドの切り替えはライフを失わずにランを一時停止します。サーバーの再起動でもランは開いたままです。**放棄**するとランをあきらめます。パーツは失われ、倒したエイリアンはその時点のとおりに支払われます。**再開**は飛行中の船からしかできません。死亡のあと、結果画面の再開ボタンは、その理由を示す一行を添えて、復帰するまで待機します。復帰した船は上限つきの船体で戻ります。船体が半分を切ると結果画面が警告しますが、**再開**はそのままの状態で戻ります。基地の修理艦は、そのオーラの内側であなたを修理します。

どのワールドも同じゲートと戦います。エイリアンの強さと報酬は、飛んでいるワールドによって変わりません。

### ウェーブ {#the-waves}

エイリアンはゲートのものと同じ（Seeker、Phantasm、Bulwark、Goombah、Crystalys）で、ゲートによって強くも弱くもなります。計画時間は、レーザー技術の初期レベルのパイロットにゲートが要求するように作られた時間です（[パイロットスキル](/wiki/03-Mechanics/Pilot-Skills.md)）。レーザー技術を育てたパイロットはもっと早く終わります。

一部のウェーブには**群れ**が来ます。ゲームのボスNPC（Boss Seeker、Boss Phantasm、Boss Goombah、Boss Crystalys）が護衛を連れ、ひとつの集団で攻めてきます。群れの船はすべてそのウェーブの一部で、最後の1隻が倒れたときにウェーブが終わります。報酬はウェーブの他の船と同じで、[エイリアンの表](#the-aliens)の数値のとおりです。**ボスNPCは、ゲームのセクターと同じように戦利品を落とします**。鉱石、プレート、弾薬、ロケットです（何を落とすかは[群れのページ](/wiki/05-Swarms/Swarms.md)にあります）。ゲートには拾う箱はありません。戦利品は報酬と一緒に、そのままインベントリに入り、報酬と同じくランごとに1度だけです。護衛は、ゲートでもセクターでも何も落とさず、ボスを回復せず、戻ってもきません。どのゲートのどのウェーブに群れが来るかは、下の表に載っています。

<!-- solo-waves:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| ゲート | ウェーブ数（ボスを含む） | ウェーブのエイリアン | ボスNPCと群れ | ボス | 計画時間 |
| :--- | ---: | :--- | :--- | :--- | :--- |
| **Alpha Rift** | 10 | 44 Seeker, 140 Phantasm | ウェーブ5：1 Seeker Swarm, 1 Phantasm Swarm | Enhanced Phantasm | 10～15 分 |
| **Beta Breach** | 14 | 64 Seeker, 158 Phantasm, 80 Bulwark, 20 Goombah | ウェーブ4：2 Seeker Swarm; ウェーブ9：1 Phantasm Swarm | Enhanced Bulwark | 15～25 分 |
| **Gamma Foundry** | 18 | 78 Phantasm, 117 Bulwark, 91 Goombah, 8 Crystalys | ウェーブ4：1 Phantasm Swarm; ウェーブ9：1 Goombah Swarm; ウェーブ14：1 Goombah Swarm | Elite Crystalys | 25～35 分 |
| **Delta Siege** | 22 | 250 Seeker, 200 Phantasm, 141 Bulwark, 130 Goombah, 12 Crystalys | ウェーブ5：2 Phantasm Swarm; ウェーブ10：2 Goombah Swarm; ウェーブ15：1 Goombah Swarm; ウェーブ20：1 Crystalys Swarm | Siege Construct | 35～45 分 |
| **Omega Vault** | 26 | 250 Seeker, 236 Phantasm, 170 Bulwark, 174 Goombah, 25 Crystalys | ウェーブ6：1 Goombah Swarm; ウェーブ11：2 Goombah Swarm; ウェーブ16：1 Crystalys Swarm; ウェーブ22：1 Phantasm Swarm | Omega Guardian | 50～60 分 |

- **Delta Siege**：ウェーブ18（250 Seeker）は任意です：カウントダウン中にスキップでき、報酬は何もありません
- **Omega Vault**：ウェーブ17（250 Seeker）は任意です：カウントダウン中にスキップでき、報酬は何もありません; ウェーブ22～24はエリートで、船体、シールド、ダメージが×1.5です

<!-- solo-waves:end -->

### ボス {#the-bosses}

ボスはエイリアンの船を大きくしたもので、船体、シールド、一斉射が専用で、ゲートやワールドの設定では変わりません。ボスの船体が表の値まで減るとフェーズが始まります。シールドが設定し直され、一斉射や全ダメージが変わり、技を始めることがあります。技はすべて予告されます。円、リング、あなたの船の上のマークが、着弾の少し前に示します。ボスが呼ぶエイリアンは、報酬もドロップもありません。

<!-- solo-bosses:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| ボス | ゲート | 船体 | シールド | レーザーの一斉射 |
| :--- | :--- | ---: | ---: | ---: |
| **Enhanced Phantasm** | Alpha Rift | 330,000 | 530,000 | 5,700–7,000 |
| **Enhanced Bulwark** | Beta Breach | 690,000 | 170,000 | 4,500–5,500 |
| **Elite Crystalys** | Gamma Foundry | 620,000 | 250,000 | 3,800–4,700 |
| **Siege Construct** | Delta Siege | 1,150,000 | 1,730,000 | 3,400–4,200 |
| **Omega Guardian** | Omega Vault | 1,340,000 | 840,000 | 2,600–3,200 |

| ボス | フェーズ | 残りの船体 | 行動 |
| :--- | :--- | :--- | :--- |
| **Enhanced Phantasm** | Enhanced Phantasm | 100%～0% | 撃つだけです。 |
| **Enhanced Bulwark** | Shielded | 100%～50% | シールドはボス本来の×4に設定されます。 |
|  | Second attack | 50%～0% | 一斉射は×1.3です。Dormant Lanceロケットを4発、1発あたり61,000で、0.5秒おきにあなたへ撃ち、30秒ごとに一斉に発射します。 |
| **Elite Crystalys** | Elite | 100%～50% | 撃つだけです。 |
|  | Reinforced | 50%～0% | シールドはボス本来の×2に設定されます。10分ごとにGoombahを10体呼び、同時に生きているのは最大10体です。報酬もドロップもありません。 |
| **Siege Construct** | Siege Construct | 100%～0% | 1分ごとに、8個のメテオの一斉落下を3回降らせます。1個あたり5,500で、着弾点から420ユニット以内のすべてに当たり、そのうち50%はあなたを狙います。各円は着弾の3秒前に表示されます。Dormant Lanceロケットを6発、1発あたり9,000で、0.5秒おきにあなたへ撃ち、1分ごとに一斉に発射します。 |
| **Omega Guardian** | Shield Fortress | 100%～70% | シールドはボス本来の×1.5に設定されます。40秒ごとにBulwarkを6体呼び、同時に生きているのは最大12体です。報酬もドロップもありません。 |
|  | Swarm Protocol | 70%～35% | 25秒ごとにPhantasmを12体呼び、同時に生きているのは最大24体です。報酬もドロップもありません。30秒ごとに、140,000の爆風がボスから700ユニット以内のすべてに当たります。リングは着弾の2秒前に表示されます。 |
|  | Overload | 35%～0% | シールドはボス本来の×0.1に設定されます。すべてのダメージが×2.5になります。フェーズに入って2分が過ぎると、すべてのダメージがさらに×2になります。25秒ごとに、28,000の爆風がボスから700ユニット以内のすべてに当たります。リングは着弾の2秒前に表示されます。 |

<!-- solo-bosses:end -->

## クリア報酬 {#what-a-clear-pays}

クリアは表の報酬を**1度だけ**まとめて、ボスが倒れた瞬間に支払います。クレジット、Thulium、経験値、名誉、鉱石、プレート、Power Core、弾薬です。経験値はダンジョンと同じく、PvEランキングポイントに数えられます。

<!-- solo-pay:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| ゲート | クレジット | Thulium | 経験値 | 名誉 |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 450,000 | 5,000 | 70,000 | 1,000 |
| **Beta Breach** | 1,500,000 | 12,000 | 180,000 | 2,500 |
| **Gamma Foundry** | 4,000,000 | 25,000 | 400,000 | 5,500 |
| **Delta Siege** | 8,000,000 | 40,000 | 800,000 | 10,000 |
| **Omega Vault** | 15,000,000 | 60,000 | 1,500,000 | 20,000 |

- **Alpha Rift**：Ship Fragment ×300, Nyxite ×300, Daraxium ×400、弾薬：Advanced Plasma ×20,000, Ultra Core ×5,000, Experimental Fusion Core ×20,000
- **Beta Breach**：Ship Fragment ×700, Nyxite ×750, Daraxium ×800, Cataclysite ×400, Quorvium ×100、弾薬：Advanced Plasma ×50,000, Ultra Core ×20,000, Experimental Fusion Core ×30,000
- **Gamma Foundry**：Ship Fragment ×1,150, Nyxite ×1,000, Cataclysite ×900, Quorvium ×400, Power Core ×15、弾薬：Advanced Plasma ×30,000, Ultra Core ×60,000, Experimental Fusion Core ×50,000
- **Delta Siege**：Ship Fragment ×2,000, Nyxite ×1,750, Cataclysite ×1,500, Quorvium ×1,000, Reinforced Hull Plate ×70, Power Core ×40, Ancient Control Unit ×3、弾薬：Advanced Plasma ×40,000, Ultra Core ×90,000, Experimental Fusion Core ×75,000
- **Omega Vault**：Ship Fragment ×3,250, Nyxite ×2,750, Cataclysite ×2,250, Quorvium ×1,600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10、弾薬：Advanced Plasma ×50,000, Ultra Core ×100,000, Experimental Fusion Core ×100,000

<!-- solo-pay:end -->

**Thuliumには上限があります。**ゲートが払い戻せるのは、スピンに使ったThuliumの一部までで、すべてのゲートとすべてのスピンを通算して数えます（その割合は一番上の一覧にあります）。クリアとそのエイリアンがそれを超えて支払うはずだった分は削られ、結果画面に削られた額が表示されます。クレジット、経験値、名誉、鉱石、プレート、弾薬は削られません。

### エイリアン {#the-aliens}

ゲートで倒したエイリアンは、飛んでいるワールドに関係なく、Alphaでの数値で支払われます。ワールド倍率、ブースター、Premiumボーナスは影響しません。ウェーブはそのエイリアンの分を、ランごとに**1度だけ**支払います。何度離れて戻っても同じです。報酬はランの各区間の終わりに支払われます。退出、死亡、ライフ切れ、放棄、クリアのときです。区間の撃破が未払いになるのは、ワイプのときと、中にいる間にサーバーが再起動されたときだけです（ランは開いたままですが、その区間の撃破は失われます）。ゲートでの撃破は、**セクターを指定しない**[ミッション](/wiki/03-Mechanics/Quests.md#where-it-counts)（チャレンジラインの大きな狩りなど）に、倒したその場で数えられます（ウェーブは、報酬が1度だけ支払われるのと同じように、ランごとに**1度だけ**数えられます）。それ以外には数えられません。撃破統計、実績のカウンター、キルフィード、ドローンやP.E.T.の経験値のどれにも入りません。ただし撃破が支払う経験値は、クリアの経験値と同じようにPvEランキングポイントに数えられます。エイリアンの戦利品は報酬と一緒に、そのままインベントリに入ります。

<!-- solo-kills:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| エイリアン | クレジット | Thulium | 経験値 | 名誉 |
| :--- | ---: | ---: | ---: | ---: |
| **Seeker** | 1,000 | 4 | 100 | 2 |
| **Phantasm** | 3,000 | 12 | 300 | 6 |
| **Bulwark** | 5,000 | 25 | 800 | 10 |
| **Goombah** | 15,000 | 75 | 3,000 | 24 |
| **Crystalys** | 75,000 | 200 | 12,000 | 52 |
| **Boss Seeker** | 10,000 | 40 | 1,000 | 20 |
| **Seeker Slave** | 125 | 1 | 12 | 1 |
| **Boss Phantasm** | 39,000 | 195 | 7,800 | 62 |
| **Phantasm Guard** | 125 | 1 | 12 | 1 |
| **Boss Goombah** | 120,000 | 600 | 24,000 | 192 |
| **Goombah Guard** | 125 | 1 | 12 | 1 |
| **Boss Crystalys** | 393,750 | 1,050 | 63,000 | 273 |
| **Crystalys Guard** | 125 | 1 | 12 | 1 |

| ゲート | クレジット | Thulium | 経験値 | 名誉 |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 514,000 | 2,099 | 55,296 | 1,018 |
| **Beta Breach** | 1,298,500 | 5,939 | 187,744 | 2,470 |
| **Gamma Foundry** | 3,064,500 | 13,693 | 541,944 | 4,696 |
| **Delta Siege** | 5,239,625 | 22,338 | 882,676 | 7,850 |
| **Omega Vault** | 7,088,125 | 29,196 | 1,196,828 | 10,022 |

<!-- solo-kills:end -->

## チャレンジと実績 {#challenges-and-achievements}

任意のチャレンジが2つあり、どのクリアでも達成できます。それぞれ実績を1つ支払い、**Thuliumは支払いません**。**ノーデス**クリアは、入り直した分も含めてラン全体で1度も死ななかったクリアです。**スピードラン**は、ゲートの最短の計画時間以内のクリアで、アリーナの中で過ごした時間で数えます。残りの6つの実績は、各ゲートのクリアと、5つすべてのクリアです。

<!-- solo-achievements:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **裂け目を封じた**（コモン）：Alpha Rift をソロでクリアする。
- **突破口を封鎖**（アンコモン）：Beta Breach をソロでクリアする。
- **鋳造所、停止**（レア）：Gamma Foundry をソロでクリアする。
- **包囲を打ち破る**（レア）：Delta Siege をソロで打ち破る。
- **金庫破り**（エピック）：Omega Vault をソロで解錠する。
- **ゲートキーパー**（レジェンダリー）：5つのソロゲートをすべてクリアする：Alpha、Beta、Gamma、Delta、Omega。
- **ノーデス**（レア）：ライフを失わずにソロゲートをクリアする。
- **時間との勝負**（レア）：最短時間以内にソロゲートをクリアする：Alpha から Omega まで、10、15、25、35、50 分。

<!-- solo-achievements:end -->

## ゲートのアイテム {#items-from-a-gate}

ゲートが与えるものは**取引可能**です。鉱石、プレート、Power Core、弾薬、エイリアンの戦利品は、ドロップやクエスト報酬と同じく[オークション](/wiki/03-Mechanics/Auction.md)に出品でき、例外もほかのアイテムと同じです。パーツのないスピンの賞品は対象外です。ゲートではなくスピンから来るからです。

## ゲートとワイプ {#gates-and-the-wipe}

- **ワイプは開いているランをすべて終わらせ**、そのパーツを返します。ランは次のシーズンには持ち越されません。
- **ワイプで残るもの：**5つのソロゲートのパーツ、保証のカウント、スピンに使った額とゲートが払い戻した額の記録。そのためThuliumの上限はシーズンをまたいで続きます。実績は永久にあなたのものです。
- **ワイプで失われるもの：**Chrono-Gateのパーツ。これまでどおりです。スピンでまた手に入れます。
- **アカウントの削除**は、パーツ、カウント、記録を削除します。
