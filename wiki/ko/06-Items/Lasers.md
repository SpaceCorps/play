<!-- wiki-i18n source: 3d97a6f4bd324d8d -->
<!-- wiki-i18n title: 레이저 -->
# 레이저와 탄약 {#lasers-ammo}

SpaceCorps에서 무기는 피해를 입히는 주된 수단입니다.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## 아이템 트리 {#item-tree}

어셈블리에서 만드는 것은 먼저 해당 기술이 필요합니다. 아이템에 마우스를 올리면 연구에 걸리는 시간을 볼 수 있습니다. 기술 트리, 연료, 부스트는 [연구](/wiki/03-Mechanics/Research.md)에 있습니다.

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

## 레이저 {#lasers}

레이저를 함선의 레이저 슬롯에 직접 장착하거나 드론 안에 장착해 공격력을 높이세요.

| 이름 | 희귀도 | 기본 피해량 | 치명타 확률 | 사거리 | 증폭기 슬롯 | 비용 |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Quantum Laser 1** | 하급 | 55 | – | 600 | 1 | 8,000 크레딧 |
| **Quantum Laser 2** | 일반 | 65 | – | 700 | 2 | 80,000 크레딧 |
| **Quantum Laser 3** | 희귀 | 80 | 10% | 800 | 3 | 제작 전용 |
| **Starfire-3** | 신화 | 135 | 15% | 850 | 3 | 제작 전용 |
| **Helios Beam** | 신화 | 185 | 25% | 900 | 3 | 제작 전용 |

사거리 열은 각 레이저의 고유 사거리입니다. **함선은 장착한 레이저 사거리의 평균**(드론에 장착한 레이저도 포함)을 가장 가까운 정수로 반올림한 거리에서 사격하며, 대상이 그 거리 안에 들어오면 모든 레이저가 사격합니다. Starfire-3 한 개와 Quantum Laser 2 두 개를 함께 쓰면 함선의 사거리는 850이 아니라 750이고, Starfire-3 세 개면 850이 유지되며, 레이저가 모두 같으면 달라지는 것이 없습니다. 대장간의 사거리 보너스는 평균을 내기 전에 해당 레이저에 먼저 적용됩니다. 레이저가 없으면 격납고에는 사거리가 표시되지 않고(줄표로 나옵니다) 레이저는 사격할 수 없지만, 로켓은 여전히 각자의 사거리로 발사할 수 있습니다([로켓](/wiki/06-Items/Rockets.md) 참고). 격납고에서는 레이저들의 사거리가 서로 다르면 타일에 “평균 사거리”라고 표시되며, 마우스를 올리면 각 레이저의 사거리가 나열됩니다.

Quantum Laser 1, 2에는 고유 치명타 확률이 없으며(“–”), 슬롯에 피해 증폭기나 치명타 증폭기를 넣어야 치명타 확률이 생깁니다. 치명타는 떠오르는 피해 숫자에서 다른 색으로 표시됩니다(얼음빛 하늘색에 더 크게, “!”가 붙습니다).

### 상위 레이저 3종 제작 {#making-the-top-three-lasers}

**Quantum Laser 3**, **Starfire-3**, **Helios Beam**은 **어셈블리**에서만 만들 수 있습니다. Quantum Laser 3는 더 이상 상점에서 판매하지 않으며, 이미 보유한 파일럿은 계속 가지고 있습니다. 각 제작법에는 [Skylab](/wiki/03-Mechanics/Skylab.md)의 단조소에서 만든 플레이트가 필요합니다.

| 레이저 | 제작 시간 | 필요 재료 |
| :--- | :---: | :--- |
| Quantum Laser 3 | 1분 | Ship Fragment 10개, Velkonite Reinforced Plate 2개, 1,500 Thulium |
| Starfire-3 | 1분 | Quantum Laser 3 1개, Ship Fragment 15개, Velkonite Reinforced Plate 8개, Reinforced Hull Plate 1개, 1,500 Thulium, 100,000 크레딧 |
| Helios Beam | 3분 | Starfire-3 1개, Cataclysite 50개, Power Core 2개, Orvium Reinforced Plate 18개, Reinforced Hull Plate 4개, 2,000 Thulium |

