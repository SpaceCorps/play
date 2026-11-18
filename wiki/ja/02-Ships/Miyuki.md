<!-- wiki-i18n source: 471213bf365fc9b9 -->
<!-- wiki-i18n title: Miyuki -->
# Miyuki

Miyuki は 5 つのレベルを持つサポート艦です。レベル I は他の艦と同じくアセンブリで製作し、その同じ艦をその場でレベル II、III、IV、V へと改造していきます。各レベルは 1 つ下のレベルから作られ、艦に装備したものはそのまま残ります。レベルが上がるごとにレーザースロットと装甲スロットが 1 つずつ増え、そのスロットはどれも研究が必要な技術です。

## ステータス {#stats}

- **ヒットポイント（HP）**：128,000
- **基本速度**：270
- **レーザースロット**：5
- **エクストラスロット**：3
- **装甲スロット**: 5

### ジェネレーターとサポートのスロット {#generator-support-slots}

- **コアスロット（効率 100%）**：3
- **サポートスロット（効率 75%）**：3
- **補助スロット（効率 50%）**：2

---

## 価格 {#price}

- **クレジット**：0（アセンブリで製造）
- **Thulium**：0

## レベル {#levels}

上のステータスはレベル I のものです。最初のレベルより上のレベルは、アセンブリで 1 つ下のレベルの Miyuki から製作します。同じ艦をその場で改造するので、装備や構成はそのまま残ります。レベルを飛ばしたり、購入したりすることはできません。

| レベル | 船体 | 基本速度 | レーザー | 装甲 | コア / サポート / 補助 | シールド容量 | シールド吸収率 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Miyuki** | 128,000 | 270 | 5 | 5 | 3 / 3 / 2 | – | – |
| **Miyuki II** | 134,400 | 270 | 6 | 6 | 3 / 3 / 2 | +5% | +2% |
| **Miyuki III** | 141,120 | 270 | 7 | 7 | 3 / 3 / 2 | +10.25% | +4.04% |
| **Miyuki IV** | 148,176 | 320 | 8 | 8 | 3 / 3 / 2 | +15.76% | +6.12% |
| **Miyuki V** | 155,585 | 320 | 9 | 9 | 4 / 4 / 4 | +21.55% | +8.24% |

シールド容量とシールド吸収率は、レベル I に対するボーナスです。

アセンブリで各レベルに必要なものです（1 つ下のレベルの Miyuki は新しいレベルに改造されます）。

| レベル | 研究 | 製作時間 | Thulium | 素材 |
| :--- | :--- | ---: | ---: | :--- |
| **Miyuki** | 1日、Dark Matter 10個 | 15分 | 6,000 | 160 Ship Fragment、25 Reinforced Hull Plate、10 Power Core、1 Ancient Control Unit |
| **Miyuki II** | 1日、Dark Matter 10個 | 10分 | 20,000 | 80 Ship Fragment、8 Reinforced Hull Plate、4 Power Core、8 Dark Matter Plate |
| **Miyuki III** | 1日、Dark Matter 10個 | 10分 | 35,000 | 120 Ship Fragment、10 Reinforced Hull Plate、6 Power Core、1 Ancient Control Unit、8 Dark Matter Plate |
| **Miyuki IV** | 2日、Dark Matter 10個 | 15分 | 50,000 | 180 Ship Fragment、18 Reinforced Hull Plate、9 Power Core、2 Ancient Control Unit、8 Dark Matter Plate |
| **Miyuki V** | 2日、Dark Matter 10個 | 15分 | 75,000 | 240 Ship Fragment、25 Reinforced Hull Plate、12 Power Core、3 Ancient Control Unit、8 Dark Matter Plate |

## アビリティ {#abilities}

