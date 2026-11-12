<!-- wiki-i18n source: 9b254c924e79c7e8 -->
<!-- wiki-i18n title: 솔로 게이트 -->
# 솔로 게이트 {#solo-gates}

<!-- wiki-search: solo gates; solo gate; gate; gates; galaxy gates; rift; rifts; alpha rift; beta breach; gamma foundry; delta siege; omega vault; chrono gate; chrono-gate; materializer; energy materializer; scan; spin; gate part; gate parts; guarantee; pity; consolation; wave; waves; nuke wave; skip; boss; lives; resume; abandon; speedrun; no death; challenge; achievement; thulium cap; 솔로 게이트; 게이트; 갤럭시 게이트; 부품; 게이트 부품; 에너지 물질화 장치; 스핀; 보장; 웨이브; 목숨; 이어하기; 포기; 무사망; 도전; 도전 과제; Thulium 상한 -->

**솔로 게이트**는 갤럭시 게이트 가운데 혼자 날아 들어가는 다섯 게이트입니다. **Alpha Rift**, **Beta Breach**, **Gamma Foundry**, **Delta Siege**, **Omega Vault**가 있습니다. 각각 자기만의 텅 빈 경기장이며, 외계인 웨이브가 차례로 몰려오고 끝에는 보스가 기다립니다. 게이트는 **부품**으로 건설하며, 부품은 Thulium으로 에너지 물질화 장치를 스핀해서 찾습니다. 클리어하면 크레딧, Thulium, 경험치, 명예, 광석, 플레이트, 탄약이 지급됩니다.

솔로 게이트는 [클랜 던전](/wiki/03-Mechanics/Dungeons.md)이 아닙니다. 던전은 클랜이 그룹을 위해 여는 미로이고 끝에 워로드가 있으며, 솔로 게이트는 당신 혼자만 있는 경기장으로 다른 누구도 함께 들어올 수 없습니다. 둘은 규칙, 보상, 제한이 따로입니다. 갤럭시 게이트 페이지에는 **Chrono-Gate**도 있는데, 날아 들어가는 곳이 아니라 초기화를 위해 당신의 [수송 보관함](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-)을 여는 게이트이며, 그 부품도 같은 스핀으로 찾습니다.

## 한눈에 보기 {#at-a-glance}

<!-- solo-glance:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **게이트**: 6: Chrono-Gate와 솔로 게이트 5개, Alpha Rift, Beta Breach, Gamma Foundry, Delta Siege와 Omega Vault
- **스핀**: 스핀 한 번에 Thulium 100, 한 번에 1, 5, 10 또는 100회 스핀
- **부품 확률**: 스핀당 13%. 부품이 속하는 게이트는 무작위로 정해지며 각 게이트가 스핀의 2.17%를 가집니다. Chrono-Gate가 완성되면 그 몫은 휠에서 빠지고 솔로 게이트는 각각 2.17%를 유지합니다
- **보장**: 부품 없이 스핀이 24번 연속되면 스핀마다 확률이 오르고, 47번 뒤에는 다음 스핀이 반드시 부품을 찾습니다. 어느 게이트의 부품이든 횟수가 처음으로 돌아갑니다
- **목숨**: 한 번의 도전에 3. 죽을 때마다 하나씩 줄어듭니다
- **카운트다운**: 모든 웨이브 전에 5초. 첫 웨이브와 보스 웨이브도 마찬가지입니다. 웨이브에는 타이머가 없고 런에도 없습니다
- **경기장**: 바위 없이 8,000 × 6,000 유닛의 열린 공간이며 그 안에는 당신뿐입니다. 월드에는 16개가 있으며 모두 사용 중이면 들어갈 수 없습니다
- **동시 외계인**: 웨이브의 동시 생존은 최대 60, 선택 웨이브는 250입니다. 나머지는 자리가 나기를 기다립니다
- **보스**: 보스는 페이즈가 바뀔 때 3초 동안 피해를 입지 않습니다
- **Thulium 상한**: 게이트가 돌려주는 것은 스핀에 쓴 Thulium의 최대 50%까지입니다. 나머지는 잘리며, 결과 화면에 얼마가 잘렸는지 표시됩니다

