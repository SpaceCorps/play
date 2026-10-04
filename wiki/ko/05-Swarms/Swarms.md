<!-- wiki-i18n source: bbd76eb145ce6188 -->
<!-- wiki-i18n title: 무리 -->
# 무리 {#swarms}

**무리**는 **리더** 아래에서 은하의 한 구역을 돌아다니는 외계인 집단입니다. 리더는 주변의 어떤 외계인보다 훨씬 강한 보스이고, **부하**들이 리더를 지키며 두 무리에서는 리더를 회복시키기도 합니다. 무리는 세 가지이며, 각각 고유한 문서가 있습니다.

- [Seeker 무리](/wiki/05-Swarms/Seeker-Swarm.md): Boss Seeker와 그 Seeker Slave. 가장 작은 무리로, 신규 파일럿이 비행하는 섹터에 있습니다.
- [Pirate 무리](/wiki/05-Swarms/Pirate-Swarm.md): Pirate Boss와 그 Pirate Scout. 그룹을 위한 긴 전투입니다.
- [Dormant 무리](/wiki/05-Swarms/Dormant-Swarm.md): Dormant Force와 그 Dormant Pulse. 가장 강한 무리이며 전리품이 가장 풍부합니다.

무리의 함선은 **각각 독립된 종류의 외계인**입니다. 고유한 이름과 고유한 처치 횟수를 가지며, Seeker나 Phantasm 같은 다른 외계인으로는 집계되지 않습니다. 무리의 함선은 바탕이 된 함선의 모양을 하고 있고, 고유한 색조를 띠며 머리 위에 이름이 표시됩니다. Boss Seeker는 훨씬 큰 Seeker입니다.

## 세 무리 {#the-three-swarms}

<!-- swarms-list:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| 무리 | 위치 | 개수 | 리더 | 부하 | 복귀 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**Pirate 무리**](/wiki/05-Swarms/Pirate-Swarm.md) | 모든 기업의 `x-2`와 `x-3` 섹터 | 해당 섹터마다 하나씩, 월드마다 6개 | **Pirate Boss** | 최대 5 × Pirate Scout, 10초마다 새로 하나 | 리더가 격파되고 2분 뒤, 같은 섹터에서 |
| [**Dormant 무리**](/wiki/05-Swarms/Dormant-Swarm.md) | 위험 섹터 `DS-1`, `DS-2`, `DS-3`, `DS-4`. 서로 사이를 비행합니다 | 월드마다 하나 | **Dormant Force** | 2 × Dormant Pulse, 리더와 함께 비행 | 무리 전체가 격파되고 1시간 뒤, 무작위 위험 섹터에서 |
| [**Seeker 무리**](/wiki/05-Swarms/Seeker-Swarm.md) | 모든 기업의 `x-1`와 `x-2` 섹터 | 해당 섹터마다 하나씩, 월드마다 6개 | **Boss Seeker** | 최대 4 × Seeker Slave, 10초마다 새로 하나 | 리더가 격파되고 2분 뒤, 같은 섹터에서 |

<!-- swarms-list:end -->

## 언제, 어디에 {#when-and-where}

무리는 **첫 접촉**부터 나타나기 시작해 초기화까지 남아 있습니다([초기화 일정](/wiki/03-Mechanics/Wipe-Timeline.md) 참조. 날짜는 아래 규칙의 첫 줄에 있습니다). **월드마다 자기만의 무리가 있으며** 위치는 같습니다. 그래서 Alpha의 Pirate Boss와 Beta의 Pirate Boss는 서로 다른 함선이고, 내 월드에서 처치한 무리가 다른 월드에서 처치되는 것은 아닙니다. 처치된 무리는 위 표의 시간이 지나면 돌아옵니다.

## 모든 무리의 규칙 {#the-rules-of-every-swarm}

