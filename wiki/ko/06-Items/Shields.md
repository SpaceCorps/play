<!-- wiki-i18n source: 7a131032ce9f07fb -->
<!-- wiki-i18n title: 실드 -->
# 실드와 방어 {#shields-defense}

방어 모듈은 실드 용량을 제공하고, 피해를 흡수하며, 방어력을 재충전합니다.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## 아이템 트리 {#item-tree}

어셈블리에서 만드는 것은 먼저 해당 기술이 필요합니다. 아이템에 마우스를 올리면 연구에 걸리는 시간을 볼 수 있습니다. 기술 트리, 연료, 부스트는 [연구](/wiki/03-Mechanics/Research.md)에 있습니다.

```tree
Light Shield Core | shield, shoddy | buy 20000 Credits | /wiki/06-Items/Shields.md#shield-cores
Basic Shield Core | shield, common | buy 2000 Thulium | /wiki/06-Items/Shields.md#shield-cores
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cores
Adaptive Core I | hybrid-generator, shoddy | buy 100000 Credits | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core II | hybrid-generator, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Adaptive Core I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core III | hybrid-generator, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Adaptive Core II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Absorption Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells

Light Shield Core -> Basic Shield Core => Heavy Shield Core
Adaptive Core I => Adaptive Core II => Adaptive Core III
Absorption Shield Cell I => Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell I => Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```
<!-- item-tree:end -->

## 실드 코어 {#shield-cores}

실드 코어를 함선의 발전기 슬롯이나 [드론](/wiki/03-Mechanics/Drones.md)에 장착하면(드론의 슬롯은 코어 슬롯으로 취급됩니다) 능동 방어막이 생성됩니다. 무거운 실드는 속도를 떨어뜨린다는 점에 유의하세요. **능력 슬롯**에 넣은 실드 코어는 대신 특수 효과 열의 **Shield Surge**를 제공합니다. Shield Surge는 10초에 걸쳐 실드를 회복시키며, 실드 코어 자체의 실드는 더해 주지 않습니다([능력](/wiki/03-Mechanics/Abilities.md) 참고).

| 이름 | 희귀도 | 용량 | 재충전 속도 | 흡수율 | 실드 % | 속도 % | 실드 셀 슬롯 | 특수 효과 | 비용 |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Light Shield Core** | 하급 | 10,000 | 333/초 | 45% | +5% | -1% | 1 | Shield Surge I | 20,000 크레딧 |
| **Basic Shield Core** | 일반 | 15,000 | 500/초 | 48% | +10% | -3% | 2 | Shield Surge II | 2,000 Thulium |
| **Heavy Shield Core** | 희귀 | 25,000 | 833/초 | 50% | +20% | -5% | 3 | Shield Surge III | 제작 전용 |

