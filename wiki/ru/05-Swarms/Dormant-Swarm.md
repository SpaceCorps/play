<!-- wiki-i18n source: fcba1b51b68a9123 -->
<!-- wiki-i18n title: Рой Dormant -->
# Рой Dormant {#dormant-swarm}

Рой Dormant — это **Dormant Force** и его **Dormant Pulse**: группа кораблей, которые никогда не начинают бой и бьют очень сильно, когда их разбудят. В опасных секторах каждого мира он только один ([Deep Void](/wiki/03-Mechanics/Deep-Void.md#the-dormant-swarms-visit) принимает свой собственный визит раз в сутки). Он переходит из одного опасного сектора в другой, и это самый тяжёлый бой и самая богатая добыча среди роёв: бой для большой группы сильнейших кораблей. С 11-го дня сезона он начинает у [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) на `DS-4`, возвращается раньше и платит вдвое больше (см. список *Кратко*).

## Коротко {#at-a-glance}

<!-- dormant-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Где**: Опасные секторы `DS-1`, `DS-2`, `DS-3`, `DS-4`, перелетает из одного в другой
- **Сколько**: По одному в каждом мире
- **Появляется**: С 4-го дня сезона и до вайпа (Бета и Гамма: с 1-го дня сезона)
- **Лидер**: Dormant Force
- **Свита**: 2 × Dormant Pulse, летят вместе с лидером
- **Свита держится**: не дальше 700 единиц от лидера
- **Лидер уничтожен**: Лидером становится Dormant Pulse
- **Лидер уничтожен**: Свита исчезает через 30 с после уничтожения лидера, даже если атакует
- **Перемещения**: Остаётся на карте 8–15 мин, затем летит к вратам другого опасного сектора. Никогда не пользуется вратами, ведущими из опасных секторов, и никогда не входит в кольцо чёрной дыры
- **Возвращается**: Через {{guide:vitals.respawn@Dormant Force#1;Dormant Force#2;Dormant Force#3}} после уничтожения всего роя, в случайном опасном секторе
- **С 11-го дня сезона**: Он появляется у [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) на `DS-4` вместо случайного опасного сектора, возвращается через 30 мин после уничтожения всего роя, и каждый корабль платит ×2 (кредиты, Thulium, XP и честь; добыча остаётся прежней)
- **Оповещения**: Пилоты всего мира узнают, когда рой появляется и когда он уничтожен. Это системные строки: они видны на вкладке **Система** чата, со счётчиком непрочитанных, а не на вкладках **Общий** и **Локальный**. Отметка показывает его на картах опасных секторов и на карте галактики. Лента убийств называет пилота, которому засчитано убийство.

<!-- dormant-glance:end -->

## Участники {#the-members}

- **Dormant Force**: Wraith в полную силу, с лазерами, бьющими втрое сильнее, чем у типичного снаряжения. Он ведёт рой, пассивен, пока по нему не попадут, и стреляет **прямыми ракетами** по первому пилоту, попавшему по нему.
- **Dormant Pulse**: Paragon в полную силу, с тяжёлыми лазерами того же рода, каждый из которых бьёт вдвое сильнее лазера Force, и собственными ракетами. У Pulse лазеров меньше, чем у Force, поэтому весь его залп больше залпа Force, но не вдвое (числа ниже). Pulse летают рядом с Force, а когда Force уничтожен, один из них берёт на себя роль лидера.

Они пассивны: никогда не нападают на пилота первыми. Если попасть по одному из них, находящиеся рядом вступают в бой против первого пилота, попавшего по нему.

## Ход боя {#how-the-fight-goes}

- **Найдите его.** Весь мир узнаёт, когда он появляется, а отметка показывает его на картах опасных секторов и на карте галактики. Он остаётся на карте столько, сколько указано в списке *Коротко*, затем летит к вратам другого опасного сектора и прыгает; он никогда не пользуется вратами, ведущими из опасных секторов, и никогда не заходит в кольцо чёрной дыры. Он летит со скоростью самого медленного корабля и, как пилот, не начинает и не завершает прыжок под огнём. С 11-го дня сезона он сначала появляется сразу за зоной [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md), где группа может ждать его вне досягаемости орудий болота, а затем вылетает через ворота `DS-4`.
- **В одиночку или малой группой его не победить.** Восемь пилотов 8-го уровня на Paragon с боеприпасами x2 или x4 уничтожают его примерно за минуту в Alpha, теряя не больше одного корабля; один Paragon уничтожается, и трое или четверо с боеприпасами x2 тоже. Рои Beta и Gamma сильнее ([Миры](/wiki/05-Swarms/Swarms.md#the-worlds)), поэтому в тех мирах нужны группы побольше.
- **Исход боя решают его лазеры.** Вместе они могут уничтожить Paragon меньше чем за минуту, а Paragon с лучшими щитами — меньше чем за две, с ракетами или без: быстро набирайте урон, с лучшими щитами, какие у вас есть.
- **Корабль за кораблём.** У каждого корабля свой корпус и своя награда, поэтому Force или Pulse может быть уничтожен первым. Рой заменяется, только когда уничтожен целиком, через время, указанное в списке *Коротко*.

## Три этапа лидера {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

У этого боя три этапа ([как они работают](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); каждый происходит один раз.

- **В начале**: Принимает 70% от каждого удара, пока жив хоть один из его Dormant Pulses.
- **Ниже двух третей**: Его Dormant Pulses выпускают ракету каждые 2,5 с в течение 15 с.
- **Ниже трети**: Пока живы все его Dormant Pulses, они лечат его на 5% корпуса в секунду в течение 6 с.

<!-- mob-ladder:end -->

## Награды и добыча {#rewards-and-drops}

Каждый корабль платит сам за себя, по нанесённому ему урону ([как оплачивается убийство босса](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)), и каждый роняет контейнер для пилота, нанёсшего ему больше всех урона. **Контейнер Force** — главный приз: очень много боеприпасов x3 и x4, эпические ракеты одного вида и время от времени N.I.K.E. или N.U.K.E. **Pulse** могут выронить Ancient Control Unit, Power Core или Dark Matter. Минута боя с роем приносит больше, чем минута боя с Crystalys, самым щедрым пришельцем. С 11-го дня сезона каждый корабль платит вдвое больше (см. список *Кратко*); контейнеры прежние.

## Значения {#the-numbers}

Значения кораблей роя в трёх мирах ([Миры](/wiki/05-Swarms/Swarms.md#the-worlds)). Кредиты, Thulium, XP и честь в таблицах — это награда до 11-го дня сезона; с этого дня убийство платит вдвое больше.

<!-- dormant-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Dormant Force

Основа: Wraith, 100% корпуса и 300% урона лазеров; скорость и дальность взяты от исходного корабля. Каждые 5 с выпускает прямую ракету: [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Корпус | {{guide:vitals.hull@Dormant Force#1}} | {{guide:vitals.hull@Dormant Force#2}} | {{guide:vitals.hull@Dormant Force#3}} |
| Щит | {{guide:vitals.shield@Dormant Force#1}} | {{guide:vitals.shield@Dormant Force#2}} | {{guide:vitals.shield@Dormant Force#3}} |
| Урон лазеров (залп в секунду) | {{guide:vitals.dps@Dormant Force#1}} | {{guide:vitals.dps@Dormant Force#2}} | {{guide:vitals.dps@Dormant Force#3}} |
| Скорость | {{guide:vitals.speed@Dormant Force#1}} | {{guide:vitals.speed@Dormant Force#2}} | {{guide:vitals.speed@Dormant Force#3}} |
| Дальность лазеров | 800 | 800 | 800 |
| Радиус агрессии | только если напали | только если напали | только если напали |
| Урон ракет, максимум | {{guide:behaviour.ability:rocket.damage@Dormant Force#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#3}} |
| Кредиты | {{guide:spoils.pay.credits@Dormant Force#1}} | {{guide:spoils.pay.credits@Dormant Force#2}} | {{guide:spoils.pay.credits@Dormant Force#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Force#1}} | {{guide:spoils.pay.thulium@Dormant Force#2}} | {{guide:spoils.pay.thulium@Dormant Force#3}} |
| Опыт (XP) | {{guide:spoils.pay.experience@Dormant Force#1}} | {{guide:spoils.pay.experience@Dormant Force#2}} | {{guide:spoils.pay.experience@Dormant Force#3}} |
| Честь | {{guide:spoils.pay.honor@Dormant Force#1}} | {{guide:spoils.pay.honor@Dormant Force#2}} | {{guide:spoils.pay.honor@Dormant Force#3}} |
| Очки PvE за убийство | 25 | 25 | 25 |

**Добыча**: один контейнер, для пилота, нанёсшего больше всех урона.

| Предмет |
| :--- |
| {{guide:spoils.box@Dormant Force#1;Dormant Force#2;Dormant Force#3}} |

### Dormant Pulse

Основа: Paragon, 100% корпуса и 600% урона лазеров; скорость и дальность взяты от исходного корабля. Каждые 5 с выпускает прямую ракету: [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Корпус | {{guide:vitals.hull@Dormant Pulse#1}} | {{guide:vitals.hull@Dormant Pulse#2}} | {{guide:vitals.hull@Dormant Pulse#3}} |
| Щит | {{guide:vitals.shield@Dormant Pulse#1}} | {{guide:vitals.shield@Dormant Pulse#2}} | {{guide:vitals.shield@Dormant Pulse#3}} |
| Урон лазеров (залп в секунду) | {{guide:vitals.dps@Dormant Pulse#1}} | {{guide:vitals.dps@Dormant Pulse#2}} | {{guide:vitals.dps@Dormant Pulse#3}} |
| Скорость | {{guide:vitals.speed@Dormant Pulse#1}} | {{guide:vitals.speed@Dormant Pulse#2}} | {{guide:vitals.speed@Dormant Pulse#3}} |
| Дальность лазеров | 800 | 800 | 800 |
| Радиус агрессии | только если напали | только если напали | только если напали |
| Урон ракет, максимум | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#3}} |
| Кредиты | {{guide:spoils.pay.credits@Dormant Pulse#1}} | {{guide:spoils.pay.credits@Dormant Pulse#2}} | {{guide:spoils.pay.credits@Dormant Pulse#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Pulse#1}} | {{guide:spoils.pay.thulium@Dormant Pulse#2}} | {{guide:spoils.pay.thulium@Dormant Pulse#3}} |
| Опыт (XP) | {{guide:spoils.pay.experience@Dormant Pulse#1}} | {{guide:spoils.pay.experience@Dormant Pulse#2}} | {{guide:spoils.pay.experience@Dormant Pulse#3}} |
| Честь | {{guide:spoils.pay.honor@Dormant Pulse#1}} | {{guide:spoils.pay.honor@Dormant Pulse#2}} | {{guide:spoils.pay.honor@Dormant Pulse#3}} |
| Очки PvE за убийство | 11 | 11 | 11 |

**Добыча**: один контейнер, для пилота, нанёсшего больше всех урона.

| Предмет |
| :--- |
| {{guide:spoils.box@Dormant Pulse#1;Dormant Pulse#2;Dormant Pulse#3}} |

<!-- dormant-members:end -->
