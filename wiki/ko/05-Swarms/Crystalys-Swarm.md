<!-- wiki-i18n source: 2b3edf7bcb1d9673 -->
<!-- wiki-i18n title: Crystalys 무리 -->
# Crystalys 무리 {#crystalys-swarm}

Crystalys 무리는 **Boss Crystalys**와 그 **Crystalys Guard**로 이루어집니다. 가장 단단한 외계인인 [Crystalys](/wiki/04-Aliens/Crystalys.md)를 더 크게 키운 것으로, 곁에 머물며 회복시키는 호위들이 따릅니다. [위험 섹터](/wiki/01-General/Danger-Sectors.md)인 `DS-1`, `DS-2`, `DS-3`에 하나씩 있으며 자기 섹터를 벗어나지 않습니다. 위험 섹터는 PvP 섹터이므로 이 전투는 최강 파일럿들의 대규모 그룹을 위한 것이고, 그곳의 위험은 보스만이 아닙니다.

## 한눈에 보기 {#at-a-glance}

<!-- crystalys-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **위치**: 위험 섹터 `DS-1`, `DS-2`, `DS-3`
- **개수**: 해당 섹터마다 하나씩, 월드마다 3개
- **출현**: 시즌 4일차부터 초기화까지(베타와 감마: 시즌 1일차부터)
- **리더**: Boss Crystalys
- **부하**: 최대 3 × Crystalys Guard, 10초마다 새로 하나
- **부하가 머무는 범위**: 리더로부터 500유닛 이내
- **회복**: 리더로부터 600유닛 이내에 있는 Crystalys Guard는 한 마리마다 리더의 선체를 회복시킵니다(Alpha에서 초당 250 HP)
- **리더 격파 후**: 리더가 격파되고 30초 뒤에 부하는 사라집니다. 단, 공격 중이면 남습니다
- **복귀**: 리더가 격파되고 {{guide:vitals.respawn@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} 뒤, 같은 섹터에서
- **알림**: 해당 섹터의 파일럿에게 리더가 나타날 때와 격파될 때 알려 줍니다. 이 줄들은 시스템 줄입니다. 채팅의 **시스템** 탭에 읽지 않은 줄 수와 함께 표시되고, **전체** 탭이나 **지역** 탭에는 나오지 않습니다. 킬 피드에 처치 공로를 인정받은 파일럿의 이름이 나옵니다.

<!-- crystalys-glance:end -->

## 구성원 {#the-members}

- **Boss Crystalys**: 무리의 색조를 띠고 머리 위에 이름이 표시되는 더 큰 Crystalys입니다. 자체 선체와 실드, 레이저 일제 사격을 갖습니다(수치는 아래에 있습니다). 비공격적이어서 파일럿에게 공격받을 때까지 돌아다니다가, 공격받으면 그 파일럿을 쫓아가 사격하고, 가까이 있는 무리의 함선들이 전투에 합류합니다. 무기 사거리와 속도는 Crystalys 그대로이며, 스스로 선체를 수리하지 않습니다. 대장의 [세 단계](#the-leaders-three-steps)와 [특수 능력](/wiki/03-Mechanics/Special-Abilities.md)은 이를 바꿀 수 있습니다.
- **Crystalys Guard**: 무리의 색조를 띤 더 작은 Crystalys입니다. Guard는 보스 곁에 머물고, 가까운 무리의 함선이 공격받으면 전투에 합류하며, 보스 가까이에 있는 Guard는 한 마리마다 보스의 선체를 회복시킵니다. Guard는 Crystalys처럼 한동안 쉬면 자기 선체를 수리합니다.

## 전투의 흐름 {#how-the-fight-goes}

- **대규모 그룹을 데려가세요.** Alpha에서는 x2 탄약을 쓰는 Paragon 레벨 8 파일럿이 여섯 명이면 충분합니다. 보스의 사격이 분산될 때 그렇고, 한 파일럿에게 집중되면 아홉 명이 필요합니다. x4 탄약이면 각각 다섯 명과 여섯 명입니다. 인원이 많을수록 전투가 빨리 끝나고 잃는 함선이 줄며, 혼자서는 격파당합니다.
- **Guard가 아니라 보스를 쏘세요.** Guard는 몇 초 만에 쓰러지지만 *한눈에 보기* 목록에 나온 간격으로 새로 나타나고, Guard가 회복시키는 양은 그룹이 입히는 피해의 일부에 불과합니다. 내버려 두면 시간이 조금 들고, 쫓아다니면 더 듭니다.
- **Beta와 Gamma는 더 어렵습니다.** 그 월드의 무리는 더 강하므로([월드](/wiki/05-Swarms/Swarms.md#the-worlds)) 더 많은 파일럿이나 더 좋은 탄약이 필요합니다.
- **위험 섹터는 PvP입니다.** 라이벌이 전투 한가운데에서 그룹을 공격하고 상자를 기다릴 수 있습니다. 상자는 30초 동안은 가장 많은 피해를 입힌 파일럿(과 소속 클랜)의 것이고, 그 뒤에는 누구나 가져갈 수 있습니다([화물](/wiki/03-Mechanics/Cargo.md)). 동료와 함께 가세요.
- **보스는 돌아옵니다.** *한눈에 보기* 목록의 시간이 지나면 같은 섹터에 온전한 상태로 나타나며, Guard는 하나씩 차례로 나타납니다.

## 대장의 세 단계 {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

이 전투에는 세 단계가 있습니다([작동 방식](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)). 각각 한 번씩만 일어납니다.

- **시작 시**: 8초 동안 모든 공격의 50%만 받습니다.
- **삼분의 이 아래**: 700 유닛의 고리가 안에 있는 모든 함선을 그 일제 사격의 4만큼으로 치고, 로켓 4발을 쏩니다.
- **삼분의 일 아래**: 선체와 실드의 20%를 회복하고(피해의 몰아치기로 중단됩니다), Crystalys Guards이(가) 3마리 더 옵니다. 최대 6마리까지 살아 있습니다.

<!-- mob-ladder:end -->

## 보상과 전리품 {#rewards-and-drops}

Boss Crystalys의 보상은 그 전투의 무게에 걸맞습니다. 1분 싸우면 가장 보상이 큰 외계인인 Crystalys와 1분 싸울 때보다 많이 받습니다. 보상은 싸운 파일럿들 사이에서 피해량에 따라 나뉩니다([보스 처치 보상](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). 상자에는 Cataclysite와 Quorvium, 이따금 Power Core, Ancient Control Unit 또는 Dark Matter, x3와 x4 탄약, 영웅 등급 로켓이 들어 있으며, 가장 많은 피해를 입힌 파일럿에게 돌아갑니다. Guard의 보상은 소액이고 아무것도 떨어뜨리지 않습니다. 보스와 함께 돌아오기 때문에 잡아도 파밍이 되지 않습니다.

## 수치 {#the-numbers}

무리 함선의 세 월드에서의 수치입니다([월드](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- crystalys-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Crystalys

바탕은 Crystalys이며, 선체는 그 350%, 레이저 피해량은 그 100%입니다. 속도와 사거리는 바탕이 된 함선의 것입니다.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 선체 | {{guide:vitals.hull@Boss Crystalys#1}} | {{guide:vitals.hull@Boss Crystalys#2}} | {{guide:vitals.hull@Boss Crystalys#3}} |
| 실드 | {{guide:vitals.shield@Boss Crystalys#1}} | {{guide:vitals.shield@Boss Crystalys#2}} | {{guide:vitals.shield@Boss Crystalys#3}} |
| 레이저 피해량(초당 일제 사격 1회) | {{guide:vitals.dps@Boss Crystalys#1}} | {{guide:vitals.dps@Boss Crystalys#2}} | {{guide:vitals.dps@Boss Crystalys#3}} |
| 속도 | {{guide:vitals.speed@Boss Crystalys#1}} | {{guide:vitals.speed@Boss Crystalys#2}} | {{guide:vitals.speed@Boss Crystalys#3}} |
| 레이저 사거리 | 900 | 900 | 900 |
| 어그로 반경 | 공격받을 때만 | 공격받을 때만 | 공격받을 때만 |
| 크레딧 | {{guide:spoils.pay.credits@Boss Crystalys#1}} | {{guide:spoils.pay.credits@Boss Crystalys#2}} | {{guide:spoils.pay.credits@Boss Crystalys#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Crystalys#1}} | {{guide:spoils.pay.thulium@Boss Crystalys#2}} | {{guide:spoils.pay.thulium@Boss Crystalys#3}} |
| 경험치(XP) | {{guide:spoils.pay.experience@Boss Crystalys#1}} | {{guide:spoils.pay.experience@Boss Crystalys#2}} | {{guide:spoils.pay.experience@Boss Crystalys#3}} |
| 명예 | {{guide:spoils.pay.honor@Boss Crystalys#1}} | {{guide:spoils.pay.honor@Boss Crystalys#2}} | {{guide:spoils.pay.honor@Boss Crystalys#3}} |
| 처치당 PvE 포인트 | 30 | 30 | 30 |

**전리품**: 가장 많은 피해를 입힌 파일럿을 위한 상자 하나.

| 아이템 |
| :--- |
| {{guide:spoils.box@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} |

### Crystalys Guard

바탕은 Crystalys이며, 선체와 실드, 피해량은 그 15%입니다. 속도와 사거리는 바탕이 된 함선의 것입니다.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 선체 | {{guide:vitals.hull@Crystalys Guard#1}} | {{guide:vitals.hull@Crystalys Guard#2}} | {{guide:vitals.hull@Crystalys Guard#3}} |
| 실드 | {{guide:vitals.shield@Crystalys Guard#1}} | {{guide:vitals.shield@Crystalys Guard#2}} | {{guide:vitals.shield@Crystalys Guard#3}} |
| 레이저 피해량(초당 일제 사격 1회) | {{guide:vitals.dps@Crystalys Guard#1}} | {{guide:vitals.dps@Crystalys Guard#2}} | {{guide:vitals.dps@Crystalys Guard#3}} |
| 속도 | {{guide:vitals.speed@Crystalys Guard#1}} | {{guide:vitals.speed@Crystalys Guard#2}} | {{guide:vitals.speed@Crystalys Guard#3}} |
| 레이저 사거리 | 900 | 900 | 900 |
| 어그로 반경 | 공격받을 때만 | 공격받을 때만 | 공격받을 때만 |
| 리더 회복(한 마리마다 초당, 선체만) | 250 | 375 | 500 |
| 크레딧 | {{guide:spoils.pay.credits@Crystalys Guard#1}} | {{guide:spoils.pay.credits@Crystalys Guard#2}} | {{guide:spoils.pay.credits@Crystalys Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Crystalys Guard#1}} | {{guide:spoils.pay.thulium@Crystalys Guard#2}} | {{guide:spoils.pay.thulium@Crystalys Guard#3}} |
| 경험치(XP) | {{guide:spoils.pay.experience@Crystalys Guard#1}} | {{guide:spoils.pay.experience@Crystalys Guard#2}} | {{guide:spoils.pay.experience@Crystalys Guard#3}} |
| 명예 | {{guide:spoils.pay.honor@Crystalys Guard#1}} | {{guide:spoils.pay.honor@Crystalys Guard#2}} | {{guide:spoils.pay.honor@Crystalys Guard#3}} |
| 처치당 PvE 포인트 | 6 | 6 | 6 |

**전리품**: 없음. 처치로 지급되는 것은 크레딧, Thulium, 경험치, 명예뿐입니다.

<!-- crystalys-members:end -->