어셈블리 페이지에는 제작법에 필요한 양과 보유량이 나란히 표시되며, 조립 버튼에는 부족한 것이 표시됩니다. 레시피의 이미지나 이름, 또는 재료에 마우스를 올리면 아이템의 전체 설명과 능력치가 표시됩니다.

**Starfire-3는 Quantum Laser 3를 재료로 만듭니다.** 먼저 Quantum Laser 3를 만들고, Starfire-3가 그것을 소모합니다. Quantum Laser 3에 이미 들어간 것은 다시 요구되지 않으므로, 둘을 합친 비용은 예전에 Starfire-3 하나가 단독으로 요구하던 것과 정확히 같습니다. 3,000 Thulium, 100,000 크레딧, Ship Fragment 25개, Velkonite Reinforced Plate 10개, Reinforced Hull Plate 1개, 그리고 2분입니다. 이미 Quantum Laser 3가 있다면 Starfire-3 자체의 몫만 치르면 됩니다. 규칙은 아래에 나오는 Helios Beam의 규칙과 같습니다. Starfire-3는 소모한 Quantum Laser 3의 인챈트 등급을 이어받고(신성한 Quantum Laser 3로는 신성한 Starfire-3가 만들어집니다) 보너스는 다시 굴리며, 어느 Quantum Laser 3를 쓸지 직접 고르고, 표준보다 높은 등급을 쓰기 전에는 카드가 먼저 묻고, Quantum Laser 3는 장착되지 않은 상태여야 합니다. **먼저 함선에서 떼어 내세요**(장착한 증폭기는 인벤토리로 돌아갑니다). 수송 보관함에서도 꺼내야 합니다. 함선에 장착되어 있으면 조립 버튼에 “먼저 Quantum Laser 3 해제”라고 표시됩니다.

**Helios Beam은 Starfire-3를 재료로 만듭니다.** 먼저 Starfire-3를 만들고(재료인 Quantum Laser 3까지 합쳐 3,000 Thulium, 100,000 크레딧), Helios Beam이 그것을 소모합니다. [Master Drone](/wiki/06-Items/Drones.md)이 Slave Drone을 소모하는 것과 같습니다. Starfire-3에 이미 들어간 것은 다시 요구되지 않으므로, 둘을 합친 비용은 Helios Beam이 단독으로 요구하던 5,000 Thulium, Cataclysite, Power Core, Reinforced Hull Plate에, Orvium 플레이트 20장 대신 18장입니다(Starfire-3의 Velkonite 플레이트 10장이 부족한 2장을 대신합니다). 이 밖에 치르는 것은 Starfire-3의 100,000 크레딧과 Ship Fragment 25개입니다. 규칙은 [모듈 업그레이드](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)와 같습니다. Helios Beam은 소모한 Starfire-3의 인챈트 등급을 이어받고(신성한 Starfire-3로는 신성한 Helios Beam이 만들어집니다) 보너스는 다시 굴리며, 여러 개를 보유하면 어느 Starfire-3를 쓸지 직접 고르고, 표준보다 높은 등급을 쓰기 전에는 카드가 먼저 묻습니다. Starfire-3는 장착되지 않은 상태여야 합니다. **먼저 함선에서 떼어 내세요**(장착한 증폭기는 인벤토리로 돌아갑니다). 수송 보관함에서도 꺼내야 합니다. 함선에 장착되어 있으면 조립 버튼에 “먼저 Starfire-3 해제”라고 표시됩니다.

플레이트의 출처는 다음과 같습니다.

- **Velkonite Reinforced Plate**(Quantum Laser 3, Starfire-3)는 Velkonite로 단조하며, 단조소 레벨 1에서는 플레이트 1장에 광석 40개가 듭니다. **Orvium Reinforced Plate**(Helios Beam)는 Orvium으로 단조하며, 플레이트 1장에 광석 80개가 듭니다.
- 광석은 Skylab의 수집기에서만 나옵니다. 레벨 5 Velkonite 수집기는 시간당 Velkonite를 18개 채굴하므로, Quantum Laser 3의 플레이트는 채굴에 약 4시간, Starfire-3의 플레이트 10장(Quantum Laser 3 단계에 2장, 자체 단계에 8장)은 약 22시간이 걸립니다. 가장 오래 걸리는 것은 Helios Beam입니다. 플레이트 18장에 Orvium 1,440개가 필요하며, 레벨 5 Orvium 수집기로 약 4일이 걸립니다.
- 자원 창고는 레벨 1에서 광석을 종류별로 240개까지 보관합니다. 단조소 레벨 1에서 Velkonite 플레이트 6장이나 Orvium 플레이트 3장 분량입니다. 그러므로 그때그때 단조하거나(레벨 1에서 단조소의 배치는 플레이트 최대 10장) 창고를 업그레이드하세요.
- 단조한 플레이트는 함선이 착륙해 있는 동안 수거할 때까지 단조소에서 기다리며, 수거하면 일반 아이템으로 인벤토리에 들어옵니다.

