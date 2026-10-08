<!-- wiki-i18n source: 9288511cf701ce85 -->
<!-- wiki-i18n title: 레이저 -->
# 레이저와 탄약 {#lasers-ammo}

<!-- wiki-search: arc amp; focus amp; pulse amp; prism amp; nova amp; apex amp; damage amp 1; crit amp 1; amps; penetration amp; shield penetration -->

SpaceCorps에서 무기는 피해를 입히는 주된 수단입니다.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## 아이템 트리 {#item-tree}

어셈블리에서 만드는 것은 먼저 해당 기술이 필요합니다. 아이템에 마우스를 올리면 연구에 걸리는 시간을 볼 수 있습니다. 기술 트리, 연료, 부스트는 [연구](/wiki/03-Mechanics/Research.md)에 있습니다.

```tree
Quantum Laser I | laser, shoddy | buy 8000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser II | laser, common | buy 80000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser III | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-III | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser III, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-III, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#lasers
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
Standard Battery | ammo, common | buy 5 Credits | /wiki/06-Items/Lasers.md#laser-ammunition
Siphon Battery | ammo, rare | buy 0.25 Thulium | /wiki/06-Items/Lasers.md#siphon-battery
Advanced Plasma | ammo, rare | buy 0.5 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Ultra Core | ammo, rare | buy 1 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Experimental Fusion Core | ammo, epic | buy 2.2 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition

Quantum Laser I -> Quantum Laser II -> Quantum Laser III => Starfire-III => Helios Beam
Damage Amp I => Damage Amp II => Damage Amp III => Damage Amp IV
Crit Amp I => Crit Amp II => Crit Amp III => Crit Amp IV
Penetration Amp I => Penetration Amp II => Penetration Amp III => Penetration Amp IV
Standard Battery -> Advanced Plasma -> Ultra Core -> Experimental Fusion Core
```
<!-- item-tree:end -->

## 레이저 {#lasers}

레이저를 함선의 레이저 슬롯에 직접 장착하거나 드론 안에 장착해 공격력을 높이세요.

| 이름 | 희귀도 | 기본 피해량 | 치명타 확률 | 사거리 | 증폭기 슬롯 | 비용 |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Quantum Laser I** | 하급 | 55 | – | 600 | 1 | 8,000 크레딧 |
| **Quantum Laser II** | 일반 | 65 | – | 700 | 2 | 80,000 크레딧 |
| **Quantum Laser III** | 희귀 | 80 | 10% | 800 | 3 | 제작 전용 |
| **Starfire-III** | 신화 | 135 | 15% | 850 | 3 | 제작 전용 |
| **Helios Beam** | 신화 | 185 | 25% | 900 | 3 | 제작 전용 |

사거리 열은 각 레이저의 고유 사거리입니다. **함선은 장착한 레이저 사거리의 평균**(드론에 장착한 레이저도 포함)을 가장 가까운 정수로 반올림한 거리에서 사격하며, 대상이 그 거리 안에 들어오면 모든 레이저가 사격합니다. Starfire-III 한 개와 Quantum Laser II 두 개를 함께 쓰면 함선의 사거리는 850이 아니라 750이고, Starfire-III 세 개면 850이 유지되며, 레이저가 모두 같으면 달라지는 것이 없습니다. 대장간의 사거리 보너스는 평균을 내기 전에 해당 레이저에 먼저 적용됩니다. 레이저가 없으면 격납고에는 사거리가 표시되지 않고(줄표로 나옵니다) 레이저는 사격할 수 없지만, 로켓은 여전히 각자의 사거리로 발사할 수 있습니다([로켓](/wiki/06-Items/Rockets.md) 참고). 격납고에서는 레이저들의 사거리가 서로 다르면 타일에 “평균 사거리”라고 표시되며, 마우스를 올리면 각 레이저의 사거리가 나열됩니다.

