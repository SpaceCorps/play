<!-- wiki-i18n source: fe17f46644fd6072 -->
<!-- wiki-i18n title: Propulsione -->
# Propulsione e velocità {#propulsion-speed}

I sistemi di propulsione determinano la velocità di movimento e la manovrabilità della tua nave.

## In un minuto {#in-one-minute}

- **I motori producono velocità, i propulsori ci stanno dentro e la aumentano.** Un motore ospita da uno a tre propulsori (un Engine I uno, un Engine II due, un Engine III tre), e lo stesso vale per un Nucleo adattivo (il suo tier dice quanti).
- **Due famiglie di quattro tier ciascuna.** Gli Impulse Thruster danno più velocità fissa. I Momentum Thruster danno meno velocità fissa e moltiplicano di più la velocità. In entrambe le famiglie ogni tier è migliore di quello sotto, in entrambi i valori.
- **Quale dove.** Come regola, metti i Momentum in un Engine III pieno (tre propulsori) e gli Impulse in un Nucleo adattivo; nei motori più piccoli i due sono vicini ai tier I e II e dal tier III in poi l’Impulse è avanti. [La tabella qui sotto](#which-thruster-where) ha i numeri. L’Engine III più veloce contiene tre Momentum Thruster IV e fa 63,3.
- **Come ottenerli.** Il tier I di ogni famiglia costa 20.000 crediti. I tier da II a IV si creano nell’Assemblaggio, ciascuno da quello sotto, e un propulsore non cambia mai famiglia.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Albero degli oggetti {#item-tree}

Ciò che crea l’Assemblaggio richiede prima la sua tecnologia; passa il puntatore su un oggetto per vedere quanto tempo serve a ricercarla. L’albero delle tecnologie, il carburante e il boost: [Ricerca](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Engine I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 4000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 2000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 60 Ship Fragment, 1 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 80 Ship Fragment, 4 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 3000 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 80 Ship Fragment, 4 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 4000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 4000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 4 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I => Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Motori {#engines}

I motori sono la fonte principale di spinta della tua nave. Un motore in uno **slot abilità** ti dà invece l’**Afterburner** indicato nella colonna Effetto speciale, uno scatto di velocità di quindici secondi (più lungo con più motori), e non aggiunge spinta propria (vedi [Abilità](/wiki/03-Mechanics/Abilities.md)).

| Nome | Rarità | Velocità base | Bonus velocità % | Bonus scudo % | Slot | Effetto speciale | Costo |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Scadente | +5 | +2% | -2% | 1 | Afterburner I | 20.000 crediti |
| **Engine II** | Comune | +10 | +3% | -8% | 2 | Afterburner II | Solo da creare |
| **Engine III** | Raro | +15 | +4% | -15% | 3 | Afterburner III | Solo da creare |

L’**Engine II** si crea in [Assemblaggio](/wiki/06-Items/Overview.md#upgrading-modules) da un Engine I, con 2.000 Thulium, 60 Ship Fragment, 1 Power Core e 4 Velkonite Reinforced Plate. L’**Engine III** si crea lì da un Engine II, con 4.000 Thulium, 110 Ship Fragment, 5 Power Core, 1 Ancient Control Unit e 4 Dark Matter Plate ([Dark Matter e Dark Matter Plate](/wiki/03-Mechanics/Dark-Matter.md)). Ciascuno mantiene il grado di incantamento e i bonus del motore che consuma ([Potenziamenti dei moduli](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Togli prima dalla tua nave il motore da consumare (e togli da esso i suoi propulsori): un motore montato sulla nave o che contiene propulsori non viene consumato.

Il Bonus scudo dei motori è nei dati dell’oggetto, ma il gioco non lo ha mai applicato: i motori non indeboliscono i tuoi scudi, e le schede degli oggetti lo omettono.

---

## Propulsori {#thrusters}

I propulsori si inseriscono dentro i motori o i Nuclei adattivi per aumentarne la resa in velocità. Ci sono due famiglie di quattro tier ciascuna: gli **Impulse Thruster** danno più velocità fissa e moltiplicano un po’ la velocità del motore in cui sono montati, i **Momentum Thruster** meno velocità fissa, ma la moltiplicano di più. In entrambe le famiglie ogni tier è migliore di quello sotto, sia nella velocità fissa sia nel moltiplicatore. Un motore (o Nucleo adattivo) con dei propulsori produce **la propria velocità base più i bonus di velocità fissi dei propulsori, il tutto per i moltiplicatori di velocità dei propulsori moltiplicati tra loro** ([come si calcola la velocità](/wiki/03-Mechanics/Speed.md)): un Engine III con tre Momentum Thruster IV produce (15 + 3 x 11,135) x 1,0935 x 1,0935 x 1,0935 = 63,3, con tre Impulse Thruster IV (15 + 3 x 14,025) x 1,02975 x 1,02975 x 1,02975 = 62,3, e un Adaptive Core II con due Impulse Thruster IV ne produce (0 + 2 x 14,025) x 1,02975 x 1,02975 = 29,7 (26,6 con due Momentum Thruster IV).

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

L’Impulse dà più velocità fissa, il Momentum moltiplica di più, quindi quale sia più veloce dipende da ciò che il motore produce già. La velocità fissa conta di più dove c’è poca velocità da moltiplicare: in un Nucleo adattivo (non ha velocità propria) e in un motore con uno o due propulsori. Un moltiplicatore conta di più in un Engine III pieno, dove c’è molta velocità da moltiplicare, e lì i Momentum Thruster vincono a ogni tier. La velocità che ciascuno produce con propulsori di tier IV in tutti gli slot:

| Dove stanno i propulsori | Con Impulse Thruster IV | Con Momentum Thruster IV | Più veloce |
| :--- | :---: | :---: | :--- |
| Engine I, 1 propulsore | 19,6 | 17,6 | Impulse |
| Engine II, 2 propulsori | 40,3 | 38,6 | Impulse |
| Engine III, 1 propulsore | 29,9 | 28,6 | Impulse |
| Engine III, 2 propulsori | 45,6 | 44,6 | Impulse |
| Engine III, 3 propulsori | 62,3 | 63,3 | Momentum |
| Adaptive Core II, 2 propulsori | 29,7 | 26,6 | Impulse |

- **Tier più bassi.** Dal tier III in poi l’Impulse è avanti ovunque tranne che nell’Engine III pieno, di 0,6–3,1. Ai tier I e II le due famiglie distano meno di un punto fuori dall’Engine III pieno: l’Impulse è avanti in un Engine I e in un Adaptive Core I o II; il Momentum è avanti o pari in un Engine III con uno o due propulsori e in un Engine II con due. L’eccezione è l’Engine III pieno: lì il Momentum è avanti a ogni tier, di 1,0–2,0.
- **L’Engine III più veloce.** Contiene tre Momentum Thruster IV: 63,3, un po’ sopra un Impulse e due Momentum Thruster IV (63,2) o tre Impulse (62,3).

Il bonus al moltiplicatore di velocità di un propulsore, della [Forgia](/wiki/06-Items/Forge.md), fa crescere la parte sopra 1 (un bonus di +15% su 1,0935x dà 1,1075x), e la Forgia non genera alcun bonus su un moltiplicatore di 1,05x o inferiore: sull’1,017x–1,02975x di un Impulse Thruster aggiungerebbe meno di 0,005 (+15% su 1,02975x dà 1,034x). Un Impulse Thruster contiene un bonus (la sua velocità fissa), un Momentum Thruster due.

Il tier I di ogni famiglia si compra a 20.000 crediti. I tier da II a IV si creano in [Assemblaggio](/wiki/06-Items/Overview.md#upgrading-modules), ciascuno dal propulsore della stessa famiglia un tier più in basso (un Impulse Thruster II da un Impulse Thruster I, un III da un II, un IV da un III), con Thulium, drop e piastre: 4 Velkonite Reinforced Plate dal tuo Skylab per il tier II o III, e 4 Dark Matter Plate e una Ancient Control Unit per il tier IV. Un propulsore non cambia mai famiglia: scegli Impulse o Momentum quando compri il tier I. Ognuno mantiene il grado di incantamento e i bonus del propulsore che consuma ([Potenziamenti dei moduli](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). I propulsori non entrano in uno [slot abilità](/wiki/03-Mechanics/Abilities.md): vanno dentro i motori e i Nuclei adattivi.

### Seminare gli alieni {#outrunning-aliens}

Gli alieni volano a 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) e 230 (Crystalys). Una nave Ostirion (velocità base 220) con un Engine II e due propulsori vola a 246,3 con gli Impulse Thruster I, a 255,6 con i II, a 265,1 con i III e a 268,2 con i IV: ogni tier supera in velocità il Crystalys, anche gli Impulse Thruster I che si possono comprare. I Momentum Thruster su questa nave volano entro due punti da questi valori (246,7 con i Momentum Thruster I; poi 255,9, 263,9 e 266,3 con i II, i III e i IV): ogni tier di entrambe le famiglie sta sopra un Crystalys, di almeno 16,3.
