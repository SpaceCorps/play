<!-- wiki-i18n source: 7254affc4860b01c -->
<!-- wiki-i18n title: レーザー -->
# レーザーと弾薬 {#lasers-ammo}

<!-- wiki-search: arc amp; focus amp; pulse amp; prism amp; nova amp; apex amp; damage amp 1; crit amp 1; amps; penetration amp; shield penetration -->

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
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-3, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp I | laser-amp, shoddy | buy 10000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp I | laser-amp, shoddy | buy 15000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp I | laser-amp, shoddy | buy 15000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Damage Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Crit Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Penetration Amp I, 20 Daraxium, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Damage Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Crit Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Penetration Amp II, 1 Power Core, 30 Nyxite, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Damage Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Crit Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp IV | laser-amp, epic | craft 1200 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Penetration Amp III, 1 Power Core, 30 Cataclysite, 40 Quorvium, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Standard Battery | ammo, common | buy 10 Credits | /wiki/06-Items/Lasers.md#laser-ammunition
Siphon Battery | ammo, rare | buy 0.25 Thulium | /wiki/06-Items/Lasers.md#siphon-battery
Advanced Plasma | ammo, rare | buy 0.5 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Ultra Core | ammo, rare | buy 1 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Experimental Fusion Core | ammo, epic | buy 2.2 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition

Quantum Laser 1 -> Quantum Laser 2 -> Quantum Laser 3 => Starfire-3 => Helios Beam
Damage Amp I => Damage Amp II => Damage Amp III => Damage Amp IV
Crit Amp I => Crit Amp II => Crit Amp III => Crit Amp IV
Penetration Amp I => Penetration Amp II => Penetration Amp III => Penetration Amp IV
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

