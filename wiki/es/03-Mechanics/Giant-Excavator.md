<!-- wiki-i18n source: 6b964707b3b7ca22 -->
<!-- wiki-i18n title: Excavadora gigante -->
# Excavadora gigante {#giant-excavator}

<!-- wiki-search: excavator; giant excavator; pulsar; mining; fuel; excavator fuel; control panel; overheat; radiation; slumbering void; voids; wave; ds-1; ds-2; ds-3; excavadora; excavadora gigante; púlsar; combustible; panel de control; sobrecalentamiento; radiación; oleada -->

Desde el primer día de la temporada brilla un **púlsar** en cada uno de los sectores de peligro `DS-1`, `DS-2` y `DS-3`, y desde el día 11 de la temporada hay una **excavadora gigante** a su lado. La excavadora mina el púlsar en busca de **Thulium y minerales raros**, y para ello quema [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md). Cualquiera puede repostarla, elegir qué mina y ponerla en marcha, y todo lo que suelta queda a su alrededor en cajas que puede recoger cualquiera. Pero una tanda es ruidosa: todo el mundo se entera cuando empieza, los **Slumbering Voids** acuden a por ella en oleadas, y una excavadora que se trabaja demasiado se sobrecalienta e irradia toda la zona. Esta página explica cómo transcurre una tanda, qué suelta y cómo sobrevivirla. Los sectores están en [Sectores de peligro](/wiki/01-General/Danger-Sectors.md); los Voids, en [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).

![The giant excavator's sheet: the fuel tank, the heat, the resource to mine, the excavator's hull and the Voids of the next wave](../../img/wiki-img/shots/excavator-sheet.jpg)

## De un vistazo {#at-a-glance}

<!-- excavator-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Dónde**: Un púlsar con una excavadora gigante en cada uno de los sectores `DS-1`, `DS-2` y `DS-3`, en todos los mundos
- **Aparece**: El púlsar desde el primer día de la temporada, la excavadora desde el día 11 de la temporada hasta el reinicio
- **Combustible**: Dark Matter. Uno dura 10 min; el depósito admite 3, que son 30 min de minería. Cualquiera puede añadir uno cada vez, de su propia carga
- **Panel**: La ventana funciona a menos de 600 unidades de la excavadora, y su etiqueta se ve desde 1.400 unidades. Cualquiera puede repostar, elegir e iniciar; la elección queda fijada mientras funciona
- **Cajas**: Una caja cada 20 s, a entre 450 y 900 unidades de la excavadora, libre para cualquiera desde el momento en que cae. Dura 5 min, y como máximo hay 24 a la vez en un mapa
- **Calor**: 30 min de minería, en tantas tandas como haga falta, y la excavadora se sobrecalienta durante 1 h. El calor se conserva entre tandas y desaparece tras el descanso
- **Radiación**: Mientras está sobrecalentada o destruida, la excavadora (a menos de 1.100 unidades) y su púlsar (a menos de 1.300 unidades) queman toda nave que haya dentro: 10 % de sus HP totales cada segundo
- **Casco**: 200.000 HP en Alpha, 300.000 en Beta y 400.000 en Gamma. Solo los Slumbering Voids pueden dañarla, y solo cuando no queda ningún piloto que la defienda
- **Voids**: 2 Slumbering Voids cada 2 min mientras mina, los primeros 1 min después del inicio; como máximo 8 vivos en un mapa
- **Avisos**: Se avisa a los pilotos de todo el mundo cuándo empieza una tanda, cuándo se sobrecalienta la excavadora y cuándo es destruida; el resto va a los pilotos de su sector. Son líneas del Sistema: aparecen en la pestaña **Sistema** del chat y en el Registro de juego, y no en **Global** ni en **Local**.

<!-- excavator-glance:end -->

## Cómo transcurre una tanda {#how-a-run-goes}

