<!-- wiki-i18n source: 55131889617bd886 -->
<!-- wiki-i18n title: Исследования -->
# Исследования {#research}

**Исследовательский центр** — лаборатория вашего [Skylab](/wiki/03-Mechanics/Skylab.md). Вы подаёте в него ресурсы, он превращает их в **науку**, а наука исследует **технологии**. Любое создание в [Сборочном цехе](/wiki/06-Items/Overview.md#upgrading-modules) сначала требует своей технологии: корабль, лазер, ускоритель или CPU нельзя создать, пока они не исследованы.

На этой странице собраны полное дерево технологий с временем каждой, наука, которую даёт каждый ресурс, буст Thulium, правило для Dark Matter и новые CPU. Числа читаются из данных самой игры, поэтому всегда совпадают с игровыми.

## Исследовательский центр {#the-research-centre}

<!-- research-centre:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **Открывается с ядра 10-го уровня.** Исследовательский центр — модуль вашего [Skylab](/wiki/03-Mechanics/Skylab.md), он строится как остальные: 25 Ship Fragment из инвентаря (корабль должен стоять на посадке), 25 000 кредитов и 500 Thulium. Его экран — вид **Исследования** на странице Skylab.
- **Уровни с 1-го по 10-й.** Более высокий уровень даёт бак побольше и потребляет больше энергии. Исследование он не ускоряет: технология занимает одно и то же время на любом уровне.
- **Бак.** Центр хранит науку в баке, который на 1-м уровне вмещает 12 ч исследования, а с каждым уровнем — на 25% больше (см. таблицу ниже).
- **От топлива к науке.** Поданный ресурс сразу становится наукой, как показывает таблица топлива. Исследование сжигает науку: 1 за каждую секунду своего времени; при пустом баке оно ждёт и продолжается, когда вы снова подадите ресурсы в центр.
- **Первый час бесплатно.** Новый центр начинает с 3 600 науки в баке, это 1 ч исследования.
- **По одному.** Центр исследует только одну технологию за раз. Очереди нет.
- **Пока вас нет.** Исследование идёт по часам сервера, поэтому продолжается после выхода из игры, пока не завершится или не опустеет бак. Нехватка энергии и улучшение центра его не останавливают.
- **Энергия.** Центр потребляет 25 на 1-м уровне и на 15% больше с каждым уровнем и не отключается.
- **Вайп сохраняет всё:** ваши технологии, науку в баке, вложенную Dark Matter, идущее исследование и буст.
- **Что у вас есть, то ваше.** Когда исследования появились в игре, каждый пилот получил технологию каждого предмета, который у него уже был, и технологии, нужные для них. Предмет, который попадёт к вам позже (подарок, код, награда), свою технологию не открывает.
- **Ниже 10-го уровня ядра** исследовать нельзя, так что в Сборочном цехе пока ничего нового не создать. Миссии станции помогут поднять ядро.

<!-- research-centre:end -->

### Бак на каждом уровне {#the-tank-at-every-level}

<!-- research-tank:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Уровень | Бак (наука) | Вмещает исследования на | … с бустом | Энергия |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 43 200 | 12 ч | 6 ч | 25 |
| 2 | 54 000 | 15 ч | 7,5 ч | 28,7 |
| 3 | 67 500 | 18,8 ч | 9,4 ч | 33,1 |
| 4 | 84 375 | 23,4 ч | 11,7 ч | 38 |
| 5 | 105 469 | 29,3 ч | 14,6 ч | 43,7 |
| 6 | 131 836 | 36,6 ч | 18,3 ч | 50,3 |
| 7 | 164 795 | 45,8 ч | 22,9 ч | 57,8 |
| 8 | 205 994 | 57,2 ч | 28,6 ч | 66,5 |
| 9 | 257 492 | 71,5 ч | 35,8 ч | 76,5 |
| 10 | 321 865 | 89,4 ч | 44,7 ч | 87,9 |

<!-- research-tank:end -->

## Топливо {#fuel}

Вы подаёте в центр ресурсы, и каждая единица сразу становится наукой. Чем больше труда стоит добыть единицу, тем больше науки она даёт: числа следуют трудности добычи, а не метке редкости, так что Power Core (Необычный) даёт больше, чем Orvium (Редкий). Руда берётся из Хранилища ресурсов вашего [Skylab](/wiki/03-Mechanics/Skylab.md#resource-storage), любой другой ресурс — из вашего инвентаря, и корабль должен стоять на посадке. Velkonite Reinforced Plate, Orvium Reinforced Plate, Dark Matter Plate, Dark Matter, кредиты и Thulium сжечь нельзя; Reinforced Hull Plate — можно.

<!-- research-fuel:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Ресурс | Редкость | Берётся из | Науки за единицу | Единиц на 1 час |
| :--- | :--- | :--- | ---: | ---: |
| [Ship Fragment](/wiki/06-Items/Resources.md#ship-fragment) | Обычный | Ваш инвентарь | 5 | 720 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | Обычный | Ваш инвентарь | 5 | 720 |
| [Daraxium](/wiki/06-Items/Resources.md#daraxium) | Обычный | Ваш инвентарь | 7 | 515 |
| [Nyxite](/wiki/06-Items/Resources.md#nyxite) | Обычный | Ваш инвентарь | 7 | 515 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | Обычный | Ваш инвентарь | 8 | 450 |
| [Reinforced Hull Plate](/wiki/06-Items/Resources.md#reinforced-hull-plate) | Обычный | Ваш инвентарь | 33 | 110 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | Необычный | Хранилище ресурсов | 40 | 90 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | Редкий | Хранилище ресурсов | 80 | 45 |
| [Power Core](/wiki/06-Items/Resources.md#power-core) | Необычный | Ваш инвентарь | 100 | 36 |
| [Ancient Control Unit](/wiki/06-Items/Resources.md#ancient-control-unit) | Редкий | Ваш инвентарь | 650 | 6 |

В последнем столбце — число единиц, которого хватает на час исследования без буста, с округлением вверх; с бустом нужно в 2 раза больше.

<!-- research-fuel:end -->

## Буст Thulium {#the-thulium-boost}

<!-- research-boost:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **5 000 Thulium** покупают буст: центр исследует **в 2 раза быстрее в течение 24 ч**.
- Он также **сжигает науку в 2 раза быстрее**, поэтому буст покупает время, но не топливо: технология сжигает одну и ту же науку, с бустом или без.
- Буст начинается в момент покупки и идёт по часам независимо от того, есть ли в баке топливо, поэтому покупайте его, пока исследование идёт. Центр отказывает в бусте, если ничего не исследуется.
- Бусты складываются: если купить буст, пока идёт другой, его конец сдвинется на 24 ч, но не более чем на 72 ч вперёд. Буст принадлежит вашему Исследовательскому центру, а не отдельному исследованию.

Что буст делает со временем исследования, если он действует с самого начала:

| Время исследования | С бустом | Бустов на всё исследование | Thulium |
| :--- | :--- | ---: | ---: |
| 30 мин | 15 мин | 1 | 5 000 |
| 3 ч | 1 ч 30 мин | 1 | 5 000 |
| 6 ч | 3 ч | 1 | 5 000 |
| 10 ч | 5 ч | 1 | 5 000 |
| 1 д | 12 ч | 1 | 5 000 |
| 2 д | 1 д | 1 | 5 000 |

<!-- research-boost:end -->

## Dark Matter {#dark-matter}

Технологиям на вершине дерева нужна ещё и Dark Matter. Её даёт [чёрная дыра](/wiki/03-Mechanics/Black-Hole.md#dark-matter): ракета N.I.K.E., долетевшая до неё, оставляет немного, а иногда её роняет Dormant Pulse из [Роя Dormant](/wiki/05-Swarms/Dormant-Swarm.md).

<!-- research-dark-matter:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

- **10 Dark Matter** на каждую из 15 технологий в таблице ниже, сверх науки: вложите её в Исследовательский центр (из инвентаря, корабль на посадке) до начала, и исследование заберёт её при старте.
- **Правило:** предмет редкости Эпический или выше, исследование которого занимает 10 ч или больше. N.I.K.E., с помощью которой добывают Dark Matter, её никогда не требует.
- **Если отменить исследование,** вложенная для него Dark Matter возвращается в центр. Прогресс и уже сожжённая наука — нет.
- Все вместе они требуют 150 Dark Matter.

| Технология | Редкость | Время исследования | Dark Matter |
| :--- | :--- | :--- | ---: |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | Эпический | 10 ч | 10 |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | Эпический | 10 ч | 10 |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | Эпический | 10 ч | 10 |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | Эпический | 10 ч | 10 |
| [Starfire-3](/wiki/06-Items/Lasers.md#lasers) | Мифический | 1 д | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | Мифический | 1 д | 10 |
| [Nova Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Эпический | 10 ч | 10 |
| [Apex Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | Эпический | 10 ч | 10 |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | Эпический | 1 д | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | Эпический | 1 д | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | Мифический | 2 д | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | Мифический | 1 д | 10 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | Легендарный | 1 д | 10 |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | Эпический | 1 д | 10 |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | Эпический | 1 д | 10 |

<!-- research-dark-matter:end -->

## Дерево технологий {#the-technology-tree}

Каждый блок — это технология: предмет, который она позволяет создать, со временем исследования под названием (часы) и, где нужна Dark Matter, со значком Dark Matter. Стрелка ведёт от технологии к той, которой она нужна, и первой вы исследуете начало стрелки; блок без стрелок можно исследовать сразу. Наведите курсор на блок, чтобы увидеть время исследования, сжигаемую науку и то, что Сборочный цех потом потребует за предмет, а щёлкните, чтобы открыть страницу предмета. Деревья рисуются по данным самой игры.

<!-- research-tree:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

### Двигательные системы и скорость {#tree-propulsion}

```tree research
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines

Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```

### Щиты и защита {#tree-shields}

```tree research
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 6 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cores

Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```

### Лазеры и боеприпасы {#tree-lasers}

```tree research
Quantum Laser 3 | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-3 | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser 3, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-3, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Nova Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Pulse Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Apex Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Prism Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-

Quantum Laser 3 => Starfire-3 => Helios Beam
```

### Бустеры {#tree-boosters}

```tree research
Damage Amp II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
```

### Дроны {#tree-drones}

```tree research
Master Drone | drone, rare | craft 40000 Thulium, 60 s | research 36000 s, 36000 science | 1 Slave Drone, 100 Ship Fragment | /wiki/06-Items/Drones.md#available-drones
```

### Корабли {#tree-ships}

```tree research
Paragon | ship, rare | craft 1500 Thulium, 900 s | research 21600 s, 21600 science | 120 Ship Fragment, 20 Reinforced Hull Plate, 5 Power Core | /wiki/02-Ships/Paragon.md
Ironclad | ship, epic | craft 10500 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit | /wiki/02-Ships/Ironclad.md
Storm | ship, epic | craft 15000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 35 Reinforced Hull Plate, 10 Power Core, 1 Ancient Control Unit | /wiki/02-Ships/Storm.md
Wraith | ship, mythical | craft 20000 Thulium, 900 s | research 172800 s, 172800 science, 10 Dark Matter | 300 Ship Fragment, 50 Reinforced Hull Plate, 15 Power Core, 3 Ancient Control Unit | /wiki/02-Ships/Wraith.md
```

### Ресурсы {#tree-resources}

```tree research
Dark Matter Plate | resource, mythical | craft 250 Thulium, 120 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Velkonite Reinforced Plate, 1 Orvium Reinforced Plate, 5 Dark Matter | /wiki/06-Items/Resources.md#dark-matter-plate
```

### Ракеты {#tree-rockets}

```tree research
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
```

### CPU {#tree-cpus}

```tree research
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 20 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 8 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu

Extra Slots CPU I => Extra Slots CPU II => Extra Slots CPU III
Base CPU I => Base CPU II => Jump CPU
```


<!-- research-tree:end -->

## Все технологии {#all-the-technologies}

<!-- research-technologies:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| Технология | Сначала нужна | Класс | Время исследования | Наука | Dark Matter |
| :--- | :--- | :--- | ---: | ---: | ---: |
| [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 мин | 1 800 | – |
| [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Impulse Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 ч | 10 800 | – |
| [Impulse Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Impulse Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 ч | 36 000 | 10 |
| [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | – | A | 30 мин | 1 800 | – |
| [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | [Momentum Thruster II](/wiki/06-Items/Propulsion.md#thrusters) | B | 3 ч | 10 800 | – |
| [Momentum Thruster IV](/wiki/06-Items/Propulsion.md#thrusters) | [Momentum Thruster III](/wiki/06-Items/Propulsion.md#thrusters) | C | 10 ч | 36 000 | 10 |
| [Engine III](/wiki/06-Items/Propulsion.md#engines) | – | B | 3 ч | 10 800 | – |
| [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 мин | 1 800 | – |
| [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 ч | 10 800 | – |
| [Absorption Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Absorption Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | C | 10 ч | 36 000 | 10 |
| [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | – | A | 30 мин | 1 800 | – |
| [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell II](/wiki/06-Items/Shields.md#shield-cells) | B | 3 ч | 10 800 | – |
| [Capacity Shield Cell IV](/wiki/06-Items/Shields.md#shield-cells) | [Capacity Shield Cell III](/wiki/06-Items/Shields.md#shield-cells) | C | 10 ч | 36 000 | 10 |
| [Heavy Shield Core](/wiki/06-Items/Shields.md#shield-cores) | – | B | 3 ч | 10 800 | – |
| [Quantum Laser 3](/wiki/06-Items/Lasers.md#lasers) | – | B | 3 ч | 10 800 | – |
| [Starfire-3](/wiki/06-Items/Lasers.md#lasers) | [Quantum Laser 3](/wiki/06-Items/Lasers.md#lasers) | D | 1 д | 86 400 | 10 |
| [Helios Beam](/wiki/06-Items/Lasers.md#lasers) | [Starfire-3](/wiki/06-Items/Lasers.md#lasers) | D | 1 д | 86 400 | 10 |
| [Nova Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | C | 10 ч | 36 000 | 10 |
| [Apex Amp](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-) | – | C | 10 ч | 36 000 | 10 |
| [Damage Amp II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 ч | 10 800 | – |
| [Shield Wall II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 ч | 10 800 | – |
| [Hull Plating II](/wiki/06-Items/Boosters.md#active-boosters) | – | B | 3 ч | 10 800 | – |
| [Master Drone](/wiki/06-Items/Drones.md#available-drones) | – | C | 10 ч | 36 000 | – |
| [Paragon](/wiki/02-Ships/Paragon.md) | – | B | 6 ч | 21 600 | – |
| [Ironclad](/wiki/02-Ships/Ironclad.md) | – | D | 1 д | 86 400 | 10 |
| [Storm](/wiki/02-Ships/Storm.md) | – | D | 1 д | 86 400 | 10 |
| [Wraith](/wiki/02-Ships/Wraith.md) | – | D | 2 д | 172 800 | 10 |
| [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | – | D | 1 д | 86 400 | 10 |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | B | 3 ч | 10 800 | – |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | – | D | 1 д | 86 400 | 10 |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | – | A | 30 мин | 1 800 | – |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | C | 10 ч | 36 000 | – |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | D | 1 д | 86 400 | 10 |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | – | B | 3 ч | 10 800 | – |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | C | 10 ч | 36 000 | – |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | D | 1 д | 86 400 | 10 |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | – | B | 6 ч | 21 600 | – |

Классы по времени исследования:

| Класс | Время исследования | Технологий | Одна за другой | Наука | Dark Matter |
| :--- | :--- | ---: | ---: | ---: | ---: |
| A | 30 мин | 5 | 2 ч 30 мин | 9 000 | 0 |
| B | от 3 ч до 6 ч | 14 | 2 д | 172 800 | 0 |
| C | 10 ч | 9 | 3 д 18 ч | 324 000 | 60 |
| D | от 1 д до 2 д | 9 | 10 д | 864 000 | 90 |
| Все |  | 37 | 15 д 20 ч 30 мин | 1 369 800 | 150 |

Если исследовать одну за другой, всё дерево займёт 15 д 20 ч 30 мин. С бустом, включённым всё время, — 7 д 22 ч 15 мин; для этого нужно бустов: 8, Thulium: 40 000. Науки уходит столько же.

<!-- research-technologies:end -->

## CPU {#the-cpus}

Новые CPU тоже исследуются здесь, а затем создаются в Сборочном цехе. Та же таблица и те же примечания есть на странице [Устройства](/wiki/06-Items/Extras.md#research-cpus).

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | Время исследования | Сначала нужна | Thulium на создание | Время создания |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 мин | – | 12 000 | 5 мин |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10 ч | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 000 | 10 мин |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1 д | [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75 000 | 15 мин |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3 ч | – | 8 000 | 5 мин |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10 ч | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 20 000 | 10 мин |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1 д | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40 000 | 15 мин |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6 ч | – | 15 000 | 10 мин |

Ни один не продаётся в магазине: исследуйте технологию, затем создайте CPU в Сборочном цехе. Наведите курсор на CPU в его дереве, чтобы увидеть, что для него требует Сборочный цех.

### Extra Slots CPUs {#extra-slots-cpus}

- **Что они делают.** Extra Slots CPU I, II и III добавляют каждому кораблю слоты устройств: 3, 5 и 7; вместе с 3 слотами, которые уже есть у каждого корабля, всего получается 6, 8 и 10. Более высокий CPU заменяет предыдущий: II не прибавляется к I.
- **Устанавливается, а не носится.** Extra Slots CPU — не предмет: когда вы забираете его в Сборочном цехе, он устанавливается в ваш Skylab, действует на каждый корабль в обеих конфигурациях и не занимает слот. Остаётся после вайпа.
- **По порядку.** Создавайте их один за другим: II — только когда установлен I, III — только когда установлен II; до тех пор Сборочный цех подскажет, какой установить сначала. Все три стоят 117 000 Thulium: 12 000, 30 000 и 75 000.

### Jump CPU {#jump-cpu}

- **Что делает.** Прыгает на вашем корабле в любой корпоративный сектор вашего мира — и вашей корпорации, и других, включая их домашние секторы (`M`, `T` и `G`, секторы с 1 по 4) — за **500 Thulium** за прыжок. Число использований не ограничено: платите только Thulium. В Опасный сектор (`DS`) и в нейтральный сектор (`N`) не ведёт никогда.
- **Прыжок.** Нажмите слот JMP, выберите сектор на карте «Звёздная система» и подтвердите: корабль заряжается 5 с, затем прибывает к вратам этого сектора под защитой, как после любого прыжка через врата. После прибытия CPU остывает 30 с.
- **Не в бою.** Нельзя начать в течение 10 с после выстрела или попадания, а выстрел или попадание во время зарядки отменяют прыжок; тогда ничего не списывается. Прыгать в маскировке нельзя.
- **Не из нейтрального сектора:** пилот в нейтральном секторе или без корпорации не может пользоваться им.
- Он может вывести из Опасного сектора, если вы не в бою.

### Base CPUs {#base-cpus}

- **Что делают.** Телепортируют ваш корабль на базу вашей корпорации, в безопасную зону вокруг её станции (`M-1`, `T-1` или `G-1`, сектор с Mission Control) без затрат Thulium. Запускаются со слота BSE на панели.
- **Не в бою.** Зарядка — 10 с, одинаковая для обоих. Нельзя начать в течение 10 с после выстрела или попадания, в маскировке или когда вы уже в безопасной зоне своей базы, а выстрел или попадание во время зарядки её отменяют.

| CPU | Использований | Перезарядка |
| :--- | ---: | ---: |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 10 | 10 мин |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 25 | 5 мин |

- **Расходуется, не перезаряжается.** Каждое использование тратит одно из использований CPU, а CPU без использований исчезает: создайте новый. Если установлены оба, первым расходуется лучший (II).

### Auto-Repair CPU {#auto-repair-cpu}

- **Что делает.** Сам выпускает Repair Drone, установленный в ваших слотах устройств, всякий раз, когда вы могли бы выпустить его вручную: корпус не полон, дрон ещё не выпущен и с последнего попадания прошло 10 с. Порог корпуса настраивать не нужно.
- Занимает собственный слот устройств и ничего не делает без Repair Drone в слоте устройств той же конфигурации. Repair Drone из слота способностей он никогда не выпускает (это кнопка Emergency Repair).
- **Если вы остановите дрон вручную,** CPU не трогает его, пока корпус снова не станет полным или пока вы сами не выпустите дрон.


<!-- research-cpus:end -->
