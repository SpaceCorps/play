<!-- wiki-i18n source: 2b3edf7bcb1d9673 -->
<!-- wiki-i18n title: Рой Crystalys -->
# Рой Crystalys {#crystalys-swarm}

Рой Crystalys — это **Boss Crystalys** со своими **Crystalys Guard**: самый прочный из пришельцев, [Crystalys](/wiki/04-Aliens/Crystalys.md), но крупнее, со стражами, которые держатся рядом с ним и лечат его. Он живёт в [опасных секторах](/wiki/01-General/Danger-Sectors.md) `DS-1`, `DS-2` и `DS-3`, по одному в каждом, и никогда не покидает свой сектор. Опасные секторы — это PvP-секторы, поэтому бой рассчитан на большую группу сильнейших пилотов, и босс там не единственная опасность.

## Коротко {#at-a-glance}

<!-- crystalys-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Где**: Опасные секторы `DS-1`, `DS-2`, `DS-3`
- **Сколько**: По одному в каждом из этих секторов, 3 в каждом мире
- **Появляется**: С 4-го дня сезона и до вайпа (Бета и Гамма: с 1-го дня сезона)
- **Лидер**: Boss Crystalys
- **Свита**: До 3 × Crystalys Guard, новый каждые 10 с
- **Свита держится**: не дальше 500 единиц от лидера
- **Лечение**: Каждый Crystalys Guard в пределах 600 единиц от лидера лечит его корпус, в Alpha 250 HP в секунду
- **Лидер уничтожен**: Свита исчезает через 30 с после уничтожения лидера, если только не атакует
- **Возвращается**: Через {{guide:vitals.respawn@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} после уничтожения лидера, в том же секторе
- **Оповещения**: Пилоты сектора узнают, когда лидер появляется и когда он уничтожен. Это системные строки: они видны на вкладке **Система** чата, со счётчиком непрочитанных, а не на вкладках **Общий** и **Локальный**. Лента убийств называет пилота, которому засчитано убийство.

<!-- crystalys-glance:end -->

## Участники {#the-members}

- **Boss Crystalys**: более крупный Crystalys в оттенке роя и с именем над ним, со своим корпусом, щитом и залпом лазеров (значения ниже). Он пассивен: бродит, пока пилот не попадёт по нему, затем преследует этого пилота и стреляет в него, а находящиеся рядом корабли его роя вступают в бой. Дальность оружия и скорость у него как у Crystalys, а корпус он никогда не восстанавливает сам. Его [три этапа](#the-leaders-three-steps) и [особая способность](/wiki/03-Mechanics/Special-Abilities.md) могут это изменить.
- **Crystalys Guard**: более мелкий Crystalys в оттенке роя. Guard держатся рядом с боссом, вступают в бой, когда попадают по ближнему кораблю роя, и каждый, кто находится рядом с боссом, лечит его корпус. Guard восстанавливает собственный корпус после передышки, как и Crystalys.

## Ход боя {#how-the-fight-goes}

- **Возьмите большую группу.** В Alpha хватит шести пилотов 8 уровня на Paragon с боеприпасами x2, если его огонь распределяется между ними, и девяти, если он весь приходится на одного пилота; с боеприпасами x4 — пяти и шести. Чем больше пилотов, тем раньше заканчивается бой и тем меньше кораблей теряется, а одиночный пилот будет уничтожен.
- **Стреляйте в босса, а не в Guard.** Guard падает за секунды, но новый приходит так часто, как сказано в списке *Коротко*, а то, что лечат Guard, — малая часть того, что наносит группа: оставить их в покое стоит немного времени, гоняться за ними — больше.
- **Beta и Gamma тяжелее.** Рои этих миров сильнее ([Миры](/wiki/05-Swarms/Swarms.md#the-worlds)), поэтому нужно больше пилотов или лучшие боеприпасы.
- **Опасные секторы — это PvP.** Соперник может напасть на группу посреди боя и дождаться контейнера: он принадлежит пилоту, нанёсшему больше всех урона (и его клану), 30 секунд, а потом любому ([Груз](/wiki/03-Mechanics/Cargo.md)). Не идите в одиночку.
- **Босс возвращается** через время, указанное в списке *Коротко*, в полной силе, в том же секторе, а его Guard приходят один за другим.

## Три этапа лидера {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

У этого боя три этапа ([как они работают](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); каждый происходит один раз.

- **В начале**: Принимает 50% от каждого удара в течение 8 с.
- **Ниже двух третей**: Кольцо в 700 единиц бьёт каждый корабль внутри на 4 его залпов, и он выпускает 4 ракет.
- **Ниже трети**: Восстанавливает 20% корпуса и щита (серия урона это прерывает), и приходят ещё 3 Crystalys Guards, живых не больше 6.

<!-- mob-ladder:end -->

## Награды и добыча {#rewards-and-drops}

Boss Crystalys платит соразмерно бою, которым он является: минута боя с ним приносит больше, чем минута боя с Crystalys, самым щедро оплачиваемым пришельцем. Выплата делится по урону между сражавшимися с ним пилотами ([как оплачивается убийство босса](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). В его контейнере Cataclysite и Quorvium, время от времени Power Core, Ancient Control Unit или Dark Matter, боеприпасы x3 и x4 и эпические ракеты, для пилота, нанёсшего больше всех урона. Guard платят немного и ничего не роняют; убивать их — не фарм, потому что они возвращаются вместе с боссом.

## Значения {#the-numbers}

Значения кораблей роя в трёх мирах ([Миры](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- crystalys-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Crystalys

Основа: Crystalys, 350% корпуса и 100% урона лазеров; скорость и дальность взяты от исходного корабля.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Корпус | {{guide:vitals.hull@Boss Crystalys#1}} | {{guide:vitals.hull@Boss Crystalys#2}} | {{guide:vitals.hull@Boss Crystalys#3}} |
| Щит | {{guide:vitals.shield@Boss Crystalys#1}} | {{guide:vitals.shield@Boss Crystalys#2}} | {{guide:vitals.shield@Boss Crystalys#3}} |
| Урон лазеров (залп в секунду) | {{guide:vitals.dps@Boss Crystalys#1}} | {{guide:vitals.dps@Boss Crystalys#2}} | {{guide:vitals.dps@Boss Crystalys#3}} |
| Скорость | {{guide:vitals.speed@Boss Crystalys#1}} | {{guide:vitals.speed@Boss Crystalys#2}} | {{guide:vitals.speed@Boss Crystalys#3}} |
| Дальность лазеров | 900 | 900 | 900 |
| Радиус агрессии | только если напали | только если напали | только если напали |
| Кредиты | {{guide:spoils.pay.credits@Boss Crystalys#1}} | {{guide:spoils.pay.credits@Boss Crystalys#2}} | {{guide:spoils.pay.credits@Boss Crystalys#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Crystalys#1}} | {{guide:spoils.pay.thulium@Boss Crystalys#2}} | {{guide:spoils.pay.thulium@Boss Crystalys#3}} |
| Опыт (XP) | {{guide:spoils.pay.experience@Boss Crystalys#1}} | {{guide:spoils.pay.experience@Boss Crystalys#2}} | {{guide:spoils.pay.experience@Boss Crystalys#3}} |
| Честь | {{guide:spoils.pay.honor@Boss Crystalys#1}} | {{guide:spoils.pay.honor@Boss Crystalys#2}} | {{guide:spoils.pay.honor@Boss Crystalys#3}} |
| Очки PvE за убийство | 30 | 30 | 30 |

**Добыча**: один контейнер, для пилота, нанёсшего больше всех урона.

| Предмет |
| :--- |
| {{guide:spoils.box@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} |

### Crystalys Guard

Основа: Crystalys, 15% корпуса, щита и урона; скорость и дальность взяты от исходного корабля.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Корпус | {{guide:vitals.hull@Crystalys Guard#1}} | {{guide:vitals.hull@Crystalys Guard#2}} | {{guide:vitals.hull@Crystalys Guard#3}} |
| Щит | {{guide:vitals.shield@Crystalys Guard#1}} | {{guide:vitals.shield@Crystalys Guard#2}} | {{guide:vitals.shield@Crystalys Guard#3}} |
| Урон лазеров (залп в секунду) | {{guide:vitals.dps@Crystalys Guard#1}} | {{guide:vitals.dps@Crystalys Guard#2}} | {{guide:vitals.dps@Crystalys Guard#3}} |
| Скорость | {{guide:vitals.speed@Crystalys Guard#1}} | {{guide:vitals.speed@Crystalys Guard#2}} | {{guide:vitals.speed@Crystalys Guard#3}} |
| Дальность лазеров | 900 | 900 | 900 |
| Радиус агрессии | только если напали | только если напали | только если напали |
| Лечит лидера, каждый, в секунду (только корпус) | 250 | 375 | 500 |
| Кредиты | {{guide:spoils.pay.credits@Crystalys Guard#1}} | {{guide:spoils.pay.credits@Crystalys Guard#2}} | {{guide:spoils.pay.credits@Crystalys Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Crystalys Guard#1}} | {{guide:spoils.pay.thulium@Crystalys Guard#2}} | {{guide:spoils.pay.thulium@Crystalys Guard#3}} |
| Опыт (XP) | {{guide:spoils.pay.experience@Crystalys Guard#1}} | {{guide:spoils.pay.experience@Crystalys Guard#2}} | {{guide:spoils.pay.experience@Crystalys Guard#3}} |
| Честь | {{guide:spoils.pay.honor@Crystalys Guard#1}} | {{guide:spoils.pay.honor@Crystalys Guard#2}} | {{guide:spoils.pay.honor@Crystalys Guard#3}} |
| Очки PvE за убийство | 6 | 6 | 6 |

**Добыча**: нет. За убийство выплачиваются только кредиты, Thulium, опыт и честь.

<!-- crystalys-members:end -->
