<!-- wiki-i18n source: 36874838d2d52590 -->
<!-- wiki-i18n title: Inventarie -->
# Inventarie och utrustning {#inventory-equipment}

Hangaren låter dig hantera dina skepp och din utrustning. Att utrusta föremål effektivt är nyckeln till överlevnad och dominans. Du kan göra det på stationen, och under flygning inifrån en säker zon: se [Hangaren under flygning](/wiki/03-Mechanics/Hangar.md).

## Utrustningsplatser och värdens effektivitet {#equipment-slots-stat-efficiencies}

Till skillnad från traditionella rymdspel har SpaceCorps utrustningsplatser i dynamiska nivåer som skalar effektiviteten hos monterade moduler.

- **Laserplatser**: För offensiva vapen (lasrar). De arbetar alltid med **100 % skada och räckvidd**.
- **Generatorplatser**: Gemensamma platser för sköldar, motorer och adaptiva kärnor. De är indelade i tre effektivitetsband, och bandet avgör hur mycket av ett föremåls grundvärden som räknas. I hangaren har varje band en (i) bredvid sitt namn som förklarar det:
  - **Kärnplatser**: Föremål som placeras här får **100 %** av sina grundvärden. Alla skepp har dem: sätt dina starkaste sköldar och motorer här.
  - **Stödplatser**: Föremål som placeras här får **75 %** av sina grundvärden (t.ex. 75 % fart eller sköldkapacitet). Alla skepp har dem.
  - **Hjälpplatser**: Föremål som placeras här får **50 %** av sina grundvärden. Bara vissa skepp har dem (Nomad har 1, Paragon 2, Ironclad och Storm 3 och Wraith 4; Protos, Kitefin och Ostirion har inga). De passar bäst för extra, svagare sköldar och motorer, medan dina starkaste sitter i kärnplatserna.
  - **Drönarplatser**: en sköld på en av dina drönare räknas som en i en kärnplats, **100 %** av sina grundvärden (se [Drönarmekanik](/wiki/03-Mechanics/Drones.md)).
  - **Otilldelade platser/äldre platser**: Föremål som placeras här bidrar inte till värdena.
  - **Staplingen ger också mindre**: sköldar och motorer rangordnas med de starkaste först, och bandets andel multipliceras sedan med deras rangs: den 1:a till 4:e räknas fullt, den 5:e till 7:e med 85 %, 70 % och 55 %, den 8:e och framåt med 50 % för sköldar och 25 % för motorer. Se [Sköldar](/wiki/03-Mechanics/Shields.md) och [Hastighet](/wiki/03-Mechanics/Speed.md).
- **Extraplatser**: För specialiserad nyttoutrustning, till exempel Repair Drones. Varje skepp har tre; Extra Slots CPU ([Extrautrustning](/wiki/06-Items/Extras.md#extra-slots-cpus)) ger varje skepp fler.

## Inventariets ordning {#inventory-order}

Inventariet listar dina föremål i samma ordning som butiken, oavsett i vilken ordning du köpte, tillverkade eller hittade dem. Slag som hör ihop står tillsammans: lasrar, laserförstärkare och laserammunition; sköldar och sköldceller; motorer och styrraketer; adaptiva kärnor; extrautrustning (Repair Drones); drönare; sedan resurser. Inom ett slag kommer det billigaste först (krediter före Thulium), sedan det som saknar pris: utrustning som bara kan tillverkas och byte, med den svagaste sällsyntheten först (lasrar av en sällsynthet, med den svagaste skadan först). Laserammunition går från x1 till x4, sedan Siphon Battery. Raketer sorteras efter slag (enkelmål före områdesskada, målsökande före raka) och sedan efter nivå, så den episka raketen, som kostar Thulium, kommer sist i sitt slag. Exemplar av ett och samma föremål sorteras efter förtrollningsnivå. Ovanför rutnätet finns en filterknapp per slag i samma ordning, var och en med antalet föremål som sökningen hittar i det slaget. Varje filterknapp slår på eller av sig själv, så du kan dölja ammunition och Repair Drones medan du arbetar med lasrar, sköldar och motorer: klicka på en filterknapp för att visa eller dölja dess slag, Shift-klicka (eller dubbelklicka) för att bara låta det slaget vara på, och klicka på den igen för att få tillbaka resten. **Alla** visar alla slag och **Inga** döljer alla, så att du kan slå på bara dem du vill ha. En överstruken filterknapp är av, en filterknapp med en bockmarkering är på. Sökningen gäller de slag som är på, och ditt val sparas med din pilot. Om allt är dolt säger rutnätet det och erbjuder **Visa alla kategorier**.

## Föremål i föremål (undersockel) {#item-to-item-equipping-sub-sockets-}

Vissa primära föremål kan ”utrusta” sekundära stödföremål (kallas att sätta i undersockel) för att förstärka sina parametrar. För att sätta i undersockel drar du stödföremålet direkt på det primära föremålet i ditt inventarie i hangaren.

### Kompatibilitetstabell {#compatibility-table}

| Primärt föremål | Godkända undersockelföremål | Resulterande effekt |
| :--- | :--- | :--- |
| **Laser** | Laserförstärkare | Ökar grundskadan och de kritiska träffvärdena |
| **Sköld** | Sköldcell | Ökar sköldkapaciteten och laddningstakten |
| **Motor** | Styrraket | Ökar motorns fart och multiplikatorer |
| **Hybridgenerator** | Sköldcell ELLER styrraket | Ökar sköldkapaciteten, laddningstakten eller farten |
| **Drönare** | Laser eller sköld, i var och en av dess platser (en Master Drone har två) | En laser lägger sin skada till din salva; en sköld räknas som en i en kärnplats (100 % av sina grundvärden) |

---

## Ammunitionshantering {#ammo-management}

Laserammunition är en förbrukningsresurs.
- Ammunition staplas i ditt inventarie.
- Du kan byta aktiv laserammunition via snabbfältet i din HUD.
- Ammunition av högre kvalitet ger skademultiplikatorer (t.ex. standard x1, Advanced Plasma x2, Ultra Core x3, Experimental Fusion Core x4). Siphon Battery gör x1 skada bara mot sköldar och ger den till din egen.
