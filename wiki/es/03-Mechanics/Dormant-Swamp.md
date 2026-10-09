<!-- wiki-i18n source: a8a96edb9a5070f1 -->
<!-- wiki-i18n title: Dormant Swamp -->
# Dormant Swamp

<!-- wiki-search: swamp; dormant swamp; base; turret; turrets; nike turret; laser turret; inert mass; unwakened; the unwakened; slumbering void; void; dormant lance; ds-4; pantano; torreta; torretas; cañón; cañones -->

Hace mucho tiempo vivió en medio de la galaxia una civilización avanzada. Construía en cristal negro violáceo, con vetas violetas que brillan, y por una razón que nadie conoce se derrumbó. El **Dormant Swamp** es su puesto avanzado, en la esquina superior izquierda de `DS-4`. Desde el día 11 de la temporada se agita: cañones en el centro disparan a toda nave que ven, las **Inert Masses** lo guardan, y en el mismo centro duerme **el Unwakened**. Es un lugar que los pilotos **todavía no deben visitar**. Bajo camuflaje puedes volar hasta el Unwakened, y por ahora no se puede hacer nada más allí: la base y sus cañones no se pueden dañar, ni entrar, ni abordar, ni comerciar con ellos.

El pantano es también donde aparece el [Enjambre Dormant](/wiki/05-Swarms/Dormant-Swarm.md) desde el día 11, y **Slumbering Voids** patrullan a su alrededor. Los mismos Voids llegan en oleadas a las [excavadoras gigantes](/wiki/03-Mechanics/Giant-Excavator.md#the-slumbering-voids). Los sectores están en [Sectores de peligro](/wiki/01-General/Danger-Sectors.md).

## De un vistazo {#at-a-glance}

<!-- swamp-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Dónde**: La esquina superior izquierda de `DS-4`: el centro está en 5.000 / 5.000
- **Aparece**: Desde el día 11 de la temporada hasta el reinicio
- **La zona**: 4.300 unidades alrededor del centro: lo más lejos que llegan los cañones, y el lugar que nadie debe visitar todavía
- **El aviso**: Una nave que cruza el anillo a 4.800 unidades del centro recibe una línea del Sistema
- **Camuflaje**: Ningún cañón ve jamás una nave camuflada, ni una dentro de la ventana de un EMP
- **Los alienígenas**: 5 Inert Masses se quedan a menos de 2.400 unidades del centro. El Unwakened duerme en el centro. 2 Slumbering Voids patrullan entre 4.600 y 6.500 unidades del centro.
- **El Enjambre Dormant**: Aparece en 9.417 / 6.606, a 4.700 unidades del centro y fuera de la zona
- **Rocas**: Ningún asteroide queda a menos de 4.900 unidades del centro

<!-- swamp-glance:end -->

## Los cañones {#the-guns}

Las torretas del pantano disparan a la **nave más cercana que puedan ver** dentro de su alcance, y a ninguna otra: la zona es el círculo que alcanza la más lejana de ellas. No son entidades de ningún tipo: no tienen puntos de vida, no se las puede fijar como objetivo y nada de lo que les dispares hace efecto. Sus disparos son reales, y el mundo escala su daño como escala el arma de cualquier alienígena.

<!-- swamp-guns:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Daño de un disparo, en cada mundo:

| Cañón | Lugar | Dispara cada | Alcance (unidades) | Alpha | Beta | Gamma |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| Torreta de [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | 5.000 / 4.400 | 2 s | 3.640 | 75.000 | 112.500 | 150.000 |
| Torreta de [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | 5.000 / 4.400 | 5 s | 1.080 | 50.000 | 75.000 | 100.000 |
| Torreta láser × 2 | 3.600 / 5.200; 6.400 / 5.200 | 1 s | 2.500 | 45.000–55.000 | 67.500–82.500 | 90.000–110.000 |

- Un cohete se dispara desde el 90 % de su alcance, para que llegue; una torreta láser dispara una vez por segundo, y su daño se sortea dentro del rango indicado.
- Un N.I.K.E. tiene 35 % de penetración de escudo, que se resta de la absorción de un escudo.
- Un N.U.K.E. estalla en un radio de 900 unidades, con más fuerza en el centro.

<!-- swamp-guns:end -->

- **Nada llega fuera de la zona,** y dentro de ella una nave es destruida en segundos: cuanto más se acerca al centro, más cañones se suman, y ni siquiera la Wraith mejor protegida aguanta.
- **Un camuflaje te mete dentro.** Ninguna torreta ve jamás una nave camuflada, ni una dentro de la ventana de un EMP, a ninguna distancia. Una explosión dirigida a una nave visible que estalla junto a una camuflada la daña igualmente y acaba con su camuflaje.
- **Disparan solo a pilotos,** nunca a alienígenas, pilotos de la corporación ni al enjambre, y la protección de una nave que acaba de volver tras una destrucción vale también contra ellas.
- **El anillo de aviso.** Una nave que cruza el anillo fuera de la zona recibe una línea del Sistema: las torretas disparan a toda nave que ven, y algo duerme en el centro. Se le vuelve a avisar solo cuando ha salido del anillo y ha regresado.
- **Salir.** Si te destruyen allí y vuelves en el sitio, o inicias sesión dentro de la zona, te colocan fuera. Un rumbo que marcas con un clic se desvía alrededor de la zona, y un aviso te advierte si el lugar donde haces clic queda dentro.

## Los alienígenas {#the-aliens}

Aquí viven tres alienígenas de la civilización perdida, cada uno con sus propias cifras. Se pagan como el jefe de un enjambre: **según el daño causado**, a todo piloto que haya hecho al menos la parte indicada en [Enjambres](/wiki/05-Swarms/Swarms.md#the-rules-of-every-swarm), y la caja va al piloto que más daño causó. Sus derribos suman a tus puntos PvE de rango como los de una nave de enjambre, en proporción a su paga ([Rangos](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points)). El escudo de cada uno absorbe el 80 % de cada impacto mientras dura ([Escudos](/wiki/03-Mechanics/Shields.md)).

- **Slumbering Void.** El cazador esbelto, el alienígena más rápido del juego (tan rápido como una Storm con Afterburner III). Algunos patrullan siempre los alrededores del pantano, y otros llegan en oleadas a las excavadoras. Es agresivo, caza al piloto más cercano que pueda ver y nunca ve una nave camuflada.
- **Inert Mass.** Un casco muerto con grietas violetas, del tamaño de una estación pequeña. Se quedan a una distancia fija del centro del pantano y por ahora no se alejan de él. Dispara **Dormant Lances**: cohetes guiados de larguísimo alcance que siguen a una nave hasta que se camufla, abre una ventana de EMP, entra en un anillo seguro, salta o muere. Es más rápida que cualquier nave, así que solo esas interrupciones sirven.
- **El Unwakened.** Un monolito que duerme en el centro del pantano, lo más grande de cualquier mapa, tan lento que nunca alcanza a una nave. No dispara nada, pero toda nave dentro de su aura se quema, **camuflada o no**. Es **inmune**: los disparos y los cohetes impactan y no hacen nada, la ventana de objetivo muestra las barras llenas y la palabra Inmune. Un evento posterior permitirá combatirlo; sus recompensas de abajo están escritas y todavía no se pueden ganar.

<!-- swamp-members:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

### Slumbering Void

2 Slumbering Voids patrullan entre 4.600 y 6.500 unidades del centro del pantano; uno que es destruido vuelve 1 h después. Las oleadas de una excavadora traen más del mismo alienígena.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 25.000 | 37.500 | 50.000 |
| Escudo | 150.000 | 225.000 | 300.000 |
| Absorción del escudo | 80 % | 80 % | 80 % |
| Daño de los láseres (una salva por segundo) | 3.000 | 4.500 | 6.000 |
| Velocidad | 400 | 400 | 400 |
| Alcance de los láseres | 800 | 800 | 800 |
| Radio de agresión | 2.500 | 2.500 | 2.500 |
| Créditos | 23.000 | 46.000 | 69.000 |
| Thulium | 60 | 120 | 180 |
| Experiencia (XP) | 3.600 | 7.200 | 10.800 |
| Honor | 16 | 32 | 48 |
| Puntos PvE por derribo | 10 | 10 | 10 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto | Probabilidad | Cantidad |
| :--- | ---: | ---: |
| Uno de Ultra Core y Experimental Fusion Core, elegido al azar | 60 % | 30–60 |
| Uno de los 4 [cohetes](/wiki/06-Items/Rockets.md) Épicos, elegido al azar | 40 % | 1–3 |

### Inert Mass

5 Inert Masses están a menos de 2.400 unidades del centro; una que es destruida vuelve 1 h después. Dispara cada 6 s una [Dormant Lance](/wiki/06-Items/Rockets.md#the-craft-only-rockets) guiada a la nave más cercana que pueda ver: velocidad 750, un vuelo de 5.250 unidades, 40 % de penetración.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 250.000 | 375.000 | 500.000 |
| Escudo | 100.000 | 150.000 | 200.000 |
| Absorción del escudo | 80 % | 80 % | 80 % |
| Daño de cada Dormant Lance | 5.000–8.000 | 7.500–12.000 | 10.000–16.000 |
| Velocidad | 60 | 60 | 60 |
| Alcance de los cohetes | 5.000 | 5.000 | 5.000 |
| Radio de agresión | 5.000 | 5.000 | 5.000 |
| Créditos | 125.000 | 250.000 | 375.000 |
| Thulium | 335 | 670 | 1.005 |
| Experiencia (XP) | 20.200 | 40.400 | 60.600 |
| Honor | 88 | 176 | 264 |
| Puntos PvE por derribo | 15 | 15 | 15 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto | Probabilidad | Cantidad |
| :--- | ---: | ---: |
| Ultra Core y Experimental Fusion Core, repartidos a partes iguales | 100 % | 400–800 en total |
| Uno de los 4 [cohetes](/wiki/06-Items/Rockets.md) Épicos, elegido al azar | 100 % | 20–40 |
| N.I.K.E. | 5 % | 1–2 |
| Dark Matter | 5 % | 1–3 |
| Ancient Control Unit | 10 % | 1 |
| Power Core | 25 % | 1–2 |

### The Unwakened

Hay uno, en el centro del pantano y en ningún otro sitio; vuelve 24 h después de ser destruido. Es **inmune** hasta que una misión posterior apague la marca: los disparos y los cohetes lo impactan y no hacen nada. Sus recompensas están escritas y todavía no se pueden ganar.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 10.000.000 | 15.000.000 | 20.000.000 |
| Escudo | 10.000.000 | 15.000.000 | 20.000.000 |
| Absorción del escudo | 80 % | 80 % | 80 % |
| Daño del aura por segundo, a toda nave dentro | 75.000 | 112.500 | 150.000 |
| Radio del aura | 700 | 700 | 700 |
| Velocidad | 10 | 10 | 10 |
| Radio de agresión | 3.000 | 3.000 | 3.000 |
| Créditos | 7.500.000 | 15.000.000 | 22.500.000 |
| Thulium | 20.000 | 40.000 | 60.000 |
| Experiencia (XP) | 1.200.000 | 2.400.000 | 3.600.000 |
| Honor | 5.200 | 10.400 | 15.600 |
| Puntos PvE por derribo | 112 | 112 | 112 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto | Probabilidad | Cantidad |
| :--- | ---: | ---: |
| Ultra Core y Experimental Fusion Core, repartidos a partes iguales | 100 % | 10.000–15.000 en total |
| Uno de los 4 [cohetes](/wiki/06-Items/Rockets.md) Épicos, elegido al azar | 100 % | 500–800 |
| N.I.K.E. | 100 % | 20–30 |
| N.U.K.E. | 100 % | 5–10 |
| Dark Matter | 100 % | 40–60 |
| Ancient Control Unit | 100 % | 10–20 |
| Power Core | 100 % | 100–200 |

<!-- swamp-members:end -->

## Qué hacer aquí {#what-to-do-here}

- **Mirar, no tocar.** El pantano es para más adelante. Lo único que puedes alcanzar sin camuflaje está fuera de la zona: los Voids que patrullan, en un anillo alrededor de la zona, son la primera línea del pantano y el lugar donde un grupo puede combatir sin los cañones.
- **Combate a los Voids con penetración.** El gran escudo de un Void absorbe el 80 % de un impacto y casi no importa: el casco que hay detrás es pequeño. Cuanta más penetración de escudo tengan tus láseres, antes cae ([Láseres y munición](/wiki/06-Items/Lasers.md)).
- **Mantente lejos de las Lances.** Una Inert Mass ve muy lejos y a una Lance no se le escapa: rompe su sujeción con un camuflaje, un EMP, un anillo seguro o un salto, o sal de su alcance. Una Mass es un combate largo incluso para un grupo grande de las naves más fuertes.
- **El Enjambre Dormant** aparece ahora justo fuera de la zona, así que un grupo puede esperarlo sin los cañones. Consulta [Enjambre Dormant](/wiki/05-Swarms/Dormant-Swarm.md).

## Dónde leer más {#where-to-read-more}

- [Sectores de peligro](/wiki/01-General/Danger-Sectors.md): qué cambió el día 11.
- [Excavadora gigante](/wiki/03-Mechanics/Giant-Excavator.md): las oleadas de Slumbering Voids y lo que guardan.
- [Enjambres](/wiki/05-Swarms/Swarms.md) y [Enjambre Dormant](/wiki/05-Swarms/Dormant-Swarm.md): cómo paga el derribo de un jefe.
- [Cohetes](/wiki/06-Items/Rockets.md#the-craft-only-rockets): el N.I.K.E. y el N.U.K.E. que dispara la torreta.
- [Agujero negro](/wiki/03-Mechanics/Black-Hole.md): el otro peligro de `DS-4`.
- [Cajas de carga](/wiki/03-Mechanics/Cargo.md): las cajas que sueltan los alienígenas.
