<!-- wiki-i18n source: 68b8f5293ad88b67 -->
<!-- wiki-i18n title: Двигательные системы -->
# Двигательные системы и скорость {#propulsion-speed}

Двигательные системы определяют скорость движения вашего корабля и его маневренность.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Дерево предметов {#item-tree}

То, что создаёт Сборочный цех, сначала требует своей технологии; наведите курсор на предмет, чтобы увидеть, сколько длится её исследование. Дерево технологий, топливо и буст: [Исследования](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | buy 2000 Thulium | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters

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

**Engine III** создаётся в [Сборочном цехе](/wiki/06-Items/Overview.md#upgrading-modules) из Engine II за 2 000 Thulium, 60 Ship Fragment, 3 Power Core и 6 Velkonite Reinforced Plate из вашего Skylab. Он сохраняет уровень зачарования израсходованного двигателя, а его бонусы выпадают заново ([Улучшение модулей](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Сначала снимите Engine II с корабля (и извлеките из него ускорители): двигатель, который установлен или в который вложены ускорители, не расходуется.

Бонус щита у двигателей записан в данных предметов, но игра его никогда не применяла: двигатели не ослабляют ваши щиты, а в карточках предметов его нет.

---

## Ускорители {#thrusters}

Ускорители вкладываются в двигатели или адаптивные ядра и увеличивают создаваемую ими скорость. Существует два семейства по четыре ступени: **Impulse Thruster** дают больше всего фиксированной скорости и немного умножают скорость двигателя, в котором стоят, **Momentum Thruster** — меньше фиксированной скорости, но умножают её сильнее. Двигатель (или адаптивное ядро) с ускорителями создаёт **собственную базовую скорость плюс фиксированные прибавки к скорости от ускорителей, и всё это — умноженное на множители скорости ускорителей, перемноженные между собой** ([как считается скорость](/wiki/03-Mechanics/Speed.md)): Engine III с тремя Momentum Thruster IV создаёт (6 + 3 x 12) x 1,14 x 1,14 x 1,14 = 62,2, с тремя Impulse Thruster IV — (6 + 3 x 17) x 1,02 x 1,02 x 1,02 = 60,5, а Adaptive Core II с двумя Impulse Thruster IV — (0 + 2 x 17) x 1,02 x 1,02 = 35,4 (31,2 с двумя Momentum Thruster IV).

| Название | Редкость | Фикс. бонус к скорости | Множитель скорости | Цена |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Ветхий | +5 | 1,02x | 20 000 кредитов |
| **Impulse Thruster II** | Обычный | +10 | 1,02x | Только крафт |
| **Impulse Thruster III** | Редкий | +15 | 1,03x | Только крафт |
| **Impulse Thruster IV** | Эпический | +17 | 1,02x | Только крафт |
| **Momentum Thruster I** | Ветхий | +4 | 1,08x | 20 000 кредитов |
| **Momentum Thruster II** | Обычный | +8 | 1,10x | Только крафт |
| **Momentum Thruster III** | Редкий | +11 | 1,13x | Только крафт |
| **Momentum Thruster IV** | Эпический | +12 | 1,14x | Только крафт |

Какое семейство быстрее, зависит от того, куда оно вставлено. Impulse Thruster дают больше в адаптивном ядре и в двигателе с одним-двумя ускорителями; Momentum Thruster той же ступени дают больше в Engine III со всеми тремя занятыми слотами (62,2 против 60,5 на ступени IV, а один Impulse Thruster IV с двумя Momentum Thruster IV — 62,3 — лучшее, что может дать Engine III).

Бонус к множителю скорости ускорителя из [Кузницы](/wiki/06-Items/Forge.md) увеличивает часть выше 1 (бонус +15% к 1,14x даёт 1,161x), а на множитель 1,05x и ниже Кузница бонус не выдаёт: на 1,02x или 1,03x у Impulse Thruster он стоил бы тысячную долю. Impulse Thruster несёт один бонус (фиксированную скорость), Momentum Thruster — два.

Ступень I каждого семейства продаётся за 20 000 кредитов. Ступени II–IV создаются в [Сборочном цехе](/wiki/06-Items/Overview.md#upgrading-modules), каждая из ускорителя того же семейства ступенью ниже (Impulse Thruster II из Impulse Thruster I, III из II, IV из III) за Thulium, добычу с пришельцев и Velkonite Reinforced Plate из вашего Skylab (2, 4 и 6 пластин). Ускоритель никогда не меняет семейство: Impulse или Momentum вы выбираете, когда покупаете ступень I. Каждый из них сохраняет уровень зачарования израсходованного ускорителя, а его бонусы выпадают заново ([Улучшение модулей](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Ускорители не подходят для [слота способности](/wiki/03-Mechanics/Abilities.md): их место — внутри двигателей и адаптивных ядер.

### Как оторваться от пришельцев {#outrunning-aliens}

Пришельцы летают со скоростью 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) и 230 (Crystalys). Ostirion с одним Engine II и двумя ускорителями летит со скоростью 223,1 с Impulse Thruster I: это всё ещё меньше, чем у Crystalys, поэтому оторваться от него можно только с ускорителем, созданным в Сборочном цехе (234,0 с Impulse Thruster II, 245,5 с III, 249,1 с IV). Momentum Thruster на этом корабле летят чуть ниже (222,6 с Momentum Thruster I; 233,2, 242,5 и 245,8 со II–IV): ступень I обоих семейств остаётся медленнее Crystalys, а любая ступень, созданная в Сборочном цехе, — быстрее.
