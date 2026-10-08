<!-- wiki-i18n source: 9b9606619f84bd51 -->
<!-- wiki-i18n title: Subasta -->
# Subasta {#auction}

La subasta es el mercado de los pilotos y, a la vez, los lotes de cada hora del propio juego, en una página del menú de la estación. Como la Tienda, es una página de la estación: la usas en el puerto, no en vuelo. Tiene cuatro secciones. **Mercado** es lo que otros pilotos tienen a la venta. **Lotes** son las ofertas del propio juego, una cada hora. **Mis anuncios** es lo que tú tienes a la venta. **Historial** son tus ventas, tus compras y los lotes que has ganado, y cómo te ha ido comerciando.

<!-- market-glance:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- Necesitas el **nivel 5** para usar la subasta: para publicar, comprar y pujar.
- Un anuncio se pone a precio por lote, en créditos enteros o en Thulium entero (no los dos), y nunca por debajo del precio mínimo del objeto. **No hay precio máximo.**
- Un precio en Thulium es como mínimo el precio mínimo en créditos dividido entre 1.000, redondeado hacia arriba, y solo para los objetos cuyo precio mínimo llega a 1 Thulium o más. Eso es todo lo que hace la tasa: **1 Thulium = 1.000 créditos es una regla para el precio mínimo, no un tipo de cambio.** No se cambia nada, no se muestra ningún valor y los créditos y el Thulium nunca se suman.
- Se pueden publicar 80 objetos distintos, y 79 de ellos también se pueden poner a precio en Thulium.
- Un anuncio dura 24 / 72 / 168 horas, a tu elección: las opciones son las mismas en todos los niveles.
- El **depósito** es el 1 % del precio por cada 24 horas que dura el anuncio, con un mínimo de 50 créditos o 1 Thulium. Lo pagas al publicar; nunca se devuelve, ni siquiera si cancelas el anuncio.
- Desde el nivel 10, el depósito es el 1,5 %.
- El **impuesto** es el 5 % del precio. Se descuenta de lo que recibe el vendedor cuando se vende el anuncio.
- El depósito y el impuesto se queman: no van a parar a nadie.
- Desde el día 28 de la temporada hasta el reinicio no hay depósito ni impuesto.
- Desde el día 30 de la temporada la subasta está cerrada hasta que empieza la nueva temporada: no se puede publicar, comprar ni pujar nada. Aun así puedes cancelar tus anuncios.
- Cada moneda tiene su propio límite de lo que puedes vender y de lo que puedes comprar en 24 horas (tabla de niveles más abajo). Lo que ganas en los Lotes no cuenta.
- Entre dos pilotos, uno que compra al otro, pasan como máximo 8.000.000 créditos o 40.000 Thulium en 24 horas.

<!-- market-glance:end -->

## Objetos comercializables {#marketable-items}

