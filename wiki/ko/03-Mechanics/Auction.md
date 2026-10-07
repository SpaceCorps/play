<!-- wiki-i18n source: d2b36e0a1271e933 -->
<!-- wiki-i18n title: 경매장 -->
# 경매장 {#auction}

경매장은 파일럿들의 시장이자 게임이 직접 여는 매시간의 로트를 정거장 메뉴의 한 페이지에 모은 곳입니다. 상점처럼 정거장의 페이지이므로 도킹한 상태에서 사용하며, 비행 중에는 쓸 수 없습니다. 네 부분이 있습니다. **시장**은 다른 파일럿들이 팔고 있는 것입니다. **로트**는 게임이 직접 내놓는 물건으로, 매시간 하나씩입니다. **내 등록**은 내가 직접 팔고 있는 것입니다. **내역**은 나의 판매, 구매, 낙찰받은 로트, 그리고 거래 성과입니다.

<!-- market-glance:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- 경매장에서 등록, 구매, 입찰을 하려면 **레벨 5** 이상이어야 합니다.
- 등록 가격은 묶음 하나당, 정수 크레딧이나 정수 Thulium 중 하나로 정하며(둘 다는 안 됩니다), 그 아이템의 최저 가격 아래로는 내려갈 수 없습니다. **최고 가격은 없습니다.**
- Thulium 가격은 크레딧 최저 가격을 환율(1,000 크레딧당 1 Thulium)로 나누어 올림한 값 이상이어야 하며, 최저 가격이 20 Thulium 이상이 되는 아이템에만 적용됩니다. 환율이 하는 일은 그것뿐입니다. **1 Thulium = 1,000 크레딧은 최저 가격을 정하는 규칙일 뿐 환율이 아닙니다.** 아무것도 교환되지 않고, 가치도 표시되지 않으며, 크레딧과 Thulium은 절대 합산되지 않습니다.
- 80종류를 등록할 수 있고, 그중 42종류는 Thulium으로도 가격을 정할 수 있습니다.
- 등록 기간은 24 / 72 / 168시간 중에서 고를 수 있으며, 선택지는 모든 레벨에서 같습니다.
- **보증금**은 등록이 진행되는 24시간마다 가격의 1%이며, 최소 50 크레딧 또는 1 Thulium입니다. 등록할 때 내며, 등록을 취소해도 돌려받지 못합니다.
- 레벨 10부터는 보증금이 1.5%입니다.
- **세금**은 가격의 5%입니다. 등록이 팔렸을 때 판매자가 받는 금액에서 차감됩니다.
- 보증금과 세금은 소멸됩니다. 누구에게도 가지 않습니다.
- 시즌 28일차부터 초기화까지는 보증금도 세금도 없습니다.
- 시즌 30일차부터는 새 시즌이 시작될 때까지 경매장이 닫힙니다. 등록, 구매, 입찰은 할 수 없지만, 자신의 등록은 취소할 수 있습니다.
- 통화마다 따로 24시간 동안 팔 수 있는 양과 살 수 있는 양의 한도가 있습니다(아래 레벨 표). 로트 낙찰은 포함되지 않습니다.
- 두 파일럿 사이에서(한쪽이 다른 쪽에서 구매할 때) 24시간 동안 오갈 수 있는 양은 최대 8,000,000 크레딧 또는 40,000 Thulium입니다.

<!-- market-glance:end -->

## 거래 가능한 아이템 {#marketable-items}

