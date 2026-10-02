<!-- wiki-i18n source: 48e9736362e10347 -->
<!-- wiki-i18n title: Utazás az űrtérképen -->
# Utazás az űrtérképen {#spacemap-travel}

Az űrtérkép a navigációs felületed, amellyel bejárhatod a SpaceCorps univerzumát. Minden vállalat az űr egy-egy szektorát irányítja, és ezeket olyan sajátos topológia szerint rendezték el, amely egyszerre teszi lehetővé a biztonságos felfedezést és a veszélyes PvP-összecsapásokat.

## Az univerzum szerkezete {#the-universe-structure}

Az univerzum három fő vállalati szektorból (Mars, Terra, Galactic) és egy központi PvP-zónából áll.

- **x-1 (Otthoni bázis)**: Minden vállalat kezdőtérképe (M-1, T-1, G-1). A legbiztonságosabb zóna.
- **x-2 -> x-3**: Terjeszkedési zónák egyre erősebb idegenekkel.
- **x-4 (Határ)**: A PvP-szektor kapuja.
- **DS-x (Veszélyes szektorok)**: A központi PvP-zóna, amely az összes vállalatot összeköti: DS-1–DS-4.

Minden [világ](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) (Alpha, Beta, Gamma) a teljes térkép saját példányával rendelkezik, és ettől függ, hol harcolhatnak egymással a pilóták: az Alphában csak az `x-4` és a `DS-x` szektorokban, a Betában az `x-1` kivételével mindenhol, a Gammában mindenhol. A galaxistérkép a világod szabálya szerint színezi a szektorokat.

## Megjelenítés {#visualization}

Az alábbi galaxistérkép az ismert univerzum valós idejű elrendezését mutatja.

```spacemap

```

## Hogyan utazz {#how-to-travel}

Az űrtérképen az utazás **ugrókapukon** (portálokon) át zajlik.

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

### Ugrókapcsolatok {#jump-links}

- **A vállalati hurok**: A Mars, a Terra és a Galactic elrendezése azonos. A kapcsolatok így futnak: `1 <-> 2 <-> 3`, `2 <-> 4` és `3 <-> 4`. Ez hurkot alkot a másodlagos térképek (`x-2` és `x-3`) és a határtérkép (`x-4`) között, az `x-1` pedig biztonságos belépési farokként csak az `x-2` szektorhoz kapcsolódik: a kezdőtérképednek mindössze egy portálja van.
- **A veszélyes szektorok hozzáférési kapui**: Minden vállalat határtérképe (`x-4`) közvetlenül a saját veszélyes szektorához kapcsolódik:
  - az `M-4` a `DS-1` szektorhoz kapcsolódik
  - a `T-4` a `DS-2` szektorhoz kapcsolódik
  - a `G-4` a `DS-3` szektorhoz kapcsolódik
- **Inváziós útvonalak (vállalatok közötti utazás)**: Ellenséges vállalat területére csak a PvP-zónán át vezet az út. Például a Mars vállalat pilótájának, aki a Terra területére akar betörni, az `M-4` szektorból a `DS-1` veszélyes szektorba kell repülnie, át kell ugrania az ugrókapun a `DS-2` szektorba, majd a `T-4` szektoron át léphet be a Terra területére; a Galactic területére a `DS-3` szektorba vezető ugrókapun át, majd a `G-4` szektoron keresztül jut be.
- **A veszélyes szektorok háromszöge**: A `DS-1`, a `DS-2` és a `DS-3` szektor mind összeköttetésben áll egymással. Mindegyikben van egy vállalat kapuja (a Mars vállalaté a `DS-1` szektorban, a Terra vállalaté a `DS-2` szektorban, a Galactic vállalaté a `DS-3` szektorban); a `DS-4` szektornak egy sincs.
- **A központi mag**: Mindhárom külső veszélyes szektor (`DS-1`, `DS-2` és `DS-3`) közvetlenül a központi **`DS-4`** térképhez kapcsolódik, amely az univerzum legveszélyesebb és legjobban jutalmazó PvP-zónája. Pontosan a közepén egy **feketelyuk** lebeg: a portálok és a köztük futó útvonalak jó messze maradnak tőle, de az a hajó, amely beröpül, először a sugárzását, majd a vonzását érzi, az eseményhorizontján pedig megsemmisül. Lásd: [A feketelyuk](/wiki/03-Mechanics/Black-Hole.md).
