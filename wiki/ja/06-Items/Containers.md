<!-- wiki-i18n source: 9cb279aeecb3bbc8 -->
<!-- wiki-i18n title: コンテナ -->
# コンテナ {#containers}

<!-- wiki-search: コンテナ; container; containers; case; crate; lootbox; loot box; ルートボックス; 確率; 排出率; 保証; 天井; pity; リール; 開封; 保管庫; るつぼ; アーカイブ; キャニスター; ラック; odds; drop rate; vault; crucible; archive; canister; rack -->

**コンテナ**は Mission Control の封印された発見物です。コンテナを開封すると、サーバーが表から報酬を1つ抽選します。その表のすべての報酬の確率は、このページに載っています。ゲームのコンテナのページにも同じ表が表示されます。

> [!NOTE]
> **コンテナはゲーム内で入手するランダムな報酬です。販売されることはなく、確率はここに公開されています。** コンテナは購入も取引も譲渡もできません。

## コンテナとは {#what-a-container-is}

- **入手するもの。** コンテナはゲーム内で入手します。価格もキーもありません。ショップでも、ほかのどこでも販売していません。
- **あなただけのもの。** コンテナはアカウントに紐づきます。取引したり、友人に渡したり、[オークション](/wiki/03-Mechanics/Auction.md)に出品したりはできません。コンテナから出たものも、そこに出品できません。
- **どのパイロットも同じ。** プレミアムでも何も変わりません。開封回数が増えることも、確率が良くなることもありません。
- **ワイプを越えて残ります。** 未開封のコンテナは、[ワイプ](/wiki/03-Mechanics/Wipe-Timeline.md)が来てもアカウントに残ります。ワイプで報酬がどうなるかは[ワイプ](#the-wipe)を見てください。
- **基地で開封します。** コンテナはドッキング中に、コンテナのページで開封します。報酬は「開封」を押した時点でサーバーが抽選し、押すこと自体は何も変えません。何が影響するかは[報酬の決まり方](#how-a-prize-is-chosen)にあります。

## コンテナの入手元 {#where-containers-come-from}

<!-- containers-sources:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

コンテナは次の方法で手に入ります。

- ゲームの管理者から
- ワイプ時のランク報酬として
- ログインカレンダーで
- 実績の報酬として

<!-- containers-sources:end -->

## 5種類のコンテナ {#the-five-containers}

<!-- containers-glance:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| コンテナ | 入っているもの | 向いている人 | ワイプ時の閉鎖 | 保証 | 最もレアな報酬 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **標本保管庫 (Specimen Vault)** | いろいろ少しずつ: クレジット、Thulium、弾薬、ロケット、装備、プレート、Dark Matter、ブースター、色 | どのパイロットも | シーズン 30 日目から | 10回の開封以内に レア 以上の等級の報酬 | 60,000 Thulium; 12,000,000 クレジット: それぞれ 0.100% |
| **鋳造所のるつぼ (Foundry Crucible)** | 弾薬、ロケット、レーザー、アンプ、シールドセル、スラスター、装備、そして艦5隻 | レベル 5 以上 | シーズン 30 日目から | 8回の開封以内に レア 以上の等級の報酬 | 艦: Wraith: 0.020% |
| **クロマ・アーカイブ (Chroma Archive)** | 外観のみ: スキン、色、排気エフェクト、オーラ | どのパイロットも | 開いたまま | 12回の開封以内に エピック 以上の等級の報酬 | Crystal Ice; Comet; Halo: それぞれ 0.667% |
| **調査キャニスター (Survey Canister)** | Skylab の鉱石、プレート、Dark Matter、Cluster Chunks、Thulium | Skylab のコア 10 以上 | シーズン 30 日目から | 8回の開封以内に レア 以上の等級の報酬 | 32 × Dark Matter Plate; 50,000 Thulium: それぞれ 0.150% |
| **試薬ラック (Reagent Rack)** | ブースター、EMP Charges、Energetic Walls、弾薬 | レベル 4 以上 | シーズン 30 日目から | 10回の開封以内に レア 以上の等級の報酬 | **フルスペクトラム**; Cloaking CPU L: それぞれ 0.100% |

<!-- containers-glance:end -->

**向いている人**は目安にすぎません。ゲームは、どのレベルでもどのコンテナも開封させてくれます。

## 等級 {#grades}

どの報酬にも**等級**があります。ゲームのレアリティの言葉のひとつです。等級は抽選で最初に決まります。リールでは報酬のタイルの枠になり、色と形で示されるので、色だけが目印になることはありません。

| 等級 | 色 | 形 |
| :--- | :--- | :--- |
| コモン | グレー | 円 |
| アンコモン | 緑 | 四角 |
| レア | 青 | ひし形 |
| エピック | 紫 | 六角形 |
| ミシカル | ピンク | 星 |
| レジェンダリー | 金 | 王冠 |

各コンテナには、等級ごとの確率が下に示されています。所持しているものによって、等級の確率が変わることはありません。

## 標本保管庫 (Specimen Vault) {#specimen-vault}

*Mission Control の異星文書係は、ひとつの分野に分類できない発見物をすべて番号付きの保管庫に封印し、未開封のまま送り出します。パイロットが封印を破るまで、保管庫に何が入っているかは基地の誰にも分かりません。*

### 等級ごとの確率 {#specimen-vault-grades}

<!-- containers-specimen-vault-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等級 | 確率 | 含まれる報酬 |
| :--- | ---: | ---: |
| コモン | 38.000% | 9 |
| アンコモン | 38.000% | 8 |
| レア | 17.000% | 8 |
| エピック | 5.500% | 5 |
| ミシカル | 1.300% | 4 |
| レジェンダリー | 0.200% | 2 |

<!-- containers-specimen-vault-grades:end -->

### すべての報酬 {#specimen-vault-prizes}

<!-- containers-specimen-vault-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等級 | 報酬 | 確率 |
| :--- | :--- | ---: |
| コモン | 50,000 クレジット | 5.000% |
| コモン | 250 Thulium | 4.000% |
| コモン | 10,000 × Standard Battery | 4.000% |
| コモン | 500 × Advanced Plasma | 4.000% |
| コモン | 250 × Ultra Core | 3.000% |
| コモン | **ロケットラック I**: 4種から1つを100個（確率は同じ）: Ember I, Lancet I, Rivet I, Scatter I | 6.000% |
| コモン | **鍛造の粉**: 1,500 × Daraxium + 1,500 × Nyxite | 3.000% |
| コモン | 4,000 × Ship Fragment | 3.000% |
| コモン | 1時間 Experience Booster | 6.000% |
| アンコモン | 150,000 クレジット | 6.000% |
| アンコモン | 750 Thulium | 6.000% |
| アンコモン | 750 × Ultra Core | 4.500% |
| アンコモン | 340 × Experimental Fusion Core | 4.000% |
| アンコモン | **ロケットラック II**: 4種から1つを190個（確率は同じ）: Ember II, Lancet II, Rivet II, Scatter II | 6.000% |
| アンコモン | 10 × Velkonite Reinforced Plate | 4.000% |
| アンコモン | 1時間 Laser Damage Booster I | 4.000% |
| アンコモン | **カラーサンプル**: 11種から1つ（確率は同じ）: Cobalt, Indigo, Violet, Magenta, Crimson, Ember, Sunset, Gold, Emerald, Jade, Teal | 3.500% |
| レア | 400,000 クレジット | 2.500% |
| レア | 2,000 Thulium | 2.500% |
| レア | 10 × Dark Matter | 1.500% |
| レア | **ロケットラック III**: 4種から1つを400個（確率は同じ）: Ember III, Lancet III, Rivet III, Scatter III | 2.000% |
| レア | 1,000 × Experimental Fusion Core | 1.500% |
| レア | 9 × Orvium Reinforced Plate | 1.500% |
| レア | 4時間 Laser Damage Booster I | 1.500% |
| レア | **ティア II のパーツ1つ**: 4種から1つ（確率は同じ）: Absorption Shield Cell II, Capacity Shield Cell II, Impulse Thruster II, Momentum Thruster II | 4.000% |
| エピック | 1,200,000 クレジット | 1.200% |
| エピック | 6,000 Thulium | 1.200% |
| エピック | 30 × Dark Matter | 0.900% |
| エピック | 26 × Orvium Reinforced Plate | 0.900% |
| エピック | **ティア III のパーツ1つ**: 5種から1つ（確率は同じ）: Absorption Shield Cell III, Capacity Shield Cell III, Impulse Thruster III, Momentum Thruster III, Starfire-III | 1.300% |
| ミシカル | 18,000 Thulium | 0.400% |
| ミシカル | 12 × Dark Matter Plate | 0.300% |
| ミシカル | Helios Beam | 0.300% |
| ミシカル | **ティア IV のアンプ1つ**: 3種から1つ（確率は同じ）: Damage Amp IV, Crit Amp IV, Penetration Amp IV | 0.300% |
| レジェンダリー | 60,000 Thulium | 0.100% |
| レジェンダリー | 12,000,000 クレジット | 0.100% |

<!-- containers-specimen-vault-prizes:end -->

**カラーサンプル**は、まだ持っていない色を1つ出します。サンプルの色をすべて持っている場合は、代わりに分解のThuliumが支払われます（[重複と分解](#duplicates-and-salvage)）。

### 保証 {#specimen-vault-guarantee}

<!-- containers-specimen-vault-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **保証**: 10回の開封ごとに少なくとも1回、レア 以上の等級の報酬
- **保証がない場合に レア 以上の等級の報酬が出る確率**: 24.000%
- **保証がある場合、多数回の開封での割合**: 25.649%
- **保証により確定する開封の割合**: 2.170%
- **そのような報酬と報酬の間の開封回数（平均）**: 3.899

<!-- containers-specimen-vault-guarantee:end -->

## 鋳造所のるつぼ (Foundry Crucible) {#foundry-crucible}

*Dormant の鋳造所は、最後のひと鋳込みがるつぼに残ったまま冷えていきました。弾薬、組み上がった装備、そして最も深い所には未完成の船体があります。Mission Control の技師たちが廃墟からるつぼを切り出し、封印されたままパイロットに渡します。どれに船体が入っているかは誰にも分からないからです。*

### 等級ごとの確率 {#foundry-crucible-grades}

<!-- containers-foundry-crucible-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等級 | 確率 | 含まれる報酬 |
| :--- | ---: | ---: |
| コモン | 45.000% | 6 |
| アンコモン | 30.000% | 7 |
| レア | 16.000% | 6 |
| エピック | 6.500% | 6 |
| ミシカル | 2.200% | 5 |
| レジェンダリー | 0.300% | 2 |

<!-- containers-foundry-crucible-grades:end -->

### すべての報酬 {#foundry-crucible-prizes}

<!-- containers-foundry-crucible-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等級 | 報酬 | 確率 |
| :--- | :--- | ---: |
| コモン | 30,000 × Standard Battery | 7.000% |
| コモン | 1,500 × Advanced Plasma | 7.000% |
| コモン | 750 × Ultra Core | 7.000% |
| コモン | 340 × Experimental Fusion Core | 5.000% |
| コモン | **ロケットラック I**: 4種から1つを300個（確率は同じ）: Ember I, Lancet I, Rivet I, Scatter I | 11.000% |
| コモン | **レーザーキット**: Quantum Laser II + Damage Amp I + Crit Amp I + Penetration Amp I | 8.000% |
| アンコモン | 2,250 × Ultra Core | 4.500% |
| アンコモン | 1,020 × Experimental Fusion Core | 4.500% |
| アンコモン | **ロケットラック II**: 4種から1つを560個（確率は同じ）: Ember II, Lancet II, Rivet II, Scatter II | 8.500% |
| アンコモン | Basic Shield Core | 4.500% |
| アンコモン | **ティア II のアンプ3点セット**: Damage Amp II + Crit Amp II + Penetration Amp II | 4.000% |
| アンコモン | Repair Drone IV | 3.900% |
| アンコモン | 艦: Nomad | 0.100% |
| レア | 1,800 × Experimental Fusion Core | 2.500% |
| レア | **ロケットラック III**: 4種から1つを500個（確率は同じ）: Ember III, Lancet III, Rivet III, Scatter III | 3.000% |
| レア | Quantum Laser III | 2.400% |
| レア | **ティア II のパーツ1つ**: 4種から1つ（確率は同じ）: Absorption Shield Cell II, Capacity Shield Cell II, Impulse Thruster II, Momentum Thruster II | 4.500% |
| レア | **ティア III のアンプ1つ**: 3種から1つ（確率は同じ）: Damage Amp III, Crit Amp III, Penetration Amp III | 3.500% |
| レア | 艦: Paragon | 0.100% |
| エピック | **ティア III のセルまたはスラスター1つ**: 4種から1つ（確率は同じ）: Absorption Shield Cell III, Capacity Shield Cell III, Impulse Thruster III, Momentum Thruster III | 3.000% |
| エピック | Starfire-III | 1.200% |
| エピック | Heavy Shield Core | 1.200% |
| エピック | Cloaking CPU M | 1.000% |
| エピック | 艦: Storm | 0.050% |
| エピック | 艦: Ironclad | 0.050% |
| ミシカル | Helios Beam | 0.600% |
| ミシカル | **ティア IV のセルまたはスラスター1つ**: 4種から1つ（確率は同じ）: Absorption Shield Cell IV, Capacity Shield Cell IV, Impulse Thruster IV, Momentum Thruster IV | 0.700% |
| ミシカル | **ティア IV のアンプ1つ**: 3種から1つ（確率は同じ）: Damage Amp IV, Crit Amp IV, Penetration Amp IV | 0.480% |
| ミシカル | Cloaking CPU L | 0.400% |
| ミシカル | 艦: Wraith | 0.020% |
| レジェンダリー | **ヘリオス武器庫**: Helios Beam + Damage Amp IV + Crit Amp IV + Penetration Amp IV | 0.150% |
| レジェンダリー | 50,000 Thulium | 0.150% |

<!-- containers-foundry-crucible-prizes:end -->

艦は基本確率とともに載っています。すでに所持している艦は出ないので、あなた自身の確率はこの表と少し違うことがあります。[艦](#the-ships)を見てください。

### 保証 {#foundry-crucible-guarantee}

<!-- containers-foundry-crucible-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **保証**: 8回の開封ごとに少なくとも1回、レア 以上の等級の報酬
- **保証がない場合に レア 以上の等級の報酬が出る確率**: 25.000%
- **保証がある場合、多数回の開封での割合**: 27.781%
- **保証により確定する開封の割合**: 3.708%
- **そのような報酬と報酬の間の開封回数（平均）**: 3.600

<!-- containers-foundry-crucible-guarantee:end -->

## クロマ・アーカイブ (Chroma Archive) {#chroma-archive}

*Dormant は紫がかった黒の結晶に紫の筋を通して建造し、記録係は色を薄いガラス板に保存しました。押し当てたものを塗り替える板です。クロマ・アーカイブは、その板を封印して積み重ねたもので、Mission Control の色彩係が索引を付け、パイロットが開くまで誰にも読まれません。*

クロマ・アーカイブは、まず等級を抽選し、次にその等級の中から、まだ持っていない外観を1つ抽選します。どの外観も確率は同じです。コレクションは1つの報酬で、持っていないスキンがすべて手に入ります。表の確率は、その等級の外観を1つも持っていないパイロットの場合の値です。集めるにつれて抽選に残る外観が減るため、確率は上がります。外観そのものについては[コスメティック](/wiki/06-Items/Cosmetics.md)を見てください。

### 等級ごとの確率 {#chroma-archive-grades}

<!-- containers-chroma-archive-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等級 | 確率 | 含まれる外観 |
| :--- | ---: | ---: |
| コモン | 6.000% | 1 |
| アンコモン | 50.000% | 14 |
| レア | 30.000% | 8 |
| エピック | 12.000% | 12 |
| ミシカル | 2.000% | 3 |
| レジェンダリー | 0.000% | – |

<!-- containers-chroma-archive-grades:end -->

### すべての報酬 {#chroma-archive-prizes}

<!-- containers-chroma-archive-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等級 | 外観 | その等級の外観を1つも持っていない場合の確率 |
| :--- | :--- | ---: |
| コモン | Glow（オーラ） | 6.000% |
| アンコモン | Company Supporter（コレクション） | 3.571% |
| アンコモン | Cobalt（色） | 3.571% |
| アンコモン | Indigo（色） | 3.571% |
| アンコモン | Violet（色） | 3.571% |
| アンコモン | Magenta（色） | 3.571% |
| アンコモン | Crimson（色） | 3.571% |
| アンコモン | Ember（色） | 3.571% |
| アンコモン | Sunset（色） | 3.571% |
| アンコモン | Gold（色） | 3.571% |
| アンコモン | Emerald（色） | 3.571% |
| アンコモン | Jade（色） | 3.571% |
| アンコモン | Teal（色） | 3.571% |
| アンコモン | Twin（排気エフェクト） | 3.571% |
| アンコモン | Breath（オーラ） | 3.571% |
| レア | Nature White（コレクション） | 3.750% |
| レア | Sunrise Orbit（コレクション） | 3.750% |
| レア | Seeker Burnt（色） | 3.750% |
| レア | Pirate Brick（色） | 3.750% |
| レア | Pulse（排気エフェクト） | 3.750% |
| レア | Helix（排気エフェクト） | 3.750% |
| レア | Motes（オーラ） | 3.750% |
| レア | Shimmer（オーラ） | 3.750% |
| エピック | Midnight Gala（コレクション） | 1.000% |
| エピック | Blue Marble（コレクション） | 1.000% |
| エピック | Mimosa（コレクション） | 1.000% |
| エピック | Olive Branch（コレクション） | 1.000% |
| エピック | Steady Pulse（コレクション） | 1.000% |
| エピック | Hollow Night（コレクション） | 1.000% |
| エピック | Dormant Void（色） | 1.000% |
| エピック | Ancient Amethyst（色） | 1.000% |
| エピック | Embers（排気エフェクト） | 1.000% |
| エピック | Gradient（排気エフェクト） | 1.000% |
| エピック | Sparkle（オーラ） | 1.000% |
| エピック | Wreath（オーラ） | 1.000% |
| ミシカル | Crystal Ice（色） | 0.667% |
| ミシカル | Comet（排気エフェクト） | 0.667% |
| ミシカル | Halo（オーラ） | 0.667% |

<!-- containers-chroma-archive-prizes:end -->

### 保証 {#chroma-archive-guarantee}

<!-- containers-chroma-archive-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **保証**: 12回の開封ごとに少なくとも1回、エピック 以上の等級の報酬
- **保証がない場合に エピック 以上の等級の報酬が出る確率**: 14.000%
- **保証がある場合、多数回の開封での割合**: 16.740%
- **保証により確定する開封の割合**: 3.186%
- **そのような報酬と報酬の間の開封回数（平均）**: 5.974

<!-- containers-chroma-archive-guarantee:end -->

## 調査キャニスター (Survey Canister) {#survey-canister}

*調査プローブは Skylab から宇宙マップの霧の中へ飛び立ち、それぞれがコアサンプルの封印キャニスターになって戻ってきます。誰も地図にしていない鉱脈の鉱石、異常現象、そして時にはマップより古い何かの欠片。Mission Control はキャニスターをセルごとに整理し、読み解きは Skylab の持ち主に任せます。*

### 等級ごとの確率 {#survey-canister-grades}

<!-- containers-survey-canister-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等級 | 確率 | 含まれる報酬 |
| :--- | ---: | ---: |
| コモン | 45.000% | 8 |
| アンコモン | 30.000% | 7 |
| レア | 16.000% | 6 |
| エピック | 6.500% | 5 |
| ミシカル | 2.200% | 3 |
| レジェンダリー | 0.300% | 2 |

<!-- containers-survey-canister-grades:end -->

### すべての報酬 {#survey-canister-prizes}

<!-- containers-survey-canister-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等級 | 報酬 | 確率 |
| :--- | :--- | ---: |
| コモン | 240 × Velkonite（Skylab へ） | 7.000% |
| コモン | 160 × Orvium（Skylab へ） | 7.000% |
| コモン | 1,300 × Reinforced Hull Plate | 5.000% |
| コモン | 9,000 × Ship Fragment | 6.000% |
| コモン | **鍛造クリスタル**: 4,000 × Cataclysite + 3,000 × Quorvium | 5.000% |
| コモン | 450 × Power Core | 5.000% |
| コモン | 450 Thulium | 5.000% |
| コモン | 4 × Regular Cluster Chunk | 5.000% |
| アンコモン | 780 × Velkonite（Skylab へ） | 5.000% |
| アンコモン | 510 × Orvium（Skylab へ） | 5.000% |
| アンコモン | 19 × Velkonite Reinforced Plate | 4.000% |
| アンコモン | 7 × Dark Matter | 5.000% |
| アンコモン | 8 × Ancient Control Unit | 3.000% |
| アンコモン | 1,450 Thulium | 4.000% |
| アンコモン | 3 × Mythical Cluster Chunk | 4.000% |
| レア | 17 × Dark Matter | 3.500% |
| レア | 15 × Orvium Reinforced Plate | 3.000% |
| レア | 1,900 × Velkonite（Skylab へ） | 2.500% |
| レア | 1,230 × Orvium（Skylab へ） | 2.500% |
| レア | 2 × Legendary Cluster Chunk | 1.500% |
| レア | 3,500 Thulium | 3.000% |
| エピック | 45 × Dark Matter | 1.500% |
| エピック | 39 × Orvium Reinforced Plate | 1.200% |
| エピック | **混合プレートの箱**: 60 × Velkonite Reinforced Plate + 20 × Orvium Reinforced Plate | 1.200% |
| エピック | 9,000 Thulium | 1.500% |
| エピック | 6 × Dark Matter Plate | 1.100% |
| ミシカル | 13 × Dark Matter Plate | 0.900% |
| ミシカル | 20,000 Thulium | 0.800% |
| ミシカル | 100 × Dark Matter | 0.500% |
| レジェンダリー | 32 × Dark Matter Plate | 0.150% |
| レジェンダリー | 50,000 Thulium | 0.150% |

<!-- containers-survey-canister-prizes:end -->

*（Skylab へ）*と書かれた鉱石は、リソースストレージの空きの範囲で、Skylab の鉱石バンクに入ります。残りは同じ鉱石としてインベントリに届きます。[Skylab](/wiki/03-Mechanics/Skylab.md)を見てください。

### 保証 {#survey-canister-guarantee}

<!-- containers-survey-canister-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **保証**: 8回の開封ごとに少なくとも1回、レア 以上の等級の報酬
- **保証がない場合に レア 以上の等級の報酬が出る確率**: 25.000%
- **保証がある場合、多数回の開封での割合**: 27.781%
- **保証により確定する開封の割合**: 3.708%
- **そのような報酬と報酬の間の開封回数（平均）**: 3.600

<!-- containers-survey-canister-guarantee:end -->

## 試薬ラック (Reagent Rack) {#reagent-rack}

*Skylab の研究センターは、試薬のアンプルから、飛ぶときに使うブースターを蒸留します。ラックは、ロットが途中で打ち切られたときに残るもので、各試薬の量を量った1回分が、それぞれ封印されたアンプルに入っています。量が劣化するのは艦が飛んでいる間だけなので、ラックは好きなだけ棚に置いておけます。*

### 等級ごとの確率 {#reagent-rack-grades}

<!-- containers-reagent-rack-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等級 | 確率 | 含まれる報酬 |
| :--- | ---: | ---: |
| コモン | 45.000% | 5 |
| アンコモン | 33.000% | 8 |
| レア | 15.000% | 8 |
| エピック | 5.500% | 6 |
| ミシカル | 1.300% | 2 |
| レジェンダリー | 0.200% | 2 |

<!-- containers-reagent-rack-grades:end -->

### すべての報酬 {#reagent-rack-prizes}

<!-- containers-reagent-rack-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等級 | 報酬 | 確率 |
| :--- | :--- | ---: |
| コモン | 1時間 Experience Booster | 11.000% |
| コモン | 1時間 Honor Booster | 11.000% |
| コモン | 1時間 Shield Regen Booster | 9.000% |
| コモン | Energetic Wall I | 8.000% |
| コモン | 500 × Advanced Plasma | 6.000% |
| アンコモン | 1時間 Laser Damage Booster I | 5.000% |
| アンコモン | 1時間 Shield Wall Booster I | 5.000% |
| アンコモン | 1時間 Hull Plating Booster I | 5.000% |
| アンコモン | 1時間 Resource Magnet Booster | 3.500% |
| アンコモン | 2時間 Experience Booster | 4.500% |
| アンコモン | 2時間 Honor Booster | 3.500% |
| アンコモン | EMP Charge | 3.500% |
| アンコモン | 3 × Energetic Wall I | 3.000% |
| レア | 2時間 Laser Damage Booster I | 2.500% |
| レア | 2時間 Shield Wall Booster I | 2.000% |
| レア | 2時間 Hull Plating Booster I | 2.000% |
| レア | 4時間 Experience Booster | 2.000% |
| レア | 4時間 Honor Booster | 2.000% |
| レア | 2時間 Loot Luck Booster | 1.500% |
| レア | 3 × EMP Charge | 2.000% |
| レア | 2時間 Resource Magnet Booster | 1.000% |
| エピック | 4時間 Laser Damage Booster I | 1.200% |
| エピック | 4時間 Shield Wall Booster I | 1.000% |
| エピック | 4時間 Hull Plating Booster I | 1.000% |
| エピック | 4時間 Resource Magnet Booster | 0.700% |
| エピック | 4時間 Loot Luck Booster | 0.900% |
| エピック | 8 × EMP Charge | 0.700% |
| ミシカル | **戦闘ラック**: 4時間 Laser Damage Booster I + 4時間 Shield Wall Booster I + 4時間 Hull Plating Booster I | 0.700% |
| ミシカル | **学者のラック**: 4時間 Experience Booster + 4時間 Honor Booster + 4時間 Resource Magnet Booster + 4時間 Loot Luck Booster | 0.600% |
| レジェンダリー | **フルスペクトラム**: 4時間 Laser Damage Booster I + 4時間 Shield Wall Booster I + 4時間 Hull Plating Booster I + 4時間 Shield Regen Booster + 4時間 Experience Booster + 4時間 Honor Booster + 4時間 Resource Magnet Booster + 4時間 Loot Luck Booster | 0.100% |
| レジェンダリー | Cloaking CPU L | 0.100% |

<!-- containers-reagent-rack-prizes:end -->

ブースターの時間は、すでに有効な同じブースターに加算され、飛行中だけ減っていきます。[ブースター](/wiki/06-Items/Boosters.md)を見てください。

### 保証 {#reagent-rack-guarantee}

<!-- containers-reagent-rack-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **保証**: 10回の開封ごとに少なくとも1回、レア 以上の等級の報酬
- **保証がない場合に レア 以上の等級の報酬が出る確率**: 22.000%
- **保証がある場合、多数回の開封での割合**: 24.001%
- **保証により確定する開封の割合**: 2.565%
- **そのような報酬と報酬の間の開封回数（平均）**: 4.167

<!-- containers-reagent-rack-guarantee:end -->

## 報酬の決まり方 {#how-a-prize-is-chosen}

コンテナを開封すると、サーバーが次の3段階で決めます。

1. **等級。** 乱数が1つ、等級の確率と照らし合わされます。
2. **報酬。** 2つ目の乱数が、その等級の報酬の確率と照らし合わされます。すでに所持している艦はそこに含まれません（[艦](#the-ships)を見てください）。
3. **同じ確率の中からの選択。** 「いくつかのうち1つ」とある報酬は、そのうち1つを出します。どれも確率は同じです。

数字はサーバーのオペレーティングシステムの乱数生成器から来て、コンテナが取り上げられたあとに抽選されます。あなたが送るものでは変えられません。ボタンも、時刻も関係ありません。

これまでのことのうち、2つは影響します。保証のカウンターは、ある開封から次の開封に引き継がれます。これは上の各コンテナの保証に書かれています。そして、すでに所持しているもの（前の開封で入手したものを含む）は、抽選に残る報酬を変えます。所持している艦は含まれず、所持している外観は、その等級にまだ持っていない外観が残っている間は抽選されません（[重複と分解](#duplicates-and-salvage)と[艦](#the-ships)を参照）。所持しているものによって等級の確率が変わることはありません。

<!-- containers-draw:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- どの確率も、100,000のうちの整数の部分です。1部分は 0.001% です。

<!-- containers-draw:end -->

**開封はすべて記録されます。** 記録には、サーバーが使ったシード（乱数）、引いた数字、抽選したテーブルのハッシュ、所持品によって抽選から外れた報酬が含まれます。コンテナのページの**履歴**にある**詳細**で読めます。

**自分で確認することもできます。** ゲームのソースにあるツール `scripts/containers-verify.py` は、テーブルと開封の詳細を読み、等級・報酬・選択がシードから導かれるかどうかを答えます。方法は短いものです。

```text
stream(seed, id): value i, for i = 0, 1, 2, ...
  = the first 8 bytes (big endian) of HMAC-SHA256(
      key     = seed,
      message = "sc-container-v1|" + id + "|" + i )
  where i is written as 4 bytes, big endian
below(n): take values until one is under 2^64 - (2^64 mod n),
  then use it modulo n (no modulo bias)
grade:    roll = below(total of the grades in play);
  the grade is the first whose running sum is above the roll
prize:    sub = below(total of the prizes left in that grade);
  the prize is the first whose running sum is above sub
choice:   a prize that is "one of N" gives the alternative
  number below(N)
seed = the 32 bytes shown under Details; id = the container's id.
When the guarantee forces an opening, only the guaranteed grade
and better are in play.
```

## 重複と分解 {#duplicates-and-salvage}

- 所持している**外観**は、その等級にまだ持っていない外観が残っている間は抽選されません。コレクションは、そのスキンをすべて持っているときに所持済みとみなされます。
- その等級の外観をすべて持っている場合は、代わりに**分解**が支払われます。等級ごとのThuliumです。保証では、その等級の報酬として数えられます。
- **アイテム**がThuliumに変わることはありません。スタックされるか、そのまま届きます。
- **艦**は二重に付与されることも、分解として支払われることもありません（[艦](#the-ships)を見てください）。

<!-- containers-salvage:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 等級 | Thulium |
| :--- | ---: |
| コモン | 25 |
| アンコモン | 100 |
| レア | 400 |
| エピック | 1,200 |
| ミシカル | 4,000 |

<!-- containers-salvage:end -->

## 艦 {#the-ships}

鋳造所のるつぼには艦が入っていることがあります。表には、どの艦も持っていないパイロットの確率である**基本確率**とともに艦が載っています。これが公開されている確率です。

すでに所持している艦は絶対に出ません。抽選から外され、その分は同じ等級のほかの報酬に、それぞれの確率に比例して回ります。つまり、所持しているものによって、あなた自身の確率は、その等級のほかの報酬で少し高くなります。等級の確率は変わらず、保証も変わりません。艦から作ったデザインは、その艦を所持しているものとして数えられます。Paragon THUNDER は Paragon を所持しているものとして数えられます。

<!-- containers-ships:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 艦 | 等級 | 確率 |
| :--- | :--- | ---: |
| Nomad | アンコモン | 0.100% |
| Paragon | レア | 0.100% |
| Storm | エピック | 0.050% |
| Ironclad | エピック | 0.050% |
| Wraith | ミシカル | 0.020% |
| **5隻すべて** | | **0.320%** |

例: 艦 Nomad を所持しているとします。アンコモンの等級の確率は変わりませんが、その等級の30,000部分のうち艦 Nomad の100部分が抽選から外れるので、アンコモンの等級のほかの報酬はそれぞれ 30,000 / 29,900 = 1.0033倍、表の確率より出やすくなります。

次の表は、その等級の艦をすべて所持している場合のものです。一部しか所持していなければ、その分の部分だけが抽選から外れるので、倍率はもっと小さくなります。

| 等級 | 等級の部分 | すべての艦の部分 | その等級のほかの報酬が出やすくなる倍率 |
| :--- | ---: | ---: | ---: |
| アンコモン | 30,000 | 100 | ×1.0033 |
| レア | 16,000 | 100 | ×1.0063 |
| エピック | 6,500 | 100 | ×1.0156 |
| ミシカル | 2,200 | 20 | ×1.0092 |

例: エピックの等級には艦が2隻あります。艦 Storm だけを所持している場合は、6,500部分のうち50部分だけが抽選から外れるので、エピックの等級のほかの報酬は 6,500 / 6,450 = 1.0078倍になり、1.0156倍にはなりません。

<!-- containers-ships:end -->

ゲームのコンテナのページは、公開値と違う場合に、あなた自身の確率を公開値の隣に表示します。所持している艦は、「この艦は所持しているため、コンテナからは出ません。」という行とともに、グレーで一覧に残ります。

## ワイプ {#the-wipe}

- **未開封のコンテナは残ります。** ワイプを越えてアカウントに残ります。
- **コンテナのアイテムは通常のアイテムです。** ワイプでは、トランスポートキャッシュに入れて持ち越さない限り失われます（[ワイプのタイムライン](/wiki/03-Mechanics/Wipe-Timeline.md)）。
- **外観と艦は手元に残ります。** ほかの外観や艦と同じです。クレジット、Thulium、ブースターの残り時間は、ワイプでそれぞれの規則に従います。
- **コンテナから出たものは、オークションに出品できません。**

<!-- containers-wipe:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **シーズン 30 日目から閉鎖**: 標本保管庫, 鋳造所のるつぼ, 調査キャニスター, 試薬ラック。中身がワイプで失われるため、ワイプが終わるまで開封できません。
- **バナー**: コンテナのページが、シーズン 28 日目から知らせます。
- **開いたまま**: クロマ・アーカイブ。外観だけを収めており、外観はワイプを越えて残ります。

<!-- containers-wipe:end -->

## テーブルのバージョン {#version-of-the-table}

このページのすべての確率は、ゲームのサーバーのテーブルのものです。確率が変わると、テーブルは新しいバージョンと新しいハッシュになり、開封のたびに、抽選したテーブルのハッシュが記録されます。

<!-- containers-version:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **テーブルのバージョン**: 1
- **テーブルのハッシュ（先頭12文字）**: `23aa20f1a5ad`

変更点:

- バージョン 1: 最初に公開されたテーブル。

<!-- containers-version:end -->
