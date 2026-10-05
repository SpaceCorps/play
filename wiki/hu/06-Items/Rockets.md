<!-- wiki-i18n source: 615b51aa98d6a27d -->
<!-- wiki-i18n title: Rakéták -->
# Rakéták {#rockets}

A rakéták a lézereid mellett egy második fegyver: néhány másodpercenként egy lövés, amely sokkal erősebben üt, mint egy lézersortűz. Tizenkét rakéta négy fajtában, fajtánként három fokozattal, plusz kettő, amelyet csak a Gyártás állít elő, és **egyetlen, 5 másodperces töltési időzítő, amelyen mindegyik osztozik**, bármelyiket lősd is ki. A Gyakori és a Ritka rakéták **kreditért** vehetők; a négy Epikus rakéta **Thuliumért**. Egy [drónformáció](/wiki/03-Mechanics/Formations.md) növelheti a rakéta sebzését, és hosszabbá vagy rövidebbé teheti ezt az időzítőt: lásd: [Drónformációk és rakéták](#drone-formations-and-rockets).

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Tárgyfa {#item-tree}

Amit a Gyártás elkészít, ahhoz előbb a technológiája kell; vidd az egeret egy tárgy fölé, hogy lásd, mennyi ideig tart a kutatása. A technológiafa, az üzemanyag és a boost: [Kutatás](/wiki/03-Mechanics/Research.md).

```tree
Lancet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets

Lancet I -> Lancet II -> Lancet III
Rivet I -> Rivet II -> Rivet III
Ember I -> Ember II -> Ember III
Scatter I -> Scatter II -> Scatter III => N.U.K.E.
```
<!-- item-tree:end -->

## A négy fajta {#the-four-kinds}

| | Egy célpont: egy hajót talál el | Területi robbanás: felrobban, mindent megsebez a közelben |
| :--- | :--- | :--- |
| **Irányított**: befogja a kijelölt célpontot, és követi | Lancet I, Lancet II, Lancet III | Ember I, Ember II, Ember III |
| **Egyenes**: a kurzorod felé repül | Rivet I, Rivet II, Rivet III | Scatter I, Scatter II, Scatter III |

Minden fajta egy **család**, amely a közönséges rakétájáról kapja a nevét, a fokozatot pedig római szám jelöli: a **Lancet I**, a **Lancet II** és a **Lancet III** a gyakori, a ritka és az epikus irányított, egy célpontú rakéta, a Rivet, az Ember és a Scatter család ugyanígy épül fel. Egy rakéta kódja a Rakéták menüben és a hangár kártyáján a családja három betűje és a száma (LNC II, RVT III, EMB I, SCT II); a két csak Gyártással készíthető rakéta megtartja a nevét és a kódját (N.U.K.E., NUK; N.I.K.E., NIK).

- Az **irányított** rakétáknak indulásukkor kell egy kijelölt célpont a **befogási távolságukon** belül. Korlátozott fordulási sebességgel követik, ezért egy távoli, gyors hajó lehagyhat egy olcsót. Ha a célpont megsemmisül, távozik vagy biztonságos zónába ér, a rakéta egyenesen repül tovább, és nem választ másikat.
- Az **egyenes** rakétáknak nem kell célpont, és figyelmen kívül hagyják a kijelöltet: mindig a **kurzorod** felé repülnek, a repülési nézetben a kurzor alatti pont felé. **Kattints egy egyenes rakéta helyére az élesítéshez** (a hely fehér keretet és célkeresztet kap, az egérkurzorod pedig célkereszt lesz az űr fölött), majd **kattints az űrbe**: a rakéta a rákattintott pont felé repül, a hajód pedig a helyén marad. Az Esc, a jobb klikk vagy ugyanannak a helynek az újbóli megnyomása elengedi. Ha a rakéták még töltődnek, a kattintás csak ezt közli, és a rakéta élesítve marad. A számgombok és a **Rakétakilövés** azonnal a kurzor utolsó, repülési nézetben lévő pontja felé lőnek; amíg a kurzor még nem járt ott, abba az irányba repülnek, **amerre a hajód néz**. Egyenesen repülnek, így egy nagy sebességgel keresztező hajó kitérhet előlük.
- Az **egy célpontú** rakéta az első hajót találja el, amelyet eltalálhat (az irányított csak a célpontját). A **területi robbanás** az első hajó mellett robban fel, amellyel találkozik, a megcélzott pontnál, vagy ahol a repülése véget ér, és minden hajót megsebez a **robbanási sugarán** belül: a középpontban teljes sebzéssel, a szél felé kevesebbel. A gyűrű, amelyet a robbanás a térképen rajzol, a pontos hatósugara.

## A tizenkét rakéta {#the-twelve-rockets}

Minden rakétának **saját sebzése van, amelyet a kilövéskor sorsol a rendszer**: a legmagasabb számának **80% és 100%** közötti értéke, a táblázat a legalacsonyabbat és a legmagasabbat mutatja. Nem függ a hajódtól, a lézereidtől, a Damage Amp erősítőidtől, a boosterektől, a lőszeredtől vagy a drónjaidtól, és a rakéta sosem kritikus. Csak egy **drónformáció** változtatja meg: az itteni táblázat a formáció nélküli sebzést adja meg (lásd: [Drónformációk és rakéták](#drone-formations-and-rockets)). Az egy célpontú rakéta az eltalált hajónak a kisorsolt sebzést okozza; a robbanás egyszer sorsol, és ugyanazt okozza **minden hajónak, amely benne van**, a középpontban a teljes számot, a szél felé kevesebbet. A *pajzsáthatolást* levonják a célpontod elnyeléséből az adott találatnál (egy hajó elnyelése a találat azon része, amelyet a pajzsai felfognak, lásd: [Pajzsmechanika](/wiki/03-Mechanics/Shields.md#shield-penetration)): egy Lancet III 35%-os áthatolása mellett egy 80%-os hajó pajzsai a találat 45%-át fogják fel, a másik 55% a hajótestre jut. A robbanásnak nincs ilyen.

| Név | Fajta | Ritkaság | Sebzés | Pajzsáthatolás | Robbanási sugár | Befogási távolság | Hatótáv | Sebesség | Ár | Legfeljebb ennyit vihetsz |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **Lancet I** | Irányított · egy célpont | Gyakori | 1 600–2 000 | 10% | – | 700 | 1 040 | 520 | 500 kredit | 5 000 |
| **Lancet II** | Irányított · egy célpont | Ritka | 3 200–4 000 | 25% | – | 1 000 | 1 584 | 660 | 800 kredit | 2 000 |
| **Lancet III** | Irányított · egy célpont | Epikus | 4 800–6 000 | 35% | – | 1 300 | 2 296 | 820 | 5 Thulium | 500 |
| **Rivet I** | Egyenes · egy célpont | Gyakori | 2 000–2 500 | 5% | – | – | 1 080 | 900 | 500 kredit | 5 000 |
| **Rivet II** | Egyenes · egy célpont | Ritka | 4 000–5 000 | 25% | – | – | 1 120 | 700 | 800 kredit | 2 000 |
| **Rivet III** | Egyenes · egy célpont | Epikus | 6 000–7 500 | 35% | – | – | 1 100 | 500 | 5 Thulium | 500 |
| **Ember I** | Irányított · területi robbanás | Gyakori | 1 120–1 400 | – | 170 | 700 | 1 000 | 500 | 500 kredit | 5 000 |
| **Ember II** | Irányított · területi robbanás | Ritka | 2 240–2 800 | – | 230 | 920 | 1 500 | 600 | 800 kredit | 2 000 |
| **Ember III** | Irányított · területi robbanás | Epikus | 3 360–4 200 | – | 300 | 1 150 | 2 030 | 700 | 5 Thulium | 500 |
| **Scatter I** | Egyenes · területi robbanás | Gyakori | 1 400–1 750 | – | 210 | – | 1 088 | 640 | 500 kredit | 5 000 |
| **Scatter II** | Egyenes · területi robbanás | Ritka | 2 800–3 500 | – | 290 | – | 1 080 | 540 | 800 kredit | 2 000 |
| **Scatter III** | Egyenes · területi robbanás | Epikus | 4 200–5 250 | – | 400 | – | 1 092 | 420 | 5 Thulium | 500 |

Minél drágább a fokozat, annál erősebben üt a rakéta, annál messzebbre hat, annál nagyobb a pajzsáthatolása, és annál kevesebbet vihetsz belőle; a drágák ráadásul a költségükhöz képest adják a legtöbb sebzést. Egy egyenes rakéta **25%-kal többet** sebez, mint az azonos fokozatú és azonos fajtájú irányított rakéta ugyanazért az árért, mert célozni kell vele. Egy robbanás az azonos fokozatú egy célpontú rakéta sebzésének 70%-át okozza, minden hajónak, amelyet lefed. A robbanás sebzése a középpontban éri el a teljes értéket; a szélén 25–35%-ra csökken. Egy kilövés átlagosan a legmagasabb számának 90%-át sebzi, és az alábbi, rakétákat számoló táblázat ezzel számol.

## Mennyibe kerülnek {#what-they-cost}

Egy Gyakori rakéta 500 kreditbe kerül, egy Ritka 800 kreditbe, egy Epikus 5 Thuliumba, minden fajtában. Minden időzítőnél kilőve ez percenként 6 000 kredit a Gyakori rakétánál, 9 600 a Ritkánál és 60 Thulium az Epikusnál, szemben azzal az 1 800 kredit/perccel, amennyit egy Ostirion három lézere x1 lőszerrel elfogyaszt. Egy teli köteg 5 000 Gyakori rakéta (2 500 000 kredit), 2 000 Ritka (1 600 000 kredit) vagy 500 Epikus (2 500 Thulium): a teli kötegig annyit veszel, amennyit akarsz, és egy rakéta *legfeljebb ennyit vihetsz* értéke az egyetlen korlát arra, hányat tarthatsz. A rakéták semmit sem nyomnak: nem foglalnak helyet a tranzittárolóban. Az 5 másodpercenkénti egy rakéta percenként csak tizenkettő, így a rakéta a lézereid tetejére jövő löket: az olcsók a gyenge idegeneknek, a drágák a nagy harcokra.

A Bolt a rakétákat fajtánként sorolja fel, mindegyiket a neve alatt, elöl a Gyakori rakétával és a végén az Epikussal; a hangár, a tranzittároló és a Rakéták menü ugyanezt a sorrendet használja.

## Az idegenek ellen {#against-the-aliens}

Hány rakéta kell egy idegen megsemmisítéséhez, egyszerre egyféle rakétával (Alphában; a Beta és a Gamma idegenei 1,5-szer, illetve 2-szer olyan erősek). A robbanás úgy számít, ahogyan az a hajó kapja, amely mellett felrobban, a középponttól egy kicsit távolabb. Egy idegen pajzsa a találat 80%-át fogja fel, mínusz a rakéta pajzsáthatolása. Itt minden rakéta az átlagot sorsolja. A legalacsonyabb sorsolásnál egy kilövéshez kb. 10–15%-kal több rakéta kell, mint a táblázatban (egy Lancet I-ből 50 kell egy Goombah-hoz, nem 45), a legjobbnál kb. 10%-kal kevesebb (40). Egy Rivet II csak 89%-os vagy magasabb sorsolásnál semmisít meg egy Phantasmot egy találattal, alatta kettő kell.

| Szükséges rakéták | Seeker (1 600) | Phantasm (5 200) | Bulwark (26 000) | Goombah (80 000) | Crystalys (416 000) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Lancet I** | 1 | 3 | 15 | 45 | 232 |
| **Lancet II** | 1 | 2 | 8 | 20 | 116 |
| **Lancet III** | 1 | 1 | 5 | 11 | 78 |
| **Rivet I** | 1 | 3 | 12 | 36 | 185 |
| **Rivet II** | 1 | 1 | 6 | 16 | 93 |
| **Rivet III** | 1 | 1 | 4 | 9 | 62 |
| **Ember I** | 2 | 5 | 25 | 77 | 399 |
| **Ember II** | 1 | 3 | 13 | 37 | 193 |
| **Ember III** | 1 | 2 | 8 | 25 | 128 |
| **Scatter I** | 2 | 4 | 20 | 60 | 311 |
| **Scatter II** | 1 | 2 | 10 | 29 | 151 |
| **Scatter III** | 1 | 2 | 7 | 20 | 100 |

- A **Gyakori** egy célpontú rakéták bármely sorsolásnál egy találattal megsemmisítenek egy Seekert, három találattal egy Phantasmot (egy Lancet I-nek a legalacsonyabb sorsolásánál negyedik is kell); ezek az első szektorok mindennapi rakétái. A **Ritkák** a Bulwarkhoz és a Goombah-hoz valók: nyolc Lancet II körülbelül 35 másodpercnyi időzítő alatt elintéz egy Bulwarkot. Az **Epikusok** bármely sorsolásnál egy találattal megsemmisítenek egy Phantasmot, és kilenc–tizenegy találattal egy Goombah-ot. A robbanások akkor érik meg az áruk, ha több idegen van közel egymáshoz: egy öt Phantasmból álló raj fölött felrobbanó Scatter III egyetlen lövéssel körülbelül 18 000 sebzést okoz a rajban.
- A kizárólag rakétákkal végzett kilövés valódi kiadás, nem a meggazdagodás útja: arra az idegenre, amelyre szánták, egy egy célpontú rakéta a kilövés jutalmának nagyjából egyhetedétől háromnegyedéig terjedő összegbe kerül (kreditben, a Thuliumot 200 kreditnek számolva darabonként), a gyenge rakéták az erős idegeneken pedig többe kerülnek, mint amennyit a kilövés fizet. A **Crystalyst** egyetlen rakétafajtával megsemmisíteni 62–399 rakétát és legalább öt percnyi időzítőt igényel; egy 500 darabos teli köteg Epikus rakéta négy–nyolc ilyen megsemmisítéséhez elég. A legerősebb idegenhez terv kell: a lézereid x2 lőszerrel, az első másodperctől minden 5 másodpercben egy közepes fokozatú rakéta, és az alább leírt nagy rakéták löketként.
- A kilövés jutalma ugyanannyi, bárhogyan hajtották végre (a legnagyobbat lásd a [Crystalys](/wiki/04-Aliens/Crystalys.md) oldalon), így egy rakétás kilövés akkor éri meg, ha időt takarít meg, és kevesebbe kerül, mint amennyit fizet.
- **Az idegenek is lőnek rakétákat.** A [rajok](/wiki/05-Swarms/Swarms.md) Pirate Bossa, Dormant Force-a és Pulse-ai egyenes Rivet-rakétákat lőnek arra a pilótára, aki megtámadta őket, ugyanazzal az 5 másodperces időzítővel. A folyamatosan mozgó hajó kitér előlük. A rajok bossai a ládáikban rakétákat is ejtenek.

## A csak gyártható rakéták {#the-craft-only-rockets}

Két rakéta nincs a Boltban. A **Gyártás** állítja elő őket, és mindenben követik az alábbi szabályokat (a közös időzítő, a biztonságos zónák, a vállalatod). Mindkettő egyenes rakéta: a kurzorod alatti pont felé repülnek, mint minden egyenes rakéta (a játék a kurzor irányát küldi, bármi is van kijelölve; csak egy régi, 0.4.3-as kliens, amely nem küld irányt, eléri, hogy a szerver a kijelölt célpontra repítse őket, ennek híján a kurzora alatti pontra, annak híján arra, amerre a hajó néz). A legmagasabb számuk **90% és 100%** között sorsolódnak, a tizenkettőnél szűkebb sávban, így amit alább egy találattal megsemmisítenek, az a legalacsonyabb sorsolásnál is igaz.

| Név | Fajta | Ritkaság | Sebzés | Pajzsáthatolás | Robbanási sugár | Hatótáv | Sebesség | Legfeljebb ennyit vihetsz | Ebből készül |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **N.U.K.E.** | Egyenes · területi robbanás | Legendás | 45 000–50 000 | – | 900 | 1 200 | 300 | 10 | Gyártásonként 1 N.U.K.E.: 150 000 kredit, 3 000 Thulium, 6 Scatter III, 4 Power Core, 10 Reinforced Hull Plate, 40 Ship Fragment, 80 Cataclysite |
| **N.I.K.E.** | Egyenes · egy célpont | Mitikus | 67 500–75 000 | 35% | – | 4 050 | 900 | 20 | Gyártásonként 5 N.I.K.E.: 100 000 kredit, 1 500 Thulium, 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite |

- **N.U.K.E.**: a játék legnagyobb robbanása. 900 egységes robbanás, a Scatter III 400-as hatósugarának kétszerese és a területének ötszöröse: 45 000–50 000 sebzés minden hajónak a robbanásban a középpontnál, a szélén a felére, 22 500–25 000-re csökkenve. Lassú (négy másodpercig van a levegőben). Egy N.U.K.E. a teljes robbanásában minden Seekert és Phantasmot megsemmisít, és egy Bulwarkot a becsapódás körüli 830 egységen belül (a legjobb sorsolásnál 934), vagyis majdnem az egész robbanásban; egy Goombah felénél többet és egy Crystalys egykilencedét viszi el. Pilóták ellen ez a legnagyobb találat: lásd az alábbi szabályokat. A gyűrű a térképen a pontos hatósugara.
- **N.I.K.E.**: egy Rivethez hasonló egy célpontú rakéta, 67 500–75 000 sebzéssel és 35%-os pajzsáthatolással: **az első hajót találja el, amelyet érint, és elfogy rajta.** Ez az a rakéta is, amely [Dark Mattert](/wiki/03-Mechanics/Black-Hole.md) termel: ha a Veszélyes szektor 4 közepén lévő feketelyukba lövöd, a lyuk elnyeli, amikor átlépi az eseményhorizontot, és Dark Mattert ad vissza. 4 050 egységet repül 4,5 másodperc alatt: a sugárzás pereme és a középponttól számított 4 380 egység között bárhonnan kilőheted. Messzebbről rövidre esik, és kárba vész. Öt N.I.K.E. körülbelül tíz Dark Mattert ad.
- **A csapda.** Az a N.I.K.E., amely útközben hajóval találkozik, egy a lövés vonalában várakozó riválissal vagy bármi mással, amit megsebezhet, 67 500–75 000-et sebez rajta, és eltűnik: a feketelyuk nem kap semmit, és te sem. A lyuk gyűrűjében semmi más nem kóborol, amit véletlenül eltalálhatna (az idegenek és a vállalati pilóták távol maradnak tőle): csak azok a pilóták, akik Dark Matterért mentek be, vagy a szélén várnak rád. A saját vállalatodon, a biztonságos zónában lévő hajókon és azokon a hajókon, amelyeket még nem sebezhetsz, átrepül. Ha a kilövés után elhagyod a térképet, tovább repül anélkül, hogy bárkit megsebezne, és a Dark Mattert így is megtermeli neked.
- A Gyártás nem indít el olyan gyártást, amely után a *legfeljebb ennyit vihetsz* értéknél többet tartanál egy rakétából, a sorba állítottakat is beleszámítva.

## Tüzelés {#firing}

1. Vegyél rakétákat a Boltban (a **Rakéta** kategóriában), mindegyikből a *legfeljebb ennyit vihetsz* korlátig: kreditért a Gyakori és a Ritka, Thuliumért az Epikus rakétákat.
2. Nyisd meg a **Rakéták** menüt a gyorssáv fölött, és húzd a kívánt rakétákat a helyekre. A menü fajtánként egy oszlopot és fokozatonként egy sort mutat, mindegyiken azzal, amennyit hordasz. Alattuk külön sor van, **Különleges · csak Gyártás**, a N.U.K.E. és a N.I.K.E. számára (egy kis kalapács jelöli azt, amelyből egyet sem hordasz).
3. Nyomd meg a hely billentyűjét. Egy **irányított** rakéta helyére kattintva a kijelölt célpontra lősz vele; egy **egyenes** rakéta helyére kattintva élesíted, és a következő űrbeli kattintásod oda lövi ki. A **Rakétakilövés** billentyű (alapértelmezés szerint `R`, a Beállítások › Irányítás alatt átállítható) az utoljára kilőtt rakétát lövi ki, vagy a sáv első rakétáját.
4. **Minden** rakétahelyen egy körcikk fut körbe a következő kilövésig tartó 5 másodpercben, a hátralévő másodpercekkel a közepén. Addig egy megnyomás csak azt közli, hogy a rakéták töltődnek (az utolsó tizedmásodpercben megnyomva még elsül). Egy drónformáció 3,65 és 6,75 másodperc közé állíthatja a várakozást (lásd lent).

Vidd az egeret egy rakétahely fölé, hogy lásd az értékeit (a legalacsonyabb és a legmagasabb sebzése; a Bolt és a hangár ugyanezt mondja), a világban pedig a befogási gyűrűjét (zöld, ha a kijelölt célpont hatótávon belül van), illetve a vonalát és a robbanási körét. A **rád** befogott rakéta pirosan villogtatja a képernyőd szélét.

A **N.U.K.E.** a térképen megrajzolja a robbanását, mielőtt kilősz (a 900 egységes kör a megcélzott pontnál), és amikor felrobban, egy fehér villanás látszik a nézet fölött, egy gyűrű, amely körülbelül egy másodperc alatt kifut a pontos hatósugarig, és még kettőig megmarad, egy gombafelhőszerűen emelkedő felhő, és egy kamerarázkódás, amely annál erősebb, minél közelebb vagy. A **Kevesebb képernyőrázkódás** megszünteti a rázkódást, a **Kevesebb mozgás** pedig a villanást egy másodperc harmadára rövidíti, a fényének felénél kisebb erősséggel (mindkettő a Beállítások › Grafika alatt található); az alacsonyabb részecskeminőség ritkítja a felhőt és elhagyja a szikrákat, a villanást és a gyűrűt sosem. A **N.I.K.E.**-t úgy célzod, mint a Rivetet, a hajód és a kurzor közötti vonallal, és a játék sosem utasítja el azért, mert messze van a feketelyuktól, vagy mert olyan térképen vagy, amelyen nincs ilyen: hogy hová megy, azt te ítéled meg. A kártyája a sebzése mellett ezt írja: **Feketelyuk: Dark Mattert ad**. Lilás nyomot hagy maga után, amely körül szikrák kígyóznak; egy hajó, amellyel találkozik, úgy kapja a találatot, mint bármelyik rakétától, ha pedig inkább az eseményhorizontot lépi át, a lyuk felvillan.

## Drónformációk és rakéták {#drone-formations-and-rockets}

A viselt [drónformáció](/wiki/03-Mechanics/Formations.md) az egyetlen dolog, ami megváltoztat egy rakétát. Az ezen az oldalon szereplő minden sebzésszám formáció nélküli hajóra érvényes.

- **Sebzés.** A Ballista (+55%), a Bodkin (+29%) és az Asterism (+24%) rakétabónusza mind a 14 rakéta sebzését szorozza, a N.U.K.E.-ét és a N.I.K.E.-ét is. A Testudo minden sebzésre vonatkozó ára a rakétákra is hat, a Culler idegenekre vonatkozó sebzése pedig az idegent találó rakétákra. Az egy rakétán lévő összes tényező együtt ×1,59-nél megáll.
- **Újratöltés.** Az Asterism 35%-kal hosszabbra (6,75 másodperc), a Cordon 11%-kal hosszabbra (5,55), a Redoubt 27%-kal rövidebbre (3,65) állítja a közös időzítőt, de soha nem rövidebbre, mint a rakéta repülése plusz egy pillanat: 4,1 másodperc egy N.U.K.E. után és 4,6 egy N.I.K.E. után. A várakozás a kilövéskor dől el, ezért a későbbi formációváltás nem rövidíti, és a rakétahelyek feletti körcikk követi.
- **A két nagy határai megmaradnak.** A legjobb formációval egy N.I.K.E. legfeljebb 116 250-es találatot ad, amit egy ép Paragon (128 000) túlél, egy N.U.K.E. legfeljebb 77 500-ast, amit egy Goombah (80 000) túlél.
- **Kitérés.** Az Asterism 7%-os kitérése 7% esélyt ad arra, hogy a rád érkező közvetlen rakéta egyáltalán nem sebez, és a hajód fölött egy lebegő „Mellé” felirat jelenik meg; a területi robbanás nem céloz, és soha nem kerülhető ki.
- **Átütés.** A Gemini és a Stiletto a pontjaikat egy közvetlen rakéta pajzsáthatolásához adják (a robbanásnak nincs), összesen legfeljebb 40%-ig.

## Szabályok {#rules}

- Rakéta kilövéséhez **nincs szükség felszerelt lézerre**, és a lézereid nem változtatják meg, mennyit sebez, sem azt, milyen messzire hat: az irányított rakéta a saját befogási távolságán belül fogja be a célpontot, az egyenes a saját hatótávjáig repül. Felszerelt lézer nélkül a hangár Hatótáv csempéje egy gondolatjelet mutat, és csak a rakétáid tüzelnek.
- Kilövésenként egy rakéta fogy el, akár talál, akár nem.
- A rakéták a lézerek szabályait követik: a **biztonságos zónán** belül semmi sem sérül, egy pilóta sem sérül a **Békeprotokoll** végéig, vagy ahol egy szektor tiltja a PvP-t, és a **saját vállalatodat és a saját csoportodat sosem sebzik meg** a rakétáid, sem közvetlenül, sem robbanással.
- A rakéta kilövése azonnal véget vet a saját biztonságos zónabeli védelmednek. Lövésnek számít: a saját **álcázásodat** is megszünteti, a Cloaking CPU pedig egy percig tölt, mint az álcázás bármelyik végén. Álcázva vagy sem, a kilövés után 10 másodpercig nem álcázhatsz (lásd: [Extrák](/wiki/06-Items/Extras.md)).
- Egy **álcázott** vagy az **EMP-je 3 másodpercén belül** lévő hajót nem lehet befogni: az irányított rakétát elutasítja a játék, az már feléje repülő pedig elveszti a célzást, és egyenesen repül tovább. Az egyenes, egy célpontú rakéta átrepül egy ilyen hajón. A **területi robbanáshoz** nem kell célzás, így megsebzi a hatókörébe eső hajókat, álcázottat is, és megszünteti az álcázást (lásd: [Extrák](/wiki/06-Items/Extras.md)).
- **Semmi sem korlátozza, mennyit sebez egy rakéta egy pilótának.** Egy másik pilóta hajója a teljes sebzést megkapja: előbb a pajzs (az elnyelése mínusz a rakéta pajzsáthatolása), aztán a hajótest. A kis hajók nem bírják. A gyári pajzsmagokkal (Light, 45% elnyelés) egy N.I.K.E. bármely sorsolásnál egy találattal megsemmisít egy ép Protost, Kitefint vagy Ostiriont (egy Paragon a hajótestének 47–53%-át veszíti el, egy Wraith nagyjából az ötödét), egy N.U.K.E. pedig a robbanás bármely pontján megsemmisít egy Protost, a becsapódás körüli kb. 50 egységen belül (a legjobb sorsolásnál 220) egy Kitefint, és semmi nagyobbat egyetlen robbanással. Két Lancet III vagy két Rivet III bármely sorsolásnál megsemmisít egy Protost; egy Wraith megsemmisítéséhez ezekből 48–75 kell. A Békeprotokoll, a biztonságos zónák és a vállalatod az, ami egy pilóta és egy rakéta között áll. Ezek a számok formáció nélküli hajóra érvényesek; egy rakétaformáció legfeljebb 55%-kal növeli őket (lásd: [Drónformációk és rakéták](#drone-formations-and-rockets)).
- Csak a rakéta **közvetlen találata** foglal le egy idegent (lásd: [Harc](/wiki/03-Mechanics/Combat.md)); a robbanás széle megsebezhet egy lefoglalt idegent anélkül, hogy elvenné. Minden idegen, amelyet egy robbanás megsebez, az alvót is beleértve, ellened fordul, ahogy egy lézertalálatnál is (a csak visszatámadó Seekert vagy Goombah-ot is beleértve); amelyiket a robbanás elvéti, az alszik tovább.
- Az időzítő a tiéd: túléli az ugrást, az újracsatlakozást, a hajócserét és a megsemmisült hajót.

Az első táblázat tizenkét rakétája megvásárolható (kreditért a Gyakori és a Ritka, Thuliumért az Epikus); a N.U.K.E. és a N.I.K.E. gyártható.

Lásd még: [Lézerek és lőszer](/wiki/06-Items/Lasers.md), [Harc](/wiki/03-Mechanics/Combat.md), [A feketelyuk](/wiki/03-Mechanics/Black-Hole.md).
