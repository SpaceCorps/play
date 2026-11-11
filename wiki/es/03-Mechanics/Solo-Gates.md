<!-- wiki-i18n source: 4d2749864875137f -->
<!-- wiki-i18n title: Puertas en solitario -->
# Puertas en solitario {#solo-gates}

<!-- wiki-search: solo gates; solo gate; gate; gates; galaxy gates; rift; rifts; alpha rift; beta breach; gamma foundry; delta siege; omega vault; chrono gate; chrono-gate; materializer; energy materializer; scan; spin; gate part; gate parts; guarantee; pity; consolation; wave; waves; nuke wave; skip; boss; lives; resume; abandon; speedrun; no death; challenge; achievement; thulium cap; puertas en solitario; puerta en solitario; puertas galácticas; pieza; piezas; materializador de energía; giro; garantía; oleada; oleadas; vidas; reanudar; abandonar; sin morir; desafío; logro; límite de thulium -->

Las **puertas en solitario** son cinco puertas de las Puertas Galácticas que pilotas solo: **Alpha Rift**, **Beta Breach**, **Gamma Foundry**, **Delta Siege** y **Omega Vault**. Cada una es una arena vacía propia donde oleadas de alienígenas llegan una tras otra y un jefe espera al final. Construyes una puerta con sus **piezas**, que encuentras girando el Materializador de Energía con Thulium, y una victoria paga Credits, Thulium, experiencia, honor, mineral, placas y munición.

Una puerta en solitario no es una [mazmorra de clan](/wiki/03-Mechanics/Dungeons.md). Una mazmorra es un laberinto que un clan abre para un grupo, con un Señor de la guerra al final; una puerta en solitario es una arena en la que solo estás tú, y nadie más puede entrar contigo. Las dos tienen reglas, pagos y límites separados. La página de las Puertas Galácticas también tiene el **Chrono-Gate**, que no es un lugar al que volar sino la puerta que abre tu [Alijo de Transporte](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) para el reinicio: sus piezas se encuentran con los mismos giros.

## De un vistazo {#at-a-glance}

<!-- solo-glance:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Puertas**: 6: el Chrono-Gate y 5 puertas en solitario, Alpha Rift, Beta Breach, Gamma Foundry, Delta Siege y Omega Vault
- **Giro**: 100 Thulium por giro, y 1, 5, 10 o 100 giros a la vez
- **Probabilidad de una pieza**: 13 % por giro. La puerta a la que pertenece la pieza se elige al azar, y cada puerta recibe el 2,17 % de los giros. Cuando el Chrono-Gate está completo su parte sale de la rueda, y las puertas en solitario conservan el 2,17 % cada una
- **Garantía**: Tras 24 giros seguidos sin pieza la probabilidad sube con cada giro, y tras 47 el siguiente giro encuentra una siempre. Una pieza de cualquier puerta reinicia la cuenta
- **Vidas**: 3 por intento; cada muerte cuesta una
- **Cuenta atrás**: 5 s antes de cada oleada, también la primera y la del jefe. Una oleada no tiene temporizador, ni la partida tampoco
- **Arena**: Espacio abierto de 8.000 × 6.000 unidades sin rocas, y estás solo en él. Un mundo tiene 16 de ellos, y cuando todos están ocupados no puedes entrar
- **Alienígenas a la vez**: Como mucho 60 de una oleada están vivos a la vez, y 250 en una oleada opcional. El resto espera hueco
- **Jefes**: Un jefe no puede ser herido durante 3 s cuando cambia de fase
- **Límite de Thulium**: Una puerta devuelve como máximo el 50 % del Thulium que gastaste en giros. El resto se recorta, y el resultado dice cuánto

<!-- solo-glance:end -->

## Encontrar piezas de puerta {#finding-gate-parts}

