<!-- wiki-i18n source: 2b63df451b6a864e -->
<!-- wiki-i18n title: 부가 장비 -->
# 부가 장비 {#extras}

부가 장비는 함선의 **부가 슬롯**(모든 함선에 구성당 3개이며, Extra Slots CPU로 더 늘어납니다)에 장착하는 장치입니다. 퀵슬롯의 부가 장비 선택창이나 부가 장비를 지정해 둔 퀵슬롯에서 켭니다. 비행 중인 구성에서만 작동하며, 다른 구성에 장착하면 구성을 전환할 때까지 대기합니다.

| 부가 장비 | 효과 | 사용 횟수 | 가격 |
| :---- | :----------- | :--- | :---- |
| **Repair Drone I~IV** | 선체를 수리합니다. 초당 최대치의 1.5%, 2.25%, 3.5%, 5% | 무제한 | 5,000 / 15,000 / 35,000 크레딧, 2,000 Thulium |
| **Cloaking CPU S** | 함선을 숨깁니다 | 10 | 5,000 Thulium |
| **Cloaking CPU M** | 함선을 숨깁니다 | 25 | 11,250 Thulium |
| **Cloaking CPU L** | 함선을 숨깁니다 | 50 | 20,000 Thulium |
| **EMP Charge** | 3초 동안 아무도 당신을 대상으로 지정할 수 없고, 당신에 대한 모든 락온이 해제되며, 주변의 모든 은폐가 해제됩니다 | 1 | 500 Thulium |

Cloaking CPU와 EMP Charge는 상점에서만 판매합니다. 병합할 수 없고, 무상으로 지급되지도 않습니다.

