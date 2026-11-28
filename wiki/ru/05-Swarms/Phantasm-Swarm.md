<!-- wiki-i18n source: 2eff9c368449da99 -->
<!-- wiki-i18n title: Рой Phantasm -->
# Рой Phantasm {#phantasm-swarm}

Рой Phantasm — это **Boss Phantasm** со своими **Phantasm Guard**: огромный [Phantasm](/wiki/04-Aliens/Phantasm.md), который никогда не начинает бой, и более мелкие, которые держатся рядом с ним и лечат его. Он живёт во внешних секторах корпораций, `x-3` и `x-4`, и это бой для группы пилотов среднего уровня.

## Коротко {#at-a-glance}

<!-- phantasm-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Где**: Секторы `x-3` и `x-4` каждой корпорации
- **Сколько**: По одному в каждом из этих секторов, 6 в каждом мире
- **Появляется**: С 4-го дня сезона и до вайпа (Бета и Гамма: с 1-го дня сезона)
- **Лидер**: Boss Phantasm
- **Свита**: До 4 × Phantasm Guard, новый каждые 10 с
- **Свита держится**: не дальше 500 единиц от лидера
- **Лечение**: Каждый Phantasm Guard в пределах 600 единиц от лидера лечит его корпус, в Alpha 30 HP в секунду
- **Лидер уничтожен**: Свита исчезает через 30 с после уничтожения лидера, если только не атакует
- **Возвращается**: Через {{guide:vitals.respawn@Boss Phantasm#1;Boss Phantasm#2;Boss Phantasm#3}} после уничтожения лидера, в том же секторе
- **Оповещения**: Пилоты сектора узнают, когда лидер появляется и когда он уничтожен. Это системные строки: они видны на вкладке **Система** чата, со счётчиком непрочитанных, а не на вкладках **Общий** и **Локальный**. Лента убийств называет пилота, которому засчитано убийство.

<!-- phantasm-glance:end -->

## Участники {#the-members}

- **Boss Phantasm**: более крупный Phantasm в оттенке роя и с именем над ним, со своим корпусом, щитом и залпом лазеров (значения ниже). Он пассивен: бродит, пока пилот не попадёт по нему, затем преследует этого пилота и стреляет в него, а находящиеся рядом корабли его роя вступают в бой. Дальность оружия и скорость у него как у Phantasm, а корпус он никогда не восстанавливает сам. Его [три этапа](#the-leaders-three-steps) и [особая способность](/wiki/03-Mechanics/Special-Abilities.md) могут это изменить.
- **Phantasm Guard**: более мелкий Phantasm в оттенке роя. Guard держатся рядом с боссом, вступают в бой, когда попадают по ближнему кораблю роя, и каждый, кто находится рядом с боссом, лечит его корпус. Guard восстанавливает собственный корпус после передышки, как и Phantasm.

## Ход боя {#how-the-fight-goes}

- **Возьмите группу.** Трое пилотов 4–5 уровня с боеприпасами x2 уничтожают его примерно за полторы минуты в Alpha, теряя не больше одного корабля; одиночный пилот этого уровня уничтожен, а двое едва побеждают, и только пока удары распределяются. Корабли получше и боеприпасы x4 делают бой гораздо быстрее.
- **Стреляйте в босса, а не в Guard.** Guard падает за секунды, но новый приходит так часто, как сказано в списке *Коротко*, а то, что лечат Guard, — малая часть того, что наносит группа: оставить их в покое стоит немного времени, гоняться за ними — больше.
- **Beta и Gamma тяжелее.** Рои этих миров сильнее ([Миры](/wiki/05-Swarms/Swarms.md#the-worlds)), поэтому нужно больше пилотов или лучшие боеприпасы.
- **Следите за сектором.** `x-4` — PvP-сектор в Alpha, а `x-3` и `x-4` — в Beta и Gamma ([Миры](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): соперник может вмешаться в бой или дождаться контейнера. Оставьте один корабль группы в дозоре.
- **Босс возвращается** через время, указанное в списке *Коротко*, в полной силе, в том же секторе, а его Guard приходят один за другим.

## Три этапа лидера {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

У этого боя три этапа ([как они работают](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); каждый происходит один раз.

- **В начале**: Каждый из его Phantasm Guards ставит слой щита, равный 10% собственного корпуса.
- **Ниже двух третей**: Появляются его копии (3), а настоящий носит кольцо.
- **Ниже трети**: Прыгает примерно на 2 500 единиц от пилотов, а его Phantasm Guards возвращаются целыми вокруг него.

<!-- mob-ladder:end -->

## Награды и добыча {#rewards-and-drops}

Boss Phantasm платит соразмерно бою, которым он является: минута боя с ним приносит больше, чем минута боя с Goombah, самым щедро оплачиваемым пришельцем этих секторов. Выплата делится по урону между сражавшимися с ним пилотами ([как оплачивается убийство босса](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). В его контейнере добыча Phantasm в многократном размере (Ship Fragment, Daraxium и Nyxite) и боеприпасы с ракетами, для пилота, нанёсшего больше всех урона. Guard платят немного и ничего не роняют; убивать их — не фарм, потому что они возвращаются вместе с боссом.

## Значения {#the-numbers}

Значения кораблей роя в трёх мирах ([Миры](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- phantasm-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Phantasm

Основа: Phantasm, 2 000% корпуса и 300% урона лазеров; скорость и дальность взяты от исходного корабля.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Корпус | {{guide:vitals.hull@Boss Phantasm#1}} | {{guide:vitals.hull@Boss Phantasm#2}} | {{guide:vitals.hull@Boss Phantasm#3}} |
| Щит | {{guide:vitals.shield@Boss Phantasm#1}} | {{guide:vitals.shield@Boss Phantasm#2}} | {{guide:vitals.shield@Boss Phantasm#3}} |
| Урон лазеров (залп в секунду) | {{guide:vitals.dps@Boss Phantasm#1}} | {{guide:vitals.dps@Boss Phantasm#2}} | {{guide:vitals.dps@Boss Phantasm#3}} |
| Скорость | {{guide:vitals.speed@Boss Phantasm#1}} | {{guide:vitals.speed@Boss Phantasm#2}} | {{guide:vitals.speed@Boss Phantasm#3}} |
| Дальность лазеров | 700 | 700 | 700 |
| Радиус агрессии | только если напали | только если напали | только если напали |
| Кредиты | {{guide:spoils.pay.credits@Boss Phantasm#1}} | {{guide:spoils.pay.credits@Boss Phantasm#2}} | {{guide:spoils.pay.credits@Boss Phantasm#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Phantasm#1}} | {{guide:spoils.pay.thulium@Boss Phantasm#2}} | {{guide:spoils.pay.thulium@Boss Phantasm#3}} |
| Опыт (XP) | {{guide:spoils.pay.experience@Boss Phantasm#1}} | {{guide:spoils.pay.experience@Boss Phantasm#2}} | {{guide:spoils.pay.experience@Boss Phantasm#3}} |
| Честь | {{guide:spoils.pay.honor@Boss Phantasm#1}} | {{guide:spoils.pay.honor@Boss Phantasm#2}} | {{guide:spoils.pay.honor@Boss Phantasm#3}} |
| Очки PvE за убийство | 8 | 8 | 8 |

**Добыча**: один контейнер, для пилота, нанёсшего больше всех урона.

| Предмет |
| :--- |
| {{guide:spoils.box@Boss Phantasm#1;Boss Phantasm#2;Boss Phantasm#3}} |

### Phantasm Guard

Основа: Phantasm, 50% корпуса, щита и урона; скорость и дальность взяты от исходного корабля.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Корпус | {{guide:vitals.hull@Phantasm Guard#1}} | {{guide:vitals.hull@Phantasm Guard#2}} | {{guide:vitals.hull@Phantasm Guard#3}} |
| Щит | {{guide:vitals.shield@Phantasm Guard#1}} | {{guide:vitals.shield@Phantasm Guard#2}} | {{guide:vitals.shield@Phantasm Guard#3}} |
| Урон лазеров (залп в секунду) | {{guide:vitals.dps@Phantasm Guard#1}} | {{guide:vitals.dps@Phantasm Guard#2}} | {{guide:vitals.dps@Phantasm Guard#3}} |
| Скорость | {{guide:vitals.speed@Phantasm Guard#1}} | {{guide:vitals.speed@Phantasm Guard#2}} | {{guide:vitals.speed@Phantasm Guard#3}} |
| Дальность лазеров | 700 | 700 | 700 |
| Радиус агрессии | только если напали | только если напали | только если напали |
| Лечит лидера, каждый, в секунду (только корпус) | 30 | 45 | 60 |
| Кредиты | {{guide:spoils.pay.credits@Phantasm Guard#1}} | {{guide:spoils.pay.credits@Phantasm Guard#2}} | {{guide:spoils.pay.credits@Phantasm Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Phantasm Guard#1}} | {{guide:spoils.pay.thulium@Phantasm Guard#2}} | {{guide:spoils.pay.thulium@Phantasm Guard#3}} |
| Опыт (XP) | {{guide:spoils.pay.experience@Phantasm Guard#1}} | {{guide:spoils.pay.experience@Phantasm Guard#2}} | {{guide:spoils.pay.experience@Phantasm Guard#3}} |
| Честь | {{guide:spoils.pay.honor@Phantasm Guard#1}} | {{guide:spoils.pay.honor@Phantasm Guard#2}} | {{guide:spoils.pay.honor@Phantasm Guard#3}} |
| Очки PvE за убийство | 1 | 1 | 1 |

**Добыча**: нет. За убийство выплачиваются только кредиты, Thulium, опыт и честь.

<!-- phantasm-members:end -->
