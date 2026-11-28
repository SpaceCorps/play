<!-- wiki-i18n source: 0a2447734a603004 -->
<!-- wiki-i18n title: Abilità speciali -->
# Abilità speciali {#special-abilities}

<!-- wiki-search: special ability; special abilities; ability; abilities; mob; mobs; regenerate; mending; shield burst; hardened plating; plating; enrage; call reinforcements; reinforcements; clones; decoy; flee and return; flee; life drain; nova pulse; nova; rocket barrage; barrage; veil; sow mines; mines; split; fragments; boss steps; ladder; three steps; warning; tell; surprise; warlord; warden; leader; abilità speciali; rigenerazione; scarica di scudo; corazza temprata; furia; richiesta di rinforzi; cloni; fuga e ritorno; drenaggio vitale; impulso nova; salva di razzi; velo; semina di mine -->

Alcuni alieni portano un’**abilità speciale**: una cosa che fanno una sola volta nella vita, quando il loro scafo è a metà. Rigenerarsi, una scarica di scudo, una fuga, una richiesta d’aiuto. Prima che cominci non si vede nulla, quindi ogni caccia può finire con una sorpresa. Questa pagina dice che cosa fa ciascuna abilità e come rispondervi. I boss funzionano diversamente: cambiano il modo di combattere in tre fasi man mano che il loro scafo cala, e i piccoli alieni dell’ultimo livello possono spezzarsi in frammenti se vengono distrutti troppo in fretta.

## Come funziona {#how-it-works}

<!-- mob-rules:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **Una volta.** Un alieno che porta un’abilità la usa una sola volta nella vita: quando, in uno scontro, il suo scafo (non il suo scudo) scende sotto 50% del massimo. Un colpo che lo distrugge da sopra quella linea non gli lascia mai sparare, e un alieno che non è in uno scontro aspetta che ne cominci uno.
- **Prima un avviso.** L’abilità comincia con un avviso: un anello che si chiude sulla nave e una parola sopra di essa. Un’abilità la cui scheda qui sotto dice che parte subito non ha avviso. L’alieno può ancora essere distrutto durante l’avviso; allora non succede nulla e paga come al solito. Le specie leggere (Seeker e Phantasm) sono più rapide: i loro avvisi e i loro effetti durano 50% del tempo normale.
- **Prima non si vede nulla.** Un alieno che porta un’abilità è uguale a qualunque altro, in ogni dettaglio, finché non comincia il suo avviso. Nulla nel gioco dice quale sia, nemmeno la [Guida del Viaggiatore](/wiki/03-Mechanics/Travelers-Guide.md).
- **Chi la porta.** Una piccola parte degli alieni dei settori delle compagnie e dei Danger Sectors: più forte il livello, più grande la parte, e i capi degli sciami (Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah e Boss Crystalys) hanno più probabilità degli altri di portarla. Gli alieni della Deep Void, dei dungeon dei clan e delle porte solo non la portano mai, né i seguaci di uno sciame, le ondate di un Guardiano, la Dormant Force o il Tesseract.
- **Paga quanto paga qualunque alieno.** Un alieno che usa un’abilità paga, lascia bottino e conta esattamente come uno che non la usa: l’abilità non aggiunge nulla all’abbattimento e gli toglie tempo. L’abbattimento resta al pilota che lo deteneva: finché l’alieno fugge, si rigenera o si nasconde, la rivendicazione non scade.
- **Le navi chiamate e le copie non sono abbattimenti.** Le navi che un alieno chiama e le copie che crea non pagano nulla, non lasciano nulla e non contano per nessuna missione, statistica o classifica. Al massimo 6 vivono per chi chiama e 24 su una mappa, e gli alieni propri della mappa tornano comunque in tempo.
- **Tutti sulla mappa lo vedono.** I piloti della mappa sono avvisati quando un’abilità comincia: il gioco disegna l’anello, la parola e l’effetto e riproduce un suono.

<!-- mob-rules:end -->

