<!-- wiki-i18n source: 630505c843ae163b -->
<!-- wiki-i18n title: 부스터 -->
# 부스터 {#boosters}

<!-- wiki-search: damage amp; damage amp ii; shield wall; shield wall ii; hull plating; hull plating ii; shield regen; experience kit; honor beacon; resource magnet; loot luck -->

부스터는 일정 시간 동안 능력치를 바꿔 주어, 함선의 전투와 방어, 레벨업, 자원 수집 능력을 끌어올립니다.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## 아이템 트리 {#item-tree}

어셈블리에서 만드는 것은 먼저 해당 기술이 필요합니다. 아이템에 마우스를 올리면 연구에 걸리는 시간을 볼 수 있습니다. 기술 트리, 연료, 부스트는 [연구](/wiki/03-Mechanics/Research.md)에 있습니다.

```tree
Experience Booster | booster, common | buy 8000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Honor Booster | booster, common | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Laser Damage Booster 2 | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster 2 | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster 2 | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Regen Booster | booster, rare | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster 1 | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster 1 | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Resource Magnet Booster | booster, rare | buy 18000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Laser Damage Booster 1 | booster, rare | buy 20000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Loot Luck Booster | booster, legendary | buy 30000 Thulium | /wiki/06-Items/Boosters.md#active-boosters

Shield Wall Booster 1 -> Shield Wall Booster 2
Hull Plating Booster 1 -> Hull Plating Booster 2
Laser Damage Booster 1 -> Laser Damage Booster 2
```
<!-- item-tree:end -->

## 중첩 규칙 {#stacking-rules}

부스터는 합산 방식으로 계산됩니다.
1. **보너스 퍼센트는 합산됩니다**: 레이저 피해량 +10%를 주는 서로 다른 부스터 2개를 구매하면, 보너스는 총 **레이저 피해량 +20%**가 됩니다.
2. **지속 시간은 곱셈 방식으로 중첩됩니다**: _같은_ 부스터를 여러 번 구매하면 활성 지속 시간이 늘어납니다. _서로 다른_ 부스터의 타이머는 동시에 흐릅니다.
3. **타이머 보기**: 활성 부스터는 HUD의 부스터 창에 표시되며, 그룹별로 합산한 활성 보너스 총합과 다음 만료 시점을 보여 줍니다.

---

## 활성 부스터 {#active-boosters}

모든 부스터의 기본 지속 시간은 **10시간**이며, 구매하거나 받거나 수령하는 즉시 활성화됩니다. **2단계** 부스터 세 가지(Laser Damage Booster 2, Shield Wall Booster 2, Hull Plating Booster 2)는 판매하지 않습니다. Skylab에서 기술을 연구한 뒤([연구](/wiki/03-Mechanics/Research.md)) 어셈블리에서 제작하며, 수령하면 구매할 때와 같이 곧바로 10시간이 시작됩니다.

| 이름 | 희귀도 | 기본 효과 (10시간) | 가격 (Thulium) |
| :--- | :--- | :--- | :--- |
| **Laser Damage Booster 1** | 희귀 | 레이저 피해량 +10% | 20,000 |
| **Laser Damage Booster 2** | 희귀 | 레이저 피해량 +10% | 어셈블리: 20,000 |
| **Shield Wall Booster 1** | 희귀 | 실드 용량 +25% (최대 실드 포인트) | 15,000 |
| **Shield Wall Booster 2** | 희귀 | 실드 용량 +25% (최대 실드 포인트) | 어셈블리: 15,000 |
| **Hull Plating Booster 1** | 희귀 | 최대 내구도 +10% | 15,000 |
| **Hull Plating Booster 2** | 희귀 | 최대 내구도 +10% | 어셈블리: 15,000 |
| **Shield Regen Booster** | 희귀 | 실드 재충전 속도 +25% (초당 회복되는 실드 포인트) | 10,000 |
| **Experience Booster** | 일반 | 경험치 획득량 +20% | 8,000 |
| **Honor Booster** | 일반 | 명예 포인트 획득량 +20% | 10,000 |
| **Resource Magnet Booster** | 희귀 | 화물 상자 획득량 +25% | 18,000 |
| **Loot Luck Booster** | 전설 | NPC에게서 얻는 희귀 드롭 확률 +5% | 30,000 |

> [!NOTE]
> **부스터인가, 증폭기인가?** 서로 다른 것입니다. 모든 부스터는 이름에 **Booster**가 들어 있고, 타이머로 작동하며, 끼울 것이 없습니다. **Laser Damage Booster 1**과 **Laser Damage Booster 2**는 10시간 동안 레이저 피해량 +10%를 주며, 상점이나 어셈블리에서 얻습니다. **Damage Amp**, **Crit Amp**, **Penetration Amp**(티어 I~IV)는 레이저 증폭기입니다. 레이저의 증폭기 슬롯에 끼우는 모듈이며, 타이머가 없습니다([레이저와 탄약](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-)). 0.4.12 이전에는 부스터의 이름이 Damage Amp와 Damage Amp II, Shield Wall과 Shield Wall II, Hull Plating과 Hull Plating II, Shield Regen, Experience Kit, Honor Beacon, Resource Magnet, Loot Luck이었습니다. 작동 중이던 부스터는 새 이름으로 계속 이어졌습니다.

---

## 실드 부스트 세 종류 {#shield-boosts-three-kinds}

실드에는 서로 다른 능력치가 세 가지 있으며, 실드 부스트는 그중 정확히 하나만 올립니다. 부스터 창은 이 셋을 구분해, 각각 아이콘과 합계를 보여 줍니다.

| 종류 | 설명 | 올려 주는 부스트 |
| :--- | :--- | :--- |
| **실드 용량** | 최대 실드 포인트 | Shield Wall Booster 1, Shield Wall Booster 2, 영구 **Shield Capacity Boost**(시즌 상점) |
| **실드 흡수율** | 공격마다 실드가 받는 몫(나머지는 선체가 받습니다). 100%를 넘을 수 있습니다 | 영구 **Shield Absorbance Boost**(시즌 상점): 레벨당 +0.1포인트(25 WP), 최대 +10포인트. 이를 올려 주는 부스터는 없습니다 |
| **실드 재충전** | 초당 회복되는 실드 포인트 | Shield Regen Booster. 이를 올려 주는 영구 버프는 없습니다 |

같은 종류의 부스트끼리는 합산되며, 다른 종류에는 절대 반영되지 않습니다. 영구 버프는 [시즌 간 성장](/wiki/03-Mechanics/Wipe-Timeline.md)에서, 능력치 자체는 [실드 시스템](/wiki/03-Mechanics/Shields.md)에서 설명합니다.
