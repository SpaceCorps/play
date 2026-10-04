<!-- wiki-i18n source: 539575474f5854de -->
<!-- wiki-i18n title: ブースター -->
# ブースター {#boosters}

ブースターは、艦のステータスを一時的に変化させ、戦闘、防御、レベル上げ、資源の収集を強化します。

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## アイテムツリー {#item-tree}

アセンブリで作れるものは、先にその技術が必要です。アイテムにカーソルを合わせると、研究にかかる時間が分かります。技術ツリー、燃料、ブーストは [研究](/wiki/03-Mechanics/Research.md) を参照してください。

```tree
Experience Kit | booster, common | buy 8000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Honor Beacon | booster, common | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Damage Amp II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Regen | booster, rare | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Resource Magnet | booster, rare | buy 18000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Damage Amp | booster, rare | buy 20000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Loot Luck | booster, legendary | buy 30000 Thulium | /wiki/06-Items/Boosters.md#active-boosters

Shield Wall -> Shield Wall II
Hull Plating -> Hull Plating II
Damage Amp -> Damage Amp II
```
<!-- item-tree:end -->

## 重ねがけのルール {#stacking-rules}

ブースターは加算方式で効果が重なります。
1. **ボーナスの割合は加算されます**：レーザーダメージ +10% のブースターを2種類購入した場合、合計で**レーザーダメージ +20%**のボーナスを受けられます。
2. **持続時間は乗算で重なります**：*同じ*ブースターを複数回購入すると、有効時間が延長されます。*別の*ブースターのタイマーは並行して進みます。
3. **タイマー表示**：有効なブースターは HUD のブースターウィンドウに表示され、種類ごとにまとめた有効ボーナスの合計と、次に期限が切れるタイミングを確認できます。

---

## 有効なブースター {#active-boosters}

すべてのブースターの基本持続時間は**10時間**で、購入、受け取り、または回収と同時にすぐ有効になります。3つの**II**ブースターは販売されていません。Skylab でその技術を研究し（[研究](/wiki/03-Mechanics/Research.md)）、アセンブリで製作します。製作したものを回収すると、購入したときと同じようにすぐ10時間が始まります。

| 名前 | レアリティ | 基本効果（10時間） | 価格（Thulium） |
| :--- | :--- | :--- | :--- |
| **Damage Amp** | レア | レーザーダメージ +10% | 20,000 |
| **Damage Amp II** | レア | レーザーダメージ +10% | アセンブリ：20,000 |
| **Shield Wall** | レア | シールド容量 +25%（最大シールドポイント） | 15,000 |
| **Shield Wall II** | レア | シールド容量 +25%（最大シールドポイント） | アセンブリ：15,000 |
| **Hull Plating** | レア | 最大 HP +10% | 15,000 |
| **Hull Plating II** | レア | 最大 HP +10% | アセンブリ：15,000 |
| **Shield Regen** | レア | シールドリチャージ速度 +25%（1秒あたりに回復するシールドポイント） | 10,000 |
| **Experience Kit** | コモン | 経験値の獲得量 +20% | 8,000 |
| **Honor Beacon** | コモン | 名誉ポイントの獲得量 +20% | 10,000 |
| **Resource Magnet** | レア | 積荷コンテナの獲得量 +25% | 18,000 |
| **Loot Luck** | レジェンダリー | NPC からのレアドロップ率 +5% | 30,000 |

---

## シールドブーストの3種類 {#shield-boosts-three-kinds}

シールドには3つの別々のステータスがあり、シールドブーストはどれも、そのうちちょうど1つだけを上げます。ブースターウィンドウでは、この3つをアイコンと合計つきで分けて表示します。

| 種類 | 内容 | 上げるブースト |
| :--- | :--- | :--- |
| **シールド容量** | 最大シールドポイント | Shield Wall、Shield Wall II、永続バフ **Shield Capacity Boost**（シーズンストア） |
| **シールド吸収率** | 各攻撃のうちシールドが受ける割合（残りは船体に当たります）。100%を超えることもあります | 永続バフ **Shield Absorbance Boost**（シーズンストア）：1レベルにつき +0.1ポイント（25 WP）、最大 +10ポイント。ブースターでは上がりません |
| **シールドリチャージ** | 1秒あたりに回復するシールドポイント | Shield Regen。永続バフでは上がりません |

同じ種類のブーストは合算され、別の種類には加算されません。永続バフについては[シーズンをまたぐ成長](/wiki/03-Mechanics/Wipe-Timeline.md)、ステータス自体については[シールドの仕組み](/wiki/03-Mechanics/Shields.md)をご覧ください。
