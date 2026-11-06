<!-- wiki-i18n source: c21ae6d189180cd7 -->
<!-- wiki-i18n title: Phantasm 무리 -->
# Phantasm 무리 {#phantasm-swarm}

Phantasm 무리는 **Boss Phantasm**과 그 **Phantasm Guard**로 이루어집니다. 먼저 싸움을 걸지 않는 거대한 [Phantasm](/wiki/04-Aliens/Phantasm.md)과, 그 곁에 머물며 회복시키는 더 작은 개체들입니다. 기업의 바깥쪽 섹터인 `x-3`과 `x-4`에 있으며, 중간 레벨 파일럿 그룹을 위한 전투입니다.

## 한눈에 보기 {#at-a-glance}

<!-- phantasm-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **위치**: 모든 기업의 `x-3`와 `x-4` 섹터
- **개수**: 해당 섹터마다 하나씩, 월드마다 6개
- **출현**: 시즌 4일차부터 초기화까지(베타와 감마: 시즌 1일차부터)
- **리더**: Boss Phantasm
- **부하**: 최대 4 × Phantasm Guard, 10초마다 새로 하나
- **부하가 머무는 범위**: 리더로부터 500유닛 이내
- **회복**: 리더로부터 600유닛 이내에 있는 Phantasm Guard는 한 마리마다 리더의 선체를 회복시킵니다(Alpha에서 초당 30 HP)
- **리더 격파 후**: 리더가 격파되고 30초 뒤에 부하는 사라집니다. 단, 공격 중이면 남습니다
- **복귀**: 리더가 격파되고 2분 뒤, 같은 섹터에서
- **알림**: 해당 섹터의 파일럿에게 리더가 나타날 때와 격파될 때 알려 줍니다. 이 줄들은 시스템 줄입니다. 채팅의 **시스템** 탭에 읽지 않은 줄 수와 함께 표시되고, **전체** 탭이나 **지역** 탭에는 나오지 않습니다. 킬 피드에 처치 공로를 인정받은 파일럿의 이름이 나옵니다.

<!-- phantasm-glance:end -->

## 구성원 {#the-members}

- **Boss Phantasm**: 무리의 색조를 띠고 머리 위에 이름이 표시되는 더 큰 Phantasm입니다. 자체 선체와 실드, 레이저 일제 사격을 갖습니다(수치는 아래에 있습니다). 비공격적이어서 파일럿에게 공격받을 때까지 돌아다니다가, 공격받으면 그 파일럿을 쫓아가 사격하고, 가까이 있는 무리의 함선들이 전투에 합류합니다. 무기 사거리와 속도는 Phantasm 그대로이며, 스스로 선체를 수리하지 않습니다.
- **Phantasm Guard**: 무리의 색조를 띤 더 작은 Phantasm입니다. Guard는 보스 곁에 머물고, 가까운 무리의 함선이 공격받으면 전투에 합류하며, 보스 가까이에 있는 Guard는 한 마리마다 보스의 선체를 회복시킵니다. Guard는 Phantasm처럼 한동안 쉬면 자기 선체를 수리합니다.

## 전투의 흐름 {#how-the-fight-goes}

