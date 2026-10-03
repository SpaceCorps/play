<!-- wiki-i18n source: c893fea350141846 -->
<!-- wiki-i18n title: 자원 -->
# 자원 {#resources}

여기서 **자원**은 게임이 주고, 대신 모아 주고, 다시 요구하는 모든 것을 말합니다. **재료**(제작과 단련에 쓰는 자원 종류의 아이템)와 두 가지 **화폐**, 즉 크레딧과 Thulium입니다. 이 페이지는 각각이 무엇인지, 어떻게 얻는지, 어디에 쓰는지, 어떻게 가장 효율적으로 모으는지를 설명합니다.

- **재료**는 격납고 인벤토리에 있는 아이템입니다. 외계인에게서 [화물 상자](/wiki/03-Mechanics/Cargo.md)로 드롭되거나, 미션 보상으로 주어지거나, [Skylab](/wiki/03-Mechanics/Skylab.md)에서 만들어집니다. 어셈블리 제작법, [대장간](/wiki/06-Items/Forge.md), Skylab 건설에 소모됩니다.
- **화폐**는 계정에 저장됩니다. 모든 외계인이 지급하며, 미션과 Skylab의 농장도 지급합니다.
- **이 페이지에 없는 것**: 탄약([레이저](/wiki/06-Items/Lasers.md), [로켓](/wiki/06-Items/Rockets.md)), 장비, 부스터는 각자의 페이지가 있습니다. 경험치와 명예는 화폐가 아니라 점수이며, 아래 외계인 표에 있습니다.

수치에 “섹터”라고 되어 있다면 소속 기업 맵의 섹터를 가리킵니다(1은 기지 바로 옆, 4는 경계입니다). 수치는 게임의 데이터를 그대로 가져온 것이므로, 드롭이나 제작법, 비율이 바뀌면 함께 바뀝니다.

<!-- resources:begin -->
<!-- Generated from the seeds and configs by scripts/resources-wiki.sh: don't edit by hand. -->

