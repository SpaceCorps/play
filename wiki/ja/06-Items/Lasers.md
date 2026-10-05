<!-- wiki-i18n source: 3d97a6f4bd324d8d -->
<!-- wiki-i18n title: レーザー -->
# レーザーと弾薬 {#lasers-ammo}

武器は、SpaceCorps でダメージを与える主な手段です。

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## アイテムツリー {#item-tree}

アセンブリで作れるものは、先にその技術が必要です。アイテムにカーソルを合わせると、研究にかかる時間が分かります。技術ツリー、燃料、ブーストは [研究](/wiki/03-Mechanics/Research.md) を参照してください。

```tree
Quantum Laser 1 | laser, shoddy | buy 8000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser 2 | laser, common | buy 80000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser 3 | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-3 | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser 3, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-3, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp 1 | laser-amp, shoddy | buy 10000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp 1 | laser-amp, shoddy | buy 15000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Arc Amp | laser-amp, uncommon | buy 60000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Focus Amp | laser-amp, uncommon | buy 60000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Pulse Amp | laser-amp, rare | buy 1500 Thulium | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Prism Amp | laser-amp, rare | buy 1500 Thulium | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Nova Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Pulse Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Apex Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Prism Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Standard Battery | ammo, common | buy 10 Credits | /wiki/06-Items/Lasers.md#laser-ammunition
Siphon Battery | ammo, rare | buy 0.25 Thulium | /wiki/06-Items/Lasers.md#siphon-battery
Advanced Plasma | ammo, rare | buy 0.5 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Ultra Core | ammo, rare | buy 1 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Experimental Fusion Core | ammo, epic | buy 2.2 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition

Quantum Laser 1 -> Quantum Laser 2 -> Quantum Laser 3 => Starfire-3 => Helios Beam
Damage Amp 1 -> Arc Amp -> Pulse Amp => Nova Amp
Crit Amp 1 -> Focus Amp -> Prism Amp => Apex Amp
Standard Battery -> Advanced Plasma -> Ultra Core -> Experimental Fusion Core
```
<!-- item-tree:end -->

## レーザー {#lasers}

レーザーは、艦のレーザースロットに直接装備するか、ドローンに装備して、攻撃力を高めます。

| 名前 | レアリティ | 基本ダメージ | クリティカル率 | 射程 | アンプスロット | コスト |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Quantum Laser 1** | 粗悪 | 55 | – | 600 | 1 | 8,000クレジット |
| **Quantum Laser 2** | コモン | 65 | – | 700 | 2 | 80,000クレジット |
| **Quantum Laser 3** | レア | 80 | 10% | 800 | 3 | 製作専用 |
| **Starfire-3** | ミシカル | 135 | 15% | 850 | 3 | 製作専用 |
| **Helios Beam** | ミシカル | 185 | 25% | 900 | 3 | 製作専用 |

射程の列は、各レーザー自身の射程です。**艦は、搭載しているレーザーの射程の平均で射撃します**（ドローンのレーザーも数えます）。平均はユニット単位で四捨五入され、ターゲットがその距離の内側に入ると、すべてのレーザーが撃ちます。Starfire-3 1基と Quantum Laser 2 を2基載せた艦の射程は、850ではなく750になります。Starfire-3 を3基載せれば850のままで、同じレーザーだけなら何も変わりません。鍛冶場の射程ボーナスは、平均を取る前に、そのレーザー自身に反映されます。レーザーがないとハンガーには射程が表示されず（ダッシュになります）、レーザーは射撃できませんが、ロケットは撃てます。ロケットにはそれぞれ固有の射程があります（[ロケット](/wiki/06-Items/Rockets.md)を参照）。ハンガーでは、レーザーの射程が異なる場合、タイルに「平均射程」と表示され、カーソルを合わせると各レーザーの射程が一覧で表示されます。

Quantum Laser 1 と 2 には、固有のクリティカル率がありません（「–」）。スロットにダメージアンプかクリティカルアンプを入れると、クリティカル率が得られます。クリティカルヒットは、浮かび上がるダメージの数字では別の色で表示されます（氷のような水色で、より大きく、「!」が付きます）。