Abre la página de las **Puertas Galácticas** y gira el Materializador de Energía. Cada giro se paga en Thulium y encuentra como mucho una pieza, y la pieza pertenece a una de las seis puertas, elegida al azar. Necesitas un número de piezas de una puerta para construirla, y las piezas son tuyas hasta que las usas. Un giro que no encuentra pieza no se pierde: paga un premio ([más abajo](#a-spin-without-a-part)). Cada giro se cobra, también con el Chrono-Gate completo. Cuando el Chrono-Gate está completo su parte de los giros no encuentra nada, y las puertas en solitario mantienen su propia probabilidad, así que una pieza de una puerta en solitario cuesta lo mismo con él o sin él.

La tabla da el coste de cada puerta en piezas y lo que cuestan de media **con la garantía** (un giro es una lotería, así que un piloto afortunado paga menos y uno desafortunado más, hasta la racha de giros más larga que permite la garantía).

<!-- solo-parts:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Puerta | Piezas para completarla | Probabilidad de una pieza por giro | Giros de media | Thulium de media |
| :--- | ---: | ---: | ---: | ---: |
| **Chrono-Gate** | 2 | 2,17 % | 91 | 9.093 |
| **Alpha Rift** | 11 | 2,17 % | 500 | 50.011 |
| **Beta Breach** | 26 | 2,17 % | 1.182 | 118.208 |
| **Gamma Foundry** | 54 | 2,17 % | 2.455 | 245.508 |
| **Delta Siege** | 87 | 2,17 % | 3.955 | 395.541 |
| **Omega Vault** | 108 | 2,17 % | 4.910 | 491.017 |

<!-- solo-parts:end -->

Las piezas del Chrono-Gate vuelven a cero en el reinicio, y las encuentras de nuevo cada temporada. **Las piezas de las puertas en solitario se quedan**, y también la cuenta de la garantía y el registro de lo que gastaste en giros y de lo que las puertas devolvieron; el reinicio no se lleva nada de eso ([Puertas y el reinicio](#gates-and-the-wipe)).

### Un giro sin pieza {#a-spin-without-a-part}

La mayoría de los giros no encuentran pieza. Cada uno de ellos paga un premio, elegido según las probabilidades de abajo: munición láser del segundo multiplicador o mejor, un lote de cohetes del segundo o tercer nivel y, de vez en cuando, un [objeto especial](/wiki/06-Items/Special-Items.md) o un [contenedor](/wiki/06-Items/Containers.md). Un premio que no se puede dar (por ejemplo, ya tienes el máximo de ese objeto especial) se convierte en un lote de munición o de cohetes con la misma tirada, así que un giro nunca paga menos que su tabla. El premio vale claramente menos de lo que cuesta el giro: las puertas son un sumidero de Thulium.

<!-- solo-prizes:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Premio | Probabilidad por giro |
| :--- | ---: |
| Un contenedor: Chroma Archive | 0,01 % |
| Un objeto especial: Magic Hammer | 0,2 % |
| Un objeto especial: Schematics | 0,2 % |
| Un objeto especial: Philosopher's Stone | 0,2 % |
| Un objeto especial: Forger's Seal | 0,2 % |
| Un objeto especial: Workforce Contract | 0,2 % |
| Un objeto especial: Tinkerer's Badge | 0,1 % |
| Munición láser: Advanced Plasma ×75 | 12,88 % |
| Munición láser: Antimatter Battery I ×62 | 8,59 % |
| Munición láser: Ultra Core ×40 | 8,59 % |
| Munición láser: Antimatter Battery II ×29 | 4,29 % |
| Munición láser: Dark Matter Ammo I ×31 | 4,29 % |
| Munición láser: Experimental Fusion Core ×17 | 2,15 % |
| Munición láser: Dark Matter Ammo II ×17 | 2,15 % |
| Cohetes: Lancet II ×4 | 8,59 % |
| Cohetes: Rivet II ×4 | 8,59 % |
| Cohetes: Ember II ×4 | 8,59 % |
| Cohetes: Scatter II ×4 | 8,59 % |
| Cohetes: Lancet III ×1 | 2,15 % |
| Cohetes: Rivet III ×1 | 2,15 % |
| Cohetes: Ember III ×1 | 2,15 % |
| Cohetes: Scatter III ×1 | 2,15 % |

<!-- solo-prizes:end -->

## Entrar {#going-in}

**Construyes** una puerta en la página de las Puertas Galácticas y **saltas** dentro por su portal. Construir se hace desde la estación, con la nave atracada: no hace falta estar volando. Hace falta:

- las piezas de la puerta: se toman **una sola vez, al construirla**, y una construcción rechazada no quita nada;
- ninguna otra partida en solitario abierta: tienes una partida a la vez, y una partida que dejaste se vuelve a entrar por su portal o se abandona antes de que construyas otra puerta;
- el servidor principal (los servidores regionales no tienen puertas).

La puerta construida está en tu **sector base** (`M-1`, `T-1` o `G-1`, según tu corporación) como un portal con su nombre, y la página de las Puertas Galácticas dice dónde está. **Despega, vuela hasta el portal y salta** por él como por cualquier portal. Tiene que haber una grieta libre en tu mundo cuando entres: cada mundo tiene un número de ellas, y cuando todas están ocupadas esperas.

Aterrizas en medio de una arena vacía, solo. Nadie puede atacarte en ella, y la Jump CPU y la Base CPU no funcionan.

## Cómo transcurre una partida {#how-a-run-goes}

1. **Antes de cada oleada hay una cuenta atrás**, también antes de la primera y antes de la del jefe. Una oleada no tiene temporizador, ni la partida tampoco: dura lo que necesites.
2. **Una oleada** aparece en un anillo a tu alrededor y vuela hacia ti, al ritmo de la puerta. Solo viven a la vez tantos de ella, y el resto espera hueco. Termina cuando muere su último alienígena.
3. **Tu progreso se guarda después de cada oleada.** Si te vas, una oleada que estaba en curso empieza de nuevo entera cuando vuelves.
4. **Una oleada opcional** es una oleada enorme de Seeker, y Delta Siege y Omega Vault tienen una cada una. Durante su cuenta atrás puedes saltarla: entonces cuenta como hecha y **no paga nada**. Si la combates, sus bajas pagan como las de cualquier oleada.
5. **La última oleada es el jefe.** Cambia de fase a medida que cae su casco, y no se le puede herir un instante en cada cambio. Cuando el jefe muere, la partida está ganada y la victoria se paga al instante.

**Vidas.** Una muerte cuesta una vida y te envía a tu base como cualquier otra muerte; la partida te espera, sin reloj en marcha. Mientras la partida está abierta y estás fuera de la arena, **el portal de tu puerta está en tu sector base**, y un salto por él te devuelve a la oleada guardada con las vidas que te quedan, como **Reanudar**; no pide piezas nuevas. Cuando se acaba tu última vida, el intento termina pero la partida sigue abierta en la última oleada superada, y volver a entrar te devuelve las vidas. **Salir**, cerrar la sesión o cambiar de mundo pausa la partida sin costar una vida. Un reinicio del servidor también mantiene tu partida abierta. **Abandonar** deja la partida: sus piezas se pierden, y los alienígenas que mataste se pagan tal como están. **Reanudar** solo funciona desde una nave en vuelo: tras una muerte, su botón en la pantalla de resultados espera, con una línea que dice por qué, hasta que hayas reaparecido. Una nave que reaparece vuelve con el casco limitado, así que cuando tu casco está por debajo de la mitad la pantalla de resultados te avisa; **Reanudar** te devuelve igualmente tal como estás. Las naves reparadoras de tu base te reparan dentro de su aura.

Todos los mundos combaten la misma puerta: la fuerza y el pago de los alienígenas no dependen del mundo en el que vueles.

### Las oleadas {#the-waves}

Los alienígenas son los del juego (Seeker, Phantasm, Bulwark, Goombah y Crystalys), hechos más duros o más blandos por la puerta. El tiempo previsto es lo que la puerta está construida para durar con un piloto en el nivel inicial de Tecnología láser ([Destrezas de piloto](/wiki/03-Mechanics/Pilot-Skills.md)); un piloto que ha subido su Tecnología láser termina antes.

<!-- solo-waves:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Puerta | Oleadas, la del jefe incluida | Alienígenas en las oleadas | Jefe | Tiempo previsto |
| :--- | ---: | :--- | :--- | :--- |
| **Alpha Rift** | 10 | 60 Seeker, 160 Phantasm | Enhanced Phantasm | 10 a 15 min |
| **Beta Breach** | 14 | 80 Seeker, 180 Phantasm, 80 Bulwark, 20 Goombah | Enhanced Bulwark | 15 a 25 min |
| **Gamma Foundry** | 18 | 100 Phantasm, 120 Bulwark, 100 Goombah, 8 Crystalys | Elite Crystalys | 25 a 35 min |
| **Delta Siege** | 22 | 250 Seeker, 200 Phantasm, 180 Bulwark, 140 Goombah, 15 Crystalys | Siege Construct | 35 a 45 min |
| **Omega Vault** | 26 | 250 Seeker, 250 Phantasm, 200 Bulwark, 200 Goombah, 25 Crystalys | Omega Guardian | 50 a 60 min |

- **Delta Siege**: la oleada 18 (250 Seeker) es opcional: puedes saltarla mientras corre su cuenta atrás, y no paga nada
- **Omega Vault**: la oleada 17 (250 Seeker) es opcional: puedes saltarla mientras corre su cuenta atrás, y no paga nada; las oleadas 22 a 24 son de élite, con ×1,5 de casco, escudo y daño

<!-- solo-waves:end -->

### Los jefes {#the-bosses}

Un jefe es la nave de un alienígena agrandada, con un casco, un escudo y una ráfaga propios, que ningún ajuste de la puerta ni del mundo cambia. Una fase empieza cuando el casco del jefe baja hasta la cifra de la tabla: su escudo puede volver a ajustarse, su ráfaga o todo su daño cambian, y puede iniciar un movimiento. Cada movimiento se anuncia: un círculo, un anillo o una marca en tu nave lo muestra un instante antes de que caiga. Los alienígenas que llama un jefe no pagan ni sueltan nada.

<!-- solo-bosses:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Jefe | Puerta | Casco | Escudo | Ráfaga láser |
| :--- | :--- | ---: | ---: | ---: |
| **Enhanced Phantasm** | Alpha Rift | 330.000 | 530.000 | 5.700–7.000 |
| **Enhanced Bulwark** | Beta Breach | 690.000 | 170.000 | 4.500–5.500 |
| **Elite Crystalys** | Gamma Foundry | 620.000 | 250.000 | 3.800–4.700 |
| **Siege Construct** | Delta Siege | 1.150.000 | 1.730.000 | 3.400–4.200 |
| **Omega Guardian** | Omega Vault | 1.340.000 | 840.000 | 2.600–3.200 |

| Jefe | Fase | Casco restante | Lo que hace |
| :--- | :--- | :--- | :--- |
| **Enhanced Phantasm** | Enhanced Phantasm | 100 % a 0 % | Solo dispara. |
| **Enhanced Bulwark** | Shielded | 100 % a 50 % | Su escudo se fija en ×4 del propio del jefe. |
|  | Second attack | 50 % a 0 % | Su ráfaga es ×1,3. Te dispara 4 cohetes Dormant Lance, de 61.000 cada uno, uno cada 0,5 s, en una andanada cada 30 s. |
| **Elite Crystalys** | Elite | 100 % a 50 % | Solo dispara. |
|  | Reinforced | 50 % a 0 % | Su escudo se fija en ×2 del propio del jefe. Cada 10 min llama a 10 Goombah, con 10 vivos como máximo; no pagan ni sueltan nada. |
| **Siege Construct** | Siege Construct | 100 % a 0 % | Cada 1 min suelta 3 lluvias de 8 meteoros, de 5.500 cada uno sobre todo lo que esté a menos de 420 unidades de donde cae, 50 % de ellos apuntados a ti; cada círculo se muestra 3 s antes de caer. Te dispara 6 cohetes Dormant Lance, de 9.000 cada uno, uno cada 0,5 s, en una andanada cada 1 min. |
| **Omega Guardian** | Shield Fortress | 100 % a 70 % | Su escudo se fija en ×1,5 del propio del jefe. Cada 40 s llama a 6 Bulwark, con 12 vivos como máximo; no pagan ni sueltan nada. |
|  | Swarm Protocol | 70 % a 35 % | Cada 25 s llama a 12 Phantasm, con 24 vivos como máximo; no pagan ni sueltan nada. Cada 30 s una explosión de 140.000 alcanza todo lo que esté a menos de 700 unidades del jefe; el anillo se muestra 2 s antes de caer. |
|  | Overload | 35 % a 0 % | Su escudo se fija en ×0,1 del propio del jefe. Todo su daño es ×2,5. Tras 2 min en la fase, todo su daño es ×2 más. Cada 25 s una explosión de 28.000 alcanza todo lo que esté a menos de 700 unidades del jefe; el anillo se muestra 2 s antes de caer. |

<!-- solo-bosses:end -->

## Lo que paga una victoria {#what-a-clear-pays}

Una victoria paga su tabla **una vez**, de golpe, en el momento en que muere el jefe: los Credits, el Thulium, la experiencia y el honor, el mineral, las placas y los Power Cores, y la munición. La experiencia cuenta para tus puntos PvE, como la de una mazmorra.

<!-- solo-pay:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Puerta | Créditos | Thulium | XP | Honor |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 450.000 | 5.000 | 70.000 | 1.000 |
| **Beta Breach** | 1.500.000 | 12.000 | 180.000 | 2.500 |
| **Gamma Foundry** | 4.000.000 | 25.000 | 400.000 | 5.500 |
| **Delta Siege** | 8.000.000 | 40.000 | 800.000 | 10.000 |
| **Omega Vault** | 15.000.000 | 60.000 | 1.500.000 | 20.000 |

- **Alpha Rift**: Ship Fragment ×300, Nyxite ×300, Daraxium ×400; munición: Advanced Plasma ×20.000, Ultra Core ×5.000, Experimental Fusion Core ×20.000
- **Beta Breach**: Ship Fragment ×700, Nyxite ×750, Daraxium ×800, Cataclysite ×400, Quorvium ×100; munición: Advanced Plasma ×50.000, Ultra Core ×20.000, Experimental Fusion Core ×30.000
- **Gamma Foundry**: Ship Fragment ×1.150, Nyxite ×1.000, Cataclysite ×900, Quorvium ×400, Power Core ×15; munición: Advanced Plasma ×30.000, Ultra Core ×60.000, Experimental Fusion Core ×50.000
- **Delta Siege**: Ship Fragment ×2.000, Nyxite ×1.750, Cataclysite ×1.500, Quorvium ×1.000, Reinforced Hull Plate ×70, Power Core ×40, Ancient Control Unit ×3; munición: Advanced Plasma ×40.000, Ultra Core ×90.000, Experimental Fusion Core ×75.000
- **Omega Vault**: Ship Fragment ×3.250, Nyxite ×2.750, Cataclysite ×2.250, Quorvium ×1.600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10; munición: Advanced Plasma ×50.000, Ultra Core ×100.000, Experimental Fusion Core ×100.000

<!-- solo-pay:end -->

**El Thulium se recorta a un límite.** Las puertas no pueden devolver más que una parte del Thulium que gastaste en giros, contada sobre todas tus puertas y todos tus giros (la parte está en la lista del principio). Lo que una victoria y sus alienígenas pagarían por encima se recorta, y la pantalla de resultados dice cuánto. Los Credits, la experiencia, el honor, el mineral, las placas y la munición nunca se recortan.

### Los alienígenas {#the-aliens}

Cada alienígena que matas en una puerta paga con las cifras que tiene en Alpha, en el mundo que sea en el que vueles: ningún multiplicador de mundo, ningún booster ni ninguna bonificación Premium las cambia. Una oleada paga por sus alienígenas **una vez** por partida, por muchas veces que salgas y vuelvas. El pago llega con el final de cada tramo de la partida: cuando sales, mueres, te quedas sin vidas, abandonas o la ganas. Las bajas de un tramo solo quedan sin pagar en el reinicio de temporada y en un reinicio del servidor mientras estás dentro (tu partida sigue abierta, pero las bajas de ese tramo se pierden). Las bajas de una puerta no cuentan para nada más: ni para las misiones, ni para las estadísticas de bajas, ni para los contadores de los logros, ni para el registro de bajas, ni para la experiencia de tus drones y P.E.T.s. La experiencia que pagan sí cuenta para tus puntos PvE, como la de una victoria. El botín de los alienígenas llega con el pago, directo a tu inventario.

<!-- solo-kills:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Alienígena | Créditos | Thulium | XP | Honor |
| :--- | ---: | ---: | ---: | ---: |
| **Seeker** | 1.000 | 4 | 100 | 2 |
| **Phantasm** | 3.000 | 12 | 300 | 6 |
| **Bulwark** | 5.000 | 25 | 800 | 10 |
| **Goombah** | 15.000 | 75 | 3.000 | 24 |
| **Crystalys** | 75.000 | 200 | 12.000 | 52 |

| Puerta | Créditos | Thulium | XP | Honor |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 540.000 | 2.160 | 54.000 | 1.080 |
| **Beta Breach** | 1.320.000 | 5.980 | 186.000 | 2.520 |
| **Gamma Foundry** | 3.000.000 | 13.300 | 522.000 | 4.616 |
| **Delta Siege** | 4.975.000 | 21.400 | 829.000 | 7.640 |
| **Omega Vault** | 6.875.000 | 29.000 | 1.160.000 | 10.100 |

<!-- solo-kills:end -->

## Desafíos y logros {#challenges-and-achievements}

Se pueden ganar dos desafíos opcionales con cualquier victoria, y cada uno paga un logro y **ningún Thulium**. Una victoria **sin morir** es una sin ninguna muerte en toda la partida, sumando todas las veces que entraste. Un **speedrun** es una victoria dentro del tiempo previsto más corto de la puerta, contado por el tiempo que pasas dentro de la arena. Los otros seis logros son por superar cada puerta, y las cinco:

<!-- solo-achievements:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Grieta cerrada** (Común): Completa la Alpha Rift en solitario.
- **Brecha sellada** (Poco común): Completa la Beta Breach en solitario.
- **Fundición clausurada** (Raro): Completa la Gamma Foundry en solitario.
- **Asedio roto** (Raro): Rompe el Delta Siege en solitario.
- **Cámara acorazada abierta** (Épico): Abre la Omega Vault en solitario.
- **Guardián de las puertas** (Legendario): Completa las cinco puertas en solitario: Alpha, Beta, Gamma, Delta y Omega.
- **Intocable** (Raro): Completa una puerta en solitario sin perder una vida.
- **Contra el reloj** (Raro): Completa una puerta en solitario en su tiempo más corto o menos: 10, 15, 25, 35 o 50 minutos, de Alpha a Omega.

<!-- solo-achievements:end -->

## Objetos de una puerta {#items-from-a-gate}

Lo que te da una puerta es **comerciable**: el mineral, las placas, los Power Cores, la munición y el botín de los alienígenas se pueden poner a la venta en la [Subasta](/wiki/03-Mechanics/Auction.md) como un botín o la recompensa de una misión, con las mismas excepciones que cualquier objeto. Los premios de un giro sin pieza no lo son: vienen de un giro, no de una puerta.

## Puertas y el reinicio {#gates-and-the-wipe}

- **El reinicio termina cualquier partida abierta** y te devuelve sus piezas. Una partida no continúa en la temporada siguiente.
- **Se conservan en el reinicio:** las piezas de las cinco puertas en solitario, la cuenta de la garantía y el registro de lo que gastaste en giros y de lo que las puertas devolvieron, así que el límite del Thulium continúa de una temporada a otra. Los logros son tuyos para siempre.
- **Se pierden en el reinicio:** las piezas del Chrono-Gate, como antes. Tus giros las compran de nuevo.
- **Eliminar una cuenta** elimina las piezas, la cuenta y el registro.
