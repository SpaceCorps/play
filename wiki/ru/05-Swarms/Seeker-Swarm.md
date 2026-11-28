<!-- wiki-i18n source: 7c6bc3eaf70223f5 -->
<!-- wiki-i18n title: Рой Seeker -->
# Рой Seeker {#seeker-swarm}

Рой Seeker — самый маленький из [роёв](/wiki/05-Swarms/Swarms.md): **Boss Seeker** и **Seeker Slave**, которые его охраняют и лечат. Он живёт в секторах, где новички начинают летать, поэтому это первый рой, с которым встречается большинство пилотов. Boss Seeker никогда не начинает бой, но стоит выстрелить в него, он гораздо опаснее [Seeker](/wiki/04-Aliens/Seeker.md), на котором построен.

## Коротко {#at-a-glance}

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Где**: Секторы `x-1` и `x-2` каждой корпорации
- **Сколько**: По одному в каждом из этих секторов, 6 в каждом мире
- **Появляется**: С 4-го дня сезона и до вайпа (Бета и Гамма: с 1-го дня сезона)
- **Лидер**: Boss Seeker
- **Свита**: До 4 × Seeker Slave, новый каждые 10 с
- **Свита держится**: не дальше 500 единиц от лидера
- **Лечение**: Каждый Seeker Slave в пределах 600 единиц от лидера лечит его корпус, в Alpha 50 HP в секунду
- **Лидер уничтожен**: Свита исчезает через 30 с после уничтожения лидера, если только не атакует
- **Возвращается**: Через {{guide:vitals.respawn@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} после уничтожения лидера, в том же секторе
- **Оповещения**: Пилоты сектора узнают, когда лидер появляется и когда он уничтожен. Это системные строки: они видны на вкладке **Система** чата, со счётчиком непрочитанных, а не на вкладках **Общий** и **Локальный**. Лента убийств называет пилота, которому засчитано убийство.

<!-- seeker-glance:end -->

## Участники {#the-members}

- **Boss Seeker**: гораздо более крупный Seeker в оттенке роя и с именем над ним, с корпусом, щитом и уроном, превышающими Seeker в несколько раз (значения ниже). Он пассивен: бродит, пока пилот не попадёт по нему, затем останавливается на месте и стреляет в этого пилота, а находящиеся рядом корабли его роя вступают в бой. Дальность оружия и скорость у него как у Seeker, а корпус он никогда не восстанавливает сам. Его [три этапа](#the-leaders-three-steps) и [особая способность](/wiki/03-Mechanics/Special-Abilities.md) могут это изменить.
- **Seeker Slave**: обычный Seeker в оттенке роя. Slave держатся рядом с боссом, вступают в бой, когда попадают по ближнему кораблю роя, и каждый, кто находится рядом с боссом, лечит его корпус. Slave восстанавливает собственный корпус после передышки, как и Seeker.

## Ход боя {#how-the-fight-goes}

- **Не трогайте его, пока ваш корабль не справится.** Boss Seeker бьёт сильнее, чем выдерживает первый корабль пилота: Protos новичка, ещё без щита, уничтожается за секунды, как только на нём оказываются босс и его Slave.
- **Держитесь вне досягаемости.** Босс и его Slave медленнее Protos, а их оружие бьёт не так далеко, как Quantum Laser II (см. [Лазеры и боеприпасы](/wiki/06-Items/Lasers.md)): пилот с такими лазерами, остающийся за пределами их дальности, не получает урона, пока они стреляют. Пилот с Quantum Laser I не может остаться вне досягаемости.
- **Slave лечат быстрее, чем бьёт одинокий новичок.** Вместе они восстанавливают больше, чем наносят лазеры одного пилота с боеприпасами x1, поэтому берите напарника и боеприпасы x2. Двое пилотов с Quantum Laser II, державшие дистанцию, убивают босса примерно за минуту в Alpha, а с боеприпасами x2 гораздо быстрее.
- **Босс возвращается** через время, указанное в списке *Коротко*, в полной силе, в том же секторе, а его Slave приходят один за другим.

## Три этапа лидера {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

У этого боя три этапа ([как они работают](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); каждый происходит один раз.

- **В начале**: Его Seeker Slaves лечат его быстрее (×2) в течение 8 с.
- **Ниже двух третей**: Появляются его копии (2), а настоящий носит кольцо.
- **Ниже трети**: Улетает от пилотов на 4 с, затем возвращается.

<!-- mob-ladder:end -->

## Награды и добыча {#rewards-and-drops}

Boss Seeker приносит **ровно десять Seeker**: в десять раз больше кредитов, Thulium, опыта и чести, чем Seeker, с разделом по урону между сражавшимися с ним пилотами ([как оплачивается убийство босса](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). В его контейнере добыча десяти Seeker и вдобавок боеприпасы и ракеты ниже эпического уровня, для пилота, нанёсшего больше всех урона. Slave платят немного и ничего не роняют; убивать их — не фарм, потому что они возвращаются вместе с боссом.

## Значения {#the-numbers}

Значения кораблей роя в трёх мирах ([Миры](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker

Основа: Seeker, 400% корпуса, щита и урона; скорость и дальность взяты от исходного корабля.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Корпус | {{guide:vitals.hull@Boss Seeker#1}} | {{guide:vitals.hull@Boss Seeker#2}} | {{guide:vitals.hull@Boss Seeker#3}} |
| Щит | {{guide:vitals.shield@Boss Seeker#1}} | {{guide:vitals.shield@Boss Seeker#2}} | {{guide:vitals.shield@Boss Seeker#3}} |
| Урон лазеров (залп в секунду) | {{guide:vitals.dps@Boss Seeker#1}} | {{guide:vitals.dps@Boss Seeker#2}} | {{guide:vitals.dps@Boss Seeker#3}} |
| Скорость | {{guide:vitals.speed@Boss Seeker#1}} | {{guide:vitals.speed@Boss Seeker#2}} | {{guide:vitals.speed@Boss Seeker#3}} |
| Дальность лазеров | 600 | 600 | 600 |
| Радиус агрессии | только если напали | только если напали | только если напали |
| Кредиты | {{guide:spoils.pay.credits@Boss Seeker#1}} | {{guide:spoils.pay.credits@Boss Seeker#2}} | {{guide:spoils.pay.credits@Boss Seeker#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Seeker#1}} | {{guide:spoils.pay.thulium@Boss Seeker#2}} | {{guide:spoils.pay.thulium@Boss Seeker#3}} |
| Опыт (XP) | {{guide:spoils.pay.experience@Boss Seeker#1}} | {{guide:spoils.pay.experience@Boss Seeker#2}} | {{guide:spoils.pay.experience@Boss Seeker#3}} |
| Честь | {{guide:spoils.pay.honor@Boss Seeker#1}} | {{guide:spoils.pay.honor@Boss Seeker#2}} | {{guide:spoils.pay.honor@Boss Seeker#3}} |
| Очки PvE за убийство | 5 | 5 | 5 |

**Добыча**: один контейнер, для пилота, нанёсшего больше всех урона.

| Предмет |
| :--- |
| {{guide:spoils.box@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} |

### Seeker Slave

Основа: Seeker, 100% корпуса, щита и урона; скорость и дальность взяты от исходного корабля.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Корпус | {{guide:vitals.hull@Seeker Slave#1}} | {{guide:vitals.hull@Seeker Slave#2}} | {{guide:vitals.hull@Seeker Slave#3}} |
| Щит | {{guide:vitals.shield@Seeker Slave#1}} | {{guide:vitals.shield@Seeker Slave#2}} | {{guide:vitals.shield@Seeker Slave#3}} |
| Урон лазеров (залп в секунду) | {{guide:vitals.dps@Seeker Slave#1}} | {{guide:vitals.dps@Seeker Slave#2}} | {{guide:vitals.dps@Seeker Slave#3}} |
| Скорость | {{guide:vitals.speed@Seeker Slave#1}} | {{guide:vitals.speed@Seeker Slave#2}} | {{guide:vitals.speed@Seeker Slave#3}} |
| Дальность лазеров | 600 | 600 | 600 |
| Радиус агрессии | только если напали | только если напали | только если напали |
| Лечит лидера, каждый, в секунду (только корпус) | 50 | 75 | 100 |
| Кредиты | {{guide:spoils.pay.credits@Seeker Slave#1}} | {{guide:spoils.pay.credits@Seeker Slave#2}} | {{guide:spoils.pay.credits@Seeker Slave#3}} |
| Thulium | {{guide:spoils.pay.thulium@Seeker Slave#1}} | {{guide:spoils.pay.thulium@Seeker Slave#2}} | {{guide:spoils.pay.thulium@Seeker Slave#3}} |
| Опыт (XP) | {{guide:spoils.pay.experience@Seeker Slave#1}} | {{guide:spoils.pay.experience@Seeker Slave#2}} | {{guide:spoils.pay.experience@Seeker Slave#3}} |
| Честь | {{guide:spoils.pay.honor@Seeker Slave#1}} | {{guide:spoils.pay.honor@Seeker Slave#2}} | {{guide:spoils.pay.honor@Seeker Slave#3}} |
| Очки PvE за убийство | 1 | 1 | 1 |

**Добыча**: нет. За убийство выплачиваются только кредиты, Thulium, опыт и честь.

<!-- seeker-members:end -->