### 上位3種のレーザーの製作 {#making-the-top-three-lasers}

**Quantum Laser 3**、**Starfire-3**、**Helios Beam** は、**アセンブリ**でのみ製作できます。Quantum Laser 3 はショップではもう販売されていませんが、すでに持っているパイロットはそのまま使えます。どのレシピも、[Skylab](/wiki/03-Mechanics/Skylab.md) の鍛造所で作るプレートを必要とします。

| レーザー | 製作時間 | 必要なもの |
| :--- | :---: | :--- |
| Quantum Laser 3 | 1分 | Ship Fragment 10個、Velkonite Reinforced Plate 2枚、1,500 Thulium |
| Starfire-3 | 1分 | Quantum Laser 3 1基、Ship Fragment 15個、Velkonite Reinforced Plate 8枚、Reinforced Hull Plate 1枚、1,500 Thulium、100,000クレジット |
| Helios Beam | 3分 | Starfire-3 1基、Cataclysite 50個、Power Core 2個、Orvium Reinforced Plate 18枚、Reinforced Hull Plate 4枚、2,000 Thulium |

アセンブリのページには、所持しているものとレシピに必要なものが並べて表示され、「製作」ボタンには足りないものが表示されます。 レシピの画像や名前、またはその材料にカーソルを合わせると、アイテムの説明全文とステータスが表示されます。

**Starfire-3 は Quantum Laser 3 から作ります。**まず Quantum Laser 3 を作り、Starfire-3 はそれを消費します。Quantum Laser 3 がすでに使ったものは、改めて要求されません。そのため、2つを合わせたコストは、Starfire-3 が単独で要求していたものとちょうど同じで、3,000 Thulium、100,000クレジット、Ship Fragment 25個、Velkonite Reinforced Plate 10枚、Reinforced Hull Plate 1枚、そして2分です。すでに Quantum Laser 3 を持っているなら、支払うのは Starfire-3 自身の分だけです。ルールは、下の Helios Beam と同じです。Starfire-3 は、消費した Quantum Laser 3 のエンチャント段階を引き継ぎ（神級の Quantum Laser 3 からは神級の Starfire-3 ができます）、ボーナスは引き直されます。どの Quantum Laser 3 を使うかは選べ、標準より上の段階のものを使うときは、カードが先に確認します。Quantum Laser 3 は外れた状態でなければなりません。**先に艦から外し**（装着していたアンプはインベントリに戻ります）、トランスポートキャッシュからも取り出してください。艦に装備されているときは、「製作」ボタンに「先にQuantum Laser 3を外してください」と表示されます。

**Helios Beam は Starfire-3 から作ります。**まず Starfire-3 を作り（Quantum Laser 3 を含めて3,000 Thulium と100,000クレジット）、Helios Beam はそれを消費します。[Master Drone](/wiki/06-Items/Drones.md) が Slave Drone を消費するのと同じです。Starfire-3 がすでに使ったものは、改めて要求されません。そのため、2つを合わせたコストは、Helios Beam が単独で要求していた5,000 Thulium、Cataclysite、Power Core、Reinforced Hull Plate と、20枚ではなく18枚の Orvium プレート（Starfire-3 の Velkonite プレート10枚が、不足する2枚の代わりになります）です。これ以外にかかるのは、Starfire-3 の100,000クレジットと Ship Fragment 25個です。ルールは[モジュールの強化](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)と同じです。Helios Beam は、消費した Starfire-3 のエンチャント段階を引き継ぎ（神級の Starfire-3 からは神級の Helios Beam ができます）、ボーナスは引き直されます。複数持っている場合はどの Starfire-3 を使うか選べ、標準より上の段階のものを使うときは、カードが先に確認します。Starfire-3 は外れた状態でなければなりません。**先に艦から外し**（装着していたアンプはインベントリに戻ります）、トランスポートキャッシュからも取り出してください。艦に装備されているときは、「製作」ボタンに「先にStarfire-3を外してください」と表示されます。

プレートの入手元：

