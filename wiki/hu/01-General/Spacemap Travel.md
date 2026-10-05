<!-- wiki-i18n source: 6ad05a3dc7e0e2f6 -->
<!-- wiki-i18n title: Utazás az űrtérképen -->
# Utazás az űrtérképen {#spacemap-travel}

Az űrtérkép a navigációs felületed, amellyel bejárhatod a SpaceCorps univerzumát. Minden vállalat az űr egy-egy szektorát irányítja, és ezeket olyan sajátos topológia szerint rendezték el, amely egyszerre teszi lehetővé a biztonságos felfedezést és a veszélyes PvP-összecsapásokat.

![Galaxy Gates](../../img/wiki-img/shots/gates.jpg)
![Sector DS-1 as the game draws it](../../img/wiki-img/shots/sector-DS-1.jpg)
![Sector DS-2 as the game draws it](../../img/wiki-img/shots/sector-DS-2.jpg)
![Sector DS-3 as the game draws it](../../img/wiki-img/shots/sector-DS-3.jpg)
![Sector DS-4 as the game draws it](../../img/wiki-img/shots/sector-DS-4.jpg)
![Sector G-1 as the game draws it](../../img/wiki-img/shots/sector-G-1.jpg)
![Sector G-2 as the game draws it](../../img/wiki-img/shots/sector-G-2.jpg)
![Sector G-3 as the game draws it](../../img/wiki-img/shots/sector-G-3.jpg)
![Sector G-4 as the game draws it](../../img/wiki-img/shots/sector-G-4.jpg)
![Sector M-1 as the game draws it](../../img/wiki-img/shots/sector-M-1.jpg)
![Sector M-2 as the game draws it](../../img/wiki-img/shots/sector-M-2.jpg)
![Sector M-3 as the game draws it](../../img/wiki-img/shots/sector-M-3.jpg)
![Sector M-4 as the game draws it](../../img/wiki-img/shots/sector-M-4.jpg)
![Sector T-1 as the game draws it](../../img/wiki-img/shots/sector-T-1.jpg)
![Sector T-2 as the game draws it](../../img/wiki-img/shots/sector-T-2.jpg)
![Sector T-3 as the game draws it](../../img/wiki-img/shots/sector-T-3.jpg)
![Sector T-4 as the game draws it](../../img/wiki-img/shots/sector-T-4.jpg)
![The Star System map: the sectors, the PvP sectors, the gates and the company routes, with the portal ring that joins each company's x-4 sector to the next company's x-3 sector](../../img/wiki-img/shots/star-system.jpg)

## Az univerzum szerkezete {#the-universe-structure}

Az univerzum három fő vállalati szektorból (Mars, Terra, Galactic) és egy központi PvP-zónából áll.

- **x-1 (Otthoni bázis)**: Minden vállalat kezdőtérképe (M-1, T-1, G-1). A legbiztonságosabb zóna.
- **x-2 -> x-3**: Terjeszkedési zónák egyre erősebb idegenekkel.
- **x-4 (Határ)**: A PvP-szektor kapuja, és egy másik vállalat `x-3` szektoráé is (a Gyűrű, lásd lent).
- **DS-x (Veszélyes szektorok)**: A központi PvP-zóna, amely az összes vállalatot összeköti: DS-1–DS-4.

Csak az otthoni bázisokon van állomás. Itt nyílik meg a **Mission Control**, az állomás biztonságos zónája pedig 1 600 egységnyire terjed ki körülötte. A veszélyes szektorokban nincs állomás, a `DS-1`-ben sem: az egyetlen biztonságos zónák ott az ugrókapuk körüli 660 egység sugarú gyűrűk, és a Mission Control sem nyitható meg; a küldetéseidért repülj vissza a bázisodra.

Minden [világ](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) (Alpha, Beta, Gamma) a teljes térkép saját példányával rendelkezik, és ettől függ, hol harcolhatnak egymással a pilóták: az Alphában csak az `x-4` és a `DS-x` szektorokban, a Betában az `x-1` kivételével mindenhol, a Gammában mindenhol. A galaxistérkép a világod szabálya szerint színezi a szektorokat.

## Megjelenítés {#visualization}

Az alábbi galaxistérkép az ismert univerzum valós idejű elrendezését mutatja. A játékban ugyanez a térkép a **Csillagrendszer** ablak.

