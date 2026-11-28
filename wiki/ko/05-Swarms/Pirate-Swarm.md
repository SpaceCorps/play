<!-- wiki-i18n source: 33448f95d2520b3a -->
<!-- wiki-i18n title: Pirate 무리 -->
# Pirate 무리 {#pirate-swarm}

Pirate 무리는 **Pirate Boss**와 그 **Pirate Scout**로 이루어집니다. Pirate Boss는 아무도 공격하지 않고 로켓으로 응수하는 거대하고 느린 함선이며, Pirate Scout는 이를 지키고 회복시키는 더 빠른 함선들의 무리입니다. 기업의 기지와 국경 사이의 섹터, 곧 게임 중반 레벨대의 장소에 있으며, 파일럿 그룹에게는 빠른 처치가 아니라 긴 전투가 됩니다.

## 한눈에 보기 {#at-a-glance}

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **위치**: 모든 기업의 `x-2`와 `x-3` 섹터
- **개수**: 해당 섹터마다 하나씩, 월드마다 6개
- **출현**: 시즌 4일차부터 초기화까지(베타와 감마: 시즌 1일차부터)
- **리더**: Pirate Boss
- **부하**: 최대 5 × Pirate Scout, 10초마다 새로 하나
- **부하가 머무는 범위**: 리더로부터 900유닛 이내
- **회복**: 리더로부터 600유닛 이내에 있는 Pirate Scout는 한 마리마다 리더의 선체를 회복시킵니다(Alpha에서 초당 40 HP)
- **리더 격파 후**: 리더가 격파되고 1분 뒤에 부하는 사라집니다. 단, 공격 중이면 남습니다
- **복귀**: 리더가 격파되고 {{guide:vitals.respawn@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} 뒤, 같은 섹터에서
- **알림**: 해당 섹터의 파일럿에게 리더가 나타날 때와 격파될 때 알려 줍니다. 이 줄들은 시스템 줄입니다. 채팅의 **시스템** 탭에 읽지 않은 줄 수와 함께 표시되고, **전체** 탭이나 **지역** 탭에는 나오지 않습니다. 킬 피드에 처치 공로를 인정받은 파일럿의 이름이 나옵니다.

<!-- pirate-glance:end -->

## 구성원 {#the-members}

- **Pirate Boss**: Ironclad를 바탕으로 한 함선으로, 그 힘의 일부를 가집니다(수치는 아래에 있습니다). 비공격적이며 **레이저를 쏘지 않습니다**. 유일한 무기는 **직선 로켓**([로켓](/wiki/06-Items/Rockets.md). 어느 로켓인지는 섹터에 따라 다르며 표를 참조하세요)이고, 자신을 공격한 파일럿에게 발사하며 발사하는 동안에도 계속 돌아다닙니다. 스스로 선체를 수리하지 않습니다. 대장의 [세 단계](#the-leaders-three-steps)와 [특수 능력](/wiki/03-Mechanics/Special-Abilities.md)은 이를 바꿀 수 있습니다.
- **Pirate Scout**: Kitefin을 바탕으로 한 함선으로, 그 힘의 일부를 가집니다. Scout는 가까이 오는 모든 파일럿을 공격하고, 보스 곁에 머물며, 보스 가까이에 있는 Scout는 한 척마다 보스의 선체를 회복시킵니다.

## 전투의 흐름 {#how-the-fight-goes}

- **Scout가 아니라 보스를 쏘세요.** Scout는 보스를 회복시키지만, 보스의 선체에 비하면 회복량은 작고, 새 Scout는 *한눈에 보기* 목록이 알려 주는 간격으로 나타납니다. Scout를 먼저 잡는 그룹은 결코 앞서지 못하고, 아주 큰 그룹만이 Scout를 치울 수 있지만 그래도 내버려 둔 그룹보다 보스를 쓰러뜨리는 데 더 오래 걸립니다. Scout는 시간을 빼앗을 뿐 전투의 승패를 가르지는 않습니다.
- **Scout를 따돌리세요.** Scout는 보스의 사거리 안에 있는 동안에만 회복시키므로, 당신을 쫓아 그 범위를 벗어난 Scout는 아무것도 회복시키지 못하고, Ostirion은 Scout보다 빠릅니다.
- **계속 움직이세요.** 보스의 로켓은 직선이며 유도되지 않습니다. 계속 움직이는 함선은 피하지만 멈춘 함선은 맞습니다.
- **그룹을 데려가세요.** Ostirion을 탄 세 파일럿은 x2 탄약으로 `x-2`에서 함선을 한 척도 잃지 않고 이기지만 간신히 이기고, `x-3`에서는 피해가 나뉘어 들어오는 동안에도 파괴됩니다. 네 명이면 Alpha에서 약 3분 만에 쓰러뜨립니다. x4 탄약이면 `x-3`에서 세 명이 약 2분 만에 쓰러뜨립니다. 다섯 명은 피해가 나뉘어 들어오면 약 2분 30초, 한 파일럿이 모든 공격을 받아 내면 약 3분 만에 쓰러뜨리지만, 그때는 함선 두 척을 잃습니다. 한 파일럿이 모든 공격을 받아 내는 그룹에는 다섯 명이 필요합니다. Beta에서는 다섯 명, Gamma에서는 일곱 명이 필요합니다(피해가 나뉘어 들어올 때. 그곳의 보스는 더 크고 Scout의 치유도 더 큽니다). Alpha의 `x-3`에서 x2 탄약을 쓰면 Ostirion 한 척으로는 못 하고 Paragon 한 척으로도 못 하지만, Paragon 두 척이면 안전하게 할 수 있습니다. Beta와 Gamma의 `x-3`에서는 x2 탄약으로도 x4 탄약으로도 Paragon 한 척은 파괴됩니다. 보스는 처음 공격한 파일럿에게 응수하므로 가장 튼튼한 함선이 먼저 공격하게 하고, 이렇게 긴 전투에서는 능력(Emergency Repair, Shield Surge: [능력](/wiki/03-Mechanics/Abilities.md))을 사용하세요. 아직 레벨 2나 3인 파일럿은 자신이 비행하는 섹터에서도 너무 약합니다. 더 강해질 때까지 가까이 가지 마세요.
- **보스는 돌아옵니다.** *한눈에 보기* 목록의 시간이 지나면 같은 섹터에 나타납니다.

## 대장의 세 단계 {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

이 전투에는 세 단계가 있습니다([작동 방식](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)). 각각 한 번씩만 일어납니다.

- **시작 시**: 처음 자신을 때린 파일럿에게 12도 간격으로 로켓 3발을 부채꼴로 쏩니다.
- **삼분의 이 아래**: Pirate Scouts을(를) 한꺼번에 5마리 더 부릅니다. 최대 10마리까지 살아 있으며, 보상은 없고 45초 뒤에 떠납니다.
- **삼분의 일 아래**: 10초 동안 속도 ×1.8로 가장 가까운 게이트로 날아간 뒤 파일럿에게 돌아섭니다.

<!-- mob-ladder:end -->

## 보상과 전리품 {#rewards-and-drops}

Pirate Boss는 그 싸움에 걸맞은 보상을 지급합니다. 그와 1분 싸우면 Goombah와 1분 싸우는 것보다 보상이 많습니다. 보상은 싸운 파일럿들 사이에서 피해량에 따라 나뉩니다([보스 처치 보상](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). 상자는 가장 많은 피해를 입힌 파일럿에게 돌아가며, **Reinforced Hull Plate**와 로켓, 탄약이 들어 있을 수 있습니다. 상자의 가치는 처치 자체가 지급하는 보상의 절반에 조금 못 미칩니다. Scout의 보상은 소액이고 아무것도 떨어뜨리지 않습니다.

## 수치 {#the-numbers}

무리 함선의 세 월드에서의 수치입니다([월드](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss

바탕은 Ironclad이며, 선체와 실드, 피해량은 그 50%입니다. 속도와 사거리는 바탕이 된 함선의 것입니다. 5초마다 직선 로켓을 한 발 발사합니다: `x-2`: [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets), `x-3`: [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 선체 | {{guide:vitals.hull@Pirate Boss#1}} | {{guide:vitals.hull@Pirate Boss#2}} | {{guide:vitals.hull@Pirate Boss#3}} |
| 실드 | {{guide:vitals.shield@Pirate Boss#1}} | {{guide:vitals.shield@Pirate Boss#2}} | {{guide:vitals.shield@Pirate Boss#3}} |
| 레이저 피해량(초당 일제 사격 1회) | 없음 | 없음 | 없음 |
| 속도 | {{guide:vitals.speed@Pirate Boss#1}} | {{guide:vitals.speed@Pirate Boss#2}} | {{guide:vitals.speed@Pirate Boss#3}} |
| 레이저 사거리 | – | – | – |
| 어그로 반경 | 공격받을 때만 | 공격받을 때만 | 공격받을 때만 |
| 로켓 피해량(최대) | {{guide:behaviour.ability:rocket.damage@Pirate Boss#1}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#2}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#3}} |
| 크레딧 | {{guide:spoils.pay.credits@Pirate Boss#1}} | {{guide:spoils.pay.credits@Pirate Boss#2}} | {{guide:spoils.pay.credits@Pirate Boss#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Boss#1}} | {{guide:spoils.pay.thulium@Pirate Boss#2}} | {{guide:spoils.pay.thulium@Pirate Boss#3}} |
| 경험치(XP) | {{guide:spoils.pay.experience@Pirate Boss#1}} | {{guide:spoils.pay.experience@Pirate Boss#2}} | {{guide:spoils.pay.experience@Pirate Boss#3}} |
| 명예 | {{guide:spoils.pay.honor@Pirate Boss#1}} | {{guide:spoils.pay.honor@Pirate Boss#2}} | {{guide:spoils.pay.honor@Pirate Boss#3}} |
| 처치당 PvE 포인트 | 15 | 15 | 15 |

**전리품**: 가장 많은 피해를 입힌 파일럿을 위한 상자 하나.

| 아이템 |
| :--- |
| {{guide:spoils.box@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} |

### Pirate Scout

바탕은 Kitefin이며, 선체는 그 50%, 레이저 피해량은 그 113%입니다. 속도와 사거리는 바탕이 된 함선의 것입니다.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| 선체 | {{guide:vitals.hull@Pirate Scout#1}} | {{guide:vitals.hull@Pirate Scout#2}} | {{guide:vitals.hull@Pirate Scout#3}} |
| 실드 | {{guide:vitals.shield@Pirate Scout#1}} | {{guide:vitals.shield@Pirate Scout#2}} | {{guide:vitals.shield@Pirate Scout#3}} |
| 레이저 피해량(초당 일제 사격 1회) | {{guide:vitals.dps@Pirate Scout#1}} | {{guide:vitals.dps@Pirate Scout#2}} | {{guide:vitals.dps@Pirate Scout#3}} |
| 속도 | {{guide:vitals.speed@Pirate Scout#1}} | {{guide:vitals.speed@Pirate Scout#2}} | {{guide:vitals.speed@Pirate Scout#3}} |
| 레이저 사거리 | 700 | 700 | 700 |
| 어그로 반경 | {{guide:vitals.aggro@Pirate Scout#1}} | {{guide:vitals.aggro@Pirate Scout#2}} | {{guide:vitals.aggro@Pirate Scout#3}} |
| 리더 회복(한 마리마다 초당, 선체만) | 40 | 60 | 80 |
| 크레딧 | {{guide:spoils.pay.credits@Pirate Scout#1}} | {{guide:spoils.pay.credits@Pirate Scout#2}} | {{guide:spoils.pay.credits@Pirate Scout#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Scout#1}} | {{guide:spoils.pay.thulium@Pirate Scout#2}} | {{guide:spoils.pay.thulium@Pirate Scout#3}} |
| 경험치(XP) | {{guide:spoils.pay.experience@Pirate Scout#1}} | {{guide:spoils.pay.experience@Pirate Scout#2}} | {{guide:spoils.pay.experience@Pirate Scout#3}} |
| 명예 | {{guide:spoils.pay.honor@Pirate Scout#1}} | {{guide:spoils.pay.honor@Pirate Scout#2}} | {{guide:spoils.pay.honor@Pirate Scout#3}} |
| 처치당 PvE 포인트 | 4 | 4 | 4 |

**전리품**: 없음. 처치로 지급되는 것은 크레딧, Thulium, 경험치, 명예뿐입니다.

<!-- pirate-members:end -->
