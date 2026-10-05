<!-- wiki-i18n source: 06696a3c765a00c4 -->
<!-- wiki-i18n title: Щиты -->
# Щиты и защита {#shields-defense}

Защитные модули дают ёмкость щита, поглощают урон и восстанавливают вашу защиту.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Дерево предметов {#item-tree}

То, что создаёт Сборочный цех, сначала требует своей технологии; наведите курсор на предмет, чтобы увидеть, сколько длится её исследование. Дерево технологий, топливо и буст: [Исследования](/wiki/03-Mechanics/Research.md).

```tree
Light Shield Core | shield, shoddy | buy 20000 Credits | /wiki/06-Items/Shields.md#shield-cores
Basic Shield Core | shield, common | buy 2000 Thulium | /wiki/06-Items/Shields.md#shield-cores
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cores
Adaptive Core I | hybrid-generator, shoddy | buy 100000 Credits | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core II | hybrid-generator, common | buy 4000 Thulium | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core III | hybrid-generator, rare | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Absorption Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells

Light Shield Core -> Basic Shield Core => Heavy Shield Core
Adaptive Core I -> Adaptive Core II -> Adaptive Core III
Absorption Shield Cell I => Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell I => Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```
<!-- item-tree:end -->

## Щиты {#shield-cores}

Устанавливайте щиты, чтобы создавать активные защитные барьеры, в слоты генераторов вашего корабля или на ваших [дронах](/wiki/03-Mechanics/Drones.md) (слот дрона считается основным слотом). Учтите, что тяжёлые щиты снижают вашу скорость. Щит в **слоте способности** вместо этого даёт вам **Shield Surge** из колонки «Особый эффект» — восстановление щита в течение десяти секунд — и сам защиты не добавляет (см. [Способности](/wiki/03-Mechanics/Abilities.md)).

| Название | Редкость | Ёмкость | Восстановление | Поглощение | Щит, % | Скорость, % | Слоты ячеек | Особый эффект | Цена |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Light Shield Core** | Ветхий | 10 000 | 333/с | 45% | +5% | -1% | 1 | Shield Surge I | 20 000 кредитов |
| **Basic Shield Core** | Обычный | 15 000 | 500/с | 48% | +10% | -3% | 2 | Shield Surge II | 2 000 Thulium |
| **Heavy Shield Core** | Редкий | 25 000 | 833/с | 50% | +20% | -5% | 3 | Shield Surge III | Только крафт |

**Heavy Shield Core** создаётся в [Сборочном цехе](/wiki/06-Items/Overview.md#upgrading-modules) из Basic Shield Core за 2 000 Thulium, 20 Cataclysite, 8 Reinforced Hull Plate и 6 Velkonite Reinforced Plate из вашего Skylab. Он сохраняет уровень зачарования израсходованного щита, а его бонусы выпадают заново ([Улучшение модулей](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Сначала снимите Basic Shield Core с корабля (и извлеките из него ячейки): щит, который установлен или в который вложены ячейки, не расходуется.

**Поглощение** — это доля каждого попадания, которую принимают ваши щиты; остальное получает корпус. Сам по себе щит даёт **от 45 до 50%**, а остальное добавляют его ячейки: лучший щит с лучшими ячейками (Heavy Shield Core с тремя ячейками Absorption Shield Cell IV) даёт **80%** — это максимум, который есть у корабля без дополнительных усилений. Сверх этого добавляют два постоянных бонуса: Shield Absorbance Boost из магазина сезона (+0,1 пункта за уровень, 100 уровней, по 25 очков вайпа каждый) и бонусы поглощения из Кузницы. Нынешние источники очков вайпа (855 в сумме при предельных значениях, переносятся через вайпы; новые источники запланированы) покупают 34 из этих 100 уровней (+3,4 пункта), что вместе с полностью выкованным комплектом уровня «Вечный» даёт около **95%**. Но значение не ограничено 100%: *пробитие щита* атакующего вычитается из него, поэтому всё, что у корабля выше 100%, — запас против пробития. См. [Механика щитов](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-).

---

## Гибридные генераторы (адаптивные ядра) {#hybrid-generators-adaptive-cores-}

Адаптивные ядра работают как гибридные генераторы, сочетая возможности щита и двигателя. В их слоты можно вкладывать и ускорители, и ячейки щита (по одному модулю на слот, любого из двух видов). Их бонусы щита и скорости учитываются так же, как у щита или двигателя (четыре лучших, умноженные на долю слота). У них нет поглощения: они не меняют поглощение вашего корабля, а ячейки в них добавляют только ёмкость и восстановление. Долю попадания принимают только щиты, поэтому для ячеек в адаптивном ядре на корабле нужен ещё и щит.

| Название | Редкость | Бонус щита, % | Бонус скорости, % | Слоты | Особый эффект | Цена |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **Adaptive Core I** | Ветхий | +5% | +3% | 1 | — | 100 000 кредитов |
| **Adaptive Core II** | Обычный | +8% | +4% | 2 | — | 4 000 Thulium |
| **Adaptive Core III** | Редкий | +15% | +5% | 3 | — | Только крафт |

---

## Ячейки щита {#shield-cells}

Ячейки щита вкладываются в щиты или адаптивные ядра (столько, сколько у ядра слотов), чтобы усилить это ядро. В щите они повышают и его поглощение — в пунктах, а с ним и долю каждого попадания, которую принимают ваши щиты. Существует два семейства по четыре ступени: ячейки **Capacity Shield Cell** дают больше всего щита и восстановления, ячейки **Absorption Shield Cell** — больше всего поглощения (на каждой ступени вдвое больше поглощения и вдвое меньше щита и восстановления, чем у Capacity той же ступени). Capacity помогает кораблю, у которого исход боя решает щит, Absorption — кораблю, у которого его решает корпус. Если все слоты ядра заполнены одинаковыми ячейками, то Light Shield Core (1 слот) даёт от 47 до 55%, Basic Shield Core (2 слота) — от 52 до 68%, а Heavy Shield Core (3 слота) — от 56 до 80%, от ячеек Capacity ступени I до ячеек Absorption ступени IV. Если снять ядро или израсходовать его как донора при объединении в [Кузнице](/wiki/06-Items/Forge.md), его ячейки возвращаются в инвентарь.

| Название | Редкость | Бонус к ёмкости | Бонус восстановления | Бонус к поглощению | Цена |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Capacity Shield Cell I** | Ветхий | +3 000 | +250/с | +2% | 30 000 кредитов |
| **Capacity Shield Cell II** | Обычный | +6 000 | +500/с | +3% | Только крафт |
| **Capacity Shield Cell III** | Редкий | +9 000 | +750/с | +4% | Только крафт |
| **Capacity Shield Cell IV** | Эпический | +12 000 | +1 000/с | +5% | Только крафт |
| **Absorption Shield Cell I** | Ветхий | +1 500 | +125/с | +4% | 30 000 кредитов |
| **Absorption Shield Cell II** | Обычный | +3 000 | +250/с | +6% | Только крафт |
| **Absorption Shield Cell III** | Редкий | +4 500 | +375/с | +8% | Только крафт |
| **Absorption Shield Cell IV** | Эпический | +6 000 | +500/с | +10% | Только крафт |

Ступень I каждого семейства продаётся за 30 000 кредитов. Ступени II–IV создаются в [Сборочном цехе](/wiki/06-Items/Overview.md#upgrading-modules), каждая из ячейки того же семейства ступенью ниже (Capacity Shield Cell II из Capacity Shield Cell I, III из II, IV из III) за Thulium, добычу с пришельцев и Velkonite Reinforced Plate из вашего Skylab (2, 4 и 6 пластин). Ячейка никогда не меняет семейство: Capacity или Absorption вы выбираете, когда покупаете ступень I. Новая ячейка сохраняет уровень зачарования израсходованной ячейки, а её бонусы выпадают заново ([Улучшение модулей](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Ячейки не подходят для [слота способности](/wiki/03-Mechanics/Abilities.md): их место — внутри щитов и адаптивных ядер.