## Le dodici abilità {#the-twelve-abilities}

Un’abilità comincia con un **avviso**, a meno che la sua scheda dica che parte subito: un anello che si chiude sulla nave e una parola sopra di essa. I tempi e i numeri qui sotto valgono per le specie pesanti. Dove un numero ha più valori, sono quelli dei livelli nominati tra parentesi, la lettera greca davanti al nome di un alieno.

<!-- mob-abilities:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

### Rigenerazione {#regenerate}

Resta fermo e ripristina 15% / 20% / 25% / 30% (α / β / γ / δ) del suo scafo e del suo scudo in 6 s, senza sparare nel frattempo. Danni che sommati raggiungono 10% del suo scafo e del suo scudo insieme la interrompono, e tiene ciò che ha già ripristinato.

- **Avviso**: 1,5 s
- **La parola sopra la nave**: SI RIGENERA
- **La portano**: qualunque alieno
- **Risposta**: Sfondalo con razzi o con una folla di navi, oppure distruggilo durante l’avviso.

### Scarica di scudo {#shield-burst}

Un nuovo strato di scudo pari a 15% / 20% / 30% / 40% (α / β / γ / δ) del suo scafo massimo si aggiunge al suo scudo. Finché regge, assorbe ogni punto di un colpo; sparisce quando è esaurito o dopo 10 s.

- **Avviso**: 1 s
- **La parola sopra la nave**: SCUDO SU
- **La portano**: qualunque alieno
- **Risposta**: Munizioni e razzi che perforano gli scudi lo attraversano meglio. Oppure spara a un altro alieno finché non sparisce.

### Corazza temprata {#hardened-plating}

Per 7 s / 8 s / 10 s (β / γ / δ) subisce solo 50% di ogni colpo, scafo e scudo insieme: il doppio più resistente. Continua a combattere, e i numeri dei tuoi colpi diventano grigi.

- **Avviso**: 1,5 s
- **La parola sopra la nave**: CORAZZA
- **La portano**: le specie pesanti (Bulwark, Goombah e Crystalys) e i capi di sciame pesanti (Pirate Boss e Boss Phantasm), dal livello β
- **Risposta**: Aspetta che finisca, colpisci un altro alieno nel frattempo e tieni le tue raffiche per dopo.

### Furia {#enrage}

Per 10 s il suo danno è moltiplicato per ×1,3 / ×1,4 / ×1,5 / ×1,75 (α / β / γ / δ) e la sua velocità per ×1,25.

- **Avviso**: 1 s
- **La parola sopra la nave**: FURIOSO
- **La portano**: qualunque alieno
- **Risposta**: Tieni alto lo scudo, continua a muoverti e resta fuori dalla sua portata.

### Richiesta di rinforzi {#call-reinforcements}

4 / 6 (γ / δ) alieni più piccoli arrivano dal bordo più vicino della mappa, in 2 ondate distanziate di 3 s. La specie che arriva: Phantasm (chiamato da Bulwark e Goombah); Bulwark (chiamato da Crystalys). Insieme hanno 45% / 60% (γ / δ) del suo scafo e del suo scudo e sparano 50% della sua raffica. Non pagano nulla, non lasciano nulla e non contano per nulla, e se ne vanno dopo 45 s, o quando chi li ha chiamati viene distrutto.

- **Avviso**: 2 s
- **La parola sopra la nave**: CHIAMA
- **La portano**: le specie pesanti (Bulwark, Goombah e Crystalys) e i capi di sciame pesanti (Boss Phantasm e Boss Goombah), dal livello γ
- **Risposta**: Distruggi chi chiama: le sue navi se ne vanno con lui. Un’arma ad area le spazza via.

### Cloni {#clones}

3 (γ / δ) copie di lui compaiono attorno a lui, con il suo nome e il suo aspetto. Insieme hanno 18% (γ / δ) del suo scafo e del suo scudo; non sparano e non pagano nulla, e durano 15 s o finché quello vero non viene distrutto. Quello vero porta un anello sottile finché le copie sono fuori, e la finestra del bersaglio chiama una copia Esca.