<!-- swarms-rules:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- 무리는 시즌 4일차부터 초기화까지 나타납니다.
- 무리의 함선이 공격받으면, 그 함선에서 1,500유닛 이내에 있는 같은 무리의 함선들이 처음 공격한 파일럿을 상대로 전투에 합류합니다.
- 리더는 모든 스테이션과 게이트 고리의 가장자리에서 최소 2,500유닛 떨어진 곳에 나타납니다.
- 보스에게 입힌 피해의 5% 이상을 입힌 파일럿이 그 처치의 보상을 받습니다.

<!-- swarms-rules:end -->

## 월드 {#the-worlds}

월드는 다른 모든 외계인과 마찬가지로 무리를 강화합니다([월드](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)). 무리 함선의 선체, 실드, 실드 재충전, 레이저 피해량, 로켓 피해량, 회복량은 Alpha의 수치에 아래의 강도를 곱한 값이고, 처치 보상에는 아래의 보상 배율이 곱해집니다. 속도, 사거리, 전리품은 모든 월드에서 같습니다. 각 문서에 세 월드에서의 함선별 수치가 나와 있습니다.

<!-- swarms-world:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| 월드 | 강도 | 보상 배율 |
| :--- | ---: | ---: |
| **Alpha** | ×1 | ×1 |
| **Beta** | ×1.5 | ×2 |
| **Gamma** | ×2 | ×3 |

<!-- swarms-world:end -->

## 파일럿에게 알려지는 내용 {#what-the-pilots-are-told}

Seeker 무리와 Pirate 무리는 보스가 나타날 때와 처치될 때 해당 섹터의 파일럿에게 알립니다. Dormant 무리는 월드 전체에 알리며, 위험 섹터 맵과 은하 지도에 표시되어 파일럿이 찾을 수 있습니다. 이 줄들은 시스템 줄입니다. 채팅의 **시스템** 탭에 읽지 않은 줄 수와 함께 표시되고, **전체** 탭이나 **지역** 탭에는 나오지 않습니다. 보스 처치는 킬 피드에도 한 줄이 올라오며, 처치 공로를 인정받은 파일럿의 이름이 나옵니다. 누구에게 알려지는지는 각 문서의 *한눈에 보기* 목록에 적혀 있습니다.

## 무리와 싸우기 {#fighting-a-swarm}

- **리더는 절대 먼저 싸움을 걸지 않습니다.** 리더는 파일럿에게 공격받을 때까지 돌아다니다가 공격받으면 반격하며, 가까이 있는 무리의 함선들이 처음 공격한 파일럿을 상대로 전투에 합류합니다(거리는 위 규칙에 있습니다). 예외는 Pirate Scout로, 가까이 오는 모든 파일럿을 공격합니다. 리더는 스스로 선체를 수리하지 않으므로, 입힌 피해는 부하가 회복시키지 않는 한 그대로 남습니다. 실드는 다른 외계인과 똑같이 재충전됩니다.
- **무리의 함선은 파일럿하고만 싸웁니다.** 외계인에게 사격하지 않고 외계인도 이들에게 사격하지 않으며, [기업 파일럿](/wiki/03-Mechanics/Company-Pilots.md)은 이들을 무시합니다. 무리의 함선을 사냥하지도, 맞서 싸우는 당신을 도우러 오지도 않습니다.
- **로켓.** Pirate Boss와 Dormant Force, Pulse는 자신을 공격한 파일럿에게 **직선** 로켓, 즉 [Rivet 로켓](/wiki/06-Items/Rockets.md)을 발사합니다. 계속 움직이는 함선은 피하지만 멈춰 있는 함선은 맞습니다.
- **전투의 규모.** Seeker 무리는 2명, Pirate 무리는 소규모 그룹, Dormant 무리는 최강 함선들의 대규모 그룹을 위한 상대입니다. 높은 월드일수록 다른 외계인과 마찬가지로 더 많은 파일럿이 필요합니다.

## 준비물 {#what-to-bring}

