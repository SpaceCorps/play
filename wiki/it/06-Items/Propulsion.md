<!-- wiki-i18n source: 969bfa836749a15e -->
<!-- wiki-i18n title: Propulsione -->
# Propulsione e velocità {#propulsion-speed}

I sistemi di propulsione determinano la velocità di movimento e la manovrabilità della tua nave.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Albero degli oggetti {#item-tree}

Ciò che crea l’Assemblaggio richiede prima la sua tecnologia; passa il puntatore su un oggetto per vedere quanto tempo serve a ricercarla. L’albero delle tecnologie, il carburante e il boost: [Ricerca](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | buy 2000 Thulium | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I -> Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Motori {#engines}

I motori sono la fonte principale di spinta della tua nave. Un motore in uno **slot abilità** ti dà invece l’**Afterburner** indicato nella colonna Effetto speciale, uno scatto di velocità di dieci secondi (più lungo con più motori), e non aggiunge spinta propria (vedi [Abilità](/wiki/03-Mechanics/Abilities.md)).

| Nome | Rarità | Velocità base | Bonus velocità % | Bonus scudo % | Slot | Effetto speciale | Costo |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Scadente | +2 | +2% | -2% | 1 | Afterburner I | 20.000 crediti |
| **Engine II** | Comune | +4 | +4% | -8% | 2 | Afterburner II | 2.000 Thulium |
| **Engine III** | Raro | +6 | +5% | -15% | 3 | Afterburner III | Solo da creare |

L’**Engine III** si crea in [Assemblaggio](/wiki/06-Items/Overview.md#upgrading-modules) da un Engine II, con 2.000 Thulium, 60 Ship Fragment, 3 Power Core e 6 Velkonite Reinforced Plate dal tuo Skylab. Mantiene il grado di incantamento del motore che consuma, e i suoi bonus vengono generati di nuovo ([Potenziamenti dei moduli](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Togli prima l’Engine II dalla tua nave (e togli da esso i suoi propulsori): un motore montato sulla nave o che contiene propulsori non viene consumato.

Il Bonus scudo dei motori è nei dati dell’oggetto, ma il gioco non lo ha mai applicato: i motori non indeboliscono i tuoi scudi, e le schede degli oggetti lo omettono.

---

## Propulsori {#thrusters}

I propulsori si inseriscono dentro i motori o i Nuclei adattivi per aumentarne la resa in velocità. Ci sono due famiglie di quattro tier ciascuna: gli **Impulse Thruster** danno più velocità fissa e moltiplicano un po’ la velocità del motore in cui sono montati, i **Momentum Thruster** meno velocità fissa, ma la moltiplicano di più. Un motore (o Nucleo adattivo) con dei propulsori produce **la propria velocità base più i bonus di velocità fissi dei propulsori, il tutto per i moltiplicatori di velocità dei propulsori moltiplicati tra loro** ([come si calcola la velocità](/wiki/03-Mechanics/Speed.md)): un Engine III con tre Momentum Thruster IV produce (6 + 3 x 12) x 1,11 x 1,11 x 1,11 = 57,4, con tre Impulse Thruster IV (6 + 3 x 17) x 1,02 x 1,02 x 1,02 = 60,5, e un Adaptive Core II con due Impulse Thruster IV ne produce (0 + 2 x 17) x 1,02 x 1,02 = 35,4 (29,6 con due Momentum Thruster IV).

| Nome | Rarità | Bonus velocità fisso | Molt. velocità | Costo |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Scadente | +5 | 1,02x | 20.000 crediti |
| **Impulse Thruster II** | Comune | +10 | 1,02x | Solo da creare |
| **Impulse Thruster III** | Raro | +15 | 1,03x | Solo da creare |
| **Impulse Thruster IV** | Epico | +17 | 1,02x | Solo da creare |
| **Momentum Thruster I** | Scadente | +4 | 1,06x | 20.000 crediti |
| **Momentum Thruster II** | Comune | +8 | 1,07x | Solo da creare |
| **Momentum Thruster III** | Raro | +11 | 1,09x | Solo da creare |
| **Momentum Thruster IV** | Epico | +12 | 1,11x | Solo da creare |

A ogni tier un Impulse Thruster produce di più del Momentum Thruster dello stesso tier, in un Nucleo adattivo come in un motore con uno, due o tre propulsori (60,5 contro 57,4 con tre propulsori di tier IV in un Engine III, e tre Impulse Thruster IV sono il meglio che un Engine III possa dare). Ciò che un Momentum Thruster ha in più è un secondo bonus (sotto).

Il bonus al moltiplicatore di velocità di un propulsore, della [Forgia](/wiki/06-Items/Forge.md), fa crescere la parte sopra 1 (un bonus di +15% su 1,11x dà 1,1265x), e la Forgia non genera alcun bonus su un moltiplicatore di 1,05x o inferiore: sull’1,02x o sull’1,03x di un Impulse Thruster varrebbe un millesimo. Un Impulse Thruster contiene un bonus (la sua velocità fissa), un Momentum Thruster due.

Il tier I di ogni famiglia si compra a 20.000 crediti. I tier da II a IV si creano in [Assemblaggio](/wiki/06-Items/Overview.md#upgrading-modules), ciascuno dal propulsore della stessa famiglia un tier più in basso (un Impulse Thruster II da un Impulse Thruster I, un III da un II, un IV da un III), con Thulium, drop e Velkonite Reinforced Plate dal tuo Skylab (2, 4 e 6 piastre). Un propulsore non cambia mai famiglia: scegli Impulse o Momentum quando compri il tier I. Ognuno mantiene il grado di incantamento del propulsore che consuma, e i suoi bonus vengono generati di nuovo ([Potenziamenti dei moduli](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). I propulsori non entrano in uno [slot abilità](/wiki/03-Mechanics/Abilities.md): vanno dentro i motori e i Nuclei adattivi.

### Seminare gli alieni {#outrunning-aliens}

Gli alieni volano a 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) e 230 (Crystalys). Una nave Ostirion con un Engine II e due propulsori vola a 223,1 con gli Impulse Thruster I: ancora sotto il Crystalys, quindi serve un propulsore creato in Assemblaggio per superarlo in velocità (234,0 con gli Impulse Thruster II, 245,5 con i III, 249,1 con i IV). I Momentum Thruster su questa nave volano un po’ più in basso (222,0 con i Momentum Thruster I; 231,8, 240,1 e 243,9 con i II, i III e i IV): il tier I di entrambe le famiglie resta sotto un Crystalys, ogni tier creato in Assemblaggio sta sopra.