- **Avviso**: 1 s
- **La parola sopra la nave**: CLONAZIONE
- **La portano**: qualunque alieno, dal livello γ
- **Risposta**: Segui l’anello e la barra dello scafo che si muove di quello vero, oppure usa un’arma ad area.

### Fuga e ritorno {#flee-and-return}

Vola via dai suoi attaccanti a velocità ×2 per 5 s / 6 s / 7 s / 8 s (α / β / γ / δ), poi si rivolta contro il primo pilota che l’ha colpito. Non lascia mai la mappa né entra in una zona sicura, può essere colpito tutto il tempo, e il pilota che deteneva il suo abbattimento lo conserva.

- **Avviso**: 0,5 s
- **La parola sopra la nave**: IN FUGA
- **La portano**: qualunque alieno
- **Risposta**: Inseguilo, oppure colpiscilo con i razzi mentre vola.

### Drenaggio vitale {#life-drain}

Per 10 s non spara altro: una volta al secondo drena ogni nave nella sua portata con una raffica completa che nulla schiva, e si cura di 75% / 100% / 100% (β / γ / δ) del danno che infligge, al massimo 20% del suo scafo in tutto.

- **Avviso**: 1 s
- **La parola sopra la nave**: ASSORBE
- **La portano**: le specie pesanti (Bulwark, Goombah e Crystalys) e i capi di sciame pesanti (Pirate Boss, Boss Phantasm, Boss Goombah e Boss Crystalys), dal livello β
- **Risposta**: Metti una roccia o un muro sulla linea, attiva la copertura o esci dalla sua portata.

### Impulso nova {#nova-pulse}

Un anello cresce a terra attorno a lui durante l’avviso. Quando l’anello è pieno, colpisce una volta ogni nave al suo interno, con 4 / 5 (γ / δ) delle sue raffiche. Il suo raggio, in unità, è 700 / 800 (γ / δ).

- **Avviso**: 2,5 s
- **La parola sopra la nave**: NOVA
- **La portano**: le specie pesanti (Bulwark, Goombah e Crystalys) e i capi di sciame pesanti (Pirate Boss, Boss Phantasm e Boss Goombah), dal livello γ
- **Risposta**: Esci dall’anello prima che si riempia: è l’unico impatto che puoi schivare.

### Salva di razzi {#rocket-barrage}

