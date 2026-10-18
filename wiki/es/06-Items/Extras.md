<!-- wiki-i18n source: b961ad7c5408494d -->
<!-- wiki-i18n title: Extras -->
# Extras

Los extras son los dispositivos que van en las **ranuras de extra** de una nave (dos en la Protos, la Kitefin, la Ostirion y la Nomad, las naves con las que empiezas o que compras, y tres en la Paragon, la Ironclad, la Wraith y la Storm, las naves que fabricas, por configuración, y 3, 5 o 7 más con las Extra Slots CPU). Los activas desde el selector de Extras de la barra rápida o desde una ranura de la barra que les hayas asignado. Solo funcionan desde la configuración que pilotas: si instalas uno en la otra configuración, espera hasta que cambies de configuración.

| Extra | Qué hace | Usos | Precio |
| :---- | :----------- | :--- | :---- |
| **Repair Drone I a IV** | Repara tu casco: 1,5 %, 2,25 %, 3,5 % y 5 % del máximo por segundo | ilimitados | 5000 / 15.000 / 35.000 créditos, 2000 Thulium |
| **Cloaking CPU S** | Oculta tu nave | 10 | 5000 Thulium |
| **Cloaking CPU M** | Oculta tu nave | 25 | 11.250 Thulium |
| **Cloaking CPU L** | Oculta tu nave | 50 | 20.000 Thulium |
| **P.E.T. Station I a III** | En ON, deja que 2, 3 o 5 [P.E.T.s](/wiki/03-Mechanics/Pets.md#the-station) acoplados den bonificaciones a tu nave, ganen experiencia y trabajen; en OFF, no hacen nada de eso | ON / OFF | Ensamblaje, tras su investigación (el árbol de objetos de abajo) |
| **Auto-Rocket CPU** | En ON, lanza sola tu cohete activo contra el objetivo de un combate | ON / OFF | Ensamblaje, tras su investigación (el árbol de objetos de abajo) |

Las Cloaking CPU se venden solo en la tienda. No se pueden fusionar y nada las regala. La **EMP Charge** ya no es un extra: desde la 0.4.21 es un consumible que se lleva en una pila, como un cohete, y no se equipa en ninguna ranura, así que no ocupa ninguna de tus ranuras de extra (consulta [Cohetes](/wiki/06-Items/Rockets.md#emp-charge)). Las dos **Energetic Wall** tampoco son ya extras: desde la 0.4.22 también son consumibles, se llevan en una pila y no van en ninguna ranura (consulta [Energetic Wall](#energetic-wall)).

El **equipo inicial** de un piloto nuevo ya instala dos extras en las dos ranuras de extra de la Protos: una **Base CPU I** (10 usos, un teletransporte a la base de tu corporación) y un **Repair Drone I**. Arrástralos desde el selector de Extras de la barra rápida a una ranura para usarlos. Solo los pilotos nuevos reciben el equipo: quien se alistó antes de la 0.4.10 no lo tiene.

Otras ocho CPU no se venden: Ensamblaje las fabrica cuando el Centro de investigación del Skylab las ha investigado (consulta [Investigación](/wiki/03-Mechanics/Research.md)). Son la Extra Slots CPU I, II y III, la Jump CPU, la Base CPU I y II, la Auto-Repair CPU y la Auto-Rocket CPU, y [la última sección](#research-cpus) cuenta qué hace cada una. Como la Cloaking CPU, la Jump CPU y las Base CPU son para un momento tranquilo: ninguna de las tres arranca dentro de los 10 segundos posteriores a un disparo tuyo o a un impacto que recibas. Las dos CPU de warp, la Jump CPU y las Base CPU, también se rechazan mientras llevas un objeto de misión («No puedes usar un CPU de warp mientras llevas un objeto de misión.»): consulta [Objetos de misión](/wiki/03-Mechanics/Quests.md#quest-items).

Cada extra tiene una etiqueta corta en su ranura de la barra rápida: **REP** para un Repair Drone, **CLK** para una Cloaking CPU y **ARP**, **ARL**, **BSE** y **JMP** para la Auto-Repair CPU, la Auto-Rocket CPU, la Base CPU y la Jump CPU. Los consumibles tienen las suyas: **EMP** y **WAL** (para una Energetic Wall). Los tres objetos **P.E.T. Station** son extras como los demás, con la etiqueta **PET**: equipa uno y su ranura pone la Station en **ON** u **OFF** (un segundo entre dos pulsaciones) y muestra cuál. En ON cuentan los [P.E.T.s](/wiki/03-Mechanics/Pets.md) acoplados; en OFF, no. La **Auto-Rocket CPU** se activa del mismo modo, en ON u OFF. Apunta a una ranura para leer qué hace ahora una pulsación, o por qué no puede.

![The Extras picker of the hotbar: the Repair Drone, the Auto-Repair, Cloaking, Base and Jump CPUs and the P.E.T. Station you have fitted (REP, ARP, CLK, BSE, JMP, PET), to drag onto a slot](../../img/wiki-img/shots/cpu-hotbar.jpg)
![The Consumables picker of the hotbar: the EMP Charge and the Energetic Wall I and II (EMP, WAL) to drag onto a slot, with how many of each you hold](../../img/wiki-img/shots/emp-hotbar.jpg)
![The hotbar with extras on its slots: a Repair Drone, a Cloaking CPU with its uses left, the P.E.T. Station that says ON, the EMP Charge and the Energetic Wall I and II with the number of each you carry](../../img/wiki-img/shots/hotbar-slots.jpg)
![The Repair Drone of an extra slot docked to its ship and its wingmen](../../img/wiki-img/shots/repair-drones-extra.jpg)
![The Shop's Consumables category: the EMP Charge and the Energetic Wall I with their prices in Thulium, and the Energetic Wall II, which only Assembly makes](../../img/wiki-img/shots/shop-consumables.jpg)

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Árbol de objetos {#item-tree}

Lo que fabrica Ensamblaje necesita antes su tecnología; pasa el cursor por un objeto para ver cuánto tarda en investigarse. El árbol de tecnologías, el combustible y el impulso: [Investigación](/wiki/03-Mechanics/Research.md).

```tree
P.E.T. Station I | extra, common | craft 100000 Credits, 2000 Thulium, 300 s | research 10800 s, 10800 science | 25 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md
Cloaking CPU S | extra, common | buy 5000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Repair Drone I | extra, common | buy 5000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone II | extra, common | buy 15000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone III | extra, common | buy 35000 Credits | /wiki/06-Items/Extras.md#repair-drones
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
P.E.T. Station II | extra, uncommon | craft 400000 Credits, 6000 Thulium, 600 s | research 36000 s, 36000 science | 60 Ship Fragment, 6 Reinforced Hull Plate, 4 Power Core, 8 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md
Cloaking CPU M | extra, uncommon | buy 11250 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 2 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Extras.md#base-cpus
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu
P.E.T. Station III | extra, rare | craft 1500000 Credits, 18000 Thulium, 900 s | research 86400 s, 86400 science | 120 Ship Fragment, 12 Reinforced Hull Plate, 8 Power Core, 2 Ancient Control Unit, 12 Velkonite Reinforced Plate, 4 Orvium Reinforced Plate | /wiki/06-Items/Extras.md
Auto-Rocket CPU | extra, rare | craft 20000 Thulium, 900 s | research 36000 s, 36000 science | 100 Ship Fragment, 10 Reinforced Hull Plate, 5 Power Core, 1 Ancient Control Unit, 8 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-rocket-cpu
Repair Drone IV | extra, rare | buy 2000 Thulium | /wiki/06-Items/Extras.md#repair-drones
Cloaking CPU L | extra, rare | buy 20000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 6 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu

P.E.T. Station I -> P.E.T. Station II -> P.E.T. Station III
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
- **Lo que ves.** Tu nave se vuelve translúcida, con un contorno violeta discontinuo, sus drones se desvanecen con ella, y un indicador en la parte superior de la pantalla dice «Camuflado» con los usos que quedan (sin segundos: no hay temporizador). La ranura CLK muestra los usos restantes; mientras estás camuflado brilla en violeta y dice ON, y cuando el camuflaje termina, sea como sea, se oscurece y cuenta los 60 segundos de recarga. Una pulsación que el servidor rechaza (recarga, zona segura, un impacto o un disparo en los últimos 10 segundos) hace parpadear la ranura en rojo, y un mensaje te dice por qué. Un aliado se muestra como un fantasma pálido con una marca de fantasma antes de su nombre, y un piloto que se camufla cerca de ti se desvanece con una onda. Arrastra CLK desde los Extras de la barra rápida a una ranura para usarlo, como REP.
- **Los usos** se guardan con la CPU. Cerrar sesión, morir o reiniciar el juego no devuelve ninguno, y una activación que cancelas se gasta igualmente. Cuando se acaba el último uso de un paquete, este se consume y su ranura se rellena con una CPU igual de repuesto que tengas en el inventario, si tienes alguna.
- **Varias CPU** en una misma configuración no se suman. Se usa primero la que menos usos tiene.

Las S, M y L se comportan igual: los paquetes más grandes solo salen más baratos por uso (500, 450 y 400 Thulium).

## Energetic Wall

Pulsa la ranura WAL y una **pared de plasma** se alza **en tu cursor**, atravesada a la línea que va de tu nave hasta él: una franja de 360 unidades de largo (unos tres modelos de nave y medio) y 10 unidades de ancho. Su centro queda como mucho a **450 unidades** del centro de la nave: un cursor más lejano la coloca a 450 unidades sobre la línea y uno a menos de 120 unidades la aparta hasta 120. Mientras la ranura está lista, una línea de puntos tenue y un contorno fantasma muestran dónde quedará. Si el juego no sabe dónde está tu cursor, se alza a 220 unidades por delante del centro de la nave, atravesada a su rumbo. Una Energetic Wall es un **consumible**, como la [EMP Charge](/wiki/06-Items/Rockets.md#emp-charge): una pila en tu inventario que no ocupa **ninguna ranura** de ninguna nave (hasta la 0.4.22 era un extra). Arrástrala desde los Consumibles de la barra rápida a una ranura para usarla; los dos niveles son dos entradas, así que una ranura guarda un nivel. Sirve para esconderse detrás y para cortar un pasillo, no para quedarse dentro.

- **Qué detiene.** Todo disparo que la cruza golpea la pared en su lugar, lo haya hecho quien lo haya hecho y desde el lado que sea: una andanada láser, un cohete, la andanada de un alienígena. Lo que está detrás no recibe nada y los puntos de vida de la pared absorben el daño. La explosión de un cohete que estalla en la pared alcanza a las naves de su lado cercano y no a las que están detrás. También tus propios disparos: no puedes disparar hacia fuera a través de tu propia pared. La N.I.K.E. y las torretas del Dormant Swamp pasan por encima, como por encima de los asteroides.
- **Qué quema.** Toda nave cuyo casco toque la franja recibe **2.500 de daño por segundo**, primero en el escudo, también la tuya, también los alienígenas y los pilotos de corporación. Una nave en una zona segura o bajo la protección de una reaparición no se quema, y dos franjas sobre una nave no se suman.
- **Cuánto dura.** Una pared de nivel 1 tiene **30.000 puntos de vida** y una de nivel 2, **90.000**. Una pared pierde por sí sola una sexagésima parte cada segundo, así que una a la que nadie dispara desaparece a los **60 segundos**. Los disparos lo acortan: una Wraith con doce Helios Beam y munición x4 derriba una pared de nivel 1 en unos 3,5 segundos.
- **Una a la vez, una pared por pulsación.** Una pared nueva ocupa el lugar de la anterior. Tras pulsar, el objeto se recarga durante **90 segundos**; la espera es tuya, no de la nave: morir o desconectarse no la acorta. Una pulsación gasta **una pared del nivel que guarda su ranura**, y solo cuando la pared se alza: una pulsación que el juego rechaza (más abajo) no gasta nada ni inicia ninguna espera. Si no queda ninguna de ese nivel, dice «Ya no te quedan Energetic Wall.» y el otro nivel nunca se gasta en su lugar.
- **Dónde no.** No mientras te proteja una zona segura o una reaparición, no donde la franja tocaría una zona segura o una puerta, no camuflado y no donde el centro de la franja quedaría fuera del mapa. El juego dice cuál es el caso.
- **Bajas.** Una nave que destruye la pared muere por radiación, y la baja es del último piloto enemigo que la golpeó en los últimos 15 segundos, si lo hubo. Quien puso la pared no recibe crédito por nada que no disparara él mismo. Un alienígena que la pared destruye no paga nada: ni recompensa ni botín.
- **Los alienígenas no la rodean.** La atraviesan y se queman, o se quedan en su lado y disparan a la pared.
- **Qué ves.** Una franja de luz blanquiazul con rayas brillantes que corren por ella y un poste de luz en cada extremo, que destella donde cae un disparo y parpadea cuando casi se ha agotado. Una pared de nivel 2 brilla en amarillo, con un núcleo más grueso y brillante y un resplandor más fuerte, pero su franja tiene las mismas 10 unidades de ancho que la de nivel 1. Una barra de vida fina junto a ella se acorta y pasa a ámbar y luego a rojo; tu ranura muestra la vida que le queda a tu pared como arco y la espera como sombra. Una pared recién puesta destella al encenderse, una derribada se desmorona en chispas y una a la que se le acabó el tiempo se desvanece. En tu ranura, además, un número cuenta las paredes de su nivel que te quedan.
- **Cómo conseguirla y llevarla.** La Energetic Wall I se vende en la tienda por **250 Thulium** la pared, y llevas hasta **20** en una pila (lo que tienes puesto en la [Subasta](/wiki/03-Mechanics/Auction.md) cuenta). La Energetic Wall II se hace en el Ensamblaje, **una pared por fabricación**, por **600 Thulium**, 5 Ship Fragments y un Power Core, cuando el Centro de investigación la ha investigado (6 horas a velocidad normal: [Investigación](/wiki/03-Mechanics/Research.md)); llevas hasta **10**. Como los cohetes, las paredes que llevas se pierden con la temporada si no las pones en el Alijo de Transporte, y las del Alijo no se pueden usar. Una Energetic Wall II que hayas hecho se puede vender en la Subasta; una Energetic Wall I, que vende la tienda, nunca.

## CPU del Centro de investigación {#research-cpus}

Dos de las CPU piden Dark Matter Plates, como el último nivel de cada cadena de mejora: **Extra Slots CPU III** pide 4 (más 2 Ancient Control Units y 6 Orvium Reinforced Plates) y **Base CPU II** pide 4 (más una Ancient Control Unit y 2 Orvium Reinforced Plates), así que investiga antes la Dark Matter Plate ([Dark Matter y Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)).

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | Tiempo de investigación | Necesita antes | Thulium para fabricar | Tiempo de fabricación |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 min | – | 12.000 | 5 min |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10 h | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30.000 | 10 min |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1 d | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75.000 | 15 min |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3 h | – | 8.000 | 5 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10 h | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | 20.000 | 10 min |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1 d | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40.000 | 15 min |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6 h | – | 15.000 | 10 min |
| [Energetic Wall II](/wiki/06-Items/Extras.md#energetic-wall) | 6 h | – | 600 | 2 min |
| [Auto-Rocket CPU](/wiki/06-Items/Extras.md#auto-rocket-cpu) | 10 h | – | 20.000 | 15 min |

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

### Auto-Rocket CPU

- **Qué hace.** Mientras esté en ON y estés en un combate (tus láseres apuntan a un alienígena o a un piloto enemigo), lanza por sí sola tu cohete activo, el último que lanzaste, contra ese objetivo, siempre que una pulsación de la tecla Disparar cohete funcionaría: el temporizador de los cohetes está listo y te queda uno. El servidor comprueba cada lanzamiento como comprueba los tuyos.
- **El interruptor.** Equípala en una ranura de Extras y pulsa su ranura ARL para ponerla en ON u OFF. Empieza en OFF y se queda como la dejaste, también cuando vuelves a iniciar sesión. La ranura dice ON u OFF y brilla cuando la CPU lanza.
- **Lo que nunca hace.** Nunca elige un objetivo, nunca lanza contra asteroides, ni desde una zona segura, ni mientras estás camuflado, y nunca lanza una N.U.K.E. ni una N.I.K.E. Un cohete que lances tú siempre funciona. Si pasan 3 minutos sin pulsar una tecla, hacer clic ni mover el ratón, espera a que hagas algo.
- **Sin cohetes.** Te avisa una vez y vuelve a lanzar en cuanto tengas más.


<!-- research-cpus:end -->
