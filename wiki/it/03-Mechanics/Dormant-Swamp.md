<!-- wiki-i18n source: ee049111031a8060 -->
<!-- wiki-i18n title: Dormant Swamp -->
# Dormant Swamp

<!-- wiki-search: swamp; dormant swamp; base; turret; turrets; nike turret; laser turret; inert mass; unwakened; the unwakened; slumbering void; void; dormant lance; ds-4; palude; torretta; torrette; cannone; cannoni -->

Molto tempo fa, al centro della galassia viveva una civiltà avanzata. Costruiva in cristallo nero-viola, con venature violette che brillano, e per un motivo che nessuno conosce è crollata. Il **Dormant Swamp** è il suo avamposto, nell’angolo in alto a sinistra di `DS-4`. Dal giorno 11 della stagione si agita: cannoni al centro sparano a ogni nave che vedono, le **Inert Mass** lo custodiscono, e proprio al centro dorme **l’Unwakened**. È un luogo che i piloti **non sono ancora tenuti a visitare**. Sotto occultamento puoi volare fino all’Unwakened, e per ora lì non si può fare altro: la base e i suoi cannoni non possono essere danneggiati, né si può entrarvi, abbordarli o commerciare con loro.

La palude è anche il luogo in cui compare lo [Sciame Dormant](/wiki/05-Swarms/Dormant-Swarm.md) dal giorno 11, e gli **Slumbering Void** pattugliano intorno. Gli stessi Void arrivano a ondate agli [escavatori giganti](/wiki/03-Mechanics/Giant-Excavator.md#the-slumbering-voids). I settori sono in [Settori pericolosi](/wiki/01-General/Danger-Sectors.md).

![Flying in towards the Dormant Swamp: the amber notice ring and, inside it, the red ring of the zone the guns reach](../../img/wiki-img/shots/swamp-rings.jpg)

## In breve {#at-a-glance}

<!-- swamp-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Dove**: L’angolo in alto a sinistra di `DS-4`: il centro è in 5.000 / 5.000
- **Compare**: Dal giorno 11 della stagione fino al reset
- **La zona**: 4.300 unità intorno al centro: fin dove arrivano al massimo i cannoni, e il luogo che nessuno è ancora tenuto a visitare
- **L’avviso**: Una nave che attraversa l’anello a 4.800 unità dal centro riceve una riga di Sistema
- **Occultamento**: Nessun cannone vede mai una nave occultata, né una dentro la finestra di un EMP
- **Gli alieni**: 5 Inert Mass restano entro 2.400 unità dal centro. L’Unwakened dorme al centro. 2 Slumbering Void pattugliano tra 4.600 e 6.500 unità dal centro.
- **Lo Sciame Dormant**: Compare in 9.417 / 6.606, a 4.700 unità dal centro e fuori dalla zona
- **Rocce**: Nessun asteroide si trova entro 4.900 unità dal centro

<!-- swamp-glance:end -->

## I cannoni {#the-guns}

Le torrette della palude sparano alla **nave più vicina che riescono a vedere** entro la loro portata, e a nessun’altra: la zona è il cerchio che raggiunge la più lontana di esse. Non sono entità di alcun genere: non hanno punti vita, non si possono bersagliare, e niente di ciò che spari loro ha effetto. I loro colpi sono reali, e il mondo ne scala il danno come scala l’arma di qualsiasi alieno.

<!-- swamp-guns:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Danno di un colpo, in ogni mondo:

| Cannone | Posizione | Spara ogni | Portata (unità) | Alpha | Beta | Gamma |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| Torretta [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | 5.000 / 4.400 | 2 s | 3.640 | 75.000 | 112.500 | 150.000 |
| Torretta [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | 5.000 / 4.400 | 5 s | 1.080 | 50.000 | 75.000 | 100.000 |
| Torretta laser × 2 | 3.600 / 5.200; 6.400 / 5.200 | 1 s | 2.500 | 45.000–55.000 | 67.500–82.500 | 90.000–110.000 |

- Un razzo viene lanciato a 90% della sua portata, perché arrivi; una torretta laser spara una volta al secondo, e il suo danno viene tirato nell’intervallo indicato.
- Un N.I.K.E. ha una penetrazione dello scudo pari a 35%, che viene tolta dall’assorbimento di uno scudo.
- Un N.U.K.E. esplode su un raggio di 900 unità, con più forza al centro.

<!-- swamp-guns:end -->

- **Niente arriva fuori dalla zona,** e dentro una nave viene distrutta in pochi secondi: più si avvicina al centro, più cannoni si aggiungono, e nemmeno la Wraith meglio protetta regge.
- **L’occultamento ti fa entrare.** Nessuna torretta vede mai una nave occultata, né una dentro la finestra di un EMP, a nessuna distanza. Un’esplosione diretta a una nave visibile che scoppia vicino a una occultata la danneggia comunque e ne pone fine all’occultamento.
- **Sparano solo ai piloti,** mai agli alieni, ai piloti di corporazione o allo sciame, e la protezione di una nave appena tornata da una distruzione vale anche contro di loro.
- **L’anello di avviso.** Una nave che attraversa l’anello fuori dalla zona riceve una riga di Sistema: le torrette sparano a ogni nave che vedono, e qualcosa dorme al centro. Viene avvisata di nuovo solo dopo aver lasciato l’anello ed esserci tornata.
- **Uscirne.** Se vieni distrutto lì e torni sul posto, oppure accedi dentro la zona, vieni messo fuori. Una rotta che clicchi viene piegata intorno alla zona, e un avviso ti segnala quando il punto cliccato cade all’interno.

## Gli alieni {#the-aliens}

Qui vivono tre alieni della civiltà perduta, ciascuno con i suoi numeri. Vengono pagati come il boss di uno sciame: **in base al danno inflitto**, a ogni pilota che ne ha fatto almeno la quota indicata in [Sciami](/wiki/05-Swarms/Swarms.md#the-rules-of-every-swarm), e la cassa va al pilota che ha inflitto più danno. I loro abbattimenti si sommano ai tuoi punti PvE di grado come quelli di una nave di sciame, in proporzione alla ricompensa ([Gradi](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points)). Lo scudo di ciascuno assorbe l’80% di ogni colpo finché regge ([Scudi](/wiki/03-Mechanics/Shields.md)).

- **Slumbering Void.** Il cacciatore snello, l’alieno più veloce del gioco (veloce come una Storm con Afterburner III). Alcuni pattugliano sempre i dintorni della palude, e altri arrivano a ondate agli escavatori. È aggressivo, dà la caccia al pilota più vicino che riesce a vedere e non vede mai una nave occultata.
- **Inert Mass.** Un relitto morto con crepe viola, grande come una piccola stazione. Restano entro una distanza fissa dal centro della palude e per ora non lo lasciano. Lancia **Dormant Lance**: razzi guidati con una portata lunghissima che seguono una nave finché non si occulta, non apre una finestra EMP, non entra in un anello sicuro, non salta o non muore. È più veloce di qualsiasi nave, quindi servono solo queste interruzioni. Un asteroide sulla traiettoria di una Dormant Lance la ferma, e la Lance lo danneggia con il proprio danno (nessuno viene pagato per questo): una roccia ripara da una Inert Mass quindi solo per pochi colpi.
- **L’Unwakened.** Un monolite che dorme al centro della palude, la cosa più grande di qualsiasi mappa, così lento da non raggiungere mai una nave. Non lancia nulla, ma ogni nave dentro la sua aura brucia, **occultata o no**. È **immune**: colpi e razzi lo raggiungono e non fanno nulla, la finestra del bersaglio mostra le barre piene e la parola Immune. Un evento successivo permetterà di combatterlo; le sue ricompense qui sotto sono scritte e non si possono ancora ottenere.

<!-- swamp-members:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

### Slumbering Void

2 Slumbering Void pattugliano tra 4.600 e 6.500 unità dal centro della palude; uno distrutto ritorna dopo 1 h. Le ondate di un escavatore portano altri dello stesso alieno.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | 25.000 | 37.500 | 50.000 |
| Scudo | 150.000 | 225.000 | 300.000 |
| Assorbimento dello scudo | 80% | 80% | 80% |
| Danno dei laser (una raffica al secondo) | 3.000 | 4.500 | 6.000 |
| Velocità | 400 | 400 | 400 |
| Portata dei laser | 800 | 800 | 800 |
| Raggio di aggressione | 2.500 | 2.500 | 2.500 |
| Crediti | 23.000 | 46.000 | 69.000 |
| Thulium | 60 | 120 | 180 |
| Esperienza (XP) | 3.600 | 7.200 | 10.800 |
| Onore | 16 | 32 | 48 |
| Punti PvE per abbattimento | 10 | 10 | 10 |

**Bottino**: una cassa, per il pilota che ha inflitto più danno.

| Oggetto | Probabilità | Quantità |
| :--- | ---: | ---: |
| Uno tra Ultra Core e Experimental Fusion Core, scelto a caso | 60% | 30–60 |
| Uno dei 4 [razzi](/wiki/06-Items/Rockets.md) Epici, scelto a caso | 40% | 1–3 |

### Inert Mass

5 Inert Mass stanno entro 2.400 unità dal centro; una distrutta ritorna dopo 1 h. Lancia ogni 6 s una [Dormant Lance](/wiki/06-Items/Rockets.md#the-craft-only-rockets) guidata contro la nave più vicina che vede: velocità 750, un volo di 5.250 unità, penetrazione 40%.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | 250.000 | 375.000 | 500.000 |
| Scudo | 100.000 | 150.000 | 200.000 |
| Assorbimento dello scudo | 80% | 80% | 80% |
| Danno di ogni Dormant Lance | 5.000–8.000 | 7.500–12.000 | 10.000–16.000 |
| Velocità | 60 | 60 | 60 |
| Portata dei razzi | 5.000 | 5.000 | 5.000 |
| Raggio di aggressione | 5.000 | 5.000 | 5.000 |
| Crediti | 125.000 | 250.000 | 375.000 |
| Thulium | 335 | 670 | 1.005 |
| Esperienza (XP) | 20.200 | 40.400 | 60.600 |
| Onore | 88 | 176 | 264 |
| Punti PvE per abbattimento | 15 | 15 | 15 |

**Bottino**: una cassa, per il pilota che ha inflitto più danno.

| Oggetto | Probabilità | Quantità |
| :--- | ---: | ---: |
| Ultra Core e Experimental Fusion Core, divisi in parti uguali | 100% | 400–800 in tutto |
| Uno dei 4 [razzi](/wiki/06-Items/Rockets.md) Epici, scelto a caso | 100% | 20–40 |
| N.I.K.E. | 5% | 1–2 |
| Dark Matter | 5% | 1–3 |
| Ancient Control Unit | 10% | 1 |
| Power Core | 25% | 1–2 |

### The Unwakened

Ce n’è uno, al centro della palude e in nessun altro luogo; ritorna dopo 24 h dalla sua distruzione. È **immune** finché una missione successiva non spegne il flag: colpi e razzi lo raggiungono e non fanno nulla. Le sue ricompense sono scritte e non si possono ancora ottenere.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Scafo | 10.000.000 | 15.000.000 | 20.000.000 |
| Scudo | 10.000.000 | 15.000.000 | 20.000.000 |
| Assorbimento dello scudo | 80% | 80% | 80% |
| Danno dell’aura al secondo, a ogni nave all’interno | 75.000 | 112.500 | 150.000 |
| Raggio dell’aura | 700 | 700 | 700 |
| Velocità | 10 | 10 | 10 |
| Raggio di aggressione | 3.000 | 3.000 | 3.000 |
| Crediti | 7.500.000 | 15.000.000 | 22.500.000 |
| Thulium | 20.000 | 40.000 | 60.000 |
| Esperienza (XP) | 1.200.000 | 2.400.000 | 3.600.000 |
| Onore | 5.200 | 10.400 | 15.600 |
| Punti PvE per abbattimento | 112 | 112 | 112 |

**Bottino**: una cassa, per il pilota che ha inflitto più danno.

| Oggetto | Probabilità | Quantità |
| :--- | ---: | ---: |
| Ultra Core e Experimental Fusion Core, divisi in parti uguali | 100% | 10.000–15.000 in tutto |
| Uno dei 4 [razzi](/wiki/06-Items/Rockets.md) Epici, scelto a caso | 100% | 500–800 |
| N.I.K.E. | 100% | 20–30 |
| N.U.K.E. | 100% | 5–10 |
| Dark Matter | 100% | 40–60 |
| Ancient Control Unit | 100% | 10–20 |
| Power Core | 100% | 100–200 |

<!-- swamp-members:end -->

## Cosa fare qui {#what-to-do-here}

- **Guarda, non toccare.** La palude è per più tardi. L’unica cosa che raggiungi senza occultamento è fuori dalla zona: i Void di pattuglia, in un anello intorno alla zona, sono la prima linea della palude e il luogo in cui un gruppo può combattere senza i cannoni.
- **Combatti i Void con la penetrazione.** Il grande scudo di un Void assorbe l’80% di un colpo e conta quasi nulla: lo scafo dietro è piccolo. Più penetrazione dello scudo hanno i tuoi laser, prima cade ([Laser e munizioni](/wiki/06-Items/Lasers.md)).
- **Stai lontano dalle Lance.** Un’Inert Mass vede lontano e a una Lance non si sfugge: spezza la sua presa con un occultamento, un EMP, un anello sicuro o un salto, oppure esci dalla sua portata. Una Mass è un combattimento lungo anche per un grande gruppo delle navi più forti.
- **Lo Sciame Dormant** compare ora appena fuori dalla zona, così un gruppo può aspettarlo senza i cannoni. Vedi [Sciame Dormant](/wiki/05-Swarms/Dormant-Swarm.md).

## Dove leggere ancora {#where-to-read-more}

- [Settori pericolosi](/wiki/01-General/Danger-Sectors.md): cosa è cambiato al giorno 11.
- [Escavatore gigante](/wiki/03-Mechanics/Giant-Excavator.md): le ondate di Slumbering Void e ciò che custodiscono.
- [Sciami](/wiki/05-Swarms/Swarms.md) e [Sciame Dormant](/wiki/05-Swarms/Dormant-Swarm.md): come paga l’abbattimento di un boss.
- [Razzi](/wiki/06-Items/Rockets.md#the-craft-only-rockets): il N.I.K.E. e il N.U.K.E. che la torretta spara.
- [Buco nero](/wiki/03-Mechanics/Black-Hole.md): l’altro pericolo di `DS-4`.
- [Casse di carico](/wiki/03-Mechanics/Cargo.md): le casse che lasciano gli alieni.
