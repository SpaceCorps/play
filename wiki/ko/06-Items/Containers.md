<!-- wiki-i18n source: 9cb279aeecb3bbc8 -->
<!-- wiki-i18n title: 컨테이너 -->
# 컨테이너 {#containers}

<!-- wiki-search: 컨테이너; container; containers; case; crate; lootbox; loot box; 랜덤박스; 확률; 드롭률; 보장; 천장; pity; 릴; 개봉; 금고; 도가니; 기록보관소; 캐니스터; 랙; odds; drop rate; vault; crucible; archive; canister; rack -->

**컨테이너**는 Mission Control의 봉인된 발견물입니다. 컨테이너를 개봉하면 서버가 표에서 보상을 하나 추첨하고, 그 표에 있는 모든 보상의 확률은 이 페이지에 실려 있습니다. 게임의 컨테이너 페이지도 같은 표를 보여 줍니다.

> [!NOTE]
> **컨테이너는 게임에서 얻는 무작위 보상입니다. 판매되지 않으며, 확률은 여기에 공개되어 있습니다.** 컨테이너는 구매, 거래, 선물을 할 수 없습니다.

## 컨테이너란 {#what-a-container-is}

- **직접 얻습니다.** 컨테이너는 게임에서 얻습니다. 가격도 열쇠도 없습니다. 상점에서도, 다른 어디서도 팔지 않습니다.
- **나만의 것입니다.** 컨테이너는 계정에 묶여 있습니다. 거래하거나, 친구에게 주거나, [경매장](/wiki/03-Mechanics/Auction.md)에 올릴 수 없고, 컨테이너에서 나온 것도 그곳에 올릴 수 없습니다.
- **모든 파일럿이 같습니다.** 프리미엄은 아무것도 바꾸지 않습니다. 개봉 횟수가 늘지도, 확률이 좋아지지도 않습니다.
- **초기화 후에도 남습니다.** 개봉하지 않은 컨테이너는 [초기화](/wiki/03-Mechanics/Wipe-Timeline.md)가 와도 계정에 남습니다. 초기화가 보상에 하는 일은 [초기화](#the-wipe)에 있습니다.
- **기지에서 개봉합니다.** 컨테이너는 정박한 상태에서 컨테이너 페이지에서 개봉합니다. 보상은 개봉을 누르는 순간 서버가 추첨하며, 누르는 행동 자체는 아무것도 바꾸지 않습니다. 무엇이 영향을 주는지는 [보상이 정해지는 방식](#how-a-prize-is-chosen)에 있습니다.

## 컨테이너를 얻는 곳 {#where-containers-come-from}

<!-- containers-sources:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

컨테이너는 다음 경로로 받습니다.

- 게임 관리자에게서
- 초기화 때 계급 보상으로
- 출석 달력에서
- 업적 보상으로

<!-- containers-sources:end -->

## 다섯 종류의 컨테이너 {#the-five-containers}

<!-- containers-glance:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 컨테이너 | 들어 있는 것 | 적합한 대상 | 초기화 때 닫힘 | 보장 | 가장 희귀한 보상 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **표본 금고 (Specimen Vault)** | 이것저것 조금씩: 크레딧, Thulium, 탄약, 로켓, 장비, 플레이트, Dark Matter, 부스터, 색상 | 모든 파일럿 | 시즌 30일째부터 | 개봉 10회 안에 희귀 등급 이상의 보상 | 60,000 Thulium; 12,000,000 크레딧: 각각 0.100% |
| **주조소 도가니 (Foundry Crucible)** | 탄약, 로켓, 레이저, 증폭기, 실드 셀, 추진기, 장비, 그리고 함선 5척 | 레벨 5 이상 | 시즌 30일째부터 | 개봉 8회 안에 희귀 등급 이상의 보상 | 함선: Wraith: 0.020% |
| **크로마 기록보관소 (Chroma Archive)** | 외형만: 스킨, 색상, 배기 효과, 오라 | 모든 파일럿 | 계속 열려 있음 | 개봉 12회 안에 영웅 등급 이상의 보상 | Crystal Ice; Comet; Halo: 각각 0.667% |
| **탐사 캐니스터 (Survey Canister)** | Skylab 광석, 플레이트, Dark Matter, Cluster Chunks, Thulium | Skylab 코어 10 이상 | 시즌 30일째부터 | 개봉 8회 안에 희귀 등급 이상의 보상 | 32 × Dark Matter Plate; 50,000 Thulium: 각각 0.150% |
| **시약 랙 (Reagent Rack)** | 부스터, EMP Charges, Energetic Walls, 탄약 | 레벨 4 이상 | 시즌 30일째부터 | 개봉 10회 안에 희귀 등급 이상의 보상 | **풀 스펙트럼**; Cloaking CPU L: 각각 0.100% |

<!-- containers-glance:end -->

**적합**은 참고용일 뿐입니다. 게임은 어떤 레벨에서든 어떤 컨테이너든 열 수 있게 해 줍니다.

## 등급 {#grades}

모든 보상에는 **등급**이 있으며, 게임의 희귀도 단어 중 하나입니다. 등급은 추첨에서 가장 먼저 정해지는 것입니다. 릴에서는 보상 타일의 테두리로 나타나며, 색과 모양이 함께 쓰여 색만으로 구분하지 않게 되어 있습니다.

| 등급 | 색 | 모양 |
| :--- | :--- | :--- |
| 일반 | 회색 | 원 |
| 고급 | 초록 | 정사각형 |
| 희귀 | 파랑 | 마름모 |
| 영웅 | 보라 | 육각형 |
| 신화 | 분홍 | 별 |
| 전설 | 금색 | 왕관 |

각 컨테이너에는 등급마다 고유한 확률이 있으며 아래에 나와 있습니다. 보유한 것이 등급의 확률을 바꾸는 일은 없습니다.

## 표본 금고 (Specimen Vault) {#specimen-vault}

*Mission Control의 외계 기록관들은 한 분야로 분류할 수 없는 발견물을 번호가 붙은 금고에 봉인해 개봉하지 않은 채 보냅니다. 파일럿이 봉인을 뜯기 전까지는 기지의 누구도 금고 안에 무엇이 있는지 모릅니다.*

### 등급별 확률 {#specimen-vault-grades}

<!-- containers-specimen-vault-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 등급 | 확률 | 포함된 보상 |
| :--- | ---: | ---: |
| 일반 | 38.000% | 9 |
| 고급 | 38.000% | 8 |
| 희귀 | 17.000% | 8 |
| 영웅 | 5.500% | 5 |
| 신화 | 1.300% | 4 |
| 전설 | 0.200% | 2 |

<!-- containers-specimen-vault-grades:end -->

### 모든 보상 {#specimen-vault-prizes}

<!-- containers-specimen-vault-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 등급 | 보상 | 확률 |
| :--- | :--- | ---: |
| 일반 | 50,000 크레딧 | 5.000% |
| 일반 | 250 Thulium | 4.000% |
| 일반 | 10,000 × Standard Battery | 4.000% |
| 일반 | 500 × Advanced Plasma | 4.000% |
| 일반 | 250 × Ultra Core | 3.000% |
| 일반 | **로켓 랙 I**: 4개 중 하나를 100개 (확률 동일): Ember I, Lancet I, Rivet I, Scatter I | 6.000% |
| 일반 | **단조 가루**: 1,500 × Daraxium + 1,500 × Nyxite | 3.000% |
| 일반 | 4,000 × Ship Fragment | 3.000% |
| 일반 | 1시간 Experience Booster | 6.000% |
| 고급 | 150,000 크레딧 | 6.000% |
| 고급 | 750 Thulium | 6.000% |
| 고급 | 750 × Ultra Core | 4.500% |
| 고급 | 340 × Experimental Fusion Core | 4.000% |
| 고급 | **로켓 랙 II**: 4개 중 하나를 190개 (확률 동일): Ember II, Lancet II, Rivet II, Scatter II | 6.000% |
| 고급 | 10 × Velkonite Reinforced Plate | 4.000% |
| 고급 | 1시간 Laser Damage Booster I | 4.000% |
| 고급 | **색상 샘플**: 11개 중 하나 (확률 동일): Cobalt, Indigo, Violet, Magenta, Crimson, Ember, Sunset, Gold, Emerald, Jade, Teal | 3.500% |
| 희귀 | 400,000 크레딧 | 2.500% |
| 희귀 | 2,000 Thulium | 2.500% |
| 희귀 | 10 × Dark Matter | 1.500% |
| 희귀 | **로켓 랙 III**: 4개 중 하나를 400개 (확률 동일): Ember III, Lancet III, Rivet III, Scatter III | 2.000% |
| 희귀 | 1,000 × Experimental Fusion Core | 1.500% |
| 희귀 | 9 × Orvium Reinforced Plate | 1.500% |
| 희귀 | 4시간 Laser Damage Booster I | 1.500% |
| 희귀 | **티어 II 부품 1개**: 4개 중 하나 (확률 동일): Absorption Shield Cell II, Capacity Shield Cell II, Impulse Thruster II, Momentum Thruster II | 4.000% |
| 영웅 | 1,200,000 크레딧 | 1.200% |
| 영웅 | 6,000 Thulium | 1.200% |
| 영웅 | 30 × Dark Matter | 0.900% |
| 영웅 | 26 × Orvium Reinforced Plate | 0.900% |
| 영웅 | **티어 III 부품 1개**: 5개 중 하나 (확률 동일): Absorption Shield Cell III, Capacity Shield Cell III, Impulse Thruster III, Momentum Thruster III, Starfire-III | 1.300% |
| 신화 | 18,000 Thulium | 0.400% |
| 신화 | 12 × Dark Matter Plate | 0.300% |
| 신화 | Helios Beam | 0.300% |
| 신화 | **티어 IV 증폭기 1개**: 3개 중 하나 (확률 동일): Damage Amp IV, Crit Amp IV, Penetration Amp IV | 0.300% |
| 전설 | 60,000 Thulium | 0.100% |
| 전설 | 12,000,000 크레딧 | 0.100% |

<!-- containers-specimen-vault-prizes:end -->

**색상 샘플**은 아직 없는 색상 하나를 줍니다. 샘플의 색상을 모두 가지고 있으면 대신 분해 Thulium를 줍니다([중복과 분해](#duplicates-and-salvage)).

### 보장 {#specimen-vault-guarantee}

<!-- containers-specimen-vault-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **보장**: 개봉 10회마다 최소 한 번은 희귀 등급 이상의 보상
- **보장이 없을 때 희귀 등급 이상의 보상이 나올 확률**: 24.000%
- **보장이 있을 때, 많은 횟수를 개봉한 경우**: 25.649%
- **보장이 강제하는 개봉**: 2.170%
- **그런 보상 사이의 평균 개봉 횟수**: 3.899

<!-- containers-specimen-vault-guarantee:end -->

## 주조소 도가니 (Foundry Crucible) {#foundry-crucible}

*Dormant의 주조소는 마지막 한 배치가 도가니에 남은 채 식어 버렸습니다. 탄약과 조립된 장비, 그리고 가장 깊은 곳에는 끝내 완성되지 못한 선체가 있습니다. Mission Control의 기술자들이 폐허에서 도가니를 잘라 내 봉인된 채로 파일럿에게 건네줍니다. 어느 도가니에 선체가 들어 있는지는 아무도 말할 수 없기 때문입니다.*

### 등급별 확률 {#foundry-crucible-grades}

<!-- containers-foundry-crucible-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 등급 | 확률 | 포함된 보상 |
| :--- | ---: | ---: |
| 일반 | 45.000% | 6 |
| 고급 | 30.000% | 7 |
| 희귀 | 16.000% | 6 |
| 영웅 | 6.500% | 6 |
| 신화 | 2.200% | 5 |
| 전설 | 0.300% | 2 |

<!-- containers-foundry-crucible-grades:end -->

### 모든 보상 {#foundry-crucible-prizes}

<!-- containers-foundry-crucible-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 등급 | 보상 | 확률 |
| :--- | :--- | ---: |
| 일반 | 30,000 × Standard Battery | 7.000% |
| 일반 | 1,500 × Advanced Plasma | 7.000% |
| 일반 | 750 × Ultra Core | 7.000% |
| 일반 | 340 × Experimental Fusion Core | 5.000% |
| 일반 | **로켓 랙 I**: 4개 중 하나를 300개 (확률 동일): Ember I, Lancet I, Rivet I, Scatter I | 11.000% |
| 일반 | **레이저 키트**: Quantum Laser II + Damage Amp I + Crit Amp I + Penetration Amp I | 8.000% |
| 고급 | 2,250 × Ultra Core | 4.500% |
| 고급 | 1,020 × Experimental Fusion Core | 4.500% |
| 고급 | **로켓 랙 II**: 4개 중 하나를 560개 (확률 동일): Ember II, Lancet II, Rivet II, Scatter II | 8.500% |
| 고급 | Basic Shield Core | 4.500% |
| 고급 | **티어 II 증폭기 3종 세트**: Damage Amp II + Crit Amp II + Penetration Amp II | 4.000% |
| 고급 | Repair Drone IV | 3.900% |
| 고급 | 함선: Nomad | 0.100% |
| 희귀 | 1,800 × Experimental Fusion Core | 2.500% |
| 희귀 | **로켓 랙 III**: 4개 중 하나를 500개 (확률 동일): Ember III, Lancet III, Rivet III, Scatter III | 3.000% |
| 희귀 | Quantum Laser III | 2.400% |
| 희귀 | **티어 II 부품 1개**: 4개 중 하나 (확률 동일): Absorption Shield Cell II, Capacity Shield Cell II, Impulse Thruster II, Momentum Thruster II | 4.500% |
| 희귀 | **티어 III 증폭기 1개**: 3개 중 하나 (확률 동일): Damage Amp III, Crit Amp III, Penetration Amp III | 3.500% |
| 희귀 | 함선: Paragon | 0.100% |
| 영웅 | **티어 III 셀 또는 추진기 1개**: 4개 중 하나 (확률 동일): Absorption Shield Cell III, Capacity Shield Cell III, Impulse Thruster III, Momentum Thruster III | 3.000% |
| 영웅 | Starfire-III | 1.200% |
| 영웅 | Heavy Shield Core | 1.200% |
| 영웅 | Cloaking CPU M | 1.000% |
| 영웅 | 함선: Storm | 0.050% |
| 영웅 | 함선: Ironclad | 0.050% |
| 신화 | Helios Beam | 0.600% |
| 신화 | **티어 IV 셀 또는 추진기 1개**: 4개 중 하나 (확률 동일): Absorption Shield Cell IV, Capacity Shield Cell IV, Impulse Thruster IV, Momentum Thruster IV | 0.700% |
| 신화 | **티어 IV 증폭기 1개**: 3개 중 하나 (확률 동일): Damage Amp IV, Crit Amp IV, Penetration Amp IV | 0.480% |
| 신화 | Cloaking CPU L | 0.400% |
| 신화 | 함선: Wraith | 0.020% |
| 전설 | **헬리오스 무기고**: Helios Beam + Damage Amp IV + Crit Amp IV + Penetration Amp IV | 0.150% |
| 전설 | 50,000 Thulium | 0.150% |

<!-- containers-foundry-crucible-prizes:end -->

함선은 기본 확률과 함께 나열되어 있습니다. 이미 보유한 함선은 나오지 않으므로, 내 확률은 이 표와 조금 다를 수 있습니다. [함선](#the-ships)을 보세요.

### 보장 {#foundry-crucible-guarantee}

<!-- containers-foundry-crucible-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **보장**: 개봉 8회마다 최소 한 번은 희귀 등급 이상의 보상
- **보장이 없을 때 희귀 등급 이상의 보상이 나올 확률**: 25.000%
- **보장이 있을 때, 많은 횟수를 개봉한 경우**: 27.781%
- **보장이 강제하는 개봉**: 3.708%
- **그런 보상 사이의 평균 개봉 횟수**: 3.600

<!-- containers-foundry-crucible-guarantee:end -->

## 크로마 기록보관소 (Chroma Archive) {#chroma-archive}

*Dormant는 보라색 줄무늬가 있는 자흑색 결정으로 건물을 지었고, 기록관들은 색을 얇은 유리판에 보관했습니다. 그 유리판은 닿는 것을 무엇이든 다시 칠합니다. 크로마 기록보관소는 그 판을 봉인해 쌓아 둔 것으로, Mission Control의 색채 담당자들이 색인을 붙였고 파일럿이 열기 전에는 아무도 읽지 못했습니다.*

크로마 기록보관소는 먼저 등급을 추첨하고, 그다음 그 등급에서 아직 가지고 있지 않은 외형 하나를 추첨합니다. 모든 외형의 확률은 같습니다. 컬렉션은 보상 하나이며, 그 컬렉션의 아직 없는 스킨을 모두 줍니다. 표의 확률은 그 등급의 외형을 하나도 가지고 있지 않은 파일럿 기준입니다. 모을수록 추첨에 남는 외형이 줄어들어 확률이 올라갑니다. 외형 자체는 [코스메틱](/wiki/06-Items/Cosmetics.md)을 보세요.

### 등급별 확률 {#chroma-archive-grades}

<!-- containers-chroma-archive-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 등급 | 확률 | 포함된 외형 |
| :--- | ---: | ---: |
| 일반 | 6.000% | 1 |
| 고급 | 50.000% | 14 |
| 희귀 | 30.000% | 8 |
| 영웅 | 12.000% | 12 |
| 신화 | 2.000% | 3 |
| 전설 | 0.000% | – |

<!-- containers-chroma-archive-grades:end -->

### 모든 보상 {#chroma-archive-prizes}

<!-- containers-chroma-archive-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 등급 | 외형 | 그 등급의 외형이 하나도 없을 때의 확률 |
| :--- | :--- | ---: |
| 일반 | Glow (오라) | 6.000% |
| 고급 | Company Supporter (컬렉션) | 3.571% |
| 고급 | Cobalt (색상) | 3.571% |
| 고급 | Indigo (색상) | 3.571% |
| 고급 | Violet (색상) | 3.571% |
| 고급 | Magenta (색상) | 3.571% |
| 고급 | Crimson (색상) | 3.571% |
| 고급 | Ember (색상) | 3.571% |
| 고급 | Sunset (색상) | 3.571% |
| 고급 | Gold (색상) | 3.571% |
| 고급 | Emerald (색상) | 3.571% |
| 고급 | Jade (색상) | 3.571% |
| 고급 | Teal (색상) | 3.571% |
| 고급 | Twin (배기 효과) | 3.571% |
| 고급 | Breath (오라) | 3.571% |
| 희귀 | Nature White (컬렉션) | 3.750% |
| 희귀 | Sunrise Orbit (컬렉션) | 3.750% |
| 희귀 | Seeker Burnt (색상) | 3.750% |
| 희귀 | Pirate Brick (색상) | 3.750% |
| 희귀 | Pulse (배기 효과) | 3.750% |
| 희귀 | Helix (배기 효과) | 3.750% |
| 희귀 | Motes (오라) | 3.750% |
| 희귀 | Shimmer (오라) | 3.750% |
| 영웅 | Midnight Gala (컬렉션) | 1.000% |
| 영웅 | Blue Marble (컬렉션) | 1.000% |
| 영웅 | Mimosa (컬렉션) | 1.000% |
| 영웅 | Olive Branch (컬렉션) | 1.000% |
| 영웅 | Steady Pulse (컬렉션) | 1.000% |
| 영웅 | Hollow Night (컬렉션) | 1.000% |
| 영웅 | Dormant Void (색상) | 1.000% |
| 영웅 | Ancient Amethyst (색상) | 1.000% |
| 영웅 | Embers (배기 효과) | 1.000% |
| 영웅 | Gradient (배기 효과) | 1.000% |
| 영웅 | Sparkle (오라) | 1.000% |
| 영웅 | Wreath (오라) | 1.000% |
| 신화 | Crystal Ice (색상) | 0.667% |
| 신화 | Comet (배기 효과) | 0.667% |
| 신화 | Halo (오라) | 0.667% |

<!-- containers-chroma-archive-prizes:end -->

### 보장 {#chroma-archive-guarantee}

<!-- containers-chroma-archive-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **보장**: 개봉 12회마다 최소 한 번은 영웅 등급 이상의 보상
- **보장이 없을 때 영웅 등급 이상의 보상이 나올 확률**: 14.000%
- **보장이 있을 때, 많은 횟수를 개봉한 경우**: 16.740%
- **보장이 강제하는 개봉**: 3.186%
- **그런 보상 사이의 평균 개봉 횟수**: 5.974

<!-- containers-chroma-archive-guarantee:end -->

## 탐사 캐니스터 (Survey Canister) {#survey-canister}

*탐사 프로브는 Skylab에서 우주 지도의 안개 속으로 날아가고, 각각 시추 시료가 담긴 봉인된 캐니스터가 되어 돌아옵니다. 아무도 지도에 올리지 못한 광맥의 광석, 이상 현상, 그리고 때로는 지도보다 오래된 무언가의 파편이 들어 있습니다. Mission Control은 캐니스터를 셀별로 분류하고, 해독은 Skylab의 주인에게 맡깁니다.*

### 등급별 확률 {#survey-canister-grades}

<!-- containers-survey-canister-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 등급 | 확률 | 포함된 보상 |
| :--- | ---: | ---: |
| 일반 | 45.000% | 8 |
| 고급 | 30.000% | 7 |
| 희귀 | 16.000% | 6 |
| 영웅 | 6.500% | 5 |
| 신화 | 2.200% | 3 |
| 전설 | 0.300% | 2 |

<!-- containers-survey-canister-grades:end -->

### 모든 보상 {#survey-canister-prizes}

<!-- containers-survey-canister-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 등급 | 보상 | 확률 |
| :--- | :--- | ---: |
| 일반 | 240 × Velkonite (Skylab으로) | 7.000% |
| 일반 | 160 × Orvium (Skylab으로) | 7.000% |
| 일반 | 1,300 × Reinforced Hull Plate | 5.000% |
| 일반 | 9,000 × Ship Fragment | 6.000% |
| 일반 | **단조 크리스털**: 4,000 × Cataclysite + 3,000 × Quorvium | 5.000% |
| 일반 | 450 × Power Core | 5.000% |
| 일반 | 450 Thulium | 5.000% |
| 일반 | 4 × Regular Cluster Chunk | 5.000% |
| 고급 | 780 × Velkonite (Skylab으로) | 5.000% |
| 고급 | 510 × Orvium (Skylab으로) | 5.000% |
| 고급 | 19 × Velkonite Reinforced Plate | 4.000% |
| 고급 | 7 × Dark Matter | 5.000% |
| 고급 | 8 × Ancient Control Unit | 3.000% |
| 고급 | 1,450 Thulium | 4.000% |
| 고급 | 3 × Mythical Cluster Chunk | 4.000% |
| 희귀 | 17 × Dark Matter | 3.500% |
| 희귀 | 15 × Orvium Reinforced Plate | 3.000% |
| 희귀 | 1,900 × Velkonite (Skylab으로) | 2.500% |
| 희귀 | 1,230 × Orvium (Skylab으로) | 2.500% |
| 희귀 | 2 × Legendary Cluster Chunk | 1.500% |
| 희귀 | 3,500 Thulium | 3.000% |
| 영웅 | 45 × Dark Matter | 1.500% |
| 영웅 | 39 × Orvium Reinforced Plate | 1.200% |
| 영웅 | **혼합 플레이트 상자**: 60 × Velkonite Reinforced Plate + 20 × Orvium Reinforced Plate | 1.200% |
| 영웅 | 9,000 Thulium | 1.500% |
| 영웅 | 6 × Dark Matter Plate | 1.100% |
| 신화 | 13 × Dark Matter Plate | 0.900% |
| 신화 | 20,000 Thulium | 0.800% |
| 신화 | 100 × Dark Matter | 0.500% |
| 전설 | 32 × Dark Matter Plate | 0.150% |
| 전설 | 50,000 Thulium | 0.150% |

<!-- containers-survey-canister-prizes:end -->

*(Skylab으로)*라고 표시된 광석은 자원 저장소의 여유가 허용하는 만큼 Skylab의 광석 창고에 들어갑니다. 나머지는 같은 광석으로 인벤토리에 도착합니다. [Skylab](/wiki/03-Mechanics/Skylab.md)을 보세요.

### 보장 {#survey-canister-guarantee}

<!-- containers-survey-canister-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **보장**: 개봉 8회마다 최소 한 번은 희귀 등급 이상의 보상
- **보장이 없을 때 희귀 등급 이상의 보상이 나올 확률**: 25.000%
- **보장이 있을 때, 많은 횟수를 개봉한 경우**: 27.781%
- **보장이 강제하는 개봉**: 3.708%
- **그런 보상 사이의 평균 개봉 횟수**: 3.600

<!-- containers-survey-canister-guarantee:end -->

## 시약 랙 (Reagent Rack) {#reagent-rack}

*Skylab의 연구 센터는 시약 앰풀에서 비행에 쓰는 부스터를 증류하며, 랙은 한 배치가 중단되었을 때 남는 것입니다. 각 시약을 정량으로 담은 앰풀이 하나씩 봉인되어 있습니다. 용량은 함선이 비행하는 동안에만 낡기 때문에, 랙은 원하는 만큼 선반에 보관할 수 있습니다.*

### 등급별 확률 {#reagent-rack-grades}

<!-- containers-reagent-rack-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 등급 | 확률 | 포함된 보상 |
| :--- | ---: | ---: |
| 일반 | 45.000% | 5 |
| 고급 | 33.000% | 8 |
| 희귀 | 15.000% | 8 |
| 영웅 | 5.500% | 6 |
| 신화 | 1.300% | 2 |
| 전설 | 0.200% | 2 |

<!-- containers-reagent-rack-grades:end -->

### 모든 보상 {#reagent-rack-prizes}

<!-- containers-reagent-rack-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 등급 | 보상 | 확률 |
| :--- | :--- | ---: |
| 일반 | 1시간 Experience Booster | 11.000% |
| 일반 | 1시간 Honor Booster | 11.000% |
| 일반 | 1시간 Shield Regen Booster | 9.000% |
| 일반 | Energetic Wall I | 8.000% |
| 일반 | 500 × Advanced Plasma | 6.000% |
| 고급 | 1시간 Laser Damage Booster I | 5.000% |
| 고급 | 1시간 Shield Wall Booster I | 5.000% |
| 고급 | 1시간 Hull Plating Booster I | 5.000% |
| 고급 | 1시간 Resource Magnet Booster | 3.500% |
| 고급 | 2시간 Experience Booster | 4.500% |
| 고급 | 2시간 Honor Booster | 3.500% |
| 고급 | EMP Charge | 3.500% |
| 고급 | 3 × Energetic Wall I | 3.000% |
| 희귀 | 2시간 Laser Damage Booster I | 2.500% |
| 희귀 | 2시간 Shield Wall Booster I | 2.000% |
| 희귀 | 2시간 Hull Plating Booster I | 2.000% |
| 희귀 | 4시간 Experience Booster | 2.000% |
| 희귀 | 4시간 Honor Booster | 2.000% |
| 희귀 | 2시간 Loot Luck Booster | 1.500% |
| 희귀 | 3 × EMP Charge | 2.000% |
| 희귀 | 2시간 Resource Magnet Booster | 1.000% |
| 영웅 | 4시간 Laser Damage Booster I | 1.200% |
| 영웅 | 4시간 Shield Wall Booster I | 1.000% |
| 영웅 | 4시간 Hull Plating Booster I | 1.000% |
| 영웅 | 4시간 Resource Magnet Booster | 0.700% |
| 영웅 | 4시간 Loot Luck Booster | 0.900% |
| 영웅 | 8 × EMP Charge | 0.700% |
| 신화 | **전투 랙**: 4시간 Laser Damage Booster I + 4시간 Shield Wall Booster I + 4시간 Hull Plating Booster I | 0.700% |
| 신화 | **학자의 랙**: 4시간 Experience Booster + 4시간 Honor Booster + 4시간 Resource Magnet Booster + 4시간 Loot Luck Booster | 0.600% |
| 전설 | **풀 스펙트럼**: 4시간 Laser Damage Booster I + 4시간 Shield Wall Booster I + 4시간 Hull Plating Booster I + 4시간 Shield Regen Booster + 4시간 Experience Booster + 4시간 Honor Booster + 4시간 Resource Magnet Booster + 4시간 Loot Luck Booster | 0.100% |
| 전설 | Cloaking CPU L | 0.100% |

<!-- containers-reagent-rack-prizes:end -->

부스터 시간은 이미 작동 중인 같은 부스터에 더해지며, 비행하는 동안에만 줄어듭니다. [부스터](/wiki/06-Items/Boosters.md)를 보세요.

### 보장 {#reagent-rack-guarantee}

<!-- containers-reagent-rack-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **보장**: 개봉 10회마다 최소 한 번은 희귀 등급 이상의 보상
- **보장이 없을 때 희귀 등급 이상의 보상이 나올 확률**: 22.000%
- **보장이 있을 때, 많은 횟수를 개봉한 경우**: 24.001%
- **보장이 강제하는 개봉**: 2.565%
- **그런 보상 사이의 평균 개봉 횟수**: 4.167

<!-- containers-reagent-rack-guarantee:end -->

## 보상이 정해지는 방식 {#how-a-prize-is-chosen}

컨테이너를 개봉하면 서버가 세 단계로 정합니다.

1. **등급.** 난수 하나를 등급별 확률과 맞춰 봅니다.
2. **보상.** 두 번째 난수를 그 등급의 보상별 확률과 맞춰 봅니다. 이미 보유한 함선은 여기에 들어가지 않습니다([함선](#the-ships) 참고).
3. **같은 확률 중의 선택.** *여럿 중 하나*라고 적힌 보상은 그중 하나를 주며, 각각의 확률은 같습니다.

숫자는 서버 운영체제의 난수 생성기에서 나오며, 컨테이너를 가져간 뒤에 추첨됩니다. 보내는 어떤 것도 숫자를 바꿀 수 없습니다. 버튼도, 시각도 마찬가지입니다.

이전의 두 가지는 영향을 줍니다. 보장 카운터는 한 번의 개봉에서 다음으로 이어지며, 이는 위의 각 컨테이너의 보장에 설명되어 있습니다. 그리고 이미 보유한 것(이전 개봉에서 얻은 것 포함)은 추첨에 남는 보상을 바꿉니다. 보유한 함선은 추첨에 들어가지 않고, 보유한 외형은 그 등급에 아직 없는 외형이 남아 있는 동안 추첨되지 않습니다([중복과 분해](#duplicates-and-salvage)와 [함선](#the-ships) 참조). 보유한 것은 등급의 확률을 바꾸지 않습니다.

<!-- containers-draw:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- 모든 확률은 100,000 중 정수 개의 몫입니다. 1몫 = 0.001%

<!-- containers-draw:end -->

**모든 개봉은 기록됩니다.** 서버가 사용한 시드(난수), 추첨된 숫자, 추첨에 쓴 표의 해시, 보유한 것 때문에 추첨에서 빠진 보상이 함께 기록됩니다. 컨테이너 페이지의 **기록**에 있는 **상세**에서 읽을 수 있습니다.

**직접 확인해 볼 수도 있습니다.** 게임 소스에 있는 도구 `scripts/containers-verify.py`는 표와 개봉의 상세를 읽고, 등급·보상·선택이 시드에서 나오는지 알려 줍니다. 방법은 짧습니다.

```text
stream(seed, id): value i, for i = 0, 1, 2, ...
  = the first 8 bytes (big endian) of HMAC-SHA256(
      key     = seed,
      message = "sc-container-v1|" + id + "|" + i )
  where i is written as 4 bytes, big endian
below(n): take values until one is under 2^64 - (2^64 mod n),
  then use it modulo n (no modulo bias)
grade:    roll = below(total of the grades in play);
  the grade is the first whose running sum is above the roll
prize:    sub = below(total of the prizes left in that grade);
  the prize is the first whose running sum is above sub
choice:   a prize that is "one of N" gives the alternative
  number below(N)
seed = the 32 bytes shown under Details; id = the container's id.
When the guarantee forces an opening, only the guaranteed grade
and better are in play.
```

## 중복과 분해 {#duplicates-and-salvage}

- 보유한 **외형**은 그 등급에 아직 없는 외형이 남아 있는 동안에는 추첨되지 않습니다. 컬렉션은 그 스킨을 모두 가지고 있을 때 보유한 것으로 칩니다.
- 그 등급의 외형을 모두 가지고 있으면 대신 **분해**가 지급됩니다. 등급별 Thulium입니다. 보장에서는 그 등급의 보상으로 셉니다.
- **아이템**은 Thulium으로 바뀌지 않습니다. 쌓이거나 그대로 도착합니다.
- **함선**은 두 번 주어지지도, 분해로 지급되지도 않습니다([함선](#the-ships) 참고).

<!-- containers-salvage:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 등급 | Thulium |
| :--- | ---: |
| 일반 | 25 |
| 고급 | 100 |
| 희귀 | 400 |
| 영웅 | 1,200 |
| 신화 | 4,000 |

<!-- containers-salvage:end -->

## 함선 {#the-ships}

주조소 도가니에는 함선이 들어 있을 수 있습니다. 표에는 함선이 **기본 확률**과 함께 나열되어 있으며, 이는 함선을 하나도 보유하지 않은 파일럿의 확률입니다. 이것이 공개된 확률입니다.

이미 보유한 함선은 절대 나오지 않습니다. 추첨에서 빠지고, 그 몫은 같은 등급의 다른 보상에 각자의 확률에 비례해 돌아갑니다. 따라서 보유한 것이 내 확률을 바꾸며, 그 등급의 다른 보상 확률이 조금 높아집니다. 등급의 확률은 바뀌지 않고, 보장도 바뀌지 않습니다. 함선으로 만든 디자인은 그 함선을 보유한 것으로 칩니다. Paragon THUNDER는 Paragon을 보유한 것으로 칩니다.

<!-- containers-ships:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| 함선 | 등급 | 확률 |
| :--- | :--- | ---: |
| Nomad | 고급 | 0.100% |
| Paragon | 희귀 | 0.100% |
| Storm | 영웅 | 0.050% |
| Ironclad | 영웅 | 0.050% |
| Wraith | 신화 | 0.020% |
| **5척 모두** | | **0.320%** |

예: 함선 Nomad 한 척을 보유했다면, 고급 등급의 확률은 그대로이지만 그 등급의 30,000몫 중 그 함선(Nomad)의 100몫이 추첨에서 빠집니다. 그래서 고급 등급의 다른 보상은 각각 30,000 / 29,900 = 1.0033배, 표보다 더 잘 나옵니다.

다음 표는 그 등급의 함선을 모두 보유한 경우입니다. 일부만 보유했다면 그 함선의 몫만 추첨에서 빠지므로 배수는 더 작아집니다.

| 등급 | 등급의 몫 | 모든 함선의 몫 | 그 등급의 다른 보상이 더 잘 나오는 배수 |
| :--- | ---: | ---: | ---: |
| 고급 | 30,000 | 100 | ×1.0033 |
| 희귀 | 16,000 | 100 | ×1.0063 |
| 영웅 | 6,500 | 100 | ×1.0156 |
| 신화 | 2,200 | 20 | ×1.0092 |

예: 영웅 등급에는 함선이 2척 있습니다. 함선 Storm 한 척만 보유했다면 6,500몫 중 그 함선의 50몫만 추첨에서 빠집니다. 그래서 영웅 등급의 다른 보상은 각각 6,500 / 6,450 = 1.0078배가 되며, 1.0156배가 아닙니다.

<!-- containers-ships:end -->

게임의 컨테이너 페이지는 공개 확률과 다를 때 내 확률을 나란히 보여 줍니다. 보유한 함선은 회색으로 목록에 남으며 “이 함선은 이미 보유하고 있어 컨테이너에서 나오지 않습니다.”라는 줄이 붙습니다.

## 초기화 {#the-wipe}

- **개봉하지 않은 컨테이너는 남습니다.** 초기화 후에도 계정에 남습니다.
- **컨테이너에서 나온 아이템은 일반 아이템입니다.** 초기화 때 수송 보관함에 넣어 가져가지 않으면 사라집니다([초기화 일정](/wiki/03-Mechanics/Wipe-Timeline.md)).
- **외형과 함선은 그대로 남습니다.** 다른 외형, 다른 함선과 같습니다. 크레딧, Thulium, 부스터의 남은 시간은 초기화 때 각자의 규칙을 따릅니다.
- **컨테이너에서 나온 것은 경매장에 올릴 수 없습니다.**

<!-- containers-wipe:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **시즌 30일째부터 닫힘**: 표본 금고, 주조소 도가니, 탐사 캐니스터, 시약 랙. 안에 든 것이 초기화 때 사라지므로, 초기화가 끝날 때까지 열 수 없습니다.
- **배너**: 컨테이너 페이지가 시즌 28일째부터 알려 줍니다.
- **계속 열려 있음**: 크로마 기록보관소. 외형만 들어 있고, 외형은 초기화 후에도 남습니다.

<!-- containers-wipe:end -->

## 표의 버전 {#version-of-the-table}

이 페이지의 모든 확률은 게임 서버의 표입니다. 확률이 바뀌면 표는 새 버전과 새 해시를 받고, 모든 개봉은 추첨에 쓴 표의 해시를 기록합니다.

<!-- containers-version:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **표 버전**: 1
- **표 해시 (앞 12자)**: `23aa20f1a5ad`

바뀐 내용:

- 버전 1: 처음 공개된 표.

<!-- containers-version:end -->