- **그룹.** [그룹](/wiki/03-Mechanics/Groups.md)으로 비행하세요. 무리는 그룹을 기준으로 균형이 맞춰져 있어, 낮은 레벨의 파일럿 혼자서는 금방 격파되고 Pirate Boss를 혼자 쓰러뜨릴 수 있는 것은 최강급 함선뿐입니다. Dormant 무리는 혼자서는 누구도 쓰러뜨릴 수 없습니다. 무리는 처음 공격한 파일럿과 싸우므로([외계인이 싸우는 상대](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)), 그룹에서 가장 튼튼한 함선이 먼저 공격하게 하세요.
- **더 좋은 탄약.** x2 이상의 탄약을 가져가세요([레이저와 탄약](/wiki/06-Items/Lasers.md) 참조). 무리 부하들의 회복량은 소규모 그룹이 x1 탄약으로 입히는 피해보다 클 수 있습니다.
- **실드와 수리**: 긴 전투에 대비하세요. 함선의 능력([능력](/wiki/03-Mechanics/Abilities.md))은 몇 분이 걸리는 Pirate 전투에서 가장 중요합니다.
- **움직일 공간.** 사거리에서 앞서는 무기의 사거리 밖에 머물고, 로켓에는 계속 움직이며 대응하세요.

## 보스 처치 보상 {#how-a-boss-kill-pays}

일반 외계인은 처음 명중시킨 파일럿에게 보상을 지급합니다([전투](/wiki/03-Mechanics/Combat.md#kill-rewards-first-hit-claims)). 무리의 리더와 각 Dormant Pulse는 대신 **입힌 피해량에 따라** 보상을 지급합니다.

- **보상은 피해량에 따라 나뉩니다.** 위 규칙에 나온 비율 이상의 피해를 입힌 파일럿이 입힌 피해에 비례해 보상을 받습니다. 처치의 크레딧, Thulium, 경험치, 명예는 이들 사이에서 나뉩니다. 그 비율에 못 미친 파일럿은 아무것도 받지 못합니다.
- **화물 상자는 가장 많은 피해를 입힌 파일럿에게 돌아갑니다.** 다른 외계인과 마찬가지로 30초 동안은 그 파일럿(과 소속 클랜)의 것이고, 그 뒤에는 누구나 가져갈 수 있습니다([화물](/wiki/03-Mechanics/Cargo.md)). Dormant의 각 함선은 자체 피해 집계와 자체 상자를 가집니다.
- **부하는 평소처럼 지급합니다.** Pirate Scout와 Seeker Slave는 처음 명중시킨 파일럿에게 지급하며, 보상은 보스에 비해 소액입니다.
- **보스의 보상은 주변 외계인보다 크게 설계되어 있습니다.** Pirate Boss와 1분 싸우면 Goombah와 1분 싸우는 것보다 보상이 많고, Dormant 무리는 그보다도 많습니다. Boss Seeker의 보상은 정확히 Seeker 10마리분입니다.

모든 처치는 그 함선 고유의 이름으로 처치 통계에 집계되며, 랭킹에 PvE 포인트를 더합니다.

<!-- swarms-points:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| 무리의 함선 | 무리 | 처치당 PvE 포인트 |
| :--- | :--- | ---: |
| **Pirate Boss** | Pirate 무리 | 10 |
| **Pirate Scout** | Pirate 무리 | 1 |
| **Dormant Force** | Dormant 무리 | 25 |
| **Dormant Pulse** | Dormant 무리 | 10 |
| **Boss Seeker** | Seeker 무리 | 5 |
| **Seeker Slave** | Seeker 무리 | 1 |

<!-- swarms-points:end -->

무리의 처치는 다른 외계인의 처치로 집계되지 않습니다. Boss Seeker나 Seeker Slave는 Seeker를 요구하는 퀘스트에서 Seeker로 인정되지 않으며, 초기화 포인트의 이정표([초기화 일정](/wiki/03-Mechanics/Wipe-Timeline.md#earning-wipe-points))도 다섯 외계인의 것뿐입니다.