- **그룹을 데려가세요.** x2 탄약을 쓰는 레벨 4–5 파일럿 세 명이면 Alpha에서 약 1분 30초 만에 쓰러뜨리며, 잃는 함선은 많아야 한 척입니다. 이 레벨의 파일럿 혼자서는 격파당하고, 두 명이어도 마찬가지입니다. 더 좋은 함선과 x4 탄약이면 훨씬 빨라집니다.
- **Guard가 아니라 보스를 쏘세요.** Guard는 몇 초 만에 쓰러지지만 *한눈에 보기* 목록에 나온 간격으로 새로 나타나고, Guard가 회복시키는 양은 그룹이 입히는 피해의 일부에 불과합니다. 내버려 두면 시간이 조금 들고, 쫓아다니면 더 듭니다.
- **Beta와 Gamma는 더 어렵습니다.** 그 월드의 무리는 더 강하므로([월드](/wiki/05-Swarms/Swarms.md#the-worlds)) 더 많은 파일럿이나 더 좋은 탄약이 필요합니다.
- **섹터를 주시하세요.** `x-4`는 Alpha에서 PvP 섹터이고, Beta와 Gamma에서는 `x-3`과 `x-4`가 그렇습니다([월드](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)). 라이벌이 전투에 끼어들거나 상자를 기다릴 수 있습니다. 그룹의 함선 한 척은 경계를 서게 하세요.
- **보스는 돌아옵니다.** *한눈에 보기* 목록의 시간이 지나면 같은 섹터에 온전한 상태로 나타나며, Guard는 하나씩 차례로 나타납니다.

## 보상과 전리품 {#rewards-and-drops}

Boss Phantasm의 보상은 그 전투의 무게에 걸맞습니다. 1분 싸우면 이 섹터들에서 가장 보상이 큰 외계인인 Goombah와 1분 싸울 때보다 많이 받습니다. 보상은 싸운 파일럿들 사이에서 피해량에 따라 나뉩니다([보스 처치 보상](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). 상자에는 Phantasm의 전리품이 여러 배로(Ship Fragment, Daraxium, Nyxite) 탄약과 로켓과 함께 들어 있으며, 가장 많은 피해를 입힌 파일럿에게 돌아갑니다. Guard의 보상은 소액이고 아무것도 떨어뜨리지 않습니다. 보스와 함께 돌아오기 때문에 잡아도 파밍이 되지 않습니다.

## 수치 {#the-numbers}

무리 함선의 세 월드에서의 수치입니다([월드](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- phantasm-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Phantasm

바탕은 Phantasm이며, 선체는 그 2,000%, 레이저 피해량은 그 300%입니다. 속도와 사거리는 바탕이 된 함선의 것입니다.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 선체 | 40,000 | 60,000 | 80,000 |
| 실드 | 64,000 | 96,000 | 128,000 |
| 레이저 피해량(초당 일제 사격 1회) | 1,050 | 1,575 | 2,100 |
| 속도 | 160 | 160 | 160 |
| 레이저 사거리 | 700 | 700 | 700 |
| 어그로 반경 | 공격받을 때만 | 공격받을 때만 | 공격받을 때만 |
| 크레딧 | 39,000 | 78,000 | 117,000 |
| Thulium | 195 | 390 | 585 |
| 경험치(XP) | 7,800 | 15,600 | 23,400 |
| 명예 | 62 | 124 | 186 |
| 처치당 PvE 포인트 | 8 | 8 | 8 |

**전리품**: 가장 많은 피해를 입힌 파일럿을 위한 상자 하나.

| 아이템 | 확률 | 수량 |
| :--- | ---: | ---: |
| Ship Fragment | 13번의 굴림마다 각각 100% | 1 |
| Daraxium | 13번의 굴림마다 각각 60% | 1–2 |
| Nyxite | 13번의 굴림마다 각각 60% | 1–2 |
| Standard Battery | 100% | 600–1,200 |
| Advanced Plasma | 100% | 60–100 |
| Ultra Core | 100% | 10–20 |
| 크레딧으로 살 수 있는 8종의 [로켓](/wiki/06-Items/Rockets.md) 중 무작위 하나 | 100% | 4–6 |

### Phantasm Guard

바탕은 Phantasm이며, 선체와 실드, 피해량은 그 50%입니다. 속도와 사거리는 바탕이 된 함선의 것입니다.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 선체 | 1,000 | 1,500 | 2,000 |
| 실드 | 1,600 | 2,400 | 3,200 |
| 레이저 피해량(초당 일제 사격 1회) | 175 | 263 | 350 |
| 속도 | 160 | 160 | 160 |
| 레이저 사거리 | 700 | 700 | 700 |
| 어그로 반경 | 공격받을 때만 | 공격받을 때만 | 공격받을 때만 |
| 리더 회복(한 마리마다 초당, 선체만) | 30 | 45 | 60 |
| 크레딧 | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| 경험치(XP) | 12 | 24 | 36 |
| 명예 | 1 | 2 | 3 |
| 처치당 PvE 포인트 | 1 | 1 | 1 |

**전리품**: 없음. 처치로 지급되는 것은 크레딧, Thulium, 경험치, 명예뿐입니다.

<!-- phantasm-members:end -->