**Heavy Shield Core**는 [어셈블리](/wiki/06-Items/Overview.md#upgrading-modules)에서 Basic Shield Core를 재료로, 2,000 Thulium, Cataclysite 20개, Reinforced Hull Plate 8개, 그리고 Dark Matter Plate 3개([Dark Matter와 Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md))를 들여 만듭니다. 소모한 코어의 인챈트 등급을 그대로 이어받으며, 보너스는 다시 굴립니다([모듈 업그레이드](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). 먼저 함선에서 Basic Shield Core를 떼어 내세요(그 안의 셀도 꺼내야 합니다). 장착되어 있거나 셀이 들어 있는 코어는 소모되지 않습니다.

**흡수율**은 공격 한 번마다 실드가 받는 몫이며, 나머지는 선체가 받습니다. 실드 단독으로는 **45~50%**이고, 나머지는 실드 셀이 더합니다. 가장 좋은 실드에 가장 좋은 셀을 조합하면(Heavy Shield Core에 Absorption Shield Cell IV 3개) **80%**로, 함선이 기본으로 가질 수 있는 최대치입니다. 여기에 영구 보너스 두 가지가 더해집니다. 시즌 상점의 Shield Absorbance Boost(레벨당 +0.1포인트, 100레벨, 레벨마다 초기화 포인트 25)와 대장간의 흡수율 보너스입니다. 현재 초기화 포인트를 얻을 수 있는 경로(상한까지 모두 채우면 총 855이며 초기화 후에도 유지되고, 경로는 앞으로 더 추가될 예정입니다)로는 그 100레벨 중 34레벨(+3.4포인트)을 살 수 있고, 완전히 단련한 영원한 등급 세트와 합치면 약 **95%**가 됩니다. 다만 이 능력치는 100%로 제한되지 않습니다. 공격자의 *실드 관통*만큼 빠지므로, 100%를 넘는 부분은 관통에 대한 여유입니다. [실드 시스템](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-)을 참고하세요.

---

## 하이브리드 발전기(적응형 코어) {#hybrid-generators-adaptive-cores-}

적응형 코어는 하이브리드 발전기로서 실드와 속도 능력을 겸합니다. 슬롯에는 추진기와 실드 셀을 모두 넣을 수 있습니다(슬롯 하나에 모듈 하나, 둘 중 어느 쪽이든 가능). 실드 보너스와 속도 보너스는 실드나 엔진의 보너스와 같은 방식으로 반영됩니다(가장 좋은 4개에 슬롯의 반영 비율을 곱함). 흡수율은 없습니다. 함선의 흡수율을 바꾸지 않으며, 안에 넣은 셀은 용량과 재충전만 더해 줍니다. 공격을 나눠 받는 것은 실드뿐이므로, 적응형 코어의 셀을 쓰려면 함선에 실드도 있어야 합니다.

| 이름 | 희귀도 | 실드 보너스 % | 속도 보너스 % | 슬롯 | 특수 효과 | 비용 |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **Adaptive Core I** | 하급 | +4% | +2.4% | 1 | — | 100,000 크레딧 |
| **Adaptive Core II** | 일반 | +6.4% | +3.2% | 2 | — | 제작 전용 |
| **Adaptive Core III** | 희귀 | +8% | +4% | 3 | — | 제작 전용 |

**Adaptive Core II**는 [어셈블리](/wiki/06-Items/Overview.md#upgrading-modules)에서 Adaptive Core I을 재료로, 1,000 Thulium, Ship Fragment 10개, Power Core 1개, Velkonite Reinforced Plate 2개를 들여 만듭니다. **Adaptive Core III**는 같은 곳에서 Adaptive Core II를 재료로, 2,000 Thulium, Ship Fragment 60개, Power Core 3개, 그리고 Dark Matter Plate 3개([Dark Matter와 Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md))를 들여 만듭니다. 둘 다 소모한 코어의 인챈트 등급을 그대로 이어받으며, 보너스는 다시 굴립니다([모듈 업그레이드](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). 먼저 함선에서 소모할 코어를 떼어 내세요(그 안의 추진기와 셀도 꺼내야 합니다). 장착되어 있거나 모듈이 들어 있는 코어는 소모되지 않습니다.

---

## 실드 셀 {#shield-cells}

실드 셀은 실드 코어나 적응형 코어 안에(코어의 슬롯 수만큼) 끼워 그 코어를 강화합니다. 실드 코어에서는 흡수율도 포인트 단위로 올려 주며, 따라서 실드가 공격마다 받는 몫도 늘어납니다. 셀은 각각 네 티어로 이루어진 두 계열이 있습니다. **Capacity Shield Cell**은 실드 용량과 재충전 속도를 가장 많이 올려 주고, **Absorption Shield Cell**은 흡수율을 가장 많이 올려 줍니다(각 티어에서 같은 티어의 Capacity보다 흡수율은 2배, 용량과 재충전 속도는 절반). Capacity는 실드가 승부를 가르는 함선에, Absorption은 선체가 승부를 가르는 함선에 유리합니다. 슬롯을 모두 같은 셀로 채운 코어는 다음과 같습니다. Light Shield Core(슬롯 1개)는 47~55%, Basic Shield Core(슬롯 2개)는 52~68%, Heavy Shield Core(슬롯 3개)는 56~80%이며, 이는 티어 I의 Capacity 셀부터 티어 IV의 Absorption 셀까지의 범위입니다. 코어를 장착 해제하거나 [대장간](/wiki/06-Items/Forge.md) 병합의 제공 아이템으로 소모하면 셀은 인벤토리로 돌아갑니다.

| 이름 | 희귀도 | 용량 증가 | 재충전 증가 | 흡수율 증가 | 비용 |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Capacity Shield Cell I** | 하급 | +3,000 | +250/초 | +2% | 30,000 크레딧 |
| **Capacity Shield Cell II** | 일반 | +6,000 | +500/초 | +3% | 제작 전용 |
| **Capacity Shield Cell III** | 희귀 | +9,000 | +750/초 | +4% | 제작 전용 |
| **Capacity Shield Cell IV** | 영웅 | +12,000 | +1,000/초 | +5% | 제작 전용 |
| **Absorption Shield Cell I** | 하급 | +1,500 | +125/초 | +4% | 30,000 크레딧 |
| **Absorption Shield Cell II** | 일반 | +3,000 | +250/초 | +6% | 제작 전용 |
| **Absorption Shield Cell III** | 희귀 | +4,500 | +375/초 | +8% | 제작 전용 |
| **Absorption Shield Cell IV** | 영웅 | +6,000 | +500/초 | +10% | 제작 전용 |

각 계열의 티어 I은 30,000 크레딧에 판매합니다. 티어 II~IV는 [어셈블리](/wiki/06-Items/Overview.md#upgrading-modules)에서 같은 계열의 한 티어 아래 셀을 재료로, Thulium, 드롭 아이템, 플레이트(티어 II와 III에는 Skylab에서 만든 Velkonite Reinforced Plate 2개와 4개, 티어 IV에는 Dark Matter Plate 3개)를 들여 만듭니다(Capacity Shield Cell I로 Capacity Shield Cell II, II로 III, III으로 IV). 셀은 계열을 바꾸지 않으므로, Capacity와 Absorption 중 어느 쪽인지는 티어 I을 살 때 고릅니다. 새 셀은 소모한 셀의 인챈트 등급을 그대로 이어받으며, 보너스는 다시 굴립니다([모듈 업그레이드](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). 셀은 [능력 슬롯](/wiki/03-Mechanics/Abilities.md)에 들어가지 않으며, 실드와 적응형 코어 안에 장착합니다.
