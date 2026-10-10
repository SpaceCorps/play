<!-- wiki-i18n source: 6227a03e20405285 -->
<!-- wiki-i18n title: ブースター -->
# ブースター {#boosters}

<!-- wiki-search: damage amp; damage amp ii; shield wall; shield wall ii; hull plating; hull plating ii; shield regen; experience kit; honor beacon; resource magnet; loot luck -->

ブースターは、艦のステータスを一時的に変化させ、戦闘、防御、レベル上げ、資源の収集を強化します。

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## アイテムツリー {#item-tree}

アセンブリで作れるものは、先にその技術が必要です。アイテムにカーソルを合わせると、研究にかかる時間が分かります。技術ツリー、燃料、ブーストは [研究](/wiki/03-Mechanics/Research.md) を参照してください。

```tree
Experience Booster | booster, common | buy 8000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Honor Booster | booster, common | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Laser Damage Booster II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Regen Booster | booster, rare | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster I | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster I | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Resource Magnet Booster | booster, rare | buy 18000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Laser Damage Booster I | booster, rare | buy 20000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Loot Luck Booster | booster, legendary | buy 30000 Thulium | /wiki/06-Items/Boosters.md#active-boosters

Shield Wall Booster I -> Shield Wall Booster II
Hull Plating Booster I -> Hull Plating Booster II
Laser Damage Booster I -> Laser Damage Booster II
```
<!-- item-tree:end -->

## 重ねがけのルール {#stacking-rules}

ブースターは加算方式で効果が重なります。
1. **ボーナスの割合は加算されます**：レーザーダメージ +10% のブースターを2種類購入した場合、合計で**レーザーダメージ +20%**のボーナスを受けられます。
2. **持続時間は乗算で重なります**：*同じ*ブースターを複数回購入すると、有効時間が延長されます。*別の*ブースターのタイマーは並行して進みます。
3. **タイマー表示**：有効なブースターは HUD のブースターウィンドウに表示され、種類ごとにまとめた有効ボーナスの合計と、次に期限が切れるタイミングを確認できます。
4. **数値には含まれます**：ハンガーのダメージ、シールド、シールド回復、吸収率、速度、船体、そしてパイロットのページには、有効なブースター、シーズンストアのバフ、クランのブーストが含まれ、戦闘ステータスのカードの小さな「ブースター込み」の表示がそれを示します。貫通、クリティカル率、射程はブースターでは変わりません。

---

## 有効なブースター {#active-boosters}

すべてのブースターの基本持続時間は**10時間**で、購入、受け取り、または回収と同時にすぐ有効になります。**2段階目**の3つのブースター（Laser Damage Booster II、Shield Wall Booster II、Hull Plating Booster II）は販売されていません。Skylab でその技術を研究し（[研究](/wiki/03-Mechanics/Research.md)）、アセンブリで製作します。製作したものを回収すると、購入したときと同じようにすぐ10時間が始まります。

| 名前 | レアリティ | 基本効果（10時間） | 価格（Thulium） |
| :--- | :--- | :--- | :--- |
| **Laser Damage Booster I** | レア | レーザーダメージ +10% | 20,000 |
| **Laser Damage Booster II** | レア | レーザーダメージ +10% | アセンブリ：20,000 |
| **Shield Wall Booster I** | レア | シールド容量 +25%（最大シールドポイント） | 15,000 |
| **Shield Wall Booster II** | レア | シールド容量 +25%（最大シールドポイント） | アセンブリ：15,000 |
| **Hull Plating Booster I** | レア | 最大 HP +10% | 15,000 |
| **Hull Plating Booster II** | レア | 最大 HP +10% | アセンブリ：15,000 |
| **Shield Regen Booster** | レア | シールドリチャージ速度 +25%（1秒あたりに回復するシールドポイント） | 10,000 |
| **Experience Booster** | コモン | 経験値の獲得量 +20% | 8,000 |
| **Honor Booster** | コモン | 名誉ポイントの獲得量 +20% | 10,000 |
| **Resource Magnet Booster** | レア | 積荷コンテナの獲得量 +25% | 18,000 |
| **Loot Luck Booster** | レジェンダリー | NPC からのレアドロップ率 +5% | 30,000 |

> [!NOTE]
> **ブースターか、アンプか？** 別のものです。すべてのブースターは名前に **Booster** が付き、タイマーで動き、装着するものはありません。**Laser Damage Booster I** と **Laser Damage Booster II** は、10時間のあいだレーザーダメージ +10% で、ショップかアセンブリで手に入ります。**Damage Amp**、**Crit Amp**、**Penetration Amp**（ティアI～IV）はレーザーアンプです。レーザーのアンプスロットに装着するモジュールで、タイマーはありません（[レーザーと弾薬](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-)）。0.4.12 より前、ブースターの名前は Damage Amp と Damage Amp II、Shield Wall と Shield Wall II、Hull Plating と Hull Plating II、Shield Regen、Experience Kit、Honor Beacon、Resource Magnet、Loot Luck でした。作動中のブースターは、新しい名前のまま続いています。Hull Plating **Booster** は、艦の装甲スロットに入る装甲 **Hull Plating** とは別のものです（[船体装甲](/wiki/06-Items/Hull-Plating.md#hull-plating-or-booster)）。

---

## シールドブーストの3種類 {#shield-boosts-three-kinds}

シールドには3つの別々のステータスがあり、シールドブーストはどれも、そのうちちょうど1つだけを上げます。ブースターウィンドウでは、この3つをアイコンと合計つきで分けて表示します。

| 種類 | 内容 | 上げるブースト |
| :--- | :--- | :--- |
| **シールド容量** | 最大シールドポイント | Shield Wall Booster I、Shield Wall Booster II、永続バフ **Shield Capacity Boost**（シーズンストア） |
| **シールド吸収率** | 各攻撃のうちシールドが受ける割合（残りは船体に当たります）。100%を超えることもあります | 永続バフ **Shield Absorbance Boost**（シーズンストア）：1レベルにつき +0.1ポイント（25 WP）、最大 +10ポイント。ブースターでは上がりません |
| **シールドリチャージ** | 1秒あたりに回復するシールドポイント | Shield Regen Booster。永続バフでは上がりません |

同じ種類のブーストは合算され、別の種類には加算されません。永続バフについては[シーズンをまたぐ成長](/wiki/03-Mechanics/Wipe-Timeline.md)、ステータス自体については[シールドの仕組み](/wiki/03-Mechanics/Shields.md)をご覧ください。