Quantum Laser 1 と 2 には、固有のクリティカル率がありません（「–」）。スロットに Damage Amp か Crit Amp を入れると、クリティカル率が得られます（Penetration Amp では得られません）。クリティカルヒットは、浮かび上がるダメージの数字では別の色で表示されます（氷のような水色で、より大きく、「!」が付きます。[ダメージと回復の数字](/wiki/03-Mechanics/Combat.md#damage-and-heal-numbers)を参照）。

### 上位3種のレーザーの製作 {#making-the-top-three-lasers}

**Quantum Laser 3**、**Starfire-3**、**Helios Beam** は、**アセンブリ**でのみ製作できます。Quantum Laser 3 はショップではもう販売されていませんが、すでに持っているパイロットはそのまま使えます。どのレシピも、[Skylab](/wiki/03-Mechanics/Skylab.md) の鍛造所で作るプレートを必要とし、Helios Beam はさらに Dark Matter Plate 3枚を必要とします。

| レーザー | 製作時間 | 必要なもの |
| :--- | :---: | :--- |
| Quantum Laser 3 | 1分 | Ship Fragment 10個、Velkonite Reinforced Plate 2枚、1,500 Thulium |
| Starfire-3 | 1分 | Quantum Laser 3 1基、Ship Fragment 15個、Velkonite Reinforced Plate 8枚、Reinforced Hull Plate 1枚、1,500 Thulium、100,000クレジット |
| Helios Beam | 3分 | Starfire-3 1基、Cataclysite 50個、Power Core 2個、Orvium Reinforced Plate 18枚、Dark Matter Plate 3枚、Reinforced Hull Plate 4枚、2,000 Thulium |

アセンブリのページには、所持しているものとレシピに必要なものが並べて表示され、「製作」ボタンには足りないものが表示されます。 レシピの画像や名前、またはその材料にカーソルを合わせると、アイテムの説明全文とステータスが表示されます。

**Starfire-3 は Quantum Laser 3 から作ります。**まず Quantum Laser 3 を作り、Starfire-3 はそれを消費します。Quantum Laser 3 がすでに使ったものは、改めて要求されません。そのため、2つを合わせたコストは、Starfire-3 が単独で要求していたものとちょうど同じで、3,000 Thulium、100,000クレジット、Ship Fragment 25個、Velkonite Reinforced Plate 10枚、Reinforced Hull Plate 1枚、そして2分です。すでに Quantum Laser 3 を持っているなら、支払うのは Starfire-3 自身の分だけです。ルールは、下の Helios Beam と同じです。Starfire-3 は、消費した Quantum Laser 3 のエンチャント段階を引き継ぎ（神級の Quantum Laser 3 からは神級の Starfire-3 ができます）、ボーナスは引き直されます。どの Quantum Laser 3 を使うかは選べ、標準より上の段階のものを使うときは、カードが先に確認します。Quantum Laser 3 は外れた状態でなければなりません。**先に艦から外し**（装着していたアンプはインベントリに戻ります）、トランスポートキャッシュからも取り出してください。艦に装備されているときは、「製作」ボタンに「先にQuantum Laser 3を外してください」と表示されます。

**Helios Beam は Starfire-3 から作ります。**まず Starfire-3 を作り（Quantum Laser 3 を含めて3,000 Thulium と100,000クレジット）、Helios Beam はそれを消費します。[Master Drone](/wiki/06-Items/Drones.md) が Slave Drone を消費するのと同じです。Starfire-3 がすでに使ったものは、改めて要求されません。そのため、2つを合わせたコストは、Helios Beam が単独で要求していた5,000 Thulium、Cataclysite、Power Core、Reinforced Hull Plate と、20枚ではなく18枚の Orvium プレート（Starfire-3 の Velkonite プレート10枚が、不足する2枚の代わりになります）、そして Helios Beam は系統の最終ティアなので Dark Matter Plate 3枚です。これ以外にかかるのは、Starfire-3 の100,000クレジットと Ship Fragment 25個です。ルールは[モジュールの強化](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)と同じです。Helios Beam は、消費した Starfire-3 のエンチャント段階を引き継ぎ（神級の Starfire-3 からは神級の Helios Beam ができます）、ボーナスは引き直されます。複数持っている場合はどの Starfire-3 を使うか選べ、標準より上の段階のものを使うときは、カードが先に確認します。Starfire-3 は外れた状態でなければなりません。**先に艦から外し**（装着していたアンプはインベントリに戻ります）、トランスポートキャッシュからも取り出してください。艦に装備されているときは、「製作」ボタンに「先にStarfire-3を外してください」と表示されます。

プレートの入手元：

- **Velkonite Reinforced Plate**（Quantum Laser 3 と Starfire-3）は Velkonite から鍛造され、鍛造所レベル1ではプレート1枚につき鉱石40個です。**Orvium Reinforced Plate**（Helios Beam）は Orvium から鍛造され、プレート1枚につき鉱石80個です。
- **Dark Matter Plate**（Helios Beam に3枚）は、レシピを研究したあと、アセンブリで Dark Matter 5個、Velkonite Reinforced Plate 1枚、Orvium Reinforced Plate 1枚、250 Thulium から圧縮して作ります。3枚で Dark Matter 15個、[ブラックホール](/wiki/03-Mechanics/Black-Hole.md)の N.I.K.E. ロケット平均7.5発分です。全体の流れは [Dark Matter と Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md) にあります。
- 鉱石は、Skylab のコレクターからのみ手に入ります。レベル5の Velkonite コレクターは1時間に18個の Velkonite を採掘するため、Quantum Laser 3 のプレートには約4時間分、Starfire-3 のプレート10枚（Quantum Laser 3 に2枚、自身の工程に8枚）には約22時間分の採掘が必要です。Helios Beam は長丁場です。18枚のプレートには Orvium 1,440個が必要で、レベル5の Orvium コレクターで約4日かかります。さらに、3枚の Dark Matter Plate に入る Orvium プレート3枚ぶんで Orvium 240個、約17時間が加わります。
- 資源貯蔵庫はレベル 1 で各鉱石を240個まで保管できます。鍛造所レベル 1 なら、Velkonite プレート6枚、または Orvium プレート3枚分です。そのため、こまめに鍛造する（鍛造所の1バッチは、レベル 1 で最大10枚）か、貯蔵庫をアップグレードしてください。
- 鍛造したプレートは、艦が着陸している間に回収するまで鍛造所で待機し、回収すると通常のアイテムとしてインベントリに入ります。

Ship Fragment、Cataclysite、Power Core、Reinforced Hull Plate はエイリアンからドロップします。各素材の入手元と使い道はすべて[資源](/wiki/06-Items/Resources.md)のページにあり、どれだけ出るかは、[Bulwark](/wiki/04-Aliens/Bulwark.md) と [Goombah](/wiki/04-Aliens/Goombah.md) のページのドロップ一覧で分かります。

---

## レーザーアンプ（アンプ） {#laser-amplifiers-amps-}

レーザーのスロットに直接装着して、その性能を高めます。系統は3つあり、それぞれ4段階で、シールドセルと同じように名付けられています。**Damage Amp** は固定値のダメージを加え、**Crit Amp** はクリティカル率と固定のクリティカルダメージを加え、**Penetration Amp** はターゲットの吸収率からポイントを差し引きます（[下記](#shield-penetration-of-a-laser-hit)）。これらは[ブースター](/wiki/06-Items/Boosters.md)ではありません。**Laser Damage Booster 1** と **Laser Damage Booster 2** は、装着するものがない時間制のブースター（10時間のあいだレーザーダメージ +10%）です。

| 名前 | レアリティ | 基本ダメージブースト | クリティカル率ブースト | 固定クリティカルダメージ | コスト |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Damage Amp I** | 粗悪 | +10 | +5% | +5 | 10,000クレジット |
| **Damage Amp II** | アンコモン | +16 | +5% | +8 | 製作専用 |
| **Damage Amp III** | レア | +26 | +6% | +13 | 製作専用 |
| **Damage Amp IV** | エピック | +38 | +7% | +20 | 製作専用 |
| **Crit Amp I** | 粗悪 | +0 | +15% | +0 | 15,000クレジット |
| **Crit Amp II** | アンコモン | +0 | +20% | +14 | 製作専用 |
| **Crit Amp III** | レア | +0 | +25% | +24 | 製作専用 |
| **Crit Amp IV** | エピック | +0 | +25% | +44 | 製作専用 |

| 名前 | レアリティ | シールド貫通 | コスト |
| :--- | :--- | :---: | :--- |
| **Penetration Amp I** | 粗悪 | +2% | 15,000クレジット |
| **Penetration Amp II** | アンコモン | +4% | 製作専用 |
| **Penetration Amp III** | レア | +6% | 製作専用 |
| **Penetration Amp IV** | エピック | +8% | 製作専用 |

**売られているのは各系統の最初のティアだけ**で、ショップで買えます。残りの3つは、[アセンブリ](/wiki/06-Items/Overview.md#upgrading-modules)で1つ下のティアのアンプから作ります。先に Skylab でその技術を研究しておく必要があります（[研究](/wiki/03-Mechanics/Research.md)）。各ステップには、Thulium、エイリアンのドロップ品、そしてプレート（ティアIIとIIIは Skylab で作る Velkonite Reinforced Plate、ティアIVは Dark Matter Plate 3枚）が必要で、新しいアンプは消費したアンプのエンチャント段階を引き継ぎ、ボーナスは引き直されます（[アセンブリでのモジュールの強化](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)）。Penetration のステップには結晶のレンズが加わります。ティアIVのアンプはどれも、各強化系統の最終ティアとして [Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md) を3枚要求するため、ティアIVのアンプの技術は、先にそのプレートの技術を必要とします。

| ステップ | Thulium | 所要時間 | 1つ下のティアのアンプに加えて |
| :--- | ---: | ---: | :--- |
| Damage Amp II / Crit Amp II | 250 | 60秒 | Cataclysite 10個、Velkonite Reinforced Plate 1枚 |
| Damage Amp III / Crit Amp III | 1,000 | 60秒 | Cataclysite 20個、Power Core 1個、Velkonite Reinforced Plate 2枚 |
| Damage Amp IV / Crit Amp IV | 1,200 | 60秒 | Cataclysite 30個、Power Core 1個、Dark Matter Plate 3枚 |
| Penetration Amp II | 250 | 60秒 | Daraxium 20個、Cataclysite 10個、Velkonite Reinforced Plate 1枚 |
| Penetration Amp III | 1,000 | 60秒 | Nyxite 30個、Cataclysite 20個、Power Core 1個、Velkonite Reinforced Plate 2枚 |
| Penetration Amp IV | 1,200 | 90秒 | Quorvium 40個、Cataclysite 30個、Power Core 1個、Dark Matter Plate 3枚 |

Helios Beam とティアIVのアンプ3つの組は、最終ティアの部品4つで、Dark Matter Plate 12枚、Dark Matter 60個、N.I.K.E. ロケット平均30発分です。すべてのスロットを最終ティアにした Wraith には Dark Matter 900個が入っています（[Dark Matter と Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md#what-the-last-tier-asks-for)）。

### どのアンプをどこに載せるか {#which-amp-goes-where}

ダメージアンプは、どのレーザーにも同じダメージを加えるため、**Quantum Laser 系**で最も価値があります。クリティカルアンプは、レーザーがすでに出しているダメージを増幅するので、レーザーの威力が高いほど価値が上がります。**Starfire-3** ではダメージ系と並び、**Helios Beam** ではダメージ系より約3.5%上回ります。レーザーのクリティカル率は100%で頭打ちです。Crit Amp III か Crit Amp IV を3個載せた Helios Beam は、ちょうど100%になります。Penetration Amp はダメージもクリティカル率も加えません。シールドが命中の大半を受け止めてしまう艦に対するものです（[下記](#when-is-a-penetration-amp-worth-a-slot)）。

同じアンプを載せた場合、レーザーは常に1つ下のレーザーより強くなります。そのため、良いアンプが良いレーザーの代わりになることはありません。Damage Amp IV を3個載せた Quantum Laser 3 のダメージは、Damage Amp I を3個載せた Helios Beam に及びません（同じエンチャント段階の部品で比べた場合です。神級以上まで鍛えた Quantum Laser 3 と Damage Amp IV が最高の値を引けば、Damage Amp I を載せた標準の Helios Beam を上回ることがあります。神級ではごくわずかな差です）。


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

**シールド貫通**は、斉射の各命中で、ターゲットの吸収率から差し引かれます。シールドが受けるのは、ターゲットの吸収率から貫通を引いた割合です（[シールドの仕組み](/wiki/03-Mechanics/Shields.md#shield-penetration)を参照）。Penetration Amp とドローン編成は弾薬の貫通に加わり、その合計の全体は[このページの下](#shield-penetration-of-a-laser-hit)にあります。吸収率80%（最高のシールドに最高のセル）の艦に対して、貫通10%の x4 弾薬を使うと、シールドが受ける割合は攻撃の70%、船体が受ける割合は30%になります。シールドに比べて船体が小さい艦に対して最も効果があり、吸収率80%の非常に大きな艦は、どちらの弾薬でも持ちこたえる程度は変わりません。エイリアンには語るほどの吸収率のステータスはなく（シールドが攻撃の80%を受けます）、貫通はそこからも差し引かれます。

### Siphon Battery

Siphon Battery は、船体を壊す代わりにシールドを奪うための弾薬です。**ターゲットのシールドに直接 x1 のダメージ**を与え、同じ量を**自分のシールド**に加えます（最大値まで）。ほかの弾薬と同じように、ホットバーの弾薬の選択画面で選びます（青緑の渦のタイルです）。ビームは出しません。細くかすかな青緑のプローブがターゲットへ飛び、当たった場所でターゲットのシールドが青緑に輝き、奪ったシールドは、光る青緑のパケット（3～10個、多く奪うほど多くなります）となって、約0.5秒かけて1つずつ、自分の艦へ流れ込む様子が見えます。パケットが届くたびに、自分のシールドが脈打ちます。視界内にいるどのパイロットの Siphon Battery でも、誰から奪う場合でも、同じ演出が見えます。相手がエイリアン、ほかのパイロット、企業パイロットの艦でも同じです。

- **シールドのみ**：船体には一切触れず、ターゲットの吸収率でダメージが分割されることもなく、Siphon Battery で何かを破壊することはできません。ダメージは、ターゲットのシールドに残っている量が上限です。
- **奪うものがない場合**：シールドが残っていないターゲットからは、何も奪えず、何も得られません。それでも、ほかの弾薬と同じようにレーザー1基につきバッテリー1個を消費し、斉射は行われます。見えるのはプローブと船体の鈍い明滅だけで、パケットは出ません。
- **獲得**：自分のシールドが最大値を超えることはなく、シールドを取り込んでも、自分のシールドのリチャージが遅れることはありません。
- **エイリアンもパイロットも**、奪えるシールドを持っています。エイリアンからシールドを奪うと、[最初の攻撃による権利](/wiki/03-Mechanics/Combat.md)の判定では命中として数えられますが、シールドが残っていなければ数えられません。また、反撃しかしない Seeker や Goombah も、ほかの命中と同じように目を覚まして反撃します。
- **クリティカルヒット**も有効です。クリティカルの斉射は1.5倍の量を奪い、その数字はクリティカルヒットとして表示されます。パケットはより大きく明るくなり、ターゲットのシールドもより強く輝きます。
- [企業パイロット](/wiki/03-Mechanics/Company-Pilots.md)は、標準の x1 弾薬を使います。

---

## レーザーの命中のシールド貫通 {#shield-penetration-of-a-laser-hit}

レーザーの命中はどれも、ターゲットの吸収率からポイントを差し引きます。差し引くものは最大3つあり、足し合わされます。あなたの**弾薬**（Ultra Core 5%、Experimental Fusion Core 10%）、あなたの **Penetration Amp**、そして**ドローン編成**（Gemini +9%、Stiletto +16%、[ドローン編成](/wiki/03-Mechanics/Formations.md)）です。合計は、レーザーでは**50%で頭打ち**、直撃ロケットでは40%で頭打ちです（[ロケット](/wiki/06-Items/Rockets.md)）。シールドは、ターゲットの吸収率から命中の貫通を引いた割合を受け、残りを船体が受けます（[シールドの仕組み](/wiki/03-Mechanics/Shields.md#shield-penetration)）。

- **アンプはレーザーの平均として数えられます。** 斉射は1回の命中なので、ゲームは各レーザーのアンプの貫通を足し合わせ（ドローンの中のレーザーも数えます）、クリティカル率と同じように、ダメージで重みを付けてレーザー全体の平均を取ります。各レーザーに Penetration Amp IV を3つずつ載せれば24%、12本のレーザーのうち1本に Penetration Amp IV を1つ載せても0.67%です。Wraith のレーザーは12本、アンプスロットは36個で、24%にするには36個すべてを埋める必要があります。
- **ハンガーに表示されます。** レーザーのアンプが貫通を与えるようになると、ハンガーの戦闘ステータスに数値付きの**貫通**タイルが現れます。弾薬と編成はそこに含まれません。
- **最強のレーザーはちょうど上限に届きます。** Experimental Fusion Core（10%）、Stiletto（16%）、各レーザーに Penetration Amp IV を3つ（24%）で、合計は50%です。
- **Penetration Amp IV への鍛冶場のボーナスは、その構成では無駄になります。** Penetration Amp も、ほかのアンプと同じように鍛造できます。ステータスは1つだけで、そのボーナスが貫通を倍化します。「永遠」のボーナス（+9%～+15%）なら、Penetration Amp IV は8ではなく8.7～9.2ポイントになります。しかし 10 + 16 + 24 でもう上限の50%に達しており、それを超えた分は切り捨てられます（「永遠」が3つなら合計は53.6%になり、50%に切られます）。

| レーザーの斉射 | 弾薬 | アンプ（3スロット） | 編成 | 合計 |
|---|---|---|---|---|
| Experimental Fusion Core のみ | 10% | – | – | **10%** |
| Fusion Core + Gemini | 10% | – | 9% | **19%** |
| Fusion Core + Stiletto（Penetration Amp 以前の最強） | 10% | – | 16% | **26%** |
| Fusion Core + 3 Penetration Amp I | 10% | 6% | – | **16%** |
| Fusion Core + 3 Penetration Amp II | 10% | 12% | – | **22%** |
| Fusion Core + 3 Penetration Amp III | 10% | 18% | – | **28%** |
| Fusion Core + 3 Penetration Amp IV | 10% | 24% | – | **34%** |
| Fusion Core + 3 Penetration Amp IV + Gemini | 10% | 24% | 9% | **43%** |
| Ultra Core + Penetration Amp IV 3つ + Stiletto（普段使いの最強） | 5% | 24% | 16% | **45%** |
| Fusion Core + Penetration Amp IV 3つ + Stiletto（最強のレーザー） | 10% | 24% | 16% | **50%** |

それがターゲットのシールドに何をするか。各マスは、命中のうち**シールドが受ける割合 / 船体が受ける割合**です。

| 防御側（吸収率） | アンプなし | Fusion Core のみ（10%） | 以前：Fusion Core + Stiletto（26%） | Fusion Core + 3 Penetration Amp IV（34%） | 最強のレーザー（50%） |
|---|---|---|---|---|---|
| Light Shield Core、セルなし（45%） | 45 / 55 | 35 / 65 | 19 / 81 | 11 / 89 | 0 / 100 |
| Heavy Shield Core、セルなし（50%） | 50 / 50 | 40 / 60 | 24 / 76 | 16 / 84 | 0 / 100 |
| Light Shield Core + Absorption Shield Cell IV（55%） | 55 / 45 | 45 / 55 | 29 / 71 | 21 / 79 | 5 / 95 |
| Heavy Shield Core + Capacity Shield Cell IV 3つ（65%） | 65 / 35 | 55 / 45 | 39 / 61 | 31 / 69 | 15 / 85 |
| 標準で最高のシールド（80%） | 80 / 20 | 70 / 30 | 54 / 46 | 46 / 54 | 30 / 70 |
| 最高のシールド、「永遠」の鍛冶場（最高の引き）とシーズンストア34レベル（95.4%） | 95 / 5 | 85 / 15 | 69 / 31 | 61 / 39 | 45 / 55 |
| 最高のシールド、「永遠」の鍛冶場（最高の引き）とシーズンストアの上限（102%） | 100 / 0 | 92 / 8 | 76 / 24 | 68 / 32 | 52 / 48 |
| どのエイリアンでも（80%） | 80 / 20 | 70 / 30 | 54 / 46 | 46 / 54 | 30 / 70 |

最強のレーザーは、セルのないシールドコアを空にします（船体が命中を丸ごと受けます）。セルのあるコアは命中の一部を保ち、最高のシールドは30%を保ちます（バフがあれば45%）。ロケットがシールドを空にすることはありません。上限は40%だからです。

### Penetration Amp は、スロットを使う価値がいつあるのか？ {#when-is-a-penetration-amp-worth-a-slot}

**Penetration Amp は、約95%を超える吸収率（シーズンストア、鍛冶場、Rampart の構成）に対抗します。標準で最高のシールド（80%）に対しては、同じティアの Crit Amp のほうが、なお約10%速く、Penetration Amp はエイリアンを、同じティアの Damage Amp や Crit Amp より速く倒すことはありません。**

- **ダメージは与えません。** Helios Beam では、Penetration Amp IV を3つ載せると1回の斉射で187ダメージ（弾薬x1、ダメージの振れ幅とクリティカルの平均）です。Damage Amp IV を3つなら356、Crit Amp IV を3つなら369で、およそ半分になります。取り戻すのはシールドの割合なので、シールドに比べて船体が小さく、吸収率が高い場合にだけ見合います。大きな船体がどのみち持ちこたえる Wraith や Ironclad に対しては、素朴な Damage か Crit の組み合わせのほうが速いです。
- **エイリアン。** そのシールドは命中の80%からあなたの貫通を引いた分を受けるので、エイリアンにも効きますが、同じティアの Damage Amp や Crit Amp のほうが、それでも速く倒せます。
- **コスト。** Penetration Amp IV 1つにつき Dark Matter Plate が3枚（Dark Matter 15個）必要です。ティアIVのアンプはどれも同じなので、36スロットすべてを埋める Wraith には、プレート108枚、Dark Matter 540個が必要です。
