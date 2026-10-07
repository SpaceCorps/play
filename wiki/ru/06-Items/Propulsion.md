<!-- wiki-i18n source: 201734b1f19e2346 -->
<!-- wiki-i18n title: Двигательные системы -->
# Двигательные системы и скорость {#propulsion-speed}

Двигательные системы определяют скорость движения вашего корабля и его маневренность.

## За одну минуту {#in-one-minute}

- **Двигатели создают скорость, ускорители вставляются в них и добавляют к ней.** В двигатель входит от одного до трёх ускорителей (в Engine I — один, в Engine II — два, в Engine III — три), и в адаптивное ядро тоже (сколько именно, зависит от его ступени).
- **Два семейства по четыре ступени.** Impulse Thruster дают больше всего фиксированной скорости. Momentum Thruster дают меньше фиксированной скорости, но сильнее умножают скорость. В обоих семействах каждая ступень лучше предыдущей по обоим числам.
- **Что куда.** Как правило, Momentum ставят в полный Engine III (три ускорителя), а Impulse — всюду в остальных местах: числа есть в [таблице ниже](#which-thruster-where). Самый быстрый Engine III смешивает их: один Impulse Thruster IV и два Momentum Thruster IV дают 62,1.
- **Где их взять.** Ступень I каждого семейства стоит 20 000 кредитов. Ступени II–IV создаются в Сборочном цехе, каждая из предыдущей, а ускоритель никогда не меняет семейство.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Дерево предметов {#item-tree}

То, что создаёт Сборочный цех, сначала требует своей технологии; наведите курсор на предмет, чтобы увидеть, сколько длится её исследование. Дерево технологий, топливо и буст: [Исследования](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | buy 2000 Thulium | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I -> Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Двигатели {#engines}

Двигатели — основной источник тяги вашего корабля. Двигатель в **слоте способности** вместо этого даёт вам **Afterburner** из колонки «Особый эффект» — рывок скорости на десять секунд (дольше, если двигателей больше) — и сам тяги не добавляет (см. [Способности](/wiki/03-Mechanics/Abilities.md)).

| Название | Редкость | Базовая скорость | Бонус скорости, % | Бонус щита, % | Слоты | Особый эффект | Цена |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Ветхий | +2 | +2% | -2% | 1 | Afterburner I | 20 000 кредитов |
| **Engine II** | Обычный | +4 | +4% | -8% | 2 | Afterburner II | 2 000 Thulium |
| **Engine III** | Редкий | +6 | +5% | -15% | 3 | Afterburner III | Только крафт |

**Engine III** создаётся в [Сборочном цехе](/wiki/06-Items/Overview.md#upgrading-modules) из Engine II за 2 000 Thulium, 60 Ship Fragment, 3 Power Core и 3 Dark Matter Plate ([Dark Matter и Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)). Он сохраняет уровень зачарования израсходованного двигателя, а его бонусы выпадают заново ([Улучшение модулей](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Сначала снимите Engine II с корабля (и извлеките из него ускорители): двигатель, который установлен или в который вложены ускорители, не расходуется.

Бонус щита у двигателей записан в данных предметов, но игра его никогда не применяла: двигатели не ослабляют ваши щиты, а в карточках предметов его нет.

---

## Ускорители {#thrusters}

Ускорители вкладываются в двигатели или адаптивные ядра и увеличивают создаваемую ими скорость. Существует два семейства по четыре ступени: **Impulse Thruster** дают больше всего фиксированной скорости и немного умножают скорость двигателя, в котором стоят, **Momentum Thruster** — меньше фиксированной скорости, но умножают её сильнее. В обоих семействах каждая ступень лучше предыдущей — и по фиксированной скорости, и по множителю. Двигатель (или адаптивное ядро) с ускорителями создаёт **собственную базовую скорость плюс фиксированные прибавки к скорости от ускорителей, и всё это — умноженное на множители скорости ускорителей, перемноженные между собой** ([как считается скорость](/wiki/03-Mechanics/Speed.md)): Engine III с тремя Momentum Thruster IV создаёт (6 + 3 x 13,1) x 1,11 x 1,11 x 1,11 = 62,0, с тремя Impulse Thruster IV — (6 + 3 x 16,5) x 1,035 x 1,035 x 1,035 = 61,5, а Adaptive Core II с двумя Impulse Thruster IV — (0 + 2 x 16,5) x 1,035 x 1,035 = 35,4 (32,3 с двумя Momentum Thruster IV).

| Название | Редкость | Фикс. бонус к скорости | Множитель скорости | Цена |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Ветхий | +5 | 1,02x | 20 000 кредитов |
| **Impulse Thruster II** | Обычный | +10 | 1,025x | Только крафт |
| **Impulse Thruster III** | Редкий | +15 | 1,03x | Только крафт |
| **Impulse Thruster IV** | Эпический | +16,5 | 1,035x | Только крафт |
| **Momentum Thruster I** | Ветхий | +4,5 | 1,06x | 20 000 кредитов |
| **Momentum Thruster II** | Обычный | +9 | 1,07x | Только крафт |
| **Momentum Thruster III** | Редкий | +12,5 | 1,09x | Только крафт |
| **Momentum Thruster IV** | Эпический | +13,1 | 1,11x | Только крафт |

### Какой ускоритель куда {#which-thruster-where}

Impulse даёт больше фиксированной скорости, Momentum сильнее умножает, поэтому то, какое семейство быстрее, зависит от того, сколько скорости двигатель уже создаёт. Фиксированная скорость важнее всего там, где умножать почти нечего: в адаптивном ядре (у него нет собственной скорости) и в двигателе с одним или двумя ускорителями. Множитель важнее всего в полном Engine III, где умножать есть что. Скорость, которую каждое семейство создаёт с ускорителями ступени IV во всех слотах:

| Где стоят ускорители | С Impulse Thruster IV | С Momentum Thruster IV | Быстрее |
| :--- | :---: | :---: | :--- |
| Engine I, 1 ускоритель | 19,1 | 16,8 | Impulse |
| Engine II, 2 ускорителя | 39,6 | 37,2 | Impulse |
| Engine III, 1 ускоритель | 23,3 | 21,2 | Impulse |
| Engine III, 2 ускорителя | 41,8 | 39,7 | Impulse |
| Engine III, 3 ускорителя | 61,5 | 62,0 | Momentum |
| Adaptive Core II, 2 ускорителя | 35,4 | 32,3 | Impulse |

- **Низшие ступени.** Ступени I–III идут так же, с двумя близкими случаями: с двумя ускорителями в Engine II семейства равны на ступенях I и II (в пределах 0,05), а с двумя в Engine III Momentum впереди примерно на 0,2 на ступенях I и II. Начиная со ступени III Impulse впереди в обоих случаях — на 1,4–2,4. В полном Engine III Momentum впереди на каждой ступени — на 0,4–1,7.
- **Смешивайте их в Engine III.** Самый быстрый Engine III несёт один Impulse Thruster IV и два Momentum Thruster IV: (6 + 16,5 + 2 x 13,1) x 1,035 x 1,11 x 1,11 = 62,1, немного больше, чем с тремя Momentum (62,0) или тремя Impulse (61,5).

Бонус к множителю скорости ускорителя из [Кузницы](/wiki/06-Items/Forge.md) увеличивает часть выше 1 (бонус +15% к 1,11x даёт 1,1265x), а на множитель 1,05x и ниже Кузница бонус не выдаёт: на 1,02x–1,035x у Impulse Thruster он добавил бы меньше 0,006 (+15% к 1,035x даёт 1,040x). Impulse Thruster несёт один бонус (фиксированную скорость), Momentum Thruster — два.

Ступень I каждого семейства продаётся за 20 000 кредитов. Ступени II–IV создаются в [Сборочном цехе](/wiki/06-Items/Overview.md#upgrading-modules), каждая из ускорителя того же семейства ступенью ниже (Impulse Thruster II из Impulse Thruster I, III из II, IV из III) за Thulium, добычу с пришельцев и пластины: 2 или 4 Velkonite Reinforced Plate из вашего Skylab для ступени II или III и 3 Dark Matter Plate для ступени IV. Ускоритель никогда не меняет семейство: Impulse или Momentum вы выбираете, когда покупаете ступень I. Каждый из них сохраняет уровень зачарования израсходованного ускорителя, а его бонусы выпадают заново ([Улучшение модулей](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Ускорители не подходят для [слота способности](/wiki/03-Mechanics/Abilities.md): их место — внутри двигателей и адаптивных ядер.

### Как оторваться от пришельцев {#outrunning-aliens}

Пришельцы летают со скоростью 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) и 230 (Crystalys). Ostirion с одним Engine II и двумя ускорителями летит со скоростью 223,1 с Impulse Thruster I: это всё ещё меньше, чем у Crystalys, поэтому оторваться от него можно только с ускорителем, созданным в Сборочном цехе (234,2 с Impulse Thruster II, 245,5 с III, 249,2 с IV). Momentum Thruster на этом корабле летят так же или чуть ниже (223,2 с Momentum Thruster I; затем 234,2, 243,8 и 246,7 со II–IV): ступень I обоих семейств остаётся медленнее Crystalys, а любая ступень, созданная в Сборочном цехе, — быстрее.
