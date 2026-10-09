<!-- wiki-i18n source: 2bd1925e336e25b6 -->
<!-- wiki-i18n title: 선체 장갑 -->
# 선체 장갑 {#hull-plating}

<!-- wiki-search: hull plate; hull plate slot; hull plate slots; plate slot; plate; armour; armor; hpl; 선체 장갑; 장갑 슬롯; 장갑판 -->

Dormant 무리를 연구한 결과 장갑 기술의 진전이 확인되었습니다. 이 기술로 함선은 선체를 강화할 수 있습니다. **선체 장갑**은 제작한 함선의 선체 플레이트 슬롯에 장착해 선체 포인트를 더해 주는 장갑입니다. [부스터](/wiki/06-Items/Boosters.md) 페이지의 Hull Plating **Booster**와는 다르며, 그쪽은 시간제 보너스입니다.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## 아이템 트리 {#item-tree}

어셈블리에서 만드는 것은 먼저 해당 기술이 필요합니다. 아이템에 마우스를 올리면 연구에 걸리는 시간을 볼 수 있습니다. 기술 트리, 연료, 부스트는 [연구](/wiki/03-Mechanics/Research.md)에 있습니다.

```tree
Hull Plating I | hull-plating, uncommon | buy 5000 Thulium | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating II | hull-plating, rare | craft 2500 Thulium, 300 s | research 86400 s, 86400 science, 25 Dark Matter | 1 Hull Plating I, 150 Ship Fragment, 20 Reinforced Hull Plate, 6 Power Core, 5 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating III | hull-plating, epic | craft 4000 Thulium, 600 s | research 172800 s, 172800 science, 40 Dark Matter | 1 Hull Plating II, 300 Ship Fragment, 40 Reinforced Hull Plate, 12 Power Core, 1 Ancient Control Unit, 8 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings

Hull Plating I => Hull Plating II => Hull Plating III
```
<!-- item-tree:end -->

## 세 가지 장갑 {#the-three-platings}

| 아이템 | 늘어나는 선체 | 얻는 방법 |
| :--- | ---: | :--- |
| **Hull Plating I** | 5,000 | 상점, 5,000 Thulium |
| **Hull Plating II** | 10,000 | 어셈블리, Hull Plating I에서 |
| **Hull Plating III** | 15,000 | 어셈블리, Hull Plating II에서 |