Per 3 s spara 4 / 6 / 8 (β / γ / δ) [razzi Rivet](/wiki/06-Items/Rockets.md#the-twelve-rockets) al suo bersaglio: Rivet I / II / II (β / γ / δ). Volano dritti e non sono guidati.

- **Avviso**: 1,5 s
- **La parola sopra la nave**: SALVA
- **La portano**: le specie pesanti (Bulwark, Goombah e Crystalys) e i capi di sciame pesanti (Boss Phantasm e Boss Goombah), dal livello β
- **Risposta**: Continua a muoverti: i razzi vanno dritti. Una roccia sulla traiettoria li ferma.

### Velo {#veil}

Per 6 s / 8 s (γ / δ) una nave a più di 700 unità da lui non può agganciarlo, e un aggancio che aveva si perde. Più vicino, si vede come sempre. Continua a combattere, e un’esplosione lo ferisce comunque.

- **Avviso**: nessuno, parte subito.
- **La parola sopra la nave**: SI VELA
- **La portano**: le specie pesanti (Bulwark, Goombah e Crystalys) e i capi di sciame pesanti (Pirate Boss, Boss Phantasm, Boss Goombah e Boss Crystalys), dal livello γ
- **Risposta**: Avvicinati a meno di 700 unità.

### Semina di mine {#sow-mines}

Posa 4 / 6 / 8 (β / γ / δ) mine su un anello di 500 unità attorno al punto in cui si trovava il suo bersaglio. Una mina si arma 3 s dopo l’atterraggio, dura 30 s ed esplode una volta, sotto la prima nave di pilota che le passa sopra, con 2 / 3 / 3 (β / γ / δ) delle raffiche dell’alieno. Una mina non ferisce mai un alieno.

- **Avviso**: 1,5 s
- **La parola sopra la nave**: SEMINA MINE
- **La portano**: le specie pesanti (Bulwark, Goombah e Crystalys) e i capi di sciame pesanti (Pirate Boss, Boss Phantasm, Boss Goombah e Boss Crystalys), dal livello β
- **Risposta**: Giraci intorno: sono disegnate a terra e si armano tardi.


<!-- mob-abilities:end -->

## Frammentazione {#splitting}

<!-- mob-split:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

I piccoli alieni dell’ultimo livello possono spezzarsi se vengono distrutti troppo in fretta. Riguarda Seeker, Phantasm, Bulwark, Goombah e Crystalys del livello δ e nessun altro alieno, e non è una delle abilità qui sopra: un alieno può avere entrambe.

- **Quando**: un pilota lo distrugge entro 5 s dal primo danno che ha subito. Non tutti gli alieni che muoiono così in fretta si spezzano.
- **Cosa ne esce**: 3 alieni della stessa specie e dello stesso livello, grandi 70% di lui, ciascuno con 25% del suo scafo e del suo scudo e una raffica completa, attorno al punto in cui è stato distrutto. Vanno contro il pilota che l’ha distrutto e se ne vanno dopo 180 s.
- **Sono alieni normali**: ciascuno paga quanto paga la sua specie, lascia ciò che lascia e conta per missioni e statistiche. Non portano alcuna abilità e non si spezzano mai.
- **Limiti**: al massimo 60 frammenti vivono su una mappa, e non trattengono gli alieni propri della mappa.
- **Cosa significa**: un equipaggio che distrugge i suoi alieni abbastanza in fretta può ricavare fino a 4 abbattimenti da un solo alieno. Un equipaggio che non ci riesce non ne ricava nulla.

<!-- mob-split:end -->

## Le tre fasi dei boss {#the-bosses-three-steps}

Ogni boss cambia il modo di combattere in tre fasi: quando lo scontro comincia, quando il suo scafo scende sotto i due terzi e quando scende sotto un terzo. Una fase avviene una volta sola e non torna mai indietro, a meno che il boss non ricominci, come detto sotto.

<!-- mob-ladders:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **Una pausa a ogni fase.** Quando dopo la prima comincia una fase che ha qualcosa da fare, il boss non può essere ferito per 1,5 s (3 s per il Signore della guerra del dungeon e per i boss delle porte solo).
- **Anche un’abilità speciale.** Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah e Boss Crystalys possono portare anche un’abilità speciale (Dormant Force e Tesseract mai): arriva tra la seconda e la terza fase; se le due dovessero cominciare insieme, la successiva aspetta al massimo 3 s. Non è mai un’abilità che le fasi del capo stesso usano.
- **Ricominciare.** Il Tesseract ricomincia le sue fasi appena si è riparato del tutto.

### I capi degli sciami {#the-swarm-leaders}

| Capo | All’inizio | Sotto i due terzi | Sotto un terzo |
| :--- | :--- | :--- | :--- |
| **Pirate Boss** | Spara un ventaglio di 3 razzi, distanziati di 12 gradi, contro il primo pilota che l’ha colpito. | Chiama 5 Pirate Scouts in più in una volta, al massimo 10 vivi. Non pagano nulla e se ne vanno dopo 45 s. | Vola a velocità ×1,8 verso la porta più vicina per 10 s, poi si rivolta contro i piloti. |
| **Boss Seeker** | I suoi Seeker Slaves lo riparano ×2 più in fretta per 8 s. | 2 copie di lui compaiono, e quello vero porta un anello. | Vola via dai piloti per 4 s, poi si rivolta. |
| **Boss Phantasm** | Ciascuno dei suoi Phantasm Guards alza uno strato di scudo pari a 10% del proprio scafo. | 3 copie di lui compaiono, e quello vero porta un anello. | Salta a circa 2.500 unità dai piloti, e i suoi Phantasm Guards tornano integri attorno a lui. |
| **Boss Goombah** | Subisce solo 50% di ogni colpo per 6 s. | Il suo danno è moltiplicato per ×1,5 e la sua velocità per ×1,25 per 10 s. | Ripristina 25% del suo scafo e del suo scudo (una raffica di danni la interrompe), e nel frattempo i suoi Goombah Guards lo riparano ×2 più in fretta. |
| **Boss Crystalys** | Subisce solo 50% di ogni colpo per 8 s. | Un anello di 700 unità colpisce ogni nave al suo interno con 4 delle sue raffiche, e spara 4 razzi. | Ripristina 20% del suo scafo e del suo scudo (una raffica di danni la interrompe), e arrivano 3 Crystalys Guards in più, al massimo 6 vivi. |
| **Dormant Force** | Subisce solo 70% di ogni colpo finché uno dei suoi Dormant Pulses è vivo. | I suoi Dormant Pulses sparano un razzo ogni 2,5 s per 15 s. | Finché tutti i suoi Dormant Pulses sono vivi, lo riparano di 5% del suo scafo al secondo per 6 s. |
| **Tesseract** | – | Arrivano 20 Facets in più in una volta, oltre il loro numero abituale. | – |

### I Guardiani dei clan {#the-clan-wardens}

| Guardiano | All’inizio | Sotto i due terzi | Sotto un terzo |
| :--- | :--- | :--- | :--- |
| **Brood Warden** (I, II, III) | Tutti i 4 droni vengono al suo fianco in una volta. | I suoi droni lo riparano ×1,5 più in fretta per 15 s. | Arrivano 2 droni in più, oltre il loro numero abituale, per 30 s. Non pagano nulla. |
| **Siege Warden** (I, II, III) | – | Spara il suo razzo ×2 più spesso per 20 s. | Ripristina 15% del suo scafo e del suo scudo (una raffica di danni la interrompe). |
| **Wrath Warden** (I, II, III) | – | I suoi laser colpiscono ×1,25 più forte. | I suoi laser colpiscono ×1,5 più forte in tutto, senza sommarsi alla fase prima. |

### Il Signore della guerra del dungeon {#the-dungeon-warlord}

- **Sotto i due terzi**: La pausa tra le sue abilità scende a 4 s e le loro attese a ×0,75.
- **Sotto un terzo**: La pausa scende a 2 s, le attese a ×0,5 e il suo danno sale a ×1,25; lancia una raffica di Meteor gratuita, e il suo Swarm non torna mai più in fretta di ogni 120 s.
- **Una pausa a ogni fase.** Quando comincia una fase, il Signore della guerra non può essere ferito per 3 s.

### I boss delle porte solo {#the-solo-gate-bosses}

Anche i sei boss delle porte solo hanno tre fasi: sono nella tabella [dei boss](/wiki/03-Mechanics/Solo-Gates.md#the-bosses) dell’articolo sulle porte solo.

<!-- mob-ladders:end -->

## Per saperne di più {#where-to-read-more}

- [Combattimento](/wiki/03-Mechanics/Combat.md#who-an-alien-fights): contro chi combatte un alieno e a chi va la sua distruzione.
- [Sciami](/wiki/05-Swarms/Swarms.md): i capi e le loro fasi, un articolo per ogni sciame.
- [Warden dei clan](/wiki/03-Mechanics/Clans.md#fighting-a-warden), il [Warlord del dungeon](/wiki/03-Mechanics/Dungeons.md#the-warlord) e i [boss delle porte solo](/wiki/03-Mechanics/Solo-Gates.md#the-bosses).
- [Guida del Viaggiatore](/wiki/03-Mechanics/Travelers-Guide.md): ciò che hai imparato su un alieno. Non dice mai quale porti un’abilità.
