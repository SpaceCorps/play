<!-- wiki-i18n source: 7859e3f6a7efac1e -->
<!-- wiki-i18n title: Goombah 무리 -->
# Goombah 무리 {#goombah-swarm}

Goombah 무리는 **Boss Goombah**와 그 **Goombah Guard**로 이루어집니다. 먼저 싸움을 걸지 않는 거대한 [Goombah](/wiki/04-Aliens/Goombah.md)와, 그 곁에 머물며 회복시키는 더 작은 개체들입니다. [Phantasm 무리](/wiki/05-Swarms/Phantasm-Swarm.md)와 같은 섹터인 `x-3`과 `x-4`에 있으며, 기업 섹터의 최강 파일럿 그룹을 위한 전투입니다.

## 한눈에 보기 {#at-a-glance}

<!-- goombah-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **위치**: 모든 기업의 `x-3`와 `x-4` 섹터
- **개수**: 해당 섹터마다 하나씩, 월드마다 6개
- **출현**: 시즌 4일차부터 초기화까지
- **리더**: Boss Goombah
- **부하**: 최대 4 × Goombah Guard, 10초마다 새로 하나
- **부하가 머무는 범위**: 리더로부터 500유닛 이내
- **회복**: 리더로부터 600유닛 이내에 있는 Goombah Guard는 한 마리마다 리더의 선체를 회복시킵니다(Alpha에서 초당 110 HP)
- **리더 격파 후**: 리더가 격파되고 30초 뒤에 부하는 사라집니다. 단, 공격 중이면 남습니다
- **복귀**: 리더가 격파되고 5분 뒤, 같은 섹터에서
- **알림**: 해당 섹터의 파일럿에게 리더가 나타날 때와 격파될 때 알려 줍니다. 이 줄들은 시스템 줄입니다. 채팅의 **시스템** 탭에 읽지 않은 줄 수와 함께 표시되고, **전체** 탭이나 **지역** 탭에는 나오지 않습니다. 킬 피드에 처치 공로를 인정받은 파일럿의 이름이 나옵니다.

<!-- goombah-glance:end -->

## 구성원 {#the-members}

- **Boss Goombah**: 무리의 색조를 띠고 머리 위에 이름이 표시되는 더 큰 Goombah입니다. 자체 선체와 실드, 레이저 일제 사격을 갖습니다(수치는 아래에 있습니다). 비공격적이어서 파일럿에게 공격받을 때까지 돌아다니다가, 공격받으면 그 파일럿을 쫓아가 사격하고, 가까이 있는 무리의 함선들이 전투에 합류합니다. 무기 사거리와 속도는 Goombah 그대로이며, 스스로 선체를 수리하지 않습니다.
- **Goombah Guard**: 무리의 색조를 띤 더 작은 Goombah입니다. Guard는 보스 곁에 머물고, 가까운 무리의 함선이 공격받으면 전투에 합류하며, 보스 가까이에 있는 Guard는 한 마리마다 보스의 선체를 회복시킵니다. Guard는 Goombah처럼 한동안 쉬면 자기 선체를 수리합니다.

## 전투의 흐름 {#how-the-fight-goes}

