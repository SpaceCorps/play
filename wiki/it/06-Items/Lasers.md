<!-- wiki-i18n source: d64d048fd518e14c -->
<!-- wiki-i18n title: Laser -->
# Laser e munizioni {#lasers-ammo}

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
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-3, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp 1 | laser-amp, shoddy | buy 10000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp 1 | laser-amp, shoddy | buy 15000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Arc Amp | laser-amp, uncommon | buy 60000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Focus Amp | laser-amp, uncommon | buy 60000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Pulse Amp | laser-amp, rare | buy 1500 Thulium | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Prism Amp | laser-amp, rare | buy 1500 Thulium | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Nova Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Pulse Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Apex Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Prism Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Standard Battery | ammo, common | buy 10 Credits | /wiki/06-Items/Lasers.md#laser-ammunition
Siphon Battery | ammo, rare | buy 0.25 Thulium | /wiki/06-Items/Lasers.md#siphon-battery
Advanced Plasma | ammo, rare | buy 0.5 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Ultra Core | ammo, rare | buy 1 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Experimental Fusion Core | ammo, epic | buy 2.2 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition

Quantum Laser 1 -> Quantum Laser 2 -> Quantum Laser 3 => Starfire-3 => Helios Beam
Damage Amp 1 -> Arc Amp -> Pulse Amp => Nova Amp
Crit Amp 1 -> Focus Amp -> Prism Amp => Apex Amp
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

Il Quantum Laser 1 e il 2 non hanno una probabilità critica propria (“–”): la portano un Damage Amp o un Crit Amp nei loro slot. I colpi critici appaiono in un colore diverso nei numeri di danno fluttuanti (azzurro ghiaccio, più grandi, con un “!”).

### Creare i tre laser più alti {#making-the-top-three-lasers}

Il **Quantum Laser 3**, la **Starfire-3** e l’**Helios Beam** si creano solo in **Assemblaggio**. Il Quantum Laser 3 non si vende più nel Negozio; un pilota che ne possiede già uno lo tiene. Ogni ricetta richiede piastre dalla Fucina dello [Skylab](/wiki/03-Mechanics/Skylab.md):

| Laser | Tempo di creazione | Occorrente |
| :--- | :---: | :--- |
| Quantum Laser 3 | 1 min | 10 Ship Fragment, 2 Velkonite Reinforced Plate, 1.500 Thulium |
| Starfire-3 | 1 min | 1 Quantum Laser 3, 15 Ship Fragment, 8 Velkonite Reinforced Plate, 1 Reinforced Hull Plate, 1.500 Thulium, 100.000 crediti |
| Helios Beam | 3 min | 1 Starfire-3, 50 Cataclysite, 2 Power Core, 18 Orvium Reinforced Plate, 4 Reinforced Hull Plate, 2.000 Thulium |

La pagina Assemblaggio mostra ciò che hai rispetto a ciò che richiede una ricetta, e il pulsante Assembla dice che cosa ti manca. Punta il cursore sull’immagine o sul nome di una ricetta, o su uno dei suoi materiali, per leggere la descrizione completa e le statistiche dell’oggetto.

**La Starfire-3 si ottiene da un Quantum Laser 3.** Crei prima il Quantum Laser 3 e la Starfire-3 lo consuma. Ciò che il Quantum Laser 3 ha già richiesto non viene chiesto di nuovo, quindi i due insieme costano esattamente ciò che costava una Starfire-3 da sola: 3.000 Thulium, 100.000 crediti, 25 Ship Fragment, 10 Velkonite Reinforced Plate, 1 Reinforced Hull Plate e 2 minuti. Se hai già un Quantum Laser 3, paghi solo la parte propria della Starfire-3. Le regole sono quelle dell’Helios Beam, qui sotto: la Starfire-3 mantiene il grado di incantamento del Quantum Laser 3 che consuma (un Quantum Laser 3 Divino produce una Starfire-3 Divina) e i suoi bonus vengono generati di nuovo; scegli tu quale Quantum Laser 3 va, la scheda chiede conferma prima di usarne uno sopra Standard, e il Quantum Laser 3 deve essere libero: **toglilo prima dalla nave** (i suoi amp tornano nel tuo inventario) e dal Deposito di trasporto. Il pulsante Assembla dice “Rimuovi Quantum Laser 3” quando è su una nave.