```spacemap

```

Ha fel van szerelve egy [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu), a térkép a célt is kiválasztja: nyomd meg a CPU gyorssáv-helyét (**JMP**), és a Csillagrendszer ablak kijelölő módban nyílik meg. Világítanak azok a szektorok, ahová a CPU elvihet; a saját szektorod és a veszélyes szektorok nem. Mutass egy világító szektorra az ár elolvasásához, kattints rá, és erősítsd meg az ugrást, amikor a térkép kéri (500 Thulium).

## Hogyan utazz {#how-to-travel}

Az űrtérképen az utazás **ugrókapukon** (portálokon) át zajlik. A [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) a másik út: nem kell hozzá kapu (lásd az oldal végét).

1. **Keress egy portált**: A portálok jellemzően a térkép sarkaiban vagy szélein találhatók.
2. **Navigáció**: Repüld a hajódat a portál szerkezetének közelébe.
3. **Aktiválás**: Az ugrás elindításához nyomd meg a **J** gombot a portáltól 500 egységen belül.
4. **Várd ki**: Az ugrás **3 másodpercig tart**. A gyorssáv felett közben egy sáv („Ugrás…”) telik meg, a portál pedig egyre fényesebben ragyog, ahogy töltődik; a többi pilóta ugyanezt a töltődést látja a portálon, amikor te ugrasz. A hajód tovább repül, de az idő lejártáig a portáltól 500 egységen belül kell maradnod: ha kirepülsz a hatótávból, az ugrás megszakad („A portál túl messze van az ugráshoz.”, és a sáv pirosra vált). Ha ugrás közben újra megnyomod a **J** gombot, az semmit sem csinál, csak szól erről.
5. **Úti cél**: A célként kijelölt térkép megfelelő portáljánál érkezel meg.

### Ugrás tűz alatt {#jumping-under-fire}

- **A veszélyes szektorokon kívül** a támadás – akár idegenektől, akár más pilótáktól – **nem** szakítja meg az ugrást: az befejeződik.
- **A veszélyes szektorokban (`DS-1`–`DS-4`)** támadás alatt nem tudsz kiugrani. Ha egy pilóta vagy egy idegen az elmúlt **10 másodpercben** eltalálta a hajódat (a pajzsát vagy a hajótestét), az ugrás nem indul el („Támadás alatt állsz: veszélyes szektorból nem tudsz kiugrani.”), az ugrás közbeni találat pedig megszakítja az ugrást (a sáv pirosra vált, és a játék közli az okát). A feketelyuk sugárzásából kapott sebzés nem számít támadásnak, ahogy az a lövés sem, amelyet egy biztonságos zóna megállított. Az a találat, amelyet azon a térképen kaptál, ahonnan ugrottál, nem követ át a portálon: tiszta lappal érkezel.
- Egyszerre egy dolgot csinálsz: ugrás közben nem tudsz [rakományládát](/wiki/03-Mechanics/Cargo.md) felvenni, és az ugrás megkezdése feladja a már elkezdett felvételt.
- Ha ugrás közben bezárod a játékot, vagy visszatérsz a bázisra, az ugrás megszakad: nem érkezel meg.
- **A CPU-k teleportja úgy töltődik, mint egy portálugrás.** A Jump CPU 5 másodpercig, a Base CPU 10 másodpercig töltődik, a gyorssáv fölött egy sávval. A saját lövésed vagy egy kapott találat bármelyik szektorban megszakítja (nem fizetsz, és nem használódik el semmi), és egyik CPU sem indul el egy lövés vagy találat után 10 másodpercen belül. A CPU helyére újra rányomva magad is megszakíthatod.

### Ugrókapcsolatok {#jump-links}

- **A vállalati hurok**: A Mars, a Terra és a Galactic elrendezése azonos. A kapcsolatok így futnak: `1 <-> 2 <-> 3`, `2 <-> 4` és `3 <-> 4`. Ez hurkot alkot a másodlagos térképek (`x-2` és `x-3`) és a határtérkép (`x-4`) között, az `x-1` pedig biztonságos belépési farokként csak az `x-2` szektorhoz kapcsolódik: a kezdőtérképednek mindössze egy portálja van.
- **A veszélyes szektorok hozzáférési kapui**: Minden vállalat határtérképe (`x-4`) közvetlenül a saját veszélyes szektorához kapcsolódik:
  - az `M-4` a `DS-1` szektorhoz kapcsolódik
  - a `T-4` a `DS-2` szektorhoz kapcsolódik
  - a `G-4` a `DS-3` szektorhoz kapcsolódik