- **최강 함선들의 그룹을 데려가세요.** x2 탄약을 쓰는 레벨 8 파일럿 세 명이면 Alpha에서 약 75초 만에 쓰러뜨리며, 잃는 함선은 많아야 한 척입니다. 그중 두 명은 x4 탄약이 필요하고, 더 낮은 레벨의 파일럿은 이길 만큼의 피해를 주지 못합니다.
- **Guard가 아니라 보스를 쏘세요.** Guard는 몇 초 만에 쓰러지지만 *한눈에 보기* 목록에 나온 간격으로 새로 나타나고, Guard가 회복시키는 양은 그룹이 입히는 피해의 일부에 불과합니다. 내버려 두면 시간이 조금 들고, 쫓아다니면 더 듭니다.
- **Beta와 Gamma는 더 어렵습니다.** 그 월드의 무리는 더 강하므로([월드](/wiki/05-Swarms/Swarms.md#the-worlds)) 더 많은 파일럿이나 더 좋은 탄약이 필요합니다.
- **섹터를 주시하세요.** `x-4`는 Alpha에서 PvP 섹터이고, Beta와 Gamma에서는 `x-3`과 `x-4`가 그렇습니다([월드](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)). 라이벌이 전투에 끼어들거나 상자를 기다릴 수 있습니다. 그룹의 함선 한 척은 경계를 서게 하세요.
- **보스는 돌아옵니다.** *한눈에 보기* 목록의 시간이 지나면 같은 섹터에 온전한 상태로 나타나며, Guard는 하나씩 차례로 나타납니다.

## 보상과 전리품 {#rewards-and-drops}

Boss Goombah의 보상은 그 전투의 무게에 걸맞습니다. 1분 싸우면 이 섹터들에서 가장 보상이 큰 외계인인 Goombah와 1분 싸울 때보다 많이 받습니다. 보상은 싸운 파일럿들 사이에서 피해량에 따라 나뉩니다([보스 처치 보상](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). 상자에는 Goombah의 전리품이 몇 배로(Cataclysite, Quorvium, Power Core, Reinforced Hull Plate, Ship Fragment) 탄약과 로켓과 함께 들어 있으며, 가장 많은 피해를 입힌 파일럿에게 돌아갑니다. Guard의 보상은 소액이고 아무것도 떨어뜨리지 않습니다. 보스와 함께 돌아오기 때문에 잡아도 파밍이 되지 않습니다.

## 수치 {#the-numbers}

무리 함선의 세 월드에서의 수치입니다([월드](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- goombah-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Goombah

바탕은 Goombah이며, 선체는 그 400%, 레이저 피해량은 그 100%입니다. 속도와 사거리는 바탕이 된 함선의 것입니다.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 선체 | 128,000 | 192,000 | 256,000 |
| 실드 | 192,000 | 288,000 | 384,000 |
| 레이저 피해량(초당 일제 사격 1회) | 3,000 | 4,500 | 6,000 |
| 속도 | 180 | 180 | 180 |
| 레이저 사거리 | 800 | 800 | 800 |
| 어그로 반경 | 공격받을 때만 | 공격받을 때만 | 공격받을 때만 |
| 크레딧 | 120,000 | 240,000 | 360,000 |
| Thulium | 600 | 1,200 | 1,800 |
| 경험치(XP) | 24,000 | 48,000 | 72,000 |
| 명예 | 192 | 384 | 576 |
| 처치당 PvE 포인트 | 14 | 14 | 14 |

**전리품**: 가장 많은 피해를 입힌 파일럿을 위한 상자 하나.

| 아이템 | 확률 | 수량 |
| :--- | ---: | ---: |
| Ship Fragment | 8번의 굴림마다 각각 100% | 3 |
| Reinforced Hull Plate | 8번의 굴림마다 각각 60% | 1 |
| Power Core | 8번의 굴림마다 각각 25% | 1 |
| Cataclysite | 8번의 굴림마다 각각 100% | 4 |
| Quorvium | 8번의 굴림마다 각각 100% | 2–4 |
| Advanced Plasma | 100% | 100–200 |
| Ultra Core | 100% | 100–200 |
| 크레딧으로 살 수 있는 8종의 [로켓](/wiki/06-Items/Rockets.md) 중 무작위 하나 | 100% | 6–10 |

### Goombah Guard

바탕은 Goombah이며, 선체와 실드, 피해량은 그 20%입니다. 속도와 사거리는 바탕이 된 함선의 것입니다.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 선체 | 6,400 | 9,600 | 12,800 |
| 실드 | 9,600 | 14,400 | 19,200 |
| 레이저 피해량(초당 일제 사격 1회) | 600 | 900 | 1,200 |
| 속도 | 180 | 180 | 180 |
| 레이저 사거리 | 800 | 800 | 800 |
| 어그로 반경 | 공격받을 때만 | 공격받을 때만 | 공격받을 때만 |
| 리더 회복(한 마리마다 초당, 선체만) | 110 | 165 | 220 |
| 크레딧 | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| 경험치(XP) | 12 | 24 | 36 |
| 명예 | 1 | 2 | 3 |
| 처치당 PvE 포인트 | 3 | 3 | 3 |

**전리품**: 없음. 처치로 지급되는 것은 크레딧, Thulium, 경험치, 명예뿐입니다.

<!-- goombah-members:end -->
