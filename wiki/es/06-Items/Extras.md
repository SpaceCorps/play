<!-- wiki-i18n source: 1855960bc32d6626 -->
<!-- wiki-i18n title: Extras -->
# Extras

Los extras son los dispositivos que van en las **ranuras de extra** de una nave (dos en la Protos, la Kitefin, la Ostirion y la Nomad, las naves con las que empiezas o que compras, y tres en la Paragon, la Ironclad, la Wraith y la Storm, las naves que fabricas, por configuración, y 3, 5 o 7 más con las Extra Slots CPU). Los activas desde el selector de Extras de la barra rápida o desde una ranura de la barra que les hayas asignado. Solo funcionan desde la configuración que pilotas: si instalas uno en la otra configuración, espera hasta que cambies de configuración.

| Extra | Qué hace | Usos | Precio |
| :---- | :----------- | :--- | :---- |
| **Repair Drone I a IV** | Repara tu casco: 1,5 %, 2,25 %, 3,5 % y 5 % del máximo por segundo | ilimitados | 5000 / 15.000 / 35.000 créditos, 2000 Thulium |
| **Cloaking CPU S** | Oculta tu nave | 10 | 5000 Thulium |
| **Cloaking CPU M** | Oculta tu nave | 25 | 11.250 Thulium |
| **Cloaking CPU L** | Oculta tu nave | 50 | 20.000 Thulium |
| **EMP Charge** | Durante 3 segundos nadie puede fijarte, todas las fijaciones sobre ti se rompen y todos los camuflajes cercanos terminan | 1 | 500 Thulium |

Las Cloaking CPU y la EMP Charge se venden solo en la tienda. No se pueden fusionar y nada las regala.

El **equipo inicial** de un piloto nuevo ya instala dos extras en las dos ranuras de extra de la Protos: una **Base CPU I** (10 usos, un teletransporte a la base de tu corporación) y un **Repair Drone I**. Arrástralos desde el selector de Extras de la barra rápida a una ranura para usarlos. Solo los pilotos nuevos reciben el equipo: quien se alistó antes de la 0.4.10 no lo tiene.

