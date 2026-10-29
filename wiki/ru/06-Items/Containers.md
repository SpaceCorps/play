<!-- wiki-i18n source: 9cb279aeecb3bbc8 -->
<!-- wiki-i18n title: Контейнеры -->
# Контейнеры {#containers}

<!-- wiki-search: контейнер; контейнеры; кейс; кейсы; лутбокс; шансы; вероятности; гарантия; пити; лента; открытие; хранилище; тигель; архив; капсула; штатив; container; case; crate; lootbox; odds; drop rate; vault; crucible; archive; canister; rack -->

**Контейнер** — это запечатанная находка Mission Control. Когда вы открываете контейнер, сервер определяет одну награду из таблицы, а шанс каждой награды этой таблицы напечатан на этой странице. Страница «Контейнеры» в игре показывает ту же таблицу.

> [!NOTE]
> **Контейнеры — это случайные награды, которые зарабатываются в игре. Их никогда не продают, а шансы опубликованы здесь.** Контейнер нельзя купить, обменять или подарить.

## Что такое контейнер {#what-a-container-is}

- **Заработанный.** Контейнеры зарабатываются в игре. У них нет ни цены, ни ключа: магазин их не продаёт, и никто другой тоже.
- **Только ваш.** Контейнер привязан к вашему аккаунту. Его нельзя обменять, отдать другу или выставить на [Аукцион](/wiki/03-Mechanics/Auction.md), и ничего из того, что выдаёт контейнер, там тоже нельзя выставить.
- **Одинаков для каждого пилота.** Премиум ничего не меняет: он не даёт дополнительных открытий и лучших шансов.
- **Сохраняется после вайпа.** Неоткрытый контейнер остаётся на вашем аккаунте, когда наступает [вайп](/wiki/03-Mechanics/Wipe-Timeline.md). Что вайп делает с наградами, написано в разделе [Вайп](#the-wipe).
- **Открывается на станции.** Вы открываете контейнер на стоянке, на странице «Контейнеры». Сервер определяет награду, когда вы нажимаете «Открыть», и само нажатие ничего не меняет. Что действительно влияет, описано в разделе [Как выбирается награда](#how-a-prize-is-chosen).

## Откуда берутся контейнеры {#where-containers-come-from}

<!-- containers-sources:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

Контейнеры попадают к вам такими путями:

- От администраторов игры
- В награду за ваше звание при вайпе
- В календаре входа
- За достижения

<!-- containers-sources:end -->

## Пять контейнеров {#the-five-containers}

<!-- containers-glance:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Контейнер | Что внутри | Подходит | Закрывается при вайпе | Гарантия | Самая редкая награда |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Хранилище образцов (Specimen Vault)** | Понемногу всего: кредиты, Thulium, боеприпасы, ракеты, снаряжение, пластины, Dark Matter, бустеры и цвета | Любому пилоту | С 30-го дня сезона | Награда класса «Редкий» или выше в течение 10 открытий | 60 000 Thulium; 12 000 000 кредитов: по 0,100% |
| **Литейный тигель (Foundry Crucible)** | Боеприпасы, ракеты, лазеры, усилители, ячейки щита, ускорители и снаряжение, а также корабли (их 5) | Уровень 5 и выше | С 30-го дня сезона | Награда класса «Редкий» или выше в течение 8 открытий | корабль: Wraith: 0,020% |
| **Хроматический архив (Chroma Archive)** | Только внешние виды: скины, цвета, эффекты выхлопа и ауры | Любому пилоту | Остаётся открытым | Награда класса «Эпический» или выше в течение 12 открытий | Crystal Ice; Comet; Halo: по 0,667% |
| **Разведочная капсула (Survey Canister)** | Руда Skylab, пластины, Dark Matter, Cluster Chunks и Thulium | Ядро Skylab 10 и выше | С 30-го дня сезона | Награда класса «Редкий» или выше в течение 8 открытий | 32 × Dark Matter Plate; 50 000 Thulium: по 0,150% |
| **Штатив с реагентами (Reagent Rack)** | Бустеры, EMP Charges, Energetic Walls и боеприпасы | Уровень 4 и выше | С 30-го дня сезона | Награда класса «Редкий» или выше в течение 10 открытий | **Полный спектр**; Cloaking CPU L: по 0,100% |

<!-- containers-glance:end -->

**Подходит** — лишь совет: игра позволяет открыть любой контейнер на любом уровне.

## Классы {#grades}

У каждой награды есть **класс** — одно из слов редкости игры. Класс определяется в розыгрыше первым. На ленте он показан рамкой плитки награды, цветом и формой, чтобы цвет никогда не был единственным признаком.

| Класс | Цвет | Форма |
| :--- | :--- | :--- |
| Обычный | Серый | Круг |
| Необычный | Зелёный | Квадрат |
| Редкий | Синий | Ромб |
| Эпический | Фиолетовый | Шестиугольник |
| Мифический | Розовый | Звезда |
| Легендарный | Золотой | Корона |

У каждого контейнера свой шанс для каждого класса, он указан ниже. То, что у вас есть, никогда не меняет шанс класса.

## Хранилище образцов (Specimen Vault) {#specimen-vault}

*Ксеноархивисты Mission Control запечатывают в пронумерованное хранилище каждую находку, которую нельзя отнести к одной области, и отправляют его нераспечатанным. Никто на станции не знает, что внутри хранилища, пока пилот не сломает печать.*

### Шансы классов {#specimen-vault-grades}

<!-- containers-specimen-vault-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Класс | Шанс | Наград в нём |
| :--- | ---: | ---: |
| Обычный | 38,000% | 9 |
| Необычный | 38,000% | 8 |
| Редкий | 17,000% | 8 |
| Эпический | 5,500% | 5 |
| Мифический | 1,300% | 4 |
| Легендарный | 0,200% | 2 |

<!-- containers-specimen-vault-grades:end -->

### Каждая награда {#specimen-vault-prizes}

<!-- containers-specimen-vault-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Класс | Награда | Шанс |
| :--- | :--- | ---: |
| Обычный | 50 000 кредитов | 5,000% |
| Обычный | 250 Thulium | 4,000% |
| Обычный | 10 000 × Standard Battery | 4,000% |
| Обычный | 500 × Advanced Plasma | 4,000% |
| Обычный | 250 × Ultra Core | 3,000% |
| Обычный | **Набор ракет I**: 100 одного из 4, шансы равны: Ember I, Lancet I, Rivet I, Scatter I | 6,000% |
| Обычный | **Кузнечная пыль**: 1 500 × Daraxium + 1 500 × Nyxite | 3,000% |
| Обычный | 4 000 × Ship Fragment | 3,000% |
| Обычный | 1 ч Experience Booster | 6,000% |
| Необычный | 150 000 кредитов | 6,000% |
| Необычный | 750 Thulium | 6,000% |
| Необычный | 750 × Ultra Core | 4,500% |
| Необычный | 340 × Experimental Fusion Core | 4,000% |
| Необычный | **Набор ракет II**: 190 одного из 4, шансы равны: Ember II, Lancet II, Rivet II, Scatter II | 6,000% |
| Необычный | 10 × Velkonite Reinforced Plate | 4,000% |
| Необычный | 1 ч Laser Damage Booster I | 4,000% |
| Необычный | **Образец цвета**: один из 11, шансы равны: Cobalt, Indigo, Violet, Magenta, Crimson, Ember, Sunset, Gold, Emerald, Jade, Teal | 3,500% |
| Редкий | 400 000 кредитов | 2,500% |
| Редкий | 2 000 Thulium | 2,500% |
| Редкий | 10 × Dark Matter | 1,500% |
| Редкий | **Набор ракет III**: 400 одного из 4, шансы равны: Ember III, Lancet III, Rivet III, Scatter III | 2,000% |
| Редкий | 1 000 × Experimental Fusion Core | 1,500% |
| Редкий | 9 × Orvium Reinforced Plate | 1,500% |
| Редкий | 4 ч Laser Damage Booster I | 1,500% |
| Редкий | **Деталь уровня II**: один из 4, шансы равны: Absorption Shield Cell II, Capacity Shield Cell II, Impulse Thruster II, Momentum Thruster II | 4,000% |
| Эпический | 1 200 000 кредитов | 1,200% |
| Эпический | 6 000 Thulium | 1,200% |
| Эпический | 30 × Dark Matter | 0,900% |
| Эпический | 26 × Orvium Reinforced Plate | 0,900% |
| Эпический | **Деталь уровня III**: один из 5, шансы равны: Absorption Shield Cell III, Capacity Shield Cell III, Impulse Thruster III, Momentum Thruster III, Starfire-III | 1,300% |
| Мифический | 18 000 Thulium | 0,400% |
| Мифический | 12 × Dark Matter Plate | 0,300% |
| Мифический | Helios Beam | 0,300% |
| Мифический | **Усилитель уровня IV**: один из 3, шансы равны: Damage Amp IV, Crit Amp IV, Penetration Amp IV | 0,300% |
| Легендарный | 60 000 Thulium | 0,100% |
| Легендарный | 12 000 000 кредитов | 0,100% |

<!-- containers-specimen-vault-prizes:end -->

**Образец цвета** даёт цвет, которого у вас ещё нет. Если у вас уже есть все цвета образца, он вместо этого выплачивает Thulium за переработку ([Дубликаты и переработка](#duplicates-and-salvage)).

### Гарантия {#specimen-vault-guarantee}

<!-- containers-specimen-vault-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Гарантия**: награда класса «Редкий» или выше хотя бы раз за каждые 10 открытий
- **Шанс награды класса «Редкий» или выше без неё**: 24,000%
- **С гарантией, за много открытий**: 25,649%
- **Открытия, которые определяет гарантия**: 2,170%
- **Открытий между двумя такими наградами, в среднем**: 3,899

<!-- containers-specimen-vault-guarantee:end -->

## Литейный тигель (Foundry Crucible) {#foundry-crucible}

*Литейные Dormant остыли, когда последняя плавка ещё была в тигле: боеприпасы, готовое снаряжение и в самых глубоких — корпус, который так и не достроили. Инженеры Mission Control вырезали тигли из руин и передают их пилотам запечатанными, потому что никто не может сказать, в каком из них корпус.*

### Шансы классов {#foundry-crucible-grades}

<!-- containers-foundry-crucible-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Класс | Шанс | Наград в нём |
| :--- | ---: | ---: |
| Обычный | 45,000% | 6 |
| Необычный | 30,000% | 7 |
| Редкий | 16,000% | 6 |
| Эпический | 6,500% | 6 |
| Мифический | 2,200% | 5 |
| Легендарный | 0,300% | 2 |

<!-- containers-foundry-crucible-grades:end -->

### Каждая награда {#foundry-crucible-prizes}

<!-- containers-foundry-crucible-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Класс | Награда | Шанс |
| :--- | :--- | ---: |
| Обычный | 30 000 × Standard Battery | 7,000% |
| Обычный | 1 500 × Advanced Plasma | 7,000% |
| Обычный | 750 × Ultra Core | 7,000% |
| Обычный | 340 × Experimental Fusion Core | 5,000% |
| Обычный | **Набор ракет I**: 300 одного из 4, шансы равны: Ember I, Lancet I, Rivet I, Scatter I | 11,000% |
| Обычный | **Лазерный комплект**: Quantum Laser II + Damage Amp I + Crit Amp I + Penetration Amp I | 8,000% |
| Необычный | 2 250 × Ultra Core | 4,500% |
| Необычный | 1 020 × Experimental Fusion Core | 4,500% |
| Необычный | **Набор ракет II**: 560 одного из 4, шансы равны: Ember II, Lancet II, Rivet II, Scatter II | 8,500% |
| Необычный | Basic Shield Core | 4,500% |
| Необычный | **Три усилителя уровня II**: Damage Amp II + Crit Amp II + Penetration Amp II | 4,000% |
| Необычный | Repair Drone IV | 3,900% |
| Необычный | корабль: Nomad | 0,100% |
| Редкий | 1 800 × Experimental Fusion Core | 2,500% |
| Редкий | **Набор ракет III**: 500 одного из 4, шансы равны: Ember III, Lancet III, Rivet III, Scatter III | 3,000% |
| Редкий | Quantum Laser III | 2,400% |
| Редкий | **Деталь уровня II**: один из 4, шансы равны: Absorption Shield Cell II, Capacity Shield Cell II, Impulse Thruster II, Momentum Thruster II | 4,500% |
| Редкий | **Усилитель уровня III**: один из 3, шансы равны: Damage Amp III, Crit Amp III, Penetration Amp III | 3,500% |
| Редкий | корабль: Paragon | 0,100% |
| Эпический | **Ячейка или ускоритель уровня III**: один из 4, шансы равны: Absorption Shield Cell III, Capacity Shield Cell III, Impulse Thruster III, Momentum Thruster III | 3,000% |
| Эпический | Starfire-III | 1,200% |
| Эпический | Heavy Shield Core | 1,200% |
| Эпический | Cloaking CPU M | 1,000% |
| Эпический | корабль: Storm | 0,050% |
| Эпический | корабль: Ironclad | 0,050% |
| Мифический | Helios Beam | 0,600% |
| Мифический | **Ячейка или ускоритель уровня IV**: один из 4, шансы равны: Absorption Shield Cell IV, Capacity Shield Cell IV, Impulse Thruster IV, Momentum Thruster IV | 0,700% |
| Мифический | **Усилитель уровня IV**: один из 3, шансы равны: Damage Amp IV, Crit Amp IV, Penetration Amp IV | 0,480% |
| Мифический | Cloaking CPU L | 0,400% |
| Мифический | корабль: Wraith | 0,020% |
| Легендарный | **Арсенал Helios**: Helios Beam + Damage Amp IV + Crit Amp IV + Penetration Amp IV | 0,150% |
| Легендарный | 50 000 Thulium | 0,150% |

<!-- containers-foundry-crucible-prizes:end -->

Корабли перечислены с их базовыми шансами. Корабль, который у вас уже есть, никогда не выпадает, поэтому ваши собственные шансы могут немного отличаться от этой таблицы: см. [Корабли](#the-ships).

### Гарантия {#foundry-crucible-guarantee}

<!-- containers-foundry-crucible-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Гарантия**: награда класса «Редкий» или выше хотя бы раз за каждые 8 открытий
- **Шанс награды класса «Редкий» или выше без неё**: 25,000%
- **С гарантией, за много открытий**: 27,781%
- **Открытия, которые определяет гарантия**: 3,708%
- **Открытий между двумя такими наградами, в среднем**: 3,600

<!-- containers-foundry-crucible-guarantee:end -->

## Хроматический архив (Chroma Archive) {#chroma-archive}

*Dormant строили из фиолетово-чёрного кристалла с фиолетовыми прожилками, а их архивисты хранили цвет в тонких стеклянных пластинах, которые перекрашивают всё, к чему их прижать. Каждый Хроматический архив — это запечатанная стопка таких пластин, внесённая в указатель колористами Mission Control и не читанная никем, пока пилот его не откроет.*

Хроматический архив сначала определяет класс, а затем один внешний вид этого класса, которого у вас ещё нет, и все такие внешние виды равновероятны. Коллекция — это одна награда: она даёт все её скины, которых у вас нет. Шанс в таблице указан для пилота, у которого нет ни одного внешнего вида этого класса. По мере коллекционирования он растёт, потому что в розыгрыше остаётся меньше внешних видов. Сами внешние виды описаны в разделе [Косметика](/wiki/06-Items/Cosmetics.md).

### Шансы классов {#chroma-archive-grades}

<!-- containers-chroma-archive-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Класс | Шанс | Внешних видов в нём |
| :--- | ---: | ---: |
| Обычный | 6,000% | 1 |
| Необычный | 50,000% | 14 |
| Редкий | 30,000% | 8 |
| Эпический | 12,000% | 12 |
| Мифический | 2,000% | 3 |
| Легендарный | 0,000% | – |

<!-- containers-chroma-archive-grades:end -->

### Каждая награда {#chroma-archive-prizes}

<!-- containers-chroma-archive-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Класс | Внешний вид | Шанс, если у вас нет ни одного из этого класса |
| :--- | :--- | ---: |
| Обычный | Glow (аура) | 6,000% |
| Необычный | Company Supporter (коллекция) | 3,571% |
| Необычный | Cobalt (цвет) | 3,571% |
| Необычный | Indigo (цвет) | 3,571% |
| Необычный | Violet (цвет) | 3,571% |
| Необычный | Magenta (цвет) | 3,571% |
| Необычный | Crimson (цвет) | 3,571% |
| Необычный | Ember (цвет) | 3,571% |
| Необычный | Sunset (цвет) | 3,571% |
| Необычный | Gold (цвет) | 3,571% |
| Необычный | Emerald (цвет) | 3,571% |
| Необычный | Jade (цвет) | 3,571% |
| Необычный | Teal (цвет) | 3,571% |
| Необычный | Twin (эффект выхлопа) | 3,571% |
| Необычный | Breath (аура) | 3,571% |
| Редкий | Nature White (коллекция) | 3,750% |
| Редкий | Sunrise Orbit (коллекция) | 3,750% |
| Редкий | Seeker Burnt (цвет) | 3,750% |
| Редкий | Pirate Brick (цвет) | 3,750% |
| Редкий | Pulse (эффект выхлопа) | 3,750% |
| Редкий | Helix (эффект выхлопа) | 3,750% |
| Редкий | Motes (аура) | 3,750% |
| Редкий | Shimmer (аура) | 3,750% |
| Эпический | Midnight Gala (коллекция) | 1,000% |
| Эпический | Blue Marble (коллекция) | 1,000% |
| Эпический | Mimosa (коллекция) | 1,000% |
| Эпический | Olive Branch (коллекция) | 1,000% |
| Эпический | Steady Pulse (коллекция) | 1,000% |
| Эпический | Hollow Night (коллекция) | 1,000% |
| Эпический | Dormant Void (цвет) | 1,000% |
| Эпический | Ancient Amethyst (цвет) | 1,000% |
| Эпический | Embers (эффект выхлопа) | 1,000% |
| Эпический | Gradient (эффект выхлопа) | 1,000% |
| Эпический | Sparkle (аура) | 1,000% |
| Эпический | Wreath (аура) | 1,000% |
| Мифический | Crystal Ice (цвет) | 0,667% |
| Мифический | Comet (эффект выхлопа) | 0,667% |
| Мифический | Halo (аура) | 0,667% |

<!-- containers-chroma-archive-prizes:end -->

### Гарантия {#chroma-archive-guarantee}

<!-- containers-chroma-archive-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Гарантия**: награда класса «Эпический» или выше хотя бы раз за каждые 12 открытий
- **Шанс награды класса «Эпический» или выше без неё**: 14,000%
- **С гарантией, за много открытий**: 16,740%
- **Открытия, которые определяет гарантия**: 3,186%
- **Открытий между двумя такими наградами, в среднем**: 5,974

<!-- containers-chroma-archive-guarantee:end -->

## Разведочная капсула (Survey Canister) {#survey-canister}

*Разведочные зонды вылетают из Skylab в туман карты вселенной, и каждый возвращается запечатанной капсулой с образцами керна. Руда из жилы, которую никто не нанёс на карту, аномалии и порой осколок чего-то более древнего, чем сама карта: Mission Control заносит капсулу в каталог по ячейке, а разбираться предоставляет владельцу Skylab.*

### Шансы классов {#survey-canister-grades}

<!-- containers-survey-canister-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Класс | Шанс | Наград в нём |
| :--- | ---: | ---: |
| Обычный | 45,000% | 8 |
| Необычный | 30,000% | 7 |
| Редкий | 16,000% | 6 |
| Эпический | 6,500% | 5 |
| Мифический | 2,200% | 3 |
| Легендарный | 0,300% | 2 |

<!-- containers-survey-canister-grades:end -->

### Каждая награда {#survey-canister-prizes}

<!-- containers-survey-canister-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Класс | Награда | Шанс |
| :--- | :--- | ---: |
| Обычный | 240 × Velkonite (в Skylab) | 7,000% |
| Обычный | 160 × Orvium (в Skylab) | 7,000% |
| Обычный | 1 300 × Reinforced Hull Plate | 5,000% |
| Обычный | 9 000 × Ship Fragment | 6,000% |
| Обычный | **Кузнечные кристаллы**: 4 000 × Cataclysite + 3 000 × Quorvium | 5,000% |
| Обычный | 450 × Power Core | 5,000% |
| Обычный | 450 Thulium | 5,000% |
| Обычный | 4 × Regular Cluster Chunk | 5,000% |
| Необычный | 780 × Velkonite (в Skylab) | 5,000% |
| Необычный | 510 × Orvium (в Skylab) | 5,000% |
| Необычный | 19 × Velkonite Reinforced Plate | 4,000% |
| Необычный | 7 × Dark Matter | 5,000% |
| Необычный | 8 × Ancient Control Unit | 3,000% |
| Необычный | 1 450 Thulium | 4,000% |
| Необычный | 3 × Mythical Cluster Chunk | 4,000% |
| Редкий | 17 × Dark Matter | 3,500% |
| Редкий | 15 × Orvium Reinforced Plate | 3,000% |
| Редкий | 1 900 × Velkonite (в Skylab) | 2,500% |
| Редкий | 1 230 × Orvium (в Skylab) | 2,500% |
| Редкий | 2 × Legendary Cluster Chunk | 1,500% |
| Редкий | 3 500 Thulium | 3,000% |
| Эпический | 45 × Dark Matter | 1,500% |
| Эпический | 39 × Orvium Reinforced Plate | 1,200% |
| Эпический | **Ящик смешанных пластин**: 60 × Velkonite Reinforced Plate + 20 × Orvium Reinforced Plate | 1,200% |
| Эпический | 9 000 Thulium | 1,500% |
| Эпический | 6 × Dark Matter Plate | 1,100% |
| Мифический | 13 × Dark Matter Plate | 0,900% |
| Мифический | 20 000 Thulium | 0,800% |
| Мифический | 100 × Dark Matter | 0,500% |
| Легендарный | 32 × Dark Matter Plate | 0,150% |
| Легендарный | 50 000 Thulium | 0,150% |

<!-- containers-survey-canister-prizes:end -->

Руда с пометкой *(в Skylab)* попадает в рудный банк вашего Skylab, насколько позволяет место вашего Хранилища ресурсов. Остальное приходит как такая же руда в инвентарь. См. [Skylab](/wiki/03-Mechanics/Skylab.md).

### Гарантия {#survey-canister-guarantee}

<!-- containers-survey-canister-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Гарантия**: награда класса «Редкий» или выше хотя бы раз за каждые 8 открытий
- **Шанс награды класса «Редкий» или выше без неё**: 25,000%
- **С гарантией, за много открытий**: 27,781%
- **Открытия, которые определяет гарантия**: 3,708%
- **Открытий между двумя такими наградами, в среднем**: 3,600

<!-- containers-survey-canister-guarantee:end -->

## Штатив с реагентами (Reagent Rack) {#reagent-rack}

*Исследовательский центр Skylab перегоняет бустеры, с которыми вы летаете, из ампул с реагентами, а штатив — это то, что остаётся, когда партию обрывают: отмеренная доза каждого реагента в своей запечатанной ампуле. Дозы стареют только пока корабль летит, так что штатив может стоять на полке сколько угодно.*

### Шансы классов {#reagent-rack-grades}

<!-- containers-reagent-rack-grades:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Класс | Шанс | Наград в нём |
| :--- | ---: | ---: |
| Обычный | 45,000% | 5 |
| Необычный | 33,000% | 8 |
| Редкий | 15,000% | 8 |
| Эпический | 5,500% | 6 |
| Мифический | 1,300% | 2 |
| Легендарный | 0,200% | 2 |

<!-- containers-reagent-rack-grades:end -->

### Каждая награда {#reagent-rack-prizes}

<!-- containers-reagent-rack-prizes:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Класс | Награда | Шанс |
| :--- | :--- | ---: |
| Обычный | 1 ч Experience Booster | 11,000% |
| Обычный | 1 ч Honor Booster | 11,000% |
| Обычный | 1 ч Shield Regen Booster | 9,000% |
| Обычный | Energetic Wall I | 8,000% |
| Обычный | 500 × Advanced Plasma | 6,000% |
| Необычный | 1 ч Laser Damage Booster I | 5,000% |
| Необычный | 1 ч Shield Wall Booster I | 5,000% |
| Необычный | 1 ч Hull Plating Booster I | 5,000% |
| Необычный | 1 ч Resource Magnet Booster | 3,500% |
| Необычный | 2 ч Experience Booster | 4,500% |
| Необычный | 2 ч Honor Booster | 3,500% |
| Необычный | EMP Charge | 3,500% |
| Необычный | 3 × Energetic Wall I | 3,000% |
| Редкий | 2 ч Laser Damage Booster I | 2,500% |
| Редкий | 2 ч Shield Wall Booster I | 2,000% |
| Редкий | 2 ч Hull Plating Booster I | 2,000% |
| Редкий | 4 ч Experience Booster | 2,000% |
| Редкий | 4 ч Honor Booster | 2,000% |
| Редкий | 2 ч Loot Luck Booster | 1,500% |
| Редкий | 3 × EMP Charge | 2,000% |
| Редкий | 2 ч Resource Magnet Booster | 1,000% |
| Эпический | 4 ч Laser Damage Booster I | 1,200% |
| Эпический | 4 ч Shield Wall Booster I | 1,000% |
| Эпический | 4 ч Hull Plating Booster I | 1,000% |
| Эпический | 4 ч Resource Magnet Booster | 0,700% |
| Эпический | 4 ч Loot Luck Booster | 0,900% |
| Эпический | 8 × EMP Charge | 0,700% |
| Мифический | **Боевой штатив**: 4 ч Laser Damage Booster I + 4 ч Shield Wall Booster I + 4 ч Hull Plating Booster I | 0,700% |
| Мифический | **Штатив учёного**: 4 ч Experience Booster + 4 ч Honor Booster + 4 ч Resource Magnet Booster + 4 ч Loot Luck Booster | 0,600% |
| Легендарный | **Полный спектр**: 4 ч Laser Damage Booster I + 4 ч Shield Wall Booster I + 4 ч Hull Plating Booster I + 4 ч Shield Regen Booster + 4 ч Experience Booster + 4 ч Honor Booster + 4 ч Resource Magnet Booster + 4 ч Loot Luck Booster | 0,100% |
| Легендарный | Cloaking CPU L | 0,100% |

<!-- containers-reagent-rack-prizes:end -->

Время бустера добавляется к тому же бустеру, если он уже действует, и идёт только пока вы летите. См. [Бустеры](/wiki/06-Items/Boosters.md).

### Гарантия {#reagent-rack-guarantee}

<!-- containers-reagent-rack-guarantee:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Гарантия**: награда класса «Редкий» или выше хотя бы раз за каждые 10 открытий
- **Шанс награды класса «Редкий» или выше без неё**: 22,000%
- **С гарантией, за много открытий**: 24,001%
- **Открытия, которые определяет гарантия**: 2,565%
- **Открытий между двумя такими наградами, в среднем**: 4,167

<!-- containers-reagent-rack-guarantee:end -->

## Как выбирается награда {#how-a-prize-is-chosen}

Сервер выбирает, когда вы открываете контейнер, в три шага:

1. **Класс.** Одно случайное число сопоставляется с шансами классов.
2. **Награда.** Второе число сопоставляется с шансами наград этого класса. Корабля, который у вас уже есть, среди них нет (см. [Корабли](#the-ships)).
3. **Выбор среди равных.** Награда, в которой сказано *один из* нескольких, даёт один из них, все равновероятны.

Числа берутся из генератора случайных чисел операционной системы сервера и определяются после того, как ваш контейнер забран. Ничто из того, что вы отправляете, не может их изменить: ни кнопка, ни время.

Две вещи из прошлого всё же учитываются. Счётчик гарантии переходит от одного открытия к следующему; его описывает гарантия каждого контейнера выше. А то, что у вас уже есть, включая выигранное в прошлых открытиях, меняет набор наград, оставшихся в розыгрыше: корабля, который у вас есть, среди них нет, а внешний вид, который у вас есть, не выпадает, пока в его классе остаётся внешний вид, которого у вас нет (см. [Дубликаты и переработка](#duplicates-and-salvage) и [Корабли](#the-ships)). То, что у вас есть, никогда не меняет шансы классов.

<!-- containers-draw:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- Каждый шанс — целое число долей из 100 000. Одна доля — это 0,001%.

<!-- containers-draw:end -->

**Каждое открытие записывается** вместе с его сидом (случайным числом, которое использовал сервер), выпавшими числами, хешем таблицы, из которой выбирали, и наградами, которые убрало из розыгрыша то, что у вас есть. Их можно прочитать в **Подробностях** в **Истории** на странице «Контейнеры».

**Одно из них можно проверить самому.** Инструмент `scripts/containers-verify.py` в исходном коде игры читает таблицу и подробности открытия и говорит, вытекают ли класс, награда и выбор из сида. Метод короткий:

```text
stream(seed, id): value i, for i = 0, 1, 2, ...
  = the first 8 bytes (big endian) of HMAC-SHA256(
      key     = seed,
      message = "sc-container-v1|" + id + "|" + i )
  where i is written as 4 bytes, big endian
below(n): take values until one is under 2^64 - (2^64 mod n),
  then use it modulo n (no modulo bias)
grade:    roll = below(total of the grades in play);
  the grade is the first whose running sum is above the roll
prize:    sub = below(total of the prizes left in that grade);
  the prize is the first whose running sum is above sub
choice:   a prize that is "one of N" gives the alternative
  number below(N)
seed = the 32 bytes shown under Details; id = the container's id.
When the guarantee forces an opening, only the guaranteed grade
and better are in play.
```

## Дубликаты и переработка {#duplicates-and-salvage}

- **Внешний вид**, который у вас есть, не выпадает, пока в классе остаётся внешний вид, которого у вас нет. Коллекция считается имеющейся, когда у вас есть все её скины.
- Когда у вас есть все внешние виды класса, награда вместо этого выплачивает **переработку**: Thulium по классу. Для гарантии она считается наградой этого класса.
- **Предметы** никогда не превращаются в Thulium: они складываются в стопки или приходят как есть.
- **Корабли** никогда не выдаются дважды и никогда не выплачиваются как переработка (см. [Корабли](#the-ships)).

<!-- containers-salvage:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Класс | Thulium |
| :--- | ---: |
| Обычный | 25 |
| Необычный | 100 |
| Редкий | 400 |
| Эпический | 1 200 |
| Мифический | 4 000 |

<!-- containers-salvage:end -->

## Корабли {#the-ships}

В Литейном тигле может быть корабль. В таблице корабли перечислены с их **базовыми шансами** — шансами для пилота, у которого нет ни одного из них. Это опубликованные шансы.

Корабль, который у вас уже есть, не может выпасть никогда. Он убирается из розыгрыша, а его доля переходит к остальным наградам того же класса пропорционально их собственным шансам. Так что то, что у вас есть, меняет ваши собственные шансы: чуть выше у остальных наград этого класса. Шансы классов не меняются никогда, как и гарантия. Дизайн, сделанный из корабля, считается за этот корабль: Paragon THUNDER считается за Paragon.

<!-- containers-ships:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

| Корабль | Класс | Шанс |
| :--- | :--- | ---: |
| Nomad | Необычный | 0,100% |
| Paragon | Редкий | 0,100% |
| Storm | Эпический | 0,050% |
| Ironclad | Эпический | 0,050% |
| Wraith | Мифический | 0,020% |
| **Все: 5** | | **0,320%** |

Пример: у вас есть корабль Nomad. Класс «Необычный» сохраняет свой шанс, но 100 долей корабля Nomad из 30 000 долей класса убираются из розыгрыша, так что каждая другая награда класса «Необычный» в 30 000 / 29 900 = 1,0033 раза вероятнее, чем указано в таблице.

Следующая таблица — на случай, когда у вас есть все корабли класса. Если у вас только некоторые из них, из розыгрыша убираются только их доли, поэтому множитель меньше.

| Класс | Доли класса | Доли всех его кораблей | Во сколько раз вероятнее каждая другая награда класса |
| :--- | ---: | ---: | ---: |
| Необычный | 30 000 | 100 | ×1,0033 |
| Редкий | 16 000 | 100 | ×1,0063 |
| Эпический | 6 500 | 100 | ×1,0156 |
| Мифический | 2 200 | 20 | ×1,0092 |

Пример: в классе «Эпический» кораблей: 2. Если у вас есть только корабль Storm, из розыгрыша убираются лишь его 50 долей из 6 500, так что каждая другая награда класса «Эпический» в 6 500 / 6 450 = 1,0078 раза вероятнее, а не в 1,0156 раза.

<!-- containers-ships:end -->

Страница «Контейнеры» в игре показывает ваши собственные шансы рядом с опубликованными, когда они различаются. Корабль, который у вас есть, остаётся в списке, затемнённым, со строкой «Этот корабль у вас уже есть, поэтому он не может выпасть из контейнера.»

## Вайп {#the-wipe}

- **Неоткрытые контейнеры сохраняются.** Они остаются на вашем аккаунте после вайпа.
- **Предметы из контейнера — обычные предметы.** При вайпе они пропадают, если вы не возьмёте их в Транспортный тайник ([Хронология вайпа](/wiki/03-Mechanics/Wipe-Timeline.md)).
- **Внешние виды и корабли остаются с вами**, как любой внешний вид и любой корабль. Кредиты, Thulium и оставшееся время бустеров при вайпе подчиняются своим правилам.
- **Ничего из контейнера нельзя выставить на Аукцион.**

<!-- containers-wipe:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Закрыты с 30-го дня сезона**: Хранилище образцов, Литейный тигель, Разведочная капсула, Штатив с реагентами. То, что в них лежит, пропало бы при вайпе, поэтому открыть их до конца вайпа нельзя.
- **Баннер**: страница «Контейнеры» предупреждает вас с 28-го дня сезона.
- **Остаётся открытым**: Хроматический архив. Внутри только внешние виды, а вайп их сохраняет.

<!-- containers-wipe:end -->

## Версия таблицы {#version-of-the-table}

Каждый шанс на этой странице — это таблица сервера игры. Когда шанс меняется, таблица получает новую версию и новый хеш, а каждое открытие записывает хеш таблицы, из которой его определяли.

<!-- containers-version:begin -->
<!-- Generated from server/Resources/Containers.json (and Cosmetics.json) by scripts/containers-wiki.sh: don't edit by hand. -->

- **Версия таблицы**: 1
- **Хеш таблицы (первые 12 символов)**: `23aa20f1a5ad`

Что изменилось:

- Версия 1: Первая опубликованная таблица.

<!-- containers-version:end -->
