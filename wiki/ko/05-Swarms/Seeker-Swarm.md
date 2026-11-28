<!-- wiki-i18n source: 7c6bc3eaf70223f5 -->
<!-- wiki-i18n title: Seeker 무리 -->
# Seeker 무리 {#seeker-swarm}

Seeker 무리는 [무리](/wiki/05-Swarms/Swarms.md) 중 가장 작으며, **Boss Seeker**와 이를 지키고 회복시키는 **Seeker Slave**로 이루어집니다. 신규 파일럿이 비행하기 시작하는 섹터에 있어서 대부분의 파일럿이 가장 먼저 만나는 무리입니다. Boss Seeker는 먼저 싸움을 걸지 않지만, 공격하면 바탕이 된 [Seeker](/wiki/04-Aliens/Seeker.md)보다 훨씬 위험합니다.

## 한눈에 보기 {#at-a-glance}

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **위치**: 모든 기업의 `x-1`와 `x-2` 섹터
- **개수**: 해당 섹터마다 하나씩, 월드마다 6개
- **출현**: 시즌 4일차부터 초기화까지(베타와 감마: 시즌 1일차부터)
- **리더**: Boss Seeker
- **부하**: 최대 4 × Seeker Slave, 10초마다 새로 하나
- **부하가 머무는 범위**: 리더로부터 500유닛 이내
- **회복**: 리더로부터 600유닛 이내에 있는 Seeker Slave는 한 마리마다 리더의 선체를 회복시킵니다(Alpha에서 초당 50 HP)
- **리더 격파 후**: 리더가 격파되고 30초 뒤에 부하는 사라집니다. 단, 공격 중이면 남습니다
- **복귀**: 리더가 격파되고 {{guide:vitals.respawn@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} 뒤, 같은 섹터에서
- **알림**: 해당 섹터의 파일럿에게 리더가 나타날 때와 격파될 때 알려 줍니다. 이 줄들은 시스템 줄입니다. 채팅의 **시스템** 탭에 읽지 않은 줄 수와 함께 표시되고, **전체** 탭이나 **지역** 탭에는 나오지 않습니다. 킬 피드에 처치 공로를 인정받은 파일럿의 이름이 나옵니다.

<!-- seeker-glance:end -->

## 구성원 {#the-members}

- **Boss Seeker**: 무리의 색조를 띠고 머리 위에 이름이 표시되는 훨씬 큰 Seeker로, 선체와 실드, 피해량이 Seeker의 몇 배입니다(수치는 아래에 있습니다). 비공격적이어서 파일럿에게 공격받을 때까지 돌아다니다가, 공격받으면 그 자리에 멈춰 그 파일럿에게 사격하고, 가까이 있는 무리의 함선들이 전투에 합류합니다. 무기 사거리와 속도는 Seeker와 같고, 스스로 선체를 수리하지 않습니다. 대장의 [세 단계](#the-leaders-three-steps)와 [특수 능력](/wiki/03-Mechanics/Special-Abilities.md)은 이를 바꿀 수 있습니다.
- **Seeker Slave**: 무리의 색조를 띤 평범한 Seeker입니다. Slave는 보스 곁에 머물고, 가까운 무리의 함선이 공격받으면 전투에 합류하며, 보스 가까이에 있는 Slave는 한 마리마다 보스의 선체를 회복시킵니다. Slave는 Seeker처럼 한동안 쉬면 자기 선체를 수리합니다.

## 전투의 흐름 {#how-the-fight-goes}

- **내 함선이 버틸 수 있을 때까지 건드리지 마세요.** Boss Seeker는 파일럿의 첫 함선이 견딜 수 있는 수준보다 강하게 때립니다. 아직 실드가 없는 신규 파일럿의 Protos는 보스와 Slave가 달라붙으면 몇 초 만에 격파됩니다.
- **사거리 밖에 머무세요.** 보스와 Slave는 Protos보다 느리고 무기 사거리도 Quantum Laser II보다 짧습니다([레이저와 탄약](/wiki/06-Items/Lasers.md) 참조). 그런 레이저를 갖추고 사거리 밖에 머무는 파일럿은 사격을 받아도 피해를 입지 않습니다. Quantum Laser I의 파일럿은 사거리 밖에 머물 수 없습니다.
- **Slave의 회복은 혼자 싸우는 신규 파일럿의 공격보다 빠릅니다.** 합치면 x1 탄약을 쓰는 파일럿 한 명의 레이저가 입히는 피해보다 많이 회복하므로, 동료와 x2 탄약을 준비하세요. Quantum Laser II를 쓰는 두 파일럿이 거리를 유지하면 Alpha에서 약 1분 만에 보스를 쓰러뜨릴 수 있고, x2 탄약이면 훨씬 빠릅니다.
- **보스는 돌아옵니다.** *한눈에 보기* 목록의 시간이 지나면 같은 섹터에 온전한 상태로 나타나며, Slave는 하나씩 차례로 나타납니다.

## 대장의 세 단계 {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

이 전투에는 세 단계가 있습니다([작동 방식](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)). 각각 한 번씩만 일어납니다.

- **시작 시**: Seeker Slaves이(가) 8초 동안 ×2의 속도로 회복시켜 줍니다.
- **삼분의 이 아래**: 분신 2개가 나타나고, 진짜는 고리를 두릅니다.
- **삼분의 일 아래**: 4초 동안 파일럿에게서 달아난 뒤 돌아섭니다.

<!-- mob-ladder:end -->

## 보상과 전리품 {#rewards-and-drops}

Boss Seeker의 보상은 **정확히 Seeker 10마리분**입니다. Seeker의 크레딧, Thulium, 경험치, 명예의 10배가 싸운 파일럿들 사이에서 피해량에 따라 나뉩니다([보스 처치 보상](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). 상자에는 Seeker 10마리분의 전리품에 더해 영웅 등급 미만의 탄약과 로켓이 들어 있으며, 가장 많은 피해를 입힌 파일럿에게 돌아갑니다. Slave의 보상은 소액이고 아무것도 떨어뜨리지 않습니다. 보스와 함께 돌아오기 때문에 잡아도 파밍이 되지 않습니다.

## 수치 {#the-numbers}

무리 함선의 세 월드에서의 수치입니다([월드](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker

바탕은 Seeker이며, 선체와 실드, 피해량은 그 400%입니다. 속도와 사거리는 바탕이 된 함선의 것입니다.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 선체 | {{guide:vitals.hull@Boss Seeker#1}} | {{guide:vitals.hull@Boss Seeker#2}} | {{guide:vitals.hull@Boss Seeker#3}} |
| 실드 | {{guide:vitals.shield@Boss Seeker#1}} | {{guide:vitals.shield@Boss Seeker#2}} | {{guide:vitals.shield@Boss Seeker#3}} |
| 레이저 피해량(초당 일제 사격 1회) | {{guide:vitals.dps@Boss Seeker#1}} | {{guide:vitals.dps@Boss Seeker#2}} | {{guide:vitals.dps@Boss Seeker#3}} |
| 속도 | {{guide:vitals.speed@Boss Seeker#1}} | {{guide:vitals.speed@Boss Seeker#2}} | {{guide:vitals.speed@Boss Seeker#3}} |
| 레이저 사거리 | 600 | 600 | 600 |
| 어그로 반경 | 공격받을 때만 | 공격받을 때만 | 공격받을 때만 |
| 크레딧 | {{guide:spoils.pay.credits@Boss Seeker#1}} | {{guide:spoils.pay.credits@Boss Seeker#2}} | {{guide:spoils.pay.credits@Boss Seeker#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Seeker#1}} | {{guide:spoils.pay.thulium@Boss Seeker#2}} | {{guide:spoils.pay.thulium@Boss Seeker#3}} |
| 경험치(XP) | {{guide:spoils.pay.experience@Boss Seeker#1}} | {{guide:spoils.pay.experience@Boss Seeker#2}} | {{guide:spoils.pay.experience@Boss Seeker#3}} |
| 명예 | {{guide:spoils.pay.honor@Boss Seeker#1}} | {{guide:spoils.pay.honor@Boss Seeker#2}} | {{guide:spoils.pay.honor@Boss Seeker#3}} |
| 처치당 PvE 포인트 | 5 | 5 | 5 |

**전리품**: 가장 많은 피해를 입힌 파일럿을 위한 상자 하나.

| 아이템 |
| :--- |
| {{guide:spoils.box@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} |

### Seeker Slave

바탕은 Seeker이며, 선체와 실드, 피해량은 그 100%입니다. 속도와 사거리는 바탕이 된 함선의 것입니다.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 선체 | {{guide:vitals.hull@Seeker Slave#1}} | {{guide:vitals.hull@Seeker Slave#2}} | {{guide:vitals.hull@Seeker Slave#3}} |
| 실드 | {{guide:vitals.shield@Seeker Slave#1}} | {{guide:vitals.shield@Seeker Slave#2}} | {{guide:vitals.shield@Seeker Slave#3}} |
| 레이저 피해량(초당 일제 사격 1회) | {{guide:vitals.dps@Seeker Slave#1}} | {{guide:vitals.dps@Seeker Slave#2}} | {{guide:vitals.dps@Seeker Slave#3}} |
| 속도 | {{guide:vitals.speed@Seeker Slave#1}} | {{guide:vitals.speed@Seeker Slave#2}} | {{guide:vitals.speed@Seeker Slave#3}} |
| 레이저 사거리 | 600 | 600 | 600 |
| 어그로 반경 | 공격받을 때만 | 공격받을 때만 | 공격받을 때만 |
| 리더 회복(한 마리마다 초당, 선체만) | 50 | 75 | 100 |
| 크레딧 | {{guide:spoils.pay.credits@Seeker Slave#1}} | {{guide:spoils.pay.credits@Seeker Slave#2}} | {{guide:spoils.pay.credits@Seeker Slave#3}} |
| Thulium | {{guide:spoils.pay.thulium@Seeker Slave#1}} | {{guide:spoils.pay.thulium@Seeker Slave#2}} | {{guide:spoils.pay.thulium@Seeker Slave#3}} |
| 경험치(XP) | {{guide:spoils.pay.experience@Seeker Slave#1}} | {{guide:spoils.pay.experience@Seeker Slave#2}} | {{guide:spoils.pay.experience@Seeker Slave#3}} |
| 명예 | {{guide:spoils.pay.honor@Seeker Slave#1}} | {{guide:spoils.pay.honor@Seeker Slave#2}} | {{guide:spoils.pay.honor@Seeker Slave#3}} |
| 처치당 PvE 포인트 | 1 | 1 | 1 |

**전리품**: 없음. 처치로 지급되는 것은 크레딧, Thulium, 경험치, 명예뿐입니다.

<!-- seeker-members:end -->