- **Velkonite Reinforced Plate**（Quantum Laser 3 と Starfire-3）は Velkonite から鍛造され、鍛造所レベル1ではプレート1枚につき鉱石40個です。**Orvium Reinforced Plate**（Helios Beam）は Orvium から鍛造され、プレート1枚につき鉱石80個です。
- 鉱石は、Skylab のコレクターからのみ手に入ります。レベル5の Velkonite コレクターは1時間に18個の Velkonite を採掘するため、Quantum Laser 3 のプレートには約4時間分、Starfire-3 のプレート10枚（Quantum Laser 3 に2枚、自身の工程に8枚）には約22時間分の採掘が必要です。Helios Beam は長丁場です。18枚のプレートには Orvium 1,440個が必要で、レベル5の Orvium コレクターで約4日かかります。
- 資源貯蔵庫はレベル 1 で各鉱石を240個まで保管できます。鍛造所レベル 1 なら、Velkonite プレート6枚、または Orvium プレート3枚分です。そのため、こまめに鍛造する（鍛造所の1バッチは、レベル 1 で最大10枚）か、貯蔵庫をアップグレードしてください。
- 鍛造したプレートは、艦が着陸している間に回収するまで鍛造所で待機し、回収すると通常のアイテムとしてインベントリに入ります。

Ship Fragment、Cataclysite、Power Core、Reinforced Hull Plate はエイリアンからドロップします。各素材の入手元と使い道はすべて[資源](/wiki/06-Items/Resources.md)のページにあり、どれだけ出るかは、[Bulwark](/wiki/04-Aliens/Bulwark.md) と [Goombah](/wiki/04-Aliens/Goombah.md) のページのドロップ一覧で分かります。

---

## レーザーアンプ（アンプ） {#laser-amplifiers-amps-}

レーザーのスロットに直接装着して、その性能を高めます。系統は2つあり、それぞれ4段階です。**ダメージ系**は固定値のダメージを加え、**クリティカル系**はクリティカル率と固定のクリティカルダメージを加えます。

| 名前 | レアリティ | 基本ダメージブースト | クリティカル率ブースト | 固定クリティカルダメージ | コスト |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Damage Amp 1** | 粗悪 | +10 | +5% | +5 | 10,000クレジット |
| **Arc Amp** | アンコモン | +16 | +5% | +8 | 60,000クレジット |
| **Pulse Amp** | レア | +26 | +6% | +13 | 1,500 Thulium |
| **Nova Amp** | エピック | +38 | +7% | +20 | 製作専用 |
| **Crit Amp 1** | 粗悪 | +0 | +15% | +0 | 15,000クレジット |
| **Focus Amp** | アンコモン | +0 | +20% | +14 | 60,000クレジット |
| **Prism Amp** | レア | +0 | +25% | +24 | 1,500 Thulium |
| **Apex Amp** | エピック | +0 | +25% | +44 | 製作専用 |