- **A Gyűrű**: Minden vállalat határtérképének (`x-4`) van még egy kapuja a **következő vállalat** `x-3` szektorába, és minden `x-3` szektornak van kapuja vissza. A három kapcsolat gyűrűt alkot a veszélyes szektorok körül, így minden vállalatnak van egy útja kifelé és egy befelé:
  - az `M-4` a Terra `T-3` szektorához kapcsolódik
  - a `T-4` a Galactic `G-3` szektorához kapcsolódik
  - a `G-4` a Mars `M-3` szektorához kapcsolódik

  A Gyűrű minden pilóta előtt nyitva áll, bármelyik vállalatnál repüljön is: ez egy második út a vállalatok térképei között, amely nem halad át a PvP-zónán. A gyűrűkapu a térképének egy külön sarkában áll, távol a térkép többi kapujától, körülötte a szokásos 660 egység sugarú biztonságos zónával, az ugrás pedig úgy működik, mint bármelyik kapunál. Hogy a túloldalon hol támadhatnak meg, az – mint mindenhol – a világodtól függ: az Alphában a `T-3` nem PvP-szektor, a `T-4` viszont az, a Betában mindkettő az, a Gammában minden szektor az.
- **Inváziós útvonalak (vállalatok közötti utazás)**: Egy másik vállalat területére a kapukon át két út vezet. A rövid a Gyűrű: a Mars vállalat pilótája az `M-4` szektorból a gyűrűkapun át a Terra `T-3` szektorába repül (három ugrás a Mars bázisától, `M-1` → `M-2` → `M-4` → `T-3`), onnan tovább a `T-4` vagy a `T-2` felé; a Galactic `G-4` szektora ugyanígy a Mars `M-3` szektorába vezet, a Terra `T-4` szektora pedig a Galactic `G-3` szektorába. A hosszú a PvP-zónán át vezet: az `M-4` szektorból a `DS-1` veszélyes szektorba, az ugrókapun át a `DS-2` szektorba, majd a `T-4` szektoron át a Terra területére; a Galactic területére a `DS-3` szektorba vezető ugrókapun át, majd a `G-4` szektoron keresztül jut be.
- **A veszélyes szektorok háromszöge**: A `DS-1`, a `DS-2` és a `DS-3` szektor mind összeköttetésben áll egymással. Mindegyikben van egy vállalat kapuja (a Mars vállalaté a `DS-1` szektorban, a Terra vállalaté a `DS-2` szektorban, a Galactic vállalaté a `DS-3` szektorban); a `DS-4` szektornak egy sincs.
- **A központi mag**: Mindhárom külső veszélyes szektor (`DS-1`, `DS-2` és `DS-3`) közvetlenül a központi **`DS-4`** térképhez kapcsolódik, amely az univerzum legveszélyesebb és legjobban jutalmazó PvP-zónája. Pontosan a közepén egy **feketelyuk** lebeg: a portálok és a köztük futó útvonalak jó messze maradnak tőle, de az a hajó, amely beröpül, először a sugárzását, majd a vonzását érzi, az eseményhorizontján pedig megsemmisül. Lásd: [A feketelyuk](/wiki/03-Mechanics/Black-Hole.md).

### A Jump CPU {#the-jump-cpu}

A [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) kapu nélkül viszi a hajódat a világod bármelyik vállalati szektorába, ugrásonként 500 Thuliumért, az ellenséges otthoni szektorokat is beleértve. Veszélyes szektorba sosem megy, harcban nem indul el, és előbb a Skylab Kutatóközpontjában kell kikutatnod ([Kutatás](/wiki/03-Mechanics/Research.md)). A [Base CPU-k](/wiki/06-Items/Extras.md#base-cpus) ugyanígy visznek haza. A warp CPU-t, vagyis a Jump CPU-t és a Base CPU-kat, megtagadja a játék, amíg küldetéstárgyat viszel („Küldetéstárggyal a fedélzeten nem használhatsz warp CPU-t.”): repülj haza a kapukon át ([Küldetéstárgyak](/wiki/03-Mechanics/Quests.md#quest-items)).