**L’Helios Beam si ottiene da una Starfire-3.** Crei prima la Starfire-3 (3.000 Thulium e 100.000 crediti, con il suo Quantum Laser 3) e l’Helios Beam la consuma, come il [Master Drone](/wiki/06-Items/Drones.md) consuma uno Slave Drone. Ciò che la Starfire-3 ha già richiesto non viene chiesto di nuovo, quindi i due insieme costano i 5.000 Thulium, la Cataclysite, i Power Core e le Reinforced Hull Plate che l’Helios Beam chiedeva da solo, e 18 piastre di Orvium invece di 20 (le dieci piastre di Velkonite della Starfire-3 sostituiscono le due mancanti); in più paghi i 100.000 crediti e i 25 Ship Fragment della Starfire-3. La regola è quella dei [potenziamenti dei moduli](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly): l’Helios Beam mantiene il grado di incantamento della Starfire-3 che consuma (una Starfire-3 Divina produce un Helios Beam Divino) e i suoi bonus vengono generati di nuovo; scegli tu quale Starfire-3 va se ne possiedi diverse, e la scheda chiede conferma prima di usarne una sopra Standard. La Starfire-3 deve essere libera: **toglila prima dalla nave** (gli amp montati al suo interno tornano nel tuo inventario) e dal Deposito di trasporto. Il pulsante Assembla dice “Rimuovi Starfire-3” quando è su una nave.

Da dove vengono le piastre:

- Le **Velkonite Reinforced Plate** (Quantum Laser 3 e Starfire-3) si forgiano dalla Velkonite, 40 unità di minerale per piastra al livello 1 della Fucina. Le **Orvium Reinforced Plate** (Helios Beam) si forgiano dall’Orvium, 80 unità di minerale per piastra.
- Il minerale viene solo dai collettori del tuo Skylab. Un Collettore Velkonite di livello 5 estrae circa 29 Velkonite all’ora, quindi le piastre di un Quantum Laser 3 richiedono circa 3 ore di estrazione e le dieci piastre di una Starfire-3 (due nel suo Quantum Laser 3, otto nel suo passaggio) circa 14. L’Helios Beam è il più lungo: le sue 18 piastre richiedono 1.440 Orvium, circa 4 giorni con un Collettore Orvium di livello 5.
- Il Magazzino risorse contiene 900 unità per ogni minerale al livello 1, quindi forgia man mano (un lotto della Fucina è di 10 piastre al livello 1) oppure potenzia il magazzino.
- Le piastre forgiate restano nella Fucina finché non le ritiri a nave atterrata, e finiscono nel tuo inventario come oggetti normali.

Ship Fragment, Cataclysite, Power Core e Reinforced Hull Plate li lasciano gli alieni; ogni fonte e ogni uso di ciascun materiale è nella pagina [Risorse](/wiki/06-Items/Resources.md); le liste del bottino nelle pagine del [Bulwark](/wiki/04-Aliens/Bulwark.md) e del [Goombah](/wiki/04-Aliens/Goombah.md) mostrano quanto.

---

## Amplificatori laser (amp) {#laser-amplifiers-amps-}

Montali direttamente nello slot di un laser per potenziarne le caratteristiche. Ci sono due linee, di quattro gradini ciascuna: la **linea del danno** aggiunge una quantità fissa di danno e la **linea critica** aggiunge probabilità critica e danno critico fisso.

| Nome | Rarità | Bonus danno base | Bonus prob. critico | Danno critico fisso | Costo |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Damage Amp 1** | Scadente | +10 | +5% | +5 | 10.000 crediti |
| **Arc Amp** | Non comune | +16 | +5% | +8 | 60.000 crediti |
| **Pulse Amp** | Raro | +26 | +6% | +13 | 1.500 Thulium |
| **Nova Amp** | Epico | +38 | +7% | +20 | Solo da creare |
| **Crit Amp 1** | Scadente | +0 | +15% | +0 | 15.000 crediti |
| **Focus Amp** | Non comune | +0 | +20% | +14 | 60.000 crediti |
| **Prism Amp** | Raro | +0 | +25% | +24 | 1.500 Thulium |
| **Apex Amp** | Epico | +0 | +25% | +44 | Solo da creare |

