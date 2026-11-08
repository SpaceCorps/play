<!-- wiki-i18n source: bb8bc80ba6889fba -->
<!-- wiki-i18n title: Dormant-raj -->
# Dormant-raj {#dormant-swarm}

A Dormant-raj egy **Dormant Force** a **Dormant Pulse-aival**: hajók csoportja, amelyek soha nem kezdenek harcot, és nagyon keményen ütnek, ha felébresztik őket. Világonként csak egy van. Az egyik veszélyes szektorból a másikba vándorol, és a rajok közül ez a legkeményebb harc és a leggazdagabb zsákmány: harc a legerősebb hajók nagy csoportjának. A szezon 11. napjától a `DS-4` [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md)-jánál indul, hamarabb tér vissza, és kétszer annyit fizet (lásd a *Dióhéjban* listát).

## Röviden {#at-a-glance}

<!-- dormant-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Hol**: A veszélyes szektorok: `DS-1`, `DS-2`, `DS-3`, `DS-4`; az egyikből a másikba repül
- **Hány**: Világonként egy
- **Megjelenik**: A szezon 4. napjától a wipe-ig (Betában és Gammában: a szezon 1. napjától)
- **Vezér**: Dormant Force
- **Kísérők**: 2 × Dormant Pulse, a vezérrel együtt repülnek
- **A kísérők közel maradnak**: legfeljebb 700 egységre a vezértől
- **A vezér megsemmisül**: A vezetést Dormant Pulse veszi át
- **A vezér megsemmisül**: A kísérők a vezér megsemmisülése után 30 mp múlva eltűnnek, akkor is, ha éppen támadnak
- **Útvonal**: 8–15 perc ideig marad egy térképen, aztán egy másik veszélyes szektor kapujához repül. Soha nem vesz igénybe veszélyes szektorokból kivezető kaput, és soha nem lép be a fekete lyuk gyűrűjébe
- **Visszatér**: 1 óra azután, hogy az egész raj megsemmisült, egy véletlenszerű veszélyes szektorban
- **A szezon 11. napjától**: A `DS-4` [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md)-jánál jelenik meg egy véletlenszerű veszélyes szektor helyett, 30 perc azután tér vissza, hogy az egész raj megsemmisült, és minden hajó ×2-szeresét fizeti (kredit, Thulium, XP és becsület; a zsákmány ugyanaz marad)
- **Értesítés**: Az egész világ pilótái értesülnek arról, mikor jelenik meg a raj, és mikor semmisül meg. Ezek rendszersorok: a chat **Rendszer** lapján jelennek meg, olvasatlan sorok számlálójával, és nem a **Globális** vagy a **Helyi** lapon. Egy jelölő mutatja a veszélyes szektorok térképén és a galaxistérképen. A kill feed megnevezi a pilótát, akinek a kilövést jóváírják.

<!-- dormant-glance:end -->

## A tagok {#the-members}

- **Dormant Force**: teljes erejű Wraith, olyan lézerekkel, amelyek háromszor olyan keményen ütnek, mint egy tipikus felszerelésé. Ő vezeti a rajt, passzív, amíg el nem találják, és **egyenes rakétákat** lő az első pilótára, aki eltalálta.
- **Dormant Pulse**: teljes erejű Paragon, ugyanolyan fajta nehéz lézerekkel, amelyek egyenként kétszer olyan keményen ütnek, mint a Force lézerei, és saját rakétákkal. Egy Pulse-nak kevesebb lézere van, mint a Force-nak, így a teljes sorozata nagyobb a Force-énál, de nem kétszer akkora (a számok lent találhatók). A Pulse-ok a Force közelében repülnek, és ha a Force megsemmisül, egyikük átveszi a vezetést.

Passzívak: soha nem mennek rá egy pilótára. Ha az egyiküket eltalálják, a közelében lévők beszállnak a harcba az első pilóta ellen, aki eltalálta.

## A harc menete {#how-the-fight-goes}

