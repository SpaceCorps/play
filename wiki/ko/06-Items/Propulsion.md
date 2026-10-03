<!-- wiki-i18n source: b04277deb1c5225f -->
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

**Engine III**는 [어셈블리](/wiki/06-Items/Overview.md#upgrading-modules)에서 Engine II를 재료로, 2,000 Thulium, Ship Fragment 60개, Power Core 3개, 그리고 Skylab에서 만든 Velkonite Reinforced Plate 6개를 들여 만듭니다. 소모한 엔진의 인챈트 등급을 그대로 이어받으며, 보너스는 다시 굴립니다([모듈 업그레이드](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). 먼저 함선에서 Engine II를 떼어 내세요(그 안의 추진기도 꺼내야 합니다). 장착되어 있거나 추진기가 들어 있는 엔진은 소모되지 않습니다.

엔진의 실드 보너스는 아이템 데이터에 들어 있지만 게임에서는 한 번도 적용된 적이 없습니다. 엔진은 실드를 약하게 만들지 않으며, 아이템 카드에도 표시되지 않습니다.

---

## 추진기 {#thrusters}

추진기는 엔진이나 적응형 코어 안에 끼워 속도 출력을 높입니다. 추진기는 각각 네 티어로 이루어진 두 계열이 있습니다. **Impulse Thruster**는 고정 속도를 가장 많이 더하고 장착한 엔진의 속도에 작은 배율도 곱하며, **Momentum Thruster**는 고정 속도를 적게 더하는 대신 더 큰 배율을 곱합니다. 추진기가 들어 있는 엔진(또는 적응형 코어)은 **자체 기본 속도에 추진기의 고정 속도 증가를 더한 값 전체에, 추진기의 속도 배율을 모두 곱한 값**을 만들어 냅니다([속도 계산 방법](/wiki/03-Mechanics/Speed.md)). Momentum Thruster IV 3개를 끼운 Engine III는 (6 + 3 x 12) x 1.14 x 1.14 x 1.14 = 62.2, Impulse Thruster IV 3개를 끼우면 (6 + 3 x 17) x 1.02 x 1.02 x 1.02 = 60.5, Impulse Thruster IV 2개를 끼운 Adaptive Core II는 (0 + 2 x 17) x 1.02 x 1.02 = 35.4입니다(Momentum Thruster IV 2개면 31.2).

| 이름 | 희귀도 | 고정 속도 증가 | 속도 배율 | 비용 |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | 하급 | +5 | 1.02x | 20,000 크레딧 |
| **Impulse Thruster II** | 일반 | +10 | 1.02x | 제작 전용 |
| **Impulse Thruster III** | 희귀 | +15 | 1.03x | 제작 전용 |
| **Impulse Thruster IV** | 영웅 | +17 | 1.02x | 제작 전용 |
| **Momentum Thruster I** | 하급 | +4 | 1.08x | 20,000 크레딧 |
| **Momentum Thruster II** | 일반 | +8 | 1.10x | 제작 전용 |
| **Momentum Thruster III** | 희귀 | +11 | 1.13x | 제작 전용 |
| **Momentum Thruster IV** | 영웅 | +12 | 1.14x | 제작 전용 |

어느 계열이 더 빠른지는 끼우는 곳에 따라 다릅니다. Impulse Thruster는 적응형 코어와 추진기가 1~2개 들어간 엔진에서 더 많은 속도를 내고, 같은 티어의 Momentum Thruster는 슬롯 세 칸을 모두 채운 Engine III에서 더 많은 속도를 냅니다(티어 IV에서 62.2 대 60.5이며, Impulse Thruster IV 1개와 Momentum Thruster IV 2개를 섞은 62.3이 Engine III가 낼 수 있는 최고입니다).

추진기의 속도 배율에 붙는 [대장간](/wiki/06-Items/Forge.md) 보너스는 1을 넘는 부분을 키웁니다(1.14x에 +15% 보너스가 붙으면 1.161x). 대장간은 배율이 1.05x 이하인 곳에는 보너스를 붙이지 않습니다. Impulse Thruster의 1.02x나 1.03x에 붙여도 천분의 일 정도의 효과밖에 없기 때문입니다. Impulse Thruster는 보너스를 1개(고정 속도) 가지며, Momentum Thruster는 2개를 가집니다.

각 계열의 티어 I은 20,000 크레딧에 판매합니다. 티어 II~IV는 [어셈블리](/wiki/06-Items/Overview.md#upgrading-modules)에서 같은 계열의 한 티어 아래 추진기를 재료로, Thulium, 드롭 아이템, 그리고 Skylab에서 만든 Velkonite Reinforced Plate(2개, 4개, 6개)를 들여 만듭니다(Impulse Thruster I로 Impulse Thruster II, II로 III, III으로 IV). 추진기는 계열을 바꾸지 않으므로, Impulse와 Momentum 중 어느 쪽인지는 티어 I을 살 때 고릅니다. 모두 소모한 추진기의 인챈트 등급을 그대로 이어받으며, 보너스는 다시 굴립니다([모듈 업그레이드](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). 추진기는 [능력 슬롯](/wiki/03-Mechanics/Abilities.md)에 들어가지 않으며, 엔진과 적응형 코어 안에 장착합니다.

### 외계인 따돌리기 {#outrunning-aliens}

외계인의 비행 속도는 Seeker 120, Phantasm 160, Bulwark 175, Goombah 180, Crystalys 230입니다. Engine II 1개와 추진기 2개를 장착한 Ostirion은 Impulse Thruster I로 223.1의 속도로 비행합니다. 아직 Crystalys보다 느리므로, 따돌리려면 어셈블리에서 만든 추진기가 필요합니다(Impulse Thruster II 234.0, III 245.5, IV 249.1). Momentum Thruster는 이 함선에서 조금 더 느립니다(Momentum Thruster I은 222.6, II~IV는 233.2, 242.5, 245.8). 두 계열 모두 티어 I은 Crystalys보다 느리고, 어셈블리에서 만든 티어는 모두 더 빠릅니다.
