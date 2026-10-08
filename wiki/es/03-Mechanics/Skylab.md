<!-- wiki-i18n source: d06e4b2673a5b545 -->
<!-- wiki-i18n title: Skylab -->
# Skylab

El Skylab es tu instalación orbital personal. Construye y mejora módulos que producen créditos y Thulium, extraen mineral, forjan las placas que el Ensamblaje convierte en los mejores láseres y, desde el nivel 10 del Núcleo, investigan las tecnologías que necesita el Ensamblaje. Trabaja para ti incluso cuando no estás conectado.

En el nivel 10 del Núcleo, el Skylab además crece: un **puente** une el Núcleo con un segundo Núcleo de seis ranuras más para módulos, y a él se acoplan dos módulos más, la **Impresora de munición** y la **Fábrica de cohetes**, que fabrican munición y cohetes de la nada (consulta [El puente y el Núcleo 2](#the-bridge-and-core-2)).

> [!NOTE]
> **Qué cambió en 0.4.10.** Cada módulo del Skylab tiene ahora su propia tabla de producción, precios y tiempos, nivel por nivel. Conservaste tus niveles: no se cobró nada ni se devolvió nada por la diferencia. Lo que tus granjas y colectores tenían en sus tolvas cuando llegó la actualización se pagó **una sola vez, a la tarifa antigua**: los créditos y el Thulium fueron a tu cuenta, el mineral a tu Almacén de recursos, y las tolvas empezaron de nuevo vacías.
>
> Hay dos reglas nuevas. **Solar produce solo el 25 % de su energía mientras se mejora**, así que en la mayoría de las estaciones todas las granjas y colectores se detienen hasta que termina la mejora (consulta el [módulo Solar](#solar-module) y [Cómo planificar una mejora de Solar](#timing-a-solar-upgrade)). **El Almacén de recursos tiene un límite propio para cada mineral**: un día de la producción del colector en el nivel 1, cuatro días en el nivel 20.

> [!NOTE]
> **Qué cambió en 0.4.15.** El paso del Núcleo del nivel 9 al nivel 10 cuesta ahora **2.000 de Thulium** más, y cuando termina aparecen un **puente** y un segundo Núcleo, el **Núcleo 2**, con seis ranuras nuevas para módulos. Solar se traslada al Núcleo 2. A él se acoplan dos módulos nuevos: la **Impresora de munición** y la **Fábrica de cohetes**. Además, Solar produce más energía desde el nivel 7, para que una estación completa siga cubierta. No pierdes nada de lo que construiste: un Núcleo que ya está en el nivel 10 o más tiene el puente enseguida y no paga nada.

![The Skylab station fully grown](../../img/wiki-img/shots/skylab-station.jpg)
![The Resource Storage card of the Skylab](../../img/wiki-img/shots/skylab-storage.jpg)
![The Skylab table of modules: level, production, storage and power of every module, with the 0.4.10 numbers](../../img/wiki-img/shots/skylab-table.jpg)

## En un minuto {#in-one-minute}

- Construye primero **Solar**: sin su energía, nada en el Skylab funciona. La Granja de créditos no cuesta nada construirla, y la Granja de Thulium cuesta 5.000 créditos y 500 Thulium.
- Las granjas y los colectores llenan una **tolva** (de 72 horas) mientras estás fuera. **Recoger** la pasa a tu cuenta (créditos, Thulium) o a tu Almacén de recursos (mineral).
- La **Granja de Thulium** es tu principal fuente de Thulium: 50 por hora en el nivel 1, 1.600 en el nivel 20. La Granja de créditos produce 500 créditos por hora en el nivel 1 y 50.000 en el nivel 20.
- El **Núcleo** marca el ritmo: ningún módulo pasa de él, y su propia subida dura unos 16 días y medio.
- En el **nivel 10 del Núcleo**, un **puente** construye el **Núcleo 2**, con seis ranuras más para módulos, y la **Impresora de munición** y la **Fábrica de cohetes** se acoplan a él. El paso al nivel 10 cuesta 2.000 de Thulium más.
- **Solar produce solo el 25 % de su energía mientras se mejora**, así que tus granjas y colectores se detienen hasta que termina. [Planifícalo](#timing-a-solar-upgrade).

## Resumen {#overview}

El Skylab funciona con su propio reloj, aparte de tu nave: los módulos producen y forjan mientras estás fuera. Lo que haces tú es construir, mejorar, mantener la energía en equilibrio y recoger. La página tiene cuatro vistas de la misma estación: **Estación** (la estación en 3D, con un chip sobre cada módulo; haz clic en uno para abrir su ficha, o pulsa del **1** al **9**), **Lista** (una tarjeta por módulo), **Tabla** (las cifras de todos los módulos en una sola tabla) e **Investigación** (la pantalla propia del Centro de investigación, consulta [Investigación](/wiki/03-Mechanics/Research.md)). Al pasar el cursor por **Construir** o **Mejorar** se ve lo que cambia el siguiente nivel, lo que cuesta y cuánto tarda.

Once módulos forman la estación:

| Módulo | Qué produce o hace | Se construye desde |
| :--- | :--- | :--- |
| **Núcleo** | Fija el nivel máximo de todos los demás módulos | Siempre presente |
| **Solar** | Produce energía | Cualquier nivel del Núcleo |
| **Granja de créditos** | Produce [créditos](/wiki/01-General/Getting-Started.md) | Cualquier nivel del Núcleo |
| **Granja de Thulium** | Produce [Thulium](/wiki/01-General/Getting-Started.md) | Cualquier nivel del Núcleo |
| **Colector de Velkonite** | Extrae mineral de Velkonite | Núcleo de nivel 5 |
| **Colector de Orvium** | Extrae mineral de Orvium | Núcleo de nivel 5 |
| **Almacén de recursos** | Guarda el mineral | Núcleo de nivel 5 |
| **Forja** | Forja el mineral en placas | Núcleo de nivel 5 |
| **Centro de investigación** | Convierte recursos en ciencia e investiga [tecnologías](/wiki/03-Mechanics/Research.md) | Núcleo de nivel 10 |
| **Impresora de munición** | Imprime munición x2, x3 o x4 de la nada | Núcleo de nivel 10, en el Núcleo 2 |
| **Fábrica de cohetes** | Fabrica cohetes de la tienda de la nada | Núcleo de nivel 10, en el Núcleo 2 |

El **puente** y el **Núcleo 2** no son módulos: aparecen cuando el Núcleo llega al nivel 10, y el Núcleo 2 no tiene nivel propio (consulta [El puente y el Núcleo 2](#the-bridge-and-core-2)).

**Misiones para el Skylab.** Diez [misiones de la estación](/wiki/03-Mechanics/Quests.md#station-missions) en Mission Control te guían por el Skylab: construir Solar, una Granja de créditos y una Granja de Thulium, subir el Núcleo y Solar, recoger tus primeros 50.000 créditos y abrir la cadena de suministro, y pagan un poco por cada paso. La primera está abierta desde el nivel 1.

## La estación en cada nivel {#the-station-at-every-level}

Esta es la vista Estación del Skylab en cada nivel del 1 al 20, todas desde el mismo ángulo, con todos los módulos en el mismo nivel. La vista encaja toda la estación en la imagen, así que la escala no es la misma en todas: salta cuando la forma crece. La estación crece por etapas: su forma cambia en los **niveles 1, 5, 10, 15 y 20**, y entre medias cada nivel enciende **una luz más** en el collar de cada módulo (el número de luces encendidas es el nivel, y el anillo de veinte luces del Núcleo se llena del mismo modo).

Las imágenes desde el nivel 10 muestran la estación como era antes del puente: desde la 0.4.15, el paso del Núcleo al nivel 10 construye además el puente y el Núcleo 2, y Solar está en el Núcleo 2 (consulta [El puente y el Núcleo 2](#the-bridge-and-core-2)).

**Niveles 1 a 4.** Los cuatro primeros módulos alrededor del Núcleo: Solar, la Granja de créditos, la Granja de Thulium y la bahía de atraque que aloja tu nave. La cadena de suministro todavía no se puede construir.

![Nivel 1](../../img/skylab/wiki/level-01.jpg)
![Nivel 2](../../img/skylab/wiki/level-02.jpg)
![Nivel 3](../../img/skylab/wiki/level-03.jpg)
![Nivel 4](../../img/skylab/wiki/level-04.jpg)

**Niveles 5 a 9.** Con el Núcleo en el nivel 5 se puede construir la cadena de suministro: los dos colectores en sus estructuras sobre la estación, el Almacén de recursos en el puerto noreste del Núcleo y la Forja en su puerto noroeste (aquí se muestran ya construidos).

![Nivel 5](../../img/skylab/wiki/level-05.jpg)
![Nivel 6](../../img/skylab/wiki/level-06.jpg)
![Nivel 7](../../img/skylab/wiki/level-07.jpg)
![Nivel 8](../../img/skylab/wiki/level-08.jpg)
![Nivel 9](../../img/skylab/wiki/level-09.jpg)

**Niveles 10 a 14.** El Núcleo luce su anillo, las granjas y los colectores adoptan su forma más grande y la Granja de Thulium recibe su propio anillo.

![Nivel 10](../../img/skylab/wiki/level-10.jpg)
![Nivel 11](../../img/skylab/wiki/level-11.jpg)
![Nivel 12](../../img/skylab/wiki/level-12.jpg)
![Nivel 13](../../img/skylab/wiki/level-13.jpg)
![Nivel 14](../../img/skylab/wiki/level-14.jpg)

**Niveles 15 a 19.** Las granjas se llenan de cajas y cristales, la bahía de atraque ilumina su aproximación y la matriz Solar le crece la parte superior.

![Nivel 15](../../img/skylab/wiki/level-15.jpg)
![Nivel 16](../../img/skylab/wiki/level-16.jpg)
![Nivel 17](../../img/skylab/wiki/level-17.jpg)
![Nivel 18](../../img/skylab/wiki/level-18.jpg)
![Nivel 19](../../img/skylab/wiki/level-19.jpg)

**Nivel 20.** La cima de la escalera: la corona del Núcleo y las torres plenamente desarrolladas de las granjas y la cadena de suministro.

![Nivel 20](../../img/skylab/wiki/level-20.jpg)

**Las tarjetas de los nueve módulos.** La vista Lista de la misma estación en el nivel 20: los cuatro módulos de la primera versión, el Colector de Velkonite, el Colector de Orvium, el Almacén de recursos y la Forja que llegaron con la cadena de suministro, y el Centro de investigación. Cada tarjeta muestra el nivel del módulo, su producción, su energía y su interruptor. Todas las tarjetas marcan el nivel 20 salvo la del Centro de investigación: tiene los niveles 1 a 10, así que su tarjeta marca el nivel 10, el máximo. La Impresora de munición y la Fábrica de cohetes tienen sus propias fichas en la misma vista; se describen [más abajo](#the-bridge-and-core-2).

![La vista Lista en el nivel 20: las tarjetas del Núcleo, Solar, la Granja de créditos, la Granja de Thulium, el Colector de Velkonite, el Colector de Orvium, el Almacén de recursos, la Forja y el Centro de investigación](../../img/skylab/wiki/modules.jpg)

## Los cuatro primeros módulos {#the-first-four-modules}

### Módulo Núcleo {#core-module}

El corazón de tu Skylab. El nivel del Núcleo decide el nivel máximo de todos los demás módulos: no puedes mejorar ningún módulo por encima de tu Núcleo. El Núcleo llega hasta el nivel 20 y, desde el **nivel 5**, abre la cadena de suministro que se describe más abajo. Sus mejoras cuestan créditos, y el paso al **nivel 10** cuesta **2.000 de Thulium** más y construye el puente y el Núcleo 2 (consulta [El puente y el Núcleo 2](#the-bridge-and-core-2)). En total son 112.326 créditos hasta el nivel 10 y 6.647.504 hasta el nivel 20, más esos 2.000 de Thulium, y duran unos 16 días y medio (consulta [Tiempos de mejora](#upgrade-times)).

### Módulo Solar {#solar-module}

La energía es el alma del Skylab. El módulo Solar produce la energía que usan todos los demás módulos.

- **Importancia**: si tu consumo de energía es mayor que la energía que produces, tus granjas y colectores se apagan.
- **Energía producida**: un módulo Solar de nivel N produce lo suficiente para **todos los demás módulos en el nivel N**, y alrededor de una décima parte más: 255 en el nivel 1, 965 en el nivel 7, 17.890 en el nivel 20. Solar de nivel 7 alimenta una estación entera en el nivel 7 (consulta Gestión de la energía para ver todos los niveles).
- **Precio**: construir Solar cuesta **500 créditos y 50 Thulium**. Sus mejoras cuestan lo mismo y duran lo mismo que las de la Forja: desde 8.000 créditos y 25 Thulium para el nivel 2 (5 minutos) hasta 9.000.000 de créditos y 10.000 Thulium para el nivel 20 (24 horas).
- **Mejora**: mientras se mejora, Solar produce solo el **25 %** de la energía de su nivel actual, y la del nivel nuevo desde que termina la mejora. Una estación que consume más que eso se detiene: todas las granjas y colectores dejan de producir y la Forja no empieza ningún lote nuevo hasta que termina la mejora. En casi todas las estaciones ocurre así: solo sigue funcionando durante la mejora si todos los demás módulos están al menos cinco niveles por debajo de Solar (seis niveles desde el nivel 10 de Solar). Planifica una mejora de Solar como un apagón de tus granjas (consulta Construcción y mejora).
- **Lugar**: desde el nivel 10 del Núcleo, Solar está en el Núcleo 2, en el extremo lejano de la estación (consulta [El puente y el Núcleo 2](#the-bridge-and-core-2)).

### Granja de créditos y Granja de Thulium {#credit-farm-and-thulium-farm}

- **Granja de créditos**: produce créditos con el tiempo: **500 por hora en el nivel 1, 50.000 en el nivel 20** (nivel 5: 2.500; nivel 10: 7.500; nivel 15: 17.000). Construirla no cuesta nada.
- **Granja de Thulium**: produce Thulium con el tiempo: **50 por hora en el nivel 1, 1.600 en el nivel 20** (nivel 5: 180; nivel 10: 450; nivel 15: 950). Construirla cuesta 5.000 créditos y 500 Thulium.
- Ambas necesitan energía, y cada una almacena 72 horas de lo que produce hasta que lo recoges.

## La cadena de suministro {#the-supply-chain}

Cuatro módulos convierten el tiempo que pasas lejos del teclado en las placas para tus mejores láseres. El mineral proviene **únicamente** de los colectores (todos los materiales y monedas están en la página [Recursos](/wiki/06-Items/Resources.md)): los alienígenas no lo sueltan y la tienda no lo vende.

1. Un **colector** extrae mineral, una cantidad por hora, en su propia tolva (72 horas de producción).
2. **Recoger** pasa el mineral de la tolva al **Almacén de recursos**, la reserva, donde cada mineral se guarda por separado.
3. La **Forja** toma de la reserva el mineral que necesita cuando empieza un lote y hace placas, a 10 segundos por placa, un lote a la vez.
4. **Recoger placas** pasa las placas terminadas a tu inventario (tu nave debe estar aterrizada). El [Ensamblaje](/wiki/06-Items/Lasers.md) las convierte en un Quantum Laser III, un Starfire-III o un Helios Beam y, una de cada con 5 Dark Matter, en una Dark Matter Plate, que piden [la Forja de Ensamblaje](/wiki/06-Items/Forge.md) y el último nivel de cada cadena de mejora.

### Colector de Velkonite y Colector de Orvium {#velkonite-collector-and-orvium-collector}

- **Mineral**: el Colector de Velkonite extrae **10 Velkonite por hora** en el nivel 1 y el Colector de Orvium **10 Orvium por hora**, y cada nivel tiene su propio ritmo: hasta 80 Velkonite y 40 Orvium por hora en el nivel 20 (nivel 5: 18 y 14 por hora; nivel 10: 32 y 24).
- **Tolva**: cada uno almacena 72 horas de su mineral y deja de extraer cuando se llena.
- **Recoger**: pasa el mineral al Almacén de recursos, hasta donde haya sitio. Sin almacén construido, o con la reserva de ese mineral llena, no hay dónde ponerlo y el botón dice por qué. El resto se queda en la tolva.
- **Energía**: 20 (Velkonite) y 30 (Orvium) en el nivel 1, con un aumento del 15 % por nivel.

### Almacén de recursos {#resource-storage}

- **Reserva**: guarda el Velkonite y el Orvium por separado y almacena una cantidad distinta de cada uno: **240 de cada uno en el nivel 1**, hasta 7.680 de Velkonite y 3.840 de Orvium en el nivel 20 (nivel 5: 720 y 560; nivel 10: 1.920 y 1.440).
- **Límite**: un día de la producción de su colector en el nivel 1, hasta cuatro días en el nivel 20. La tolva de un colector guarda tres días, así que desde el nivel 13 la reserva guarda al menos una tolva llena.
- **Por encima del límite**: si una reserva guarda más que su límite (el pago de la actualización 0.4.10 pudo dejarla así), no se quita nada, pero Recoger no añade más de ese mineral hasta que hayas gastado algo.
- El mineral entra solo al recoger de un colector y sale solo hacia la Forja. Nunca llega a tu inventario.
- **El mineral guardado se conserva** tras el reinicio de la temporada.
- **Energía**: 10 en el nivel 1, con un aumento del 10 % por nivel. No se puede apagar.

### Forja {#forgery}

- **Placas**: la Forja hace una **Velkonite Reinforced Plate** a partir de Velkonite y una **Orvium Reinforced Plate** a partir de Orvium: **40 Velkonite** u **80 Orvium** por placa en el nivel 1, y baja con cada nivel hasta 30 y 60 en el nivel 20 (nunca por debajo del 75 %).
- **Lotes**: un lote de un solo tipo de placa a la vez, de **10 placas en el nivel 1** y 5 más por cada nivel superior. El mineral sale del Almacén de recursos en el momento en que empieza el lote, y cada placa tarda **10 segundos**. Las placas se hacen una tras otra, también mientras estás fuera.
- **Recoger placas**: pasa las placas terminadas a tu inventario mientras tu **nave está aterrizada**, y el resto del lote sigue en marcha. Se puede empezar un lote nuevo cuando la Forja está vacía.
- Un lote en marcha termina aunque apagues la Forja o la mejores. Un lote **nuevo** necesita que la Forja esté encendida, que no se esté mejorando y que la energía del Skylab esté en equilibrio.
- **Energía**: 30 en el nivel 1, con un aumento del 15 % por nivel.
- **No comercializable**: las placas que fabrica la Forja no se pueden vender en la [Subasta](/wiki/03-Mechanics/Auction.md#marketable-items); si no, serían el mayor producto de su Mercado. Siguen sirviendo como material para el Ensamblaje y la Forja.

### Construirlos {#building-them}

Los dos colectores cuestan **10 Ship Fragments, 20.000 créditos y 500 de Thulium** cada uno, el Almacén de recursos **10 Ship Fragments, 5.000 créditos y 250 de Thulium** y la Forja **10 Ship Fragments, 5.000 créditos y 500 de Thulium**; los cuatro necesitan el Núcleo en el nivel 5.

- Los Ship Fragments se toman de tu inventario (no del Alijo de Transporte) y tu nave debe estar aterrizada. La ficha de construcción muestra lo que tienes frente a lo que hace falta, y lo que te falta.
- Consumen energía. Antes de construir, la ficha muestra tu balance de energía ahora y después: **construir puede dejar una estación en déficit** cuando su Solar va por detrás de los demás módulos, y un déficit detiene todas las granjas y colectores. Apaga un módulo o mejora primero Solar.
- Los dos colectores cuelgan de estructuras sobre la estación, el Almacén de recursos está en el puerto noreste del Núcleo y la Forja en su puerto noroeste.

## El Centro de investigación {#the-research-centre}

El noveno módulo convierte recursos en ciencia e investiga las tecnologías que Ensamblaje necesita antes de fabricar nada nuevo. Se construye desde el nivel 10 del Núcleo, tiene los niveles 1 a 10, consume energía y no se puede apagar. Sus números, lo que quema como combustible, el impulso y el árbol de tecnologías completo están en la página de [Investigación](/wiki/03-Mechanics/Research.md). Las tecnologías más altas necesitan además Dark Matter, que añades al Centro: [Dark Matter y Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md) explica cómo conseguirlo.

## El puente y el Núcleo 2 {#the-bridge-and-core-2}

La mejora del Núcleo al **nivel 10** construye un **puente** y un segundo Núcleo. El puente se acopla al puerto norte del Núcleo, donde estaba Solar, y lo une en el extremo lejano con el **Núcleo 2**.

- **Coste**: el paso del nivel 9 al nivel 10 cuesta **2.000 de Thulium** además de sus 38.443 créditos, y dura lo mismo que antes, 1 h 20 min. El puente y el Núcleo 2 no cuestan nada más y no tardan tiempo propio. Una mejora que ya estaba en marcha conserva el precio con el que empezó, y un Núcleo en el nivel 10 o más no paga nada.
- **El Núcleo 2 no tiene nivel**: no hay nada que mejorar ni que pagar. Da a tu estación **seis ranuras más para módulos**, y la ficha del Núcleo muestra cuántas están libres.
- **Solar se traslada**: Solar deja el puerto norte del Núcleo, que ahora ocupa el puente, y pasa al puerto norte del Núcleo 2, en el extremo lejano de la estación. Su nivel, su energía y una mejora en curso quedan intactos.
- **Una regla, no una obra**: dónde está cada módulo depende solo del nivel del Núcleo. El puente aparece en el momento en que termina la mejora del Núcleo al nivel 10 (un sonido suave y un mensaje te lo dicen), y un Skylab cuyo Núcleo ya está en el nivel 10 o más lo tiene en la siguiente visita. No se pierde ni se borra ningún módulo, y solo Solar cambia de sitio.
- **Ranuras**: la **Impresora de munición** ocupa la ranura noreste del Núcleo 2 y la **Fábrica de cohetes** la noroeste; las otras cuatro quedan libres para módulos futuros. Ambas solo se pueden construir cuando el Núcleo 2 ya existe: antes, el botón de construir dice «Requiere Núcleo 2».
- **Niveles**: un módulo del Núcleo 2 sigue el nivel del Núcleo como cualquier otro módulo: ninguno pasa del Núcleo, así que el Núcleo 2 añade ranuras, no niveles.

### Impresora de munición {#ammo-printer}

La Impresora de munición imprime munición láser de la nada, de un tipo cada vez: sin mineral y sin créditos, solo energía. Tiene los niveles 1 a 20.

- **Producción**: **x2** (Advanced Plasma) **100 por hora en el nivel 1, 2.000 en el nivel 20** (100 más por cada nivel); **x3** (Ultra Core) la mitad, de 50 a 1.000; **x4** (Experimental Fusion Core) una cuarta parte, de 25 a 500.
- **Modo**: eliges x2, x3 o x4 en su ficha o su ventana. Un cambio conserva las horas ya almacenadas y las cuenta desde entonces a la tasa del nuevo modo.
- **Almacenamiento**: un día, 24 horas de producción al nivel y en el tipo que estén en uso (2.400 de x2 en el nivel 1, 48.000 en el nivel 20). El tiempo sin conexión cuenta, y un almacén lleno simplemente se detiene.
- **Recoger**: pasa las unidades enteras a tu inventario mientras tu **nave está aterrizada**. La munición no tiene límite de carga, y la parte de una unidad se queda y sigue contando.
- **Energía**: 40 en el nivel 1, con un aumento del 20 % por nivel. Con un déficit de energía se detiene como las granjas y los colectores, y lo que guarda se queda y se puede recoger.
- **Construcción**: 20.000 créditos, 500 de Thulium y 10 Ship Fragments (de tu inventario, con la nave aterrizada), solo en el Núcleo 2. Sus mejoras cuestan desde 21.000 créditos y 140 de Thulium hasta 5.600.000 créditos y 11.000 de Thulium, y duran lo mismo que las de la Forja, de 5 minutos a 24 horas y 5 d 13 h en total (consulta las tablas de más abajo).
- **No comercializable**: lo que imprime no se puede vender en la [Subasta](/wiki/03-Mechanics/Auction.md#marketable-items).

### Fábrica de cohetes {#rocket-factory}

La Fábrica de cohetes fabrica cohetes de la tienda de la nada, de un tipo cada vez. Tiene los niveles 1 a 20.

- **Qué fabrica**: uno solo de los doce cohetes de la tienda, el que elijas: Lancet, Rivet, Scatter o Ember, gamas I, II y III. El N.U.K.E. y el N.I.K.E. no se fabrican nunca.
- **Producción**: la gama III **0,5 por hora en el nivel 1, 10 en el nivel 20** (0,5 más por cada nivel), la gama II 1,25 veces eso y la gama I el doble. Solo cuentan los cohetes enteros: la parte de uno se queda y sigue contando.
- **Almacenamiento**: un día, 24 horas de producción al nivel y con el cohete en uso (240 de la gama III en el nivel 20). El tiempo sin conexión cuenta, un almacén lleno simplemente se detiene, y un cambio de cohete conserva las horas ya almacenadas.
- **Recoger**: pasa los cohetes a tu inventario mientras tu **nave está aterrizada**, tantos como puedas llevar: como máximo 5.000 de la gama I, 2.000 de la gama II y 500 de la gama III, el límite de la propia tienda. Lo que no cabe se queda en la fábrica.
- **Energía**: 24 en el nivel 1, con un aumento del 15 % por nivel. Con un déficit de energía se detiene como la impresora.
- **Construcción**: 20.000 créditos, 500 de Thulium y 15 Ship Fragments (de tu inventario, con la nave aterrizada), solo en el Núcleo 2. Sus mejoras cuestan una cuarta parte de las de la impresora, desde 5.300 créditos y 35 de Thulium hasta 1.400.000 créditos y 2.800 de Thulium, y duran lo mismo: 5 d 13 h en total.
- **No comercializable**: lo que fabrica no se puede vender en la [Subasta](/wiki/03-Mechanics/Auction.md#marketable-items).

## Mecánicas {#mechanics}

### Construcción y mejora {#building-and-upgrading}

- **Construcción**: cada módulo se construye por separado. Un módulo está en el nivel 1 en el momento en que se construye, y mejorarlo aumenta su producción (o la energía que produce) y su almacenamiento, y también lo que consume de energía.
- **Tiempo y costo**: las mejoras cuestan créditos y Thulium y llevan tiempo, y cada módulo tiene su propio precio y tiempo para cada nivel (pasa el cursor por **Mejorar** para ver el siguiente; los totales están más abajo). El precio se paga al empezar la mejora. El costo no depende del tiempo.
- **Temporizadores**: una mejora funciona con el reloj del servidor, así que termina mientras estás fuera, días después si hace falta. Empiézala, desconéctate, vuelve: el módulo está en su nuevo nivel cuando abres la página del Skylab.
- **Tiempos de mejora**: los primeros niveles son rápidos y los últimos llevan hasta 36 horas, los del Núcleo hasta 6 días (consulta las tablas de abajo). Cada módulo tiene su propio temporizador, así que puedes mejorar varios a la vez.
- **Pausa de producción**: mientras se mejora un módulo, está desconectado: no produce nada y no consume energía. Solar es la excepción: sigue produciendo una cuarta parte de su energía (consulta más abajo).
- **Solar produce solo el 25 % de su energía mientras se mejora**: Solar produce toda la energía del Skylab y, mientras se mejora (24 horas para el último nivel), produce una cuarta parte de la energía de su nivel **actual**; la del nivel nuevo toma el relevo en cuanto termina la mejora. Una estación completa consume alrededor del 90 % de lo que Solar produce en su propio nivel, así que una cuarta parte de eso solo sostiene una estación que esté cinco o seis niveles por debajo de Solar. Si no, todas las granjas y colectores se detienen durante toda la mejora, lo que tengas almacenado se conserva y se puede recoger, y la Forja no empieza ningún lote nuevo. Un módulo que se está mejorando o que está apagado no consume energía, así que subir las granjas a la vez que Solar no cuesta nada extra, y apagar módulos deja sitio a los demás; la Granja de Thulium es, con diferencia, la que más energía consume.

### Cuánto cuesta {#what-it-costs}

El precio de toda la subida, la construcción más cada mejora, hasta el nivel 10 y hasta el nivel 20. El Núcleo siempre está ahí y sus pasos cuestan créditos, con 2.000 de Thulium más en el paso al nivel 10; el Centro de investigación tiene los niveles 1 a 10 y sus cifras están en la página [Investigación](/wiki/03-Mechanics/Research.md). La Impresora de munición y la Fábrica de cohetes se construyen en el Núcleo 2, así que solo cuando el Núcleo está en el nivel 10, y su nivel 1 es la construcción.

| Módulo | Créditos hasta el nivel 10 | Thulium hasta el nivel 10 | Créditos hasta el nivel 20 | Thulium hasta el nivel 20 |
| :--- | ---: | ---: | ---: | ---: |
| Núcleo | 112.326 | 2.000 | 6.647.504 | 2.000 |
| Solar | 1.219.500 | 1.600 | 35.039.500 | 36.850 |
| Granja de créditos | 840.000 | 109 | 26.240.000 | 2.399 |
| Granja de Thulium | 1.154.000 | 4.190 | 32.254.000 | 67.890 |
| Colector de Velkonite | 696.000 | 6.950 | 20.996.000 | 78.950 |
| Colector de Orvium | 696.000 | 6.950 | 20.996.000 | 78.950 |
| Almacén de recursos | 619.500 | 359 | 18.169.500 | 2.649 |
| Forja | 1.224.000 | 2.050 | 35.044.000 | 37.300 |
| Impresora de munición | 1.411.000 | 5.140 | 22.031.000 | 47.940 |
| Fábrica de cohetes | 377.300 | 1.674 | 5.547.300 | 12.494 |

Los primeros pasos son baratos y los últimos caros: el paso de la Granja de créditos del nivel 1 al 2 cuesta 5.000 créditos y 1 Thulium, y su paso del 19 al 20 cuesta 7.000.000 de créditos y 550 Thulium. Los de la Granja de Thulium cuestan 7.000 créditos y 45 Thulium, y después 8.500.000 créditos y 16.000 Thulium. Las mejoras de Solar cuestan en cada nivel lo mismo que las de la Forja, y los dos colectores cuestan lo mismo entre sí.

### Tiempos de mejora {#upgrade-times}

<!-- upgrade-times:start -->
<!-- Generated from server/Resources/SkylabConfig.json by the test skylab::duration_tests::the_wiki_page_is_the_config (run it with SKYLAB_WIKI_WRITE=1 to rewrite this part). -->

**Tiempos de mejora**, por módulo (la mejora desde el nivel de la primera columna):

| Nivel | Núcleo | Solar | Granja de créditos | Granja de Thulium | Almacén de recursos | Colector de Velkonite | Colector de Orvium | Forja | Centro de investigación |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 a 2 | 72 s | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 78 s |
| 2 a 3 | 86 s | 15 min | 10 min | 15 min | 10 min | 15 min | 15 min | 15 min | 101 s |
| 3 a 4 | 104 s | 30 min | 15 min | 30 min | 15 min | 20 min | 20 min | 30 min | 132 s |
| 4 a 5 | 124 s | 45 min | 20 min | 45 min | 20 min | 30 min | 30 min | 45 min | 171 s |
| 5 a 6 | 149 s | 1 h | 30 min | 1 h | 30 min | 45 min | 45 min | 1 h | 223 s |
| 6 a 7 | 20 min | 1 h 15 min | 45 min | 1 h 30 min | 45 min | 50 min | 50 min | 1 h 15 min | 20 min |
| 7 a 8 | 30 min | 1 h 30 min | 1 h | 2 h | 1 h | 1 h | 1 h | 1 h 30 min | 30 min |
| 8 a 9 | 50 min | 2 h | 1 h 20 min | 3 h | 1 h 20 min | 1 h 15 min | 1 h 15 min | 2 h | 50 min |
| 9 a 10 | 1 h 20 min | 3 h | 1 h 40 min | 4 h | 1 h 40 min | 1 h 30 min | 1 h 30 min | 3 h | 1 h 20 min |
| 10 a 11 | 2 h 15 min | 4 h | 2 h | 5 h | 2 h | 2 h | 2 h | 4 h | – |
| 11 a 12 | 3 h 30 min | 5 h | 2 h 30 min | 6 h | 2 h 30 min | 3 h | 3 h | 5 h | – |
| 12 a 13 | 5 h 30 min | 6 h | 3 h | 8 h | 3 h | 4 h | 4 h | 6 h | – |
| 13 a 14 | 9 h | 8 h | 3 h 30 min | 10 h | 3 h 30 min | 6 h | 6 h | 8 h | – |
| 14 a 15 | 14 h | 10 h | 4 h | 11 h | 4 h | 8 h | 8 h | 10 h | – |
| 15 a 16 | 1 d | 12 h | 5 h | 12 h | 5 h | 10 h | 10 h | 12 h | – |
| 16 a 17 | 1 d 12 h | 16 h | 6 h | 14 h | 6 h | 12 h | 12 h | 16 h | – |
| 17 a 18 | 2 d 12 h | 18 h | 8 h | 18 h | 8 h | 16 h | 18 h | 18 h | – |
| 18 a 19 | 4 d | 20 h | 10 h | 1 d | 10 h | 20 h | 1 d | 20 h | – |
| 19 a 20 | 6 d | 1 d | 12 h | 1 d 12 h | 12 h | 1 d | 1 d 12 h | 1 d | – |
| **Total** | 16 d 13 h | 5 d 13 h | 2 d 14 h | 6 d 13 h | 2 d 14 h | 4 d 16 h | 5 d 10 h | 5 d 13 h | 3 h 12 min |
<!-- upgrade-times:end -->

Una mejora que ya está en marcha cuando cambian los tiempos conserva la hora de finalización que se le dio. Solo el Núcleo tarda unos **16 días y medio** de mejora seguida en pasar del nivel 1 al nivel 20. Ningún módulo supera el nivel del Núcleo, así que el último paso de todos los demás módulos (de 12 a 36 horas) solo puede empezar cuando el Núcleo está en el nivel 20: con todos los temporizadores ocupados y los créditos y el Thulium disponibles, la estación entera tarda unos **18 días**.

### Gestión de la energía {#power-management}

Tu Skylab tiene un presupuesto de energía limitado.

- **Balance**: mantén la producción de tu Solar por encima de la energía que usan todos los demás módulos. La página del Skylab muestra el balance y avisa antes de que una construcción lo deje por debajo de cero.
- **Solar sigue el ritmo**: un módulo Solar de nivel N produce la energía de **todos los demás módulos en el nivel N** (el Núcleo, las dos granjas, el Almacén de recursos, los dos colectores y la Forja, y desde el nivel 10 el Centro de investigación) y alrededor de una décima parte más, así que una estación cuyos módulos están todos en el nivel 7 necesita Solar 7, y lo tiene cubierto. Solar un nivel por debajo no basta para una estación completa (la última columna), así que Solar tiene que seguir subiendo con el resto. El Núcleo consume poco, así que puede ir por delante: Solar 5 y superior cubre una estación completa en su nivel con el Núcleo en cualquier nivel. La tabla de más abajo cuenta además la Impresora de munición desde el nivel 7 y la Fábrica de cohetes desde el nivel 10.
- **Estado activo**: puedes encender o apagar las granjas, los colectores y la Forja para gestionar la energía. El Núcleo, Solar, el Almacén de recursos y el Centro de investigación siempre funcionan. La Impresora de munición y la Fábrica de cohetes también se pueden encender y apagar.
- **Déficit de energía**: si el consumo de energía es mayor que la energía producida, todas las granjas y colectores dejan de producir hasta que se recupera el balance. Lo que ya almacenan se conserva y aún puedes recogerlo. La Forja no empieza ningún lote nuevo, y el Centro de investigación no empieza ninguna investigación nueva (una investigación en curso sigue). La Impresora de munición y la Fábrica de cohetes se detienen como las granjas y los colectores.
- **Mejora de Solar**: mientras se mejora, Solar produce solo una cuarta parte de su energía, así que, si tus demás módulos no están muy por debajo, la estación entra en déficit y las granjas y los colectores se detienen hasta que termina la mejora (consulta el [módulo Solar](#solar-module)).

La energía de Solar en cada nivel, frente a lo que consumen los demás módulos en el mismo nivel (todos los módulos en ese nivel, el Núcleo incluido, y el Centro de investigación desde el nivel 10):

<!-- skylab-power:start -->
<!-- Generated from server/Resources/SkylabConfig.json by docs/design/skylab-power-model.py --doc (--check fails while this part is behind). -->

| Nivel | Solar produce | Los otros siete módulos consumen | Sobrante | Con Solar un nivel por debajo |
| :--- | ---: | ---: | ---: | :--- |
| 1 | 255 | 230 | 25 | – |
| 2 | 310 | 278 | 32 | 255: faltan 23 |
| 3 | 375 | 337 | 38 | 310: faltan 27 |
| 4 | 455 | 410 | 45 | 375: faltan 35 |
| 5 | 555 | 501 | 54 | 455: faltan 46 |
| 6 | 680 | 615 | 65 | 555: faltan 60 |
| 7 | 965 | 875 | 90 | 680: faltan 195 |
| 8 | 1.185 | 1.076 | 109 | 965: faltan 111 |
| 9 | 1.460 | 1.327 | 133 | 1.185: faltan 142 |
| 10 | 2.000 | 1.814 | 186 | 1.460: faltan 354 |
| 11 | 2.445 | 2.221 | 224 | 2.000: faltan 221 |
| 12 | 3.005 | 2.731 | 274 | 2.445: faltan 286 |
| 13 | 3.715 | 3.373 | 342 | 3.005: faltan 368 |
| 14 | 4.605 | 4.183 | 422 | 3.715: faltan 468 |
| 15 | 5.730 | 5.205 | 525 | 4.605: faltan 600 |
| 16 | 7.150 | 6.499 | 651 | 5.730: faltan 769 |
| 17 | 8.955 | 8.140 | 815 | 7.150: faltan 990 |
| 18 | 11.250 | 10.225 | 1.025 | 8.955: faltan 1.270 |
| 19 | 14.170 | 12.879 | 1.291 | 11.250: faltan 1.629 |
| 20 | 17.890 | 16.261 | 1.629 | 14.170: faltan 2.091 |
<!-- skylab-power:end -->

La tabla cuenta todos los módulos en el mismo nivel. La Granja de Thulium consume casi tres cuartas partes de ese total en lo más alto (11.695 en el nivel 20, frente a 16.261 de los diez), así que una estación con esa granja muy por delante del resto necesita más Solar de lo que sugiere su Núcleo.

### Recogida {#collecting}

Cada granja y cada colector tiene una tolva para unas 72 horas de lo que produce. La recogida es manual.

- **Capacidad**: cuando una tolva se llena, deja de producir hasta que recoges.
- **Granjas**: los créditos y el Thulium recogidos van directamente a tu cuenta.
- **Colectores**: el mineral va al Almacén de recursos, hasta donde haya sitio.
- **Forja**: las placas van a tu inventario, cuando tu nave está aterrizada.
- **Impresora de munición y Fábrica de cohetes**: la munición y los cohetes pasan a tu inventario, cuando tu nave está aterrizada. Cada una guarda solo 24 horas de producción (consulta [Impresora de munición](#ammo-printer) y [Fábrica de cohetes](#rocket-factory)).
- **Recoger todo** lo toma todo de una vez, incluidos los módulos apagados y en mejora.
- Una insignia **(!)** señala una tolva llena que puedes vaciar y las placas que esperan en la Forja, en la página del Skylab y en la fila del Skylab de la barra lateral.

### El reinicio {#the-wipe}

El Skylab nunca se reinicia: los módulos conservan sus niveles, el Almacén de recursos conserva su mineral y el Centro de investigación conserva sus tecnologías, su depósito de ciencia, el Dark Matter que contiene y una investigación en curso. Las placas de tu inventario son objetos como cualquier otro, así que siguen las [reglas del reinicio](/wiki/03-Mechanics/Wipe-Timeline.md). La Impresora de munición y la Fábrica de cohetes conservan sus niveles, lo que tienen que fabricar y lo que guardan.

## Planifica tu Skylab {#planning-your-skylab}

El Skylab tarda semanas en crecer, así que un poco de planificación compensa. Las cifras son las de las tablas de arriba.

### Qué mejorar primero {#what-to-upgrade-first}

1. **Solar, y luego la Granja de créditos.** Solar cuesta 500 créditos y 50 Thulium y sin él nada funciona; la Granja de créditos no cuesta nada. Las diez [misiones de la estación](/wiki/03-Mechanics/Quests.md#station-missions) te guían en estos primeros pasos y te pagan por ellos 52.000 créditos y 610 Thulium, como base: tu mundo, tus potenciadores y las bonificaciones de tu clan la multiplican.
2. **Después la Granja de Thulium: es tu principal fuente de Thulium.** En el nivel 10 produce 450 Thulium por hora, 10.800 al día, tanto como pagan 54 bajas de un [Crystalys](/wiki/04-Aliens/Crystalys.md) en Alpha (200 cada una). Llegar al nivel 10 cuesta 1.154.000 créditos y 4.190 Thulium, con la construcción incluida. En el nivel 15 la granja produce 22.800 al día y en el nivel 20, 38.400. Su tolva guarda 72 horas, así que vuelve al menos cada tres días. Lo que se compra con Thulium está en la página [Recursos](/wiki/06-Items/Resources.md#thulium).
3. **La Granja de créditos es el ingreso estable de segundo plano.** En el nivel 10 produce 7.500 créditos por hora, 180.000 al día, por 840.000 créditos y 109 Thulium. Los niveles altos se amortizan despacio: el paso del nivel 9 al 10 cuesta 300.000 créditos por 1.000 más por hora, es decir, 300 horas. Mejórala cuando te sobren créditos.
4. **Mantén ocupado el Núcleo.** Nada pasa del Núcleo, y el Núcleo solo tarda unos 16 días y medio en llegar al nivel 20. No hay cola, así que empieza su siguiente paso cada vez que vuelvas.
5. **Construye la cadena de suministro como un conjunto.** Los colectores, el Almacén de recursos y la Forja se abren en el nivel 5 del Núcleo. Un colector solo puede guardar mineral en un Almacén de recursos, y la reserva guarda un día de la producción de su colector en el nivel 1 y cuatro días en el nivel 20, así que mejora el Almacén junto con los colectores o el mineral esperará en sus tolvas.
6. **Ten 2.000 de Thulium listos para el nivel 10 del Núcleo.** El paso del Núcleo del nivel 9 al nivel 10 los pide, y construye el puente y el Núcleo 2, donde se construyen la [Impresora de munición](#ammo-printer) y la [Fábrica de cohetes](#rocket-factory).

### Cómo planificar una mejora de Solar {#timing-a-solar-upgrade}

Mientras se mejora, Solar produce una cuarta parte de su energía, y una estación casi siempre consume más. Las granjas y los colectores se detienen entonces durante toda la mejora: lo que guardan se conserva, pero lo que habrían producido se pierde. La tabla da, para cada paso de Solar, su duración, la estación más grande que sigue funcionando durante él (todos los módulos en el mismo nivel, con el Núcleo y la cadena de suministro; una estación más pequeña aguanta algo más) y lo que una Granja de créditos y una Granja de Thulium de ese nivel habrían producido en ese tiempo. Por ejemplo, Solar del nivel 10 al 11 tarda 4 horas, y unas granjas del nivel 10 habrían producido en ellas 30.000 créditos y 1.800 Thulium. La tabla cuenta además la Impresora de munición desde el nivel 7 y la Fábrica de cohetes desde el nivel 10.

| Mejora de Solar | Tiempo | Estación que sigue funcionando, hasta el nivel | La Granja de créditos produce entretanto | La Granja de Thulium produce entretanto |
| :--- | ---: | ---: | ---: | ---: |
| 1 a 2 | 5 min | ninguna | 42 | 4 |
| 2 a 3 | 15 min | ninguna | 250 | 20 |
| 3 a 4 | 30 min | ninguna | 750 | 55 |
| 4 a 5 | 45 min | ninguna | 1.500 | 105 |
| 5 a 6 | 1 h | ninguna | 2.500 | 180 |
| 6 a 7 | 1 h 15 min | ninguna | 4.375 | 288 |
| 7 a 8 | 1 h 30 min | 1 | 6.750 | 420 |
| 8 a 9 | 2 h | 2 | 11.000 | 660 |
| 9 a 10 | 3 h | 3 | 19.500 | 1.140 |
| 10 a 11 | 4 h | 4 | 30.000 | 1.800 |
| 11 a 12 | 5 h | 5 | 45.000 | 2.750 |
| 12 a 13 | 6 h | 6 | 66.000 | 3.900 |
| 13 a 14 | 8 h | 7 | 104.000 | 6.000 |
| 14 a 15 | 10 h | 8 | 150.000 | 8.500 |
| 15 a 16 | 12 h | 9 | 204.000 | 11.400 |
| 16 a 17 | 16 h | 9 | 320.000 | 17.600 |
| 17 a 18 | 18 h | 11 | 432.000 | 22.500 |
| 18 a 19 | 20 h | 12 | 580.000 | 28.000 |
| 19 a 20 | 1 d | 13 | 840.000 | 36.000 |

- **Sube las granjas a la vez que Solar.** Un módulo en mejora no produce nada y no consume energía de todos modos, así que el tiempo que una granja pasa mejorándose durante la pausa no cuesta nada extra.
- **Mantén bajos los demás módulos si no puedes permitirte una pausa.** Una estación solo sigue funcionando durante una mejora de Solar si todos sus demás módulos están al menos cinco niveles por debajo de Solar (seis desde el nivel 10 de Solar), y una estación completa necesita algo más, como muestra la tabla.
- **Apaga lo que puedas dejar sin usar.** Un módulo apagado no consume energía, así que apagar la Granja de Thulium, la que más consume (80 en el nivel 1 y un 30 % más por nivel), deja sitio a los demás.
