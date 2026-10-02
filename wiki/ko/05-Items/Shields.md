<!-- wiki-i18n source: 301d58f06f810979 -->
<!-- wiki-i18n title: 실드 -->
# 실드와 방어 {#shields-defense}

방어 모듈은 실드 용량을 제공하고, 피해를 흡수하며, 방어력을 재충전합니다.

## 실드 코어 {#shield-cores}

실드 코어를 함선의 발전기 슬롯이나 [드론](/wiki/03-Mechanics/Drones.md)에 장착하면(드론의 슬롯은 코어 슬롯으로 취급됩니다) 능동 방어막이 생성됩니다. 무거운 실드는 속도를 떨어뜨린다는 점에 유의하세요. **능력 슬롯**에 넣은 실드 코어는 대신 특수 효과 열의 **Shield Surge**를 제공합니다. Shield Surge는 10초에 걸쳐 실드를 회복시키며, 실드 코어 자체의 실드는 더해 주지 않습니다([능력](/wiki/03-Mechanics/Abilities.md) 참고).

| 이름 | 희귀도 | 용량 | 재충전 속도 | 흡수율 | 실드 % | 속도 % | 실드 셀 슬롯 | 특수 효과 | 비용 |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Light Shield Core** | 하급 | 10,000 | 333/초 | 45% | +5% | -1% | 1 | Shield Surge I | 20,000 크레딧 |
| **Basic Shield Core** | 일반 | 15,000 | 500/초 | 48% | +10% | -3% | 2 | Shield Surge II | 2,000 Thulium |
| **Heavy Shield Core** | 희귀 | 25,000 | 833/초 | 50% | +20% | -5% | 3 | Shield Surge III | 제작 전용 |

**Heavy Shield Core**는 [어셈블리](/wiki/05-Items/Overview.md#upgrading-modules)에서 Basic Shield Core를 재료로, 2,000 Thulium, Cataclysite 20개, Reinforced Hull Plate 8개, 그리고 Skylab에서 만든 Velkonite Reinforced Plate 6개를 들여 만듭니다. 소모한 코어의 인챈트 등급을 그대로 이어받으며, 보너스는 다시 굴립니다([모듈 업그레이드](/wiki/05-Items/Forge.md#module-upgrades-in-the-assembly)). 먼저 함선에서 Basic Shield Core를 떼어 내세요(그 안의 셀도 꺼내야 합니다). 장착되어 있거나 셀이 들어 있는 코어는 소모되지 않습니다.

**흡수율**은 공격 한 번마다 실드가 받는 몫이며, 나머지는 선체가 받습니다. 실드 단독으로는 **45~50%**이고, 나머지는 실드 셀이 더합니다. 가장 좋은 실드에 가장 좋은 셀을 조합하면(Heavy Shield Core에 Sovereign Shield Cell 3개) **80%**로, 함선이 기본으로 가질 수 있는 최대치입니다. 여기에 영구 보너스 두 가지가 더해집니다. 시즌 상점의 Shield Absorbance Boost(레벨당 +0.1포인트, 100레벨, 레벨마다 초기화 포인트 25)와 대장간의 흡수율 보너스입니다. 현재 초기화 포인트를 얻을 수 있는 경로(상한까지 모두 채우면 총 855이며 초기화 후에도 유지되고, 경로는 앞으로 더 추가될 예정입니다)로는 그 100레벨 중 34레벨(+3.4포인트)을 살 수 있고, 완전히 단련한 영원한 등급 세트와 합치면 약 **95%**가 됩니다. 다만 이 능력치는 100%로 제한되지 않습니다. 공격자의 *실드 관통*만큼 빠지므로, 100%를 넘는 부분은 관통에 대한 여유입니다. [실드 시스템](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-)을 참고하세요.

---

## 하이브리드 발전기(적응형 코어) {#hybrid-generators-adaptive-cores-}

적응형 코어는 하이브리드 발전기로서 실드와 속도 능력을 겸합니다. 슬롯에는 추진기와 실드 셀을 모두 넣을 수 있습니다(슬롯 하나에 모듈 하나, 둘 중 어느 쪽이든 가능). 실드 보너스와 속도 보너스는 실드나 엔진의 보너스와 같은 방식으로 반영됩니다(가장 좋은 4개에 슬롯의 반영 비율을 곱함). 흡수율은 없습니다. 함선의 흡수율을 바꾸지 않으며, 안에 넣은 셀은 용량과 재충전만 더해 줍니다. 공격을 나눠 받는 것은 실드뿐이므로, 적응형 코어의 셀을 쓰려면 함선에 실드도 있어야 합니다.

| 이름 | 희귀도 | 실드 보너스 % | 속도 보너스 % | 슬롯 | 특수 효과 | 비용 |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **Adaptive Core I** | 하급 | +5% | +3% | 1 | — | 100,000 크레딧 |
| **Adaptive Core II** | 일반 | +8% | +4% | 2 | — | 4,000 Thulium |
| **Adaptive Core III** | 희귀 | +15% | +5% | 3 | — | 제작 전용 |

---

## 실드 셀 {#shield-cells}

실드 셀은 실드 코어나 적응형 코어 안에(코어의 슬롯 수만큼) 끼워 그 코어를 강화합니다. 실드 코어에서는 흡수율도 포인트 단위로 올려 주며, 따라서 실드가 공격마다 받는 몫도 늘어납니다. 슬롯을 모두 같은 셀로 채운 코어는 다음과 같습니다. Light Shield Core(슬롯 1개)는 47~55%, Basic Shield Core(슬롯 2개)는 52~68%, Heavy Shield Core(슬롯 3개)는 56~80%이며, 이는 Basic Shield Cell부터 Sovereign Shield Cell까지의 범위입니다. 코어를 장착 해제하거나 [대장간](/wiki/05-Items/Forge.md) 병합의 제공 아이템으로 소모하면 셀은 인벤토리로 돌아갑니다.

| 이름 | 희귀도 | 용량 증가 | 재충전 증가 | 흡수율 증가 | 비용 |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Basic Shield Cell** | 하급 | +1,000 | +100/초 | +2% | 10,000 크레딧 |
| **Advanced Shield Cell** | 일반 | +2,500 | +250/초 | +4% | 30,000 크레딧 |
| **Reinforced Shield Cell** | 고급 | +4,200 | +350/초 | +6% | 90,000 크레딧 |
| **Elite Shield Cell** | 희귀 | +6,000 | +500/초 | +7% | 5,000 Thulium |
| **Prime Shield Cell** | 희귀 | +8,500 | +700/초 | +8% | 8,000 Thulium |
| **Sovereign Shield Cell** | 영웅 | +12,000 | +1,000/초 | +10% | 제작 전용 |

Sovereign Shield Cell은 [어셈블리](/wiki/05-Items/Overview.md#upgrading-modules)에서 Prime Shield Cell을 재료로, Thulium, 드롭 아이템, 그리고 Skylab에서 만든 Velkonite Reinforced Plate 6개를 들여 만듭니다. 소모한 셀의 인챈트 등급을 그대로 이어받으며, 보너스는 다시 굴립니다([모듈 업그레이드](/wiki/05-Items/Forge.md#module-upgrades-in-the-assembly)). 셀은 [능력 슬롯](/wiki/03-Mechanics/Abilities.md)에 들어가지 않으며, 실드와 적응형 코어 안에 장착합니다.
