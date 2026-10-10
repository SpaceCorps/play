<!-- wiki-i18n source: 1433a0058afe39fa -->
<!-- wiki-i18n title: Двигательные системы -->
# Двигательные системы и скорость {#propulsion-speed}

Двигательные системы определяют скорость движения вашего корабля и его маневренность.

## За одну минуту {#in-one-minute}

- **Двигатели создают скорость, ускорители вставляются в них и добавляют к ней.** В двигатель входит от одного до трёх ускорителей (в Engine I — один, в Engine II — два, в Engine III — три), и в адаптивное ядро тоже (сколько именно, зависит от его ступени).
- **Два семейства по четыре ступени.** Impulse Thruster дают больше всего фиксированной скорости. Momentum Thruster дают меньше фиксированной скорости, но сильнее умножают скорость. В обоих семействах каждая ступень лучше предыдущей по обоим числам.
- **Что куда.** Как правило, ставьте Impulse всюду: только в полном Engine III (три ускорителя) Momentum ступеней I и II оказываются впереди. Числа есть в [таблице ниже](#which-thruster-where). Самый быстрый Engine III несёт три Impulse Thruster IV и даёт 52,5.
- **Где их взять.** Ступень I каждого семейства стоит 20 000 кредитов. Ступени II–IV создаются в Сборочном цехе, каждая из предыдущей, а ускоритель никогда не меняет семейство.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Дерево предметов {#item-tree}

То, что создаёт Сборочный цех, сначала требует своей технологии; наведите курсор на предмет, чтобы увидеть, сколько длится её исследование. Дерево технологий, топливо и буст: [Исследования](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Engine I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I => Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Двигатели {#engines}

Двигатели — основной источник тяги вашего корабля. Двигатель в **слоте способности** вместо этого даёт вам **Afterburner** из колонки «Особый эффект» — рывок скорости на десять секунд (дольше, если двигателей больше) — и сам тяги не добавляет (см. [Способности](/wiki/03-Mechanics/Abilities.md)).

| Название | Редкость | Базовая скорость | Бонус скорости, % | Бонус щита, % | Слоты | Особый эффект | Цена |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Ветхий | +2 | +2% | -2% | 1 | Afterburner I | 20 000 кредитов |
| **Engine II** | Обычный | +4 | +4% | -8% | 2 | Afterburner II | Только крафт |
| **Engine III** | Редкий | +6 | +5% | -15% | 3 | Afterburner III | Только крафт |

**Engine II** создаётся в [Сборочном цехе](/wiki/06-Items/Overview.md#upgrading-modules) из Engine I за 1 000 Thulium, 10 Ship Fragment, 1 Power Core и 2 Velkonite Reinforced Plate. **Engine III** создаётся там же из Engine II за 2 000 Thulium, 60 Ship Fragment, 3 Power Core и 3 Dark Matter Plate ([Dark Matter и Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)). Каждый сохраняет уровень зачарования израсходованного двигателя, а его бонусы выпадают заново ([Улучшение модулей](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Сначала снимите с корабля двигатель, который пойдёт в расход (и извлеките из него ускорители): двигатель, который установлен или в который вложены ускорители, не расходуется.

Бонус щита у двигателей записан в данных предметов, но игра его никогда не применяла: двигатели не ослабляют ваши щиты, а в карточках предметов его нет.

---

## Ускорители {#thrusters}

Ускорители вкладываются в двигатели или адаптивные ядра и увеличивают создаваемую ими скорость. Существует два семейства по четыре ступени: **Impulse Thruster** дают больше всего фиксированной скорости и немного умножают скорость двигателя, в котором стоят, **Momentum Thruster** — меньше фиксированной скорости, но умножают её сильнее. В обоих семействах каждая ступень лучше предыдущей — и по фиксированной скорости, и по множителю. Двигатель (или адаптивное ядро) с ускорителями создаёт **собственную базовую скорость плюс фиксированные прибавки к скорости от ускорителей, и всё это — умноженное на множители скорости ускорителей, перемноженные между собой** ([как считается скорость](/wiki/03-Mechanics/Speed.md)): Engine III с тремя Momentum Thruster IV создаёт (6 + 3 x 11,135) x 1,0935 x 1,0935 x 1,0935 = 51,5, с тремя Impulse Thruster IV — (6 + 3 x 14,025) x 1,02975 x 1,02975 x 1,02975 = 52,5, а Adaptive Core II с двумя Impulse Thruster IV — (0 + 2 x 14,025) x 1,02975 x 1,02975 = 29,7 (26,6 с двумя Momentum Thruster IV).

| Название | Редкость | Фикс. бонус к скорости | Множитель скорости | Цена |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Ветхий | +4,25 | 1,017x | 20 000 кредитов |
| **Impulse Thruster II** | Обычный | +8,5 | 1,02125x | Только крафт |
| **Impulse Thruster III** | Редкий | +12,75 | 1,0255x | Только крафт |
| **Impulse Thruster IV** | Эпический | +14,025 | 1,02975x | Только крафт |
| **Momentum Thruster I** | Ветхий | +3,825 | 1,051x | 20 000 кредитов |
| **Momentum Thruster II** | Обычный | +7,65 | 1,0595x | Только крафт |
| **Momentum Thruster III** | Редкий | +10,625 | 1,0765x | Только крафт |
| **Momentum Thruster IV** | Эпический | +11,135 | 1,0935x | Только крафт |

### Какой ускоритель куда {#which-thruster-where}

Impulse даёт больше фиксированной скорости, Momentum сильнее умножает, поэтому то, какое семейство быстрее, зависит от того, сколько скорости двигатель уже создаёт. Фиксированная скорость важнее всего там, где умножать почти нечего: в адаптивном ядре (у него нет собственной скорости) и в двигателе с одним или двумя ускорителями. Множитель важнее всего в полном Engine III, где умножать есть что, но выигрывают там только Momentum ступеней I и II. Скорость, которую каждое семейство создаёт с ускорителями ступени IV во всех слотах:

| Где стоят ускорители | С Impulse Thruster IV | С Momentum Thruster IV | Быстрее |
| :--- | :---: | :---: | :--- |
| Engine I, 1 ускоритель | 16,5 | 14,4 | Impulse |
| Engine II, 2 ускорителя | 34,0 | 31,4 | Impulse |
| Engine III, 1 ускоритель | 20,6 | 18,7 | Impulse |
| Engine III, 2 ускорителя | 36,1 | 33,8 | Impulse |
| Engine III, 3 ускорителя | 52,5 | 51,5 | Impulse |
| Adaptive Core II, 2 ускорителя | 29,7 | 26,6 | Impulse |

- **Низшие ступени.** Низшие ступени идут так же, с двумя близкими случаями и одним исключением: с двумя ускорителями в Engine II семейства равны на ступенях I и II (Impulse впереди на 0,06 и 0,24), и с двумя в Engine III тоже (в пределах 0,1). Начиная со ступени III Impulse впереди в обоих случаях — на 1,5–2,6. Исключение — полный Engine III: там Momentum впереди на ступенях I и II — на 0,6 и 0,9, а Impulse на ступенях III и IV — на 0,5 и 1,0.
- **Самый быстрый Engine III.** Он несёт три Impulse Thruster IV: 52,5, немного больше, чем с одним Impulse и двумя Momentum Thruster IV (52,1) или тремя Momentum (51,5).

Бонус к множителю скорости ускорителя из [Кузницы](/wiki/06-Items/Forge.md) увеличивает часть выше 1 (бонус +15% к 1,0935x даёт 1,1075x), а на множитель 1,05x и ниже Кузница бонус не выдаёт: на 1,017x–1,02975x у Impulse Thruster он добавил бы меньше 0,005 (+15% к 1,02975x даёт 1,034x). Impulse Thruster несёт один бонус (фиксированную скорость), Momentum Thruster — два.

Ступень I каждого семейства продаётся за 20 000 кредитов. Ступени II–IV создаются в [Сборочном цехе](/wiki/06-Items/Overview.md#upgrading-modules), каждая из ускорителя того же семейства ступенью ниже (Impulse Thruster II из Impulse Thruster I, III из II, IV из III) за Thulium, добычу с пришельцев и пластины: 2 или 4 Velkonite Reinforced Plate из вашего Skylab для ступени II или III и 3 Dark Matter Plate для ступени IV. Ускоритель никогда не меняет семейство: Impulse или Momentum вы выбираете, когда покупаете ступень I. Каждый из них сохраняет уровень зачарования израсходованного ускорителя, а его бонусы выпадают заново ([Улучшение модулей](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Ускорители не подходят для [слота способности](/wiki/03-Mechanics/Abilities.md): их место — внутри двигателей и адаптивных ядер.

### Как оторваться от пришельцев {#outrunning-aliens}

Пришельцы летают со скоростью 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) и 230 (Crystalys). Ostirion с одним Engine II и двумя ускорителями летит со скоростью 221,4 с Impulse Thruster I: это всё ещё меньше, чем у Crystalys, поэтому оторваться от него можно только с ускорителем, созданным в Сборочном цехе (230,8 с Impulse Thruster II, 240,3 с III, 243,3 с IV). Momentum Thruster на этом корабле летят так же или чуть ниже (221,4 с Momentum Thruster I; затем 230,5, 238,4 и 240,7 со II–IV): ступень I обоих семейств остаётся медленнее Crystalys, а любая ступень, созданная в Сборочном цехе, — быстрее, ступень II лишь на 0,8 и 0,5.