Ship Fragment, Cataclysite, Power Core, Reinforced Hull Plate는 외계인이 드롭합니다. 각 재료의 모든 획득처와 용도는 [자원](/wiki/06-Items/Resources.md) 페이지에 있으며, [Bulwark](/wiki/04-Aliens/Bulwark.md)와 [Goombah](/wiki/04-Aliens/Goombah.md) 페이지의 전리품 목록에서 드롭량을 확인할 수 있습니다.

---

## 레이저 증폭기(Amp) {#laser-amplifiers-amps-}

레이저의 증폭기 슬롯에 직접 끼워 레이저의 특성을 강화합니다. 계열은 두 가지이며 각각 4단계입니다. **피해 계열**은 고정 피해량을 더하고, **치명타 계열**은 치명타 확률과 고정 치명타 피해를 더합니다.

| 이름 | 희귀도 | 기본 피해량 증가 | 치명타 확률 증가 | 고정 치명타 피해 | 비용 |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Damage Amp 1** | 하급 | +10 | +5% | +5 | 10,000 크레딧 |
| **Arc Amp** | 고급 | +16 | +5% | +8 | 60,000 크레딧 |
| **Pulse Amp** | 희귀 | +26 | +6% | +13 | 1,500 Thulium |
| **Nova Amp** | 영웅 | +38 | +7% | +20 | 제작 전용 |
| **Crit Amp 1** | 하급 | +0 | +15% | +0 | 15,000 크레딧 |
| **Focus Amp** | 고급 | +0 | +20% | +14 | 60,000 크레딧 |
| **Prism Amp** | 희귀 | +0 | +25% | +24 | 1,500 Thulium |
| **Apex Amp** | 영웅 | +0 | +25% | +44 | 제작 전용 |

