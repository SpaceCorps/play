<!-- wiki-i18n source: 201734b1f19e2346 -->
<!-- wiki-i18n title: 추진 장치 -->
# 추진 장치와 속도 {#propulsion-speed}

추진 장치는 함선의 이동 속도와 기동성을 결정합니다.

## 1분 요약 {#in-one-minute}

- **엔진은 속도를 만들고, 추진기는 엔진 안에 끼워 그 속도를 높입니다.** 엔진에는 추진기를 1~3개 끼울 수 있고(Engine I은 1개, Engine II는 2개, Engine III는 3개), 적응형 코어도 마찬가지입니다(티어에 따라 개수가 정해집니다).
- **네 티어씩 두 계열.** Impulse Thruster는 고정 속도를 가장 많이 더하고, Momentum Thruster는 고정 속도를 적게 더하는 대신 속도를 더 크게 곱합니다. 두 계열 모두 티어가 오를 때마다 두 수치가 모두 아래 티어보다 높아집니다.
- **어느 것을 어디에.** 기본적으로 Momentum은 추진기 3개를 모두 채운 Engine III에, Impulse는 그 밖의 모든 곳에 알맞습니다. 수치는 [아래 표](#which-thruster-where)에 있습니다. 가장 빠른 Engine III는 둘을 섞은 것으로, Impulse Thruster IV 1개와 Momentum Thruster IV 2개로 62.1이 됩니다.
- **구하는 법.** 각 계열의 티어 I은 20,000 크레딧에 팔고, 티어 II~IV는 어셈블리에서 한 티어 아래의 추진기로 제작합니다. 추진기는 계열이 바뀌지 않습니다.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## 아이템 트리 {#item-tree}

어셈블리에서 만드는 것은 먼저 해당 기술이 필요합니다. 아이템에 마우스를 올리면 연구에 걸리는 시간을 볼 수 있습니다. 기술 트리, 연료, 부스트는 [연구](/wiki/03-Mechanics/Research.md)에 있습니다.

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | buy 2000 Thulium | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I -> Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## 엔진 {#engines}

엔진은 함선의 주된 추력원입니다. **능력 슬롯**에 넣은 엔진은 대신 특수 효과 열의 **Afterburner**를 제공합니다. Afterburner는 10초 동안 속도를 크게 높이며(엔진이 많을수록 더 오래 지속), 엔진 자체의 추력은 더해 주지 않습니다([능력](/wiki/03-Mechanics/Abilities.md) 참고).

| 이름 | 희귀도 | 기본 속도 | 속도 보너스 % | 실드 보너스 % | 슬롯 | 특수 효과 | 비용 |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | 하급 | +2 | +2% | -2% | 1 | Afterburner I | 20,000 크레딧 |
| **Engine II** | 일반 | +4 | +4% | -8% | 2 | Afterburner II | 2,000 Thulium |
| **Engine III** | 희귀 | +6 | +5% | -15% | 3 | Afterburner III | 제작 전용 |

**Engine III**는 [어셈블리](/wiki/06-Items/Overview.md#upgrading-modules)에서 Engine II를 재료로, 2,000 Thulium, Ship Fragment 60개, Power Core 3개, 그리고 Dark Matter Plate 3개([Dark Matter와 Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md))를 들여 만듭니다. 소모한 엔진의 인챈트 등급을 그대로 이어받으며, 보너스는 다시 굴립니다([모듈 업그레이드](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). 먼저 함선에서 Engine II를 떼어 내세요(그 안의 추진기도 꺼내야 합니다). 장착되어 있거나 추진기가 들어 있는 엔진은 소모되지 않습니다.

엔진의 실드 보너스는 아이템 데이터에 들어 있지만 게임에서는 한 번도 적용된 적이 없습니다. 엔진은 실드를 약하게 만들지 않으며, 아이템 카드에도 표시되지 않습니다.

---

## 추진기 {#thrusters}

추진기는 엔진이나 적응형 코어 안에 끼워 속도 출력을 높입니다. 추진기는 각각 네 티어로 이루어진 두 계열이 있습니다. **Impulse Thruster**는 고정 속도를 가장 많이 더하고 장착한 엔진의 속도에 작은 배율도 곱하며, **Momentum Thruster**는 고정 속도를 적게 더하는 대신 더 큰 배율을 곱합니다. 두 계열 모두 티어가 오를 때마다 고정 속도와 배율이 모두 아래 티어보다 높아집니다. 추진기가 들어 있는 엔진(또는 적응형 코어)은 **자체 기본 속도에 추진기의 고정 속도 증가를 더한 값 전체에, 추진기의 속도 배율을 모두 곱한 값**을 만들어 냅니다([속도 계산 방법](/wiki/03-Mechanics/Speed.md)). Momentum Thruster IV 3개를 끼운 Engine III는 (6 + 3 x 13.1) x 1.11 x 1.11 x 1.11 = 62.0, Impulse Thruster IV 3개를 끼우면 (6 + 3 x 16.5) x 1.035 x 1.035 x 1.035 = 61.5, Impulse Thruster IV 2개를 끼운 Adaptive Core II는 (0 + 2 x 16.5) x 1.035 x 1.035 = 35.4입니다(Momentum Thruster IV 2개면 32.3).

| 이름 | 희귀도 | 고정 속도 증가 | 속도 배율 | 비용 |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | 하급 | +5 | 1.02x | 20,000 크레딧 |
| **Impulse Thruster II** | 일반 | +10 | 1.025x | 제작 전용 |
| **Impulse Thruster III** | 희귀 | +15 | 1.03x | 제작 전용 |
| **Impulse Thruster IV** | 영웅 | +16.5 | 1.035x | 제작 전용 |
| **Momentum Thruster I** | 하급 | +4.5 | 1.06x | 20,000 크레딧 |
| **Momentum Thruster II** | 일반 | +9 | 1.07x | 제작 전용 |
| **Momentum Thruster III** | 희귀 | +12.5 | 1.09x | 제작 전용 |
| **Momentum Thruster IV** | 영웅 | +13.1 | 1.11x | 제작 전용 |

### 어느 추진기를 어디에 {#which-thruster-where}

Impulse는 고정 속도를 더 많이 더하고 Momentum은 더 크게 곱하므로, 어느 쪽이 더 빠른지는 엔진이 이미 만들어 내는 속도에 달려 있습니다. 고정 속도는 곱할 속도가 적은 곳, 즉 적응형 코어(자체 속도가 없습니다)와 추진기가 1~2개인 엔진에서 가장 큰 효과를 냅니다. 배율은 곱할 속도가 많은 곳, 즉 추진기 3개를 모두 채운 Engine III에서 가장 큰 효과를 냅니다. 모든 슬롯에 티어 IV 추진기를 끼웠을 때 각 구성이 내는 속도는 다음과 같습니다.

| 추진기를 끼운 곳 | Impulse Thruster IV일 때 | Momentum Thruster IV일 때 | 더 빠른 쪽 |
| :--- | :---: | :---: | :--- |
| Engine I, 추진기 1개 | 19.1 | 16.8 | Impulse |
| Engine II, 추진기 2개 | 39.6 | 37.2 | Impulse |
| Engine III, 추진기 1개 | 23.3 | 21.2 | Impulse |
| Engine III, 추진기 2개 | 41.8 | 39.7 | Impulse |
| Engine III, 추진기 3개 | 61.5 | 62.0 | Momentum |
| Adaptive Core II, 추진기 2개 | 35.4 | 32.3 | Impulse |

- **낮은 티어.** 티어 I~III도 같은 양상이지만, 접전인 경우가 둘 있습니다. Engine II에 추진기를 2개 끼우면 티어 I과 II에서는 두 계열이 비슷하고(차이 0.05 이내), Engine III에 2개를 끼우면 티어 I과 II에서 Momentum이 약 0.2 앞섭니다. 티어 III부터는 두 경우 모두 Impulse가 1.4~2.4 앞섭니다. 추진기 3개를 모두 채운 Engine III에서는 모든 티어에서 Momentum이 0.4~1.7 앞섭니다.
- **Engine III에서는 섞으세요.** 가장 빠른 Engine III는 Impulse Thruster IV 1개와 Momentum Thruster IV 2개를 끼운 것입니다. (6 + 16.5 + 2 x 13.1) x 1.035 x 1.11 x 1.11 = 62.1로, Momentum 3개(62.0)나 Impulse 3개(61.5)보다 조금 높습니다.

추진기의 속도 배율에 붙는 [대장간](/wiki/06-Items/Forge.md) 보너스는 1을 넘는 부분을 키웁니다(1.11x에 +15% 보너스가 붙으면 1.1265x). 대장간은 배율이 1.05x 이하인 곳에는 보너스를 붙이지 않습니다. Impulse Thruster의 1.02x~1.035x에 붙여도 늘어나는 것은 0.006 미만입니다(1.035x에 +15%면 1.040x). Impulse Thruster는 보너스를 1개(고정 속도) 가지며, Momentum Thruster는 2개를 가집니다.

각 계열의 티어 I은 20,000 크레딧에 판매합니다. 티어 II~IV는 [어셈블리](/wiki/06-Items/Overview.md#upgrading-modules)에서 같은 계열의 한 티어 아래 추진기를 재료로, Thulium, 드롭 아이템, 플레이트(티어 II와 III에는 Skylab에서 만든 Velkonite Reinforced Plate 2개와 4개, 티어 IV에는 Dark Matter Plate 3개)를 들여 만듭니다(Impulse Thruster I로 Impulse Thruster II, II로 III, III으로 IV). 추진기는 계열을 바꾸지 않으므로, Impulse와 Momentum 중 어느 쪽인지는 티어 I을 살 때 고릅니다. 모두 소모한 추진기의 인챈트 등급을 그대로 이어받으며, 보너스는 다시 굴립니다([모듈 업그레이드](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). 추진기는 [능력 슬롯](/wiki/03-Mechanics/Abilities.md)에 들어가지 않으며, 엔진과 적응형 코어 안에 장착합니다.

### 외계인 따돌리기 {#outrunning-aliens}

외계인의 비행 속도는 Seeker 120, Phantasm 160, Bulwark 175, Goombah 180, Crystalys 230입니다. Engine II 1개와 추진기 2개를 장착한 Ostirion은 Impulse Thruster I로 223.1의 속도로 비행합니다. 아직 Crystalys보다 느리므로, 따돌리려면 어셈블리에서 만든 추진기가 필요합니다(Impulse Thruster II 234.2, III 245.5, IV 249.2). Momentum Thruster는 이 함선에서 같거나 조금 더 느립니다(Momentum Thruster I은 223.2, II~IV는 234.2, 243.8, 246.7). 두 계열 모두 티어 I은 Crystalys보다 느리고, 어셈블리에서 만든 티어는 모두 더 빠릅니다.
