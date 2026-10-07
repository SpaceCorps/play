<!-- wiki-i18n source: fbb5e8cfaee8aa9f -->
<!-- wiki-i18n title: Лазеры -->
# Лазеры и боеприпасы {#lasers-ammo}

<!-- wiki-search: arc amp; focus amp; pulse amp; prism amp; nova amp; apex amp; damage amp 1; crit amp 1; amps; penetration amp; shield penetration -->

Оружие — основной способ наносить урон в SpaceCorps.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Дерево предметов {#item-tree}

То, что создаёт Сборочный цех, сначала требует своей технологии; наведите курсор на предмет, чтобы увидеть, сколько длится её исследование. Дерево технологий, топливо и буст: [Исследования](/wiki/03-Mechanics/Research.md).

```tree
Quantum Laser 1 | laser, shoddy | buy 8000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser 2 | laser, common | buy 80000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser 3 | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-3 | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser 3, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-3, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp I | laser-amp, shoddy | buy 10000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp I | laser-amp, shoddy | buy 15000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp I | laser-amp, shoddy | buy 15000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Damage Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Crit Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Penetration Amp I, 20 Daraxium, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Damage Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Crit Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Penetration Amp II, 1 Power Core, 30 Nyxite, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Damage Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Crit Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp IV | laser-amp, epic | craft 1200 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Penetration Amp III, 1 Power Core, 30 Cataclysite, 40 Quorvium, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Standard Battery | ammo, common | buy 10 Credits | /wiki/06-Items/Lasers.md#laser-ammunition
Siphon Battery | ammo, rare | buy 0.25 Thulium | /wiki/06-Items/Lasers.md#siphon-battery
Advanced Plasma | ammo, rare | buy 0.5 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Ultra Core | ammo, rare | buy 1 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Experimental Fusion Core | ammo, epic | buy 2.2 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition

Quantum Laser 1 -> Quantum Laser 2 -> Quantum Laser 3 => Starfire-3 => Helios Beam
Damage Amp I => Damage Amp II => Damage Amp III => Damage Amp IV
Crit Amp I => Crit Amp II => Crit Amp III => Crit Amp IV
Penetration Amp I => Penetration Amp II => Penetration Amp III => Penetration Amp IV
Standard Battery -> Advanced Plasma -> Ultra Core -> Experimental Fusion Core
```
<!-- item-tree:end -->

## Лазеры {#lasers}

Устанавливайте лазеры прямо в слоты лазеров корабля или в дронов, чтобы повысить свою огневую мощь.

| Название | Редкость | Базовый урон | Шанс крита | Дальность | Слоты усилителей | Цена |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Quantum Laser 1** | Ветхий | 55 | – | 600 | 1 | 8 000 кредитов |
| **Quantum Laser 2** | Обычный | 65 | – | 700 | 2 | 80 000 кредитов |
| **Quantum Laser 3** | Редкий | 80 | 10% | 800 | 3 | Только крафт |
| **Starfire-3** | Мифический | 135 | 15% | 850 | 3 | Только крафт |
| **Helios Beam** | Мифический | 185 | 25% | 900 | 3 | Только крафт |

В колонке «Дальность» указана дальность каждого лазера по отдельности. **Ваш корабль стреляет на среднюю дальность своих лазеров** (лазеры в ваших дронах тоже учитываются), округлённую до ближайшей единицы, и все лазеры стреляют, как только цель оказывается в пределах этого расстояния. Starfire-3 рядом с двумя Quantum Laser 2 даёт кораблю дальность 750, а не 850; три Starfire-3 сохраняют 850, а одинаковые лазеры ничего не меняют. Бонус дальности из Кузницы учитывается у своего лазера до усреднения. Без лазеров ангар не показывает дальность (прочерк), и лазеры стрелять не могут, но ваши ракеты всё равно могут, каждая со своей дальностью (см. [Ракеты](/wiki/06-Items/Rockets.md)). В ангаре плитка показывает «Ср. дальность», если лазеры различаются, а при наведении курсора перечисляется дальность каждого лазера.

У Quantum Laser 1 и 2 собственного шанса крита нет («–»): его даёт Damage Amp или Crit Amp в их слотах (Penetration Amp не даёт). Критические попадания отображаются в плавающих числах урона другим цветом (ледяной голубой, крупнее, с «!»; см. [Числа урона и лечения](/wiki/03-Mechanics/Combat.md#damage-and-heal-numbers)).

Лазеры тоже повреждают [астероиды](/wiki/03-Mechanics/Asteroid-Mining.md#breaking-one), но лишь на 5% от того, что залп наносит кораблю (усилители, бустеры, боеприпасы и критические попадания учитываются, потом вычитается броня астероида; Siphon Battery астероиды повредить не может). Чтобы разбить астероид, нужны ракеты.

### Создание трёх лучших лазеров {#making-the-top-three-lasers}

**Quantum Laser 3**, **Starfire-3** и **Helios Beam** создаются только в **Сборочном цехе**. Quantum Laser 3 больше не продаётся в магазине; у пилота, который уже владеет им, он остаётся. Каждый рецепт требует пластины из Кузницы [Skylab](/wiki/03-Mechanics/Skylab.md), а Helios Beam — ещё и 3 Dark Matter Plate:

| Лазер | Время создания | Что требуется |
| :--- | :---: | :--- |
| Quantum Laser 3 | 1 мин | 10 Ship Fragment, 2 Velkonite Reinforced Plate, 1 500 Thulium |
| Starfire-3 | 1 мин | 1 Quantum Laser 3, 15 Ship Fragment, 8 Velkonite Reinforced Plate, 1 Reinforced Hull Plate, 1 500 Thulium, 100 000 кредитов |
| Helios Beam | 3 мин | 1 Starfire-3, 50 Cataclysite, 2 Power Core, 18 Orvium Reinforced Plate, 3 Dark Matter Plate, 4 Reinforced Hull Plate, 2 000 Thulium |

Страница Сборочного цеха показывает, что у вас есть и что требует рецепт, а кнопка «Собрать» сообщает, чего вам не хватает. Наведите курсор на изображение или название рецепта либо на один из его материалов, чтобы увидеть полное описание и характеристики предмета.

**Starfire-3 создаётся из Quantum Laser 3.** Сначала вы создаёте Quantum Laser 3, а Starfire-3 расходует его. То, что уже потратил Quantum Laser 3, повторно не требуется, поэтому вместе они стоят ровно столько, сколько раньше стоил один Starfire-3: 3 000 Thulium, 100 000 кредитов, 25 Ship Fragment, 10 Velkonite Reinforced Plate, 1 Reinforced Hull Plate и 2 минуты. Если Quantum Laser 3 у вас уже есть, вы платите только за собственную часть Starfire-3. Правила те же, что у Helios Beam (ниже): Starfire-3 сохраняет уровень зачарования израсходованного Quantum Laser 3 (Божественный Quantum Laser 3 даёт Божественный Starfire-3), а его бонусы выпадают заново; вы выбираете, какой Quantum Laser 3 пойдёт в дело, карточка сначала спросит подтверждение, прежде чем использовать предмет выше Стандартного, а Quantum Laser 3 должен быть свободным: **сначала снимите его с корабля** (вложенные в него усилители вернутся в инвентарь) и извлеките из транспортного тайника. Когда он стоит на корабле, кнопка «Собрать» сообщает «Сначала снимите Quantum Laser 3».

**Helios Beam создаётся из Starfire-3.** Сначала вы создаёте Starfire-3 (3 000 Thulium и 100 000 кредитов вместе с его Quantum Laser 3), а Helios Beam расходует его, как [Master Drone](/wiki/06-Items/Drones.md) расходует Slave Drone. То, что уже потратил Starfire-3, повторно не требуется, поэтому вместе они стоят те 5 000 Thulium, Cataclysite, Power Core и Reinforced Hull Plate, которые Helios Beam требовал сам по себе, и 18 пластин Orvium вместо 20 (десять пластин Velkonite у Starfire-3 заменяют недостающие две), а ещё, раз Helios Beam — последняя ступень своей цепочки, 3 Dark Matter Plate; сверх этого вы платите 100 000 кредитов и 25 Ship Fragment за Starfire-3. Правило то же, что и у [улучшения модулей](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly): Helios Beam сохраняет уровень зачарования израсходованного Starfire-3 (Божественный Starfire-3 даёт Божественный Helios Beam), а его бонусы выпадают заново; если у вас несколько Starfire-3, вы выбираете, какой пойдёт в дело, а карточка сначала спросит подтверждение, прежде чем использовать предмет выше Стандартного. Starfire-3 должен быть свободным: **сначала снимите его с корабля** (вложенные в него усилители вернутся в инвентарь) и извлеките из транспортного тайника. Когда он стоит на корабле, кнопка «Собрать» сообщает «Сначала снимите Starfire-3».

Откуда берутся пластины:

- **Velkonite Reinforced Plate** (Quantum Laser 3 и Starfire-3) куются из Velkonite, по 40 руды на пластину на 1-м уровне Кузницы Skylab. **Orvium Reinforced Plate** (Helios Beam) куются из Orvium, по 80 руды на пластину.
- **Dark Matter Plate** (3 для Helios Beam) прессуются в Сборочном цехе из 5 Dark Matter, Velkonite Reinforced Plate, Orvium Reinforced Plate и 250 Thulium, после того как вы изучите их рецепт. На три нужно 15 Dark Matter — в среднем 7,5 ракеты N.I.K.E., выпущенной в [чёрную дыру](/wiki/03-Mechanics/Black-Hole.md). Весь путь описан в статье [Dark Matter и Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md).
- Руда поступает только от сборщиков вашего Skylab. Сборщик Velkonite 5-го уровня добывает 18 Velkonite в час, поэтому пластины для Quantum Laser 3 требуют около 4 часов добычи, а десять пластин для Starfire-3 (две в его Quantum Laser 3, восемь на его собственном шаге) — около 22. Дольше всего делается Helios Beam: для его 18 пластин нужно 1 440 Orvium, то есть около 4 суток работы сборщика Orvium 5-го уровня, а ещё 3 пластины Orvium внутри его 3 Dark Matter Plate добавляют 240 Orvium, около 17 часов.
- Хранилище ресурсов вмещает 240 единиц каждой руды на 1-м уровне: 6 пластин Velkonite или 3 пластины Orvium при кузнице 1-го уровня. Поэтому куйте по ходу дела (партия кузницы — до 10 пластин на 1-м уровне) или улучшайте хранилище.
- Откованные пластины ждут в Кузнице, пока вы не заберёте их (корабль должен стоять в отсеке), и попадают в инвентарь как обычные предметы.

Ship Fragment, Cataclysite, Power Core и Reinforced Hull Plate выпадают из пришельцев; все источники и применения каждого материала описаны на странице [Ресурсы](/wiki/06-Items/Resources.md); сколько именно выпадает, показано в списках добычи на страницах [Bulwark](/wiki/04-Aliens/Bulwark.md) и [Goombah](/wiki/04-Aliens/Goombah.md).

---

## Лазерные усилители (Amp) {#laser-amplifiers-amps-}

Устанавливайте их прямо в слот лазера, чтобы улучшить его характеристики. Есть **три линейки по четыре ступени**, названные как ячейки щита: **Damage Amp** добавляет фиксированное количество урона, **Crit Amp** добавляет шанс критического попадания и фиксированный критический урон, а **Penetration Amp** вычитает очки из поглощения вашей цели ([ниже](#shield-penetration-of-a-laser-hit)). Это не [бустеры](/wiki/06-Items/Boosters.md): **Laser Damage Booster 1** и **Laser Damage Booster 2** — бустеры с таймером (+10% к урону лазеров на 10 часов), и вставлять в них нечего.

| Название | Редкость | Бонус к базовому урону | Бонус к шансу крита | Фикс. критический урон | Цена |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Damage Amp I** | Ветхий | +10 | +5% | +5 | 10 000 кредитов |
| **Damage Amp II** | Необычный | +16 | +5% | +8 | Только крафт |
| **Damage Amp III** | Редкий | +26 | +6% | +13 | Только крафт |
| **Damage Amp IV** | Эпический | +38 | +7% | +20 | Только крафт |
| **Crit Amp I** | Ветхий | +0 | +15% | +0 | 15 000 кредитов |
| **Crit Amp II** | Необычный | +0 | +20% | +14 | Только крафт |
| **Crit Amp III** | Редкий | +0 | +25% | +24 | Только крафт |
| **Crit Amp IV** | Эпический | +0 | +25% | +44 | Только крафт |

| Название | Редкость | Пробитие щита | Цена |
| :--- | :--- | :---: | :--- |
| **Penetration Amp I** | Ветхий | +2% | 15 000 кредитов |
| **Penetration Amp II** | Необычный | +4% | Только крафт |
| **Penetration Amp III** | Редкий | +6% | Только крафт |
| **Penetration Amp IV** | Эпический | +8% | Только крафт |

**В магазине продаётся только первая ступень каждой линейки.** Остальные три создаются в [Сборочном цехе](/wiki/06-Items/Overview.md#upgrading-modules) из усилителя ступенью ниже, когда вы исследуете их технологию в Skylab ([Исследования](/wiki/03-Mechanics/Research.md)). Каждый шаг требует Thulium, добычу с пришельцев и пластины (Velkonite Reinforced Plate из вашего Skylab для ступеней II и III, 3 Dark Matter Plate для ступени IV), а новый усилитель сохраняет уровень зачарования израсходованного, и его бонусы выпадают заново ([Улучшения модулей в Сборочном цехе](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Шаги Penetration добавляют кристальную линзу. Каждому усилителю ступени IV нужны 3 [Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md), как и последней ступени каждой цепочки улучшений, так что технология усилителя ступени IV сначала требует технологию пластины.

| Шаг | Thulium | Время | Кроме усилителя ступенью ниже |
| :--- | ---: | ---: | :--- |
| Damage Amp II / Crit Amp II | 250 | 60 с | 10 Cataclysite, 1 Velkonite Reinforced Plate |
| Damage Amp III / Crit Amp III | 1 000 | 60 с | 20 Cataclysite, 1 Power Core, 2 Velkonite Reinforced Plate |
| Damage Amp IV / Crit Amp IV | 1 200 | 60 с | 30 Cataclysite, 1 Power Core, 3 Dark Matter Plate |
| Penetration Amp II | 250 | 60 с | 20 Daraxium, 10 Cataclysite, 1 Velkonite Reinforced Plate |
| Penetration Amp III | 1 000 | 60 с | 30 Nyxite, 20 Cataclysite, 1 Power Core, 2 Velkonite Reinforced Plate |
| Penetration Amp IV | 1 200 | 90 с | 40 Quorvium, 30 Cataclysite, 1 Power Core, 3 Dark Matter Plate |

Helios Beam с тремя Amp ступени IV — это 4 модуля последней ступени: 12 Dark Matter Plate, 60 Dark Matter, в среднем 30 ракет N.I.K.E. Wraith с последней ступенью в каждом слоте содержит 900 Dark Matter ([Dark Matter и Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md#what-the-last-tier-asks-for)).

### Какой усилитель куда ставить {#which-amp-goes-where}

Усилитель урона добавляет любому лазеру одинаковый урон, поэтому больше всего он даёт на **лазерах Quantum**. Усилитель крита умножает то, что лазер уже наносит, так что чем сильнее бьёт лазер, тем он ценнее: на **Starfire-3** он равен линейке урона, а на **Helios Beam** выходит вперёд примерно на 3,5%. Шанс крита лазера ограничен 100%: три Crit Amp III или Crit Amp IV доводят Helios Beam ровно до этого значения. Penetration Amp не даёт ни урона, ни шанса крита: он нужен против кораблей, чьи щиты иначе приняли бы большую часть вашего попадания ([ниже](#when-is-a-penetration-amp-worth-a-slot)).

С одинаковыми усилителями лазер всегда сильнее нижестоящего, поэтому лучший усилитель никогда не заменяет лучший лазер: Quantum Laser 3 с тремя Damage Amp IV наносит меньше урона, чем Helios Beam с тремя Damage Amp I (при деталях одного уровня зачарования: Quantum Laser 3 и Damage Amp IV, выкованные до «Божественного» уровня или выше, с лучшими выпавшими бонусами, могут обойти обычный Helios Beam с Damage Amp I, на уровне «Божественный» — едва-едва).


---

## Лазерные боеприпасы {#laser-ammunition}

Расходуемые батареи, умножающие урон ваших лазерных залпов:

| Название | Редкость | Множитель урона | Пробитие щита | Цена за шт. |
| :--- | :--- | :---: | :---: | :--- |
| **Standard Battery** | Обычный | 1,0x | – | 10 кредитов |
| **Advanced Plasma** | Редкий | 2,0x | – | 0,5 Thulium |
| **Ultra Core** | Редкий | 3,0x | 5% | 1,0 Thulium |
| **Experimental Fusion Core** | Эпический | 4,0x | 10% | 2,2 Thulium |
| **Siphon Battery** | Редкий | 1,0x, только по щитам | – | 0,25 Thulium |

**Пробитие щита** вычитается из поглощения вашей цели при каждом попадании ваших залпов: щиты принимают поглощение цели за вычетом пробития (см. [Механика щитов](/wiki/03-Mechanics/Shields.md#shield-penetration)). Ваши Penetration Amp и построение дронов прибавляются к пробитию боеприпасов, а вся сумма описана [ниже на этой странице](#shield-penetration-of-a-laser-hit). Против корабля с 80% (лучший щит с лучшими ячейками) 10% у боеприпасов x4 оставляют щитам 70% попадания, а корпусу — 30%. Больше всего это важно против кораблей, у которых корпус мал по сравнению со щитом; очень большой корабль с 80% держится одинаково в обоих случаях. У пришельцев нет заметной характеристики поглощения (их щиты принимают 80% попадания), и пробитие вычитается и из неё.

### Siphon Battery

Siphon Battery — боеприпас для кражи щитов вместо разрушения корпусов. Он наносит **урон x1 прямо щиту цели** и добавляет столько же **вашему собственному щиту**, но не больше вашего максимума. Выбирайте его в списке боеприпасов на панели, как любые другие (это плитка с бирюзовым вихрем). Луч он не выпускает: к цели уходит тонкий слабый бирюзовый зонд, щит цели вспыхивает бирюзовым в месте попадания, а похищенный щит видимо стекает к вашему кораблю светящимися бирюзовыми пакетами (от трёх до десяти, чем больше похищено, тем их больше), один за другим примерно за полсекунды. Каждый долетевший пакет вызывает пульсацию вашего щита. То же вы видите для Siphon Battery любого пилота в поле зрения, у кого бы он ни забирал щит: у пришельцев, других пилотов и кораблей пилотов корпораций.

- **Только щит**: корпус не затрагивается никогда, поглощение цели не делит урон, а Siphon Battery не может ничего уничтожить. Его урон ограничен тем, что ещё осталось в щите цели.
- **Нечего забирать**: по цели без щита он ничего не вытягивает и ничего не даёт. Залп всё равно тратится — по одной батарее на лазер, как и с любыми боеприпасами. Вы видите только зонд и тусклое мерцание на корпусе, пакетов нет.
- **Прирост**: ваш щит никогда не превышает максимума, а получение щита не задерживает собственную регенерацию щита.
- **Щиты, которые можно вытянуть, есть и у пришельцев, и у пилотов.** Кража щита у пришельца считается попаданием для [права первого попадания](/wiki/03-Mechanics/Combat.md); если щита нет, не считается. Такое попадание, как и любое другое, будит и Seeker или Goombah, которые только дают отпор.
- **Критические попадания** учитываются: критический залп вытягивает в 1,5 раза больше, а его число рисуется как критическое попадание. Пакеты крупнее и ярче, а щит цели вспыхивает сильнее.
- [Пилоты корпораций](/wiki/03-Mechanics/Company-Pilots.md) стреляют стандартными боеприпасами x1.

---

## Пробитие щита при попадании лазера {#shield-penetration-of-a-laser-hit}

Каждое попадание лазера вычитает очки из поглощения вашей цели из трёх источников, которые складываются: ваши **боеприпасы** (Ultra Core 5%, Experimental Fusion Core 10%), ваши **Penetration Amp** и **построение дронов** (Gemini +9%, Stiletto +16%; [Построения дронов](/wiki/03-Mechanics/Formations.md)). Сумма **останавливается на 50%** для лазера; сумма прямой ракеты — на 40% ([Ракеты](/wiki/06-Items/Rockets.md)). Щиты затем принимают поглощение цели за вычетом пробития попадания, а корпус — остальное ([Механика щитов](/wiki/03-Mechanics/Shields.md#shield-penetration)).

- **Ваши усилители считаются как среднее по вашим лазерам.** Залп — это одно попадание, поэтому игра складывает пробитие усилителей каждого лазера (лазеры в ваших дронах тоже считаются) и берёт среднее по вашим лазерам, где вес каждого — его урон, как и для шанса крита. Три Penetration Amp IV в каждом лазере дают 24%; один Penetration Amp IV в одном лазере из двенадцати — 0,67%. У Wraith 12 лазеров и 36 слотов усилителей, и нужно заполнить все 36, чтобы получить 24%.
- **Ангар это показывает.** Как только усилители ваших лазеров дают пробитие, среди боевых характеристик Ангара появляется плитка **Пробитие** с цифрой; боеприпасы и построение в неё не входят.
- **Лучший лазер достигает потолка ровно.** Experimental Fusion Core (10%), Stiletto (16%) и три Penetration Amp IV в каждом лазере (24%) дают 50%.
- **Бонус Кузницы на Penetration Amp IV в такой сборке пропадает впустую.** Penetration Amp можно ковать, как и другие усилители, и его единственный бонус умножает пробитие: «Вечный» бонус (от +9% до +15%) делает Penetration Amp IV 8,7–9,2 пункта вместо 8. Но 10 + 16 + 24 уже дают потолок 50%, и каждый лишний пункт отсекается (три «Вечных» дали бы 53,6%, обрезанные до 50%).

| Лазерный залп | Боеприпасы | Усилители (3 слота) | Построение | Итого |
|---|---|---|---|---|
| Один Experimental Fusion Core | 10% | – | – | **10%** |
| Fusion Core + Gemini | 10% | – | 9% | **19%** |
| Fusion Core + Stiletto (лучшее до Penetration Amp) | 10% | – | 16% | **26%** |
| Fusion Core + 3 Penetration Amp I | 10% | 6% | – | **16%** |
| Fusion Core + 3 Penetration Amp II | 10% | 12% | – | **22%** |
| Fusion Core + 3 Penetration Amp III | 10% | 18% | – | **28%** |
| Fusion Core + 3 Penetration Amp IV | 10% | 24% | – | **34%** |
| Fusion Core + 3 Penetration Amp IV + Gemini | 10% | 24% | 9% | **43%** |
| Ultra Core + 3 Penetration Amp IV + Stiletto (лучшее на каждый день) | 5% | 24% | 16% | **45%** |
| Fusion Core + 3 Penetration Amp IV + Stiletto (лучший лазер) | 10% | 24% | 16% | **50%** |

Что это делает со щитами цели: каждая ячейка — доля попадания, которую **принимают щиты / принимает корпус**.

| Защитник (поглощение) | Без усилителей | Один Fusion Core (10%) | Раньше: Fusion Core + Stiletto (26%) | Fusion Core + 3 Penetration Amp IV (34%) | Лучший лазер (50%) |
|---|---|---|---|---|---|
| Light Shield Core, без ячейки (45%) | 45 / 55 | 35 / 65 | 19 / 81 | 11 / 89 | 0 / 100 |
| Heavy Shield Core, без ячейки (50%) | 50 / 50 | 40 / 60 | 24 / 76 | 16 / 84 | 0 / 100 |
| Light Shield Core + Absorption Shield Cell IV (55%) | 55 / 45 | 45 / 55 | 29 / 71 | 21 / 79 | 5 / 95 |
| Heavy Shield Core + 3 Capacity Shield Cell IV (65%) | 65 / 35 | 55 / 45 | 39 / 61 | 31 / 69 | 15 / 85 |
| Лучший щит из коробки (80%) | 80 / 20 | 70 / 30 | 54 / 46 | 46 / 54 | 30 / 70 |
| Лучший щит, «Вечная» Кузница (лучший бросок) и 34 уровня магазина сезона (95,4%) | 95 / 5 | 85 / 15 | 69 / 31 | 61 / 39 | 45 / 55 |
| Лучший щит, «Вечная» Кузница (лучший бросок) и магазин сезона на пределе (102%) | 100 / 0 | 92 / 8 | 76 / 24 | 68 / 32 | 52 / 48 |
| Любой пришелец (80%) | 80 / 20 | 70 / 30 | 54 / 46 | 46 / 54 | 30 / 70 |

Лучший лазер опустошает ядро щита без ячейки (корпус принимает всё попадание); ядро с ячейкой сохраняет часть каждого попадания, а лучший щит — 30% (45% с бонусами). Ракета никогда не опустошает щит: её потолок — 40%.

### Когда Penetration Amp стоит слота? {#when-is-a-penetration-amp-worth-a-slot}

**Penetration Amp противостоит поглощению выше примерно 95% (сборки с магазином сезона, Кузницей и Rampart). Против лучшего щита из коробки (80%) Crit Amp той же ступени всё равно примерно на 10% быстрее, а Penetration Amp не убивает пришельцев быстрее, чем Damage Amp или Crit Amp его ступени.**

- **Урона он не даёт.** На Helios Beam три Penetration Amp IV дают 187 урона за залп (боеприпасы x1, среднее по разбросу и критам), где три Damage Amp IV дают 356, а три Crit Amp IV — 369: примерно вдвое меньше. Он возвращает долю щита, поэтому окупается только там, где корпус мал по сравнению со щитом, а поглощение высоко; против Wraith или Ironclad, чей большой корпус держится и так, простой набор Damage или Crit быстрее.
- **Пришельцы.** Их щиты принимают 80% попадания за вычетом вашего пробития, так что он действует и на них, но Damage Amp или Crit Amp той же ступени всё равно убивает их быстрее.
- **Сколько он стоит.** Каждому Penetration Amp IV нужны 3 Dark Matter Plate (15 Dark Matter), как и любому усилителю ступени IV, так что Wraith, заполняющему все 36 слотов, нужно 108 пластин, 540 Dark Matter.