Quantum Laser I, 2에는 고유 치명타 확률이 없으며(“–”), 슬롯에 Damage Amp나 Crit Amp를 넣어야 치명타 확률이 생깁니다(Penetration Amp는 아닙니다). 치명타는 떠오르는 피해 숫자에서 다른 색으로 표시됩니다(얼음빛 하늘색에 더 크게, “!”가 붙습니다. [피해와 회복 숫자](/wiki/03-Mechanics/Combat.md#damage-and-heal-numbers) 참고).

레이저도 [소행성](/wiki/03-Mechanics/Asteroid-Mining.md#breaking-one)에 피해를 주지만, 일제 사격이 함선에 주는 피해의 5%뿐입니다(증폭기, 부스터, 탄약, 치명타가 반영되고 그다음 소행성의 장갑이 차감되며, Siphon Battery는 소행성에 피해를 줄 수 없습니다). 소행성을 부수는 데 맞는 도구는 로켓입니다.

### 상위 레이저 3종 제작 {#making-the-top-three-lasers}

**Quantum Laser III**, **Starfire-III**, **Helios Beam**은 **어셈블리**에서만 만들 수 있습니다. Quantum Laser III는 더 이상 상점에서 판매하지 않으며, 이미 보유한 파일럿은 계속 가지고 있습니다. 각 제작법에는 [Skylab](/wiki/03-Mechanics/Skylab.md)의 단조소에서 만든 플레이트가 필요하며, Helios Beam에는 Dark Matter Plate 3개도 필요합니다.

| 레이저 | 제작 시간 | 필요 재료 |
| :--- | :---: | :--- |
| Quantum Laser III | 1분 | Ship Fragment 10개, Velkonite Reinforced Plate 2개, 1,500 Thulium |
| Starfire-III | 1분 | Quantum Laser III 1개, Ship Fragment 15개, Velkonite Reinforced Plate 8개, Reinforced Hull Plate 1개, 1,500 Thulium, 100,000 크레딧 |
| Helios Beam | 3분 | Starfire-III 1개, Cataclysite 50개, Power Core 2개, Orvium Reinforced Plate 18개, Dark Matter Plate 3개, Reinforced Hull Plate 4개, 2,000 Thulium |

어셈블리 페이지에는 제작법에 필요한 양과 보유량이 나란히 표시되며, 조립 버튼에는 부족한 것이 표시됩니다. 레시피의 이미지나 이름, 또는 재료에 마우스를 올리면 아이템의 전체 설명과 능력치가 표시됩니다.

**Starfire-III는 Quantum Laser III를 재료로 만듭니다.** 먼저 Quantum Laser III를 만들고, Starfire-III가 그것을 소모합니다. Quantum Laser III에 이미 들어간 것은 다시 요구되지 않으므로, 둘을 합친 비용은 예전에 Starfire-III 하나가 단독으로 요구하던 것과 정확히 같습니다. 3,000 Thulium, 100,000 크레딧, Ship Fragment 25개, Velkonite Reinforced Plate 10개, Reinforced Hull Plate 1개, 그리고 2분입니다. 이미 Quantum Laser III가 있다면 Starfire-III 자체의 몫만 치르면 됩니다. 규칙은 아래에 나오는 Helios Beam의 규칙과 같습니다. Starfire-III는 소모한 Quantum Laser III의 인챈트 등급을 이어받고(신성한 Quantum Laser III로는 신성한 Starfire-III가 만들어집니다) 보너스는 다시 굴리며, 어느 Quantum Laser III를 쓸지 직접 고르고, 표준보다 높은 등급을 쓰기 전에는 카드가 먼저 묻고, Quantum Laser III는 장착되지 않은 상태여야 합니다. **먼저 함선에서 떼어 내세요**(장착한 증폭기는 인벤토리로 돌아갑니다). 수송 보관함에서도 꺼내야 합니다. 함선에 장착되어 있으면 조립 버튼에 “먼저 Quantum Laser III 해제”라고 표시됩니다.

**Helios Beam은 Starfire-III를 재료로 만듭니다.** 먼저 Starfire-III를 만들고(재료인 Quantum Laser III까지 합쳐 3,000 Thulium, 100,000 크레딧), Helios Beam이 그것을 소모합니다. [Master Drone](/wiki/06-Items/Drones.md)이 Slave Drone을 소모하는 것과 같습니다. Starfire-III에 이미 들어간 것은 다시 요구되지 않으므로, 둘을 합친 비용은 Helios Beam이 단독으로 요구하던 5,000 Thulium, Cataclysite, Power Core, Reinforced Hull Plate에, Orvium 플레이트 20장 대신 18장(Starfire-III의 Velkonite 플레이트 10장이 부족한 2장을 대신합니다)을 더하고, Helios Beam은 계열의 마지막 티어이므로 Dark Matter Plate 3개도 더한 것입니다. 이 밖에 치르는 것은 Starfire-III의 100,000 크레딧과 Ship Fragment 25개입니다. 규칙은 [모듈 업그레이드](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)와 같습니다. Helios Beam은 소모한 Starfire-III의 인챈트 등급을 이어받고(신성한 Starfire-III로는 신성한 Helios Beam이 만들어집니다) 보너스는 다시 굴리며, 여러 개를 보유하면 어느 Starfire-III를 쓸지 직접 고르고, 표준보다 높은 등급을 쓰기 전에는 카드가 먼저 묻습니다. Starfire-III는 장착되지 않은 상태여야 합니다. **먼저 함선에서 떼어 내세요**(장착한 증폭기는 인벤토리로 돌아갑니다). 수송 보관함에서도 꺼내야 합니다. 함선에 장착되어 있으면 조립 버튼에 “먼저 Starfire-III 해제”라고 표시됩니다.

플레이트의 출처는 다음과 같습니다.

- **Velkonite Reinforced Plate**(Quantum Laser III, Starfire-III)는 Velkonite로 단조하며, 단조소 레벨 1에서는 플레이트 1장에 광석 40개가 듭니다. **Orvium Reinforced Plate**(Helios Beam)는 Orvium으로 단조하며, 플레이트 1장에 광석 80개가 듭니다.
- **Dark Matter Plate**(Helios Beam에 3개)는 그 제작법을 연구한 뒤 어셈블리에서 Dark Matter 5개, Velkonite Reinforced Plate 1개, Orvium Reinforced Plate 1개, 250 Thulium으로 압착해 만듭니다. 3개에는 Dark Matter 15개가 들며, [블랙홀](/wiki/03-Mechanics/Black-Hole.md)에서 N.I.K.E. 로켓 평균 7.5발 분량입니다. 전체 과정은 [Dark Matter와 Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)에 있습니다.
- 광석은 Skylab의 수집기에서만 나옵니다. 레벨 5 Velkonite 수집기는 시간당 Velkonite를 18개 채굴하므로, Quantum Laser III의 플레이트는 채굴에 약 4시간, Starfire-III의 플레이트 10장(Quantum Laser III 단계에 2장, 자체 단계에 8장)은 약 22시간이 걸립니다. 가장 오래 걸리는 것은 Helios Beam입니다. 플레이트 18장에 Orvium 1,440개가 필요하며, 레벨 5 Orvium 수집기로 약 4일이 걸립니다. 여기에 Dark Matter Plate 3개에 들어가는 Orvium 플레이트 3장이 Orvium 240개, 약 17시간을 더합니다.
- 자원 창고는 레벨 1에서 광석을 종류별로 240개까지 보관합니다. 단조소 레벨 1에서 Velkonite 플레이트 6장이나 Orvium 플레이트 3장 분량입니다. 그러므로 그때그때 단조하거나(레벨 1에서 단조소의 배치는 플레이트 최대 10장) 창고를 업그레이드하세요.
- 단조한 플레이트는 함선이 착륙해 있는 동안 수거할 때까지 단조소에서 기다리며, 수거하면 일반 아이템으로 인벤토리에 들어옵니다.

Ship Fragment, Cataclysite, Power Core, Reinforced Hull Plate는 외계인이 드롭합니다. 각 재료의 모든 획득처와 용도는 [자원](/wiki/06-Items/Resources.md) 페이지에 있으며, [Bulwark](/wiki/04-Aliens/Bulwark.md)와 [Goombah](/wiki/04-Aliens/Goombah.md) 페이지의 전리품 목록에서 드롭량을 확인할 수 있습니다.

---

## 레이저 증폭기(Amp) {#laser-amplifiers-amps-}

레이저의 증폭기 슬롯에 직접 끼워 레이저의 특성을 강화합니다. **계열은 세 가지이며 각각 4단계**로, 실드 셀과 같은 방식으로 이름이 붙었습니다. **Damage Amp**는 고정 피해량을 더하고, **Crit Amp**는 치명타 확률과 고정 치명타 피해를 더하며, **Penetration Amp**는 대상의 흡수율에서 포인트를 깎습니다([아래](#shield-penetration-of-a-laser-hit)). 이것은 [부스터](/wiki/06-Items/Boosters.md)가 아닙니다. **Laser Damage Booster I**과 **Laser Damage Booster II**는 끼울 것이 없는 시간제 부스터(10시간 동안 레이저 피해량 +10%)입니다.

| 이름 | 희귀도 | 기본 피해량 증가 | 치명타 확률 증가 | 고정 치명타 피해 | 비용 |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Damage Amp I** | 하급 | +10 | +5% | +5 | 10,000 크레딧 |
| **Damage Amp II** | 고급 | +16 | +5% | +8 | 제작 전용 |
| **Damage Amp III** | 희귀 | +26 | +6% | +13 | 제작 전용 |
| **Damage Amp IV** | 영웅 | +38 | +7% | +20 | 제작 전용 |
| **Crit Amp I** | 하급 | +0 | +15% | +0 | 15,000 크레딧 |
| **Crit Amp II** | 고급 | +0 | +20% | +14 | 제작 전용 |
| **Crit Amp III** | 희귀 | +0 | +25% | +24 | 제작 전용 |
| **Crit Amp IV** | 영웅 | +0 | +25% | +44 | 제작 전용 |

| 이름 | 희귀도 | 실드 관통 | 비용 |
| :--- | :--- | :---: | :--- |
| **Penetration Amp I** | 하급 | +2% | 15,000 크레딧 |
| **Penetration Amp II** | 고급 | +4% | 제작 전용 |
| **Penetration Amp III** | 희귀 | +6% | 제작 전용 |
| **Penetration Amp IV** | 영웅 | +8% | 제작 전용 |

**각 계열의 첫 티어만 팝니다**, 상점에서. 나머지 셋은 [어셈블리](/wiki/06-Items/Overview.md#upgrading-modules)에서 한 티어 아래의 증폭기로 만들며, 먼저 Skylab에서 그 기술을 연구해야 합니다([연구](/wiki/03-Mechanics/Research.md)). 각 단계에는 Thulium, 외계인 드롭, 플레이트(티어 II와 III에는 Skylab에서 만든 Velkonite Reinforced Plate, 티어 IV에는 Dark Matter Plate 3개)가 들고, 새 증폭기는 소모한 증폭기의 인챈트 등급을 이어받으며 보너스는 다시 굴립니다([어셈블리의 모듈 업그레이드](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Penetration 단계에는 결정 렌즈가 더해집니다. 티어 IV 증폭기는 어느 것이나 [Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md) 3개를 요구하므로(모든 강화 계열의 마지막 티어가 그렇습니다), 티어 IV 증폭기의 기술은 먼저 그 플레이트의 기술을 요구합니다.

| 단계 | Thulium | 시간 | 한 티어 아래 증폭기에 더해 |
| :--- | ---: | ---: | :--- |
| Damage Amp II / Crit Amp II | 250 | 60초 | Cataclysite 10개, Velkonite Reinforced Plate 1개 |
| Damage Amp III / Crit Amp III | 1,000 | 60초 | Cataclysite 20개, Power Core 1개, Velkonite Reinforced Plate 2개 |
| Damage Amp IV / Crit Amp IV | 1,200 | 60초 | Cataclysite 30개, Power Core 1개, Dark Matter Plate 3개 |
| Penetration Amp II | 250 | 60초 | Daraxium 20개, Cataclysite 10개, Velkonite Reinforced Plate 1개 |
| Penetration Amp III | 1,000 | 60초 | Nyxite 30개, Cataclysite 20개, Power Core 1개, Velkonite Reinforced Plate 2개 |
| Penetration Amp IV | 1,200 | 90초 | Quorvium 40개, Cataclysite 30개, Power Core 1개, Dark Matter Plate 3개 |

Helios Beam과 티어 IV 증폭기 3개는 마지막 티어 부품 4개로, Dark Matter Plate 12개, Dark Matter 60개, N.I.K.E. 로켓 평균 30발 분량입니다. 모든 슬롯을 마지막 티어로 채운 Wraith에는 Dark Matter 900개가 들어갑니다([Dark Matter와 Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md#what-the-last-tier-asks-for)).

### 어느 증폭기를 어디에 쓸까 {#which-amp-goes-where}

피해 증폭기는 어떤 레이저에든 같은 양의 피해를 더하므로 **Quantum 레이저**에서 가치가 가장 큽니다. 치명타 증폭기는 레이저가 이미 내는 피해에 곱해지므로 레이저가 강할수록 가치가 커집니다. **Starfire-III**에서는 피해 계열과 동률이 되고, **Helios Beam**에서는 약 3.5% 앞섭니다. 레이저의 치명타 확률은 100%에서 멈춥니다. Crit Amp III나 Crit Amp IV 세 개를 달면 Helios Beam이 정확히 그 값에 이릅니다. Penetration Amp는 피해도 치명타 확률도 더하지 않습니다. 실드가 공격의 대부분을 받아 낼 함선을 상대하기 위한 것입니다([아래](#when-is-a-penetration-amp-worth-a-slot)).

같은 증폭기로 채우면 레이저는 항상 바로 아래 레이저보다 강하므로, 더 좋은 증폭기가 더 좋은 레이저를 대신할 수는 없습니다. Damage Amp IV 세 개를 단 Quantum Laser III는 Damage Amp I 세 개를 단 Helios Beam보다 피해량이 낮습니다(같은 인챈트 등급의 부품끼리 비교한 경우입니다. 신성한 등급 이상으로 단련하고 최고의 보너스를 굴린 Quantum Laser III와 Damage Amp IV라면, Damage Amp I을 단 평범한 Helios Beam을 넘어설 수 있으며, 신성한 등급에서는 간발의 차입니다).


---

## 레이저 탄약 {#laser-ammunition}

레이저 일제 사격의 피해를 배가시키는 소모성 배터리입니다.

| 이름 | 희귀도 | 피해 배율 | 실드 관통 | 개당 가격 |
| :--- | :--- | :---: | :---: | :--- |
| **Standard Battery** | 일반 | 1.0x | – | 5 크레딧 |
| **Advanced Plasma** | 희귀 | 2.0x | – | 0.5 Thulium |
| **Ultra Core** | 희귀 | 3.0x | 5% | 1.0 Thulium |
| **Experimental Fusion Core** | 영웅 | 4.0x | 10% | 2.2 Thulium |
| **Siphon Battery** | 희귀 | 1.0x, 실드에만 | – | 0.25 Thulium |

**실드 관통**은 일제 사격의 매 공격마다 대상의 흡수율에서 차감됩니다. 즉 실드는 대상의 흡수율에서 관통을 뺀 몫을 받습니다([실드 시스템](/wiki/03-Mechanics/Shields.md#shield-penetration) 참고). Penetration Amp와 드론 편대는 탄약의 관통에 더해지며, 그 합계 전체는 [이 페이지 아래](#shield-penetration-of-a-laser-hit)에 있습니다. 80%(가장 좋은 실드에 가장 좋은 셀)인 함선을 상대로 x4 탄약의 10%는 실드가 공격의 70%를, 선체가 30%를 받게 합니다. 실드에 비해 선체가 작은 함선에 가장 큰 의미가 있으며, 80%인 아주 큰 함선은 어느 쪽이든 똑같이 버팁니다. 외계인에게는 이렇다 할 흡수율 능력치가 없으며(외계인의 실드는 공격의 80%를 받습니다), 관통은 거기서도 차감됩니다.

### Siphon Battery

Siphon Battery는 선체를 부수는 대신 실드를 빼앗는 탄약입니다. **대상의 실드에 x1 피해를 직접** 입히고, 같은 양을 최대치까지 **자신의 실드**에 더합니다. 다른 탄약과 마찬가지로 퀵슬롯의 탄약 선택창에서 고르세요(청록색 소용돌이가 그려진 타일입니다). 광선을 쏘지 않습니다. 가늘고 희미한 청록색 탐침이 대상에게 뻗어 나가고, 닿은 자리에서 대상의 실드가 청록색으로 번쩍이며, 빼앗은 실드는 빛나는 청록색 입자(3~10개, 많이 빼앗을수록 더 많이)가 약 0.5초 동안 하나씩 차례로 함선으로 흘러 들어오는 모습으로 눈에 보입니다. 입자가 하나 도착할 때마다 실드가 맥동합니다. 시야에 들어온 모든 파일럿의 Siphon Battery도 누구에게서 빼앗든(외계인, 다른 파일럿, 기업 파일럿의 함선) 똑같이 보입니다.

- **실드 전용**: 선체는 절대 건드리지 않고, 대상의 흡수율로 피해가 나뉘지도 않으며, Siphon Battery로는 아무것도 파괴할 수 없습니다. 피해량은 대상의 실드에 남아 있는 양을 넘지 못합니다.
- **빼앗을 것이 없을 때**: 실드가 남지 않은 대상에게는 아무것도 빼앗지 못하고 얻는 것도 없습니다. 일제 사격은 다른 탄약과 마찬가지로 레이저 1개당 배터리 1개씩 소모됩니다. 탐침과 선체에서 둔하게 깜박이는 빛만 보이고 입자는 나타나지 않습니다.
- **획득**: 자신의 실드는 최대치를 넘지 않으며, 실드를 흡수해도 자신의 실드 재생이 늦춰지지 않습니다.
- **외계인과 파일럿** 모두 빼앗을 실드가 있습니다. 외계인에게서 실드를 빼앗으면 [첫 타격 선점](/wiki/03-Mechanics/Combat.md)에서 공격으로 인정되고, 실드가 없어 빼앗지 못하면 인정되지 않습니다. 반격만 하는 Seeker나 Goombah도 다른 공격과 마찬가지로 깨웁니다.
- **치명타**도 적용됩니다. 치명타 일제 사격은 1.5배를 빼앗으며 숫자도 치명타로 표시됩니다. 입자는 더 크고 밝으며, 대상의 실드는 더 강하게 번쩍입니다.
- [기업 파일럿](/wiki/03-Mechanics/Company-Pilots.md)은 기본 x1 탄약을 사용합니다.

---

## 레이저 공격의 실드 관통 {#shield-penetration-of-a-laser-hit}

레이저 공격은 모두 대상의 흡수율에서 포인트를 깎으며, 그 출처는 최대 세 가지이고 서로 더해집니다. 내 **탄약**(Ultra Core 5%, Experimental Fusion Core 10%), 내 **Penetration Amp**, 그리고 **드론 편대**(Gemini +9%, Stiletto +16%, [드론 편대](/wiki/03-Mechanics/Formations.md))입니다. 합계는 레이저는 **50%에서 멈추고**, 직접 로켓은 40%에서 멈춥니다([로켓](/wiki/06-Items/Rockets.md)). 그러면 실드는 대상의 흡수율에서 공격의 관통을 뺀 몫을 받고, 선체가 나머지를 받습니다([실드 시스템](/wiki/03-Mechanics/Shields.md#shield-penetration)).

- **증폭기는 레이저의 평균으로 계산됩니다.** 일제 사격은 한 번의 공격이므로, 게임은 각 레이저의 증폭기 관통을 더하고(드론 안의 레이저도 포함) 치명타 확률과 마찬가지로 각 레이저를 피해량으로 가중해 레이저 전체의 평균을 냅니다. 모든 레이저에 Penetration Amp IV 3개씩이면 24%, 레이저 12개 중 하나에 Penetration Amp IV 하나면 0.67%입니다. Wraith는 레이저가 12개, 증폭기 슬롯이 36개이며, 24%를 내려면 36개를 모두 채워야 합니다.
- **격납고에 표시됩니다.** 격납고의 전투 능력치에는 모든 기체에 증폭기 수치를 보여 주는 **관통** 타일이 있습니다(Penetration Amp가 없으면 0.0%). 탄약과 편대는 그 수치에 들어 있지 않습니다. 타일에 마우스를 올리면 상한을 읽을 수 있습니다. 레이저 명중의 합계는 50%, 로켓은 40%에서 멈춥니다.
- **최강의 레이저는 정확히 상한에 닿습니다.** Experimental Fusion Core(10%), Stiletto(16%), 모든 레이저에 Penetration Amp IV 3개(24%)면 합계가 50%입니다.
- **Penetration Amp IV에 붙은 대장간 보너스는 그 구성에서는 낭비됩니다.** Penetration Amp도 다른 증폭기처럼 단련할 수 있으며, 하나뿐인 보너스가 관통을 곱합니다. 영원한 등급의 보너스(+9%~+15%)는 Penetration Amp IV를 8이 아니라 8.7~9.2포인트로 만듭니다. 하지만 10 + 16 + 24가 이미 상한 50%이고, 더해진 만큼은 잘려 나갑니다(영원한 등급 셋이면 53.6%가 되지만 50%로 잘립니다).

| 레이저 일제 사격 | 탄약 | 증폭기(슬롯 3개) | 편대 | 합계 |
|---|---|---|---|---|
| Experimental Fusion Core 단독 | 10% | – | – | **10%** |
| Fusion Core + Gemini | 10% | – | 9% | **19%** |
| Fusion Core + Stiletto(Penetration Amp 이전의 최강) | 10% | – | 16% | **26%** |
| Fusion Core + 3 Penetration Amp I | 10% | 6% | – | **16%** |
| Fusion Core + 3 Penetration Amp II | 10% | 12% | – | **22%** |
| Fusion Core + 3 Penetration Amp III | 10% | 18% | – | **28%** |
| Fusion Core + 3 Penetration Amp IV | 10% | 24% | – | **34%** |
| Fusion Core + 3 Penetration Amp IV + Gemini | 10% | 24% | 9% | **43%** |
| Ultra Core + Penetration Amp IV 3개 + Stiletto(평소 쓰는 최강) | 5% | 24% | 16% | **45%** |
| Fusion Core + Penetration Amp IV 3개 + Stiletto(최강의 레이저) | 10% | 24% | 16% | **50%** |

그것이 대상의 실드에 하는 일입니다. 각 칸은 공격 중 **실드가 받는 몫 / 선체가 받는 몫**입니다.

| 방어 측(흡수율) | 증폭기 없음 | Fusion Core 단독(10%) | 이전: Fusion Core + Stiletto(26%) | Fusion Core + 3 Penetration Amp IV(34%) | 최강의 레이저(50%) |
|---|---|---|---|---|---|
| Light Shield Core, 셀 없음(45%) | 45 / 55 | 35 / 65 | 19 / 81 | 11 / 89 | 0 / 100 |
| Heavy Shield Core, 셀 없음(50%) | 50 / 50 | 40 / 60 | 24 / 76 | 16 / 84 | 0 / 100 |
| Light Shield Core + Absorption Shield Cell IV(55%) | 55 / 45 | 45 / 55 | 29 / 71 | 21 / 79 | 5 / 95 |
| Heavy Shield Core + Capacity Shield Cell IV 3개(65%) | 65 / 35 | 55 / 45 | 39 / 61 | 31 / 69 | 15 / 85 |
| 기본으로 가장 좋은 실드(80%) | 80 / 20 | 70 / 30 | 54 / 46 | 46 / 54 | 30 / 70 |
| 가장 좋은 실드, 영원한 등급 대장간(최고 롤)과 시즌 상점 34레벨(95.4%) | 95 / 5 | 85 / 15 | 69 / 31 | 61 / 39 | 45 / 55 |
| 가장 좋은 실드, 영원한 등급 대장간(최고 롤)과 시즌 상점 최대치(102%) | 100 / 0 | 92 / 8 | 76 / 24 | 68 / 32 | 52 / 48 |
| 모든 외계인(80%) | 80 / 20 | 70 / 30 | 54 / 46 | 46 / 54 | 30 / 70 |

최강의 레이저는 셀이 없는 실드 코어를 비웁니다(선체가 공격 전체를 받습니다). 셀이 있는 코어는 공격의 일부를 지키고, 가장 좋은 실드는 30%를 지킵니다(버프가 있으면 45%). 로켓은 실드를 비우지 못합니다. 상한이 40%이기 때문입니다.

### Penetration Amp는 언제 슬롯을 쓸 만한가? {#when-is-a-penetration-amp-worth-a-slot}

**Penetration Amp는 약 95%를 넘는 흡수율(시즌 상점, 대장간, Rampart 구성)에 맞섭니다. 기본으로 가장 좋은 실드(80%)를 상대로는 같은 티어의 Crit Amp가 여전히 약 10% 더 빠르며, Penetration Amp는 외계인을 같은 티어의 Damage Amp나 Crit Amp보다 빨리 처치하지 못합니다.**

- **피해는 주지 않습니다.** Helios Beam에서 Penetration Amp IV 3개는 일제 사격당 피해 187(탄약 x1, 무작위와 치명타의 평균)을 내고, Damage Amp IV 3개는 356, Crit Amp IV 3개는 369로, 대략 절반입니다. 되찾는 것은 실드의 몫이므로 실드에 비해 선체가 작고 흡수율이 높을 때에만 보람이 있습니다. 큰 선체가 어차피 버티는 Wraith나 Ironclad를 상대로는 평범한 Damage나 Crit 구성이 더 빠릅니다.
- **외계인.** 그 실드는 공격의 80%에서 내 관통을 뺀 몫을 받으므로 외계인에게도 통하지만, 같은 티어의 Damage Amp나 Crit Amp가 여전히 더 빨리 처치합니다.
- **비용.** Penetration Amp IV마다 Dark Matter Plate 3개(Dark Matter 15개)가 필요합니다. 티어 IV 증폭기는 모두 같으므로, 36개 슬롯을 모두 채우는 Wraith에는 플레이트 108개, Dark Matter 540개가 필요합니다.