Il Nova Amp e l’Apex Amp si creano in [Assemblaggio](/wiki/06-Items/Overview.md#upgrading-modules) da un Pulse Amp e da un Prism Amp, con Thulium, drop e 3 Velkonite Reinforced Plate ciascuno dal tuo Skylab. Mantengono il grado di incantamento dell’amp che consumano e i loro bonus vengono generati di nuovo ([Potenziamenti dei moduli](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)).

### Quale amp va dove {#which-amp-goes-where}

Un amp di danno aggiunge lo stesso danno a qualsiasi laser, quindi vale di più sui **Quantum Laser**. Un amp critico moltiplica ciò che il laser fa già, quindi vale di più quanto più forte colpisce il laser: sulla **Starfire-3** pareggia con la linea del danno e sull’**Helios Beam** risulta in vantaggio di circa il 3,5%. La probabilità critica di un laser si ferma al 100%: tre Prism Amp o Apex Amp portano un Helios Beam esattamente a quel valore.

Riempito con lo stesso amp, un laser è sempre più forte di quello inferiore, quindi un amp migliore non sostituisce mai un laser migliore: un Quantum Laser 3 con tre Nova Amp fa meno danno di un Helios Beam con tre Damage Amp 1 (con pezzi dello stesso grado di incantamento: un Quantum Laser 3 e dei Nova Amp forgiati a Divino o oltre, con i valori migliori, possono superare un Helios Beam semplice con dei Damage Amp 1, per un soffio a Divino).

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

La **penetrazione dello scudo** viene tolta all’assorbimento del bersaglio per ogni colpo delle tue raffiche: gli scudi prendono l’assorbimento del bersaglio meno la penetrazione (vedi [Meccaniche degli scudi](/wiki/03-Mechanics/Shields.md#shield-penetration)). Contro una nave all’80% (il miglior scudo con le migliori celle) il 10% delle munizioni x4 lascia agli scudi il 70% del colpo e allo scafo il 30%. Conta di più contro le navi il cui scafo è piccolo rispetto allo scudo; una nave molto grande all’80% regge allo stesso modo in entrambi i casi. Gli alieni non hanno una vera statistica di assorbimento (i loro scudi prendono l’80% di un colpo), e la penetrazione si toglie anche da quello.

### Siphon Battery {#siphon-battery}

La Siphon Battery è una munizione per rubare scudi invece di spaccare scafi. Infligge **danno x1 direttamente allo scudo del bersaglio** e aggiunge la stessa quantità al **tuo scudo**, fino al massimo. Scegliila dal selettore delle munizioni della barra rapida come qualsiasi altra munizione (è il riquadro con il vortice turchese). Non spara un raggio: una sonda turchese sottile e tenue parte verso il bersaglio, lo scudo del bersaglio si accende di turchese dove arriva, e lo scudo che hai drenato torna visibilmente verso la tua nave sotto forma di pacchetti turchesi luminosi (da tre a dieci, di più per un drenaggio più grande), uno dopo l’altro nell’arco di circa mezzo secondo. Ogni pacchetto che arriva fa pulsare il tuo scudo. Lo stesso lo vedi per la Siphon Battery di ogni pilota in vista, chiunque drenino: alieni, altri piloti e navi dei piloti di corporazione.

- **Solo scudo**: lo scafo non viene mai toccato, l’assorbimento del bersaglio non ripartisce il danno e una Siphon Battery non può mai distruggere nulla. Il suo danno è limitato da ciò che lo scudo del bersaglio ha ancora.
- **Niente da prendere**: contro un bersaglio senza più scudo non drena e non dà nulla. La raffica viene comunque spesa, una batteria per laser, come con ogni munizione. Vedi solo la sonda e un debole sfarfallio sullo scafo, e nessun pacchetto.
- **Guadagno**: il tuo scudo non supera mai il massimo, e prendere scudo non ritarda la rigenerazione del tuo scudo.
- **Alieni e piloti** hanno entrambi scudi da drenare. Un drenaggio che toglie scudo a un alieno conta come colpo per la [rivendicazione del primo colpo](/wiki/03-Mechanics/Combat.md); uno che non trova scudo no. Sveglia anche un Seeker o un Goombah, che reagiscono soltanto, come qualsiasi altro colpo.
- **I colpi critici** contano: una raffica critica drena 1,5 volte tanto e il suo numero viene mostrato come colpo critico. I suoi pacchetti sono più grandi e luminosi, e lo scudo del bersaglio si accende più forte.
- I [piloti di corporazione](/wiki/03-Mechanics/Company-Pilots.md) sparano munizioni standard x1.
