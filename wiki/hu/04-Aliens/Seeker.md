<!-- wiki-i18n source: f0eea7ebd1631a1f -->
<!-- wiki-i18n title: Seeker -->
# Seeker {#seeker}

A Seeker idegenek egyszerű felderítő- és megfigyelőegységek. Passzívak, vagyis sosem ők kezdik a harcot: a Seeker arra a pilótára fordul, aki rálő, és csakis arra. Elengedi a célpontját, ha 10 másodpercig senki sem találta el, a hajóteste pedig javulni kezd, miután 30 másodpercig békén hagyták. A [Seeker-raj](/wiki/05-Swarms/Seeker-Swarm.md) Boss Seekere és Seeker Slave-jei úgy néznek ki, mint a Seekerek, de saját fajt alkotnak: a kilövésüket a saját nevük alatt számolják, nem Seeker-kilövésként.

## Értékek {#stats}

- **Életerő (HP)**: 800
- **Pajzs**: 800
- **Sebzés**: 180
- **Sebesség**: 120
- **Támadási hatótáv**: 600
- **Viselkedés**: Passzív

## Viselkedés {#behavior}

- A Seeker sosem megy utána a közelébe érő hajónak: addig barangol, amíg valaki rá nem lő, aztán üldözi, és tüzel arra a pilótára, aki elsőként lőtt rá, mindaddig, amíg az a pilóta folyamatosan találja, és el tudja érni; közben más pilóták lövései nem fordítják el, és ha az első kiesik a harcból, a következő pilótát veszi célba, aki beszállt a harcba (lásd [Kivel harcol egy idegen](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)). Más idegen lövése és a sebzést nem okozó találat sosem provokálja.
- **10 másodperccel** azután feladja, hogy valaki utoljára eltalálta, és újra barangol. Amíg egy pilóta folyamatosan találja, arra a pilótára repül, valahányszor az a fegyvere hatótávján (600 egység) kívül van, és tüzel, amint a pilóta hatótávon belülre ér.
- Elengedi a tőle **2 500 egységnél** távolabb lévő pilótát, vagy ha **3 000 egységet** repült az üldözés kezdőpontjától, és 8 másodpercig nem megy újra utána, kivéve ha a pilóta még egyszer rálő (lásd [Harc](/wiki/03-Mechanics/Combat.md)).
- Ha **30 másodpercig** békén hagyják, a hajóteste javulni kezd: másodpercenként a maximumának 2%-ával (a teljes hajótest nagyjából 50 másodperc alatt telik meg). A pajzsa úgy töltődik, mint minden idegené: az utolsó találat után 15 másodperccel kezdődik.
- Senkivel nem harcol, aki nem találta el, és sosem hív maga mellé másik idegent.
- A [vállalati pilóták](/wiki/03-Mechanics/Company-Pilots.md) vadásznak a Seeker idegenekre. Az a pilóta, aki rálő egyre, magára vonja a tüzét, hacsak az nem harcol már valaki mással.

## Jutalmak {#rewards}

- **Kredit**: 1 000
- **Thulium**: 4
- **Tapasztalat (XP)**: 100
- **Becsület**: 2
- **PvE-pont kilövésenként**: 1
- **Pajzstöltődés**: másodpercenként 10 (15 mp késleltetés)

## Zsákmány {#loot-drops}

Egy [rakományláda](/wiki/03-Mechanics/Cargo.md) marad belőle ott, ahol felrobban, és 30 másodpercig a kilövőé.

Hogy melyik zsákmány mire jó, és hol található még: [Nyersanyagok](/wiki/06-Items/Resources.md).

- **Ship Fragment**: 20% esély (min. 1, max. 1)
- **Daraxium**: 50% esély (min. 1, max. 2)

## Háttértörténet {#lore}

A Seeker idegenek az idegen Raj által bevetett könnyű felderítő szondák, amelyek a szektorok ugrókapuit térképezik fel, és az emberi flották elektromágneses jeleit követik. Minimális fegyverzettel és törékeny szerkezettel rendelkeznek, ezért rendkívül passzívak: visszavonulnak, vagy figyelmen kívül hagyják a hajókat, hacsak nem lőnek rájuk. A nagyobb harci egységekkel viszont összehangolják a mozgásukat, és ha harcba keverednek, jelzik a helyzetüket.
