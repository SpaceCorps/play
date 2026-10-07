<!-- wiki-i18n source: fbb5e8cfaee8aa9f -->
<!-- wiki-i18n title: Laser -->
# Laser e munizioni {#lasers-ammo}

<!-- wiki-search: arc amp; focus amp; pulse amp; prism amp; nova amp; apex amp; damage amp 1; crit amp 1; amps; penetration amp; shield penetration -->

Le armi sono il mezzo principale per infliggere danno in SpaceCorps.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Albero degli oggetti {#item-tree}

Ciò che crea l’Assemblaggio richiede prima la sua tecnologia; passa il puntatore su un oggetto per vedere quanto tempo serve a ricercarla. L’albero delle tecnologie, il carburante e il boost: [Ricerca](/wiki/03-Mechanics/Research.md).

```tree
Quantum Laser 1 | laser, shoddy | buy 8000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser 2 | laser, common | buy 80000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser 3 | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-3 | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser 3, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-3, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp I | laser-amp, shoddy | buy 10000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp I | laser-amp, shoddy | buy 15000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp I | laser-amp, shoddy | buy 15000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Damage Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Crit Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Penetration Amp I, 20 Daraxium, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Damage Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Crit Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Penetration Amp II, 1 Power Core, 30 Nyxite, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Damage Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Crit Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp IV | laser-amp, epic | craft 1200 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Penetration Amp III, 1 Power Core, 30 Cataclysite, 40 Quorvium, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Standard Battery | ammo, common | buy 10 Credits | /wiki/06-Items/Lasers.md#laser-ammunition
Siphon Battery | ammo, rare | buy 0.25 Thulium | /wiki/06-Items/Lasers.md#siphon-battery
Advanced Plasma | ammo, rare | buy 0.5 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Ultra Core | ammo, rare | buy 1 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Experimental Fusion Core | ammo, epic | buy 2.2 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition

Quantum Laser 1 -> Quantum Laser 2 -> Quantum Laser 3 => Starfire-3 => Helios Beam
Damage Amp I => Damage Amp II => Damage Amp III => Damage Amp IV
Crit Amp I => Crit Amp II => Crit Amp III => Crit Amp IV
Penetration Amp I => Penetration Amp II => Penetration Amp III => Penetration Amp IV
Standard Battery -> Advanced Plasma -> Ultra Core -> Experimental Fusion Core
```
<!-- item-tree:end -->

## Laser {#lasers}

Equipaggia i laser direttamente negli slot laser della nave o dentro i droni per aumentare la tua capacità offensiva.

| Nome | Rarità | Danno base | Prob. critico | Portata | Slot amp | Costo |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Quantum Laser 1** | Scadente | 55 | – | 600 | 1 | 8.000 crediti |
| **Quantum Laser 2** | Comune | 65 | – | 700 | 2 | 80.000 crediti |
| **Quantum Laser 3** | Raro | 80 | 10% | 800 | 3 | Solo da creare |
| **Starfire-3** | Mitico | 135 | 15% | 850 | 3 | Solo da creare |
| **Helios Beam** | Mitico | 185 | 25% | 900 | 3 | Solo da creare |

La colonna Portata è quella di ciascun laser. **La tua nave spara alla media delle portate dei suoi laser** (contano anche i laser nei tuoi droni), arrotondata all’unità più vicina, e ogni laser spara quando il bersaglio è entro quella distanza. Una Starfire-3 accanto a due Quantum Laser 2 dà alla nave una portata di 750, non di 850; tre Starfire-3 mantengono 850, e laser tutti uguali non cambiano nulla. Un bonus di portata della Forgia conta sul proprio laser prima che si faccia la media. Senza laser l’Hangar non indica nessuna portata (un trattino) e i laser non possono sparare, ma i tuoi razzi sì, ognuno con la propria portata (vedi [Razzi](/wiki/06-Items/Rockets.md)). Nell’Hangar il riquadro dice “Portata media” dove i tuoi laser differiscono, e passandoci sopra elenca la portata di ciascun laser.

Il Quantum Laser 1 e il 2 non hanno una probabilità critica propria (“–”): la porta un Damage Amp o un Crit Amp nei loro slot (un Penetration Amp no). I colpi critici appaiono in un colore diverso nei numeri di danno fluttuanti (azzurro ghiaccio, più grandi, con un “!”; vedi [Numeri di danno e di cura](/wiki/03-Mechanics/Combat.md#damage-and-heal-numbers)).

I laser danneggiano anche gli [asteroidi](/wiki/03-Mechanics/Asteroid-Mining.md#breaking-one), ma solo al 5% di quello che una raffica fa a una nave (contano i tuoi amp, booster, munizioni e colpi critici, poi si toglie la corazza dell’asteroide; la Siphon Battery non può danneggiarne nessuno). Per spezzarli lo strumento sono i razzi.

### Creare i tre laser più alti {#making-the-top-three-lasers}

Il **Quantum Laser 3**, la **Starfire-3** e l’**Helios Beam** si creano solo in **Assemblaggio**. Il Quantum Laser 3 non si vende più nel Negozio; un pilota che ne possiede già uno lo tiene. Ogni ricetta richiede piastre dalla Fucina dello [Skylab](/wiki/03-Mechanics/Skylab.md), e l’Helios Beam anche 3 Dark Matter Plate:

| Laser | Tempo di creazione | Occorrente |
| :--- | :---: | :--- |
| Quantum Laser 3 | 1 min | 10 Ship Fragment, 2 Velkonite Reinforced Plate, 1.500 Thulium |
| Starfire-3 | 1 min | 1 Quantum Laser 3, 15 Ship Fragment, 8 Velkonite Reinforced Plate, 1 Reinforced Hull Plate, 1.500 Thulium, 100.000 crediti |
| Helios Beam | 3 min | 1 Starfire-3, 50 Cataclysite, 2 Power Core, 18 Orvium Reinforced Plate, 3 Dark Matter Plate, 4 Reinforced Hull Plate, 2.000 Thulium |

La pagina Assemblaggio mostra ciò che hai rispetto a ciò che richiede una ricetta, e il pulsante Assembla dice che cosa ti manca. Punta il cursore sull’immagine o sul nome di una ricetta, o su uno dei suoi materiali, per leggere la descrizione completa e le statistiche dell’oggetto.

**La Starfire-3 si ottiene da un Quantum Laser 3.** Crei prima il Quantum Laser 3 e la Starfire-3 lo consuma. Ciò che il Quantum Laser 3 ha già richiesto non viene chiesto di nuovo, quindi i due insieme costano esattamente ciò che costava una Starfire-3 da sola: 3.000 Thulium, 100.000 crediti, 25 Ship Fragment, 10 Velkonite Reinforced Plate, 1 Reinforced Hull Plate e 2 minuti. Se hai già un Quantum Laser 3, paghi solo la parte propria della Starfire-3. Le regole sono quelle dell’Helios Beam, qui sotto: la Starfire-3 mantiene il grado di incantamento del Quantum Laser 3 che consuma (un Quantum Laser 3 Divino produce una Starfire-3 Divina) e i suoi bonus vengono generati di nuovo; scegli tu quale Quantum Laser 3 va, la scheda chiede conferma prima di usarne uno sopra Standard, e il Quantum Laser 3 deve essere libero: **toglilo prima dalla nave** (i suoi amp tornano nel tuo inventario) e dal Deposito di trasporto. Il pulsante Assembla dice “Rimuovi Quantum Laser 3” quando è su una nave.

**L’Helios Beam si ottiene da una Starfire-3.** Crei prima la Starfire-3 (3.000 Thulium e 100.000 crediti, con il suo Quantum Laser 3) e l’Helios Beam la consuma, come il [Master Drone](/wiki/06-Items/Drones.md) consuma uno Slave Drone. Ciò che la Starfire-3 ha già richiesto non viene chiesto di nuovo, quindi i due insieme costano i 5.000 Thulium, la Cataclysite, i Power Core e le Reinforced Hull Plate che l’Helios Beam chiedeva da solo, e 18 piastre di Orvium invece di 20 (le dieci piastre di Velkonite della Starfire-3 sostituiscono le due mancanti), più, poiché l’Helios Beam è l’ultimo tier della sua catena, 3 Dark Matter Plate; in più paghi i 100.000 crediti e i 25 Ship Fragment della Starfire-3. La regola è quella dei [potenziamenti dei moduli](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly): l’Helios Beam mantiene il grado di incantamento della Starfire-3 che consuma (una Starfire-3 Divina produce un Helios Beam Divino) e i suoi bonus vengono generati di nuovo; scegli tu quale Starfire-3 va se ne possiedi diverse, e la scheda chiede conferma prima di usarne una sopra Standard. La Starfire-3 deve essere libera: **toglila prima dalla nave** (gli amp montati al suo interno tornano nel tuo inventario) e dal Deposito di trasporto. Il pulsante Assembla dice “Rimuovi Starfire-3” quando è su una nave.

Da dove vengono le piastre:

- Le **Velkonite Reinforced Plate** (Quantum Laser 3 e Starfire-3) si forgiano dalla Velkonite, 40 unità di minerale per piastra al livello 1 della Fucina. Le **Orvium Reinforced Plate** (Helios Beam) si forgiano dall’Orvium, 80 unità di minerale per piastra.
- Le **Dark Matter Plate** (3 per l’Helios Beam) si pressano in Assemblaggio da 5 Dark Matter, una Velkonite Reinforced Plate, una Orvium Reinforced Plate e 250 Thulium, dopo che hai ricercato la loro ricetta. Le tre richiedono 15 Dark Matter, 7,5 razzi N.I.K.E. in media dal [buco nero](/wiki/03-Mechanics/Black-Hole.md): [Dark Matter e Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md) mostra tutto il percorso.
- Il minerale viene solo dai collettori del tuo Skylab. Un Collettore Velkonite di livello 5 estrae 18 Velkonite all’ora, quindi le piastre di un Quantum Laser 3 richiedono circa 4 ore di estrazione e le dieci piastre di una Starfire-3 (due nel suo Quantum Laser 3, otto nel suo passaggio) circa 22. L’Helios Beam è il più lungo: le sue 18 piastre richiedono 1.440 Orvium, circa 4 giorni con un Collettore Orvium di livello 5, e le 3 piastre di Orvium in più dentro le sue 3 Dark Matter Plate aggiungono 240 Orvium, circa 17 ore.
- Il Magazzino risorse contiene 240 unità per ogni minerale al livello 1: 6 piastre di Velkonite o 3 di Orvium con la Fucina al livello 1. Quindi forgia man mano (un lotto della Fucina è fino a 10 piastre al livello 1) oppure potenzia il magazzino.
- Le piastre forgiate restano nella Fucina finché non le ritiri a nave atterrata, e finiscono nel tuo inventario come oggetti normali.

Ship Fragment, Cataclysite, Power Core e Reinforced Hull Plate li lasciano gli alieni; ogni fonte e ogni uso di ciascun materiale è nella pagina [Risorse](/wiki/06-Items/Resources.md); le liste del bottino nelle pagine del [Bulwark](/wiki/04-Aliens/Bulwark.md) e del [Goombah](/wiki/04-Aliens/Goombah.md) mostrano quanto.

---

## Amplificatori laser (amp) {#laser-amplifiers-amps-}

Montali direttamente nello slot di un laser per potenziarne le caratteristiche. Ci sono **tre linee di quattro tier**, chiamate come le celle scudo: il **Damage Amp** aggiunge una quantità fissa di danno, il **Crit Amp** aggiunge probabilità critica e danno critico fisso, e il **Penetration Amp** toglie punti all’assorbimento del tuo bersaglio ([più sotto](#shield-penetration-of-a-laser-hit)). Non sono i [booster](/wiki/06-Items/Boosters.md): il **Laser Damage Booster 1** e il **Laser Damage Booster 2** sono booster a tempo (+10% di danno laser per 10 ore), senza nulla da montare.

| Nome | Rarità | Bonus danno base | Bonus prob. critico | Danno critico fisso | Costo |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Damage Amp I** | Scadente | +10 | +5% | +5 | 10.000 crediti |
| **Damage Amp II** | Non comune | +16 | +5% | +8 | Solo da creare |
| **Damage Amp III** | Raro | +26 | +6% | +13 | Solo da creare |
| **Damage Amp IV** | Epico | +38 | +7% | +20 | Solo da creare |
| **Crit Amp I** | Scadente | +0 | +15% | +0 | 15.000 crediti |
| **Crit Amp II** | Non comune | +0 | +20% | +14 | Solo da creare |
| **Crit Amp III** | Raro | +0 | +25% | +24 | Solo da creare |
| **Crit Amp IV** | Epico | +0 | +25% | +44 | Solo da creare |

| Nome | Rarità | Penetrazione scudo | Costo |
| :--- | :--- | :---: | :--- |
| **Penetration Amp I** | Scadente | +2% | 15.000 crediti |
| **Penetration Amp II** | Non comune | +4% | Solo da creare |
| **Penetration Amp III** | Raro | +6% | Solo da creare |
| **Penetration Amp IV** | Epico | +8% | Solo da creare |

**Solo il primo tier di ogni linea è in vendita**, nel Negozio. Gli altri tre si creano in [Assemblaggio](/wiki/06-Items/Overview.md#upgrading-modules) dall’amp del tier sotto, dopo aver ricercato la loro tecnologia nello Skylab ([Ricerca](/wiki/03-Mechanics/Research.md)). Ogni passo richiede Thulium, drop degli alieni e piastre (Velkonite Reinforced Plate dal tuo Skylab per i tier II e III, 3 Dark Matter Plate per il tier IV), e il nuovo amp mantiene il grado di incantamento dell’amp che consuma mentre i suoi bonus vengono generati di nuovo ([Potenziamenti dei moduli nell’Assemblaggio](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). I passi Penetration aggiungono una lente di cristallo. Ogni amp del tier IV richiede 3 [Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md), come l’ultimo tier di ogni catena di potenziamento: la tecnologia di un amp del tier IV richiede quindi prima quella della plate.

| Passo | Thulium | Tempo | Oltre all’amp del tier sotto |
| :--- | ---: | ---: | :--- |
| Damage Amp II / Crit Amp II | 250 | 60 s | 10 Cataclysite, 1 Velkonite Reinforced Plate |
| Damage Amp III / Crit Amp III | 1.000 | 60 s | 20 Cataclysite, 1 Power Core, 2 Velkonite Reinforced Plate |
| Damage Amp IV / Crit Amp IV | 1.200 | 60 s | 30 Cataclysite, 1 Power Core, 3 Dark Matter Plate |
| Penetration Amp II | 250 | 60 s | 20 Daraxium, 10 Cataclysite, 1 Velkonite Reinforced Plate |
| Penetration Amp III | 1.000 | 60 s | 30 Nyxite, 20 Cataclysite, 1 Power Core, 2 Velkonite Reinforced Plate |
| Penetration Amp IV | 1.200 | 90 s | 40 Quorvium, 30 Cataclysite, 1 Power Core, 3 Dark Matter Plate |

Un Helios Beam con i suoi 3 amp del tier IV contiene 4 pezzi dell’ultimo tier: 12 Dark Matter Plate, 60 Dark Matter, 30 razzi N.I.K.E. in media. Un Wraith con l’ultimo tier in ogni slot contiene 900 Dark Matter ([Dark Matter e Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md#what-the-last-tier-asks-for)).

### Quale amp va dove {#which-amp-goes-where}

Un amp di danno aggiunge lo stesso danno a qualsiasi laser, quindi vale di più sui **Quantum Laser**. Un amp critico moltiplica ciò che il laser fa già, quindi vale di più quanto più forte colpisce il laser: sulla **Starfire-3** pareggia con la linea del danno e sull’**Helios Beam** risulta in vantaggio di circa il 3,5%. La probabilità critica di un laser si ferma al 100%: tre Crit Amp III o Crit Amp IV portano un Helios Beam esattamente a quel valore. Un Penetration Amp non dà né danno né probabilità critica: serve contro le navi i cui scudi altrimenti prenderebbero la maggior parte del tuo colpo ([più sotto](#when-is-a-penetration-amp-worth-a-slot)).

Riempito con lo stesso amp, un laser è sempre più forte di quello inferiore, quindi un amp migliore non sostituisce mai un laser migliore: un Quantum Laser 3 con tre Damage Amp IV fa meno danno di un Helios Beam con tre Damage Amp I (con pezzi dello stesso grado di incantamento: un Quantum Laser 3 e dei Damage Amp IV forgiati a Divino o oltre, con i valori migliori, possono superare un Helios Beam semplice con dei Damage Amp I, per un soffio a Divino).


---

## Munizioni laser {#laser-ammunition}

Batterie consumabili che moltiplicano il danno delle tue raffiche laser:

| Nome | Rarità | Molt. danno | Penetrazione scudo | Prezzo per unità |
| :--- | :--- | :---: | :---: | :--- |
| **Standard Battery** | Comune | 1,0x | – | 10 crediti |
| **Advanced Plasma** | Raro | 2,0x | – | 0,5 Thulium |
| **Ultra Core** | Raro | 3,0x | 5% | 1,0 Thulium |
| **Experimental Fusion Core** | Epico | 4,0x | 10% | 2,2 Thulium |
| **Siphon Battery** | Raro | 1,0x, solo scudi | – | 0,25 Thulium |

La **penetrazione dello scudo** viene tolta all’assorbimento del bersaglio per ogni colpo delle tue raffiche: gli scudi prendono l’assorbimento del bersaglio meno la penetrazione (vedi [Meccaniche degli scudi](/wiki/03-Mechanics/Shields.md#shield-penetration)). I tuoi Penetration Amp e una formazione di droni si sommano a quella delle munizioni, e la somma intera è [più sotto in questa pagina](#shield-penetration-of-a-laser-hit). Contro una nave all’80% (il miglior scudo con le migliori celle) il 10% delle munizioni x4 lascia agli scudi il 70% del colpo e allo scafo il 30%. Conta di più contro le navi il cui scafo è piccolo rispetto allo scudo; una nave molto grande all’80% regge allo stesso modo in entrambi i casi. Gli alieni non hanno una vera statistica di assorbimento (i loro scudi prendono l’80% di un colpo), e la penetrazione si toglie anche da quello.

### Siphon Battery

La Siphon Battery è una munizione per rubare scudi invece di spaccare scafi. Infligge **danno x1 direttamente allo scudo del bersaglio** e aggiunge la stessa quantità al **tuo scudo**, fino al massimo. Scegliila dal selettore delle munizioni della barra rapida come qualsiasi altra munizione (è il riquadro con il vortice turchese). Non spara un raggio: una sonda turchese sottile e tenue parte verso il bersaglio, lo scudo del bersaglio si accende di turchese dove arriva, e lo scudo che hai drenato torna visibilmente verso la tua nave sotto forma di pacchetti turchesi luminosi (da tre a dieci, di più per un drenaggio più grande), uno dopo l’altro nell’arco di circa mezzo secondo. Ogni pacchetto che arriva fa pulsare il tuo scudo. Lo stesso lo vedi per la Siphon Battery di ogni pilota in vista, chiunque drenino: alieni, altri piloti e navi dei piloti di corporazione.

- **Solo scudo**: lo scafo non viene mai toccato, l’assorbimento del bersaglio non ripartisce il danno e una Siphon Battery non può mai distruggere nulla. Il suo danno è limitato da ciò che lo scudo del bersaglio ha ancora.
- **Niente da prendere**: contro un bersaglio senza più scudo non drena e non dà nulla. La raffica viene comunque spesa, una batteria per laser, come con ogni munizione. Vedi solo la sonda e un debole sfarfallio sullo scafo, e nessun pacchetto.
- **Guadagno**: il tuo scudo non supera mai il massimo, e prendere scudo non ritarda la rigenerazione del tuo scudo.
- **Alieni e piloti** hanno entrambi scudi da drenare. Un drenaggio che toglie scudo a un alieno conta come colpo per la [rivendicazione del primo colpo](/wiki/03-Mechanics/Combat.md); uno che non trova scudo no. Sveglia anche un Seeker o un Goombah, che reagiscono soltanto, come qualsiasi altro colpo.
- **I colpi critici** contano: una raffica critica drena 1,5 volte tanto e il suo numero viene mostrato come colpo critico. I suoi pacchetti sono più grandi e luminosi, e lo scudo del bersaglio si accende più forte.
- I [piloti di corporazione](/wiki/03-Mechanics/Company-Pilots.md) sparano munizioni standard x1.

---

## Penetrazione dello scudo di un colpo laser {#shield-penetration-of-a-laser-hit}

Ogni colpo laser toglie punti all’assorbimento del tuo bersaglio, da un massimo di tre fonti che si sommano: le tue **munizioni** (Ultra Core 5%, Experimental Fusion Core 10%), i tuoi **Penetration Amp** e una **formazione di droni** (Gemini +9%, Stiletto +16%; [Formazioni di droni](/wiki/03-Mechanics/Formations.md)). Il totale **si ferma al 50%** per un laser; quello di un razzo diretto si ferma al 40% ([Razzi](/wiki/06-Items/Rockets.md)). Gli scudi prendono poi l’assorbimento del bersaglio meno la penetrazione del colpo, lo scafo il resto ([Meccaniche degli scudi](/wiki/03-Mechanics/Shields.md#shield-penetration)).

- **I tuoi amp contano come la media dei tuoi laser.** Una raffica è un solo colpo, quindi il gioco somma la penetrazione degli amp di ciascun laser (contano anche i laser nei tuoi droni) e fa la media sui tuoi laser, ciascuno pesato per il suo danno, come per la probabilità critica. Tre Penetration Amp IV in ogni laser fanno 24%; un Penetration Amp IV in un laser su dodici fa 0,67%. Un Wraith ha 12 laser e 36 slot amp, e vanno riempiti tutti e 36 per arrivare al 24%.
- **L’Hangar lo mostra.** Appena gli amp dei tuoi laser danno penetrazione, le statistiche di combattimento dell’Hangar hanno un riquadro **Penetrazione** con il valore; munizioni e formazione non ne fanno parte.
- **Il miglior laser raggiunge il tetto esattamente.** Un Experimental Fusion Core (10%), uno Stiletto (16%) e tre Penetration Amp IV in ogni laser (24%) fanno 50%.
- **Un bonus della Forgia su un Penetration Amp IV è sprecato in quella configurazione.** Un Penetration Amp si forgia come gli altri amp, e il suo unico bonus moltiplica la penetrazione: un bonus Eterno (da +9% a +15%) porta un Penetration Amp IV a 8,7–9,2 punti invece di 8. Ma 10 + 16 + 24 fanno già il tetto del 50%, e ogni punto in più viene tagliato (tre Eterni farebbero 53,6%, tagliato a 50%).

| Raffica laser | Munizioni | Amp (3 slot) | Formazione | Totale |
|---|---|---|---|---|
| Experimental Fusion Core da solo | 10% | – | – | **10%** |
| Fusion Core + Gemini | 10% | – | 9% | **19%** |
| Fusion Core + Stiletto (il migliore prima dei Penetration Amp) | 10% | – | 16% | **26%** |
| Fusion Core + 3 Penetration Amp I | 10% | 6% | – | **16%** |
| Fusion Core + 3 Penetration Amp II | 10% | 12% | – | **22%** |
| Fusion Core + 3 Penetration Amp III | 10% | 18% | – | **28%** |
| Fusion Core + 3 Penetration Amp IV | 10% | 24% | – | **34%** |
| Fusion Core + 3 Penetration Amp IV + Gemini | 10% | 24% | 9% | **43%** |
| Ultra Core + 3 Penetration Amp IV + Stiletto (il migliore di ogni giorno) | 5% | 24% | 16% | **45%** |
| Fusion Core + 3 Penetration Amp IV + Stiletto (il miglior laser) | 10% | 24% | 16% | **50%** |

Cosa fa questo agli scudi del bersaglio: ogni cella è la quota di un colpo che **gli scudi prendono / lo scafo prende**.

| Difensore (assorbimento) | Senza amp | Fusion Core da solo (10%) | Prima: Fusion Core + Stiletto (26%) | Fusion Core + 3 Penetration Amp IV (34%) | Il miglior laser (50%) |
|---|---|---|---|---|---|
| Light Shield Core, senza celle (45%) | 45 / 55 | 35 / 65 | 19 / 81 | 11 / 89 | 0 / 100 |
| Heavy Shield Core, senza celle (50%) | 50 / 50 | 40 / 60 | 24 / 76 | 16 / 84 | 0 / 100 |
| Light Shield Core + Absorption Shield Cell IV (55%) | 55 / 45 | 45 / 55 | 29 / 71 | 21 / 79 | 5 / 95 |
| Heavy Shield Core + 3 Capacity Shield Cell IV (65%) | 65 / 35 | 55 / 45 | 39 / 61 | 31 / 69 | 15 / 85 |
| Il miglior scudo di serie (80%) | 80 / 20 | 70 / 30 | 54 / 46 | 46 / 54 | 30 / 70 |
| Il miglior scudo, Forgia Eterna (miglior tiro) e 34 livelli dell’Emporio (95,4%) | 95 / 5 | 85 / 15 | 69 / 31 | 61 / 39 | 45 / 55 |
| Il miglior scudo, Forgia Eterna (miglior tiro) e l’Emporio al suo limite (102%) | 100 / 0 | 92 / 8 | 76 / 24 | 68 / 32 | 52 / 48 |
| Qualsiasi alieno (80%) | 80 / 20 | 70 / 30 | 54 / 46 | 46 / 54 | 30 / 70 |

Il miglior laser svuota un nucleo scudo senza cella (lo scafo prende tutto il colpo); un nucleo con una cella conserva una quota di ogni colpo, e il miglior scudo ne conserva il 30% (il 45% con i bonus). Un razzo non svuota mai uno scudo: il suo tetto è il 40%.

### Quando vale uno slot un Penetration Amp? {#when-is-a-penetration-amp-worth-a-slot}

**Un Penetration Amp contrasta un assorbimento oltre il 95% circa (configurazioni con Emporio, Forgia e Rampart). Contro il miglior scudo di serie (80%) un Crit Amp dello stesso tier è comunque circa il 10% più veloce, e un Penetration Amp non uccide gli alieni più in fretta di un Damage Amp o di un Crit Amp del suo tier.**

- **Non dà danno.** Su un Helios Beam, tre Penetration Amp IV fanno 187 di danno a raffica (munizioni x1, la media del tiro e dei critici), dove tre Damage Amp IV ne fanno 356 e tre Crit Amp IV 369: circa la metà. Ciò che riguadagna è la quota dello scudo, quindi conviene solo dove lo scafo è piccolo rispetto allo scudo e l’assorbimento è alto; contro un Wraith o un Ironclad, il cui grande scafo regge comunque, un set semplice di Damage o Crit è più veloce.
- **Alieni.** I loro scudi prendono l’80% di un colpo meno la tua penetrazione, quindi funziona anche su di loro, ma un Damage Amp o un Crit Amp del tier li uccide comunque più in fretta.
- **Quanto costa.** Ogni Penetration Amp IV richiede 3 Dark Matter Plate (15 Dark Matter), come ogni amp del tier IV, quindi un Wraith che riempie i suoi 36 slot ha bisogno di 108 plate, 540 Dark Matter.