이 페이지의 모든 획득량은 **처치 1회당 평균값**입니다. 각 드롭의 확률에 수량의 중간값을 곱해 모두 더한 값입니다. 시간이 아니라 처치 횟수를 기준으로 하므로, Crystalys는 Seeker보다 처치하는 데 훨씬 오래 걸립니다. 상자가 내 것이고(Resource Magnet 없음) 행운이 없다고(Loot Luck 부스터도, 시즌 상점의 Luck Boost도 없음. 둘 다 모든 드롭의 확률을 높이며, Luck Boost는 최대 10포인트까지 높입니다) 가정하며, 모든 드롭은 따로따로 굴립니다. 크레딧과 Thulium 수치는 Alpha 월드 기준이며, 다른 월드는 더 많이 줍니다([화폐](/wiki/06-Items/Resources.md#currencies) 참고).

## 재료 한눈에 보기 {#the-materials-at-a-glance}

| 재료 | 희귀도 | 획득처 | 쓰이는 곳 |
| :--- | :--- | :--- | :--- |
| [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) | 일반 | Crystalys, Goombah, Bulwark, Phantasm, Seeker, 스페셜 미션 | Master Drone, Quantum Laser 3, Starfire-3, Paragon, Wraith, Damage Amp II, Shield Wall II, Hull Plating II, Impulse Thruster IV, Ironclad, Engine III, Impulse Thruster III, Impulse Thruster II, Momentum Thruster II, Momentum Thruster III, Momentum Thruster IV, N.U.K.E., N.I.K.E., 대장간, Skylab 건설 |
| [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) | 일반 | Goombah, Bulwark, 스페셜 미션 | Starfire-3, Helios Beam, Paragon, Wraith, Absorption Shield Cell IV, Ironclad, Heavy Shield Core, Absorption Shield Cell II, Absorption Shield Cell III, Capacity Shield Cell II, Capacity Shield Cell III, Capacity Shield Cell IV, N.U.K.E., N.I.K.E., 대장간 |
| [Power Core](/wiki/06-Items/Resources.md#power-core) | 고급 | Crystalys, Goombah, 스페셜 미션 | Helios Beam, Paragon, Wraith, Nova Amp, Apex Amp, Impulse Thruster IV, Ironclad, Engine III, Impulse Thruster III, Impulse Thruster II, Momentum Thruster II, Momentum Thruster III, Momentum Thruster IV, N.U.K.E., 대장간 |
| [Ancient Control Unit](/wiki/06-Items/Resources.md#ancient-control-unit) | 희귀 | Crystalys, 스페셜 미션 | Wraith, Ironclad |
| [Daraxium](/wiki/06-Items/Resources.md#daraxium) | 일반 | Phantasm, Seeker | 대장간 |
| [Nyxite](/wiki/06-Items/Resources.md#nyxite) | 일반 | Phantasm, Bulwark | 대장간 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | 일반 | Crystalys, Goombah, Bulwark | Helios Beam, Nova Amp, Apex Amp, Absorption Shield Cell IV, Heavy Shield Core, Absorption Shield Cell II, Absorption Shield Cell III, Capacity Shield Cell II, Capacity Shield Cell III, Capacity Shield Cell IV, N.U.K.E., N.I.K.E., 대장간 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | 일반 | Crystalys, Goombah | 대장간 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | 고급 | Skylab 수집기 | Skylab 단조소 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | 희귀 | Skylab 수집기 | Skylab 단조소 |
| [Velkonite Reinforced Plate](/wiki/06-Items/Resources.md#velkonite-reinforced-plate) | 희귀 | Skylab 단조소 | Quantum Laser 3, Starfire-3, Nova Amp, Apex Amp, Absorption Shield Cell IV, Impulse Thruster IV, Dark Matter Plate, Heavy Shield Core, Engine III, Impulse Thruster III, Absorption Shield Cell II, Absorption Shield Cell III, Capacity Shield Cell II, Capacity Shield Cell III, Capacity Shield Cell IV, Impulse Thruster II, Momentum Thruster II, Momentum Thruster III, Momentum Thruster IV |
| [Orvium Reinforced Plate](/wiki/06-Items/Resources.md#orvium-reinforced-plate) | 영웅 | Skylab 단조소 | Helios Beam, Dark Matter Plate |
| [Dark Matter](/wiki/06-Items/Resources.md#dark-matter) | 영웅 | 블랙홀(삼켜진 N.I.K.E.) | Dark Matter Plate |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | 신화 | 어셈블리 | 대장간 |

## 재료 {#materials}

### Ship Fragment {#ship-fragment}

*일반 자원.* NPC가 드롭합니다. 더 강한 함선을 만드는 데 필요합니다.

**얻는 방법**

| 외계인 | 섹터 | 드롭 | 처치당 평균 |
| :--- | :---: | :--- | --: |
| [Crystalys](/wiki/04-Aliens/Crystalys.md) | 4 | 100% 확률로 5개; 50% 확률로 1개; 25% 확률로 2개 | 6 |
| [Goombah](/wiki/04-Aliens/Goombah.md) | 3, 4 | 100% 확률로 3개; 25% 확률로 1개 | 3.25 |
| [Bulwark](/wiki/04-Aliens/Bulwark.md) | 3, 4 | 100% 확률로 2개 | 2 |
| [Phantasm](/wiki/04-Aliens/Phantasm.md) | 2, 3 | 100% 확률로 1개 | 1 |
| [Seeker](/wiki/04-Aliens/Seeker.md) | 1, 2 | 20% 확률로 1개 | 0.2 |

- **미션**: Phantasm 섬멸(레벨 2 스페셜) 5; 밤의 장막(레벨 3 스페셜) 10; Bulwark 분쇄자(레벨 4 스페셜) 10; 강철의 파도(레벨 5 스페셜) 15; 거상(레벨 6 스페셜) 15; Goombah 포위전(레벨 7 스페셜) 20; 전선 지휘(레벨 8 스페셜) 25.
- **그 밖에**: 상점에서 판매하지 않습니다.

**쓰이는 곳**

- [Master Drone](/wiki/06-Items/Drones.md): **100** (함께 필요: Slave Drone 1개, Thulium 40,000)
- [Quantum Laser 3](/wiki/06-Items/Lasers.md): **10** (함께 필요: Velkonite Reinforced Plate 2개, Thulium 1,500)
- [Starfire-3](/wiki/06-Items/Lasers.md): **15** (함께 필요: Quantum Laser 3 1개, Reinforced Hull Plate 1개, Velkonite Reinforced Plate 8개, 크레딧 100,000, Thulium 1,500)
- [Paragon](/wiki/02-Ships/Paragon.md): **120** (함께 필요: Power Core 5개, Reinforced Hull Plate 20개, Thulium 1,500)
- [Wraith](/wiki/02-Ships/Wraith.md): **300** (함께 필요: Ancient Control Unit 3개, Power Core 15개, Reinforced Hull Plate 50개, Thulium 20,000)
- [Damage Amp II](/wiki/06-Items/Boosters.md): **5** (함께 필요: Thulium 20,000)
- [Shield Wall II](/wiki/06-Items/Boosters.md): **5** (함께 필요: Thulium 15,000)
- [Hull Plating II](/wiki/06-Items/Boosters.md): **5** (함께 필요: Thulium 15,000)
- [Impulse Thruster IV](/wiki/06-Items/Propulsion.md): **60** (함께 필요: Impulse Thruster III 1개, Power Core 3개, Velkonite Reinforced Plate 6개, Thulium 2,000)
- [Ironclad](/wiki/02-Ships/Ironclad.md): **200** (함께 필요: Ancient Control Unit 1개, Power Core 10개, Reinforced Hull Plate 35개, Thulium 10,500)
- [Engine III](/wiki/06-Items/Propulsion.md): **60** (함께 필요: Engine II 1개, Power Core 3개, Velkonite Reinforced Plate 6개, Thulium 2,000)
- [Impulse Thruster III](/wiki/06-Items/Propulsion.md): **30** (함께 필요: Impulse Thruster II 1개, Power Core 2개, Velkonite Reinforced Plate 4개, Thulium 1,500)
- [Impulse Thruster II](/wiki/06-Items/Propulsion.md): **10** (함께 필요: Impulse Thruster I 1개, Power Core 1개, Velkonite Reinforced Plate 2개, Thulium 1,000)
- [Momentum Thruster II](/wiki/06-Items/Propulsion.md): **10** (함께 필요: Momentum Thruster I 1개, Power Core 1개, Velkonite Reinforced Plate 2개, Thulium 1,000)
- [Momentum Thruster III](/wiki/06-Items/Propulsion.md): **30** (함께 필요: Momentum Thruster II 1개, Power Core 2개, Velkonite Reinforced Plate 4개, Thulium 1,500)
- [Momentum Thruster IV](/wiki/06-Items/Propulsion.md): **60** (함께 필요: Momentum Thruster III 1개, Power Core 3개, Velkonite Reinforced Plate 6개, Thulium 2,000)
- [N.U.K.E.](/wiki/06-Items/Rockets.md): **40** (함께 필요: Cataclysite 80개, Power Core 4개, Reinforced Hull Plate 10개, Scatter III 6개, 크레딧 150,000, Thulium 3,000)
- [N.I.K.E.](/wiki/06-Items/Rockets.md) (1회 5개 제작): **20** (함께 필요: Cataclysite 40개, Reinforced Hull Plate 4개, 크레딧 100,000, Thulium 1,500)
- [대장간](/wiki/06-Items/Forge.md), 표준 → 오염된: **5** (함께 필요: Daraxium 15개, 크레딧 10,000; 성공 확률 100%)
- [대장간](/wiki/06-Items/Forge.md), 오염된 → 신성한: **30** (함께 필요: Nyxite 45개, 크레딧 50,000; 성공 확률 90%)
- [Skylab](/wiki/03-Mechanics/Skylab.md) 모듈 건설: 단조소, Orvium 수집기, 자원 창고, Velkonite 수집기 각각 **10**개(수송 보관함이 아니라 인벤토리에서 가져감)

실패한 대장간 단계는 재료의 50%를 돌려주며, 소수점 이하는 내림합니다.

**모으는 방법**: [Crystalys](/wiki/04-Aliens/Crystalys.md)(섹터 4) 처치, 처치당 평균 6개. 가장 가까운 획득처: 섹터 1의 [Seeker](/wiki/04-Aliens/Seeker.md), 처치당 0.2개.

### Reinforced Hull Plate {#reinforced-hull-plate}

*일반 자원.* NPC가 드롭합니다. 더 강한 함선을 만드는 데 필요합니다.

**얻는 방법**

| 외계인 | 섹터 | 드롭 | 처치당 평균 |
| :--- | :---: | :--- | --: |
| [Goombah](/wiki/04-Aliens/Goombah.md) | 3, 4 | 60% 확률로 1개 | 0.6 |
| [Bulwark](/wiki/04-Aliens/Bulwark.md) | 3, 4 | 30% 확률로 1개 | 0.3 |

- **미션**: Bulwark 분쇄자(레벨 4 스페셜) 2; 강철의 파도(레벨 5 스페셜) 3; 거상(레벨 6 스페셜) 3; Goombah 포위전(레벨 7 스페셜) 5.
- **그 밖에**: 상점에서 판매하지 않습니다.

**쓰이는 곳**

- [Starfire-3](/wiki/06-Items/Lasers.md): **1** (함께 필요: Quantum Laser 3 1개, Ship Fragment 15개, Velkonite Reinforced Plate 8개, 크레딧 100,000, Thulium 1,500)
- [Helios Beam](/wiki/06-Items/Lasers.md): **4** (함께 필요: Cataclysite 50개, Orvium Reinforced Plate 18개, Power Core 2개, Starfire-3 1개, Thulium 2,000)
- [Paragon](/wiki/02-Ships/Paragon.md): **20** (함께 필요: Power Core 5개, Ship Fragment 120개, Thulium 1,500)
- [Wraith](/wiki/02-Ships/Wraith.md): **50** (함께 필요: Ancient Control Unit 3개, Power Core 15개, Ship Fragment 300개, Thulium 20,000)
- [Absorption Shield Cell IV](/wiki/06-Items/Shields.md): **8** (함께 필요: Absorption Shield Cell III 1개, Cataclysite 20개, Velkonite Reinforced Plate 6개, Thulium 2,500)
- [Ironclad](/wiki/02-Ships/Ironclad.md): **35** (함께 필요: Ancient Control Unit 1개, Power Core 10개, Ship Fragment 200개, Thulium 10,500)
- [Heavy Shield Core](/wiki/06-Items/Shields.md): **8** (함께 필요: Basic Shield Core 1개, Cataclysite 20개, Velkonite Reinforced Plate 6개, Thulium 2,000)
- [Absorption Shield Cell II](/wiki/06-Items/Shields.md): **4** (함께 필요: Absorption Shield Cell I 1개, Cataclysite 10개, Velkonite Reinforced Plate 2개, Thulium 1,000)
- [Absorption Shield Cell III](/wiki/06-Items/Shields.md): **6** (함께 필요: Absorption Shield Cell II 1개, Cataclysite 15개, Velkonite Reinforced Plate 4개, Thulium 1,500)
- [Capacity Shield Cell II](/wiki/06-Items/Shields.md): **4** (함께 필요: Capacity Shield Cell I 1개, Cataclysite 10개, Velkonite Reinforced Plate 2개, Thulium 1,000)
- [Capacity Shield Cell III](/wiki/06-Items/Shields.md): **6** (함께 필요: Capacity Shield Cell II 1개, Cataclysite 15개, Velkonite Reinforced Plate 4개, Thulium 1,500)
- [Capacity Shield Cell IV](/wiki/06-Items/Shields.md): **8** (함께 필요: Capacity Shield Cell III 1개, Cataclysite 20개, Velkonite Reinforced Plate 6개, Thulium 2,500)
- [N.U.K.E.](/wiki/06-Items/Rockets.md): **10** (함께 필요: Cataclysite 80개, Power Core 4개, Scatter III 6개, Ship Fragment 40개, 크레딧 150,000, Thulium 3,000)
- [N.I.K.E.](/wiki/06-Items/Rockets.md) (1회 5개 제작): **4** (함께 필요: Cataclysite 40개, Ship Fragment 20개, 크레딧 100,000, Thulium 1,500)
- [대장간](/wiki/06-Items/Forge.md), 신성한 → 파열하는: **20** (함께 필요: Cataclysite 120개, Dark Matter Plate 2개, 크레딧 200,000; 성공 확률 75%)

실패한 대장간 단계는 재료의 50%를 돌려주며, 소수점 이하는 내림합니다.

**모으는 방법**: [Goombah](/wiki/04-Aliens/Goombah.md)(섹터 3, 4) 처치, 처치당 평균 0.6개.

### Power Core {#power-core}

*고급 자원.* NPC가 드롭합니다. 더 강한 함선, 레이저, 실드, 속도, 하이브리드 발전기를 만드는 데 필요합니다.

**얻는 방법**

| 외계인 | 섹터 | 드롭 | 처치당 평균 |
| :--- | :---: | :--- | --: |
| [Crystalys](/wiki/04-Aliens/Crystalys.md) | 4 | 50% 확률로 1개 | 0.5 |
| [Goombah](/wiki/04-Aliens/Goombah.md) | 3, 4 | 25% 확률로 1개 | 0.25 |

- **미션**: 강철의 파도(레벨 5 스페셜) 1; 거상(레벨 6 스페셜) 1; Goombah 포위전(레벨 7 스페셜) 2; 전선 지휘(레벨 8 스페셜) 1.
- **그 밖에**: 상점에서 판매하지 않습니다.

**쓰이는 곳**

- [Helios Beam](/wiki/06-Items/Lasers.md): **2** (함께 필요: Cataclysite 50개, Orvium Reinforced Plate 18개, Reinforced Hull Plate 4개, Starfire-3 1개, Thulium 2,000)
- [Paragon](/wiki/02-Ships/Paragon.md): **5** (함께 필요: Reinforced Hull Plate 20개, Ship Fragment 120개, Thulium 1,500)
- [Wraith](/wiki/02-Ships/Wraith.md): **15** (함께 필요: Ancient Control Unit 3개, Reinforced Hull Plate 50개, Ship Fragment 300개, Thulium 20,000)
- [Nova Amp](/wiki/06-Items/Lasers.md): **1** (함께 필요: Cataclysite 30개, Pulse Amp 1개, Velkonite Reinforced Plate 3개, Thulium 1,200)
- [Apex Amp](/wiki/06-Items/Lasers.md): **1** (함께 필요: Cataclysite 30개, Prism Amp 1개, Velkonite Reinforced Plate 3개, Thulium 1,200)
- [Impulse Thruster IV](/wiki/06-Items/Propulsion.md): **3** (함께 필요: Impulse Thruster III 1개, Ship Fragment 60개, Velkonite Reinforced Plate 6개, Thulium 2,000)
- [Ironclad](/wiki/02-Ships/Ironclad.md): **10** (함께 필요: Ancient Control Unit 1개, Reinforced Hull Plate 35개, Ship Fragment 200개, Thulium 10,500)
- [Engine III](/wiki/06-Items/Propulsion.md): **3** (함께 필요: Engine II 1개, Ship Fragment 60개, Velkonite Reinforced Plate 6개, Thulium 2,000)
- [Impulse Thruster III](/wiki/06-Items/Propulsion.md): **2** (함께 필요: Impulse Thruster II 1개, Ship Fragment 30개, Velkonite Reinforced Plate 4개, Thulium 1,500)
- [Impulse Thruster II](/wiki/06-Items/Propulsion.md): **1** (함께 필요: Impulse Thruster I 1개, Ship Fragment 10개, Velkonite Reinforced Plate 2개, Thulium 1,000)
- [Momentum Thruster II](/wiki/06-Items/Propulsion.md): **1** (함께 필요: Momentum Thruster I 1개, Ship Fragment 10개, Velkonite Reinforced Plate 2개, Thulium 1,000)
- [Momentum Thruster III](/wiki/06-Items/Propulsion.md): **2** (함께 필요: Momentum Thruster II 1개, Ship Fragment 30개, Velkonite Reinforced Plate 4개, Thulium 1,500)
- [Momentum Thruster IV](/wiki/06-Items/Propulsion.md): **3** (함께 필요: Momentum Thruster III 1개, Ship Fragment 60개, Velkonite Reinforced Plate 6개, Thulium 2,000)
- [N.U.K.E.](/wiki/06-Items/Rockets.md): **4** (함께 필요: Cataclysite 80개, Reinforced Hull Plate 10개, Scatter III 6개, Ship Fragment 40개, 크레딧 150,000, Thulium 3,000)
- [대장간](/wiki/06-Items/Forge.md), 파열하는 → 영원한: **8** (함께 필요: Quorvium 240개, Dark Matter Plate 2개, 크레딧 500,000, Thulium 2,000; 성공 확률 60%)

실패한 대장간 단계는 재료의 50%를 돌려주며, 소수점 이하는 내림합니다.

**모으는 방법**: [Crystalys](/wiki/04-Aliens/Crystalys.md)(섹터 4) 처치, 처치당 평균 0.5개. 가장 가까운 획득처: 섹터 3의 [Goombah](/wiki/04-Aliens/Goombah.md), 처치당 0.25개.

### Ancient Control Unit {#ancient-control-unit}

*희귀 자원.* NPC가 드롭합니다. 더 강한 함선과 레이저를 만드는 데 필요합니다.

**얻는 방법**

| 외계인 | 섹터 | 드롭 | 처치당 평균 |
| :--- | :---: | :--- | --: |
| [Crystalys](/wiki/04-Aliens/Crystalys.md) | 4 | 20% 확률로 1개 | 0.2 |

- **미션**: 전선 지휘(레벨 8 스페셜) 1.
- **그 밖에**: 상점에서 판매하지 않습니다.

**쓰이는 곳**

- [Wraith](/wiki/02-Ships/Wraith.md): **3** (함께 필요: Power Core 15개, Reinforced Hull Plate 50개, Ship Fragment 300개, Thulium 20,000)
- [Ironclad](/wiki/02-Ships/Ironclad.md): **1** (함께 필요: Power Core 10개, Reinforced Hull Plate 35개, Ship Fragment 200개, Thulium 10,500)

**모으는 방법**: [Crystalys](/wiki/04-Aliens/Crystalys.md)(섹터 4) 처치, 처치당 평균 0.2개.

### Daraxium {#daraxium}

*일반 자원.* NPC가 드롭합니다. 대장간에서 장비를 오염된 등급으로 올리는 데 쓰입니다.

**얻는 방법**

| 외계인 | 섹터 | 드롭 | 처치당 평균 |
| :--- | :---: | :--- | --: |
| [Phantasm](/wiki/04-Aliens/Phantasm.md) | 2, 3 | 60% 확률로 1~2개 | 0.9 |
| [Seeker](/wiki/04-Aliens/Seeker.md) | 1, 2 | 50% 확률로 1~2개 | 0.75 |

- **그 밖에**: 상점에서 판매하지 않습니다.

**쓰이는 곳**

- [대장간](/wiki/06-Items/Forge.md), 표준 → 오염된: **15** (함께 필요: Ship Fragment 5개, 크레딧 10,000; 성공 확률 100%)

실패한 대장간 단계는 재료의 50%를 돌려주며, 소수점 이하는 내림합니다.

**모으는 방법**: [Phantasm](/wiki/04-Aliens/Phantasm.md)(섹터 2, 3) 처치, 처치당 평균 0.9개. 가장 가까운 획득처: 섹터 1의 [Seeker](/wiki/04-Aliens/Seeker.md), 처치당 0.75개.

### Nyxite {#nyxite}

*일반 자원.* NPC가 드롭합니다. 대장간에서 장비를 신성한 등급으로 올리는 데 쓰입니다.

**얻는 방법**

| 외계인 | 섹터 | 드롭 | 처치당 평균 |
| :--- | :---: | :--- | --: |
| [Phantasm](/wiki/04-Aliens/Phantasm.md) | 2, 3 | 60% 확률로 1~2개 | 0.9 |
| [Bulwark](/wiki/04-Aliens/Bulwark.md) | 3, 4 | 40% 확률로 1~2개 | 0.6 |

- **그 밖에**: 상점에서 판매하지 않습니다.

**쓰이는 곳**

- [대장간](/wiki/06-Items/Forge.md), 오염된 → 신성한: **45** (함께 필요: Ship Fragment 30개, 크레딧 50,000; 성공 확률 90%)

실패한 대장간 단계는 재료의 50%를 돌려주며, 소수점 이하는 내림합니다.

**모으는 방법**: [Phantasm](/wiki/04-Aliens/Phantasm.md)(섹터 2, 3) 처치, 처치당 평균 0.9개.

### Cataclysite {#cataclysite}

*일반 자원.* NPC가 드롭합니다. 가장 강한 레이저를 만들고, 대장간에서 장비를 파열하는 등급으로 올리는 데 쓰입니다.

**얻는 방법**

| 외계인 | 섹터 | 드롭 | 처치당 평균 |
| :--- | :---: | :--- | --: |
| [Crystalys](/wiki/04-Aliens/Crystalys.md) | 4 | 100% 확률로 8개 | 8 |
| [Goombah](/wiki/04-Aliens/Goombah.md) | 3, 4 | 100% 확률로 4개 | 4 |
| [Bulwark](/wiki/04-Aliens/Bulwark.md) | 3, 4 | 100% 확률로 2개 | 2 |

- **그 밖에**: 상점에서 판매하지 않습니다.

**쓰이는 곳**

- [Helios Beam](/wiki/06-Items/Lasers.md): **50** (함께 필요: Orvium Reinforced Plate 18개, Power Core 2개, Reinforced Hull Plate 4개, Starfire-3 1개, Thulium 2,000)
- [Nova Amp](/wiki/06-Items/Lasers.md): **30** (함께 필요: Power Core 1개, Pulse Amp 1개, Velkonite Reinforced Plate 3개, Thulium 1,200)
- [Apex Amp](/wiki/06-Items/Lasers.md): **30** (함께 필요: Power Core 1개, Prism Amp 1개, Velkonite Reinforced Plate 3개, Thulium 1,200)
- [Absorption Shield Cell IV](/wiki/06-Items/Shields.md): **20** (함께 필요: Absorption Shield Cell III 1개, Reinforced Hull Plate 8개, Velkonite Reinforced Plate 6개, Thulium 2,500)
- [Heavy Shield Core](/wiki/06-Items/Shields.md): **20** (함께 필요: Basic Shield Core 1개, Reinforced Hull Plate 8개, Velkonite Reinforced Plate 6개, Thulium 2,000)
- [Absorption Shield Cell II](/wiki/06-Items/Shields.md): **10** (함께 필요: Absorption Shield Cell I 1개, Reinforced Hull Plate 4개, Velkonite Reinforced Plate 2개, Thulium 1,000)
- [Absorption Shield Cell III](/wiki/06-Items/Shields.md): **15** (함께 필요: Absorption Shield Cell II 1개, Reinforced Hull Plate 6개, Velkonite Reinforced Plate 4개, Thulium 1,500)
- [Capacity Shield Cell II](/wiki/06-Items/Shields.md): **10** (함께 필요: Capacity Shield Cell I 1개, Reinforced Hull Plate 4개, Velkonite Reinforced Plate 2개, Thulium 1,000)
- [Capacity Shield Cell III](/wiki/06-Items/Shields.md): **15** (함께 필요: Capacity Shield Cell II 1개, Reinforced Hull Plate 6개, Velkonite Reinforced Plate 4개, Thulium 1,500)
- [Capacity Shield Cell IV](/wiki/06-Items/Shields.md): **20** (함께 필요: Capacity Shield Cell III 1개, Reinforced Hull Plate 8개, Velkonite Reinforced Plate 6개, Thulium 2,500)
- [N.U.K.E.](/wiki/06-Items/Rockets.md): **80** (함께 필요: Power Core 4개, Reinforced Hull Plate 10개, Scatter III 6개, Ship Fragment 40개, 크레딧 150,000, Thulium 3,000)
- [N.I.K.E.](/wiki/06-Items/Rockets.md) (1회 5개 제작): **40** (함께 필요: Reinforced Hull Plate 4개, Ship Fragment 20개, 크레딧 100,000, Thulium 1,500)
- [대장간](/wiki/06-Items/Forge.md), 신성한 → 파열하는: **120** (함께 필요: Reinforced Hull Plate 20개, Dark Matter Plate 2개, 크레딧 200,000; 성공 확률 75%)

실패한 대장간 단계는 재료의 50%를 돌려주며, 소수점 이하는 내림합니다.

**모으는 방법**: [Crystalys](/wiki/04-Aliens/Crystalys.md)(섹터 4) 처치, 처치당 평균 8개. 가장 가까운 획득처: 섹터 3의 [Goombah](/wiki/04-Aliens/Goombah.md), 처치당 4개.

### Quorvium {#quorvium}

*일반 자원.* NPC가 드롭합니다. 대장간에서 장비를 영원한 등급으로 올리는 데 쓰입니다.

**얻는 방법**

| 외계인 | 섹터 | 드롭 | 처치당 평균 |
| :--- | :---: | :--- | --: |
| [Crystalys](/wiki/04-Aliens/Crystalys.md) | 4 | 100% 확률로 6~10개 | 8 |
| [Goombah](/wiki/04-Aliens/Goombah.md) | 3, 4 | 100% 확률로 2~4개 | 3 |

- **그 밖에**: 상점에서 판매하지 않습니다.

**쓰이는 곳**

- [대장간](/wiki/06-Items/Forge.md), 파열하는 → 영원한: **240** (함께 필요: Power Core 8개, Dark Matter Plate 2개, 크레딧 500,000, Thulium 2,000; 성공 확률 60%)

실패한 대장간 단계는 재료의 50%를 돌려주며, 소수점 이하는 내림합니다.

**모으는 방법**: [Crystalys](/wiki/04-Aliens/Crystalys.md)(섹터 4) 처치, 처치당 평균 8개. 가장 가까운 획득처: 섹터 3의 [Goombah](/wiki/04-Aliens/Goombah.md), 처치당 3개.

### Velkonite {#velkonite}

*고급 자원.* 내 Skylab의 Velkonite 수집기가 채굴해 자원 창고에 보관하는 광석입니다. 단조소가 이것으로 Velkonite Reinforced Plate를 만듭니다.

**얻는 방법**

- **Skylab**: Velkonite 수집기만 채굴하며, 72시간분을 저장하는 저장소에 쌓입니다. 수거하면 자원 창고로 옮겨집니다. 외계인은 드롭하지 않습니다.

| 모듈 레벨 | 1 | 5 | 10 | 15 | 20 |
| :--- | --: | --: | --: | --: | --: |
| 시간당 Velkonite | 12 | 29 | 89 | 273 | 833 |

이 수치는 전력이 공급되는 정거장 기준입니다. 전력 부족이 생기면 모든 농장과 수집기가 멈추고, 모듈은 코어보다 높은 레벨로 업그레이드할 수 없으며 코어는 레벨 20에서 멈춥니다([Skylab](/wiki/03-Mechanics/Skylab.md) 참고).

수집기 건설 비용: 코어 레벨 5, Ship Fragment 10개, 크레딧 10,000, Thulium 500.

- **그 밖에**: 상점에서 판매하지 않습니다.

**쓰이는 곳**

- [Skylab](/wiki/03-Mechanics/Skylab.md) 단조소: 단조소 레벨 1에서 Velkonite Reinforced Plate 1장당 **40**개, 레벨 1을 넘는 레벨마다 1.5%씩 줄어듭니다(레벨 20에서는 그 71.5%)

**모으는 방법**: 수집기 레벨을 올리고(레벨마다 시간당 생산량이 25%씩 늘어납니다), 저장소가 차기 전에 비우세요. 가득 차면 멈춥니다.

### Orvium {#orvium}

*희귀 자원.* 내 Skylab의 Orvium 수집기가 채굴해 자원 창고에 보관하는 희귀 광석입니다. 단조소가 이것으로 Orvium Reinforced Plate를 만듭니다.

**얻는 방법**

- **Skylab**: Orvium 수집기만 채굴하며, 72시간분을 저장하는 저장소에 쌓입니다. 수거하면 자원 창고로 옮겨집니다. 외계인은 드롭하지 않습니다.

| 모듈 레벨 | 1 | 5 | 10 | 15 | 20 |
| :--- | --: | --: | --: | --: | --: |
| 시간당 Orvium | 6 | 15 | 45 | 136 | 416 |

이 수치는 전력이 공급되는 정거장 기준입니다. 전력 부족이 생기면 모든 농장과 수집기가 멈추고, 모듈은 코어보다 높은 레벨로 업그레이드할 수 없으며 코어는 레벨 20에서 멈춥니다([Skylab](/wiki/03-Mechanics/Skylab.md) 참고).

수집기 건설 비용: 코어 레벨 5, Ship Fragment 10개, 크레딧 10,000, Thulium 500.

- **그 밖에**: 상점에서 판매하지 않습니다.

**쓰이는 곳**

- [Skylab](/wiki/03-Mechanics/Skylab.md) 단조소: 단조소 레벨 1에서 Orvium Reinforced Plate 1장당 **80**개, 레벨 1을 넘는 레벨마다 1.5%씩 줄어듭니다(레벨 20에서는 그 71.5%)

**모으는 방법**: 수집기 레벨을 올리고(레벨마다 시간당 생산량이 25%씩 늘어납니다), 저장소가 차기 전에 비우세요. 가득 차면 멈춥니다.

### Velkonite Reinforced Plate {#velkonite-reinforced-plate}

*희귀 자원.* Skylab 단조소에서 Velkonite로 단조합니다. 어셈블리가 더 강한 장비와 Dark Matter Plate를 만들 때 요구합니다.

**얻는 방법**

- **Skylab**: 단조소에서만 만들 수 있습니다. 원료: Velkonite, 플레이트 1장에 10초. 외계인은 드롭하지 않습니다.

| 단조소 레벨 | 1 | 5 | 10 | 15 | 20 |
| :--- | --: | --: | --: | --: | --: |
| 플레이트당 Velkonite | 40 | 37.6 | 34.6 | 31.6 | 28.6 |
| 배치당 플레이트 수 | 10 | 30 | 55 | 80 | 105 |
| 가득 찬 배치당 Velkonite | 400 | 1,128 | 1,903 | 2,528 | 3,003 |

배치의 광석은 배치 전체를 기준으로 계산하며(올림), 배치를 시작할 때 자원 창고에서 빠져나갑니다. 단조소 레벨에는 그 레벨 이상의 코어가 필요하며, 정거장에 전력이 모자라면 단조소는 새 배치를 시작하지 않습니다.

- **그 밖에**: 상점에서 판매하지 않습니다.

**쓰이는 곳**

- [Quantum Laser 3](/wiki/06-Items/Lasers.md): **2** (함께 필요: Ship Fragment 10개, Thulium 1,500)
- [Starfire-3](/wiki/06-Items/Lasers.md): **8** (함께 필요: Quantum Laser 3 1개, Reinforced Hull Plate 1개, Ship Fragment 15개, 크레딧 100,000, Thulium 1,500)
- [Nova Amp](/wiki/06-Items/Lasers.md): **3** (함께 필요: Cataclysite 30개, Power Core 1개, Pulse Amp 1개, Thulium 1,200)
- [Apex Amp](/wiki/06-Items/Lasers.md): **3** (함께 필요: Cataclysite 30개, Power Core 1개, Prism Amp 1개, Thulium 1,200)
- [Absorption Shield Cell IV](/wiki/06-Items/Shields.md): **6** (함께 필요: Absorption Shield Cell III 1개, Cataclysite 20개, Reinforced Hull Plate 8개, Thulium 2,500)
- [Impulse Thruster IV](/wiki/06-Items/Propulsion.md): **6** (함께 필요: Impulse Thruster III 1개, Power Core 3개, Ship Fragment 60개, Thulium 2,000)
- Dark Matter Plate: **1** (함께 필요: Dark Matter 5개, Orvium Reinforced Plate 1개, Thulium 250)
- [Heavy Shield Core](/wiki/06-Items/Shields.md): **6** (함께 필요: Basic Shield Core 1개, Cataclysite 20개, Reinforced Hull Plate 8개, Thulium 2,000)
- [Engine III](/wiki/06-Items/Propulsion.md): **6** (함께 필요: Engine II 1개, Power Core 3개, Ship Fragment 60개, Thulium 2,000)
- [Impulse Thruster III](/wiki/06-Items/Propulsion.md): **4** (함께 필요: Impulse Thruster II 1개, Power Core 2개, Ship Fragment 30개, Thulium 1,500)
- [Absorption Shield Cell II](/wiki/06-Items/Shields.md): **2** (함께 필요: Absorption Shield Cell I 1개, Cataclysite 10개, Reinforced Hull Plate 4개, Thulium 1,000)
- [Absorption Shield Cell III](/wiki/06-Items/Shields.md): **4** (함께 필요: Absorption Shield Cell II 1개, Cataclysite 15개, Reinforced Hull Plate 6개, Thulium 1,500)
- [Capacity Shield Cell II](/wiki/06-Items/Shields.md): **2** (함께 필요: Capacity Shield Cell I 1개, Cataclysite 10개, Reinforced Hull Plate 4개, Thulium 1,000)
- [Capacity Shield Cell III](/wiki/06-Items/Shields.md): **4** (함께 필요: Capacity Shield Cell II 1개, Cataclysite 15개, Reinforced Hull Plate 6개, Thulium 1,500)
- [Capacity Shield Cell IV](/wiki/06-Items/Shields.md): **6** (함께 필요: Capacity Shield Cell III 1개, Cataclysite 20개, Reinforced Hull Plate 8개, Thulium 2,500)
- [Impulse Thruster II](/wiki/06-Items/Propulsion.md): **2** (함께 필요: Impulse Thruster I 1개, Power Core 1개, Ship Fragment 10개, Thulium 1,000)
- [Momentum Thruster II](/wiki/06-Items/Propulsion.md): **2** (함께 필요: Momentum Thruster I 1개, Power Core 1개, Ship Fragment 10개, Thulium 1,000)
- [Momentum Thruster III](/wiki/06-Items/Propulsion.md): **4** (함께 필요: Momentum Thruster II 1개, Power Core 2개, Ship Fragment 30개, Thulium 1,500)
- [Momentum Thruster IV](/wiki/06-Items/Propulsion.md): **6** (함께 필요: Momentum Thruster III 1개, Power Core 3개, Ship Fragment 60개, Thulium 2,000)

**모듈 업그레이드**: 어셈블리에서 업그레이드할 수 있는 조합: Quantum Laser 3 → Starfire-3, Pulse Amp → Nova Amp, Prism Amp → Apex Amp, Absorption Shield Cell III → Absorption Shield Cell IV, Impulse Thruster III → Impulse Thruster IV, Basic Shield Core → Heavy Shield Core, Engine II → Engine III, Impulse Thruster II → Impulse Thruster III, Absorption Shield Cell I → Absorption Shield Cell II, Absorption Shield Cell II → Absorption Shield Cell III, Capacity Shield Cell I → Capacity Shield Cell II, Capacity Shield Cell II → Capacity Shield Cell III, Capacity Shield Cell III → Capacity Shield Cell IV, Impulse Thruster I → Impulse Thruster II, Momentum Thruster I → Momentum Thruster II, Momentum Thruster II → Momentum Thruster III 및 Momentum Thruster III → Momentum Thruster IV. 업그레이드할 때마다 출발 부품은 소모되며, 다른 재료와 함께 이 플레이트도 필요합니다. 새 부품은 넣은 부품의 대장간 등급을 이어받으며 보너스는 다시 굴리므로, 이전 보너스보다 좋을 수도 나쁠 수도 있습니다. 참고: [어셈블리의 모듈 업그레이드](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly).

**모으는 방법**: 단조소에 광석을 공급하고, 배치를 가득 채워 시작한 뒤, 함선이 착륙해 있을 때 플레이트를 수거하세요.

### Orvium Reinforced Plate {#orvium-reinforced-plate}

*영웅 자원.* Skylab 단조소에서 Orvium으로 단조합니다. 어셈블리가 Helios Beam이나 Dark Matter Plate를 만들 때 요구합니다.

**얻는 방법**

- **Skylab**: 단조소에서만 만들 수 있습니다. 원료: Orvium, 플레이트 1장에 10초. 외계인은 드롭하지 않습니다.

| 단조소 레벨 | 1 | 5 | 10 | 15 | 20 |
| :--- | --: | --: | --: | --: | --: |
| 플레이트당 Orvium | 80 | 75.2 | 69.2 | 63.2 | 57.2 |
| 배치당 플레이트 수 | 10 | 30 | 55 | 80 | 105 |
| 가득 찬 배치당 Orvium | 800 | 2,256 | 3,806 | 5,056 | 6,006 |

배치의 광석은 배치 전체를 기준으로 계산하며(올림), 배치를 시작할 때 자원 창고에서 빠져나갑니다. 단조소 레벨에는 그 레벨 이상의 코어가 필요하며, 정거장에 전력이 모자라면 단조소는 새 배치를 시작하지 않습니다.

- **그 밖에**: 상점에서 판매하지 않습니다.

**쓰이는 곳**

- [Helios Beam](/wiki/06-Items/Lasers.md): **18** (함께 필요: Cataclysite 50개, Power Core 2개, Reinforced Hull Plate 4개, Starfire-3 1개, Thulium 2,000)
- Dark Matter Plate: **1** (함께 필요: Dark Matter 5개, Velkonite Reinforced Plate 1개, Thulium 250)

**모듈 업그레이드**: 어셈블리에서 업그레이드할 수 있는 조합: Starfire-3 → Helios Beam. 업그레이드할 때마다 출발 부품은 소모되며, 다른 재료와 함께 이 플레이트도 필요합니다. 새 부품은 넣은 부품의 대장간 등급을 이어받으며 보너스는 다시 굴리므로, 이전 보너스보다 좋을 수도 나쁠 수도 있습니다. 참고: [어셈블리의 모듈 업그레이드](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly).

**모으는 방법**: 단조소에 광석을 공급하고, 배치를 가득 채워 시작한 뒤, 함선이 착륙해 있을 때 플레이트를 수거하세요.

### Dark Matter {#dark-matter}

*영웅 자원.* 블랙홀이 삼킨 N.I.K.E. 한 발마다 돌려주는 것으로, 블랙홀 영역 가장자리의 작은 상자에 담겨 나옵니다. 어셈블리가 이것 5개를 Velkonite Reinforced Plate, Orvium Reinforced Plate 하나씩과 함께 압착해 Dark Matter Plate 하나를 만듭니다.

**얻는 방법**

- **블랙홀**: [N.I.K.E.](/wiki/06-Items/Rockets.md) 로켓이 위험 섹터 4 한가운데 있는 블랙홀의 사건의 지평선을 넘으면 삼켜지고, 블랙홀은 영역 가장자리(중심에서 3,050~3,950유닛)의 상자(상자당 최대 2개)에 **1, 2 또는 3**개의 Dark Matter(평균 2개)를 돌려줍니다. 상자는 60초 동안 내 것이자 내 클랜의 것이며, 240초 동안 남아 있습니다. 도중에 함선을 만난 N.I.K.E.는 그 함선을 대신 맞히고 소모됩니다. [블랙홀](/wiki/03-Mechanics/Black-Hole.md#dark-matter)을 참고하세요.
- **그 밖에**: 상점에서 판매하지 않습니다.

**쓰이는 곳**

- Dark Matter Plate: **5** (함께 필요: Orvium Reinforced Plate 1개, Velkonite Reinforced Plate 1개, Thulium 250)

**모으는 방법**: [N.I.K.E.](/wiki/06-Items/Rockets.md) 로켓을 블랙홀에 쏘고(어셈블리에서 제작), 다른 누군가가 가져가기 전에 블랙홀 영역 가장자리의 상자를 회수하세요.

### Dark Matter Plate {#dark-matter-plate}

*신화 자원.* 어셈블리에서 Dark Matter와 강화 플레이트 두 장으로 압착해 만듭니다. 대장간은 최상위 두 단계마다 이것을 두 개씩 요구합니다.

**얻는 방법**

- **어셈블리**: 압착해 만듭니다. 재료: Dark Matter 5개, Orvium Reinforced Plate 1개 및 Velkonite Reinforced Plate 1개. 소요: Thulium 250 및 120초. 외계인은 드롭하지 않습니다.
- **그 밖에**: 상점에서 판매하지 않습니다.

**쓰이는 곳**

- [대장간](/wiki/06-Items/Forge.md), 신성한 → 파열하는: **2** (함께 필요: Reinforced Hull Plate 20개, Cataclysite 120개, 크레딧 200,000; 성공 확률 75%)
- [대장간](/wiki/06-Items/Forge.md), 파열하는 → 영원한: **2** (함께 필요: Power Core 8개, Quorvium 240개, 크레딧 500,000, Thulium 2,000; 성공 확률 60%)

실패한 대장간 단계는 재료의 50%를 돌려주며, 소수점 이하는 내림합니다.

**모으는 방법**: 찾는 것이 아니라 압착해 만듭니다. Dark Matter(위 참고)와 Skylab 단조소가 만드는 플레이트 두 종류를 모은 뒤, 어셈블리에서 제작을 시작하세요.

## 화폐 {#currencies}

크레딧과 Thulium은 재료와 마찬가지로 모으며 같은 곳에 씁니다. 인벤토리가 아니라 계정에 저장됩니다.

### 외계인이 주는 보상 {#what-each-alien-pays}

| 외계인 | 섹터 | 크레딧 | Thulium | 경험치 | 명예 |
| :--- | :---: | --: | --: | --: | --: |
| [Seeker](/wiki/04-Aliens/Seeker.md) | 1, 2 | 800 | 4 | 100 | 2 |
| [Phantasm](/wiki/04-Aliens/Phantasm.md) | 2, 3 | 2,400 | 12 | 300 | 6 |
| [Bulwark](/wiki/04-Aliens/Bulwark.md) | 3, 4 | 4,000 | 25 | 800 | 10 |
| [Goombah](/wiki/04-Aliens/Goombah.md) | 3, 4 | 12,000 | 75 | 3,000 | 24 |
| [Crystalys](/wiki/04-Aliens/Crystalys.md) | 4 | 60,000 | 200 | 12,000 | 52 |

이 수치는 **Alpha** 월드(1배) 기준입니다. 처치 보상은 Beta에서 이 수치의 **2배**, Gamma에서 **3배**이며, 미션 보상은 미션을 수행한 월드를 기준으로 합니다([월드](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)). 전리품 드롭은 모든 월드에서 같습니다. 여기에 시즌 상점의 영구 Credit Boost(최대 +50%)와 Thulium Boost(최대 +30%)가 처치와 미션이 주는 두 화폐의 양을 늘려 줍니다.

경험치와 명예는 돈이 아니라 점수이며, 레벨과 계급을 올려 주고 소비되지 않습니다.

### 크레딧 {#credits}

*기본 화폐.* 상점 대부분의 구매, 대장간, Skylab의 모든 모듈, 몇몇 서비스에 씁니다.

**얻는 방법**

- **시작 시**: 신규 파일럿의 계정에 들어 있는 크레딧: 10,000.
- **외계인**: 처치할 때마다 지급합니다(위의 표).
- **[미션](/wiki/03-Mechanics/Quests.md)**: Alpha 기준 미션 88개의 크레딧 합계: 6,667,000(레벨 1의 84,500부터 레벨 8의 2,720,000까지).
- **[Skylab](/wiki/03-Mechanics/Skylab.md)**: 자리를 비운 동안 크레딧 농장에서 생산해 72시간분을 저장하는 저장소에 쌓습니다.

| 모듈 레벨 | 1 | 5 | 10 | 15 | 20 |
| :--- | --: | --: | --: | --: | --: |
| 시간당 크레딧 | 1,000 | 3,842 | 20,661 | 111,120 | 597,630 |

이 수치는 전력이 공급되는 정거장 기준입니다. 전력 부족이 생기면 모든 농장과 수집기가 멈추고, 모듈은 코어보다 높은 레벨로 업그레이드할 수 없으며 코어는 레벨 20에서 멈춥니다([Skylab](/wiki/03-Mechanics/Skylab.md) 참고).

- **[클랜](/wiki/03-Mechanics/Clans.md) 지급**: 클랜 리더는 클랜 은행에서 멤버에게 크레딧을 지급할 수 있습니다.
- **보너스 코드**: 이벤트나 공식 Discord에서 나눠 주는 코드로 크레딧을 받을 수 있으며, 재료, 장비, 부스터, 함선이 함께 지급되기도 합니다. Thulium 페이지의 보너스 코드 카드에 입력하세요. 코드는 파일럿당 한 번씩 사용할 수 있습니다.
- 실패한 대장간 단계는 크레딧을 돌려주지 않으며, 재료와 Thulium은 50%만 돌아옵니다.

**쓰이는 곳**

- **상점**: 아이템 27개의 가격이 크레딧으로 책정되어 있습니다(가격은 각 아이템 페이지에 나옵니다: [아이템 개요](/wiki/06-Items/Overview.md) 및 [로켓](/wiki/06-Items/Rockets.md)).
- **어셈블리**, 제작 1회당: [Starfire-3](/wiki/06-Items/Lasers.md) 100,000, [N.U.K.E.](/wiki/06-Items/Rockets.md) 150,000, [N.I.K.E.](/wiki/06-Items/Rockets.md) (1회 5개 제작) 100,000.
- **[대장간](/wiki/06-Items/Forge.md)**, 등급 단계당: 표준 → 오염된 10,000, 오염된 → 신성한 50,000, 신성한 → 파열하는 200,000, 파열하는 → 영원한 500,000.
- **대장간 병합**, 만들어지는 등급별: 오염된 5,000, 신성한 25,000, 파열하는 100,000, 영원한 250,000.
- **[Skylab](/wiki/03-Mechanics/Skylab.md)** 건설과 업그레이드, 모듈별 기본 가격: 크레딧 농장 1,000(레벨마다 x1.6), 단조소 10,000(레벨마다 x1.5), Orvium 수집기 10,000(레벨마다 x1.5), 태양광 500(레벨마다 x1.4), 자원 창고 10,000(레벨마다 x1.4), Thulium 농장 5,000(레벨마다 x1.8), Velkonite 수집기 10,000(레벨마다 x1.5). 코어는 처음부터 있으므로 처음 내는 가격은 레벨 2의 가격입니다: 1,500(그 뒤로는 레벨마다 x1.5).
- **에너지 물질화 장치**: 스캔 1회에 크레딧 5,000, Chrono-Gate 부품을 찾습니다([자세히](/wiki/03-Mechanics/Wipe-Timeline.md#the-energy-materializer)).
- **기업 변경**: 크레딧 5,000(처음 기업을 고를 때는 무료).
- **[클랜](/wiki/03-Mechanics/Clans.md)**: 클랜 은행 기부(파일럿당 24시간 동안 최대 크레딧 1,000,000)와 클랜의 일일 세금(리더가 정한 내 크레딧의 일정 비율).

**모으는 방법**: 처치당 가장 많이 주는 외계인: [Crystalys](/wiki/04-Aliens/Crystalys.md)(Alpha 60,000, Gamma 180,000; 섹터 4). 가장 가까운 획득처: [Seeker](/wiki/04-Aliens/Seeker.md)(Alpha 800; 섹터 1). 전력이 공급되는 크레딧 농장의 생산량은 레벨 1에서 시간당 1,000, 레벨 20에서 597,630입니다(코어 레벨 20 기준). 저장소는 가득 차면 멈추므로 제때 수거하세요.

### Thulium {#thulium}

*희귀 화폐.* 최고급 장비와 부스터에 씁니다.

**얻는 방법**

- **시작 시**: 신규 파일럿의 계정에 들어 있는 Thulium: 100.
- **외계인**: 처치할 때마다 지급합니다(위의 표).
- **[미션](/wiki/03-Mechanics/Quests.md)**: Alpha 기준 미션 88개의 Thulium 합계: 50,980(레벨 1의 170부터 레벨 8의 21,760까지).
- **[Skylab](/wiki/03-Mechanics/Skylab.md)**: 자리를 비운 동안 Thulium 농장에서 생산해 72시간분을 저장하는 저장소에 쌓습니다.

| 모듈 레벨 | 1 | 5 | 10 | 15 | 20 |
| :--- | --: | --: | --: | --: | --: |
| 시간당 Thulium | 50 | 143 | 530 | 1,969 | 7,310 |

이 수치는 전력이 공급되는 정거장 기준입니다. 전력 부족이 생기면 모든 농장과 수집기가 멈추고, 모듈은 코어보다 높은 레벨로 업그레이드할 수 없으며 코어는 레벨 20에서 멈춥니다([Skylab](/wiki/03-Mechanics/Skylab.md) 참고).

- **보너스 코드**: 이벤트나 공식 Discord에서 나눠 주는 코드로 Thulium을 받을 수 있으며, 재료, 장비, 부스터, 함선이 함께 지급되기도 합니다. Thulium 페이지의 보너스 코드 카드에 입력하세요. 코드는 파일럿당 한 번씩 사용할 수 있습니다.
- 실패한 대장간 단계는 Thulium의 50%를 돌려주며, 소수점 이하는 내림합니다.

**쓰이는 곳**

- **상점**: 아이템 27개의 가격이 Thulium으로 책정되어 있습니다(가격은 각 아이템 페이지에 나옵니다: [아이템 개요](/wiki/06-Items/Overview.md) 및 [로켓](/wiki/06-Items/Rockets.md)).
- **어셈블리**, 제작 1회당: [Master Drone](/wiki/06-Items/Drones.md) 40,000, [Quantum Laser 3](/wiki/06-Items/Lasers.md) 1,500, [Starfire-3](/wiki/06-Items/Lasers.md) 1,500, [Helios Beam](/wiki/06-Items/Lasers.md) 2,000, [Paragon](/wiki/02-Ships/Paragon.md) 1,500, [Wraith](/wiki/02-Ships/Wraith.md) 20,000, [Damage Amp II](/wiki/06-Items/Boosters.md) 20,000, [Shield Wall II](/wiki/06-Items/Boosters.md) 15,000, [Hull Plating II](/wiki/06-Items/Boosters.md) 15,000, [Nova Amp](/wiki/06-Items/Lasers.md) 1,200, [Apex Amp](/wiki/06-Items/Lasers.md) 1,200, [Absorption Shield Cell IV](/wiki/06-Items/Shields.md) 2,500, [Impulse Thruster IV](/wiki/06-Items/Propulsion.md) 2,000, Dark Matter Plate 250, [Ironclad](/wiki/02-Ships/Ironclad.md) 10,500, [Heavy Shield Core](/wiki/06-Items/Shields.md) 2,000, [Engine III](/wiki/06-Items/Propulsion.md) 2,000, [Impulse Thruster III](/wiki/06-Items/Propulsion.md) 1,500, [Absorption Shield Cell II](/wiki/06-Items/Shields.md) 1,000, [Absorption Shield Cell III](/wiki/06-Items/Shields.md) 1,500, [Capacity Shield Cell II](/wiki/06-Items/Shields.md) 1,000, [Capacity Shield Cell III](/wiki/06-Items/Shields.md) 1,500, [Capacity Shield Cell IV](/wiki/06-Items/Shields.md) 2,500, [Impulse Thruster II](/wiki/06-Items/Propulsion.md) 1,000, [Momentum Thruster II](/wiki/06-Items/Propulsion.md) 1,000, [Momentum Thruster III](/wiki/06-Items/Propulsion.md) 1,500, [Momentum Thruster IV](/wiki/06-Items/Propulsion.md) 2,000, [N.U.K.E.](/wiki/06-Items/Rockets.md) 3,000, [N.I.K.E.](/wiki/06-Items/Rockets.md) (1회 5개 제작) 1,500.
- **[대장간](/wiki/06-Items/Forge.md)**, 등급 단계당: 파열하는 → 영원한 2,000.
- **[Skylab](/wiki/03-Mechanics/Skylab.md)** 건설과 업그레이드, 모듈별 기본 가격: 크레딧 농장 100(레벨마다 x1.6), 단조소 500(레벨마다 x1.5), Orvium 수집기 500(레벨마다 x1.5), 태양광 50(레벨마다 x1.4), 자원 창고 500(레벨마다 x1.4), Thulium 농장 500(레벨마다 x1.8), Velkonite 수집기 500(레벨마다 x1.5).
- **에너지 물질화 장치**: 스캔 1회에 Thulium 5, Chrono-Gate 부품을 찾습니다([자세히](/wiki/03-Mechanics/Wipe-Timeline.md#the-energy-materializer)).

**모으는 방법**: 처치당 가장 많이 주는 외계인: [Crystalys](/wiki/04-Aliens/Crystalys.md)(Alpha 200, Gamma 600; 섹터 4). 가장 가까운 획득처: [Seeker](/wiki/04-Aliens/Seeker.md)(Alpha 4; 섹터 1). 전력이 공급되는 Thulium 농장의 생산량은 레벨 1에서 시간당 50, 레벨 20에서 7,310입니다(코어 레벨 20 기준). 저장소는 가득 차면 멈추므로 제때 수거하세요.

## 알아 두면 좋은 점 {#good-to-know}

- **상자**: 외계인의 드롭은 폭발한 자리에 상자 하나로 떨어지며, 처치한 파일럿과 그 클랜이 30초 동안 독점합니다. [Resource Magnet](/wiki/06-Items/Boosters.md) 부스터는 상자에 든 양을 25% 늘려 줍니다. [화물](/wiki/03-Mechanics/Cargo.md)을 참고하세요.
- **잔해**: 격파된 [기업 파일럿](/wiki/03-Mechanics/Company-Pilots.md)은 누가 또는 무엇이 격파하든 상자도 부품도 남기지 않으므로, 파일럿의 함선은 재료를 얻는 수단이 아닙니다. 평화 프로토콜이 끝난 뒤 [월드](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)가 PvP를 허용하는 곳에서는 다른 기업의 파일럿을 격추할 수 있으며, 소속 기업의 파일럿을 격파하면 명예가 100 깎입니다.
- **모듈 업그레이드**: 어셈블리는 한 단계 아래 부품을 업그레이드해 Starfire-3, Helios Beam, Nova Amp, Apex Amp, Absorption Shield Cell IV, Impulse Thruster IV, Heavy Shield Core, Engine III, Impulse Thruster III, Absorption Shield Cell II, Absorption Shield Cell III, Capacity Shield Cell II, Capacity Shield Cell III, Capacity Shield Cell IV, Impulse Thruster II, Momentum Thruster II, Momentum Thruster III 및 Momentum Thruster IV 아이템을 만들며, 그 부품은 소모됩니다. 업그레이드에 필요한 플레이트: Velkonite Reinforced Plate 및 Orvium Reinforced Plate. Quantum Laser 3 및 Dark Matter Plate도 같은 플레이트를 요구합니다. 새 부품은 넣은 부품의 대장간 등급을 이어받으며 보너스는 다시 굴리므로, 이전 보너스보다 좋을 수도 나쁠 수도 있습니다. 참고: [어셈블리의 모듈 업그레이드](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly).
- **보관 위치**: 어셈블리, 대장간, Skylab 건설에 쓰이는 것은 인벤토리에 장착되지 않은 채 쌓인 묶음입니다. 함선에 장착된 것이나 수송 보관함에 있는 묶음은 쓰이지 않습니다.
- **초기화**: 인벤토리의 재료는 [초기화 규칙](/wiki/03-Mechanics/Wipe-Timeline.md)을 따르며, Skylab의 자원 창고에 보관된 광석은 남습니다.

<!-- resources:end -->