CPU 일곱 가지는 판매하지 않습니다. Skylab의 연구 센터가 연구를 마치면 어셈블리에서 제작할 수 있습니다([연구](/wiki/03-Mechanics/Research.md) 참고). Extra Slots CPU I·II·III, Jump CPU, Base CPU I·II, Auto-Repair CPU이며, 각각의 기능은 [마지막 절](#research-cpus)에 있습니다. Cloaking CPU처럼 Jump CPU와 Base CPU도 조용한 때를 위한 장비입니다. 내가 사격하거나 공격을 받고 나서 10초 안에는 이 셋 중 어느 것도 시작되지 않습니다.

부가 장비마다 퀵슬롯에 짧은 표기가 붙습니다. Repair Drone은 **REP**, Cloaking CPU는 **CLK**, EMP Charge는 **EMP**이고, Auto-Repair CPU, Base CPU, Jump CPU는 각각 **ARP**, **BSE**, **JMP**입니다. Extra Slots CPU에는 슬롯이 없으며 Skylab에 설치됩니다. 슬롯에 포인터를 올리면 지금 누르면 무엇이 일어나는지, 또는 왜 아무 일도 일어나지 않는지 볼 수 있습니다.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## 아이템 트리 {#item-tree}

어셈블리에서 만드는 것은 먼저 해당 기술이 필요합니다. 아이템에 마우스를 올리면 연구에 걸리는 시간을 볼 수 있습니다. 기술 트리, 연료, 부스트는 [연구](/wiki/03-Mechanics/Research.md)에 있습니다.

```tree
Cloaking CPU S | extra, common | buy 5000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Repair Drone I | extra, common | buy 5000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone II | extra, common | buy 15000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone III | extra, common | buy 35000 Credits | /wiki/06-Items/Extras.md#repair-drones
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
EMP Charge | extra, uncommon | buy 500 Thulium | /wiki/06-Items/Extras.md#emp-charge
Cloaking CPU M | extra, uncommon | buy 11250 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 8 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu
Repair Drone IV | extra, rare | buy 2000 Thulium | /wiki/06-Items/Extras.md#repair-drones
Cloaking CPU L | extra, rare | buy 20000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 20 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu

Cloaking CPU S -> Cloaking CPU M -> Cloaking CPU L
Repair Drone I -> Repair Drone II -> Repair Drone III -> Repair Drone IV
Extra Slots CPU I -> Extra Slots CPU II -> Extra Slots CPU III
Base CPU I -> Base CPU II
```
<!-- item-tree:end -->

## Repair Drone {#repair-drones}

Repair Drone을 켜면(REP) 선체가 가득 찰 때까지 수리합니다. 피격 없이 10초가 지나야 작동을 시작하고, 피격되면 즉시 꺼집니다. 여러 개를 장착하면 가장 좋은 것 하나만 작동합니다. [Auto-Repair CPU](#auto-repair-cpu)가 있으면 다시 켜 줍니다. 수리 속도는 [전투](/wiki/03-Mechanics/Combat.md)에 있습니다.

## Cloaking CPU {#cloaking-cpu}

CLK 슬롯을 누르면 은폐합니다. **한 번 누를 때마다 1회 사용으로 계산되며**, 팩의 종류와는 상관없습니다. 남은 사용 횟수는 슬롯과 격납고에서 확인할 수 있습니다. 은폐에는 **시간 제한이 없습니다**. 직접 끄거나 무언가가 해제할 때까지 유지됩니다.

- **당신을 볼 수 없는 대상.** 다른 기업의 파일럿과 외계인은 당신의 함선을 전혀 보지 못합니다. 화면에도 대상 목록에도 나타나지 않으며, 아무도 락온할 수 없습니다. 다른 기업의 기업 파일럿도 당신의 함선을 무시합니다.
- **레이더 점.** 같은 기업을 제외한 맵의 다른 모든 파일럿에게는 미니맵의 당신 위치에 평범한 **빨간 점**이 보여, 은폐 중인 누군가가 근처에 있다는 것을 알 수 있습니다. 이 점에는 이름, 함선, 기업, ID가 없고 클릭하거나 대상으로 지정할 수 없으며, 마우스를 올려도 “여기에 은폐 중인 무언가가 있습니다”라고만 표시됩니다. 점은 둥글고 고리 안에 있으며(미니맵에서 함선은 사각형입니다), 고리는 천천히 숨 쉬듯 커졌다 줄어들고, 움직임 줄이기를 켜 두었다면 가만히 있습니다. 서버가 약 1초에 두 번 갱신하고, 그 사이는 게임이 부드럽게 이동시킵니다. 누군가가 어디에 있는지만 알려 줄 뿐 누구인지는 알려 주지 않습니다. 은폐하는 모습을 본 파일럿은 점을 따라갈 수 있고, 점을 겨냥한 **로켓의 폭발**은 여전히 당신을 맞힙니다.
- **볼 수 있는 대상.** 자신의 함선은 윤곽선이 있는 흐릿한 모습으로 보입니다. 같은 기업의 파일럿에게는 옅은 유령처럼 보입니다. 다른 기업 소속의 클랜원은 볼 수 없는데, 클랜은 가입을 신청한 누구든 받아 주기 때문입니다. 유령은 같은 기업이라도 대상으로 지정할 수 없습니다.
- 안전 지대 안에 있거나, CPU가 재충전 중이거나, 피격 또는 사격 후 **10초** 이내에는 **은폐할 수 없습니다**.
- **은폐가 해제되는 경우.** 슬롯을 다시 누를 때, 첫 일제 사격이나 로켓(명중하면 모습이 드러납니다), 안전 지대 진입, CPU가 비행 중인 구성에서 빠질 때, 누가 발동했든 **1,500유닛 이내에서 EMP가 발동**했을 때(같은 기업의 EMP도 해당하지만 같은 그룹원의 EMP는 제외), 그리고 당신을 맞힌 로켓의 범위 폭발입니다. 시간이 지나는 것, 화물 회수(회수한 상자는 모두에게서 사라지므로 그 자리 가까이에 누군가 있었다는 것은 알려지지만 누구인지는 알려지지 않습니다), 능력 사용으로는 해제되지 않으며, 블랙홀의 방사선은 은폐 중인 함선에도 피해를 주지만 은폐를 해제하지는 않습니다. 로그아웃하거나 파괴되면 해제됩니다. 조종하지 않는 함선은 은폐 상태가 아니기 때문입니다.
- **재충전.** 은폐가 어떤 이유로 끝나든, 이후 CPU는 **60초** 동안 재충전됩니다. 재충전은 함선이 아니라 파일럿에게 귀속되므로, 포털로 점프하거나 로그아웃하거나 파괴되어도 계속됩니다. 누를 때마다 사용 횟수는 여전히 소모됩니다.
- 당신을 쫓던 **외계인**은 당신을 놓칩니다. 은폐하면 처치 선점도 해제됩니다.
- **로켓.** 아무도 당신에게 유도 로켓을 락온할 수 없고, 직선 단일 대상 로켓은 당신을 통과해 날아갑니다. **범위 폭발**은 범위 안의 함선에 여전히 피해를 주고 그 함선의 은폐를 해제하며, 그 함선의 위치를 볼 수 있는 파일럿들에게는 피해 수치가 나타나기 전에 위치가 표시됩니다. 로켓 발사는 사격이므로 일제 사격과 마찬가지로 자신의 은폐를 해제하고(이후 CPU는 위의 60초 동안 재충전됩니다), 은폐 중이든 아니든 발사 후 10초 동안은 은폐할 수 없습니다.
- **블랙홀**은 은폐 중인 함선도 다른 함선과 똑같이 삼키며, 그 사실은 맵 전체에 알려집니다.
- **화면 표시.** 함선이 보라색 점선 윤곽과 함께 반투명해지고, 화면 상단의 칩에 남은 사용 횟수와 함께 “은폐”라고 표시됩니다(타이머가 없으므로 초 표시는 없습니다). CLK 슬롯에는 남은 사용 횟수가 표시되며, 은폐 중에는 보라색으로 빛나며 ON이라고 표시되고, 은폐가 어떤 이유로 끝나든 끝나면 어두워지면서 재충전 60초를 셉니다. 서버가 거부한 입력(재충전 중, 안전 지대, 최근 10초 이내의 피격이나 사격)은 슬롯을 빨갛게 번쩍이게 하고, 메시지로 이유를 알려 줍니다. 아군은 이름 앞에 유령 표시가 붙은 옅은 유령으로 보이며, 근처에서 은폐하는 파일럿은 물결처럼 번지며 사라집니다. REP처럼 퀵슬롯의 부가 장비에서 CLK를 슬롯으로 끌어다 놓으면 사용할 수 있습니다.
- **사용 횟수**는 CPU에 저장됩니다. 로그아웃, 파괴, 게임 재시작으로는 돌려받지 못하며, 취소한 발동도 이미 소모된 것으로 처리됩니다. 한 팩의 마지막 사용 횟수가 소진되면 그 팩은 소모되고, 인벤토리에 같은 CPU의 예비가 있으면 그것으로 슬롯이 다시 채워집니다.
- 한 구성에 **CPU 여러 개**를 장착해도 효과는 합산되지 않습니다. 남은 사용 횟수가 가장 적은 것부터 사용됩니다.

S, M, L은 동작이 같습니다. 큰 팩일수록 사용 1회당 가격만 저렴합니다(500, 450, 400 Thulium).

## EMP Charge {#emp-charge}

전투 중에 EMP 슬롯을 누르세요. **3초** 동안 아무도 당신을 락온할 수 없으며, 당신을 락온하고 있던 **모든 대상은 즉시 락온을 잃습니다**. 어디에 있든 마찬가지이며, 파일럿, 외계인, 기업 파일럿 모두 해당합니다. 락온이 풀린 파일럿에게는 “락온 해제: 대상이 EMP를 사용했습니다”라고 알려 줍니다. 그 3초 동안 락온을 시도하는 대상은 거부됩니다.

- **무적이 아닙니다.** 락온이 필요한 공격, 즉 레이저, 유도 로켓, 그리고 당신을 통과해 날아가는 직선 단일 대상 로켓의 타격을 막아 줍니다. **범위 폭발**은 락온이 필요 없으므로 범위 안에 있으면 여전히 피해를 입으며, 블랙홀은 애초에 사격이 아닙니다.
- **행동은 계속할 수 있습니다.** 사격해도 해제되지 않습니다. 은폐(은폐 자체의 규칙이 허용할 때)와 다른 부가 장비도 사용할 수 있습니다.
- **주변의 은폐를 해제합니다.** 펄스가 터질 때 당신으로부터 **1,500유닛** 이내에서 은폐 중인 모든 함선은 즉시 모습이 드러나고, 해당 함선의 CPU는 60초 동안의 재충전에 들어갑니다. 소속 기업은 상관없으며 당신의 기업도 포함됩니다. 다만 당신의 [그룹](/wiki/03-Mechanics/Groups.md) 함선은 예외로, 은폐가 유지됩니다. 해당 파일럿에게는 “은폐 해제: 근처에서 EMP가 발동했습니다.”라고 알려지고, 함선은 다른 은폐 해제 때와 같은 물결 효과와 함께 다시 나타나며, 슬롯은 재충전을 시작합니다. 자신이 은폐 중일 때는 EMP를 사용할 수 없습니다.
- **아무것도 숨기지 않습니다.** 모두가 여전히 당신을 볼 수 있으며, 3초 동안은 지직거리는 전기 막이 함선을 감쌉니다.
- 안전 지대의 보호를 받는 동안, 은폐 중일 때, 또는 마지막 EMP 사용 후 **30초** 이내에는 **사용할 수 없습니다**. 그 밖의 모든 곳에서 작동하며, 시즌 초반(평화 프로토콜)에도 사용할 수 있습니다. 그때도 외계인은 계속 사냥에 나섭니다.
- 3초 동안 당신이 공격한 외계인은 그 3초가 끝날 때까지 당신에게 반격하지 않습니다. 처치 선점과 첫 타격 규칙은 달라지지 않습니다.
- **화면 표시.** 휘어진 공간의 펄스가 파일럿에게서 은폐를 해제하는 거리(1,500유닛)까지 퍼져 나가며, 범위 안의 모두가 이를 봅니다. 3초 동안은 지직거리는 전기 막이 함선을 감싸고, 자신의 함선 둘레의 고리와 화면 상단의 칩이 남은 시간을 셉니다. 당신을 선택해 둔 모든 대상의 대상 링은 짧은 전기 충격음과 함께 깨집니다. EMP 슬롯에는 보유한 충전량이 표시되고, 막이 유지되는 동안 파란색으로 빛나며, 재충전 중에는 어두워집니다.
- **충전 1개에 1회 사용.** 더 보유하고 있으면 슬롯은 인벤토리에서 다시 채워집니다. **30초**의 재충전 시간은 저장되지 않습니다. 로그아웃하거나 포털로 점프하면 사라지며, 다음 펄스에는 충전 1개가 소모됩니다.

## 연구 센터의 CPU {#research-cpus}

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | 연구 시간 | 먼저 필요한 기술 | 제작에 필요한 Thulium | 제작 시간 |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30분 | – | 12,000 | 5분 |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10시간 | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30,000 | 10분 |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1일 | [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75,000 | 15분 |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3시간 | – | 8,000 | 5분 |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10시간 | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 20,000 | 10분 |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1일 | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40,000 | 15분 |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6시간 | – | 15,000 | 10분 |

어느 것도 상점에서 팔지 않습니다. 기술을 연구한 뒤 어셈블리에서 CPU를 제작합니다. 트리에서 CPU에 마우스를 올리면 어셈블리가 무엇을 요구하는지 볼 수 있습니다.

### Extra Slots CPUs {#extra-slots-cpus}

- **기능.** Extra Slots CPU I·II·III은 모든 함선의 부가 슬롯을 3개, 5개, 7개 늘려 줍니다. 모든 함선이 원래 가진 3개를 더하면 총 6개, 8개, 10개입니다. 상위 CPU는 하위 CPU를 대체합니다. II가 I에 더해지지는 않습니다.
- **장착이 아니라 설치.** Extra Slots CPU는 아이템이 아닙니다. 어셈블리에서 받으면 Skylab에 설치되어 두 구성 모두의 모든 함선에 적용되고, 슬롯을 차지하지 않습니다. 초기화 후에도 남습니다.
- **순서대로.** 하나씩 차례로 제작하세요. II는 I이 설치된 뒤에, III은 II가 설치된 뒤에만 제작할 수 있으며, 그때까지는 어셈블리가 먼저 설치할 것을 알려 줍니다. 셋을 합치면 Thulium 117,000이 듭니다: 12,000, 30,000, 75,000.

### Jump CPU {#jump-cpu}

- **기능.** 함선을 내 월드의 어느 기업 섹터(내 기업의 섹터든 다른 기업의 섹터든, 기지 섹터도 포함. `M`, `T`, `G`의 섹터 1~4)로든 점프시키며, 1회당 **Thulium 500**이 듭니다. 사용 횟수 제한은 없고 Thulium만 내면 됩니다. 위험 섹터(`DS`)나 중립 섹터(`N`)로는 가지 못합니다.
- **점프.** JMP 슬롯을 누르고 항성계 지도에서 섹터를 골라 확정하면, 함선이 5초 동안 충전한 뒤 그 섹터의 게이트에 도착하며, 일반 게이트 점프 후와 같은 보호를 받습니다. 도착 후 CPU는 30초 동안 재사용 대기에 들어갑니다.
- **전투 중에는 불가.** 발사하거나 피격당한 뒤 10초 이내에는 시작할 수 없고, 충전 중 발사하거나 피격당하면 점프가 취소됩니다. 이때는 아무것도 지불하지 않습니다. 은폐 중에는 점프할 수 없습니다.
- **중립 섹터에서는 불가:** 중립 섹터에 있거나 기업에 소속되지 않은 파일럿은 쓸 수 없습니다.
- 전투 중이 아니면 위험 섹터에서 떠날 수 있습니다.

### Base CPUs {#base-cpus}

- **기능.** 함선을 소속 기업의 기지에 있는 정거장 주변 안전 지대(`M-1`, `T-1`, `G-1`, Mission Control이 있는 섹터)로 순간이동시킵니다. Thulium은 들지 않습니다. 퀵슬롯의 BSE 슬롯에서 시작합니다.
- **전투 중에는 불가.** 충전은 10초이며 둘 다 같습니다. 발사하거나 피격당한 뒤 10초 이내, 은폐 중, 이미 기지의 안전 지대 안에 있을 때는 시작할 수 없고, 충전 중 발사하거나 피격당하면 취소됩니다.

| CPU | 사용 횟수 | 재사용 대기 |
| :--- | ---: | ---: |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 10 | 10분 |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 25 | 5분 |

- **소모형, 재충전 없음.** 사용할 때마다 CPU의 사용 횟수가 하나씩 줄고, 횟수가 다 떨어진 CPU는 사라집니다. 새로 제작하세요. 둘 다 장착했다면 상위인 II부터 사용됩니다.

### Auto-Repair CPU {#auto-repair-cpu}

- **기능.** 직접 출격시킬 수 있는 상황이 될 때마다, 부가 슬롯에 장착한 Repair Drone을 자동으로 출격시킵니다. 선체가 가득 차지 않았고, 드론이 이미 나와 있지 않으며, 마지막 피격 후 10초가 지났을 때입니다. 선체 기준치를 설정할 필요는 없습니다.
- 전용 부가 슬롯을 하나 차지하며, 같은 구성의 부가 슬롯에 Repair Drone이 없으면 아무것도 하지 않습니다. 능력 슬롯에 있는 Repair Drone은 내보내지 않습니다(그것은 Emergency Repair 버튼입니다).
- **드론을 직접 멈추면** 선체가 다시 가득 차거나 직접 드론을 출격시킬 때까지 CPU는 건드리지 않습니다.


<!-- research-cpus:end -->