1. **Encuentra una.** Desde el día 11 de la temporada cada uno de los tres sectores de peligro que tienen un púlsar tiene una excavadora, en cada mundo. Una etiqueta, **Excavadora**, cuelga sobre ella cuando estás cerca, y el mapa del Sistema estelar marca cada sector de peligro que tiene una: el color de la marca es el estado de su excavadora, y su información emergente dice el tiempo que falta para su próximo cambio.
2. **Abre el panel.** Haz clic en la etiqueta. La ventana **Excavadora gigante** funciona mientras tu nave esté dentro del alcance del panel de la excavadora (la lista *De un vistazo* lo indica). Una nave camuflada puede usarlo, y usarlo no termina el camuflaje.
3. **Reposta.** **Añadir Dark Matter** pone un Dark Matter de tu carga en el depósito. Puede hacerlo cualquiera. El depósito nunca admite más de lo que la excavadora puede quemar antes de sobrecalentarse, así que no se desperdicia combustible.
4. **Elige qué minar** en la lista y pulsa **Iniciar minería**. Hace falta al menos un Dark Matter en el depósito y un recurso. Cualquiera puede cambiar la elección hasta el inicio; una vez en marcha, el recurso queda fijado. El inicio se avisa a todos los pilotos del mundo, con tu nombre, el sector y el recurso.
5. **Defiéndela.** Mientras mina, cada pocos segundos cae una caja alrededor de la excavadora, y poco después del inicio llegan los primeros Slumbering Voids. Defiende la excavadora y recoge las cajas.
6. **Vigila el calor.** La barra de Calor se llena mientras la excavadora mina y nunca se vacía mientras espera. En su límite la excavadora se sobrecalienta. Vete antes: el juego avisa al mapa dos veces.
7. **Descansa.** Sobrecalentada o destruida, la excavadora y su púlsar quedan irradiados hasta que termina el descanso; entonces vuelve a estar lista, con el calor a cero y el casco lleno.

La ventana muestra además el sector, el depósito (una celda por cada Dark Matter, la que se quema dibujada a medias), cuánto Dark Matter llevas, el casco de la excavadora, lo que cada recurso suelta por minuto en tu mundo y, mientras mina, el tiempo hasta la siguiente oleada y los Voids vivos. Cuando algo es rechazado, lees el motivo en rojo: estás demasiado lejos del panel, no tienes Dark Matter, el depósito está lleno, aún no hay combustible o recurso elegido, el recurso está fijado mientras funciona, o la excavadora está caliente.

| Estado | Qué es | Qué puedes hacer |
| :--- | :--- | :--- |
| **Lista** | Sin combustible, o con combustible y sin iniciar. El calor acumulado se conserva. | Añadir Dark Matter, elegir, iniciar. |
| **Minando** | Quema Dark Matter y acumula calor; el recurso está fijado. | Añadir más Dark Matter hasta el hueco que quede, combatir a los Voids, recoger las cajas. |
| **Sobrecalentada** | El calor llegó a su límite. El depósito se vacía; las cajas ya soltadas se quedan. | Nada. La zona está irradiada: mantente fuera. |
| **Destruida** | Los Voids llevaron el casco a cero. El combustible se pierde, el casco vuelve a estar lleno de inmediato. | Nada. La zona está irradiada: mantente fuera. |

Si el combustible se agota antes del límite, la excavadora vuelve a **Lista** con su calor conservado, y los Voids que quedan se van pasado un tiempo, salvo que estén combatiendo.

## Qué mina {#what-it-mines}

Un depósito lleno suelta aproximadamente lo que ganarían cinco pilotos en media hora del mejor cultivo de Thulium. Beta y Gamma sueltan más, igual que pagan más por cada derribo. Eliges un recurso por tanda. Una caja es igual para todos, y una caja de Thulium es dinero en efectivo que se paga al recogerla, como el Thulium de los asteroides.

<!-- excavator-resources:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Un depósito lleno (3 Dark Matter, 30 min de minería) suelta las cantidades de abajo, en 90 cajas.