Hull Plating I은 구매합니다. **II와 III는 업그레이드입니다.** 어셈블리는 한 단계 아래 장갑 하나(인벤토리에 그냥 있는 것)를 소모하고, Thulium, 재료, **Dark Matter Plate**를 요구합니다. II는 5개, III는 8개로, 다른 장비의 마지막 티어가 요구하는 3개보다 많습니다. 둘 다 먼저 기술이 필요하며, [연구](/wiki/03-Mechanics/Research.md#tree-hull-plating) 페이지의 Hull Plating 트리에 있습니다. II는 1일과 Dark Matter 25개, III는 2일과 Dark Matter 40개가 들며, Dark Matter Plate 자체의 기술에 더해 필요합니다. 위의 트리에 가격, 재료, 시간이 나와 있습니다.

[대장간](/wiki/06-Items/Forge.md)은 모든 장갑을 다룹니다. 업그레이드하면 소모한 장갑의 단련 등급이 이어지고 보너스는 다시 굴려집니다. 장갑의 능력치는 선체 하나뿐이므로 보너스도 하나만 가지며, 등급에 따라 +2%에서 +15%입니다. 영원한 등급의 Hull Plating III는 최대 17,250을 더합니다. [경매장](/wiki/03-Mechanics/Auction.md)에는 Hull Plating II와 III를 올릴 수 있고, 상점에서 파는 Hull Plating I은 올릴 수 없습니다.

## 장갑 슬롯 {#hull-plate-slots}

선체 장갑은 **장갑 슬롯**에만 들어갑니다. 어셈블리에서 제작하는 네 함선이 레이저, 발전기, 부가 장비, 능력, 드론 슬롯에 더해 갖는 별도의 슬롯 종류입니다.

| 함선 | 장갑 슬롯 | Hull Plating III 한 벌이 더하는 선체 |
| :--- | ---: | ---: |
| **Paragon** | 5 | 75,000 |
| **Storm** | 7 | 105,000 |
| **Ironclad** | 15 | 225,000 |
| **Wraith** | 9 | 135,000 |

- **처음에는 모두 잠겨 있습니다.** 슬롯은 Skylab에서 연구하면 열립니다. 슬롯마다 기술이 하나이며, 1시간과 Dark Matter 10개로 첫 번째부터 순서대로 연구합니다. [연구](/wiki/03-Mechanics/Research.md#ship-technologies) 화면에서는 함선의 슬롯이 슬롯마다 점이 하나씩 붙은 카드 한 장으로 보입니다.
- **함선 한 척이 아니라 함선의 종류입니다.** Paragon을 위해 연 슬롯은 Paragon의 모든 디자인에서도 열려 있습니다([함선 디자인](/wiki/03-Mechanics/Ship-Designs.md)). 기술은 영구히 내 것입니다. 초기화 뒤에도 남습니다.
- **두 구성이 함께 씁니다.** 장갑은 함선에 속합니다. 구성을 바꿔도 그대로 끼워져 있으며, 격납고는 두 구성에서 같은 장갑을 보여 줍니다.
- **어떻게 섞어도 됩니다.** 슬롯에는 어떤 선체 장갑이든 들어가며, 같은 것 두 개도 괜찮습니다.
- **선체의 비율은 그대로입니다.** 장갑을 끼우거나 빼도 지금 가진 선체의 비율이 유지되므로, 장갑이 나를 치료하지도 해치지도 않습니다.
- **다른 장비와 마찬가지로** 장갑은 격납고에서, 또는 안전 지대 안에서 격납고 창으로 끼우고 뺍니다. 필드에서는 할 수 없습니다. 연구하지 않은 슬롯은 장갑을 받지 않습니다.

격납고에서는 **선체 장갑** 카드가 슬롯을 보여 줍니다. 열린 슬롯에는 다른 슬롯과 마찬가지로 드래그 앤 드롭으로 장갑을 넣고, 잠긴 슬롯에는 자물쇠가 표시되며 클릭하면 Skylab의 연구가 열립니다. 다른 능력치 옆의 타일은 끼운 장갑이 주는 합계를 보여 줍니다.

## 선체가 합쳐지는 방식 {#how-the-hull-adds-up}

장갑은 함선 자체의 선체에 자기 선체를 더하며, 격납고와 함선 창에는 더 큰 수치가 표시됩니다. 함선의 선체와 장갑을 합한 값은 전과 같은 배율을 거칩니다. [Hull Plating Booster](/wiki/06-Items/Boosters.md)와 착용 중인 [드론 편대](/wiki/03-Mechanics/Formations.md)입니다. 선체를 바꾸는 디자인(BUCKY는 25% 더 많습니다)은 함선 자체의 선체를 바꾸며, 장갑은 그 위에 더해집니다.

## Hull Plating과 Hull Plating Booster {#hull-plating-or-booster}

같은 이름을 쓰는 것이 둘 있습니다. **선체 장갑**(이 페이지)은 장갑입니다. 제작한 함선의 장갑 슬롯에 들어가는 판이며, 끼워져 있는 동안 자기 선체를 더합니다. **Hull Plating Booster**는 [부스터](/wiki/06-Items/Boosters.md) 페이지의 시간제 보너스로, 조종 중인 함선에 10시간 동안 최대 체력 +10%를 주며 끼울 것은 없습니다. 둘은 겹쳐 적용됩니다. 장갑이 먼저 더해지고, Booster의 10%는 그 합계에 붙습니다.
