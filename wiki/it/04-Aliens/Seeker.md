<!-- wiki-i18n source: d1f973df95aefca8 -->
<!-- wiki-i18n title: Seeker -->
# Seeker {#seeker}

I Seeker sono unità base di esplorazione e ricognizione. Sono passivi, cioè non iniziano mai uno scontro: un Seeker si rivolta contro il pilota che gli spara, e solo contro quel pilota. Smette di inseguire se nessuno lo colpisce da 10 secondi, e il suo scafo si ripara una volta lasciato in pace per 30 secondi. Il Boss Seeker e i Seeker Slave dello [Sciame Seeker](/wiki/05-Swarms/Seeker-Swarm.md) somigliano ai Seeker ma sono specie a sé: i loro abbattimenti sono contati con il loro nome, non come abbattimenti di Seeker.

## Statistiche {#stats}

- **Punti scafo (HP)**: 800
- **Scudo**: 800
- **Danno**: 180
- **Velocità**: 120
- **Portata d’attacco**: 600
- **Comportamento**: Passivo

## Comportamento {#behavior}

- Un Seeker non va mai all’attacco di una nave che si avvicina: vaga finché qualcuno non gli spara, poi insegue e fa fuoco sul primo pilota che gli ha sparato, finché quel pilota continua a colpirlo e il Seeker può ancora raggiungerlo; nel frattempo i colpi degli altri piloti non gli fanno cambiare bersaglio, e quando il primo esce di scena passa al pilota successivo che si è unito allo scontro (vedi [Contro chi combatte un alieno](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)). Il fuoco di un altro alieno e un colpo che non fa danno non lo provocano mai.
- Rinuncia **10 secondi** dopo l’ultimo colpo subito da chiunque, e riprende a vagare. Finché un pilota continua a colpirlo, gli vola contro ogni volta che il pilota è oltre la portata delle sue armi (600 unità) e fa fuoco non appena è a portata.
- Lascia andare un pilota che si trova a più di **2.500 unità** da lui, o quando ha volato per **3.000 unità** dal punto in cui è iniziato l’inseguimento, e non gli dà di nuovo la caccia per 8 secondi a meno che il pilota non gli spari ancora una volta (vedi [Combattimento](/wiki/03-Mechanics/Combat.md)).
- Lasciato in pace per **30 secondi**, il suo scafo si ripara del 2% del massimo al secondo (uno scafo pieno in circa 50 secondi). Lo scudo si ricarica come quello di qualsiasi alieno, a partire da 15 secondi dopo l’ultimo colpo.
- Non combatte contro nessuno da cui non sia stato colpito, e non chiama mai un altro alieno in aiuto.
- I [piloti di corporazione](/wiki/03-Mechanics/Company-Pilots.md) danno la caccia ai Seeker. Un pilota che ne colpisce uno attira il suo fuoco, a meno che non stia già combattendo contro qualcun altro.

## Ricompense {#rewards}

- **Crediti**: 800
- **Thulium**: 4
- **Esperienza (XP)**: 100
- **Onore**: 2
- **Punti PvE per abbattimento**: 1
- **Ricarica scudo**: 10 al secondo (dopo 15 s)

## Bottino {#loot-drops}

Il bottino cade come [cassa di carico](/wiki/03-Mechanics/Cargo.md) nel punto in cui esplode, riservata per 30 secondi a chi l’ha abbattuto.

A cosa serve ogni oggetto del bottino e dove altro trovarlo: [Risorse](/wiki/06-Items/Resources.md).

- **Ship Fragment**: 20% di probabilità (min. 1, max. 1)
- **Daraxium**: 50% di probabilità (min. 1, max. 2)

## Storia {#lore}

I Seeker sono sonde di esplorazione leggere, schierate dallo Sciame alieno per mappare le porte di salto dei settori e rintracciare le firme elettromagnetiche delle flotte umane. Dotati di armamento minimo e strutture fragili, sono estremamente passivi: si ritirano o ignorano le navi a meno che non vengano attaccati. Tuttavia si coordinano con le unità da combattimento più grandi e segnalano la propria posizione se vengono ingaggiati.
