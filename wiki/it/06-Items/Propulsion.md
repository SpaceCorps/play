<!-- wiki-i18n source: 1433a0058afe39fa -->
<!-- wiki-i18n title: Propulsione -->
# Propulsione e velocità {#propulsion-speed}

I sistemi di propulsione determinano la velocità di movimento e la manovrabilità della tua nave.

## In un minuto {#in-one-minute}

- **I motori producono velocità, i propulsori ci stanno dentro e la aumentano.** Un motore ospita da uno a tre propulsori (un Engine I uno, un Engine II due, un Engine III tre), e lo stesso vale per un Nucleo adattivo (il suo tier dice quanti).
- **Due famiglie di quattro tier ciascuna.** Gli Impulse Thruster danno più velocità fissa. I Momentum Thruster danno meno velocità fissa e moltiplicano di più la velocità. In entrambe le famiglie ogni tier è migliore di quello sotto, in entrambi i valori.
- **Quale dove.** Come regola, metti l’Impulse ovunque: solo in un Engine III pieno (tre propulsori) il Momentum dei tier I e II passa in vantaggio. [La tabella qui sotto](#which-thruster-where) ha i numeri. L’Engine III più veloce contiene tre Impulse Thruster IV e fa 52,5.
- **Come ottenerli.** Il tier I di ogni famiglia costa 20.000 crediti. I tier da II a IV si creano nell’Assemblaggio, ciascuno da quello sotto, e un propulsore non cambia mai famiglia.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Albero degli oggetti {#item-tree}

Ciò che crea l’Assemblaggio richiede prima la sua tecnologia; passa il puntatore su un oggetto per vedere quanto tempo serve a ricercarla. L’albero delle tecnologie, il carburante e il boost: [Ricerca](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Engine I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I => Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Motori {#engines}

I motori sono la fonte principale di spinta della tua nave. Un motore in uno **slot abilità** ti dà invece l’**Afterburner** indicato nella colonna Effetto speciale, uno scatto di velocità di dieci secondi (più lungo con più motori), e non aggiunge spinta propria (vedi [Abilità](/wiki/03-Mechanics/Abilities.md)).

| Nome | Rarità | Velocità base | Bonus velocità % | Bonus scudo % | Slot | Effetto speciale | Costo |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Scadente | +2 | +2% | -2% | 1 | Afterburner I | 20.000 crediti |
| **Engine II** | Comune | +4 | +4% | -8% | 2 | Afterburner II | Solo da creare |
| **Engine III** | Raro | +6 | +5% | -15% | 3 | Afterburner III | Solo da creare |

L’**Engine II** si crea in [Assemblaggio](/wiki/06-Items/Overview.md#upgrading-modules) da un Engine I, con 1.000 Thulium, 10 Ship Fragment, 1 Power Core e 2 Velkonite Reinforced Plate. L’**Engine III** si crea lì da un Engine II, con 2.000 Thulium, 60 Ship Fragment, 3 Power Core e 3 Dark Matter Plate ([Dark Matter e Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)). Ciascuno mantiene il grado di incantamento del motore che consuma, e i suoi bonus vengono generati di nuovo ([Potenziamenti dei moduli](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Togli prima dalla tua nave il motore da consumare (e togli da esso i suoi propulsori): un motore montato sulla nave o che contiene propulsori non viene consumato.

Il Bonus scudo dei motori è nei dati dell’oggetto, ma il gioco non lo ha mai applicato: i motori non indeboliscono i tuoi scudi, e le schede degli oggetti lo omettono.

---

## Propulsori {#thrusters}

I propulsori si inseriscono dentro i motori o i Nuclei adattivi per aumentarne la resa in velocità. Ci sono due famiglie di quattro tier ciascuna: gli **Impulse Thruster** danno più velocità fissa e moltiplicano un po’ la velocità del motore in cui sono montati, i **Momentum Thruster** meno velocità fissa, ma la moltiplicano di più. In entrambe le famiglie ogni tier è migliore di quello sotto, sia nella velocità fissa sia nel moltiplicatore. Un motore (o Nucleo adattivo) con dei propulsori produce **la propria velocità base più i bonus di velocità fissi dei propulsori, il tutto per i moltiplicatori di velocità dei propulsori moltiplicati tra loro** ([come si calcola la velocità](/wiki/03-Mechanics/Speed.md)): un Engine III con tre Momentum Thruster IV produce (6 + 3 x 11,135) x 1,0935 x 1,0935 x 1,0935 = 51,5, con tre Impulse Thruster IV (6 + 3 x 14,025) x 1,02975 x 1,02975 x 1,02975 = 52,5, e un Adaptive Core II con due Impulse Thruster IV ne produce (0 + 2 x 14,025) x 1,02975 x 1,02975 = 29,7 (26,6 con due Momentum Thruster IV).

| Nome | Rarità | Bonus velocità fisso | Molt. velocità | Costo |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Scadente | +4,25 | 1,017x | 20.000 crediti |
| **Impulse Thruster II** | Comune | +8,5 | 1,02125x | Solo da creare |
| **Impulse Thruster III** | Raro | +12,75 | 1,0255x | Solo da creare |
| **Impulse Thruster IV** | Epico | +14,025 | 1,02975x | Solo da creare |
| **Momentum Thruster I** | Scadente | +3,825 | 1,051x | 20.000 crediti |
| **Momentum Thruster II** | Comune | +7,65 | 1,0595x | Solo da creare |
| **Momentum Thruster III** | Raro | +10,625 | 1,0765x | Solo da creare |
| **Momentum Thruster IV** | Epico | +11,135 | 1,0935x | Solo da creare |

### Quale propulsore dove {#which-thruster-where}

L’Impulse dà più velocità fissa, il Momentum moltiplica di più, quindi quale sia più veloce dipende da ciò che il motore produce già. La velocità fissa conta di più dove c’è poca velocità da moltiplicare: in un Nucleo adattivo (non ha velocità propria) e in un motore con uno o due propulsori. Un moltiplicatore conta di più in un Engine III pieno, dove c’è molta velocità da moltiplicare, ma lì vincono solo i Momentum Thruster dei tier I e II. La velocità che ciascuno produce con propulsori di tier IV in tutti gli slot:

| Dove stanno i propulsori | Con Impulse Thruster IV | Con Momentum Thruster IV | Più veloce |
| :--- | :---: | :---: | :--- |
| Engine I, 1 propulsore | 16,5 | 14,4 | Impulse |
| Engine II, 2 propulsori | 34,0 | 31,4 | Impulse |
| Engine III, 1 propulsore | 20,6 | 18,7 | Impulse |
| Engine III, 2 propulsori | 36,1 | 33,8 | Impulse |
| Engine III, 3 propulsori | 52,5 | 51,5 | Impulse |
| Adaptive Core II, 2 propulsori | 29,7 | 26,6 | Impulse |

- **Tier più bassi.** I tier più bassi vanno allo stesso modo, con due casi tirati e un’eccezione: con due propulsori in un Engine II le famiglie sono pari ai tier I e II (l’Impulse è avanti di 0,06 e 0,24), e con due in un Engine III lo sono ugualmente (entro 0,1). Dal tier III in poi l’Impulse è avanti in entrambi, di 1,5–2,6. L’eccezione è l’Engine III pieno: lì il Momentum è avanti ai tier I e II, di 0,6 e 0,9, e l’Impulse ai tier III e IV, di 0,5 e 1,0.
- **L’Engine III più veloce.** Contiene tre Impulse Thruster IV: 52,5, un po’ sopra un Impulse e due Momentum Thruster IV (52,1) o tre Momentum (51,5).

Il bonus al moltiplicatore di velocità di un propulsore, della [Forgia](/wiki/06-Items/Forge.md), fa crescere la parte sopra 1 (un bonus di +15% su 1,0935x dà 1,1075x), e la Forgia non genera alcun bonus su un moltiplicatore di 1,05x o inferiore: sull’1,017x–1,02975x di un Impulse Thruster aggiungerebbe meno di 0,005 (+15% su 1,02975x dà 1,034x). Un Impulse Thruster contiene un bonus (la sua velocità fissa), un Momentum Thruster due.

Il tier I di ogni famiglia si compra a 20.000 crediti. I tier da II a IV si creano in [Assemblaggio](/wiki/06-Items/Overview.md#upgrading-modules), ciascuno dal propulsore della stessa famiglia un tier più in basso (un Impulse Thruster II da un Impulse Thruster I, un III da un II, un IV da un III), con Thulium, drop e piastre: 2 o 4 Velkonite Reinforced Plate dal tuo Skylab per il tier II o III, e 3 Dark Matter Plate per il tier IV. Un propulsore non cambia mai famiglia: scegli Impulse o Momentum quando compri il tier I. Ognuno mantiene il grado di incantamento del propulsore che consuma, e i suoi bonus vengono generati di nuovo ([Potenziamenti dei moduli](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). I propulsori non entrano in uno [slot abilità](/wiki/03-Mechanics/Abilities.md): vanno dentro i motori e i Nuclei adattivi.

### Seminare gli alieni {#outrunning-aliens}

Gli alieni volano a 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) e 230 (Crystalys). Una nave Ostirion con un Engine II e due propulsori vola a 221,4 con gli Impulse Thruster I: ancora sotto il Crystalys, quindi serve un propulsore creato in Assemblaggio per superarlo in velocità (230,8 con gli Impulse Thruster II, 240,3 con i III, 243,3 con i IV). I Momentum Thruster su questa nave volano alla stessa velocità o un po’ più in basso (221,4 con i Momentum Thruster I; poi 230,5, 238,4 e 240,7 con i II, i III e i IV): il tier I di entrambe le famiglie resta sotto un Crystalys, ogni tier creato in Assemblaggio sta sopra, il tier II di soli 0,8 e 0,5.
