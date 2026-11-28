<!-- wiki-i18n source: 3c07d568f3af3aab -->
<!-- wiki-i18n title: Dormant Swamp -->
# Dormant Swamp

<!-- wiki-search: swamp; dormant swamp; base; turret; turrets; nike turret; laser turret; inert mass; unwakened; the unwakened; slumbering void; void; dormant lance; ds-4; pantano; torreta; torretas; cañón; cañones -->

Hace mucho tiempo vivió en medio de la galaxia una civilización avanzada. Construía en cristal negro violáceo, con vetas violetas que brillan, y por una razón que nadie conoce se derrumbó. El **Dormant Swamp** es su puesto avanzado, en la esquina superior izquierda de `DS-4`. Desde el día 11 de la temporada se agita: cañones en el centro disparan a toda nave que ven, las **Inert Masses** lo guardan, y en el mismo centro duerme **el Unwakened**. Bajo camuflaje puedes volar hasta el Unwakened. Desde que se abrió el [Deep Void](/wiki/03-Mechanics/Deep-Void.md), los cañones y el Unwakened pueden ser destruidos, y la primera muerte del Unwakened en una temporada abre, en cada mundo, el Threshold de ese mundo. En la base en sí no se puede entrar, no se la puede abordar ni se puede comerciar con ella.

