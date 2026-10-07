<!-- wiki-i18n source: 6b5935229efa5068 -->
<!-- wiki-i18n title: 연구 -->
# 연구 {#research}

**연구 센터**는 [Skylab](/wiki/03-Mechanics/Skylab.md)의 실험실입니다. 자원을 넣으면 **과학**으로 바뀌고, 그 과학이 **기술**을 연구합니다. [어셈블리](/wiki/06-Items/Overview.md#upgrading-modules)에서 하는 제작은 모두 먼저 해당 기술이 필요합니다. 함선, 레이저, 추진기, CPU는 연구가 끝나기 전에는 만들 수 없습니다.

이 페이지에는 기술 트리 전체와 각 기술의 소요 시간, 자원별 과학량, Thulium 부스트, Dark Matter 규칙, 새로운 CPU가 모여 있습니다. 수치는 게임 자체 데이터에서 읽어 오므로 언제나 게임 속 수치와 같습니다.

![The Research view with a technology that needs Dark Matter picked: its Dark Matter row, the Add and Take back buttons, where Dark Matter comes from and the Wiki button](../../img/wiki-img/shots/research-dark-matter.jpg)
![The Research view filtered to the Defence tree: the shield and hull formations, each a technology with its Dark Matter](../../img/wiki-img/shots/research-formations.jpg)
![The Research view of the Skylab with the pointer on Impulse Thruster III: its kind and tier, what it does, its numbers, the four tiers of its family and what Assembly asks to craft it](../../img/wiki-img/shots/research-hover.jpg)

## 연구 센터 {#the-research-centre}

<!-- research-centre:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **코어 레벨 10에서 열립니다.** 연구 센터는 [Skylab](/wiki/03-Mechanics/Skylab.md)의 모듈이며 다른 모듈처럼 건설합니다. 인벤토리의 Ship Fragment 25개(함선이 착륙한 상태), 크레딧 25,000, Thulium 500이 필요합니다. 화면은 Skylab 페이지의 **연구** 보기입니다.
- **레벨 1~10.** 레벨이 높을수록 탱크가 커지고 전력을 더 씁니다. 연구가 빨라지지는 않습니다. 기술은 어느 레벨에서나 같은 시간이 걸립니다.
- **탱크.** 연구 센터는 과학을 탱크에 보관합니다. 탱크는 레벨 1에서 12시간 분량의 연구를 담고, 레벨이 오를 때마다 25%씩 더 담습니다(아래 표).
- **연료가 과학으로.** 넣은 자원은 즉시 과학이 됩니다(연료 표 참고). 연구는 소요 시간 1초마다 과학 1을 태웁니다. 탱크가 비면 기다렸다가, 센터에 다시 넣으면 이어서 진행됩니다.
- **첫 1시간은 무료.** 새 연구 센터는 탱크에 과학 3,600(연구 1시간 분량)를 담은 채 시작합니다.
- **한 번에 하나.** 연구 센터는 한 번에 기술 하나만 연구합니다. 대기열은 없습니다.
- **자리를 비운 동안.** 연구는 서버의 시계로 진행되므로 로그아웃해도 계속되며, 끝나거나 탱크가 빌 때까지 이어집니다. 전력 부족이나 연구 센터 업그레이드로는 멈추지 않습니다.
- **전력.** 연구 센터는 레벨 1에서 25를 쓰고 레벨이 오를 때마다 15%씩 더 쓰며, 끌 수 없습니다.
- **초기화해도 모두 남습니다:** 기술, 탱크의 과학, 넣어 둔 Dark Matter, 진행 중인 연구, 부스트.
- **가진 것은 내 것입니다.** 연구가 게임에 들어올 때, 모든 파일럿은 이미 가지고 있던 아이템 각각의 기술과 그것에 필요했던 기술을 받았습니다. 나중에 얻은 아이템(선물, 코드, 보상)은 그 기술을 열어 주지 않습니다.
- **코어 레벨 10 미만**에서는 연구할 수 없으므로 어셈블리에서 새로운 것을 아직 만들 수 없습니다. 정거장 미션이 코어를 올리도록 안내해 줍니다.

<!-- research-centre:end -->

**레이저 증폭기와 마지막 티어.** 티어 II~IV의 Damage Amp, Crit Amp, Penetration Amp는 다른 제작품과 똑같이 연구합니다. 증폭기 계열이 나왔을 때 증폭기를 가지고 있었거나 제작 대기 중이던 파일럿은 그 증폭기 각각의 기술과 그 아래 티어의 기술을 받았습니다. 다른 트리의 기술을 필요로 하는 기술은 12개입니다. 자원 트리에 있는 Dark Matter Plate의 기술입니다. 모든 강화 계열의 마지막 티어가 플레이트 3개를 요구하기 때문이며, 티어 IV의 Damage Amp, Crit Amp, Penetration Amp, 티어 IV의 Absorption Shield Cell, Capacity Shield Cell, 티어 IV의 Impulse Thruster, Momentum Thruster, 그리고 Heavy Shield Core, Engine III, Helios Beam, Extra Slots CPU III, Base CPU II가 여기에 해당합니다. 이미 그중 하나를 연구했다면 그 기술은 그대로 남지만, 거기에 필요한 플레이트를 만들려면 Dark Matter Plate의 기술이 필요합니다. 아래 트리에는 그것을 위한 화살표가 그려지지 않지만, 표에는 나와 있고 게임 안의 카드에도 이름이 나옵니다([Dark Matter와 Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)).

Skylab의 **연구** 보기에서는 기술이 아래 트리의 상자보다 더 많은 것을 알려 줍니다. 기술에 마우스를 올리면 연구 시간과 소모되는 과학이 적힌 카드가 열리고, 그 아래에 그 아이템이 **무엇이며 무엇을 하는지**가 표시됩니다. 종류와 계열 안에서의 등급(예: Impulse Thruster 네 개 중 세 번째), 설명, 격납고와 상점이 보여 주는 것과 같은 수치(레이저의 피해, 치명타 확률, 사거리, 실드의 실드 용량, 재충전 속도, 흡수율, 추진기의 속도 증가와 속도 배율, 로켓의 피해, 폭발 반경, 사거리, 드론 편대가 주는 것과 치르는 대가), 같은 계열의 등급별 작은 표, 그리고 연구 후 어셈블리가 제작에 요구하는 것(시간, 크레딧과 Thulium, 재료)이 나옵니다. 그래서 연구하기 전에 그 등급이 무엇을 주는지 볼 수 있습니다. 기술을 클릭하면 선택되고, 트리 옆의 카드가 같은 내용을 전부 **연구 시작** 버튼 아래에 보여 줍니다.

### 레벨별 탱크 {#the-tank-at-every-level}

<!-- research-tank:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| 레벨 | 탱크(과학) | 담을 수 있는 연구 시간 | … 부스트 시 | 전력 |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 43,200 | 12시간 | 6시간 | 25 |
| 2 | 54,000 | 15시간 | 7.5시간 | 28.7 |
| 3 | 67,500 | 18.8시간 | 9.4시간 | 33.1 |
| 4 | 84,375 | 23.4시간 | 11.7시간 | 38 |
| 5 | 105,469 | 29.3시간 | 14.6시간 | 43.7 |
| 6 | 131,836 | 36.6시간 | 18.3시간 | 50.3 |
| 7 | 164,795 | 45.8시간 | 22.9시간 | 57.8 |
| 8 | 205,994 | 57.2시간 | 28.6시간 | 66.5 |
| 9 | 257,492 | 71.5시간 | 35.8시간 | 76.5 |
| 10 | 321,865 | 89.4시간 | 44.7시간 | 87.9 |

<!-- research-tank:end -->

## 연료 {#fuel}

연구 센터에 자원을 넣으면 한 개씩 즉시 과학으로 바뀝니다. 얻기 힘든 자원일수록 더 많은 과학을 줍니다. 수치는 희귀도 표시가 아니라 얻기 어려운 정도를 따릅니다. 광석은 예외입니다. 한 개가 주는 과학은 수집기가 그것을 캐는 데 걸리는 초 수보다 많으므로, 레벨의 중간쯤에 있는 수집기의 한 시간분 광석이 연구 약 두 시간을 감당합니다. 광석은 [Skylab](/wiki/03-Mechanics/Skylab.md#resource-storage)의 자원 창고에서, 그 밖의 자원은 인벤토리에서 가져오며, 함선이 착륙해 있어야 합니다. Velkonite Reinforced Plate, Orvium Reinforced Plate, Dark Matter Plate, Dark Matter, 크레딧, Thulium은 태울 수 없지만 Reinforced Hull Plate는 태울 수 있습니다.

<!-- research-fuel:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| 자원 | 희귀도 | 가져오는 곳 | 1개당 과학 | 1시간에 필요한 수 |
| :--- | :--- | :--- | ---: | ---: |
| [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) | 일반 | 인벤토리 | 5 | 720 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | 일반 | 인벤토리 | 5 | 720 |
| [Daraxium](/wiki/06-Items/Resources.md#daraxium) | 일반 | 인벤토리 | 7 | 515 |
| [Nyxite](/wiki/06-Items/Resources.md#nyxite) | 일반 | 인벤토리 | 7 | 515 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | 일반 | 인벤토리 | 8 | 450 |
| [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) | 일반 | 인벤토리 | 33 | 110 |
| [Power Core](/wiki/06-Items/Resources.md#power-core) | 고급 | 인벤토리 | 100 | 36 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | 고급 | 자원 창고 | 210 | 18 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | 희귀 | 자원 창고 | 321 | 12 |
| [Ancient Control Unit](/wiki/06-Items/Resources.md#ancient-control-unit) | 희귀 | 인벤토리 | 650 | 6 |

마지막 열은 부스트 없이 연구 1시간을 돌리는 데 필요한 개수이며 올림한 값입니다. 부스트를 쓰면 2배가 필요합니다.

<!-- research-fuel:end -->

## Thulium 부스트 {#the-thulium-boost}

<!-- research-boost:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **5,000 Thulium**으로 부스트 하나를 삽니다. 연구 센터가 **24시간 동안 2배 빠르게** 연구합니다.
- 과학도 **2배 빠르게 타므로**, 부스트가 사는 것은 시간이지 연료가 아닙니다. 기술이 태우는 과학은 부스트가 있든 없든 같습니다.
- 부스트는 산 순간 시작되어 탱크에 연료가 있든 없든 시계대로 흘러가므로, 연구가 진행 중일 때 사세요. 아무것도 연구하지 않을 때는 센터가 거절합니다.
- 부스트는 쌓입니다. 다른 부스트가 진행 중일 때 하나 더 사면 그 끝이 24시간 늘어나며, 최대 72시간 앞까지 쌓을 수 있습니다. 부스트는 개별 연구가 아니라 내 연구 센터에 속합니다.

연구 처음부터 부스트를 걸었을 때 연구 시간이 어떻게 되는지:

| 연구 시간 | 부스트 시 | 전체에 필요한 부스트 | Thulium |
| :--- | :--- | ---: | ---: |
| 30분 | 15분 | 1 | 5,000 |
| 3시간 | 1시간 30분 | 1 | 5,000 |
| 6시간 | 3시간 | 1 | 5,000 |
| 10시간 | 5시간 | 1 | 5,000 |
| 1일 | 12시간 | 1 | 5,000 |
| 2일 | 1일 | 1 | 5,000 |

<!-- research-boost:end -->

## Dark Matter

기술 트리 맨 위의 기술에는 Dark Matter도 필요합니다. Dark Matter는 [블랙홀](/wiki/03-Mechanics/Black-Hole.md#dark-matter)에서 나오는데, 블랙홀에 닿은 N.I.K.E. 로켓이 얼마간 남기고 가며, 가끔 [Dormant 무리](/wiki/05-Swarms/Dormant-Swarm.md)의 Dormant Pulse에게서도 나옵니다.

<!-- research-dark-matter:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- 아래 표의 기술 16개 각각에 과학과는 별도로 **Dark Matter 10개**가 필요합니다. 시작 전에 연구 센터에 넣어 두세요(인벤토리에서, 함선이 착륙한 상태). 연구는 시작할 때 그것을 가져갑니다.
- **규칙:** 희귀도가 영웅 이상이면서 연구에 10시간 이상 걸리는 아이템. Dark Matter를 만드는 N.I.K.E.에는 결코 필요하지 않습니다.
- **드론 편대**는 이 규칙에서 제외됩니다. 모든 편대 연구는 강도에 따라 Dark Matter 5, 13 또는 20개를 요구합니다(표 참고).
- **연구를 취소하면** 그 연구를 위해 넣어 둔 Dark Matter는 센터로 돌아옵니다. 진행도와 이미 태운 과학은 돌아오지 않습니다.
- 전부 합치면 Dark Matter 349개가 필요합니다.

| 기술 | 희귀도 | 연구 시간 | Dark Matter |
| :--- | :--- | :--- | ---: |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | 영웅 | 10시간 | 10 |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | 영웅 | 10시간 | 10 |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | 영웅 | 10시간 | 10 |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | 영웅 | 10시간 | 10 |
| [Starfire-3](/wiki/06-Items/Lasers.md#lasers) | 신화 | 1일 | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | 신화 | 1일 | 10 |
| [Damage Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | 영웅 | 10시간 | 10 |
| [Crit Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | 영웅 | 10시간 | 10 |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | 영웅 | 1일 | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | 영웅 | 1일 | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | 신화 | 2일 | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | 신화 | 1일 | 10 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | 전설 | 1일 | 10 |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 영웅 | 1일 | 10 |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 영웅 | 1일 | 10 |
| [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 영웅 | 10시간 | 5 |
| [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 영웅 | 1일 | 13 |
| [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 영웅 | 10시간 | 5 |
| [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 신화 | 2일 | 20 |
| [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 영웅 | 10시간 | 5 |
| [Ballista Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 영웅 | 1일 | 13 |
| [Stiletto Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 신화 | 2일 | 20 |
| [Rampart Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 신화 | 2일 | 20 |
| [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 영웅 | 1일 | 13 |
| [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 영웅 | 10시간 | 5 |
| [Culler Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 영웅 | 1일 | 13 |
| [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 영웅 | 1일 | 13 |
| [Auger Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 영웅 | 1일 | 13 |
| [Cordon Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 영웅 | 1일 | 13 |
| [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 영웅 | 10시간 | 5 |
| [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | 영웅 | 1일 | 13 |
| [Penetration Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | 영웅 | 10시간 | 10 |

<!-- research-dark-matter:end -->

## 기술 트리 {#the-technology-tree}

각 상자는 기술 하나입니다. 그 기술로 만들 수 있게 되는 아이템이며, 이름 아래에 연구 시간(시계)이, Dark Matter가 필요한 곳에는 Dark Matter 배지가 표시됩니다. 화살표는 어떤 기술에서 그것을 필요로 하는 기술로 이어지며, 먼저 연구하는 쪽은 화살표가 시작되는 기술입니다. 화살표가 없는 상자는 바로 연구할 수 있습니다. 상자에 마우스를 올리면 연구 시간, 소모되는 과학, 연구 후 어셈블리가 그 아이템에 요구하는 것이 표시되고, 클릭하면 아이템 페이지가 열립니다. 트리는 게임 자체 데이터로 그려집니다. 트리 중 **방어**와 **공격·기동** 두 개에는 16종의 [드론 편대](/wiki/03-Mechanics/Formations.md)가 들어 있습니다.

<!-- research-tree:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

### 추진 장치와 속도 {#tree-propulsion}

```tree research
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines

Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```

### 실드와 방어 {#tree-shields}

```tree research
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cores

Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```

### 레이저와 탄약 {#tree-lasers}

```tree research
Quantum Laser 3 | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-3 | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser 3, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-3, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Damage Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Crit Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Damage Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Damage Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Crit Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Crit Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Penetration Amp I, 20 Daraxium, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Penetration Amp II, 1 Power Core, 30 Nyxite, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp IV | laser-amp, epic | craft 1200 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Penetration Amp III, 1 Power Core, 30 Cataclysite, 40 Quorvium, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-

Quantum Laser 3 => Starfire-3 => Helios Beam
Damage Amp II => Damage Amp III => Damage Amp IV
Crit Amp II => Crit Amp III => Crit Amp IV
Penetration Amp II => Penetration Amp III => Penetration Amp IV
```

### 부스터 {#tree-boosters}

```tree research
Laser Damage Booster 2 | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster 2 | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster 2 | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
```

### 드론 {#tree-drones}

```tree research
Master Drone | drone, rare | craft 40000 Thulium, 60 s | research 36000 s, 36000 science | 1 Slave Drone, 100 Ship Fragment | /wiki/06-Items/Drones.md#available-drones
```

### 함선 {#tree-ships}

```tree research
Paragon | ship, rare | craft 1500 Thulium, 900 s | research 21600 s, 21600 science | 120 Ship Fragment, 20 Reinforced Hull Plate, 5 Power Core | /wiki/02-Ships/Paragon.md
Ironclad | ship, epic | craft 10500 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit | /wiki/02-Ships/Ironclad.md
Storm | ship, epic | craft 15000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit | /wiki/02-Ships/Storm.md
Wraith | ship, mythical | craft 20000 Thulium, 900 s | research 172800 s, 172800 science, 10 Dark Matter | 300 Ship Fragment, 50 Reinforced Hull Plate, 15 Power Core, 3 Ancient Control Unit | /wiki/02-Ships/Wraith.md
```

### 자원 {#tree-resources}

```tree research
Dark Matter Plate | resource, mythical | craft 250 Thulium, 120 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Velkonite Reinforced Plate, 1 Orvium Reinforced Plate, 5 Dark Matter | /wiki/06-Items/Resources.md#dark-matter-plate
```

### 로켓 {#tree-rockets}

```tree research
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
```

### CPU {#tree-cpus}

```tree research
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 6 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 2 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Extras.md#base-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu

Extra Slots CPU I => Extra Slots CPU II => Extra Slots CPU III
Base CPU I => Base CPU II => Jump CPU
```

### 방어 {#tree-defence}

```tree research
Testudo Formation | formation, epic | craft 7500 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Adamant Formation | formation, epic | craft 9000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Rampart Formation | formation, mythical | craft 38500 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Sanctum Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Redoubt Formation | formation, epic | craft 21000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Cordon Formation | formation, epic | craft 21500 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations

Testudo Formation => Sanctum Formation => Rampart Formation
Adamant Formation => Redoubt Formation => Cordon Formation
```

### 공격·기동 {#tree-strike-mobility}

```tree research
Bodkin Formation | formation, epic | craft 21000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Asterism Formation | formation, epic | craft 7000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Gemini Formation | formation, mythical | craft 38000 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Ballista Formation | formation, epic | craft 24000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Stiletto Formation | formation, mythical | craft 46000 Thulium, 900 s | research 172800 s, 172800 science, 20 Dark Matter | 260 Ship Fragment, 26 Reinforced Hull Plate, 13 Power Core, 2 Ancient Control Unit, 14 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Shrike Formation | formation, epic | craft 8500 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Culler Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Auger Formation | formation, epic | craft 20500 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Centurion Formation | formation, epic | craft 8000 Thulium, 300 s | research 36000 s, 36000 science, 5 Dark Matter | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 4 Velkonite Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations
Gyre Formation | formation, epic | craft 20000 Thulium, 600 s | research 86400 s, 86400 science, 13 Dark Matter | 180 Ship Fragment, 18 Reinforced Hull Plate, 9 Power Core, 8 Velkonite Reinforced Plate, 3 Orvium Reinforced Plate | /wiki/03-Mechanics/Formations.md#the-sixteen-formations

Asterism Formation => Bodkin Formation => Ballista Formation
Gemini Formation => Stiletto Formation
Centurion Formation => Shrike Formation => Culler Formation
Gyre Formation => Auger Formation
```


<!-- research-tree:end -->

## 모든 기술 {#all-the-technologies}

<!-- research-technologies:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| 기술 | 먼저 필요한 기술 | 등급 | 연구 시간 | 과학 | Dark Matter |
| :--- | :--- | :--- | ---: | ---: | ---: |
| [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30분 | 1,800 | – |
| [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3시간 | 10,800 | – |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10시간 | 36,000 | 10 |
| [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30분 | 1,800 | – |
| [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3시간 | 10,800 | – |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10시간 | 36,000 | 10 |
| [Engine III](/wiki/06-Items/Propulsion.md#engines) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | B | 3시간 | 10,800 | – |
| [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30분 | 1,800 | – |
| [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3시간 | 10,800 | – |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10시간 | 36,000 | 10 |
| [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30분 | 1,800 | – |
| [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3시간 | 10,800 | – |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10시간 | 36,000 | 10 |
| [Heavy Shield Core](/wiki/06-Items/Shields.md#shield-cores) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | B | 3시간 | 10,800 | – |
| [Quantum Laser 3](/wiki/06-Items/Lasers.md#lasers) | – | B | 3시간 | 10,800 | – |
| [Starfire-3](/wiki/06-Items/Lasers.md#lasers) | [Quantum Laser 3](/wiki/06-Items/Lasers.md#lasers) | D | 1일 | 86,400 | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Starfire-3](/wiki/06-Items/Lasers.md#lasers) | D | 1일 | 86,400 | 10 |
| [Damage Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Damage Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10시간 | 36,000 | 10 |
| [Crit Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Crit Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10시간 | 36,000 | 10 |
| [Laser Damage Booster 2](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3시간 | 10,800 | – |
| [Shield Wall Booster 2](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3시간 | 10,800 | – |
| [Hull Plating Booster 2](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3시간 | 10,800 | – |
| [Master Drone](/wiki/06-Items/Drones.md#available-drones) | – | C | 10시간 | 36,000 | – |
| [Paragon](/wiki/02-Ships/Paragon.md) | – | B | 6시간 | 21,600 | – |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | – | D | 1일 | 86,400 | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | – | D | 1일 | 86,400 | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | – | D | 2일 | 172,800 | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | – | D | 1일 | 86,400 | 10 |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | B | 3시간 | 10,800 | – |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | D | 1일 | 86,400 | 10 |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | – | A | 30분 | 1,800 | – |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | C | 10시간 | 36,000 | – |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | D | 1일 | 86,400 | 10 |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | – | B | 3시간 | 10,800 | – |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | C | 10시간 | 36,000 | – |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | D | 1일 | 86,400 | 10 |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | – | B | 6시간 | 21,600 | – |
| [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10시간 | 36,000 | 5 |
| [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1일 | 86,400 | 13 |
| [Asterism Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10시간 | 36,000 | 5 |
| [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | D | 2일 | 172,800 | 20 |
| [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10시간 | 36,000 | 5 |
| [Ballista Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Bodkin Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1일 | 86,400 | 13 |
| [Stiletto Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Gemini Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 2일 | 172,800 | 20 |
| [Rampart Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 2일 | 172,800 | 20 |
| [Sanctum Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Testudo Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1일 | 86,400 | 13 |
| [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | C | 10시간 | 36,000 | 5 |
| [Culler Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Shrike Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1일 | 86,400 | 13 |
| [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Adamant Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1일 | 86,400 | 13 |
| [Auger Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1일 | 86,400 | 13 |
| [Cordon Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | [Redoubt Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | D | 1일 | 86,400 | 13 |
| [Centurion Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | C | 10시간 | 36,000 | 5 |
| [Gyre Formation](/wiki/03-Mechanics/Formations.md#the-sixteen-formations) | – | D | 1일 | 86,400 | 13 |
| [Damage Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30분 | 1,800 | – |
| [Damage Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Damage Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3시간 | 10,800 | – |
| [Crit Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30분 | 1,800 | – |
| [Crit Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Crit Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3시간 | 10,800 | – |
| [Penetration Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | A | 30분 | 1,800 | – |
| [Penetration Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Penetration Amp II](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | B | 3시간 | 10,800 | – |
| [Penetration Amp IV](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Penetration Amp III](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | C | 10시간 | 36,000 | 10 |

연구 시간별 등급:

| 등급 | 연구 시간 | 기술 수 | 차례로 연구한 합계 | 과학 | Dark Matter |
| :--- | :--- | ---: | ---: | ---: | ---: |
| A | 30분 | 8 | 4시간 | 14,400 | 0 |
| B | 3시간~6시간 | 17 | 2일 9시간 | 205,200 | 0 |
| C | 10시간 | 15 | 6일 6시간 | 540,000 | 95 |
| D | 1일~2일 | 20 | 24일 | 2,073,600 | 254 |
| 전체 |  | 60 | 32일 19시간 | 2,833,200 | 349 |

하나씩 차례로 연구하면 트리 전체에 32일 19시간이 걸립니다. 부스트를 계속 켜 두면 16일 9시간 30분이 걸리며, 부스트 17개와 Thulium 85,000이 듭니다. 과학은 같습니다.

<!-- research-technologies:end -->

## CPU {#the-cpus}

새 CPU도 여기서 연구한 다음 어셈블리에서 제작합니다. 같은 표와 설명이 [부가 장비](/wiki/06-Items/Extras.md#research-cpus) 페이지에도 있습니다.

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | 연구 시간 | 먼저 필요한 기술 | 제작에 필요한 Thulium | 제작 시간 |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30분 | – | 12,000 | 5분 |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10시간 | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30,000 | 10분 |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1일 | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75,000 | 15분 |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3시간 | – | 8,000 | 5분 |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10시간 | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | 20,000 | 10분 |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1일 | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40,000 | 15분 |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6시간 | – | 15,000 | 10분 |

어느 것도 상점에서 팔지 않습니다. 기술을 연구한 뒤 어셈블리에서 CPU를 제작합니다. 트리에서 CPU에 마우스를 올리면 어셈블리가 무엇을 요구하는지 볼 수 있습니다.

### Extra Slots CPUs

- **기능.** Extra Slots CPU I·II·III은 모든 함선의 부가 슬롯을 3개, 5개, 7개 늘려 줍니다. 함선이 원래 3개를 가졌다면 총 6개, 8개, 10개이고, 2개를 가졌다면 5개, 7개, 9개입니다. 상위 CPU는 하위 CPU를 대체합니다. II가 I에 더해지지는 않습니다.
- **장착이 아니라 설치.** Extra Slots CPU는 아이템이 아닙니다. 어셈블리에서 받으면 Skylab에 설치되어 두 구성 모두의 모든 함선에 적용되고, 슬롯을 차지하지 않습니다. 초기화 후에도 남습니다.
- **순서대로.** 하나씩 차례로 제작하세요. II는 I이 설치된 뒤에, III은 II가 설치된 뒤에만 제작할 수 있으며, 그때까지는 어셈블리가 먼저 설치할 것을 알려 줍니다. 셋을 합치면 Thulium 117,000이 듭니다: 12,000, 30,000, 75,000.

### Jump CPU

- **기능.** 함선을 내 월드의 어느 기업 섹터(내 기업의 섹터든 다른 기업의 섹터든, 기지 섹터도 포함. `M`, `T`, `G`의 섹터 1~4)로든 점프시키며, 1회당 **Thulium 500**이 듭니다. 사용 횟수 제한은 없고 Thulium만 내면 됩니다. 위험 섹터(`DS`)나 중립 섹터(`N`)로는 가지 못합니다.
- **점프.** JMP 슬롯을 누르고 항성계 지도에서 섹터를 골라 확정하면, 함선이 5초 동안 충전한 뒤 그 섹터의 게이트에 도착하며, 일반 게이트 점프 후와 같은 보호를 받습니다. 도착 후 CPU는 30초 동안 재사용 대기에 들어갑니다.
- **전투 중에는 불가.** 발사하거나 피격당한 뒤 10초 이내에는 시작할 수 없고, 충전 중 발사하거나 피격당하면 점프가 취소됩니다. 이때는 아무것도 지불하지 않습니다. 은폐 중에는 점프할 수 없습니다.
- **중립 섹터에서는 불가:** 중립 섹터에 있거나 기업에 소속되지 않은 파일럿은 쓸 수 없습니다.
- 전투 중이 아니면 위험 섹터에서 떠날 수 있습니다.

### Base CPUs

- **기능.** 함선을 소속 기업의 기지에 있는 정거장 주변 안전 지대(`M-1`, `T-1`, `G-1`, Mission Control이 있는 섹터)로 순간이동시킵니다. Thulium은 들지 않습니다. 퀵슬롯의 BSE 슬롯에서 시작합니다.
- **전투 중에는 불가.** 충전은 10초이며 둘 다 같습니다. 발사하거나 피격당한 뒤 10초 이내, 은폐 중, 이미 기지의 안전 지대 안에 있을 때는 시작할 수 없고, 충전 중 발사하거나 피격당하면 취소됩니다.

| CPU | 사용 횟수 | 재사용 대기 |
| :--- | ---: | ---: |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 10 | 10분 |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 25 | 5분 |

- **소모형, 재충전 없음.** 사용할 때마다 CPU의 사용 횟수가 하나씩 줄고, 횟수가 다 떨어진 CPU는 사라집니다. 새로 제작하세요. 둘 다 장착했다면 상위인 II부터 사용됩니다.

### Auto-Repair CPU

- **기능.** 직접 출격시킬 수 있는 상황이 될 때마다, 부가 슬롯에 장착한 Repair Drone을 자동으로 출격시킵니다. 선체가 가득 차지 않았고, 드론이 이미 나와 있지 않으며, 마지막 피격 후 10초가 지났을 때입니다. 선체 기준치를 설정할 필요는 없습니다.
- 전용 부가 슬롯을 하나 차지하며, 같은 구성의 부가 슬롯에 Repair Drone이 없으면 아무것도 하지 않습니다. 능력 슬롯에 있는 Repair Drone은 내보내지 않습니다(그것은 Emergency Repair 버튼입니다).
- **드론을 직접 멈추면** 선체가 다시 가득 차거나 직접 드론을 출격시킬 때까지 CPU는 건드리지 않습니다.


<!-- research-cpus:end -->
