<!-- wiki-i18n source: 6c44f12b3eb7ef7a -->
<!-- wiki-i18n title: 研究 -->
# 研究 {#research}

**研究センター**は、あなたの [Skylab](/wiki/03-Mechanics/Skylab.md) の研究所です。資源を与えると**科学**に変わり、その科学が**技術**を研究します。[アセンブリ](/wiki/06-Items/Overview.md#upgrading-modules)での製作はすべて、先にその技術が必要です。艦、レーザー、スラスター、CPU は、研究が終わるまで製作できません。

このページには、技術ツリー全体と各技術の所要時間、各資源が与える科学、Thulium ブースト、Dark Matter のルール、新しい CPU がまとまっています。数値はゲーム自身のデータから読み込んでいるので、常にゲーム内と同じです。

![The Research view with a technology that needs Dark Matter picked: its Dark Matter row, the Add and Take back buttons, where Dark Matter comes from and the Wiki button](../../img/wiki-img/shots/research-dark-matter.jpg)
![The Research view filtered to the Defence tree: the shield and hull formations, each a technology with its Dark Matter](../../img/wiki-img/shots/research-formations.jpg)
![The Research view of the Skylab with the pointer on Impulse Thruster III: its kind and tier, what it does, its numbers, the four tiers of its family and what Assembly asks to craft it](../../img/wiki-img/shots/research-hover.jpg)

## 研究センター {#the-research-centre}

<!-- research-centre:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **コアレベル 10 で解放。** 研究センターは [Skylab](/wiki/03-Mechanics/Skylab.md) のモジュールで、ほかのモジュールと同じように建設します。インベントリの Ship Fragment 25個（艦を着陸させた状態）、25,000 クレジット、500 Thulium が必要です。画面は Skylab ページの**研究**表示です。
- **レベル 1 から 10。** レベルが高いほどタンクが大きくなり、消費電力も増えます。研究は速くなりません。技術の所要時間はどのレベルでも同じです。
- **タンク。** 研究センターは科学をタンクに蓄えます。タンクはレベル 1 で 12時間分の研究を、レベルが上がるごとに 25% ずつ多く蓄えられます（下の表）。
- **燃料が科学になる。** 与えた資源はすぐに科学になります（燃料の表のとおり）。研究は、所要時間の1秒ごとに科学 1 を燃やします。タンクが空の間は待機し、センターに補給すると再開します。
- **最初の1時間は無料。** 新しい研究センターは、タンクに科学 3,600（1時間分の研究）を入れた状態で始まります。
- **同時に1つだけ。** 研究センターが同時に研究できる技術は1つだけですが、「キューに追加」ボタンで、その後ろにさらに最大5件まで並べられます。前の研究が終わった瞬間に、不在でも次の研究が自動で始まります。キューに追加しても何も支払いません。技術は開始時に Dark Matter を使い、キューに入れた技術は無料で外せます。
- **不在の間も。** 研究はサーバーの時計で進むので、ログアウトしても続き、完了するかタンクが空になるまで進みます。電力不足や研究センターのアップグレードでは止まりません。
- **電力。** 研究センターはレベル 1 で 25 を消費し、レベルが上がるごとに 15% ずつ増えます。オフにはできません。
- **ワイプでもすべて残る：** 技術、タンクの科学、セットした Dark Matter、進行中の研究、ブースト。
- **持っているものはあなたのもの。** 研究がゲームに加わったとき、すべてのパイロットは、すでに持っていた各アイテムの技術と、そのために必要だった技術を受け取りました。あとから手に入ったアイテム（ギフト、コード、報酬）は、その技術を解放しません。
- **コアレベル 10 未満**では研究できないので、アセンブリで新しいものはまだ製作できません。ステーションミッションがコアを上げる手助けをしてくれます。

<!-- research-centre:end -->

**レーザーアンプと最終ティア。** ティアII～IVの Damage Amp、Crit Amp、Penetration Amp は、ほかの製作物と同じく研究します。アンプの系統が登場した時点でアンプを所持していた、または製作待ちにしていたパイロットは、そのアンプそれぞれの技術と、その下のティアの技術を受け取りました。別のツリーの技術を必要とする技術は12あります。リソースのツリーにある Dark Matter Plate の技術です。各強化系統の最終ティアがプレートを3枚要求するためで、ティアIVの Damage Amp・Crit Amp・Penetration Amp、ティアIVの Absorption Shield Cell・Capacity Shield Cell、ティアIVの Impulse Thruster・Momentum Thruster、Heavy Shield Core、Engine III、Helios Beam、Extra Slots CPU III、Base CPU II が該当します。以前にそのどれかを研究済みなら、その技術はそのまま残りますが、必要なプレートを作るには Dark Matter Plate の技術が要ります。下のツリーにはそのための矢印は描かれませんが、表には載っており、ゲーム内のカードにも名前が出ます（[Dark Matter と Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)）。

Skylab の**研究**表示では、技術が下のツリーのボックスより多くのことを教えてくれます。技術にカーソルを合わせると、研究時間と燃やす科学のカードが開き、その下に、そのアイテムが**何で、何をするか**が表示されます。種類とファミリー内の段階（たとえば4つの Impulse Thruster の3つ目）、説明、ハンガーやショップと同じ形の数値（レーザーのダメージ、クリティカル率、射程、シールドのシールド容量、リチャージ速度、吸収率、スラスターの速度ブーストと速度倍率、ロケットのダメージ、爆発半径、射程、ドローン編成が与えるものと代償）、同じファミリーの各段階の小さな表、そして研究後にアセンブリが製造に要求するもの（時間、クレジットと Thulium、素材）です。これで、研究する前に、その段階で何が得られるかが分かります。技術をクリックすると選択され、ツリーの横のカードに同じ内容がすべて、**研究を開始**ボタンの下に表示されます。 研究が進行中は、開始ボタンの代わりに**キューに追加**が表示されます。キューに入れた技術はツリー上に順番の番号が出て、実行中の研究の下のキューのカードにすべて並び、それぞれの×で外せます。次の技術が開始できないとき（必要な Dark Matter がセンターにない、またはタンクが空）は、キューは待機して理由を表示し、原因を解消して**キューを開始**を押すまで止まっています。

### 各レベルのタンク {#the-tank-at-every-level}

<!-- research-tank:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| レベル | タンク（科学） | 蓄えられる研究時間 | … ブースト時 | 電力 |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 43,200 | 12時間 | 6時間 | 25 |
| 2 | 54,000 | 15時間 | 7.5時間 | 28.7 |
| 3 | 67,500 | 18.8時間 | 9.4時間 | 33.1 |
| 4 | 84,375 | 23.4時間 | 11.7時間 | 38 |
| 5 | 105,469 | 29.3時間 | 14.6時間 | 43.7 |
| 6 | 131,836 | 36.6時間 | 18.3時間 | 50.3 |
| 7 | 164,795 | 45.8時間 | 22.9時間 | 57.8 |
| 8 | 205,994 | 57.2時間 | 28.6時間 | 66.5 |
| 9 | 257,492 | 71.5時間 | 35.8時間 | 76.5 |
| 10 | 321,865 | 89.4時間 | 44.7時間 | 87.9 |

<!-- research-tank:end -->

## 燃料 {#fuel}

研究センターに資源を与えると、1個ずつすぐ科学に変わります。入手に手間がかかる資源ほど、多くの科学を与えます。数値は入手の難しさに従い、レアリティの表示には従いません。鉱石は例外です。1個が与える科学は、コレクターがそれを採掘するのにかかる秒数より多いので、レベルの中ほどにあるコレクターの1時間分の鉱石で、およそ2時間分の研究をまかなえます。鉱石は [Skylab](/wiki/03-Mechanics/Skylab.md#resource-storage) の資源貯蔵庫から、それ以外の資源はインベントリから使われ、艦は着陸している必要があります。Velkonite Reinforced Plate、Orvium Reinforced Plate、Dark Matter Plate、Dark Matter、クレジット、Thulium は燃料にできません。Reinforced Hull Plate は燃料にできます。

<!-- research-fuel:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| 資源 | レアリティ | 使用元 | 1個あたりの科学 | 1時間に必要な数 |
| :--- | :--- | :--- | ---: | ---: |
| [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) | コモン | インベントリ | 5 | 720 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | コモン | インベントリ | 5 | 720 |
| [Daraxium](/wiki/06-Items/Resources.md#daraxium) | コモン | インベントリ | 7 | 515 |
| [Nyxite](/wiki/06-Items/Resources.md#nyxite) | コモン | インベントリ | 7 | 515 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | コモン | インベントリ | 8 | 450 |
| [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) | コモン | インベントリ | 33 | 110 |
| [Power Core](/wiki/06-Items/Resources.md#power-core) | アンコモン | インベントリ | 100 | 36 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | アンコモン | 資源貯蔵庫 | 210 | 18 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | レア | 資源貯蔵庫 | 321 | 12 |
| [Ancient Control Unit](/wiki/06-Items/Resources.md#ancient-control-unit) | レア | インベントリ | 650 | 6 |

最後の列は、ブーストなしで研究を1時間続けるのに必要な個数（切り上げ）です。ブーストありでは 2 倍必要です。

<!-- research-fuel:end -->

## Thulium ブースト {#the-thulium-boost}

<!-- research-boost:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **5,000 Thulium** でブーストを1つ買えます。研究センターは **24 時間、2 倍の速さで**研究します。
- 科学も **2 倍の速さで燃える**ので、ブーストが買うのは時間であって燃料ではありません。技術が燃やす科学は、ブーストの有無で変わりません。
- ブーストは買った瞬間に始まり、タンクに燃料があってもなくても時計どおりに進むので、研究が動いている間に買いましょう。何も研究していないときは、センターが購入を断ります。
- ブーストは重なります。別のブーストが動いている間にもう1つ買うと、その終わりが 24 時間延び、最大で 72 時間先まで積めます。ブーストは個々の研究ではなく、あなたの研究センターのものです。

研究の最初からブーストをかけたとき、研究時間がどうなるか：

| 研究時間 | ブースト時 | 全体に必要なブースト数 | Thulium |
| :--- | :--- | ---: | ---: |
| 30分 | 15分 | 1 | 5,000 |
| 3時間 | 1時間30分 | 1 | 5,000 |
| 6時間 | 3時間 | 1 | 5,000 |
| 10時間 | 5時間 | 1 | 5,000 |
| 1日 | 12時間 | 1 | 5,000 |
| 2日 | 1日 | 1 | 5,000 |

<!-- research-boost:end -->

## Dark Matter

技術ツリーの頂点にある技術には、Dark Matter も必要です。Dark Matter は[ブラックホール](/wiki/03-Mechanics/Black-Hole.md#dark-matter)から得られ、到達した N.I.K.E. ロケットが少量を残します。また、[Dormant の群れ](/wiki/05-Swarms/Dormant-Swarm.md)の Dormant Pulse からも、ときどき手に入ります。

<!-- research-dark-matter:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- 下の表の 16個の技術それぞれに、科学に加えて **10 個の Dark Matter** が必要です。開始前に研究センターへセットしてください（インベントリから、艦は着陸した状態で）。研究は開始時にそれを受け取ります。
- **ルール：** レアリティが エピック 以上で、研究に 10時間 以上かかるアイテム。Dark Matter を作るための N.I.K.E. には、これは決して必要ありません。
- **ドローン編成**はこのルールの対象外です。編成の研究はどれも Dark Matter を必要とし、強さに応じて 5、13、20 のいずれかです（表のとおり）。
- **船体装甲**もこのルールの対象外です。2つの研究はより多く必要とし、1日の研究で Dark Matter 25、2日の研究で 40 です（表のとおり）。
- **研究をキャンセルすると、**そのためにセットした Dark Matter はセンターに戻ります。進捗と、すでに燃やした科学は戻りません。
- すべて合わせて 414 個の Dark Matter が必要です。

| 技術 | レアリティ | 研究時間 | Dark Matter |
| :--- | :--- | :--- | ---: |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | エピック | 10時間 | 10 |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | エピック | 10時間 | 10 |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | エピック | 10時間 | 10 |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | エピック | 10時間 | 10 |
| [Starfire-III](/wiki/06-Items/Lasers.md#lasers) | ミシカル | 1日 | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | ミシカル | 1日 | 10 |
| [Damage Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | エピック | 10時間 | 10 |
| [Crit Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | エピック | 10時間 | 10 |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | エピック | 1日 | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | エピック | 1日 | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | ミシカル | 2日 | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | ミシカル | 1日 | 10 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | レジェンダリー | 1日 | 10 |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | エピック | 1日 | 10 |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | エピック | 1日 | 10 |
| [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | エピック | 10時間 | 5 |
| [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | エピック | 1日 | 13 |
| [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | エピック | 10時間 | 5 |
| [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | ミシカル | 2日 | 20 |
| [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | エピック | 10時間 | 5 |
| [Ballista Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | エピック | 1日 | 13 |
| [Stiletto Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | ミシカル | 2日 | 20 |
| [Rampart Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | ミシカル | 2日 | 20 |
| [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | エピック | 1日 | 13 |
| [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | エピック | 10時間 | 5 |
| [Culler Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | エピック | 1日 | 13 |
| [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | エピック | 1日 | 13 |
| [Auger Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | エピック | 1日 | 13 |
| [Cordon Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | エピック | 1日 | 13 |
| [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | エピック | 10時間 | 5 |
| [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | エピック | 1日 | 13 |
| [Penetration Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | エピック | 10時間 | 10 |
| [Hull Plating II](/wiki/06-Items/Hull-Plating.md#the-three-platings) | レア | 1日 | 25 |
| [Hull Plating III](/wiki/06-Items/Hull-Plating.md#the-three-platings) | エピック | 2日 | 40 |

<!-- research-dark-matter:end -->

## 技術ツリー {#the-technology-tree}

各ボックスは1つの技術です。名前の下に研究時間（時計）が、Dark Matter が必要なものには Dark Matter バッジが付きます。矢印は、ある技術から、それを必要とする技術へ向かいます。先に研究するのは矢印の元の技術です。矢印のないボックスはすぐに研究できます。ボックスにカーソルを合わせると、研究時間、燃やす科学、研究後にアセンブリが要求するものが表示され、クリックするとそのアイテムのページが開きます。ツリーはゲーム自身のデータから描いています。ツリーのうち **防衛** と **攻撃と機動** の2つには、16種類の[ドローン編成](/wiki/03-Mechanics/Formations.md)が入っています。

<!-- research-tree:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

### 推進装置と速度 {#tree-propulsion}

```tree research
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines

Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```

### シールドと防御 {#tree-shields}

```tree research
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cores

Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```

### レーザーと弾薬 {#tree-lasers}

```tree research
Quantum Laser III | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Quantum Laser II, 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-III | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser III, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-III, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Damage Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Crit Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Damage Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Damage Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Crit Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Crit Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Penetration Amp I, 20 Daraxium, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Penetration Amp II, 1 Power Core, 30 Nyxite, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp IV | laser-amp, epic | craft 1200 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Penetration Amp III, 1 Power Core, 30 Cataclysite, 40 Quorvium, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-

Quantum Laser III => Starfire-III => Helios Beam
Damage Amp II => Damage Amp III => Damage Amp IV
Crit Amp II => Crit Amp III => Crit Amp IV
Penetration Amp II => Penetration Amp III => Penetration Amp IV
```

### ブースター {#tree-boosters}

```tree research
Laser Damage Booster II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
```

### ドローン {#tree-drones}

```tree research
Master Drone | drone, rare | craft 40000 Thulium, 60 s | research 36000 s, 36000 science | 1 Slave Drone, 100 Ship Fragment | /wiki/06-Items/Drones.md#available-drones
```

### 艦船 {#tree-ships}

```tree research
Paragon | ship, rare | craft 1500 Thulium, 900 s | research 21600 s, 21600 science | 120 Ship Fragment, 20 Reinforced Hull Plate, 5 Power Core | /wiki/02-Ships/Paragon.md
Ironclad | ship, epic | craft 10500 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit | /wiki/02-Ships/Ironclad.md
Storm | ship, epic | craft 15000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit | /wiki/02-Ships/Storm.md
Wraith | ship, mythical | craft 20000 Thulium, 900 s | research 172800 s, 172800 science, 10 Dark Matter | 300 Ship Fragment, 50 Reinforced Hull Plate, 15 Power Core, 3 Ancient Control Unit | /wiki/02-Ships/Wraith.md
```

### 資源 {#tree-resources}

```tree research
Dark Matter Plate | resource, mythical | craft 250 Thulium, 120 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Velkonite Reinforced Plate, 1 Orvium Reinforced Plate, 5 Dark Matter | /wiki/06-Items/Resources.md#dark-matter-plate
```

### ロケット {#tree-rockets}

```tree research
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
```

### CPU {#tree-cpus}

```tree research
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 6 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 2 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Extras.md#base-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu

Extra Slots CPU I => Extra Slots CPU II => Extra Slots CPU III
Base CPU I => Base CPU II => Jump CPU
```

### 防衛 {#tree-defence}

```tree research
Testudo Formation | formation, epic | craft 7500 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Adamant Formation | formation, epic | craft 9000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Rampart Formation | formation, mythical | craft 38500 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Sanctum Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Redoubt Formation | formation, epic | craft 21000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Cordon Formation | formation, epic | craft 21500 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations

Testudo Formation => Sanctum Formation => Rampart Formation
Adamant Formation => Redoubt Formation => Cordon Formation
```

### 攻撃と機動 {#tree-strike-mobility}

```tree research
Bodkin Formation | formation, epic | craft 21000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Asterism Formation | formation, epic | craft 7000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Gemini Formation | formation, mythical | craft 38000 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Ballista Formation | formation, epic | craft 24000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Stiletto Formation | formation, mythical | craft 46000 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Shrike Formation | formation, epic | craft 8500 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Culler Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Auger Formation | formation, epic | craft 20500 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Centurion Formation | formation, epic | craft 8000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Gyre Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations

Asterism Formation => Bodkin Formation => Ballista Formation
Gemini Formation => Stiletto Formation
Centurion Formation => Shrike Formation => Culler Formation
Gyre Formation => Auger Formation
```

### 船体装甲 {#tree-hull-plating}

```tree research
Hull Plating II | hull-plating, rare | craft 2500 Thulium, 300 s | research 86400 s, 86400 science, 25 Dark Matter | 1 Hull Plating I, 150 Ship Fragment, 20 Reinforced Hull Plate, 6 Power Core, 5 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating III | hull-plating, epic | craft 4000 Thulium, 600 s | research 172800 s, 172800 science, 40 Dark Matter | 1 Hull Plating II, 300 Ship Fragment, 40 Reinforced Hull Plate, 12 Power Core, 1 Ancient Control Unit, 8 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings

Hull Plating II => Hull Plating III
```


<!-- research-tree:end -->

## 艦のデザインと装甲スロット {#ship-technologies}

Skylab の研究画面の「艦」ファミリーには、製作ではない技術が2種類あります。上のツリーには含まれていません。開くのがアイテムではなく、スロットか改造だからです。

- **装甲スロット。** アセンブリで製作する4隻の艦の[装甲スロット](/wiki/06-Items/Hull-Plating.md#hull-plate-slots)1つにつき、技術が1つあります。どれも前のものの次に進みます。最初のものは艦自身の技術の次です。ゲームでは、艦のスロットは1枚のカードにまとめられ、スロット1つにつき点が1つ付きます。
- **艦のデザイン。** [デザイン](/wiki/03-Mechanics/Ship-Designs.md)1つにつき、技術が1つあります。どれも艦の技術と Dark Matter Plate の技術が必要です。

それぞれの時間、Dark Matter、合計は[艦のデザイン](/wiki/03-Mechanics/Ship-Designs.md#the-technologies)のページにあります。

## すべての技術 {#all-the-technologies}

<!-- research-technologies:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| 技術 | 先に必要 | クラス | 研究時間 | 科学 | Dark Matter |
| :--- | :--- | :--- | ---: | ---: | ---: |
| [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30分 | 1,800 | – |
| [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3時間 | 10,800 | – |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10時間 | 36,000 | 10 |
| [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30分 | 1,800 | – |
| [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3時間 | 10,800 | – |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10時間 | 36,000 | 10 |
| [Engine III](/wiki/06-Items/Propulsion.md#engines) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | B | 3時間 | 10,800 | – |
| [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30分 | 1,800 | – |
| [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3時間 | 10,800 | – |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10時間 | 36,000 | 10 |
| [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30分 | 1,800 | – |
| [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3時間 | 10,800 | – |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10時間 | 36,000 | 10 |
| [Heavy Shield Core](/wiki/06-Items/Shields.md#shield-cores) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | B | 3時間 | 10,800 | – |
| [Quantum Laser III](/wiki/06-Items/Lasers.md#lasers) | – | B | 3時間 | 10,800 | – |
| [Starfire-III](/wiki/06-Items/Lasers.md#lasers) | [Quantum Laser III](/wiki/06-Items/Lasers.md#lasers) | D | 1日 | 86,400 | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Starfire-III](/wiki/06-Items/Lasers.md#lasers) | D | 1日 | 86,400 | 10 |
| [Damage Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Damage Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10時間 | 36,000 | 10 |
| [Crit Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Crit Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10時間 | 36,000 | 10 |
| [Laser Damage Booster II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3時間 | 10,800 | – |
| [Shield Wall Booster II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3時間 | 10,800 | – |
| [Hull Plating Booster II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3時間 | 10,800 | – |
| [Master Drone](/wiki/06-Items/Drones.md#available-drones) | – | C | 10時間 | 36,000 | – |
| [Paragon](/wiki/02-Ships/Paragon.md) | – | B | 6時間 | 21,600 | – |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | – | D | 1日 | 86,400 | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | – | D | 1日 | 86,400 | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | – | D | 2日 | 172,800 | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | – | D | 1日 | 86,400 | 10 |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | B | 3時間 | 10,800 | – |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | D | 1日 | 86,400 | 10 |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | – | A | 30分 | 1,800 | – |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | C | 10時間 | 36,000 | – |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | D | 1日 | 86,400 | 10 |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | – | B | 3時間 | 10,800 | – |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10時間 | 36,000 | – |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | D | 1日 | 86,400 | 10 |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | – | B | 6時間 | 21,600 | – |
| [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10時間 | 36,000 | 5 |
| [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1日 | 86,400 | 13 |
| [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10時間 | 36,000 | 5 |
| [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | D | 2日 | 172,800 | 20 |
| [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10時間 | 36,000 | 5 |
| [Ballista Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1日 | 86,400 | 13 |
| [Stiletto Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 2日 | 172,800 | 20 |
| [Rampart Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 2日 | 172,800 | 20 |
| [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1日 | 86,400 | 13 |
| [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | C | 10時間 | 36,000 | 5 |
| [Culler Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1日 | 86,400 | 13 |
| [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1日 | 86,400 | 13 |
| [Auger Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1日 | 86,400 | 13 |
| [Cordon Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1日 | 86,400 | 13 |
| [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10時間 | 36,000 | 5 |
| [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | D | 1日 | 86,400 | 13 |
| [Damage Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30分 | 1,800 | – |
| [Damage Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Damage Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3時間 | 10,800 | – |
| [Crit Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30分 | 1,800 | – |
| [Crit Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Crit Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3時間 | 10,800 | – |
| [Penetration Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30分 | 1,800 | – |
| [Penetration Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Penetration Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3時間 | 10,800 | – |
| [Penetration Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Penetration Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10時間 | 36,000 | 10 |
| [Hull Plating II](/wiki/06-Items/Hull-Plating.md#the-three-platings) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | D | 1日 | 86,400 | 25 |
| [Hull Plating III](/wiki/06-Items/Hull-Plating.md#the-three-platings) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Hull Plating II](/wiki/06-Items/Hull-Plating.md#the-three-platings) | D | 2日 | 172,800 | 40 |

研究時間によるクラス：

| クラス | 研究時間 | 技術数 | 順に研究した合計 | 科学 | Dark Matter |
| :--- | :--- | ---: | ---: | ---: | ---: |
| A | 30分 | 8 | 4時間 | 14,400 | 0 |
| B | 3時間～6時間 | 17 | 2日9時間 | 205,200 | 0 |
| C | 10時間 | 15 | 6日6時間 | 540,000 | 95 |
| D | 1日～2日 | 22 | 27日 | 2,332,800 | 319 |
| 合計 |  | 62 | 35日19時間 | 3,092,400 | 414 |

1つずつ順に研究すると、ツリー全体で 35日19時間 かかります。ブーストを常にかけると 17日21時間30分 で、ブースト 18 個と 90,000 Thulium になります。科学は同じです。

<!-- research-technologies:end -->

## CPU {#the-cpus}

新しい CPU もここで研究し、アセンブリで製作します。同じ表と注記は[エクストラ](/wiki/06-Items/Extras.md#research-cpus)のページにもあります。

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