El pantano es también donde aparece el [Enjambre Dormant](/wiki/05-Swarms/Dormant-Swarm.md) desde el día 11, y **Slumbering Voids** patrullan a su alrededor. Los mismos Voids llegan en oleadas a las [excavadoras gigantes](/wiki/03-Mechanics/Giant-Excavator.md#the-slumbering-voids). Los sectores están en [Sectores de peligro](/wiki/01-General/Danger-Sectors.md).

![Flying in towards the Dormant Swamp: the amber notice ring and, inside it, the red ring of the zone the guns reach](../../img/wiki-img/shots/swamp-rings.jpg)

## De un vistazo {#at-a-glance}

<!-- swamp-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Dónde**: La esquina superior izquierda de `DS-4`: el centro está en 5.000 / 5.000
- **Aparece**: Desde el día 11 de la temporada hasta el reinicio
- **La zona**: 4.300 unidades alrededor del centro: lo más lejos que llegan los cañones
- **El aviso**: Una nave que cruza el anillo a 4.800 unidades del centro recibe una línea del Sistema
- **Camuflaje**: Ningún cañón ve jamás una nave camuflada, ni una dentro de la ventana de un EMP
- **Los alienígenas**: 5 Inert Masses se quedan a menos de 2.400 unidades del centro. El Unwakened duerme en el centro. 2 Slumbering Voids patrullan entre 4.600 y 6.500 unidades del centro.
- **El Enjambre Dormant**: Aparece en 9.417 / 6.606, a 4.700 unidades del centro y fuera de la zona
- **Rocas**: Ningún asteroide queda a menos de 4.900 unidades del centro

<!-- swamp-glance:end -->

## Los cañones {#the-guns}

Las torretas del pantano disparan a la **nave más cercana que puedan ver** dentro de su alcance, y a ninguna otra: la zona es el círculo que alcanza la más lejana de ellas. No son naves, pero desde que se abrió el Deep Void cada una tiene puntos de vida: haz clic en una torreta para disparar tus láseres contra ella, y un cohete que estalle cerca también la daña. Una torreta destruida sigue destruida hasta que vuelve el Unwakened. Sus disparos son reales, y el mundo escala su daño como escala el arma de cualquier alienígena.

<!-- swamp-guns:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Daño de un disparo, en cada mundo:

| Cañón | Lugar | Dispara cada | Alcance (unidades) | Alpha | Beta | Gamma |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| Torreta de [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | 5.000 / 4.400 | 2 s | 3.640 | 75.000 | 112.500 | 150.000 |
| Torreta de [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) | 5.000 / 4.400 | 5 s | 1.080 | 50.000 | 75.000 | 100.000 |
| Torreta láser × 2 | 3.600 / 5.200; 6.400 / 5.200 | 1 s | 2.500 | 45.000–55.000 | 67.500–82.500 | 90.000–110.000 |

- Un cohete se dispara desde el 82 % del alcance que tiene el mismo cohete en manos de un piloto, para que llegue; una torreta láser dispara una vez por segundo, y su daño se sortea dentro del rango indicado.
- Un N.I.K.E. tiene 35 % de penetración de escudo, que se resta de la absorción de un escudo.
- El N.I.K.E. de la torreta vuela un 25 % más rápido y 2× más lejos que el tuyo: 1.250 unidades por segundo, 8.910 unidades en total, así que una nave que huye de él es perseguida durante un buen trecho.
- Un N.U.K.E. estalla en un radio de 1.013 unidades, con más fuerza en el centro.
- El N.U.K.E. de la torreta vuela un 25 % más rápido y 2× más lejos que el tuyo: 375 unidades por segundo, 2.640 unidades en total, así que una nave que huye de él es perseguida durante un buen trecho.

<!-- swamp-guns:end -->

- **Nada dispara desde fuera de la zona,** y dentro de ella una nave es destruida en segundos: cuanto más se acerca al centro, más cañones se suman, y ni siquiera la Wraith mejor protegida aguanta. Un cohete que ya está en el aire sigue su camino, eso sí, y los cohetes de la torreta vuelan más rápido y más lejos que los tuyos: huir en línea recta de uno no te lo quita de encima.
- **Un camuflaje te mete dentro.** Ninguna torreta ve jamás una nave camuflada, ni una dentro de la ventana de un EMP, a ninguna distancia. Una explosión dirigida a una nave visible que estalla junto a una camuflada la daña igualmente y acaba con su camuflaje.
- **Disparan solo a pilotos,** nunca a alienígenas, pilotos de la corporación ni al enjambre, y la protección de una nave que acaba de volver tras una destrucción vale también contra ellas.
- **El anillo de aviso.** Una nave que cruza el anillo fuera de la zona recibe una línea del Sistema: las torretas disparan a toda nave que ven, y algo duerme en el centro. Se le vuelve a avisar solo cuando ha salido del anillo y ha regresado.
- **Salir.** Si te destruyen allí no puedes volver en el sitio (un sector de peligro solo ofrece la base y el portal más cercano), y si inicias sesión dentro de la zona, te colocan fuera. Un rumbo que marcas con un clic se desvía alrededor de la zona, y un aviso te advierte si el lugar donde haces clic queda dentro.

## Los alienígenas {#the-aliens}

Aquí viven tres alienígenas de la civilización perdida, cada uno con sus propias cifras. Se pagan como el jefe de un enjambre: **según el daño causado**, a todo piloto que haya hecho al menos la parte indicada en [Enjambres](/wiki/05-Swarms/Swarms.md#the-rules-of-every-swarm), y la caja va al piloto que más daño causó. Sus derribos suman a tus puntos PvE de rango como los de una nave de enjambre, en proporción a su paga ([Rangos](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points)). El escudo de cada uno absorbe el {{guide:vitals.absorbance@Slumbering Void;Inert Mass;The Unwakened}} de cada impacto mientras dura ([Escudos](/wiki/03-Mechanics/Shields.md)).

- **Slumbering Void.** El cazador esbelto, el alienígena más rápido del juego (más rápido que una Storm con Afterburner III). Algunos patrullan siempre los alrededores del pantano, y otros llegan en oleadas a las excavadoras. Es agresivo, caza al piloto más cercano que pueda ver y nunca ve una nave camuflada.
- **Inert Mass.** Un casco muerto con grietas violetas, del tamaño de una estación pequeña. Se quedan a una distancia fija del centro del pantano y por ahora no se alejan de él. Dispara **Dormant Lances**: cohetes guiados de larguísimo alcance que siguen a una nave hasta que se camufla, abre una ventana de EMP, entra en un anillo seguro, salta o muere. Es más rápida que cualquier nave, así que solo esas interrupciones sirven. Un asteroide en el camino de una Dormant Lance la detiene, y la Lance daña ese asteroide con su propio daño (nadie cobra por ello), así que una roca protege de una Inert Mass solo durante unos pocos impactos.
- **El Unwakened.** Un monolito que duerme en el centro del pantano, lo más grande de cualquier mapa, tan lento que nunca alcanza a una nave. No dispara nada, pero toda nave dentro de su aura se quema, **camuflada o no**. Desde que se abrió el [Deep Void](/wiki/03-Mechanics/Deep-Void.md) puede ser destruido: se paga por el daño causado, vuelve un día después de su muerte, y la primera muerte de la temporada en cada mundo abre el Threshold de ese mundo. La **Tecnología de radiación** de un piloto reduce su quemadura, hasta 0,40 de ella en el nivel 100.

<!-- swamp-members:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

### Slumbering Void

2 Slumbering Voids patrullan entre 4.600 y 6.500 unidades del centro del pantano; uno que es destruido vuelve {{guide:vitals.respawn@Slumbering Void}} después. Las oleadas de una excavadora traen más del mismo alienígena.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Slumbering Void}} | {{guide:vitals.hull*1.5@Slumbering Void}} | {{guide:vitals.hull*2@Slumbering Void}} |
| Escudo | {{guide:vitals.shield@Slumbering Void}} | {{guide:vitals.shield*1.5@Slumbering Void}} | {{guide:vitals.shield*2@Slumbering Void}} |
| Absorción del escudo | {{guide:vitals.absorbance@Slumbering Void}} | {{guide:vitals.absorbance@Slumbering Void}} | {{guide:vitals.absorbance@Slumbering Void}} |
| Daño de los láseres (una salva por segundo) | {{guide:vitals.dps@Slumbering Void}} | {{guide:vitals.dps*1.5@Slumbering Void}} | {{guide:vitals.dps*2@Slumbering Void}} |
| Velocidad | {{guide:vitals.speed@Slumbering Void}} | {{guide:vitals.speed@Slumbering Void}} | {{guide:vitals.speed@Slumbering Void}} |
| Alcance de los láseres | 800 | 800 | 800 |
| Radio de agresión | {{guide:vitals.aggro@Slumbering Void}} | {{guide:vitals.aggro@Slumbering Void}} | {{guide:vitals.aggro@Slumbering Void}} |
| Créditos | {{guide:spoils.pay.credits@Slumbering Void}} | {{guide:spoils.pay.credits*2@Slumbering Void}} | {{guide:spoils.pay.credits*3@Slumbering Void}} |
| Thulium | {{guide:spoils.pay.thulium@Slumbering Void}} | {{guide:spoils.pay.thulium*2@Slumbering Void}} | {{guide:spoils.pay.thulium*3@Slumbering Void}} |
| Experiencia (XP) | {{guide:spoils.pay.experience@Slumbering Void}} | {{guide:spoils.pay.experience*2@Slumbering Void}} | {{guide:spoils.pay.experience*3@Slumbering Void}} |
| Honor | {{guide:spoils.pay.honor@Slumbering Void}} | {{guide:spoils.pay.honor*2@Slumbering Void}} | {{guide:spoils.pay.honor*3@Slumbering Void}} |
| Puntos PvE por derribo | 10 | 10 | 10 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto |
| :--- |
| {{guide:spoils.box@Slumbering Void}} |

### Inert Mass

5 Inert Masses están a menos de 2.400 unidades del centro; una que es destruida vuelve {{guide:vitals.respawn@Inert Mass}} después. Dispara cada 6 s una [Dormant Lance](/wiki/06-Items/Rockets.md#the-craft-only-rockets) guiada a la nave más cercana que pueda ver: velocidad 750, un vuelo de 5.250 unidades, 40 % de penetración.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Inert Mass}} | {{guide:vitals.hull*1.5@Inert Mass}} | {{guide:vitals.hull*2@Inert Mass}} |
| Escudo | {{guide:vitals.shield@Inert Mass}} | {{guide:vitals.shield*1.5@Inert Mass}} | {{guide:vitals.shield*2@Inert Mass}} |
| Absorción del escudo | {{guide:vitals.absorbance@Inert Mass}} | {{guide:vitals.absorbance@Inert Mass}} | {{guide:vitals.absorbance@Inert Mass}} |
| Daño de cada Dormant Lance | {{guide:behaviour.ability:rocket.damageMin@Inert Mass}}–{{guide:behaviour.ability:rocket.damage@Inert Mass}} | {{guide:behaviour.ability:rocket.damageMin*1.5@Inert Mass}}–{{guide:behaviour.ability:rocket.damage*1.5@Inert Mass}} | {{guide:behaviour.ability:rocket.damageMin*2@Inert Mass}}–{{guide:behaviour.ability:rocket.damage*2@Inert Mass}} |
| Velocidad | {{guide:vitals.speed@Inert Mass}} | {{guide:vitals.speed@Inert Mass}} | {{guide:vitals.speed@Inert Mass}} |
| Alcance de los cohetes | 5.000 | 5.000 | 5.000 |
| Radio de agresión | {{guide:vitals.aggro@Inert Mass}} | {{guide:vitals.aggro@Inert Mass}} | {{guide:vitals.aggro@Inert Mass}} |
| Créditos | {{guide:spoils.pay.credits@Inert Mass}} | {{guide:spoils.pay.credits*2@Inert Mass}} | {{guide:spoils.pay.credits*3@Inert Mass}} |
| Thulium | {{guide:spoils.pay.thulium@Inert Mass}} | {{guide:spoils.pay.thulium*2@Inert Mass}} | {{guide:spoils.pay.thulium*3@Inert Mass}} |
| Experiencia (XP) | {{guide:spoils.pay.experience@Inert Mass}} | {{guide:spoils.pay.experience*2@Inert Mass}} | {{guide:spoils.pay.experience*3@Inert Mass}} |
| Honor | {{guide:spoils.pay.honor@Inert Mass}} | {{guide:spoils.pay.honor*2@Inert Mass}} | {{guide:spoils.pay.honor*3@Inert Mass}} |
| Puntos PvE por derribo | 15 | 15 | 15 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto |
| :--- |
| {{guide:spoils.box@Inert Mass}} |

### The Unwakened

Hay uno, en el centro del pantano y en ningún otro sitio; vuelve {{guide:vitals.respawn@The Unwakened}} después de ser destruido. Desde que se abrió el Deep Void puede ser destruido, y se paga por el daño causado como los demás alienígenas de aquí.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@The Unwakened}} | {{guide:vitals.hull*1.5@The Unwakened}} | {{guide:vitals.hull*2@The Unwakened}} |
| Escudo | {{guide:vitals.shield@The Unwakened}} | {{guide:vitals.shield*1.5@The Unwakened}} | {{guide:vitals.shield*2@The Unwakened}} |
| Absorción del escudo | {{guide:vitals.absorbance@The Unwakened}} | {{guide:vitals.absorbance@The Unwakened}} | {{guide:vitals.absorbance@The Unwakened}} |
| Daño del aura por segundo, a toda nave dentro | {{guide:behaviour.ability:aura.damagePerSecond@The Unwakened}} | {{guide:behaviour.ability:aura.damagePerSecond*1.5@The Unwakened}} | {{guide:behaviour.ability:aura.damagePerSecond*2@The Unwakened}} |
| Radio del aura | 700 | 700 | 700 |
| Velocidad | {{guide:vitals.speed@The Unwakened}} | {{guide:vitals.speed@The Unwakened}} | {{guide:vitals.speed@The Unwakened}} |
| Radio de agresión | {{guide:vitals.aggro@The Unwakened}} | {{guide:vitals.aggro@The Unwakened}} | {{guide:vitals.aggro@The Unwakened}} |
| Créditos | {{guide:spoils.pay.credits@The Unwakened}} | {{guide:spoils.pay.credits*2@The Unwakened}} | {{guide:spoils.pay.credits*3@The Unwakened}} |
| Thulium | {{guide:spoils.pay.thulium@The Unwakened}} | {{guide:spoils.pay.thulium*2@The Unwakened}} | {{guide:spoils.pay.thulium*3@The Unwakened}} |
| Experiencia (XP) | {{guide:spoils.pay.experience@The Unwakened}} | {{guide:spoils.pay.experience*2@The Unwakened}} | {{guide:spoils.pay.experience*3@The Unwakened}} |
| Honor | {{guide:spoils.pay.honor@The Unwakened}} | {{guide:spoils.pay.honor*2@The Unwakened}} | {{guide:spoils.pay.honor*3@The Unwakened}} |
| Puntos PvE por derribo | 112 | 112 | 112 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto |
| :--- |
| {{guide:spoils.box@The Unwakened}} |