Solo se pueden vender los objetos que has **ganado**. Todo lo que ganas lleva en el [Hangar](/wiki/03-Mechanics/Inventory.md#marketable-items) una pequeña etiqueta, **Comercializable**: lo que recoges en el espacio (botín de alienígenas, enjambres, Wardens y agujero negro: [Carga](/wiki/03-Mechanics/Cargo.md)), lo que paga una misión ([Misiones](/wiki/03-Mechanics/Quests.md#rewards)) y todo lo que fabrican el Ensamblaje y la Forja. Lo que has **comprado** en la Tienda, ganado en un lote, comprado en el Mercado, recibido con un código de bonificación, un paquete de invitación o el kit inicial, o recuperado como reembolso no es comercializable y no se puede volver a vender, para que nada se compre solo para revenderlo. Las placas que fabrica la Forja del Skylab tampoco son comercializables; las Reinforced Plates que paga una misión sí.

La etiqueta es un número de unidades, no un interruptor: una pila de munición puede tener balas compradas y ganadas, y la tarjeta dice «Comercializable (3 de 5)». Cuando gastas parte de una pila (disparar, fabricar), se van primero las unidades normales, así que las comercializables duran más. Al combinar dos piezas en la [Forja](/wiki/06-Items/Forge.md#merge), la etiqueta se mantiene solo si las dos piezas la tenían, y la vista previa lo dice; un paso de la Forja que falla devuelve sus materiales como unidades normales.

El chip **Solo comercializable** del Hangar muestra solo lo que puedes vender, y el **martillo** junto a la papelera de un objeto con etiqueta abre la hoja de venta de la Subasta para él. En el Ensamblaje, una receta cuyo resultado es comercializable lo dice, y un material que te falta tiene un enlace que abre la Subasta con su nombre en el cuadro de búsqueda.

Cuando llegó la Subasta (0.4.12), el equipo que ya tenías y que la Tienda no vende, y los recursos, se etiquetaron una vez. No se etiquetaron estos, porque la Tienda los vendió en su día o porque lo que tienes mezcla piezas compradas y ganadas: el Quantum Laser III, las Absorption Shield Cells II y III, los Impulse Thrusters II y III, las dos Reinforced Plates y la Base CPU I más antigua de cada piloto (la del kit inicial). Los nuevos de estos que ganes o fabriques sí llevan etiqueta.

## Qué se puede vender {#what-can-be-sold}

<!-- market-kinds:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Categoría | Objetos que puedes vender | Número |
| :--- | :--- | ---: |
| **Láseres** | Quantum Laser I, Quantum Laser II, Quantum Laser III, Starfire-III, Helios Beam | 5 |
| **Amplificadores láser** | Damage Amp I, Crit Amp I, Penetration Amp I, Damage Amp II, Crit Amp II, Penetration Amp II, Damage Amp III, Crit Amp III, Penetration Amp III, Damage Amp IV, Crit Amp IV, Penetration Amp IV | 12 |
| **Núcleos de escudo** | Light Shield Core, Basic Shield Core, Heavy Shield Core | 3 |
| **Motores** | Engine I, Engine II, Engine III | 3 |
| **Adaptive Cores** | Adaptive Core I, Adaptive Core II, Adaptive Core III | 3 |
| **Células de escudo** | Absorption Shield Cell I, Capacity Shield Cell I, Absorption Shield Cell II, Capacity Shield Cell II, Absorption Shield Cell III, Capacity Shield Cell III, Absorption Shield Cell IV, Capacity Shield Cell IV | 8 |
| **Propulsores** | Impulse Thruster I, Momentum Thruster I, Impulse Thruster II, Momentum Thruster II, Impulse Thruster III, Momentum Thruster III, Impulse Thruster IV, Momentum Thruster IV | 8 |
| **Munición láser** | Standard Battery (en lotes de 100), Siphon Battery (en lotes de 10), Advanced Plasma (en lotes de 10), Ultra Core (en lotes de 10), Experimental Fusion Core | 5 |
| **Cohetes** | Ember I, Lancet I, Rivet I, Scatter I, Ember II, Lancet II, Rivet II, Scatter II, Ember III, Lancet III, Rivet III, Scatter III | 12 |
| **Extras** | Repair Drone I, Repair Drone II, Repair Drone III, EMP Charge, Repair Drone IV, Cloaking CPU S, Base CPU I, Cloaking CPU M, Auto-Repair CPU, Cloaking CPU L, Base CPU II | 11 |
| **Recursos** | Cataclysite (en lotes de 100), Ship Fragment (en lotes de 100), Daraxium (en lotes de 100), Nyxite (en lotes de 100), Quorvium (en lotes de 10), Reinforced Hull Plate (en lotes de 10), Power Core, Velkonite Reinforced Plate, Dark Matter, Orvium Reinforced Plate | 10 |

<!-- market-kinds:end -->

Las naves, los drones, las formaciones de drones, los potenciadores y las suscripciones no se pueden vender nunca, ni tampoco la Ancient Control Unit, los minerales Velkonite y Orvium, la Dark Matter Plate, la Jump CPU, las Extra Slots CPU, la N.U.K.E. y la N.I.K.E. Las Dark Matter Plates no están en la Subasta en absoluto, ni como mercancía ni como precio. No se puede publicar un objeto equipado, encajado en otro objeto, con módulos dentro o en el [Alijo de Transporte](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-), ni una Cloaking CPU, una EMP Charge o una Base CPU que ya se haya usado. La munición y los cohetes se venden desde la estación: aterriza primero tu nave.

## Vender {#selling}

Pulsa **Vender un objeto** (o el martillo del Hangar), elige lo que has ganado (un menú de categorías acota la lista, con las mismas categorías que el Mercado), escoge créditos o Thulium, fija el precio de un lote y cuánto dura el anuncio: 1, 3 o 7 días. La hoja muestra el precio mínimo, tres chips que rellenan un precio (**Mínimo**; **Venta rápida**, uno por debajo del anuncio más barato ahora; y **Justo**, el precio de la última venta) y el depósito, el impuesto y lo que recibes, antes de publicar. Bajo el precio, **Anuncios similares** muestra en un gráfico a qué precios se anuncia ahora el mismo objeto con el mismo encantamiento, en la moneda que has elegido: tu precio es una línea en él, el precio mínimo, la última venta y el precio de la Tienda van marcados, una línea en palabras dice dónde quedaría tu precio y debajo se ven los tres anuncios más baratos. Una pieza es un lote de uno; la munición y algunos recursos se venden en lotes de 10 o 100, y vendes un número entero de lotes. Lo que publicas sale de tu inventario y el servidor lo guarda hasta que se venda, lo canceles o caduque; entonces vuelve, con su etiqueta. Puedes cancelar en cualquier momento, incluso en los últimos días de una temporada. Un anuncio es una instantánea: para cambiar un precio, cancela el anuncio y publícalo de nuevo (el depósito se paga otra vez).

Cada objeto tiene un **precio mínimo** y **no hay precio máximo**: pide lo que quieras. La tabla muestra el precio mínimo de algunos objetos.

<!-- market-bands:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Objeto | Se vende en lotes de | Precio mínimo, créditos | Precio mínimo, Thulium |
| :--- | ---: | ---: | ---: |
| Quantum Laser II | 1 | 32.000 | 32 |
| Quantum Laser III | 1 | 170.000 | 170 |
| Helios Beam | 1 | 1.600.000 | 1.600 |
| Absorption Shield Cell IV | 1 | 1.100.000 | 1.100 |
| Heavy Shield Core | 1 | 870.000 | 870 |
| Impulse Thruster IV | 1 | 980.000 | 980 |
| EMP Charge | 1 | 40.000 | 40 |
| Cloaking CPU S | 1 | 400.000 | 400 |
| Ultra Core | 10 | 800 | 1 |
| Lancet I | 1 | 200 | 1 |
| Ship Fragment | 100 | 600 | 1 |
| Dark Matter | 1 | 33.000 | 33 |

<!-- market-bands:end -->

Un precio en Thulium sigue una sola regla: el precio mínimo en créditos dividido entre la tasa, redondeado hacia arriba. La tasa no es un valor que el juego dé al Thulium. Es solo la forma de calcular el precio mínimo en Thulium, y por ella un anuncio en Thulium puede ser barato para un piloto que tiene Thulium. La mayoría de los vendedores pedirá créditos. Todo objeto salvo el **Quorvium** puede ponerse a precio en Thulium, también los baratos (munición, cohetes, los recursos comunes): su precio mínimo es entonces 1 Thulium, el paso más pequeño. Solo el Quorvium va únicamente en créditos, porque 1 Thulium sería más de lo que vale un lote suyo.

Tus **anuncios abiertos** (y un anuncio que un admin haya puesto en espera) ocupan huecos. Al subir de nivel tienes más huecos, hasta un máximo, y puedes vender y comprar más cada día. Cuánto puede durar un anuncio es igual en todos los niveles.

<!-- market-limits:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Nivel | Anuncios abiertos | Duración máxima | Al día, créditos | Al día, Thulium | Depósito por 24 h |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 5 | 20 | 168 h | 4.500.000 | 22.500 | 1 % |
| 6 | 40 | 168 h | 6.000.000 | 30.000 | 1 % |
| 7 | 70 | 168 h | 7.500.000 | 37.500 | 1 % |
| 8 | 100 | 168 h | 8.500.000 | 42.500 | 1 % |
| 9 | 100 | 168 h | 10.000.000 | 50.000 | 1 % |
| 10 | 100 | 168 h | 15.000.000 | 75.000 | 1,5 % |
| 11 | 100 | 168 h | 15.000.000 | 75.000 | 1,5 % |
| 12 | 100 | 168 h | 15.000.000 | 75.000 | 1,5 % |
| 13 | 100 | 168 h | 20.000.000 | 100.000 | 1,5 % |
| 14 | 100 | 168 h | 20.000.000 | 100.000 | 1,5 % |
| 15 | 100 | 168 h | 20.000.000 | 100.000 | 1,5 % |
| 16 | 100 | 168 h | 20.000.000 | 100.000 | 1,5 % |
| 17 | 100 | 168 h | 20.000.000 | 100.000 | 1,5 % |
| 18 | 100 | 168 h | 20.000.000 | 100.000 | 1,5 % |
| 19 | 100 | 168 h | 20.000.000 | 100.000 | 1,5 % |
| 20 o más | 100 | 168 h | 20.000.000 | 100.000 | 1,5 % |

<!-- market-limits:end -->

## Comisiones {#fees}

Un anuncio cuesta un **depósito**, que se paga al publicar y nunca se devuelve, y una venta cuesta un **impuesto**, que se descuenta de lo que recibe el vendedor. Los dos se pagan en la moneda del anuncio y se **queman**: no van a parar a nadie, así que nadie gana comerciando consigo mismo. En los dos últimos días de una temporada no hay depósito ni impuesto.

<!-- market-fees:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Anuncio | Precio | Depósito | Impuesto | El vendedor recibe |
| :--- | ---: | ---: | ---: | ---: |
| Quantum Laser III: nivel 6, 24 h | 170.000 créditos | 1.700 créditos | 8.500 créditos | 161.500 créditos |
| Quantum Laser III: nivel 10, 72 h | 170 Thulium | 8 Thulium | 8 Thulium | 162 Thulium |
| Helios Beam: nivel 12, 168 h | 2.500.000 créditos | 262.500 créditos | 125.000 créditos | 2.375.000 créditos |
| Helios Beam: nivel 12, 168 h, en los últimos días de una temporada | 2.500.000 créditos | 0 créditos | 0 créditos | 2.500.000 créditos |

<!-- market-fees:end -->

## Comprar {#buying}

El **Mercado** muestra lo que venden otros pilotos. Acota la lista con los **chips de categoría** (uno por cada tipo de objeto, con el número de anuncios que tiene), busca por nombre, filtra por encantamiento y moneda, y ordena por precio, por lo que termina antes o por lo más nuevo. Elige un anuncio para ver qué es, quién lo vende, cuánto dura y cómo está su precio frente a la última venta, el precio más bajo ahora y el precio de la Tienda. Una pila se compra en lotes enteros. Una compra grande te pide confirmar una vez más. El vendedor cobra al instante, menos el impuesto; tú no pagas depósito ni impuesto. Lo que compras **no es comercializable**: la página dice «Recibes: no comerciable» junto a **Comprar por …**, porque solo se puede vender lo que ganas. No puedes comprar tu propio anuncio. Un anuncio que se vende mientras lo miras dice «Ese anuncio ya no está.»

## Límites {#limits}

Cada moneda tiene su propio límite diario de lo que puedes vender y de lo que puedes comprar, contado en las últimas 24 horas, y un límite de lo que pasa entre dos pilotos, para que una segunda cuenta no sea una forma rápida de mover una fortuna. Los créditos y el Thulium nunca se suman: quien vende por Thulium gasta su límite de Thulium y nada más. La hoja de venta te avisa cuando una venta pasaría tu límite diario de ventas, y cuando una compra pasaría tu límite diario de compras, el Mercado te lo dice y deja **Comprar por …** desactivado. Los límites crecen con el nivel, y Premium no cambia ninguno. Lo que ganas en los Lotes no cuenta.

Los cohetes de un anuncio, de un lote en el que vas en cabeza y de tu bodega cuentan todos para el máximo de un cohete que puedes llevar: un anuncio no sirve para llevar más de lo que permite la pila de la Tienda.

## Mis anuncios e Historial {#my-listings-and-history}

**Mis anuncios** muestra tus huecos y cada anuncio con su estado (abierto, vendido, cancelado, caducado, devuelto o en espera), un botón **Cancelar**, **Publicar de nuevo** para uno cerrado y un chip **Superado** cuando otro anuncio del mismo objeto pide menos. Un anuncio que ha caducado vuelve solo a tu inventario. El **Historial** empieza con tu actividad de los últimos 30 días: tus ventas y compras, lo que ingresaste y gastaste, las tasas e impuestos que pagaste, tu resultado neto, tu mejor venta, tu venta media y el objeto que más negociaste, y dos gráficos de línea: lo que ingresas cada día y tu resultado hasta ahora (para créditos o para Thulium, de uno en uno). Debajo está la lista de lo que vendiste, compraste y ganaste, con el impuesto. El juego guarda el libro de cuentas de la Subasta 90 días.

Te enteras de que algo se vende por un aviso emergente, el sonido de la Subasta y el nuevo saldo, y por una insignia en la entrada de la Subasta mientras la página está cerrada. Una racha de ventas es un solo aviso. La Subasta tiene sus propios sonidos suaves, uno para cada cosa que haces o que te pasa allí (publicar, terminar, una venta, una puja, que te superen, ganar), y siguen el volumen de la interfaz.

## Los Lotes de cada hora {#the-hourly-lots}

Los Lotes son las ofertas del propio juego: munición, cohetes y EMP Charges, cada hora, para pujar. Son una forma de comprar munición por menos de lo que pide la Tienda, y un sumidero: la puja ganadora se quema. Solo se abren los lotes de la tabla del día de abajo (nunca munición x1 ni x4, nunca Siphon Batteries, nunca un cohete especial), en la moneda de la Tienda. Un lote de cohetes nunca supera el máximo de ese cohete que puedes llevar (la pila de la Tienda), así que se rechaza una puja que te haría pasarte de él: puja por un lote de cohetes cuando lleves pocos de ese cohete.

<!-- market-lots:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- Al comienzo de cada hora UTC se abre un lote nuevo, que sigue abierto 4 horas, así que hay 4 abiertos a la vez.
- La puja inicial es el 40 % del precio de la tienda de lo que se ofrece. Cada puja posterior debe superar la puja más alta en al menos un 5 %, y en al menos 100 créditos o 1 Thulium.
- Tu puja se paga al instante y queda retenida. Si alguien te supera, te la devuelven al instante.
- Una puja en los últimos 2 min de un lote mueve su final a 2 min después de la puja, como máximo 5 veces.
- Lo que ganas es para volar, no para comerciar: nunca es comercializable. La puja ganadora se quema. Un lote en el que nadie puja no se vende y no le cuesta nada a nadie.
- El tamaño de un lote depende de los pilotos de nivel 5 o más que han mirado la subasta en los últimos 3 días: con ninguno es el 10 % del tamaño de la tabla, con 30 o más es el tamaño completo, en pasos de 500 para munición, 50 para cohetes y 1 para EMP Charges.
- En las últimas 6 horas de una temporada no se crea ningún lote. El reinicio cancela los lotes que siguen abiertos y se devuelven todas las pujas.

<!-- market-lots:end -->

<!-- market-day:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Hora UTC | Lote | Tamaño completo | Se paga en | Puja inicial con tamaño completo |
| :--- | :--- | ---: | :--- | ---: |
| 00:00 | Scatter III | 1.250 | Thulium | 2.500 Thulium |
| 01:00 | Advanced Plasma | 25.000 | Thulium | 5.000 Thulium |
| 02:00 | Lancet I | 12.500 | Créditos | 2.500.000 créditos |
| 03:00 | EMP Charge | 5 | Thulium | 1.000 Thulium |
| 04:00 | Ultra Core | 25.000 | Thulium | 10.000 Thulium |
| 05:00 | Rivet II | 5.000 | Créditos | 1.600.000 créditos |
| 06:00 | Advanced Plasma | 10.000 | Thulium | 2.000 Thulium |
| 07:00 | Advanced Plasma | 50.000 | Thulium | 10.000 Thulium |
| 08:00 | Ember I | 12.500 | Créditos | 2.500.000 créditos |
| 09:00 | Ultra Core | 50.000 | Thulium | 20.000 Thulium |
| 10:00 | Scatter II | 5.000 | Créditos | 1.600.000 créditos |
| 11:00 | EMP Charge | 5 | Thulium | 1.000 Thulium |
| 12:00 | Advanced Plasma | 50.000 | Thulium | 10.000 Thulium |
| 13:00 | Lancet III | 1.250 | Thulium | 2.500 Thulium |
| 14:00 | Ultra Core | 10.000 | Thulium | 4.000 Thulium |
| 15:00 | Advanced Plasma | 25.000 | Thulium | 5.000 Thulium |
| 16:00 | Ultra Core | 50.000 | Thulium | 20.000 Thulium |
| 17:00 | Rivet I | 12.500 | Créditos | 2.500.000 créditos |
| 18:00 | Advanced Plasma | 50.000 | Thulium | 10.000 Thulium |
| 19:00 | Ember II | 5.000 | Créditos | 1.600.000 créditos |
| 20:00 | Ultra Core | 25.000 | Thulium | 10.000 Thulium |
| 21:00 | Advanced Plasma | 25.000 | Thulium | 5.000 Thulium |
| 22:00 | Advanced Plasma | 10.000 | Thulium | 2.000 Thulium |
| 23:00 | EMP Charge | 5 | Thulium | 1.000 Thulium |

<!-- market-day:end -->

Cuando pocos pilotos usan la Subasta, los lotes son pequeños, para que a un puñado de pilotos no se le ofrezcan miles de balas cada hora; crecen cuantos más pilotos miran.

## La temporada y el reinicio {#the-season-and-the-wipe}

La Subasta sigue la temporada (consulta la [Cronología del reinicio](/wiki/03-Mechanics/Wipe-Timeline.md)). En los dos últimos días no hay comisiones. Desde el día 30, cuando empieza la cuenta atrás de cinco minutos del reinicio, está cerrada: no se publica, compra ni puja nada, un lote que termina entonces se cancela y se devuelve su puja, y aun así puedes cancelar tus propios anuncios. Un anuncio nunca dura más allá del final de la temporada.

Con el reinicio, **cada anuncio abierto vuelve a su vendedor** como objetos sueltos, y el reinicio borra después los objetos sueltos como cualquier otro (solo se queda lo que guardas en el [Alijo de Transporte](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-)): así que vende, o cancela y guarda en el Alijo lo que quieras conservar. Los lotes que siguen abiertos se cancelan y las pujas se devuelven. Los créditos y el Thulium no se borran.

## Lo que la Subasta no te da {#what-the-auction-does-not-give-you}

La Subasta sirve para comerciar con lo que ganas, y es honesta sobre sus límites.

- **Vender botín no es un grind.** Los botines en bruto de los alienígenas son solo recursos y valen entre el 0,4 y el 0,9 por ciento de lo que paga en bajas la misma hora de caza a nivel 5. Lo que el Mercado da a un piloto nuevo es el equipo que le pagan sus misiones y que no necesita (una vez), los recursos de las misiones de Desafío, las cajas de los jefes de enjambre y lo que fabrica.
- **No hay comerciante.** Las órdenes de compra, en las que un piloto dice qué quiere comprar y por cuánto, no están en esta versión. Hasta que lleguen, los únicos comerciantes son el artesano, que compra materiales, fabrica equipo en el Ensamblaje y lo vende, y el piloto almacén, que guarda existencias en el Alijo de Transporte durante el reinicio.
- **El equipo de la Tienda no es para revender.** El equipo que has comprado en la Tienda no se puede volver a vender: eso incluye el Quantum Laser I y II, los Light y Basic Shield Core, Engine I y II, el primer grado de células y propulsores, los amps que vende la Tienda y la munición comprada. El único Quantum Laser II comercializable de un piloto es el que paga una misión una vez.
- **Las placas vienen de misiones.** Las Velkonite y Orvium Reinforced Plates del Mercado son las que pagan las misiones de Desafío. Las placas de la Forja se quedan fuera; si no, serían el mayor producto del Mercado.

Si un anuncio te parece raro, avísalo de la forma habitual: los administradores del juego pueden poner un anuncio en espera, devolverlo, pausar la Subasta o prohibir a un piloto usarla, y cada una de esas acciones queda registrada.