Miyuki のアビリティはアイテムではなく艦に属します。アビリティスロットは使わず、装備も必要ありません。それぞれの働きは[艦のアビリティ](/wiki/03-Mechanics/Abilities.md#ship-abilities)に、各レベルが持つものはこの表にあります。

| レベル | Heal Pod | Channel Heal | Channel Shield |
| :--- | :--- | :--- | :--- |
| **Miyuki** | 7.5秒、20,000 + 2% | – | – |
| **Miyuki II** | 7.5秒、20,000 + 2% | 毎秒50,000の船体（あなたは10,000）、120秒 | – |
| **Miyuki III** | 7.5秒、30,000 + 3% | 毎秒50,000の船体（あなたは10,000）、120秒 | 毎秒150,000 + 3%のシールド（あなたは30,000 + 3%）、120秒 |
| **Miyuki IV** | 7.5秒、30,000 + 3% | 毎秒75,000の船体（あなたは10,000）、100秒 | 毎秒150,000 + 4%のシールド（あなたは30,000 + 4%）、120秒 |
| **Miyuki V** | 7.5秒、30,000 + 3% | 毎秒75,000の船体（あなたは10,000）、100秒 | 毎秒150,000 + 5%のシールド（あなたは30,000 + 5%）、80秒 |

リンクは5秒続き、グループまたは企業の艦に1,200ユニット以内で届きます。Heal Pod は600まで届きます。Channel Shield は点数に加えて、毎秒、双方の艦の最大シールドの一部も回復します。Miyuki III は3%、IV は4%、V は5%です（表の割合）。

## 研究 {#research}

- **レベル。** Miyuki II～V は Skylab の独立した技術で、それぞれ 1 つ下のレベルの先にあります。II と III は 1日、IV と V は 2日、いずれも Dark Matter 10個 が必要です。研究ビューでは5つのレベルが縦に並び、各レベルから次のレベルへ矢印が伸びます。II は I の後、III は II の後、IV は III の後、V は IV の後に研究します。
- **スロット。** 装甲スロット、6 番目以降のレーザースロット、9 番目以降のジェネレータースロットは、それぞれ Skylab の独立した技術で、1時間と Dark Matter 10個 が必要です。装甲スロットは 1～9 を最初のものから順に、レーザースロットは 6～9（それぞれのレベルの先）、ジェネレータースロットは 9～12（それぞれレベル V の先）です。スロットは研究するとすぐに、艦のレベルに関係なく開きます。まだ研究していないスロットは、ハンガーでロックされた状態で表示されます。
- **装甲スロット。** Miyuki には、[船体装甲](/wiki/06-Items/Hull-Plating.md)用の[装甲スロット](/wiki/06-Items/Hull-Plating.md#hull-plate-slots)がレベル I で 5 つ、レベル V で 9 つあり、製作した時点ではすべてロックされています。9 つすべてを Hull Plating III で埋めると、船体が 225,000 増えます。

<!-- research-ship:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **先に研究。** アセンブリでこの艦を製作できるのは、その技術を研究したあとです。研究時間は 1日 で、研究センターにセットする Dark Matter が 10 個必要です。[研究](/wiki/03-Mechanics/Research.md)ページの[艦船のツリー](/wiki/03-Mechanics/Research.md#tree-ships)にその技術があります。
- **エクストラスロットの追加。** Skylab に導入された Extra Slots CPU I・II・III は、この艦のエクストラスロットを 3、5、7 増やします。艦がもともと持つ 3 を足すと、合計は 6、8、10 です。ほかのアイテムと同じように研究して製作します。詳しくは [Extra Slots CPUs](/wiki/06-Items/Extras.md#extra-slots-cpus) を参照してください。

<!-- research-ship:end -->

## 伝承 {#lore}

Miyuki は、Skylab の造船所である問いから生まれました。艦隊を支える艦が、それを操縦するパイロットとともに成長できたらどうだろうか、と。改造のたびに装備と構成はそのまま残り、あらゆる面が少しずつ強くなります。Miyuki V は、パイロットが初日に出撃させたあの艦が、旗艦の大きさにまで成長した姿です。