<!-- swamp-members:end -->

## Con el Deep Void {#with-the-deep-void}

Lo que el Deep Void cambió aquí, en resumen:

- **El Unwakened puede ser destruido.** Ya no es inmune: se paga por el daño causado, como los demás alienígenas de aquí, y vuelve un día después de su muerte.
- **Los cañones pueden ser destruidos.** Cada uno de los tres cañones (la torreta de cohetes, que dispara tanto el N.I.K.E. como el N.U.K.E., y las dos torretas láser) tiene ahora puntos de vida, y los láseres y los cohetes los dañan. Un cañón destruido sigue destruido hasta que vuelve el Unwakened.
- **La primera muerte abre el Threshold.** La primera muerte del Unwakened en una temporada abre, en cada mundo, el Threshold de ese mundo en la esquina opuesta de `DS-4`, donde empieza el [Deep Void](/wiki/03-Mechanics/Deep-Void.md).

## Qué hacer aquí {#what-to-do-here}

- **La primera muerte abre el camino.** La primera muerte del Unwakened en una temporada abre el Threshold de su mundo y, con él, el camino al [Deep Void](/wiki/03-Mechanics/Deep-Void.md); dentro de la zona los cañones destruyen una nave en segundos. Fuera de la zona, los Voids que patrullan, en un anillo alrededor de la zona, son la primera línea del pantano y el lugar donde un grupo puede combatir sin los cañones.
- **Combate a los Voids con penetración.** El gran escudo de un Void absorbe el {{guide:vitals.absorbance@Slumbering Void;Inert Mass;The Unwakened}} de un impacto y casi no importa: el casco que hay detrás es pequeño. Cuanta más penetración de escudo tengan tus láseres, antes cae ([Láseres y munición](/wiki/06-Items/Lasers.md)).
- **Mantente lejos de las Lances.** Una Inert Mass ve muy lejos y a una Lance no se le escapa: rompe su sujeción con un camuflaje, un EMP, un anillo seguro o un salto, o sal de su alcance. Una Mass es un combate largo incluso para un grupo grande de las naves más fuertes.
- **El Enjambre Dormant** aparece ahora justo fuera de la zona, así que un grupo puede esperarlo sin los cañones. Consulta [Enjambre Dormant](/wiki/05-Swarms/Dormant-Swarm.md).

## Dónde leer más {#where-to-read-more}

- [Sectores de peligro](/wiki/01-General/Danger-Sectors.md): qué cambió el día 11.
- [Excavadora gigante](/wiki/03-Mechanics/Giant-Excavator.md): las oleadas de Slumbering Voids y lo que guardan.
- [Enjambres](/wiki/05-Swarms/Swarms.md) y [Enjambre Dormant](/wiki/05-Swarms/Dormant-Swarm.md): cómo paga el derribo de un jefe.
- [Cohetes](/wiki/06-Items/Rockets.md#the-craft-only-rockets): el N.I.K.E. y el N.U.K.E. que dispara la torreta.
- [Agujero negro](/wiki/03-Mechanics/Black-Hole.md): el otro peligro de `DS-4`.
- [Cajas de carga](/wiki/03-Mechanics/Cargo.md): las cajas que sueltan los alienígenas.