팔 수 있는 것은 **직접 얻은** 아이템뿐입니다. 얻은 것에는 모두 [격납고](/wiki/03-Mechanics/Inventory.md#marketable-items)에서 작은 **거래 가능** 표시가 붙습니다. 우주에서 주운 것(에일리언, 무리, Warden, 블랙홀의 드롭: [화물](/wiki/03-Mechanics/Cargo.md)), 미션이 지급하는 것([퀘스트](/wiki/03-Mechanics/Quests.md#rewards)), 그리고 어셈블리와 대장간이 만든 모든 것이 그렇습니다. 상점에서 **구매한** 것, 로트에서 낙찰받은 것, 시장에서 산 것, 보너스 코드·초대 패키지·스타터 키트로 받은 것, 환불로 돌려받은 것은 거래 가능이 아니며 다시는 팔 수 없습니다. 그래서 되팔려고만 사는 일이 없습니다. Skylab의 단조소가 만드는 플레이트도 거래 가능이 아니지만, 미션이 지급하는 Reinforced Plate는 거래 가능합니다.

표시는 스위치가 아니라 유닛 수입니다. 탄약 묶음에는 산 것과 얻은 것이 섞여 있을 수 있고, 카드에는 “거래 가능 (3/5)”라고 나옵니다. 묶음의 일부를 쓸 때(발사, 제작)는 일반 유닛이 먼저 줄어들어 거래 가능한 것이 가장 오래 남습니다. [대장간](/wiki/06-Items/Forge.md#merge)에서 두 품목을 병합하면 두 품목 모두 표시가 있었을 때만 표시가 남고, 미리 보기가 그렇게 알려 줍니다. 실패한 대장간 단계는 재료를 일반 유닛으로 돌려줍니다.

격납고의 **거래 가능한 것만** 칩은 팔 수 있는 것만 보여 주고, 표시가 붙은 아이템의 휴지통 옆 **망치**는 그 아이템의 경매장 판매 창을 엽니다. 어셈블리에서는 결과물이 거래 가능한 레시피에 그렇게 표시되고, 부족한 재료에는 그 이름을 검색창에 넣어 경매장을 여는 링크가 있습니다.

경매장이 생겼을 때(0.4.12), 이미 가지고 있던 상점에서 팔지 않는 장비와 자원에는 한 번 표시가 붙었습니다. 다음은 붙지 않았습니다. 상점이 한때 팔았거나, 가진 것에 산 것과 얻은 것이 섞여 있기 때문입니다. Quantum Laser 3, Absorption Shield Cell II와 III, Impulse Thruster II와 III, 두 종류의 Reinforced Plate, 그리고 파일럿마다 가장 오래된 Base CPU I(스타터 키트의 것)입니다. 이것들을 새로 얻거나 제작한 것에는 표시가 붙습니다.

## 팔 수 있는 것 {#what-can-be-sold}

<!-- market-kinds:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| 종류 | 판매할 수 있는 아이템 | 개수 |
| :--- | :--- | ---: |
| **레이저** | Quantum Laser 1, Quantum Laser 2, Quantum Laser 3, Starfire-3, Helios Beam | 5 |
| **레이저 증폭기** | Damage Amp I, Crit Amp I, Penetration Amp I, Damage Amp II, Crit Amp II, Penetration Amp II, Damage Amp III, Crit Amp III, Penetration Amp III, Damage Amp IV, Crit Amp IV, Penetration Amp IV | 12 |
| **실드 코어** | Light Shield Core, Basic Shield Core, Heavy Shield Core | 3 |
| **엔진** | Engine I, Engine II, Engine III | 3 |
| **Adaptive Core** | Adaptive Core I, Adaptive Core II, Adaptive Core III | 3 |
| **실드 셀** | Absorption Shield Cell I, Capacity Shield Cell I, Absorption Shield Cell II, Capacity Shield Cell II, Absorption Shield Cell III, Capacity Shield Cell III, Absorption Shield Cell IV, Capacity Shield Cell IV | 8 |
| **추진기** | Impulse Thruster I, Momentum Thruster I, Impulse Thruster II, Momentum Thruster II, Impulse Thruster III, Momentum Thruster III, Impulse Thruster IV, Momentum Thruster IV | 8 |
| **레이저 탄약** | Standard Battery (100개 묶음), Siphon Battery (10개 묶음), Advanced Plasma (10개 묶음), Ultra Core (10개 묶음), Experimental Fusion Core | 5 |
| **로켓** | Ember I, Lancet I, Rivet I, Scatter I, Ember II, Lancet II, Rivet II, Scatter II, Ember III, Lancet III, Rivet III, Scatter III | 12 |
| **부가 장비** | Repair Drone I, Repair Drone II, Repair Drone III, EMP Charge, Repair Drone IV, Cloaking CPU S, Base CPU I, Cloaking CPU M, Auto-Repair CPU, Cloaking CPU L, Base CPU II | 11 |
| **자원** | Cataclysite (100개 묶음), Ship Fragment (100개 묶음), Daraxium (100개 묶음), Nyxite (100개 묶음), Quorvium (10개 묶음), Reinforced Hull Plate (10개 묶음), Power Core, Velkonite Reinforced Plate, Dark Matter, Orvium Reinforced Plate | 10 |

<!-- market-kinds:end -->

함선, 드론, 드론 포메이션, 부스터, 구독은 팔 수 없고, Ancient Control Unit, 광석인 Velkonite와 Orvium, Dark Matter Plate, Jump CPU, Extra Slots CPU, N.U.K.E., N.I.K.E.도 팔 수 없습니다. Dark Matter Plate는 상품으로도 가격으로도 경매장에 전혀 나오지 않습니다. 장착 중인 아이템, 다른 아이템에 끼워진 아이템, 모듈이 들어 있는 아이템, [수송 보관함](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-)에 있는 아이템은 등록할 수 없고, 사용한 Cloaking CPU, EMP Charge, Base CPU도 등록할 수 없습니다. 탄약과 로켓은 정거장에서 팝니다. 먼저 기체를 착륙시키세요.

## 판매 {#selling}

**아이템 판매**를 누르고(또는 격납고의 망치를 누르고), 얻은 것을 고르고(카테고리 드롭다운으로 목록을 좁힐 수 있으며, 카테고리는 시장과 같습니다), 크레딧이나 Thulium을 고르고, 묶음 하나의 가격과 등록 기간(1일, 3일, 7일)을 정합니다. 창에는 최저 가격, 가격을 채워 주는 세 칩(**최저가**, 지금 가장 싼 등록보다 하나 낮은 **빠른 판매**, 마지막 판매 가격인 **적정가**), 그리고 등록하기 전에 보증금, 세금, 받는 금액이 표시됩니다. 가격 아래의 **비슷한 등록**은 고른 통화로 같은 아이템과 같은 인챈트가 지금 얼마에 올라와 있는지를 그래프로 보여 줍니다. 내 가격은 선으로 표시되고, 최저 가격, 마지막 판매, 상점 가격에 표시가 붙으며, 내 가격이 어디쯤 놓일지 말로 알려 주는 한 줄과 가장 싼 등록 세 개도 나옵니다. 한 점은 한 묶음입니다. 탄약과 일부 자원은 10개나 100개 묶음으로 팔며, 정수 개의 묶음을 팝니다. 등록한 것은 인벤토리를 떠나 팔리거나, 취소하거나, 기간이 끝날 때까지 서버가 보관하고, 그 뒤에는 표시를 단 채 돌아옵니다. 언제든 취소할 수 있으며 시즌의 마지막 며칠에도 마찬가지입니다. 등록은 스냅샷입니다. 가격을 바꾸려면 등록을 취소하고 다시 등록하세요(보증금은 다시 냅니다).

모든 아이템에는 **최저 가격**이 있지만 **최고 가격은 없습니다**. 원하는 만큼 부르세요. 표는 몇몇 아이템의 최저 가격입니다.

<!-- market-bands:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| 아이템 | 묶음 크기 | 최저 가격, 크레딧 | 최저 가격, Thulium |
| :--- | ---: | ---: | ---: |
| Quantum Laser 2 | 1 | 32,000 | 32 |
| Quantum Laser 3 | 1 | 170,000 | 170 |
| Helios Beam | 1 | 1,600,000 | 1,600 |
| Absorption Shield Cell IV | 1 | 1,100,000 | 1,100 |
| Heavy Shield Core | 1 | 870,000 | 870 |
| Impulse Thruster IV | 1 | 980,000 | 980 |
| EMP Charge | 1 | 40,000 | 40 |
| Cloaking CPU S | 1 | 400,000 | 400 |
| Ultra Core | 10 | 800 | 크레딧만 |
| Lancet I | 1 | 200 | 크레딧만 |
| Ship Fragment | 100 | 600 | 크레딧만 |
| Dark Matter | 1 | 33,000 | 33 |

<!-- market-bands:end -->

Thulium 가격에는 규칙이 하나뿐입니다. 크레딧 최저 가격을 환율로 나누어 올림한 값입니다. 환율은 게임이 Thulium에 매긴 가치가 아닙니다. Thulium 최저 가격을 계산하는 방법일 뿐이며, 그래서 Thulium을 가진 파일럿에게는 Thulium 등록이 쌀 수 있습니다. 대부분의 판매자는 크레딧을 부를 것입니다. 싼 아이템(탄약, 로켓, 대부분 장비의 첫 단계, 흔한 자원)은 Thulium 하나가 너무 큰 단위이므로 크레딧으로만 가격을 정합니다.

**열린 등록**(과 관리자가 보류한 등록)은 칸을 차지합니다. 레벨이 오르면 칸이 최대치까지 늘고, 하루에 더 많이 팔고 살 수 있습니다. 등록을 얼마나 오래 둘 수 있는지는 모든 레벨에서 같습니다.

<!-- market-limits:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| 레벨 | 열린 등록 | 가장 긴 등록 기간 | 하루, 크레딧 | 하루, Thulium | 24시간당 보증금 |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 5 | 20 | 168시간 | 4,500,000 | 22,500 | 1% |
| 6 | 40 | 168시간 | 6,000,000 | 30,000 | 1% |
| 7 | 70 | 168시간 | 7,500,000 | 37,500 | 1% |
| 8 | 100 | 168시간 | 8,500,000 | 42,500 | 1% |
| 9 | 100 | 168시간 | 10,000,000 | 50,000 | 1% |
| 10 | 100 | 168시간 | 15,000,000 | 75,000 | 1.5% |
| 11 | 100 | 168시간 | 15,000,000 | 75,000 | 1.5% |
| 12 | 100 | 168시간 | 15,000,000 | 75,000 | 1.5% |
| 13 | 100 | 168시간 | 20,000,000 | 100,000 | 1.5% |
| 14 | 100 | 168시간 | 20,000,000 | 100,000 | 1.5% |
| 15 | 100 | 168시간 | 20,000,000 | 100,000 | 1.5% |
| 16 | 100 | 168시간 | 20,000,000 | 100,000 | 1.5% |
| 17 | 100 | 168시간 | 20,000,000 | 100,000 | 1.5% |
| 18 | 100 | 168시간 | 20,000,000 | 100,000 | 1.5% |
| 19 | 100 | 168시간 | 20,000,000 | 100,000 | 1.5% |
| 20 이상 | 100 | 168시간 | 20,000,000 | 100,000 | 1.5% |

<!-- market-limits:end -->

## 수수료 {#fees}

등록에는 등록할 때 내고 돌려받지 못하는 **보증금**이 들고, 판매에는 판매자가 받는 금액에서 차감되는 **세금**이 듭니다. 둘 다 등록의 통화로 내며 **소멸됩니다**. 누구에게도 가지 않으므로 자기 자신과 거래해서 이득을 보는 사람은 없습니다. 시즌의 마지막 이틀에는 보증금도 세금도 없습니다.

<!-- market-fees:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| 등록 | 가격 | 보증금 | 세금 | 판매자가 받는 금액 |
| :--- | ---: | ---: | ---: | ---: |
| Quantum Laser 3: 레벨 6, 24시간 | 170,000 크레딧 | 1,700 크레딧 | 8,500 크레딧 | 161,500 크레딧 |
| Quantum Laser 3: 레벨 10, 72시간 | 170 Thulium | 8 Thulium | 8 Thulium | 162 Thulium |
| Helios Beam: 레벨 12, 168시간 | 2,500,000 크레딧 | 262,500 크레딧 | 125,000 크레딧 | 2,375,000 크레딧 |
| Helios Beam: 레벨 12, 168시간, 시즌 마지막 며칠 | 2,500,000 크레딧 | 0 크레딧 | 0 크레딧 | 2,500,000 크레딧 |

<!-- market-fees:end -->

## 구매 {#buying}

**시장**에는 다른 파일럿들이 파는 것이 보입니다. **카테고리 칩**(아이템 종류마다 하나씩이며, 들어 있는 등록 수가 붙습니다)으로 목록을 좁히고, 이름으로 검색하고, 인챈트와 통화로 거르고, 가격순, 곧 끝나는 순, 최신순으로 정렬합니다. 등록을 고르면 그것이 무엇인지, 누가 파는지, 언제까지인지, 그리고 가격이 마지막 판매, 지금의 최저가, 상점 가격과 비교해 어떤지 볼 수 있습니다. 묶음은 정수 개의 묶음 단위로 삽니다. 큰 구매는 한 번 더 확인을 묻습니다. 판매자는 세금을 뺀 금액을 즉시 받습니다. 구매자는 보증금도 세금도 내지 않습니다. 산 것은 **거래 가능이 아닙니다**. 팔 수 있는 것은 직접 얻은 것뿐이라서, 페이지는 **구매** 버튼 옆에 “받는 것: 거래 불가”라고 표시합니다. 자신의 등록은 살 수 없습니다. 보고 있는 동안 팔린 등록은 “그 등록은 더 이상 없습니다.”라고 알려 줍니다.

## 한도 {#limits}

통화마다 따로 하루에 팔 수 있는 양과 살 수 있는 양의 한도가 있고 최근 24시간으로 셉니다. 두 파일럿 사이에 오가는 양에도 한도가 있어서, 보조 계정으로 큰돈을 빠르게 옮길 수 없습니다. 크레딧과 Thulium은 절대 합산되지 않습니다. Thulium으로 판 사람이 쓰는 것은 Thulium 한도뿐입니다. 판매 창은 판매가 하루 판매 한도를 넘을 때 경고하고, 구매가 하루 구매 한도를 넘을 때는 시장이 그렇게 알려 주며 **구매** 버튼을 막아 둡니다. 한도는 레벨과 함께 늘고, 프리미엄은 어느 것도 바꾸지 않습니다. 로트 낙찰은 포함되지 않습니다.

등록 중인 로켓, 선두에 서 있는 로트의 로켓, 가지고 있는 로켓은 모두 한 로켓을 가질 수 있는 최대 수에 포함됩니다. 등록을 이용해 상점의 묶음이 허용하는 것보다 많이 가질 수는 없습니다.

## 내 등록과 내역 {#my-listings-and-history}

**내 등록**에는 칸과 각 등록이 상태(열림, 판매됨, 취소됨, 만료됨, 반환됨, 보류 중)와 함께 표시되며, **취소** 버튼, 끝난 등록의 **다시 등록**, 같은 아이템의 다른 등록이 더 싸게 나와 있을 때의 **더 저렴한 등록 있음** 칩이 있습니다. 만료된 등록은 저절로 인벤토리로 돌아옵니다. **내역**은 최근 30일의 거래로 시작합니다. 판매와 구매, 수입과 지출, 낸 수수료와 세금, 순이익, 최고 판매, 평균 판매가, 가장 많이 거래한 아이템과 함께 하루 수입과 지금까지의 결과를 보여 주는 꺾은선 그래프 두 개가 나옵니다(크레딧과 Thulium은 하나씩 봅니다). 그 아래에 팔고, 사고, 낙찰받은 것의 목록이 세금과 함께 나옵니다. 게임은 경매장의 장부를 90일 동안 보관합니다.

무언가 팔리면 알림(토스트), 경매장 소리, 새 잔액으로 알려 주며, 페이지가 닫혀 있는 동안에는 경매장 항목에 배지가 붙습니다. 연달아 팔려도 알림은 하나입니다. 경매장에는 전용의 조용한 소리가 있어서, 그곳에서 하는 일이나 일어나는 일마다(등록, 종료, 판매, 입찰, 밀림, 낙찰) 하나씩 울리며 인터페이스 볼륨을 따릅니다.

## 매시간의 로트 {#the-hourly-lots}

로트는 게임이 직접 내놓는 물건으로, 탄약, 로켓, EMP Charge를 매시간 입찰로 팝니다. 상점보다 싸게 탄약을 구하는 방법이자, 낙찰가가 소멸되므로 싱크이기도 합니다. 아래 하루 표에 있는 로트만 열립니다(x1이나 x4 탄약, Siphon Battery, 특수 로켓은 절대 나오지 않습니다). 통화는 상점의 것입니다. 로켓 로트는 그 로켓을 가질 수 있는 최대 수(상점의 묶음)를 넘지 않으며, 넘게 되는 입찰은 거절됩니다. 그러니 그 로켓을 적게 가지고 있을 때 로켓 로트에 입찰하세요.

<!-- market-lots:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- UTC 정시마다 새 로트가 열리고 4시간 동안 열려 있어서, 동시에 4개가 열려 있습니다.
- 시작가는 상품의 상점 가격의 40%입니다. 이후 입찰은 최고 입찰가보다 5% 이상 높아야 하고, 100 크레딧 또는 1 Thulium 이상 더 많아야 합니다.
- 입찰금은 즉시 지불되고 보관됩니다. 누군가 더 높게 부르면 즉시 돌려받습니다.
- 로트 종료 전 마지막 2분 안에 입찰하면 종료가 입찰 2분 뒤로 미뤄지며, 최대 5번까지입니다.
- 낙찰받은 것은 비행을 위한 것이지 거래를 위한 것이 아닙니다. 절대 거래 가능이 되지 않습니다. 낙찰가는 소멸됩니다. 아무도 입찰하지 않은 로트는 팔리지 않고, 누구에게도 비용이 들지 않습니다.
- 로트의 크기는 최근 3일 안에 경매장을 본 레벨 5 이상 파일럿 수에 따릅니다. 한 명도 없으면 표 크기의 10%, 30명 이상이면 전체 크기이며, 단위는 탄약 500, 로켓 50, EMP Charge 1입니다.
- 시즌의 마지막 6시간에는 로트가 만들어지지 않습니다. 초기화 때 아직 열린 로트는 취소되고 모든 입찰금이 반환됩니다.

<!-- market-lots:end -->

<!-- market-day:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| UTC 시각 | 로트 | 전체 크기 | 지불 통화 | 전체 크기일 때 시작가 |
| :--- | :--- | ---: | :--- | ---: |
| 00:00 | Scatter III | 1,250 | Thulium | 2,500 Thulium |
| 01:00 | Advanced Plasma | 25,000 | Thulium | 5,000 Thulium |
| 02:00 | Lancet I | 12,500 | 크레딧 | 2,500,000 크레딧 |
| 03:00 | EMP Charge | 5 | Thulium | 1,000 Thulium |
| 04:00 | Ultra Core | 25,000 | Thulium | 10,000 Thulium |
| 05:00 | Rivet II | 5,000 | 크레딧 | 1,600,000 크레딧 |
| 06:00 | Advanced Plasma | 10,000 | Thulium | 2,000 Thulium |
| 07:00 | Advanced Plasma | 50,000 | Thulium | 10,000 Thulium |
| 08:00 | Ember I | 12,500 | 크레딧 | 2,500,000 크레딧 |
| 09:00 | Ultra Core | 50,000 | Thulium | 20,000 Thulium |
| 10:00 | Scatter II | 5,000 | 크레딧 | 1,600,000 크레딧 |
| 11:00 | EMP Charge | 5 | Thulium | 1,000 Thulium |
| 12:00 | Advanced Plasma | 50,000 | Thulium | 10,000 Thulium |
| 13:00 | Lancet III | 1,250 | Thulium | 2,500 Thulium |
| 14:00 | Ultra Core | 10,000 | Thulium | 4,000 Thulium |
| 15:00 | Advanced Plasma | 25,000 | Thulium | 5,000 Thulium |
| 16:00 | Ultra Core | 50,000 | Thulium | 20,000 Thulium |
| 17:00 | Rivet I | 12,500 | 크레딧 | 2,500,000 크레딧 |
| 18:00 | Advanced Plasma | 50,000 | Thulium | 10,000 Thulium |
| 19:00 | Ember II | 5,000 | 크레딧 | 1,600,000 크레딧 |
| 20:00 | Ultra Core | 25,000 | Thulium | 10,000 Thulium |
| 21:00 | Advanced Plasma | 25,000 | Thulium | 5,000 Thulium |
| 22:00 | Advanced Plasma | 10,000 | Thulium | 2,000 Thulium |
| 23:00 | EMP Charge | 5 | Thulium | 1,000 Thulium |

<!-- market-day:end -->

경매장을 쓰는 파일럿이 적을 때는 로트도 작아서, 소수의 파일럿에게 매시간 수천 발의 탄약이 제시되는 일은 없습니다. 보는 파일럿이 늘수록 커집니다.

## 시즌과 초기화 {#the-season-and-the-wipe}

경매장은 시즌을 따릅니다([초기화 일정](/wiki/03-Mechanics/Wipe-Timeline.md) 참조). 마지막 이틀에는 수수료가 없습니다. 30일차, 초기화의 5분 카운트다운이 시작될 때부터는 닫혀서 등록, 구매, 입찰이 안 되고, 그때 끝나는 로트는 취소되어 입찰금이 반환되며, 자신의 등록은 여전히 취소할 수 있습니다. 등록은 시즌이 끝나는 시점을 넘겨 이어지지 않습니다.

초기화 때 **열려 있는 모든 등록은 판매자에게 돌아와** 낱개 아이템이 되고, 초기화는 그 뒤에 낱개 아이템을 다른 것과 똑같이 지웁니다(남는 것은 [수송 보관함](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-)에 넣은 것뿐입니다). 그러니 간직하고 싶은 것은 팔거나, 취소하고 보관함에 넣으세요. 아직 열려 있는 로트는 취소되고 입찰금은 반환됩니다. 크레딧과 Thulium은 초기화되지 않습니다.

## 경매장이 주지 않는 것 {#what-the-auction-does-not-give-you}

경매장은 직접 얻은 것을 거래하는 곳이며, 그 한계에 대해서도 솔직합니다.

- **드롭을 파는 것은 노가다가 아닙니다.** 에일리언의 원본 드롭은 자원뿐이며, 같은 레벨 5 사냥 한 시간이 처치로 지급하는 양의 0.4~0.9퍼센트의 가치밖에 없습니다. 새 파일럿에게 시장이 주는 것은 미션이 지급하지만 필요 없는 장비(한 번뿐), 도전 미션의 자원, 무리 보스의 상자, 그리고 직접 만든 것입니다.
- **딜러는 없습니다.** 파일럿이 무엇을 얼마에 사고 싶은지 밝히는 구매 주문은 이 버전에 없습니다. 그때까지 상인은 재료를 사서 어셈블리에서 장비를 만들어 파는 장인과, 초기화를 넘겨 수송 보관함에 재고를 두는 창고 파일럿뿐입니다.
- **상점의 장비는 되팔라고 있는 것이 아닙니다.** 상점에서 구매한 장비는 다시 팔 수 없습니다. Quantum Laser 1과 2, Light와 Basic Shield Core, Engine I과 II, 셀과 추진기의 첫 단계, 상점이 파는 증폭기, 구매한 탄약이 여기에 들어갑니다. 파일럿이 가질 수 있는 거래 가능한 Quantum Laser 2는 미션이 한 번 지급하는 그 하나뿐입니다.
- **플레이트는 미션에서 나옵니다.** 시장에 나오는 Velkonite와 Orvium Reinforced Plate는 도전 미션이 지급하는 것입니다. 단조소의 플레이트는 제외됩니다. 포함하면 시장 최대의 상품이 되기 때문입니다.

등록이 이상해 보이면 평소 방법대로 신고하세요. 게임 관리자는 등록을 보류하거나, 반환하거나, 경매장을 일시 중지하거나, 파일럿의 이용을 금지할 수 있으며, 그런 조치는 모두 기록됩니다.