Otras siete CPU no se venden: Ensamblaje las fabrica cuando el Centro de investigación del Skylab las ha investigado (consulta [Investigación](/wiki/03-Mechanics/Research.md)). Son la Extra Slots CPU I, II y III, la Jump CPU, la Base CPU I y II y la Auto-Repair CPU, y [la última sección](#research-cpus) cuenta qué hace cada una. Como la Cloaking CPU, la Jump CPU y las Base CPU son para un momento tranquilo: ninguna de las tres arranca dentro de los 10 segundos posteriores a un disparo tuyo o a un impacto que recibas. Las dos CPU de warp, la Jump CPU y las Base CPU, también se rechazan mientras llevas un objeto de misión («No puedes usar un CPU de warp mientras llevas un objeto de misión.»): consulta [Objetos de misión](/wiki/03-Mechanics/Quests.md#quest-items).

Cada extra tiene una etiqueta corta en su ranura de la barra rápida: **REP** para un Repair Drone, **CLK** para una Cloaking CPU, **EMP** para la EMP Charge y **ARP**, **BSE** y **JMP** para la Auto-Repair CPU, la Base CPU y la Jump CPU. Las Extra Slots CPU no tienen ranura: se instalan en tu Skylab. Apunta a una ranura para leer qué hace ahora una pulsación, o por qué no puede.

![The Extras picker of the hotbar: Cloaking, Base and Jump CPUs to drag onto a slot](../../img/wiki-img/shots/cpu-hotbar.jpg)
![The Repair Drone of an extra slot docked to its ship and its wingmen](../../img/wiki-img/shots/repair-drones-extra.jpg)

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Árbol de objetos {#item-tree}

Lo que fabrica Ensamblaje necesita antes su tecnología; pasa el cursor por un objeto para ver cuánto tarda en investigarse. El árbol de tecnologías, el combustible y el impulso: [Investigación](/wiki/03-Mechanics/Research.md).

```tree
Cloaking CPU S | extra, common | buy 5000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Repair Drone I | extra, common | buy 5000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone II | extra, common | buy 15000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone III | extra, common | buy 35000 Credits | /wiki/06-Items/Extras.md#repair-drones
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
EMP Charge | extra, uncommon | buy 500 Thulium | /wiki/06-Items/Extras.md#emp-charge
Cloaking CPU M | extra, uncommon | buy 11250 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 8 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu
Repair Drone IV | extra, rare | buy 2000 Thulium | /wiki/06-Items/Extras.md#repair-drones
Cloaking CPU L | extra, rare | buy 20000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 20 Velkonite Reinforced Plate, 6 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu

Cloaking CPU S -> Cloaking CPU M -> Cloaking CPU L
Repair Drone I -> Repair Drone II -> Repair Drone III -> Repair Drone IV
Extra Slots CPU I -> Extra Slots CPU II -> Extra Slots CPU III
Base CPU I -> Base CPU II
```
<!-- item-tree:end -->

## Repair Drones

Activa un Repair Drone (REP) y repara el casco hasta que esté completo. Solo empieza tras 10 segundos sin recibir impactos, y cualquier impacto lo apaga. Con varios instalados, trabaja el mejor. Una [Auto-Repair CPU](#auto-repair-cpu) lo vuelve a activar por ti. Las tasas están en [Combate](/wiki/03-Mechanics/Combat.md). Mientras repara, pequeños drones de reparación salen de la nave, la rodean y alcanzan el casco con sus rayos, uno para un Repair Drone I, dos para un II, tres para un III o un IV, y los pilotos cercanos los ven; vuelven a acoplarse cuando la reparación se detiene.

## Cloaking CPU

Pulsa la ranura CLK para camuflarte. **Una pulsación es un uso**, sea cual sea el paquete, y los usos que quedan se ven en la ranura y en el hangar. Un camuflaje **no tiene límite de tiempo**: sigue activo hasta que lo apagas o algo lo rompe.

- **Quién no puede verte.** Los pilotos de otras corporaciones y los alienígenas no ven tu nave en absoluto: no aparece en su pantalla ni en su lista de objetivos, y nadie puede fijarla. Los pilotos de corporación de otras corporaciones también la ignoran.
- **El punto de radar.** Todos los demás pilotos del mapa, salvo los de tu propia corporación, ven un simple **punto rojo** en el minimapa donde estás, así que saben que hay alguien camuflado cerca. El punto no tiene nombre, nave, corporación ni id, y no admite clics ni fijación; al pasar el cursor por encima solo dice «Hay algo camuflado aquí». Es redondo, dentro de un anillo (las naves en el minimapa son cuadrados), y el anillo «respira» despacio, o se queda quieto si tienes activado Reducir movimiento. El servidor lo actualiza unas dos veces por segundo y tu juego lo mueve con suavidad entre una actualización y otra. Dice que hay alguien y dónde, no quién: un piloto que te vio camuflarte puede seguir el punto, y la **explosión de un cohete** dirigida a él aun así te alcanza.
- **Quién sí te ve.** Tú ves tu propia nave, tenue y con un contorno. Los pilotos de tu corporación te ven como un fantasma pálido; los compañeros de clan de otras corporaciones no, porque un clan admite a cualquiera que lo solicite. Nadie puede fijar al fantasma, ni siquiera tu corporación.
- **No puedes camuflarte** dentro de una zona segura, mientras la CPU se recarga, ni en los **10 segundos** posteriores a recibir un impacto o disparar.
- **Qué lo termina.** Volver a pulsar la ranura, tu primera andanada o cohete (llega a su destino y te ven), entrar en una zona segura, que la CPU salga de la configuración que pilotas, un **EMP que se active a menos de 1500 unidades** de ti, lo haya lanzado quien lo haya lanzado (también el de tu corporación, pero no el de un compañero de grupo), y la explosión en área de un cohete que te alcanza. El tiempo no lo termina, recoger carga tampoco (una caja que recoges desaparece para todos, así que se enteran de que algo estuvo al alcance de ese punto, no de quién), las habilidades tampoco, y la radiación del agujero negro daña a una nave camuflada pero no termina su camuflaje. Cerrar sesión o morir lo termina, porque una nave que nadie pilota no está camuflada.
- **Recarga.** Cuando un camuflaje termina, sea como sea, la CPU se recarga durante **60 segundos**. La recarga es tuya, no de la nave: continúa si saltas por un portal, cierras sesión o mueres. Cada pulsación sigue costando un uso.
- **Los alienígenas** que iban tras de ti te pierden. Tus reclamaciones de derribo se liberan cuando te camuflas.
- **Cohetes.** Nadie puede fijar un cohete guiado sobre ti, y un cohete recto de un objetivo te atraviesa. Una **explosión en área** sigue dañando a una nave que cubre y termina su camuflaje, y a los pilotos que pueden ver el lugar de la nave se les muestra antes de que aparezca el número de daño. Lanzar un cohete es un disparo: termina tu propio camuflaje igual que una andanada (la CPU se recarga entonces los 60 segundos indicados arriba) y, camuflado o no, te impide camuflarte durante los 10 segundos siguientes.
- **El agujero negro** se traga una nave camuflada como cualquier otra, y todo el mapa lo oye.
- **Lo que ves.** Tu nave se vuelve translúcida, con un contorno violeta discontinuo, y un indicador en la parte superior de la pantalla dice «Camuflado» con los usos que quedan (sin segundos: no hay temporizador). La ranura CLK muestra los usos restantes; mientras estás camuflado brilla en violeta y dice ON, y cuando el camuflaje termina, sea como sea, se oscurece y cuenta los 60 segundos de recarga. Una pulsación que el servidor rechaza (recarga, zona segura, un impacto o un disparo en los últimos 10 segundos) hace parpadear la ranura en rojo, y un mensaje te dice por qué. Un aliado se muestra como un fantasma pálido con una marca de fantasma antes de su nombre, y un piloto que se camufla cerca de ti se desvanece con una onda. Arrastra CLK desde los Extras de la barra rápida a una ranura para usarlo, como REP.
- **Los usos** se guardan con la CPU. Cerrar sesión, morir o reiniciar el juego no devuelve ninguno, y una activación que cancelas se gasta igualmente. Cuando se acaba el último uso de un paquete, este se consume y su ranura se rellena con una CPU igual de repuesto que tengas en el inventario, si tienes alguna.
- **Varias CPU** en una misma configuración no se suman. Se usa primero la que menos usos tiene.

Las S, M y L se comportan igual: los paquetes más grandes solo salen más baratos por uso (500, 450 y 400 Thulium).

## EMP Charge

Pulsa la ranura EMP en combate. Durante **3 segundos** nadie puede fijarte, y **todos los que te tenían fijado pierden la fijación** al instante, estén donde estén: pilotos, alienígenas y pilotos de corporación. A un piloto al que se le rompe la fijación se le avisa con «Fijación perdida: el objetivo usó un EMP». Quien intente fijarte en esos 3 segundos es rechazado.

- **No es invulnerabilidad.** Detiene lo que necesita fijación: los láseres, los cohetes guiados y el contacto de un cohete recto de un objetivo, que te atraviesa. Una **explosión en área** no necesita fijación, así que sigue dañándote si estás dentro, y el agujero negro no es un disparo en absoluto.
- **Sigues pudiendo actuar.** Disparar no lo termina. Puedes camuflarte (si las reglas propias del camuflaje lo permiten) y usar otros extras.
- **Termina los camuflajes cercanos.** Toda nave camuflada a menos de **1500 unidades** de ti cuando se activa el pulso se muestra al instante y su CPU empieza sus 60 segundos de recarga, sea de la corporación que sea, también la tuya; las naves de tu propio [grupo](/wiki/03-Mechanics/Groups.md) son la excepción: conservan su camuflaje. Al piloto se le avisa con «Camuflaje roto: se ha lanzado un EMP cerca.», ve reaparecer la nave con la misma onda que en cualquier descamuflaje, y la ranura empieza su recarga. No puedes usar un EMP estando tú mismo camuflado.
- **No oculta nada.** Todos te siguen viendo, con una envoltura eléctrica crepitante durante los 3 segundos.
- **No puedes usarlo** mientras te protege una zona segura, estando camuflado, ni en los **30 segundos** posteriores al último. Funciona en todos los demás sitios, incluidos los primeros días de una temporada (el Protocolo de paz): entonces los alienígenas siguen cazando.
- Un alienígena al que alcances durante los 3 segundos no se vuelve contra ti hasta que terminen. Tus reclamaciones de derribo y las reglas del primer impacto no cambian.
- **Lo que ves.** Un pulso de espacio deformado sale disparado desde el piloto hasta donde el pulso termina camuflajes (1500 unidades), todos los que están al alcance lo ven, y una envoltura eléctrica crepitante lo rodea durante los 3 segundos, con un anillo alrededor de tu propia nave y un indicador en la parte superior de la pantalla que cuentan el tiempo. El anillo de objetivo de todos los que te tenían seleccionado se rompe en pedazos, con un chispazo corto. La ranura EMP muestra las cargas que tienes, se ilumina en azul mientras la envoltura está activa y se oscurece mientras se recarga.
- **Una carga, un uso.** La ranura se rellena desde tu inventario cuando tienes más. Los **30 segundos** de recarga no se guardan: cerrar sesión o saltar por un portal los borra, y el siguiente pulso cuesta una carga.

## CPU del Centro de investigación {#research-cpus}

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | Tiempo de investigación | Necesita antes | Thulium para fabricar | Tiempo de fabricación |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 min | – | 12.000 | 5 min |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10 h | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30.000 | 10 min |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1 d | [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75.000 | 15 min |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3 h | – | 8.000 | 5 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10 h | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 20.000 | 10 min |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1 d | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40.000 | 15 min |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6 h | – | 15.000 | 10 min |

Ninguna se vende en la tienda: investiga la tecnología y luego fabrica la CPU en Ensamblaje. Pasa el cursor por una CPU en su árbol para ver qué pide Ensamblaje para fabricarla.

### Extra Slots CPUs

- **Qué hacen.** La Extra Slots CPU I, II y III dan a cada nave 3, 5 y 7 ranuras de extra más, es decir, 6, 8 y 10 en total en una nave que tiene 3 propias, y 5, 7 y 9 en una que tiene 2. Una CPU superior sustituye a la anterior: la II no se suma a la I.
- **Se instala, no se lleva.** Una Extra Slots CPU no es un objeto: cuando la recoges en Ensamblaje se instala sola en tu Skylab, para todas las naves en las dos configuraciones, y no ocupa ninguna ranura. Se conserva tras el reinicio.
- **En orden.** Fabrícalas una tras otra: la II solo cuando la I está instalada, la III solo cuando la II está instalada; hasta entonces Ensamblaje te dice cuál instalar primero. Las tres cuestan 117.000 Thulium en total: 12.000, 30.000 y 75.000.

### Jump CPU

- **Qué hace.** Salta con tu nave a cualquier sector de corporación de tu mundo, tanto de tu propia corporación como de las demás, con sus sectores base incluidos (`M`, `T` y `G`, sectores 1 a 4), por **500 Thulium** cada salto. No tiene límite de usos: solo pagas el Thulium. Nunca lleva a un sector de peligro (`DS`) ni a un sector neutral (`N`).
- **El salto.** Pulsa la ranura JMP, elige el sector en el mapa del Sistema estelar y confirma: la nave se carga durante 5 segundos y luego llega a una puerta de ese sector, protegida como tras cualquier salto de puerta. La CPU se enfría durante 30 segundos tras tu llegada.
- **No en combate.** No puede empezar dentro de los 10 segundos posteriores a disparar o recibir un golpe, y un disparo o un golpe mientras se carga cancela el salto; entonces no se paga nada. No puedes saltar camuflado.
- **No desde un sector neutral:** un piloto que esté en un sector neutral o no tenga corporación no puede usarla.
- Puede salir de un sector de peligro cuando no estás en combate.

### Base CPUs

- **Qué hacen.** Teletransportan tu nave a la base de tu corporación, a la zona segura que rodea su estación (`M-1`, `T-1` o `G-1`, el sector con Mission Control), sin coste de Thulium. Las inicias desde la ranura BSE de la barra rápida.
- **No en combate.** Una carga de 10 segundos, la misma para ambas. No puede empezar dentro de los 10 segundos posteriores a disparar o recibir un golpe, ni estando camuflado ni cuando ya estás dentro de la zona segura de tu base, y un disparo o un golpe mientras se carga la cancela.

| CPU | Usos | Enfriamiento |
| :--- | ---: | ---: |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 10 | 10 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 25 | 5 min |

- **Se gasta, no se recarga.** Cada uso consume uno de los usos de la CPU, y una CPU sin usos restantes desaparece: fabrica otra. Si llevas las dos puestas, se usa primero la mejor (II).

### Auto-Repair CPU

- **Qué hace.** Lanza por sí sola el Repair Drone que llevas en las ranuras de extra, siempre que pudieras haberlo lanzado a mano: tu casco no está lleno, el dron no está ya fuera y han pasado 10 segundos desde el último golpe. No hay ningún nivel de casco que configurar.
- Ocupa una ranura de extra propia y no hace nada sin un Repair Drone en una ranura de extra de la misma configuración. Nunca lanza un Repair Drone de una ranura de habilidad (ese es el botón Emergency Repair).
- **Si detienes el dron a mano,** la CPU lo deja en paz hasta que tu casco vuelva a estar lleno o hasta que lo lances tú.


<!-- research-cpus:end -->