| Recurso | Alpha | Beta | Gamma | Un minuto, en Alpha | Una caja, en Alpha |
| :--- | ---: | ---: | ---: | ---: | ---: |
| [Thulium](/wiki/06-Items/Resources.md#thulium) | 9.643 | 15.429 | 19.286 | 321,4 | 107,1 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | 2.314 | 3.703 | 4.629 | 77,1 | 25,7 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | 1.029 | 1.646 | 2.057 | 34,3 | 11,4 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | 640 | 640 | 640 | 21,3 | 7,1 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | 320 | 320 | 320 | 10,7 | 3,6 |

- Una tanda de Velkonite o Orvium suelta como máximo 8 horas de un colector del [Skylab](/wiki/03-Mechanics/Skylab.md) de nivel 20 de ese mineral (640 Velkonite, 320 Orvium), en todos los mundos: son los minerales del Skylab, y una tanda nunca acelera su ritmo en más que eso.
- Una caja contiene aproximadamente la cantidad de la última columna, 15 % arriba o abajo. Una caja de Thulium es dinero en efectivo: la recogida lo paga. Una caja de mineral contiene el objeto.

<!-- excavator-resources:end -->

Los potenciadores del propio piloto funcionan como con cualquier carga: la bonificación del Resource Magnet Booster aumenta una caja de mineral. No hay límite diario para las cajas: el combustible y el reloj son lo que limita una tanda.

**Para qué sirve el mineral.** El mineral de una caja va a tu carga como cualquier objeto. El Cataclysite y el Quorvium se usan en el Ensamblaje y en la Forja ([Recursos](/wiki/06-Items/Resources.md)). La Forja y el Centro de investigación del Skylab toman el Velkonite y el Orvium solo del Almacén de recursos, que llenan los colectores, así que el mineral de una caja no sirve de nada en tu carga: aterriza tu nave y la [Bahía de mineral](/wiki/03-Mechanics/Skylab.md#ore-bay) de tu Skylab (nivel 10 del Núcleo) lo pasa al almacén, hasta su cupo por hora, y de allí lo toman la Forja y el [Centro de investigación](/wiki/03-Mechanics/Research.md#fuel).

## Los Slumbering Voids {#the-slumbering-voids}

Una tanda atrae a los **Slumbering Voids**, cazadores de la civilización perdida que llegan volando desde el borde del mapa para proteger el púlsar de quien quiera vaciarlo. Cazan a los pilotos cercanos a la excavadora, y cuando ya no queda nadie a quien cazar, van a por la excavadora. Las cifras del Void y su paga están en [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).

<!-- excavator-voids:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Oleadas.** 2 Slumbering Voids cada 2 min; los primeros 1 min después del inicio, y ninguno en los últimos 1 min de una tanda. Como máximo 8 están vivos a la vez en un mapa: una oleada que encuentra el mapa lleno se omite.
- **Llegada.** Una oleada aparece en el borde del mapa, 900 unidades hacia dentro y como mínimo a 2.500 unidades de todo anillo de puerta, y vuela hasta la excavadora en unos 20 s. El mensaje nombra el lado del mapa por el que llega.
- **Caza.** Un Void caza al piloto más cercano que pueda ver a menos de 2.500 unidades, y se mantiene a menos de 7.000 unidades de la excavadora.
- **Asedio.** Cuando durante 15 s no hay ningún piloto que puedan ver a menos de 7.000 unidades de la excavadora, los Voids atacan la excavadora, y cada láser hace 25 % de su daño habitual. A cero la excavadora es destruida: su combustible se pierde, su casco vuelve a estar lleno de inmediato y descansa 1 h.
- **Retirada.** Cuando termina una tanda, los Voids que quedan se quedan 90 s más y siguen combatiendo si se les combate; luego se van.

<!-- excavator-voids:end -->

- **Un Void es un cañón de cristal.** Su escudo es grande, pero absorbe el 80 % de un impacto, así que el casco que hay detrás cae tras unas pocas veces su tamaño en daño, y mucho antes con penetración de escudo. Dos o tres pilotos bien equipados aguantan una tanda en Alpha; Beta y Gamma necesitan grupos mayores, como con cualquier alienígena.
- **Un camuflaje no defiende el lugar.** Los Voids no ven las naves camufladas, así que un piloto que se esconde no los aparta de la excavadora; y un piloto que se refugia en un anillo de puerta no puede ser alcanzado y tampoco cuenta.
- **Cada Void paga,** según el daño que le causaste, y suelta una caja ([cómo paga el derribo de un jefe](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Sus derribos suman a tus puntos PvE de rango como los de una nave de enjambre.

## Calor y radiación {#heat-and-radiation}

La minería añade calor segundo a segundo. El calor es **acumulativo y nunca se enfría mientras la excavadora espera**: una tanda que termina pronto le deja al siguiente piloto una más corta. Cuando llega al límite, la excavadora **se sobrecalienta**, y cuando su casco llega a cero es **destruida**; en ambos casos la excavadora y su púlsar irradian hasta que termina el descanso.

<!-- excavator-radiation:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

| Círculo | Radio | HP totales por segundo | Una nave llena aguanta |
| :--- | ---: | ---: | ---: |
| La excavadora gigante | 1.100 | 10 % | 10 s |
| El púlsar | 1.300 | 10 % | 10 s |

- **La dosis.** 10 % de los HP máximos totales de una nave (casco más escudo) cada segundo, así que una nave llena aguanta 10 s, sea cual sea su clase. El escudo la recibe primero y su absorción no cuenta.
- **A quién.** A toda nave dentro de los círculos, también a las camufladas; a ningún alienígena. Cuenta como daño recibido: un Dron reparador se detiene y el escudo no se recarga, como en el agujero negro.
- **Acreditación.** Un piloto que muere abrasado se acredita al último enemigo que lo impactó en los 15 s anteriores.
- **Avisos.** Se avisa al mapa 1 min y 15 s antes del sobrecalentamiento.

<!-- excavator-radiation:end -->

- **El aviso.** Dos veces antes del sobrecalentamiento (los tiempos están en la lista de arriba) se avisa al mapa, una nave dentro de los círculos ve una advertencia y los círculos se dibujan en el suelo durante el vuelo y en el minimapa. Cuando irradian, los círculos son rojos y el indicador de Radiación muestra la dosis.
- **Salir.** Toda nave de serie puede salir desde el borde del panel o desde la caja más lejana que quede, salvo la Ironclad, que es lenta: sale durante el aviso, o no sale. No te quedes sobre una caja cuando se acabe el calor.
- **Botín en los círculos.** Las cajas soltadas antes del sobrecalentamiento se quedan en la radiación: una caja que está allí cuando empieza se recoge al precio de la dosis.
- **Un reinicio del servidor** detiene una tanda: el combustible y el calor vuelven como estaban, el descanso sigue según el reloj, y la primera oleada tras el reinicio llega un minuto después.

## Pelear por una tanda {#fighting-over-a-run}

La excavadora **no tiene un anillo especial**: valen las reglas normales de tu mundo, así que pueden venir rivales, dispararte y llevarse las cajas (una caja es libre para cualquiera desde el momento en que cae). Robar y tender emboscadas forma parte del evento. Algunas cosas que conviene prever:

- **Quien reposta no es quien gana.** Cualquiera puede repostar, elegir e iniciar; un rival puede cambiar el recurso antes de que pulses Iniciar. Comprueba la elección antes de pulsar.
- **El combustible corre peligro.** Si la excavadora es destruida, el Dark Matter de su depósito se pierde y nadie lo recupera. Lo máximo que se puede perder es el depósito lleno.
- **Ve con un grupo** y decidid quién se queda cerca de la excavadora y quién recoge las cajas, y no pierdas de vista el calor: los pilotos que recogen las últimas cajas son los que la radiación atrapa.
- **Los Voids van a la excavadora, no a las cajas.** Un grupo que sostiene la excavadora mantiene ocupados a los Voids; el que se marcha se la deja al asedio.

## De qué se entera el mundo {#what-the-world-is-told}

Son líneas del Sistema (aparecen en la pestaña **Sistema** del chat y en el Registro de juego, y no en **Global** ni en **Local**). Las tres primeras van a todo el mundo; la última, a los pilotos del sector de la excavadora.

- El día en que empieza el evento 2: los sectores de peligro han cambiado.
- Un piloto **inicia** una excavadora, con el sector, el recurso y los minutos de combustible.
- La excavadora **se sobrecalienta** o es **destruida**.
- Se agota el combustible; la excavadora está a punto de sobrecalentarse (dos avisos); viene una **oleada** de Voids, con su número y el lado del mapa por el que llega; no queda ningún piloto, así que los Voids atacan la excavadora.

Cada acción del panel y cada aviso tiene un sonido suave propio, con el volumen de efectos.

## Dónde leer más {#where-to-read-more}

- [Sectores de peligro](/wiki/01-General/Danger-Sectors.md): dónde están los púlsares y qué más hay de nuevo.
- [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md): el Slumbering Void, la Inert Mass y el Unwakened.
- [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md) y [El agujero negro](/wiki/03-Mechanics/Black-Hole.md): de dónde viene el combustible.
- [Recursos](/wiki/06-Items/Resources.md): los minerales que suelta la excavadora.
- [Cajas de carga](/wiki/03-Mechanics/Cargo.md): cajas, recogida y el Resource Magnet Booster.
- [Rangos](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points): los puntos PvE de un Void.
