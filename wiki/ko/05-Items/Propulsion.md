<!-- wiki-i18n source: 7fa3db40f02537c2 -->
<!-- wiki-i18n title: 추진 장치 -->
# 추진 장치와 속도 {#propulsion-speed}

추진 장치는 함선의 이동 속도와 기동성을 결정합니다.

## 엔진 {#engines}

엔진은 함선의 주된 추력원입니다. **능력 슬롯**에 넣은 엔진은 대신 특수 효과 열의 **Afterburner**를 제공합니다. Afterburner는 10초 동안 속도를 크게 높이며(엔진이 많을수록 더 오래 지속), 엔진 자체의 추력은 더해 주지 않습니다([능력](/wiki/03-Mechanics/Abilities.md) 참고).

| 이름 | 희귀도 | 기본 속도 | 속도 보너스 % | 실드 보너스 % | 슬롯 | 특수 효과 | 비용 |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | 하급 | +2 | +2% | -2% | 1 | Afterburner I | 20,000 크레딧 |
| **Engine II** | 일반 | +4 | +4% | -8% | 2 | Afterburner II | 2,000 Thulium |
| **Engine III** | 희귀 | +6 | +5% | -15% | 3 | Afterburner III | 제작 전용 |

**Engine III**는 [어셈블리](/wiki/05-Items/Overview.md#upgrading-modules)에서 Engine II를 재료로, 2,000 Thulium, Ship Fragment 60개, Power Core 3개, 그리고 Skylab에서 만든 Velkonite Reinforced Plate 6개를 들여 만듭니다. 소모한 엔진의 인챈트 등급을 그대로 이어받으며, 보너스는 다시 굴립니다([모듈 업그레이드](/wiki/05-Items/Forge.md#module-upgrades-in-the-assembly)). 먼저 함선에서 Engine II를 떼어 내세요(그 안의 추진기도 꺼내야 합니다). 장착되어 있거나 추진기가 들어 있는 엔진은 소모되지 않습니다.

엔진의 실드 보너스는 아이템 데이터에 들어 있지만 게임에서는 한 번도 적용된 적이 없습니다. 엔진은 실드를 약하게 만들지 않으며, 아이템 카드에도 표시되지 않습니다.

---

## 추진기 {#thrusters}

추진기는 엔진이나 적응형 코어 안에 끼워 속도 출력을 높입니다.

| 이름 | 희귀도 | 고정 속도 증가 | 속도 배율 | 비용 |
| :--- | :--- | :---: | :---: | :--- |
| **Thruster I** | 하급 | +5 | 1.00x | 20,000 크레딧 |
| **Vector Thruster** | 고급 | +7 | 1.02x | 80,000 크레딧 |
| **Thruster II** | 일반 | +10 | 1.05x | 2,000 Thulium |
| **Ion Thruster** | 희귀 | +13 | 1.08x | 3,000 Thulium |
| **Thruster III** | 희귀 | +15 | 1.10x | 제작 전용 |
| **Plasma Thruster** | 영웅 | +18 | 1.12x | 제작 전용 |

Plasma Thruster는 [어셈블리](/wiki/05-Items/Overview.md#upgrading-modules)에서 Ion Thruster를 재료로, Thulium, 드롭 아이템, 그리고 Skylab에서 만든 Velkonite Reinforced Plate 6개를 들여 만들고, **Thruster III**는 Thruster II를 재료로, 1,500 Thulium, Ship Fragment 30개, Power Core 2개, Velkonite Reinforced Plate 4개를 들여 만듭니다. 둘 다 소모한 추진기의 인챈트 등급을 그대로 이어받으며, 보너스는 다시 굴립니다([모듈 업그레이드](/wiki/05-Items/Forge.md#module-upgrades-in-the-assembly)). 추진기는 [능력 슬롯](/wiki/03-Mechanics/Abilities.md)에 들어가지 않으며, 엔진과 적응형 코어 안에 장착합니다.

### 외계인 따돌리기 {#outrunning-aliens}

외계인의 비행 속도는 Seeker 120, Phantasm 160, Bulwark 175, Goombah 180, Crystalys 230입니다. Engine II 1개와 추진기 2개를 장착한 Ostirion은 Thruster I로 222.6, Vector Thruster로 226.9의 속도로 비행합니다. 둘 다 Crystalys보다 느리므로, Thulium 추진기와 그것으로 만든 추진기(Thruster II 233.4, Ion Thruster 239.9, Thruster III 244.2, Plasma Thruster 250.7)만이 Crystalys를 따돌릴 수 있습니다.