Nova Amp와 Apex Amp는 [어셈블리](/wiki/06-Items/Overview.md#upgrading-modules)에서 각각 Pulse Amp와 Prism Amp를 재료로, Thulium, 드롭 아이템, Skylab에서 만든 Velkonite Reinforced Plate 3개를 들여 만듭니다. 소모한 증폭기의 인챈트 등급을 이어받으며 보너스는 다시 굴립니다([모듈 업그레이드](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)).

### 어느 증폭기를 어디에 쓸까 {#which-amp-goes-where}

피해 증폭기는 어떤 레이저에든 같은 양의 피해를 더하므로 **Quantum 레이저**에서 가치가 가장 큽니다. 치명타 증폭기는 레이저가 이미 내는 피해에 곱해지므로 레이저가 강할수록 가치가 커집니다. **Starfire-3**에서는 피해 계열과 동률이 되고, **Helios Beam**에서는 약 3.5% 앞섭니다. 레이저의 치명타 확률은 100%에서 멈춥니다. Prism Amp나 Apex Amp 세 개를 달면 Helios Beam이 정확히 그 값에 이릅니다.

같은 증폭기로 채우면 레이저는 항상 바로 아래 레이저보다 강하므로, 더 좋은 증폭기가 더 좋은 레이저를 대신할 수는 없습니다. Nova Amp 세 개를 단 Quantum Laser 3는 Damage Amp 1 세 개를 단 Helios Beam보다 피해량이 낮습니다(같은 인챈트 등급의 부품끼리 비교한 경우입니다. 신성한 등급 이상으로 단련하고 최고의 보너스를 굴린 Quantum Laser 3와 Nova Amp라면, Damage Amp 1을 단 평범한 Helios Beam을 넘어설 수 있으며, 신성한 등급에서는 간발의 차입니다).

---

## 레이저 탄약 {#laser-ammunition}

레이저 일제 사격의 피해를 배가시키는 소모성 배터리입니다.

| 이름 | 희귀도 | 피해 배율 | 실드 관통 | 개당 가격 |
| :--- | :--- | :---: | :---: | :--- |
| **Standard Battery** | 일반 | 1.0x | – | 10 크레딧 |
| **Advanced Plasma** | 희귀 | 2.0x | – | 0.5 Thulium |
| **Ultra Core** | 희귀 | 3.0x | 5% | 1.0 Thulium |
| **Experimental Fusion Core** | 영웅 | 4.0x | 10% | 2.2 Thulium |
| **Siphon Battery** | 희귀 | 1.0x, 실드에만 | – | 0.25 Thulium |

**실드 관통**은 일제 사격의 매 공격마다 대상의 흡수율에서 차감됩니다. 즉 실드는 대상의 흡수율에서 관통을 뺀 몫을 받습니다([실드 시스템](/wiki/03-Mechanics/Shields.md#shield-penetration) 참고). 80%(가장 좋은 실드에 가장 좋은 셀)인 함선을 상대로 x4 탄약의 10%는 실드가 공격의 70%를, 선체가 30%를 받게 합니다. 실드에 비해 선체가 작은 함선에 가장 큰 의미가 있으며, 80%인 아주 큰 함선은 어느 쪽이든 똑같이 버팁니다. 외계인에게는 이렇다 할 흡수율 능력치가 없으며(외계인의 실드는 공격의 80%를 받습니다), 관통은 거기서도 차감됩니다.

### Siphon Battery

Siphon Battery는 선체를 부수는 대신 실드를 빼앗는 탄약입니다. **대상의 실드에 x1 피해를 직접** 입히고, 같은 양을 최대치까지 **자신의 실드**에 더합니다. 다른 탄약과 마찬가지로 퀵슬롯의 탄약 선택창에서 고르세요(청록색 소용돌이가 그려진 타일입니다). 광선을 쏘지 않습니다. 가늘고 희미한 청록색 탐침이 대상에게 뻗어 나가고, 닿은 자리에서 대상의 실드가 청록색으로 번쩍이며, 빼앗은 실드는 빛나는 청록색 입자(3~10개, 많이 빼앗을수록 더 많이)가 약 0.5초 동안 하나씩 차례로 함선으로 흘러 들어오는 모습으로 눈에 보입니다. 입자가 하나 도착할 때마다 실드가 맥동합니다. 시야에 들어온 모든 파일럿의 Siphon Battery도 누구에게서 빼앗든(외계인, 다른 파일럿, 기업 파일럿의 함선) 똑같이 보입니다.

- **실드 전용**: 선체는 절대 건드리지 않고, 대상의 흡수율로 피해가 나뉘지도 않으며, Siphon Battery로는 아무것도 파괴할 수 없습니다. 피해량은 대상의 실드에 남아 있는 양을 넘지 못합니다.
- **빼앗을 것이 없을 때**: 실드가 남지 않은 대상에게는 아무것도 빼앗지 못하고 얻는 것도 없습니다. 일제 사격은 다른 탄약과 마찬가지로 레이저 1개당 배터리 1개씩 소모됩니다. 탐침과 선체에서 둔하게 깜박이는 빛만 보이고 입자는 나타나지 않습니다.
- **획득**: 자신의 실드는 최대치를 넘지 않으며, 실드를 흡수해도 자신의 실드 재생이 늦춰지지 않습니다.
- **외계인과 파일럿** 모두 빼앗을 실드가 있습니다. 외계인에게서 실드를 빼앗으면 [첫 타격 선점](/wiki/03-Mechanics/Combat.md)에서 공격으로 인정되고, 실드가 없어 빼앗지 못하면 인정되지 않습니다. 반격만 하는 Seeker나 Goombah도 다른 공격과 마찬가지로 깨웁니다.
- **치명타**도 적용됩니다. 치명타 일제 사격은 1.5배를 빼앗으며 숫자도 치명타로 표시됩니다. 입자는 더 크고 밝으며, 대상의 실드는 더 강하게 번쩍입니다.
- [기업 파일럿](/wiki/03-Mechanics/Company-Pilots.md)은 기본 x1 탄약을 사용합니다.
