<!-- wiki-i18n source: 630505c843ae163b -->
<!-- wiki-i18n title: Бустеры -->
# Бустеры {#boosters}

<!-- wiki-search: damage amp; damage amp ii; shield wall; shield wall ii; hull plating; hull plating ii; shield regen; experience kit; honor beacon; resource magnet; loot luck -->

Бустеры временно меняют характеристики, усиливая боевые возможности вашего корабля, его защиту, набор уровней и сбор ресурсов.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Дерево предметов {#item-tree}

То, что создаёт Сборочный цех, сначала требует своей технологии; наведите курсор на предмет, чтобы увидеть, сколько длится её исследование. Дерево технологий, топливо и буст: [Исследования](/wiki/03-Mechanics/Research.md).

```tree
Experience Booster | booster, common | buy 8000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Honor Booster | booster, common | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Laser Damage Booster 2 | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster 2 | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster 2 | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Regen Booster | booster, rare | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall Booster 1 | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating Booster 1 | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Resource Magnet Booster | booster, rare | buy 18000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Laser Damage Booster 1 | booster, rare | buy 20000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Loot Luck Booster | booster, legendary | buy 30000 Thulium | /wiki/06-Items/Boosters.md#active-boosters

Shield Wall Booster 1 -> Shield Wall Booster 2
Hull Plating Booster 1 -> Hull Plating Booster 2
Laser Damage Booster 1 -> Laser Damage Booster 2
```
<!-- item-tree:end -->

## Правила сложения {#stacking-rules}

Бустеры работают по аддитивной системе:
1. **Проценты бонусов складываются**: если вы купите два разных бустера, и каждый даёт +10% к урону лазеров, суммарный бонус составит **+20% к урону лазеров**.
2. **Длительность растёт кратно**: повторная покупка _того же_ бустера продлевает время его действия. Таймеры _разных_ бустеров идут параллельно.
3. **Таймеры**: активные бустеры показаны в HUD, в окне «Бустеры»: там видны суммарные бонусы по группам и ближайшее окончание действия.

---

## Активные бустеры {#active-boosters}

Каждый бустер действует базовые **10 часов** и включается сразу после покупки, получения или сбора. Три бустера **второй ступени** (Laser Damage Booster 2, Shield Wall Booster 2 и Hull Plating Booster 2) не продаются: вы исследуете их технологию в Skylab ([Исследования](/wiki/03-Mechanics/Research.md)), затем создаёте их в Сборочном цехе, а когда вы забираете такой бустер, его 10 часов начинаются сразу, как при покупке.

| Название | Редкость | Базовый эффект (10 часов) | Цена (Thulium) |
| :--- | :--- | :--- | :--- |
| **Laser Damage Booster 1** | Редкий | +10% к урону лазеров | 20 000 |
| **Laser Damage Booster 2** | Редкий | +10% к урону лазеров | Сборочный цех: 20 000 |
| **Shield Wall Booster 1** | Редкий | +25% к ёмкости щита (максимум очков щита) | 15 000 |
| **Shield Wall Booster 2** | Редкий | +25% к ёмкости щита (максимум очков щита) | Сборочный цех: 15 000 |
| **Hull Plating Booster 1** | Редкий | +10% к максимальной прочности | 15 000 |
| **Hull Plating Booster 2** | Редкий | +10% к максимальной прочности | Сборочный цех: 15 000 |
| **Shield Regen Booster** | Редкий | +25% к скорости восстановления щита (очков щита в секунду) | 10 000 |
| **Experience Booster** | Обычный | +20% к получаемому опыту | 8 000 |
| **Honor Booster** | Обычный | +20% к получаемым очкам чести | 10 000 |
| **Resource Magnet Booster** | Редкий | +25% к содержимому грузовых контейнеров | 18 000 |
| **Loot Luck Booster** | Легендарный | +5% к шансу выпадения редкой добычи с NPC | 30 000 |

> [!NOTE]
> **Бустер или усилитель?** Это разные вещи. У каждого бустера в названии есть **Booster**, он работает по таймеру, и вставлять в него нечего: **Laser Damage Booster 1** и **Laser Damage Booster 2** дают +10% к урону лазеров на 10 часов, из магазина или из Сборочного цеха. **Damage Amp**, **Crit Amp** и **Penetration Amp** (ступени I–IV) — лазерные усилители: модули, которые вставляются в слот усилителя лазера, без таймера ([Лазеры и боеприпасы](/wiki/06-Items/Lasers.md#laser-amplifiers-amps-)). До 0.4.12 бустеры назывались Damage Amp и Damage Amp II, Shield Wall и Shield Wall II, Hull Plating и Hull Plating II, Shield Regen, Experience Kit, Honor Beacon, Resource Magnet и Loot Luck; те, что у вас шли, продолжили идти под новыми названиями.

---

## Усиление щита: три вида {#shield-boosts-three-kinds}

У щитов три отдельные характеристики, и каждое усиление щита повышает ровно одну из них. В окне «Бустеры» они показаны раздельно, у каждой свой значок и своя сумма:

| Вид | Что это | Что её повышает |
| :--- | :--- | :--- |
| **Ёмкость щита** | Ваш максимум очков щита | Shield Wall Booster 1, Shield Wall Booster 2, постоянный бонус **Shield Capacity Boost** (магазин сезона) |
| **Поглощение щита** | Доля каждого попадания, которую принимают ваши щиты (остальное получает корпус); может превышать 100% | Постоянный бонус **Shield Absorbance Boost** (магазин сезона): +0,1 пункта за уровень за 25 ОВ, не больше +10 пунктов. Ни один бустер его не повышает |
| **Регенерация щита** | Очки щита, восстанавливаемые за секунду | Shield Regen Booster. Ни один постоянный бонус её не повышает |

Усиления одного вида складываются; в другой вид они никогда не засчитываются. Постоянные бонусы описаны в разделе [Прогресс между сезонами](/wiki/03-Mechanics/Wipe-Timeline.md); сами характеристики — на странице [Механика щитов](/wiki/03-Mechanics/Shields.md).