<!-- solo-glance:end -->

## 게이트 부품 찾기 {#finding-gate-parts}

**갤럭시 게이트** 페이지를 열고 에너지 물질화 장치를 스핀합니다. 스핀은 한 번마다 Thulium으로 지불하며 부품은 많아야 하나 찾습니다. 그 부품은 여섯 게이트 중 하나에 속하며 무작위로 정해집니다. 게이트를 건설하려면 그 게이트의 부품이 일정 수 필요하고, 부품은 쓰기 전까지 당신의 것입니다. 부품을 찾지 못한 스핀은 버려지지 않고 상품을 지급합니다([아래](#a-spin-without-a-part)). 스핀은 Chrono-Gate가 완성되어 있어도 매번 청구됩니다. Chrono-Gate가 완성되면 그 몫의 스핀은 아무것도 찾지 못하고, 솔로 게이트는 자기 확률을 유지하므로 솔로 게이트의 부품은 Chrono-Gate가 있든 없든 같은 비용입니다.

표는 각 게이트의 부품 수와 **보장을 포함한** 평균 비용을 보여 줍니다(스핀은 추첨이므로 운 좋은 파일럿은 덜 내고 운 나쁜 파일럿은 더 내며, 보장이 허용하는 가장 긴 연속 스핀까지입니다).

<!-- solo-parts:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| 게이트 | 완성에 필요한 부품 | 스핀당 부품 확률 | 평균 스핀 수 | 평균 Thulium |
| :--- | ---: | ---: | ---: | ---: |
| **Chrono-Gate** | 2 | 2.17% | 91 | 9,093 |
| **Alpha Rift** | 11 | 2.17% | 500 | 50,011 |
| **Beta Breach** | 26 | 2.17% | 1,182 | 118,208 |
| **Gamma Foundry** | 54 | 2.17% | 2,455 | 245,508 |
| **Delta Siege** | 87 | 2.17% | 3,955 | 395,541 |
| **Omega Vault** | 108 | 2.17% | 4,910 | 491,017 |

<!-- solo-parts:end -->

Chrono-Gate의 부품은 초기화 때 0으로 돌아가며 시즌마다 다시 찾습니다. **솔로 게이트의 부품은 남습니다.** 보장의 횟수와 스핀에 쓴 양, 게이트가 돌려준 양의 기록도 남으며, 초기화는 어느 것도 가져가지 않습니다([게이트와 초기화](#gates-and-the-wipe)).

### 부품 없는 스핀 {#a-spin-without-a-part}

대부분의 스핀은 부품을 찾지 못합니다. 각 스핀은 아래 확률로 정해지는 상품 하나를 지급합니다. 두 번째 배율 이상의 레이저 탄약, 두 번째 또는 세 번째 등급의 로켓 묶음, 그리고 가끔 [특수 아이템](/wiki/06-Items/Special-Items.md)이나 [컨테이너](/wiki/06-Items/Containers.md)입니다. 줄 수 없는 상품(예를 들어 그 특수 아이템을 이미 최대로 가진 경우)은 같은 추첨에서 탄약이나 로켓 묶음으로 바뀌므로, 스핀은 표보다 적게 지급하는 일이 없습니다. 상품의 가치는 스핀 비용보다 분명히 낮습니다. 게이트는 Thulium을 빨아들이는 곳입니다.

<!-- solo-prizes:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| 보상 | 스핀당 확률 |
| :--- | ---: |
| 컨테이너: Chroma Archive | 0.01% |
| 특수 아이템: Magic Hammer | 0.2% |
| 특수 아이템: Schematics | 0.2% |
| 특수 아이템: Philosopher's Stone | 0.2% |
| 특수 아이템: Forger's Seal | 0.2% |
| 특수 아이템: Workforce Contract | 0.2% |
| 특수 아이템: Tinkerer's Badge | 0.1% |
| 레이저 탄약: Advanced Plasma ×75 | 12.88% |
| 레이저 탄약: Antimatter Battery I ×62 | 8.59% |
| 레이저 탄약: Ultra Core ×40 | 8.59% |
| 레이저 탄약: Antimatter Battery II ×29 | 4.29% |
| 레이저 탄약: Dark Matter Ammo I ×31 | 4.29% |
| 레이저 탄약: Experimental Fusion Core ×17 | 2.15% |
| 레이저 탄약: Dark Matter Ammo II ×17 | 2.15% |
| 로켓: Lancet II ×4 | 8.59% |
| 로켓: Rivet II ×4 | 8.59% |
| 로켓: Ember II ×4 | 8.59% |
| 로켓: Scatter II ×4 | 8.59% |
| 로켓: Lancet III ×1 | 2.15% |
| 로켓: Rivet III ×1 | 2.15% |
| 로켓: Ember III ×1 | 2.15% |
| 로켓: Scatter III ×1 | 2.15% |

<!-- solo-prizes:end -->

## 들어가기 {#going-in}

게이트는 갤럭시 게이트 페이지에서 **건설**하고, 그 포털로 **점프해 들어갑니다**. 건설은 스테이션에서 함선을 도킹한 채로 할 수 있고, 비행 중에도 할 수 있습니다. 툴바의 게이트 버튼으로 여는 **갤럭시 게이트 창**에서 페이지와 똑같이 스핀, 건설, 목적지 선택을 할 수 있습니다. 다음이 필요합니다.

- 게이트의 부품이 있어야 합니다. 부품은 **건설할 때 한 번** 가져가며, 거부된 건설은 아무것도 가져가지 않습니다.
- 열려 있는 다른 솔로 런이 없어야 합니다. 런은 한 번에 하나만 가질 수 있고, 떠난 런은 다른 게이트를 건설하기 전에 포털로 다시 들어가거나 포기해야 합니다.
- 홈 서버에 있어야 합니다(지역 서버에는 게이트가 없습니다).

건설한 게이트는 당신의 **기지 섹터**(기업에 따라 `M-1`, `T-1`, `G-1`)에 게이트 이름이 붙은 포털로 서 있으며, 어디에 있는지는 갤럭시 게이트 페이지가 알려 줍니다. **출격해서 포털까지 날아가 점프**하면 됩니다. 다른 포털과 같습니다. 들어갈 때 월드에 빈 균열이 있어야 합니다. 월드마다 균열이 일정 수 있으며, 모두 사용 중이면 기다립니다.

**지역 서버에서 (Singapore, US East).** 게이트 자체는 홈 서버에 남습니다. 지역 서버에서는 아무것도 건설하거나 플레이하거나 보상받지 않습니다. 그래도 건설한 게이트는 그곳에서도 잊히지 않습니다. 도착할 때 그 사실을 알려 주고, 게이트의 포털은 그곳에서도 당신의 기지 섹터에 서 있습니다. 그 포털로 점프하면 홈 서버로 돌아가며, 거기서 위와 같이 게이트로 출격하면 됩니다.

텅 빈 경기장 한가운데에 혼자 내립니다. 안에서는 누구도 당신을 공격할 수 없고, Jump CPU와 Base CPU는 작동하지 않습니다.

## 런이 진행되는 방식 {#how-a-run-goes}

1. **모든 웨이브 전에 카운트다운이 있습니다.** 첫 웨이브와 보스 웨이브도 마찬가지입니다. 웨이브에는 타이머가 없고 런에도 없습니다. 필요한 만큼 걸립니다.
2. **웨이브**는 당신 주위의 고리에서 나타나 게이트의 속도로 날아옵니다. 한 번에 일정 수만 살아 있고 나머지는 자리가 나기를 기다립니다. 마지막 외계인이 죽으면 끝납니다.
3. **진행 상황은 모든 웨이브 뒤에 저장됩니다.** 떠나면 진행 중이던 웨이브는 돌아왔을 때 처음부터 다시 시작합니다.
4. **선택 웨이브**는 Seeker의 거대한 웨이브이며 Delta Siege와 Omega Vault에 하나씩 있습니다. 카운트다운 중에 건너뛸 수 있으며, 건너뛰면 완료로 치고 **아무것도** 지급하지 않습니다. 싸우면 처치 보상은 다른 웨이브와 똑같이 지급됩니다.
5. **마지막 웨이브는 보스입니다.** 선체가 줄어들면 페이즈가 바뀌고, 바뀔 때마다 잠깐 피해를 입지 않습니다. 보스가 죽으면 런이 클리어되고 클리어 보상이 즉시 지급됩니다.

**목숨.** 죽으면 목숨 하나를 잃고 다른 죽음처럼 기지로 보내집니다. 런은 시계 없이 당신을 기다립니다. 런이 열려 있고 당신이 아레나 밖에 있는 동안에는 **게이트의 포털이 기지 섹터에 서 있고**, 그 포털로 점프하면 **이어하기**처럼 저장된 웨이브로 남은 목숨과 함께 돌려보내며 새 부품을 요구하지 않습니다. 마지막 목숨까지 잃으면 도전은 끝나지만 런은 마지막으로 클리어한 웨이브에서 열려 있고, 다시 들어가면 목숨이 다시 채워집니다. **나가기**, 로그오프, 월드 변경은 목숨을 잃지 않고 런을 일시 정지합니다. 서버를 재시작해도 런은 열려 있습니다. **포기**는 런을 포기하는 것으로, 부품은 사라지고 처치한 외계인은 그 시점 그대로 지급됩니다. **이어하기**는 비행 중인 함선에서만 됩니다. 죽은 뒤에는 결과 화면의 버튼이 이유를 알려 주는 한 줄과 함께, 리스폰할 때까지 기다립니다. 리스폰한 함선은 제한된 선체로 돌아오므로, 선체가 절반 아래이면 결과 화면이 경고합니다. 그래도 **이어하기**는 지금 상태 그대로 돌려보냅니다. 기지의 수리선은 오라 안에서 당신을 수리합니다.

모든 월드가 같은 게이트와 싸웁니다. 외계인의 강함과 보상은 날고 있는 월드에 따라 달라지지 않습니다.

### 웨이브 {#the-waves}

외계인은 게임의 그 외계인(Seeker, Phantasm, Bulwark, Goombah, Crystalys)이며 게이트에 따라 더 단단하게 또는 더 무르게 조정됩니다. 계획 시간은 레이저 기술이 시작 레벨인 파일럿에게 게이트가 걸리도록 만들어진 시간입니다([파일럿 스킬](/wiki/03-Mechanics/Pilot-Skills.md)). 레이저 기술을 올린 파일럿은 더 일찍 끝냅니다.

일부 웨이브에는 **무리**가 나옵니다. 게임의 보스 NPC(Boss Seeker, Boss Phantasm, Boss Goombah 또는 Boss Crystalys)가 호위대를 거느리고 하나의 집단으로 공격합니다. 무리의 모든 함선은 그 웨이브의 일부이며, 마지막 함선이 파괴되면 웨이브가 끝납니다. 보상은 웨이브의 다른 함선과 같이 [외계인 표](#the-aliens)의 수치대로 지급됩니다. **보스 NPC는 게임의 섹터에서와 똑같이 전리품을 떨어뜨립니다**. 광석, 플레이트, 탄약, 로켓입니다(무엇을 떨어뜨리는지는 [무리의 페이지](/wiki/05-Swarms/Swarms.md)에 있습니다). 게이트에는 주워야 할 상자가 없습니다. 전리품은 보상과 함께 바로 인벤토리로 들어오며, 보상처럼 런마다 한 번만 들어옵니다. 호위대는 게이트에서도 섹터에서도 아무것도 떨어뜨리지 않고, 보스를 치료하지도 돌아오지도 않습니다. 각 게이트의 어느 웨이브에 무리가 나오는지는 아래의 표에 나와 있습니다.

<!-- solo-waves:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| 게이트 | 웨이브 수(보스 포함) | 웨이브의 외계인 | 보스 NPC와 무리 | 보스 | 계획 시간 |
| :--- | ---: | :--- | :--- | :--- | :--- |
| **Alpha Rift** | 10 | 44 Seeker, 140 Phantasm | 웨이브 5: 1 Seeker Swarm, 1 Phantasm Swarm | Enhanced Phantasm | 10~15 분 |
| **Beta Breach** | 14 | 64 Seeker, 158 Phantasm, 80 Bulwark, 20 Goombah | 웨이브 4: 2 Seeker Swarm; 웨이브 9: 1 Phantasm Swarm | Enhanced Bulwark | 15~25 분 |
| **Gamma Foundry** | 18 | 78 Phantasm, 117 Bulwark, 91 Goombah, 8 Crystalys | 웨이브 4: 1 Phantasm Swarm; 웨이브 9: 1 Goombah Swarm; 웨이브 14: 1 Goombah Swarm | Elite Crystalys | 25~35 분 |
| **Delta Siege** | 22 | 250 Seeker, 200 Phantasm, 141 Bulwark, 130 Goombah, 12 Crystalys | 웨이브 5: 2 Phantasm Swarm; 웨이브 10: 2 Goombah Swarm; 웨이브 15: 1 Goombah Swarm; 웨이브 20: 1 Crystalys Swarm | Siege Construct | 35~45 분 |
| **Omega Vault** | 26 | 250 Seeker, 236 Phantasm, 170 Bulwark, 174 Goombah, 25 Crystalys | 웨이브 6: 1 Goombah Swarm; 웨이브 11: 2 Goombah Swarm; 웨이브 16: 1 Crystalys Swarm; 웨이브 22: 1 Phantasm Swarm | Omega Guardian | 50~60 분 |

- **Delta Siege**: 웨이브 18(250 Seeker)은 선택입니다. 카운트다운 중에 건너뛸 수 있으며 아무것도 지급하지 않습니다
- **Omega Vault**: 웨이브 17(250 Seeker)은 선택입니다. 카운트다운 중에 건너뛸 수 있으며 아무것도 지급하지 않습니다; 웨이브 22~24은 엘리트이며 선체, 실드, 피해가 ×1.5입니다

<!-- solo-waves:end -->

### 보스 {#the-bosses}

보스는 외계인의 함선을 키운 것으로, 선체, 실드, 일제 사격이 따로 있으며 게이트나 월드의 어떤 설정도 이를 바꾸지 않습니다. 보스의 선체가 표의 수치로 내려가면 페이즈가 시작됩니다. 실드가 다시 설정될 수 있고, 일제 사격이나 모든 피해가 바뀌며, 기술을 시작할 수 있습니다. 모든 기술은 예고됩니다. 원, 고리, 또는 당신의 함선 위의 표시가 떨어지기 직전에 알려 줍니다. 보스가 부르는 외계인은 보상도 드롭도 없습니다.

<!-- solo-bosses:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| 보스 | 게이트 | 선체 | 실드 | 레이저 일제 사격 |
| :--- | :--- | ---: | ---: | ---: |
| **Enhanced Phantasm** | Alpha Rift | 330,000 | 530,000 | 5,700–7,000 |
| **Enhanced Bulwark** | Beta Breach | 690,000 | 170,000 | 4,500–5,500 |
| **Elite Crystalys** | Gamma Foundry | 620,000 | 250,000 | 3,800–4,700 |
| **Siege Construct** | Delta Siege | 1,150,000 | 1,730,000 | 3,400–4,200 |
| **Omega Guardian** | Omega Vault | 1,340,000 | 840,000 | 2,600–3,200 |

| 보스 | 페이즈 | 남은 선체 | 하는 일 |
| :--- | :--- | :--- | :--- |
| **Enhanced Phantasm** | Enhanced Phantasm | 100%~0% | 쏘기만 합니다. |
| **Enhanced Bulwark** | Shielded | 100%~50% | 실드는 보스 본래 실드의 ×4로 설정됩니다. |
|  | Second attack | 50%~0% | 일제 사격은 ×1.3입니다. Dormant Lance 로켓 4발을 61,000씩 0.5초 간격으로 당신에게 쏘며, 30초마다 한 차례 일제히 발사합니다. |
| **Elite Crystalys** | Elite | 100%~50% | 쏘기만 합니다. |
|  | Reinforced | 50%~0% | 실드는 보스 본래 실드의 ×2로 설정됩니다. 10분마다 Goombah 10기를 부르며 동시에 최대 10기까지 살아 있습니다. 보상도 드롭도 없습니다. |
| **Siege Construct** | Siege Construct | 100%~0% | 1분마다 메테오 8개의 일제 낙하를 3번 떨어뜨립니다. 하나당 5,500이며 낙하 지점에서 420 유닛 이내의 모든 것에 적중하고, 그중 50%는 당신을 겨냥합니다. 각 원은 낙하 3초 전에 표시됩니다. Dormant Lance 로켓 6발을 9,000씩 0.5초 간격으로 당신에게 쏘며, 1분마다 한 차례 일제히 발사합니다. |
| **Omega Guardian** | Shield Fortress | 100%~70% | 실드는 보스 본래 실드의 ×1.5로 설정됩니다. 40초마다 Bulwark 6기를 부르며 동시에 최대 12기까지 살아 있습니다. 보상도 드롭도 없습니다. |
|  | Swarm Protocol | 70%~35% | 25초마다 Phantasm 12기를 부르며 동시에 최대 24기까지 살아 있습니다. 보상도 드롭도 없습니다. 30초마다 140,000의 폭발이 보스에서 700 유닛 이내의 모든 것에 적중합니다. 고리는 낙하 2초 전에 표시됩니다. |
|  | Overload | 35%~0% | 실드는 보스 본래 실드의 ×0.1로 설정됩니다. 모든 피해가 ×2.5입니다. 페이즈에 들어간 지 2분이 지나면 모든 피해가 추가로 ×2가 됩니다. 25초마다 28,000의 폭발이 보스에서 700 유닛 이내의 모든 것에 적중합니다. 고리는 낙하 2초 전에 표시됩니다. |

<!-- solo-bosses:end -->

## 클리어 보상 {#what-a-clear-pays}

클리어는 표의 보상을 보스가 죽는 순간 **한 번에 모두** 지급합니다. 크레딧, Thulium, 경험치와 명예, 광석, 플레이트와 Power Core, 탄약입니다. 경험치는 던전의 경험치처럼 PvE 랭킹 포인트에 들어갑니다.

<!-- solo-pay:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| 게이트 | 크레딧 | Thulium | 경험치 | 명예 |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 450,000 | 5,000 | 70,000 | 1,000 |
| **Beta Breach** | 1,500,000 | 12,000 | 180,000 | 2,500 |
| **Gamma Foundry** | 4,000,000 | 25,000 | 400,000 | 5,500 |
| **Delta Siege** | 8,000,000 | 40,000 | 800,000 | 10,000 |
| **Omega Vault** | 15,000,000 | 60,000 | 1,500,000 | 20,000 |

- **Alpha Rift**: Ship Fragment ×300, Nyxite ×300, Daraxium ×400; 탄약: Advanced Plasma ×20,000, Ultra Core ×5,000, Experimental Fusion Core ×20,000
- **Beta Breach**: Ship Fragment ×700, Nyxite ×750, Daraxium ×800, Cataclysite ×400, Quorvium ×100; 탄약: Advanced Plasma ×50,000, Ultra Core ×20,000, Experimental Fusion Core ×30,000
- **Gamma Foundry**: Ship Fragment ×1,150, Nyxite ×1,000, Cataclysite ×900, Quorvium ×400, Power Core ×15; 탄약: Advanced Plasma ×30,000, Ultra Core ×60,000, Experimental Fusion Core ×50,000
- **Delta Siege**: Ship Fragment ×2,000, Nyxite ×1,750, Cataclysite ×1,500, Quorvium ×1,000, Reinforced Hull Plate ×70, Power Core ×40, Ancient Control Unit ×3; 탄약: Advanced Plasma ×40,000, Ultra Core ×90,000, Experimental Fusion Core ×75,000
- **Omega Vault**: Ship Fragment ×3,250, Nyxite ×2,750, Cataclysite ×2,250, Quorvium ×1,600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10; 탄약: Advanced Plasma ×50,000, Ultra Core ×100,000, Experimental Fusion Core ×100,000

<!-- solo-pay:end -->

**Thulium에는 상한이 있습니다.** 게이트가 돌려줄 수 있는 것은 스핀에 쓴 Thulium의 일정 몫까지이며, 모든 게이트와 모든 스핀을 합쳐 셉니다(그 몫은 맨 위 목록에 있습니다). 클리어와 외계인이 그 이상 지급했을 몫은 잘리며, 결과 화면에 얼마가 잘렸는지 표시됩니다. 크레딧, 경험치, 명예, 광석, 플레이트, 탄약은 잘리지 않습니다.

### 외계인 {#the-aliens}

게이트에서 처치한 외계인은 어느 월드를 날든 Alpha에서의 수치로 지급합니다. 월드 배율, 부스터, 프리미엄 보너스는 영향을 주지 않습니다. 웨이브는 외계인에 대한 보상을 런마다 **한 번만** 지급하며, 몇 번을 떠났다 돌아와도 같습니다. 보상은 런의 각 구간이 끝날 때 지급됩니다. 떠날 때, 죽을 때, 목숨이 다할 때, 포기할 때, 클리어할 때입니다. 구간의 처치가 지급되지 않는 경우는 초기화와, 안에 있는 동안 서버가 재시작될 때뿐입니다(런은 열린 채로 남지만 그 구간의 처치는 사라집니다). 게이트에서의 처치는 **섹터를 지정하지 않는** [미션](/wiki/03-Mechanics/Quests.md#where-it-counts)(도전 과제 라인의 큰 사냥 등)에 처치하는 순간 집계됩니다(웨이브는 보상이 한 번만 지급되듯이 런마다 **한 번만** 집계됩니다). 그 밖의 어디에도 집계되지 않습니다. 처치 통계, 도전 과제 카운터, 킬 피드, 드론과 P.E.T.의 경험치 어디에도 들어가지 않습니다. 다만 처치가 지급하는 경험치는 클리어의 경험치처럼 PvE 랭킹 포인트에 들어갑니다. 외계인의 전리품은 보상과 함께 바로 인벤토리로 들어옵니다.

<!-- solo-kills:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| 외계인 | 크레딧 | Thulium | 경험치 | 명예 |
| :--- | ---: | ---: | ---: | ---: |
| **Seeker** | 1,000 | 4 | 100 | 2 |
| **Phantasm** | 3,000 | 12 | 300 | 6 |
| **Bulwark** | 5,000 | 25 | 800 | 10 |
| **Goombah** | 15,000 | 75 | 3,000 | 24 |
| **Crystalys** | 75,000 | 200 | 12,000 | 52 |
| **Boss Seeker** | 10,000 | 40 | 1,000 | 20 |
| **Seeker Slave** | 125 | 1 | 12 | 1 |
| **Boss Phantasm** | 39,000 | 195 | 7,800 | 62 |
| **Phantasm Guard** | 125 | 1 | 12 | 1 |
| **Boss Goombah** | 120,000 | 600 | 24,000 | 192 |
| **Goombah Guard** | 125 | 1 | 12 | 1 |
| **Boss Crystalys** | 393,750 | 1,050 | 63,000 | 273 |
| **Crystalys Guard** | 125 | 1 | 12 | 1 |

| 게이트 | 크레딧 | Thulium | 경험치 | 명예 |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 514,000 | 2,099 | 55,296 | 1,018 |
| **Beta Breach** | 1,298,500 | 5,939 | 187,744 | 2,470 |
| **Gamma Foundry** | 3,064,500 | 13,693 | 541,944 | 4,696 |
| **Delta Siege** | 5,239,625 | 22,338 | 882,676 | 7,850 |
| **Omega Vault** | 7,088,125 | 29,196 | 1,196,828 | 10,022 |

<!-- solo-kills:end -->

## 도전과 도전 과제 {#challenges-and-achievements}

선택 도전이 둘 있으며 어떤 클리어에서든 달성할 수 있습니다. 각각 도전 과제 하나를 지급하고 **Thulium은 지급하지 않습니다.** **무사망** 클리어는 다시 들어간 횟수를 모두 합쳐 런 전체에서 한 번도 죽지 않은 클리어입니다. **스피드런**은 게이트의 가장 짧은 계획 시간 안의 클리어이며 경기장 안에서 보낸 시간으로 셉니다. 나머지 여섯 개의 도전 과제는 각 게이트를 클리어한 것과 다섯 게이트 모두를 클리어한 것입니다.

<!-- solo-achievements:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **균열 봉인** (일반): Alpha Rift를 혼자서 클리어하세요.
- **돌파구 봉쇄** (고급): Beta Breach를 혼자서 클리어하세요.
- **주조소 가동 중단** (희귀): Gamma Foundry를 혼자서 클리어하세요.
- **포위 돌파** (희귀): Delta Siege를 혼자서 돌파하세요.
- **금고 해제** (영웅): Omega Vault를 혼자서 뚫으세요.
- **게이트 키퍼** (전설): 다섯 개의 솔로 게이트를 모두 클리어하세요: Alpha, Beta, Gamma, Delta, Omega.
- **무적** (희귀): 생명을 잃지 않고 솔로 게이트를 클리어하세요.
- **시간과의 싸움** (희귀): 가장 짧은 시간 이내에 솔로 게이트를 클리어하세요: Alpha부터 Omega까지 10, 15, 25, 35, 50분.

<!-- solo-achievements:end -->

## 게이트에서 나온 아이템 {#items-from-a-gate}

게이트가 주는 것은 **거래 가능**합니다. 광석, 플레이트, Power Core, 탄약, 외계인의 전리품은 드롭이나 퀘스트 보상처럼 [경매장](/wiki/03-Mechanics/Auction.md)에 등록할 수 있으며, 예외도 다른 아이템과 같습니다. 부품 없는 스핀의 상품은 해당되지 않습니다. 게이트가 아니라 스핀에서 나온 것이기 때문입니다.

## 게이트와 초기화 {#gates-and-the-wipe}

- **초기화는 열려 있는 모든 런을 끝내고** 그 부품을 돌려줍니다. 런은 다음 시즌으로 이어지지 않습니다.
- **초기화를 거쳐 유지되는 것:** 다섯 솔로 게이트의 부품, 보장의 횟수, 스핀에 쓴 양과 게이트가 돌려준 양의 기록이며, 그래서 Thulium 상한은 시즌을 넘어 이어집니다. 도전 과제는 영원히 당신의 것입니다.
- **초기화 때 사라지는 것:** Chrono-Gate의 부품은 전과 같습니다. 스핀으로 다시 얻습니다.
- **계정 삭제**는 부품, 횟수, 기록을 삭제합니다.