Nova Amp と Apex Amp は、[アセンブリ](/wiki/06-Items/Overview.md#upgrading-modules)で、それぞれ Pulse Amp と Prism Amp から作ります。Thulium、ドロップ品、そして Skylab で作る Velkonite Reinforced Plate 3枚が、それぞれ必要です。消費したアンプのエンチャント段階は引き継がれ、ボーナスは引き直されます（[アセンブリでの部品の強化](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)）。

### どのアンプをどこに載せるか {#which-amp-goes-where}

ダメージアンプは、どのレーザーにも同じダメージを加えるため、**Quantum Laser 系**で最も価値があります。クリティカルアンプは、レーザーがすでに出しているダメージを増幅するので、レーザーの威力が高いほど価値が上がります。**Starfire-3** ではダメージ系と並び、**Helios Beam** ではダメージ系より約3.5%上回ります。レーザーのクリティカル率は100%で頭打ちです。Prism Amp か Apex Amp を3個載せた Helios Beam は、ちょうど100%になります。

同じアンプを載せた場合、レーザーは常に1つ下のレーザーより強くなります。そのため、良いアンプが良いレーザーの代わりになることはありません。Nova Amp を3個載せた Quantum Laser 3 のダメージは、Damage Amp 1 を3個載せた Helios Beam に及びません（同じエンチャント段階の部品で比べた場合です。神級以上まで鍛えた Quantum Laser 3 と Nova Amp が最高の値を引けば、Damage Amp 1 を載せた標準の Helios Beam を上回ることがあります。神級ではごくわずかな差です）。

---

## レーザー弾薬 {#laser-ammunition}

レーザーの斉射のダメージを倍化させる、消耗品のバッテリーです。

| 名前 | レアリティ | ダメージ倍率 | シールド貫通 | 1個あたりの価格 |
| :--- | :--- | :---: | :---: | :--- |
| **Standard Battery** | コモン | 1.0倍 | – | 10クレジット |
| **Advanced Plasma** | レア | 2.0倍 | – | 0.5 Thulium |
| **Ultra Core** | レア | 3.0倍 | 5% | 1.0 Thulium |
| **Experimental Fusion Core** | エピック | 4.0倍 | 10% | 2.2 Thulium |
| **Siphon Battery** | レア | 1.0倍（シールドのみ） | – | 0.25 Thulium |

**シールド貫通**は、斉射の各命中で、ターゲットの吸収率から差し引かれます。シールドが受けるのは、ターゲットの吸収率から貫通を引いた割合です（[シールドの仕組み](/wiki/03-Mechanics/Shields.md#shield-penetration)を参照）。吸収率80%（最高のシールドに最高のセル）の艦に対して、貫通10%の x4 弾薬を使うと、シールドが受ける割合は攻撃の70%、船体が受ける割合は30%になります。シールドに比べて船体が小さい艦に対して最も効果があり、吸収率80%の非常に大きな艦は、どちらの弾薬でも持ちこたえる程度は変わりません。エイリアンには語るほどの吸収率のステータスはなく（シールドが攻撃の80%を受けます）、貫通はそこからも差し引かれます。

### Siphon Battery

Siphon Battery は、船体を壊す代わりにシールドを奪うための弾薬です。**ターゲットのシールドに直接 x1 のダメージ**を与え、同じ量を**自分のシールド**に加えます（最大値まで）。ほかの弾薬と同じように、ホットバーの弾薬の選択画面で選びます（青緑の渦のタイルです）。ビームは出しません。細くかすかな青緑のプローブがターゲットへ飛び、当たった場所でターゲットのシールドが青緑に輝き、奪ったシールドは、光る青緑のパケット（3～10個、多く奪うほど多くなります）となって、約0.5秒かけて1つずつ、自分の艦へ流れ込む様子が見えます。パケットが届くたびに、自分のシールドが脈打ちます。視界内にいるどのパイロットの Siphon Battery でも、誰から奪う場合でも、同じ演出が見えます。相手がエイリアン、ほかのパイロット、企業パイロットの艦でも同じです。

- **シールドのみ**：船体には一切触れず、ターゲットの吸収率でダメージが分割されることもなく、Siphon Battery で何かを破壊することはできません。ダメージは、ターゲットのシールドに残っている量が上限です。
- **奪うものがない場合**：シールドが残っていないターゲットからは、何も奪えず、何も得られません。それでも、ほかの弾薬と同じようにレーザー1基につきバッテリー1個を消費し、斉射は行われます。見えるのはプローブと船体の鈍い明滅だけで、パケットは出ません。
- **獲得**：自分のシールドが最大値を超えることはなく、シールドを取り込んでも、自分のシールドのリチャージが遅れることはありません。
- **エイリアンもパイロットも**、奪えるシールドを持っています。エイリアンからシールドを奪うと、[最初の攻撃による権利](/wiki/03-Mechanics/Combat.md)の判定では命中として数えられますが、シールドが残っていなければ数えられません。また、反撃しかしない Seeker や Goombah も、ほかの命中と同じように目を覚まして反撃します。
- **クリティカルヒット**も有効です。クリティカルの斉射は1.5倍の量を奪い、その数字はクリティカルヒットとして表示されます。パケットはより大きく明るくなり、ターゲットのシールドもより強く輝きます。
- [企業パイロット](/wiki/03-Mechanics/Company-Pilots.md)は、標準の x1 弾薬を使います。
