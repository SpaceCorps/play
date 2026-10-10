<!-- wiki-i18n source: 13c9ac551cfd01fa -->
<!-- wiki-i18n title: Settori pericolosi -->
# Settori pericolosi {#danger-sectors}

<!-- wiki-search: ds; ds-1; ds-2; ds-3; ds-4; central pvp zone; pvp zone; pulsar; giant excavator; excavator; dormant swamp; swamp; event 2; tech surge; settore pericoloso; escavatore gigante; escavatore; palude; balzo tecnologico -->

I **settori pericolosi** sono i quattro settori al centro della galassia, da `DS-1` a `DS-4`. Qui si incontrano le tre corporazioni, e in ogni mondo i piloti possono combattere tra loro ([Viaggiare sulla mappa](/wiki/01-General/Spacemap%20Travel.md)). `DS-1`, `DS-2` e `DS-3` hanno ciascuno il portale di una corporazione; `DS-4` è il nucleo, con il [buco nero](/wiki/03-Mechanics/Black-Hole.md) al centro. In nessuno c’è una stazione: gli unici luoghi sicuri sono gli anelli intorno ai portali di salto.

Qui visse una civiltà dell’antica galassia, avanzata e nera-viola, e per un motivo che nessuno conosce è crollata. I suoi resti non sono mai stati del tutto morti: lo [Sciame Dormant](/wiki/05-Swarms/Dormant-Swarm.md) è stato il primo segno. Dal **giorno 11 della stagione**, l’inizio dell’evento 2 (**Balzo tecnologico**, vedi la [Cronologia del reset](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule)), se ne risveglia di più e i settori pericolosi cambiano. Ogni pilota del mondo ne viene avvisato il giorno in cui inizia, e ciò che è nuovo resta fino al reset.

![Flying in towards the Dormant Swamp: the amber notice ring and, inside it, the red ring of the zone the guns reach](../../img/wiki-img/shots/swamp-rings.jpg)

## Cosa c’è di nuovo dal giorno 11 {#what-is-new-from-day-11}

- **Escavatori giganti.** `DS-1`, `DS-2` e `DS-3` hanno ciascuno un pulsar dal primo giorno della stagione, una luce nel cielo e nient’altro; dal giorno 11 ciascuno riceve accanto un **escavatore gigante**. Metti Dark Matter nel serbatoio dell’escavatore, scegli una risorsa, e lui estrae il pulsar: Thulium e minerali rari cadono intorno a lui in casse che chiunque può prendere. È la cosa più ricca per cui combattere nei settori pericolosi, e la più pericolosa. Vedi [Escavatore gigante](/wiki/03-Mechanics/Giant-Excavator.md).
- **Slumbering Void.** Mentre un escavatore estrae, gli **Slumbering Void** arrivano a ondate dal bordo della mappa e danno la caccia ai piloti vicini. Altri pattugliano la palude. Vedi [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).
- **Il Dormant Swamp.** In un angolo di `DS-4` sorge la base della civiltà perduta: cannoni che sparano a ogni nave che vedono, Inert Mass che la custodiscono e, al centro, l’Unwakened. È un luogo che i piloti non sono ancora tenuti a visitare. Vedi [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md).
- **Uno Sciame Dormant più veloce e più ricco.** Lo sciame compare ora nella palude, ritorna prima dopo la distruzione e paga il doppio. Vedi [Sciame Dormant](/wiki/05-Swarms/Dormant-Swarm.md).
- **Prima del giorno 11** brillano solo i pulsar: per il resto i settori pericolosi sono come li descrive [Viaggiare sulla mappa](/wiki/01-General/Spacemap%20Travel.md). Un mondo al giorno 11 o dopo ha tutto in un colpo.

## Dove si trova ogni cosa {#where-everything-is}

Ogni mondo ha una copia tutta sua di ogni cosa, e un pulsar e il suo escavatore stanno nel terzo aperto del loro settore, lontano da ogni anello di portale, sul lato rivolto verso il centro della mappa. Le distanze sono in unità della mappa; i settori misurano 32.000 per 18.000 unità.

<!-- danger-sites:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

| Settore | Portale della corporazione | Pulsar | Escavatore gigante |
| :--- | :--- | :--- | :--- |
| `DS-1` | Mars | 8.000 / 5.000 | 8.805 / 5.402 |
| `DS-2` | Terra | 8.000 / 13.000 | 8.805 / 12.598 |
| `DS-3` | Galactic | 24.000 / 13.000 | 23.195 / 12.598 |

<!-- danger-sites:end -->

`DS-4` non ha un pulsar: lì c’è il buco nero. Il suo angolo contiene invece il Dormant Swamp; i numeri della palude sono in [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#at-a-glance).

<!-- danger-rules:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- I pulsar brillano dal primo giorno della stagione; tutto il resto di nuovo compare al giorno 11 della stagione e resta fino al reset.
- Ogni mondo ha i propri pulsar, escavatori e palude: quello che succede in uno non succede in un altro.
- Nessun asteroide si trova entro 2.600 unità da un pulsar, entro 2.200 unità da un escavatore gigante o entro 4.900 unità dal centro del Dormant Swamp.

<!-- danger-rules:end -->

## Come evitare guai {#keeping-out-of-trouble}

- **Radiazioni.** Un escavatore che si è surriscaldato o è stato distrutto, e il suo pulsar, bruciano ogni nave che resta dentro i loro cerchi ([Escavatore gigante](/wiki/03-Mechanics/Giant-Excavator.md#heat-and-radiation)). Il gioco ti avvisa prima, e i cerchi vengono disegnati a terra in volo e sulla minimappa.
- **I cannoni della palude.** Le torrette della palude sparano a una nave che possono vedere ben prima che questa veda qualcosa che valga il viaggio ([Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#the-guns)). Una rotta che clicchi viene piegata intorno ai cannoni e alle radiazioni, come intorno al buco nero, e un avviso ti segnala quando il punto cliccato cade all’interno.
- **Se vieni distrutto lì,** la scelta di tornare **sul posto** ti mette nel punto più vicino fuori dalle radiazioni e fuori dalla zona della palude, come per il buco nero ([Per iniziare](/wiki/01-General/Getting-Started.md#dying-and-coming-back)).
- **Un gruppo e una via di fuga.** Gli escavatori attirano i Void e i rivali allo stesso modo. Porta un [gruppo](/wiki/03-Mechanics/Groups.md), sappi qual è il portale più vicino e ricorda che nei settori pericolosi non puoi saltare via mentre vieni attaccato ([Saltare sotto attacco](/wiki/01-General/Spacemap%20Travel.md#jumping-under-fire)).
- **Il resto è PvP come sempre.** Niente qui è un posto sicuro: valgono le regole normali del tuo mondo, rivali compresi.

## Dove leggere ancora {#where-to-read-more}

- [Escavatore gigante](/wiki/03-Mechanics/Giant-Excavator.md): il pannello, il carburante, cosa estrae, i Void, il calore e le radiazioni.
- [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md): i cannoni, i tre alieni e la nuova casa dello sciame.
- [Sciame Dormant](/wiki/05-Swarms/Dormant-Swarm.md) e [Sciami](/wiki/05-Swarms/Swarms.md).
- [Il buco nero](/wiki/03-Mechanics/Black-Hole.md) e [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md): da dove viene il carburante.
- [Estrazione di asteroidi](/wiki/03-Mechanics/Asteroid-Mining.md): le rocce dei settori pericolosi.
