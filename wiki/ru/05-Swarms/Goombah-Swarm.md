<!-- wiki-i18n source: 38ffa8ba7cbf5000 -->
<!-- wiki-i18n title: Рой Goombah -->
# Рой Goombah {#goombah-swarm}

Рой Goombah — это **Boss Goombah** со своими **Goombah Guard**: огромный [Goombah](/wiki/04-Aliens/Goombah.md), который никогда не начинает бой, и более мелкие, которые держатся рядом с ним и лечат его. Он живёт в тех же секторах, что и [рой Phantasm](/wiki/05-Swarms/Phantasm-Swarm.md), — `x-3` и `x-4`, — и это бой для группы сильнейших пилотов корпоративных секторов.

## Коротко {#at-a-glance}

<!-- goombah-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Где**: Секторы `x-3` и `x-4` каждой корпорации
- **Сколько**: По одному в каждом из этих секторов, 6 в каждом мире
- **Появляется**: С 4-го дня сезона и до вайпа (Бета и Гамма: с 1-го дня сезона)
- **Лидер**: Boss Goombah
- **Свита**: До 4 × Goombah Guard, новый каждые 10 с
- **Свита держится**: не дальше 500 единиц от лидера
- **Лечение**: Каждый Goombah Guard в пределах 600 единиц от лидера лечит его корпус, в Alpha 110 HP в секунду
- **Лидер уничтожен**: Свита исчезает через 30 с после уничтожения лидера, если только не атакует
- **Возвращается**: Через {{guide:vitals.respawn@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} после уничтожения лидера, в том же секторе
- **Оповещения**: Пилоты сектора узнают, когда лидер появляется и когда он уничтожен. Это системные строки: они видны на вкладке **Система** чата, со счётчиком непрочитанных, а не на вкладках **Общий** и **Локальный**. Лента убийств называет пилота, которому засчитано убийство.

<!-- goombah-glance:end -->

## Участники {#the-members}

- **Boss Goombah**: более крупный Goombah в оттенке роя и с именем над ним, со своим корпусом, щитом и залпом лазеров (значения ниже). Он пассивен: бродит, пока пилот не попадёт по нему, затем преследует этого пилота и стреляет в него, а находящиеся рядом корабли его роя вступают в бой. Дальность оружия и скорость у него как у Goombah, а корпус он никогда не восстанавливает сам. Его [три этапа](#the-leaders-three-steps) и [особая способность](/wiki/03-Mechanics/Special-Abilities.md) могут это изменить.
- **Goombah Guard**: более мелкий Goombah в оттенке роя. Guard держатся рядом с боссом, вступают в бой, когда попадают по ближнему кораблю роя, и каждый, кто находится рядом с боссом, лечит его корпус. Guard восстанавливает собственный корпус после передышки, как и Goombah.

## Ход боя {#how-the-fight-goes}

- **Возьмите группу сильнейших кораблей.** Трое пилотов 8 уровня с боеприпасами x2 уничтожают его примерно за 75 секунд в Alpha, теряя не больше одного корабля; двоим нужны боеприпасы x4, а пилоты более низких уровней наносят недостаточно урона, чтобы победить.
- **Стреляйте в босса, а не в Guard.** Guard падает за секунды, но новый приходит так часто, как сказано в списке *Коротко*, а то, что лечат Guard, — малая часть того, что наносит группа: оставить их в покое стоит немного времени, гоняться за ними — больше.
- **Beta и Gamma тяжелее.** Рои этих миров сильнее ([Миры](/wiki/05-Swarms/Swarms.md#the-worlds)), поэтому нужно больше пилотов или лучшие боеприпасы.
- **Следите за сектором.** `x-4` — PvP-сектор в Alpha, а `x-3` и `x-4` — в Beta и Gamma ([Миры](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): соперник может вмешаться в бой или дождаться контейнера. Оставьте один корабль группы в дозоре.
- **Босс возвращается** через время, указанное в списке *Коротко*, в полной силе, в том же секторе, а его Guard приходят один за другим.

## Три этапа лидера {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

У этого боя три этапа ([как они работают](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); каждый происходит один раз.

- **В начале**: Принимает 50% от каждого удара в течение 6 с.
- **Ниже двух третей**: Его урон ×1,5, а скорость ×1,25 в течение 10 с.
- **Ниже трети**: Восстанавливает 25% корпуса и щита (серия урона это прерывает), а его Goombah Guards тем временем лечат его быстрее (×2).

<!-- mob-ladder:end -->

## Награды и добыча {#rewards-and-drops}

Boss Goombah платит соразмерно бою, которым он является: минута боя с ним приносит больше, чем минута боя с Goombah, самым щедро оплачиваемым пришельцем этих секторов. Выплата делится по урону между сражавшимися с ним пилотами ([как оплачивается убийство босса](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). В его контейнере добыча Goombah в несколько раз большем размере (Cataclysite, Quorvium, Power Core, Reinforced Hull Plate и Ship Fragment) и боеприпасы с ракетами, для пилота, нанёсшего больше всех урона. Guard платят немного и ничего не роняют; убивать их — не фарм, потому что они возвращаются вместе с боссом.

## Значения {#the-numbers}

Значения кораблей роя в трёх мирах ([Миры](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- goombah-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Goombah

Основа: Goombah, 400% корпуса и 100% урона лазеров; скорость и дальность взяты от исходного корабля.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Корпус | {{guide:vitals.hull@Boss Goombah#1}} | {{guide:vitals.hull@Boss Goombah#2}} | {{guide:vitals.hull@Boss Goombah#3}} |
| Щит | {{guide:vitals.shield@Boss Goombah#1}} | {{guide:vitals.shield@Boss Goombah#2}} | {{guide:vitals.shield@Boss Goombah#3}} |
| Урон лазеров (залп в секунду) | {{guide:vitals.dps@Boss Goombah#1}} | {{guide:vitals.dps@Boss Goombah#2}} | {{guide:vitals.dps@Boss Goombah#3}} |
| Скорость | {{guide:vitals.speed@Boss Goombah#1}} | {{guide:vitals.speed@Boss Goombah#2}} | {{guide:vitals.speed@Boss Goombah#3}} |
| Дальность лазеров | 800 | 800 | 800 |
| Радиус агрессии | только если напали | только если напали | только если напали |
| Кредиты | {{guide:spoils.pay.credits@Boss Goombah#1}} | {{guide:spoils.pay.credits@Boss Goombah#2}} | {{guide:spoils.pay.credits@Boss Goombah#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Goombah#1}} | {{guide:spoils.pay.thulium@Boss Goombah#2}} | {{guide:spoils.pay.thulium@Boss Goombah#3}} |
| Опыт (XP) | {{guide:spoils.pay.experience@Boss Goombah#1}} | {{guide:spoils.pay.experience@Boss Goombah#2}} | {{guide:spoils.pay.experience@Boss Goombah#3}} |
| Честь | {{guide:spoils.pay.honor@Boss Goombah#1}} | {{guide:spoils.pay.honor@Boss Goombah#2}} | {{guide:spoils.pay.honor@Boss Goombah#3}} |
| Очки PvE за убийство | 14 | 14 | 14 |

**Добыча**: один контейнер, для пилота, нанёсшего больше всех урона.

| Предмет |
| :--- |
| {{guide:spoils.box@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} |

### Goombah Guard

Основа: Goombah, 20% корпуса, щита и урона; скорость и дальность взяты от исходного корабля.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Корпус | {{guide:vitals.hull@Goombah Guard#1}} | {{guide:vitals.hull@Goombah Guard#2}} | {{guide:vitals.hull@Goombah Guard#3}} |
| Щит | {{guide:vitals.shield@Goombah Guard#1}} | {{guide:vitals.shield@Goombah Guard#2}} | {{guide:vitals.shield@Goombah Guard#3}} |
| Урон лазеров (залп в секунду) | {{guide:vitals.dps@Goombah Guard#1}} | {{guide:vitals.dps@Goombah Guard#2}} | {{guide:vitals.dps@Goombah Guard#3}} |
| Скорость | {{guide:vitals.speed@Goombah Guard#1}} | {{guide:vitals.speed@Goombah Guard#2}} | {{guide:vitals.speed@Goombah Guard#3}} |
| Дальность лазеров | 800 | 800 | 800 |
| Радиус агрессии | только если напали | только если напали | только если напали |
| Лечит лидера, каждый, в секунду (только корпус) | 110 | 165 | 220 |
| Кредиты | {{guide:spoils.pay.credits@Goombah Guard#1}} | {{guide:spoils.pay.credits@Goombah Guard#2}} | {{guide:spoils.pay.credits@Goombah Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Goombah Guard#1}} | {{guide:spoils.pay.thulium@Goombah Guard#2}} | {{guide:spoils.pay.thulium@Goombah Guard#3}} |
| Опыт (XP) | {{guide:spoils.pay.experience@Goombah Guard#1}} | {{guide:spoils.pay.experience@Goombah Guard#2}} | {{guide:spoils.pay.experience@Goombah Guard#3}} |
| Честь | {{guide:spoils.pay.honor@Goombah Guard#1}} | {{guide:spoils.pay.honor@Goombah Guard#2}} | {{guide:spoils.pay.honor@Goombah Guard#3}} |
| Очки PvE за убийство | 3 | 3 | 3 |

**Добыча**: нет. За убийство выплачиваются только кредиты, Thulium, опыт и честь.

<!-- goombah-members:end -->
