<!-- wiki-i18n source: 1bd9596fdd648d47 -->
<!-- wiki-i18n title: 드론 -->
# 드론 {#drones}

드론은 구매하거나 제작할 수 있는 지원 유닛입니다. Slave Drone과 Master Drone을 합쳐 최대 **드론 8기**를 동시에 활성화할 수 있습니다. 아래 트리에 있는 16종의 **드론 편대**는 드론이 아닙니다. 연구하고 제작해서 퀵슬롯에서 하나씩 쓰는 것이며, 드론을 최소 한 기 가지고 있는 동안만 작동합니다([드론 편대](/wiki/03-Mechanics/Formations.md) 참고).

![The Repair Drone of an extra slot docked to its ship and its wingmen](../../img/wiki-img/shots/repair-drones-extra.jpg)

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## 아이템 트리 {#item-tree}

어셈블리에서 만드는 것은 먼저 해당 기술이 필요합니다. 아이템에 마우스를 올리면 연구에 걸리는 시간을 볼 수 있습니다. 기술 트리, 연료, 부스트는 [연구](/wiki/03-Mechanics/Research.md)에 있습니다.

```tree
Slave Drone | drone, common | buy 100000 Credits | /wiki/06-Items/Drones.md#available-drones
Master Drone | drone, rare | craft 40000 Thulium, 60 s | research 36000 s, 36000 science | 1 Slave Drone, 100 Ship Fragment | /wiki/06-Items/Drones.md#available-drones
Testudo Formation | formation, epic | craft 7500 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Bodkin Formation | formation, epic | craft 21000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Asterism Formation | formation, epic | craft 7000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Adamant Formation | formation, epic | craft 9000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Ballista Formation | formation, epic | craft 24000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Sanctum Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Shrike Formation | formation, epic | craft 8500 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Culler Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Redoubt Formation | formation, epic | craft 21000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Auger Formation | formation, epic | craft 20500 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Cordon Formation | formation, epic | craft 21500 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Centurion Formation | formation, epic | craft 8000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Gyre Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Gemini Formation | formation, mythical | craft 38000 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Stiletto Formation | formation, mythical | craft 46000 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Rampart Formation | formation, mythical | craft 38500 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations

Slave Drone => Master Drone
```
<!-- item-tree:end -->

## 사용 가능한 드론 {#available-drones}

| 이름 | 희귀도 | 슬롯 | 설명 | 비용 |
| :--------------- | :----- | :---- | :------------------------------------------------------------------------------------------- | :------------------------------- |
| **Slave Drone**  | 일반 | 1     | 장비 슬롯이 하나인 기본 드론입니다. 외계인을 격파하며 8레벨까지 성장합니다. | 100,000 크레딧부터 (아래 참고) |
| **Master Drone** | 희귀   | 2     | 어셈블리에서 업그레이드한 Slave Drone입니다. 금색으로 비행하고, 드론 번호와 장착한 장비는 그대로이며, 두 번째 장비 슬롯이 생기고, 레벨 1부터 다시 시작합니다. | Slave Drone 업그레이드: 40,000 Thulium과 Ship Fragment 100개 |

Slave Drone은 작은 구체로 시작해 레벨 8에서는 중무장한 건십으로 성장합니다. 보유한 모든 드론은 외계인을 격파할 때마다 같은 경험치를 얻으며, 레벨이 높을수록 드론 슬롯에 장착한 레이저의 피해량이 조금씩 늘어납니다(레벨 8에서 최대 +7%). 각 레벨과 그에 필요한 경험치는 게임 시스템 분류의 드론 시스템 페이지에서 볼 수 있습니다. Master Drone 제작은 드론을 소모하지 않습니다. 선택한 Slave Drone을 그 자리에서 업그레이드하며, 업그레이드가 끝나면 **레벨과 경험치가 0으로 초기화됩니다**(어셈블리가 이를 알려 주고 확인을 요청합니다). 그 대신 드론의 **장비 슬롯이 하나에서 두 개**로 늘어납니다. 장착하고 있던 장비는 첫 번째 슬롯에 그대로 남고 두 번째 슬롯은 비어 있습니다. 보유한 드론은 레벨과 경험치까지 포함해 시즌 초기화 후에도 유지됩니다.

## Slave Drone 가격 {#slave-drone-prices}

구매하는 Slave Drone은 하나씩 살 때마다 가격이 오릅니다. 가격은 구매 시점에 보유한 드론 수에 따라 정해지며(Master Drone도 1기로 셉니다), 상점에는 항상 다음 드론의 가격이 표시됩니다. 처음 3기는 크레딧만 들고, 4번째부터는 Thulium이 추가됩니다.

| 드론 | 크레딧 | Thulium |
| :---- | :--------- | :------ |
| 1번째 | 100,000    | –       |
| 2번째 | 200,000    | –       |
| 3번째 | 400,000    | –       |
| 4번째 | 800,000    | 10,000  |
| 5번째 | 1,600,000  | 20,000  |
| 6번째 | 3,200,000  | 30,000  |
| 7번째 | 6,400,000  | 40,000  |
| 8번째 | 12,800,000 | 50,000  |

8기를 모두 사는 데는 25,500,000 크레딧과 150,000 Thulium이 듭니다. 드론은 시즌 초기화 후에도 유지되므로 가격은 보유한 수에서 이어집니다. 드론이 3기면 다음 드론은 항상 4번째이고, 8기를 보유하면 더 살 드론이 없습니다.

## 사용법 {#usage}

1. 상점에서 Slave Drone을 **구매**합니다. 금색 드론이 필요하면 어셈블리에서 하나를 Master Drone으로 **업그레이드**합니다(레벨과 경험치는 다시 시작합니다).
2. 격납고의 “드론” 탭에서 드론을 **장착**합니다.
3. 드론에 레이저나 실드를 **탑재**해 전투력을 높입니다. Slave Drone은 슬롯이 하나, Master Drone은 둘입니다. 레이저는 함선과 함께 발사하고, 실드는 코어 슬롯에 장착한 것과 똑같이 취급되어 모든 능력치가 그대로 적용됩니다.
4. 외계인을 격파해 드론을 **성장**시킵니다. 격납고에서 각 드론의 레벨과 다음 레벨에 필요한 경험치를 확인할 수 있습니다.
5. 제작한 **드론 편대**가 있다면 쓰세요. 편대 목록에서 퀵슬롯으로 드래그해 놓고 그 슬롯의 키를 누릅니다([드론 편대](/wiki/03-Mechanics/Formations.md)).

**Repair Drone**은 이 함대의 드론이 아니라 [부가 장비](/wiki/06-Items/Extras.md#repair-drones)입니다. 선체를 수리하는 동안 작은 수리 드론이 함선에서 날아 나와 빔을 쏘고, 근처 파일럿에게도 보입니다.