- **Keresd meg.** Az egész világ értesül róla, amikor megjelenik, és egy jelölő mutatja a veszélyes szektorok térképén és a galaxistérképen. A *Röviden* listában szereplő ideig marad egy térképen, aztán egy másik veszélyes szektor kapujához repül, és ugrik; soha nem vesz igénybe veszélyes szektorokból kivezető kaput, és soha nem repül a fekete lyuk gyűrűjébe. A leglassabb hajója sebességével repül, és mint egy pilóta, tűz alatt nem kezd és nem fejez be ugrást. A szezon 11. napjától először közvetlenül a [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) zónáján kívül jelenik meg, ahol egy csoport a mocsár lövegeitől távol várhatja, majd a `DS-4` egyik kapuján át kirepül.
- **Egyedül vagy kevesen nem győzhető le.** Nyolc 8. szintű pilóta Paragonban, x2 vagy x4 lőszerrel, nagyjából egy perc alatt megsemmisíti Alphában, legfeljebb egy hajót veszítve; egy Paragon egyedül megsemmisül, és három vagy négy is, x2 lőszerrel. A Beta és a Gamma rajai erősebbek ([Világok](/wiki/05-Swarms/Swarms.md#the-worlds)), ezért azokhoz a világokhoz nagyobb csoportok kellenek.
- **A lézerei döntik el a harcot.** Együtt egy percen belül megsemmisíthetnek egy Paragont, a legjobb pajzsokkal felszereltet is két percen belül, rakéták nélkül is: gyorsan vidd be a sebzésedet, a legjobb pajzsokkal, amid van.
- **Hajóról hajóra.** Minden hajónak saját hajóteste és saját fizetése van, így a Force vagy egy Pulse előbb is megsemmisülhet. A rajt csak akkor pótolják, ha teljesen megsemmisült, a *Röviden* lista szerinti idő múlva.

## Jutalmak és zsákmány {#rewards-and-drops}

Minden hajó külön fizet, a rá leadott sebzés szerint ([hogyan fizet egy boss megölése](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)), és mindegyik ládát ejt annak a pilótának, aki neki a legtöbb sebzést okozta. A **Force ládája** a fődíj: rengeteg x3 és x4 lőszer, egyféle Epikus rakéta, és időnként egy N.I.K.E. vagy egy N.U.K.E. A **Pulse-ok** ejthetnek Ancient Control Unitot, Power Core-t vagy Dark Mattert. Egy perc harc a rajjal többet fizet, mint egy perc harc a Crystalysszel, a legjobban fizető idegennel. A szezon 11. napjától minden hajó kétszer annyit fizet (lásd a *Dióhéjban* listát); a ládák ugyanazok.

## A számok {#the-numbers}

A raj hajóinak értékei mindhárom világban ([Világok](/wiki/05-Swarms/Swarms.md#the-worlds)). A táblázatok kreditjei, Thuliuma, XP-je és becsülete a szezon 11. napja előtti fizetések; attól a naptól egy kilövés kétszer annyit fizet.

<!-- dormant-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Dormant Force

Alapja: Wraith, hajótestének 100%-a és lézersebzésének 300%-a; a sebessége és a hatótávja a mintahajóé. 5 mp alatt egy egyenes rakétát lő ki: [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | 256 000 | 384 000 | 512 000 |
| Pajzs | 83 400 | 125 100 | 166 800 |
| Lézersebzés (másodpercenként egy sorozat) | 3 120 | 4 680 | 6 240 |
| Sebesség | 210 | 210 | 210 |
| Lézer hatótávja | 800 | 800 | 800 |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Rakétasebzés, legfeljebb | 7 500 | 11 250 | 15 000 |
| Kredit | 185 000 | 370 000 | 555 000 |
| Thulium | 485 | 970 | 1 455 |
| Tapasztalat (XP) | 29 200 | 58 400 | 87 600 |
| Becsület | 127 | 254 | 381 |
| PvE-pont kilövésenként | 25 | 25 | 25 |

**Zsákmány**: egy láda, annak a pilótának, aki a legtöbb sebzést okozta.

| Tárgy | Esély | Mennyiség |
| :--- | ---: | ---: |
| Ultra Core és Experimental Fusion Core, egyenlően elosztva | 100% | összesen 2 000–3 000 |
| Egy a 4 Epikus [rakéta](/wiki/06-Items/Rockets.md) közül, véletlenszerűen | 100% | 30–50 |
| Egy a következők közül: [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) és [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets), véletlenszerűen | 50% | 1 |

### Dormant Pulse

Alapja: Paragon, hajótestének 100%-a és lézersebzésének 600%-a; a sebessége és a hatótávja a mintahajóé. 5 mp alatt egy egyenes rakétát lő ki: [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hajótest | 128 000 | 192 000 | 256 000 |
| Pajzs | 64 570 | 96 855 | 129 140 |
| Lézersebzés (másodpercenként egy sorozat) | 4 320 | 6 480 | 8 640 |
| Sebesség | 230 | 230 | 230 |
| Lézer hatótávja | 800 | 800 | 800 |
| Aggrósugár | csak ha megtámadják | csak ha megtámadják | csak ha megtámadják |
| Rakétasebzés, legfeljebb | 5 000 | 7 500 | 10 000 |
| Kredit | 105 000 | 210 000 | 315 000 |
| Thulium | 275 | 550 | 825 |
| Tapasztalat (XP) | 16 600 | 33 200 | 49 800 |
| Becsület | 72 | 144 | 216 |
| PvE-pont kilövésenként | 11 | 11 | 11 |

**Zsákmány**: egy láda, annak a pilótának, aki a legtöbb sebzést okozta.

| Tárgy | Esély | Mennyiség |
| :--- | ---: | ---: |
| Ancient Control Unit | 20% | 1 |
| Power Core | 20% | 1 |
| Dark Matter | 20% | 1–5 |

<!-- dormant-members:end -->
