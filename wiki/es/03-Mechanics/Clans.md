<!-- wiki-i18n source: cc29967a9f16c91b -->
<!-- wiki-i18n title: Clanes -->
# Clanes {#clans}

Fundar un clan o unirte a uno te permite reunir recursos, mejorar el banco compartido, fijar tasas de impuesto, coordinarte con los miembros de tu facción y gestionar la diplomacia. Un clan también tiene trabajo que hacer en conjunto: cada día recibe una **línea diaria** de misiones que termina con un jefe que solo el clan puede dañar, y los puntos que gana compran **mejoras permanentes** para cada miembro. (En la página Clan del juego un clan se llama *flota*; sus puntos y mejoras se llaman allí puntos de flota y mejoras de la flota.)

**En un minuto**

- Cada día de temporada tu clan recibe una [línea diaria](#daily-line): cuatro misiones hechas en orden (derribar alienígenas, volar una distancia y, algunos días, abatir jefes de enjambre) y después un [guardián del clan](#clan-wardens), un jefe que invocas tú y que solo tu clan puede dañar.
- Cada paso terminado paga puntos de clan al instante: 15, 15, 20, 20 y 30, o sea **100 puntos** por una línea completa.
- El líder y los colíderes gastan los puntos en tres [mejoras](#clan-points-and-boosts) de diez niveles cada una: **Daño** (hasta +5 %), **Thulium** (hasta +10 %) y **Créditos** (hasta +10 %).
- Un clan que termina todas las líneas ha comprado todos los niveles el **día 12 de la temporada**. Los puntos y los niveles vuelven a empezar con cada reinicio.
- Necesitas al menos **tres miembros** que hayan hecho su parte y unos cinco pilotos para el combate contra el guardián.
- La línea y las mejoras requieren un juego de la versión 0.4.10 o posterior.

![Buying a level of a clan boost: the sheet shows the level, the bonus the whole fleet gets and the cost in clan points](../../img/wiki-img/shots/clan-boosts.jpg)
![Summoning a Warden for the clan](../../img/wiki-img/shots/clan-warden.jpg)

## Progreso del clan {#clan-progression}

Los clanes empiezan en el nivel 1 y pueden mejorar hasta el nivel 5. Mejorar el clan requiere créditos, que se pagan del **Banco del clan**. Las mejoras aumentan la capacidad de miembros y los límites diarios de pago.

| Nivel del clan | Límite de miembros | Límite diario de pago (por miembro) | Costo de mejora (créditos) |
| :---: | :---: | :---: | :--- |
| **Nivel 1** | 10 | 1.000.000 Cr | — |
| **Nivel 2** | 25 | 2.000.000 Cr | 10.000.000 Cr |
| **Nivel 3** | 50 | 3.000.000 Cr | 100.000.000 Cr |
| **Nivel 4** | 75 | 4.000.000 Cr | 1.000.000.000 Cr |
| **Nivel 5** | 100 | 5.000.000 Cr | 10.000.000.000 Cr |

---

## Economía e impuestos del clan {#clan-economy-taxation}

Los clanes funcionan con un sistema financiero basado en impuestos:

### 1. Impuesto diario {#1-daily-taxation}

- **Tasa de impuesto**: el líder o los colíderes pueden fijar una tasa de impuesto diaria de entre el **0 % y el 5 %**.
- **Cobro automático**: una vez al día (UTC), el servidor cobra automáticamente los impuestos a todos los miembros del clan.
- **Fórmula**: el impuesto se calcula como `ClanTaxRate` del saldo actual de créditos de cada miembro.
  - *Ejemplo*: si tienes 10.000.000 de créditos y el impuesto del clan es del 2 %, se descontarán 200.000 créditos de tu cuenta y se ingresarán en el Banco del clan.
  - También se pueden hacer donaciones voluntarias de créditos, hasta el límite de la sección siguiente.

### 2. Donaciones {#2-donations}

- **Donar**: cualquier miembro puede enviar créditos al Banco del clan desde la página Clan. La ventana muestra lo que aún puedes enviar.
- **Límite de donaciones**: un piloto puede enviar como máximo **1.000.000 de créditos a clanes en cualquier periodo de 24 horas**, contando todos los clanes en los que haya estado. Salir de un clan y unirse a otro no da una asignación nueva.
- **Sin reinicio diario**: las 24 horas se desplazan. Cada donación deja de contar exactamente 24 horas después de hacerse, y la ventana te dice cuándo ocurre con la más antigua y cuánto se recupera. Una donación que supere lo que queda se rechaza entera.
- El impuesto diario no es una donación y no gasta tu asignación.

### 3. Pagos del banco {#3-bank-payouts}

- **Límites de pago**: los líderes y oficiales del clan pueden repartir créditos del Banco del clan a miembros concretos.
- **Límite diario**: un miembro no puede recibir más de `1,000,000 * ClanLevel` créditos en pagos en un mismo día natural (UTC).

---

## Jerarquía y rangos {#hierarchy-roles}

Los clanes usan una estructura de rangos basada en roles para gestionar los permisos:

- **Líder (rol 3)**: tiene acceso administrativo completo, incluido mejorar, fijar impuestos, la diplomacia, los ascensos, las expulsiones y la disolución del clan.
- **Colíder (rol 2)**: puede fijar tasas de impuesto, pagar créditos, gestionar la diplomacia y ascender o degradar a rangos inferiores.
- **Veterano (rol 1)**: miembro de confianza que puede aceptar solicitudes nuevas de ingreso al clan.
- **Miembro (rol 0)**: jugador normal sin permisos administrativos.

### Tabla de permisos {#permissions-table}

| Acción | Líder | Colíder | Veterano | Miembro |
| :--- | :---: | :---: | :---: | :---: |
| **Disolver el clan** | ✅ | ❌ | ❌ | ❌ |
| **Mejorar el clan** | ✅ | ❌ | ❌ | ❌ |
| **Fijar la tasa de impuesto** | ✅ | ✅ | ❌ | ❌ |
| **Pagar créditos** | ✅ | ✅ | ❌ | ❌ |
| **Gestionar la diplomacia** | ✅ | ✅ | ❌ | ❌ |
| **Comprar mejoras del clan** | ✅ | ✅ | ❌ | ❌ |
| **Invocar al guardián del clan** | ✅ | ✅ | ❌ | ❌ |
| **Ascender / expulsar** | ✅ | ✅* | ❌ | ❌ |
| **Aceptar solicitudes** | ✅ | ✅ | ✅ | ❌ |

*\*Los colíderes solo pueden ascender, degradar o expulsar a miembros de un rango inferior al suyo.*

### Cuando el líder se va {#when-the-leader-leaves}

Un líder no puede salir de un clan que aún tiene otros miembros: antes debe ascender a un colíder a líder (el líder pasa a colíder) o salir el último, lo que disuelve el clan. Si el líder elimina su cuenta (Configuración › Cuenta), el liderazgo pasa al miembro de mayor rango y, en caso de empate, al que lleve más tiempo; un líder que esté solo en el clan lo disuelve, banco incluido.

---

## Línea diaria {#daily-line}

Cada clan recibe una **línea diaria** al día: cinco pasos, hechos **en orden**, por todo el clan junto. Los cuatro primeros son misiones: derribar tantos alienígenas, volar tanta distancia o, algunos días, abatir jefes de enjambre. El quinto es un **guardián del clan**, un jefe al que invocas y destruyes. Abre **Comunidad › Clan** y su pestaña **Operaciones** para ver la línea de hoy, el paso abierto con su barra, tu propia parte y el tiempo que queda.

### Los cinco pasos {#the-five-steps}

| Paso | Qué | Puntos de clan |
| :---: | :--- | ---: |
| 1 | Primera misión | 15 |
| 2 | Segunda misión | 15 |
| 3 | Tercera misión | 20 |
| 4 | Cuarta misión | 20 |
| 5 | El guardián del clan del día | 30 |
| | **Una línea terminada** | **100** |

- Solo cuenta el **paso abierto**. Un derribo hecho mientras el paso 1 está abierto cuenta para el paso 1 y para nada más. Cuando el paso 1 termina, el paso 2 se abre desde cero. Lo que derribes por encima del objetivo de un paso no se guarda para el siguiente.
- Un paso paga sus puntos **en el momento en que termina**. Un clan que termina las cuatro misiones y luego no consigue reunir una tripulación para el guardián conserva igualmente **70 puntos**.
- El trabajo de todos va a **un solo contador compartido**: los derribos del alienígena del paso abierto y la distancia que vuelan todos tus miembros se suman, así que nadie tiene que hacer un paso solo.

### El día {#the-day}

- El día de un clan es un **día de temporada**: 24 horas contadas desde el inicio de la temporada ([Cronología del reinicio](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule)). Una línea nueva empieza a la misma hora cada día, que no es la medianoche UTC (el impuesto diario del clan sigue cobrándose a medianoche UTC). La pestaña Operaciones cuenta atrás hasta el cambio.
- Una línea que no se termina **caduca** cuando acaba el día. Los pasos ya hechos conservan sus puntos, el progreso del paso abierto se pierde y no se puede recuperar. Las líneas corren los días de temporada 1 a 29.
- Los pilotos del clan que están conectados reciben una línea del Sistema cuando empieza la línea nueva, cuando se termina un paso y **una hora antes del cambio** si la línea no está terminada.

### Niveles de dificultad {#difficulty-tiers}

Cada día el juego toma el **nivel medio de los cinco pilotos de mayor nivel** del clan (todos, si tiene menos de cinco) y fija con él la categoría del día:

| Categoría | Nivel medio | Guardián |
| :--- | :--- | :---: |
| Recluta | menos de 4 | I |
| Veterano | de 4 a menos de 7 | II |
| Élite | 7 o más | III |

La categoría decide cuántos alienígenas piden las misiones, qué alienígena pide el paso «pesado» y lo fuerte que es el guardián. **Los puntos son los mismos en todas las categorías.** Los pilotos nuevos de nivel bajo no hunden la categoría: solo cuentan los cinco mejores.

### Quién cuenta {#who-counts}

- **Cuenta el total del clan.** Las barras de la pestaña Operaciones son las de todo el clan.
- **Tu mínimo.** Para compartir la recompensa del día debes hacer el **5 % del trabajo del día**, unos ocho minutos de caza real. La pestaña lo muestra como «Tu trabajo de hoy: 312 de 469 unidades». Una unidad de trabajo es un segundo de juego: un derribo cuenta lo que se tarda en encontrar y destruir a ese alienígena, y un tramo de vuelo lo que se tarda en volarlo. Para un clan Veterano un Seeker vale unas 12 unidades, un Phantasm 22, un Bulwark 123 y 1.000 unidades voladas unas 5; el mínimo es de 446 a 480 unidades, sea cual sea el día y la categoría.
- **Al menos tres miembros** deben haber alcanzado su mínimo para que un paso pueda terminar. Si un paso está lleno y han llegado menos, **espera** («El paso 3 está lleno, pero solo 2 miembros han alcanzado su mínimo»), y los derribos del alienígena de ese paso siguen sumando al trabajo de los miembros que los hicieron hasta que llegue el tercero. Un clan de menos de tres pilotos no puede terminar ningún paso.
- **Quién se lleva un derribo.** El piloto al que se le paga el derribo y sus compañeros de grupo a menos de 4.000 unidades que dispararon en los últimos 15 segundos ([Grupos](/wiki/03-Mechanics/Groups.md#sharing-kills)). Un clan cuenta un derribo **una sola vez**, por muchos pilotos suyos que hubiera en el grupo, y el trabajo del derribo se reparte a partes iguales entre ellos. Dos clanes en un grupo lo cuentan una vez cada uno.
- **Qué derribos.** Solo el alienígena del paso abierto: el Seeker, Phantasm, Bulwark o Goombah normales. Las naves de enjambre, otros pilotos y los ayudantes de un guardián no cuentan como esos alienígenas. Vale cualquier mundo, y un derribo cuenta más en un mundo más fuerte: **1 en Alpha, 1,5 en Beta, 2 en Gamma** ([Mundos](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)). Un paso de jefes cuenta los jefes de los [enjambres](/wiki/05-Swarms/Swarms.md), uno por cada clan que tenga un piloto que haya causado al menos el 5 % del daño.
- **Volar.** Un paso de patrulla cuenta la distancia que vuela cada piloto fuera de las zonas seguras; cinco pilotos que vuelan juntos suman cinco veces la distancia.
- **Entrar y salir.** Lo que hiciste sigue contando si te vas. Un piloto que entra cuenta desde ese momento.

### Las siete líneas {#the-seven-lines}

Las líneas van en un ciclo de siete: la línea del día de temporada *d* es la número 1 + ((*d* − 1) mod 7), así que cada una vuelve cada siete días. Las cifras son para un clan **Recluta / Veterano / Élite**. Las dos líneas **Swarm Break** piden jefes de enjambre y solo llegan desde el día 4, cuando aparecen los [enjambres](/wiki/05-Swarms/Swarms.md). Todas las cifras están hechas para unas **2,6 horas de juego en total**, media hora cada uno con cinco pilotos (una estimación, no una medición).

| Línea | Días de temporada | Paso 1 | Paso 2 | Paso 3 | Paso 4 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Seeker Sweep | 1, 8, 15, 22, 29 | 150 / 300 / 425 Seeker | 115.000 / 155.000 / 185.000 unidades | 21 / 70 / 130 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah |
| Phantasm Purge | 2, 9, 16, 23 | 40 / 140 / 270 Phantasm | 60 / 120 / 170 Seeker | 175.000 / 230.000 / 275.000 unidades | 26 Phantasm / 15 Bulwark / 17 Goombah |
| Long Haul | 3, 10, 17, 24 | 290.000 / 385.000 / 460.000 unidades | 90 / 180 / 260 Seeker | 26 / 85 / 170 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah |
| Swarm Break I | 4, 11, 18, 25 | 75 / 150 / 220 Seeker | 3 Boss Seeker / 3 Boss Seeker / 2 Pirate Boss | 26 / 85 / 170 Phantasm | 30 Phantasm / 18 Bulwark / 21 Goombah |
| Heavy Iron | 5, 12, 19, 26 | 40 Phantasm / 24 Bulwark / 28 Goombah | 21 / 70 / 130 Phantasm | 175.000 / 230.000 / 275.000 unidades | 75 / 150 / 220 Seeker |
| Swarm Break II | 6, 13, 20, 27 | 75 / 150 / 220 Seeker | 21 / 70 / 130 Phantasm | 4 Boss Seeker / 1 Pirate Boss / 3 Pirate Boss | 350.000 / 460.000 / 550.000 unidades |
| Grand Round | 7, 14, 21, 28 | 100 / 210 / 300 Seeker | 26 / 85 / 170 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah | 230.000 / 305.000 / 365.000 unidades |

### Tu recompensa {#the-reward-for-you}

Cuando la línea está terminada, cada miembro que alcanzó el mínimo y sigue en el clan cobra, aunque esté desconectado. El pago es fijo: no lo cambian las mejoras, los potenciadores ni el mundo.

| Categoría | Créditos | Thulium |
| :--- | ---: | ---: |
| Recluta | 5.000 | 20 |
| Veterano | 15.000 | 60 |
| Élite | 22.000 | 90 |

---

## Guardianes del clan {#clan-wardens}

Un **guardián del clan** es el jefe del final de la línea diaria. No es uno de los [enjambres](/wiki/05-Swarms/Swarms.md) públicos que vagan por un sector: tu clan **lo invoca** y **solo tu clan puede dañarlo**. Tres guardianes se turnan, uno por día: el día 1 **Brood**, el día 2 **Siege**, el día 3 **Wrath**, el día 4 otra vez Brood, y así sucesivamente (el día 15 toca Wrath). Cada uno viene en tres fuerzas, **I, II y III**, que fija la categoría del clan. Un guardián es un alienígena de un tipo propio, como las naves de un enjambre: no cuenta como Seeker, Phantasm ni ningún otro alienígena.

| Guardián | Días de temporada | Papel | Cómo lucha |
| :--- | :--- | :--- | :--- |
| **Brood Warden** | 1, 4, 7, 10 … | Guardián de la colmena: reparte tu fuego | Cuatro pequeños **Brood Drones** curan su casco y llega uno nuevo cada 8 segundos mientras haya menos de cuatro vivos. Destruye primero los drones y luego al guardián. |
| **Siege Warden** | 2, 5, 8, 11 … | Rompesitios: no dejes de moverte | Se desplaza y dispara un [cohete Rivet](/wiki/06-Items/Rockets.md#the-twelve-rockets) recto al primer piloto que lo golpeó, y se repara solo. Dos **Siege Escorts** añaden fuego láser. No dejes de moverte y túrnense como objetivo. |
| **Wrath Warden** | 3, 6, 9, 12 … | Señor de la guerra: vence a la furia | Lucha sin moverse y se repara solo. Por debajo de la mitad del casco, sus láseres golpean **una vez y media más fuerte**. Dos **Wrath Guards** añaden fuego láser. Derríbalo rápido y mantén los escudos arriba. |

### Invocar a un guardián {#calling-a-warden}

- **Cuándo.** Después de terminar el paso 4. Un clan tiene **dos invocaciones al día**, un solo guardián fuera a la vez, y al día le deben quedar **al menos 30 minutos**.
- **Quién.** El líder o un colíder.
- **Cómo.** En vuelo: el botón **Invocar aquí** aparece en la pantalla de vuelo en cuanto el paso 4 está terminado y te pide confirmar. Colócate fuera de las zonas seguras, en un sector de corporación **x-2, x-3 o x-4** (de cualquier corporación) de tu mundo. La pestaña Operaciones muestra el guardián del día, las invocaciones que quedan y por qué el botón está atenuado, pero un guardián se invoca desde la nave.
- **Dónde aparece.** A entre 3.000 y 4.500 unidades de tu nave, en tu mundo: solo los pilotos de ese mundo pueden llegar a él. La pestaña recomienda **x-2 para un clan Recluta, x-3 para Veterano y x-4 para Élite**. Siguen valiendo las [reglas de PvP](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) habituales del sector que elijas.
- **Calentamiento.** Permanece **90 segundos** con escudo y pasivo («cargando») y cada piloto del clan que esté conectado sabe dónde. Vuela hacia él mientras se carga: pasados los 90 segundos está activo.
- **Solo tu clan.** Los disparos de pilotos de cualquier otro clan se ignoran y no hacen que responda.
- **Cómo termina.** Cuando lo destruyen. Se **retira** 40 minutos después de activarse, cuando acaba el día, cuando ningún piloto de tu clan lleva 2 minutos en vuelo en su mapa o cuando el servidor se reinicia (esa invocación se devuelve). Un guardián que se retira cuesta una invocación, y la siguiente es el mismo guardián con toda su fuerza.

### Combatir a un guardián {#fighting-a-warden}

- **Un guardián lucha contra el primer piloto que lo golpeó**, como cualquier jefe: deja que empiece la nave más resistente de la tripulación y usa [Shield Surge y Emergency Repair](/wiki/03-Mechanics/Abilities.md).
- **Lleva munición x2** ([Láseres](/wiki/06-Items/Lasers.md#laser-ammunition)). Una tripulación de cinco gana incluso con munición x1, más despacio; una de tres, no.
- **Brood:** los drones curan su casco, y una tripulación de tres que los ignora pierde. Destrúyelos primero: uno muere en un segundo o menos bajo el fuego de cinco pilotos y el siguiente llega a los 8 segundos.
- **Siege:** sus cohetes son rectos y sin guía, así que una nave que no deja de moverse esquiva la mayoría. No dejes de moverte y túrnense como objetivo.
- **Wrath:** cuando su casco baja de la mitad, cada salva golpea una vez y media más fuerte, así que la segunda mitad del combate es la peligrosa. Derriba la primera mitad rápido, mantén los escudos arriba y guarda Emergency Repair para la furia.

### Qué tripulación hace falta {#how-big-a-crew}

> [!NOTE]
> Estos tiempos están **calculados** con las cifras de abajo, no medidos en juego: una tripulación en las naves y el equipo para los que está hecha la categoría, todos disparando al guardián. Un guion significa que no lo calculamos.

| Tripulación | Con munición x2 | Con munición x1 |
| :--- | :--- | :--- |
| 2 pilotos | pierden contra Brood y Siege; ganan a Wrath en unos 17 minutos | – |
| 3 pilotos | ganan en 9 a 10 minutos, por la mínima: el casco del tanque acaba bajo y puede caer algún piloto | pierden |
| 5 pilotos | ganan en unos 5 minutos | ganan en 12 a 14 minutos |
| 7 pilotos | ganan en unos 3,4 minutos | – |
| 10 pilotos | ganan en unos 2,3 minutos | – |

Una tripulación de una categoría inferior a la del guardián pierde: una tripulación Recluta de cinco no puede matar a un guardián Veterano, ni una Veterana a uno de Élite. El guardián de **tu** clan siempre se ajusta a **tu** categoría.

### Cifras de los guardianes {#warden-numbers}

Los guardianes tienen las mismas cifras en todos los mundos (las de Alpha), y también su paga. Cada dron, escolta o guardia tiene las cifras de la segunda tabla, y se quedan junto al guardián: un Brood Drone cura el casco del guardián, un Siege Escort o un Wrath Guard dispara láseres.

| Guardián | Casco | Escudo | Daño de los láseres (una salva por segundo) | Velocidad | Alcance de los láseres | Se repara solo (casco por segundo) | Cohete y segundos entre disparos |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| Brood Warden I | 166.000 | 136.000 | 43 | 90 | 600 | – | – |
| Brood Warden II | 288.000 | 236.000 | 259 | 90 | 700 | – | – |
| Brood Warden III | 1.060.000 | 870.000 | 1.030 | 90 | 800 | – | – |
| Siege Warden I | 143.000 | 117.000 | 16 | 110 | 600 | 215 | Rivet I: 24 |
| Siege Warden II | 248.000 | 203.000 | 97 | 110 | 700 | 375 | Rivet II: 12 |
| Siege Warden III | 915.000 | 745.000 | 615 | 110 | 800 | 1.385 | Rivet III: 8 |
| Wrath Warden I | 163.000 | 133.000 | 32 | 90 | 700 | 215 | – |
| Wrath Warden II | 282.000 | 231.000 | 194 | 90 | 800 | 375 | – |
| Wrath Warden III | 1.040.000 | 850.000 | 820 | 90 | 900 | 1.385 | – |

| Ayudante | Cuántos | Casco | Escudo | Daño de los láseres (una salva por segundo) | Velocidad | Cura al guardián (casco por segundo) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Brood Drone I | 4 | 700 | 500 | 4 | 170 | 120 |
| Brood Drone II | 4 | 1.200 | 900 | 26 | 170 | 210 |
| Brood Drone III | 4 | 4.000 | 3.500 | 105 | 170 | 770 |
| Siege Escort I | 2 | 4.300 | 3.500 | 2 | 175 | – |
| Siege Escort II | 2 | 7.400 | 6.100 | 15 | 175 | – |
| Siege Escort III | 2 | 27.500 | 22.500 | 95 | 175 | – |
| Wrath Guard I | 2 | 4.900 | 4.000 | 6 | 180 | – |
| Wrath Guard II | 2 | 8.500 | 6.900 | 39 | 180 | – |
| Wrath Guard III | 2 | 31.000 | 25.500 | 165 | 180 | – |

### Paga y botín {#warden-pay-and-loot}

Un guardián paga lo mismo que un montón del alienígena pesado de la categoría: **30 Phantasm** para un guardián I, **24 Bulwark** para un II y **16 Goombah** para un III. Es un solo bote, repartido según el daño entre los pilotos que causaron al menos el 5 % del daño, igual que con el líder de un [enjambre](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays). Tus [mejoras del clan](#what-the-boosts-apply-to) se aplican a tu parte. Según nuestro cálculo, los créditos cubren la munición x1 que quema una tripulación de cinco, y la munición x2 cuesta más Thulium del que paga el guardián: es una lucha por los puntos y el cofre.

| Fuerza del guardián | Créditos | Thulium | Experiencia (XP) | Honor |
| :--- | ---: | ---: | ---: | ---: |
| I | 90.000 | 360 | 9.000 | 180 |
| II | 120.000 | 600 | 19.200 | 240 |
| III | 240.000 | 1.200 | 48.000 | 384 |

El guardián suelta **un cofre** para el piloto que causó más daño; es suyo y de su clan durante 30 segundos ([Carga](/wiki/03-Mechanics/Cargo.md)). Una probabilidad entre paréntesis vale para cada una de esas tiradas: (5 × 50 %) son cinco tiradas con un 50 % de probabilidad cada una.

| Guardián | Objeto | I | II | III |
| :--- | :--- | :---: | :---: | :---: |
| Brood Warden | Ship Fragment | 3–5 | 8–12 | 15–25 |
| Brood Warden | Advanced Plasma | 100–200 | 300–600 | – |
| Brood Warden | Daraxium | 1–2 (5 × 50 %) | – | – |
| Brood Warden | Nyxite | – | 2–4 (5 × 50 %) | – |
| Brood Warden | Ultra Core | – | – | 300–500 |
| Brood Warden | Quorvium | – | – | 5–10 (60 %) |
| Siege Warden | Ship Fragment | 2–4 | 6–10 | 12–20 |
| Siege Warden | Siphon Battery | 100–200 | 300–500 | 800–1.200 |
| Siege Warden | Cohete de la tienda de créditos (un tipo, al azar) | 2–3 | 5–8 | 8–12 |
| Siege Warden | Reinforced Hull Plate | – | 1 (30 %) | – |
| Siege Warden | Cohete épico (un tipo, al azar) | – | – | 1–2 (50 %) |
| Wrath Warden | Ship Fragment | 4–6 | 8–12 | – |
| Wrath Warden | Cataclysite | 3–5 | 5–10 | – |
| Wrath Warden | Reinforced Hull Plate | 1 (25 %) | 1 (50 %) | 1–2 (70 %) |
| Wrath Warden | Power Core | – | 1 (15 %) | 1 (35 %) |
| Wrath Warden | Quorvium | – | – | 5–10 (70 %) |
| Wrath Warden | Ancient Control Unit | – | – | 1 (8 %) |

Un guardián cuenta con su propio nombre en tus estadísticas de derribos y suma puntos PvE a tu [rango](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points): **13 a 35** por el líder, según el guardián y su fuerza (un guardián III es el que más vale), y **1 a 6** por cada ayudante, más cuanto más fuerte es la tripulación.

---

## Puntos y mejoras del clan {#clan-points-and-boosts}

Los puntos de clan pertenecen al clan. Cada paso que el clan termina suma a su saldo. El **líder y los colíderes** lo gastan en la tarjeta **Mejoras de la flota** de la pestaña Operaciones: tres mejoras de diez niveles cada una, y todos los miembros las tienen al instante. Una compra es definitiva: no hay reembolso ni reasignación.

### Las tres mejoras {#the-three-boosts}

| Mejora | Niveles | Por nivel | Nivel máximo | Actúa sobre |
| :--- | :---: | :---: | :---: | :--- |
| **Daño de flota** | 10 | +0,5 % | +5 % | Daño láser a alienígenas y pilotos |
| **Thulium de flota** | 10 | +1 % | +10 % | Thulium de derribos y recompensas de misiones |
| **Créditos de flota** | 10 | +1 % | +10 % | Créditos de derribos y recompensas de misiones |

### Precios {#boost-prices}

El precio de un nivel es **22 puntos de clan más 4 por cada nivel anterior**, y es el mismo para las tres mejoras: 400 puntos por una mejora, **1.200 por las tres**, que son doce líneas terminadas.

| Nivel | Precio | Total de esta mejora | Daño de flota | Thulium de flota | Créditos de flota |
| :---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 22 | 22 | +0,5 % | +1 % | +1 % |
| 2 | 26 | 48 | +1 % | +2 % | +2 % |
| 3 | 30 | 78 | +1,5 % | +3 % | +3 % |
| 4 | 34 | 112 | +2 % | +4 % | +4 % |
| 5 | 38 | 150 | +2,5 % | +5 % | +5 % |
| 6 | 42 | 192 | +3 % | +6 % | +6 % |
| 7 | 46 | 238 | +3,5 % | +7 % | +7 % |
| 8 | 50 | 288 | +4 % | +8 % | +8 % |
| 9 | 54 | 342 | +4,5 % | +9 % | +9 % |
| 10 | 58 | 400 | +5 % | +10 % | +10 % |

### Sobre qué actúan las mejoras {#what-the-boosts-apply-to}

- **Daño de flota** suma a todo el daño láser que causa tu nave: a alienígenas, naves de enjambre, guardianes y otros pilotos. **No afecta a los cohetes**, de ningún tipo.
- **Thulium de flota y Créditos de flota** suman a la paga de los derribos de alienígenas (los tuyos, tu parte de un jefe y tu parte de un derribo en grupo) y a la recompensa de cada misión que cobras, de nivel, de la estación o Desafío ([Misiones](/wiki/03-Mechanics/Quests.md#rewards)). **No afectan** a las granjas del [Skylab](/wiki/03-Mechanics/Skylab.md#credit-farm-and-thulium-farm), a los pagos del banco, a los códigos de bonificación ni a la recompensa de la línea diaria.
- **Se suman a tus otras bonificaciones** (potenciadores como el Damage Amp, las mejoras de la [tienda de mejoras permanentes](/wiki/03-Mechanics/Wipe-Timeline.md#the-permanent-buff-store)): los porcentajes se suman. Los amplificadores láser (Amps) no cuentan entre ellos: suman daño fijo, y los porcentajes se aplican al total. Cinco puntos de Daño de flota junto a 50 de otras fuentes dan 55, que es un 3,3 % más de daño que antes.
- **Una fracción no se pierde.** Una mejora suele añadir menos de una unidad a un derribo: el 10 % de los 4 Thulium de un Seeker es 0,4. El juego guarda la fracción y la paga con las unidades de tus siguientes derribos, de modo que diez Seekers pagan los 4 que te corresponden. La fracción que guardas se pierde al cerrar sesión.
- **Entrar y salir.** Un piloto tiene las mejoras desde el momento en que entra en el clan y las pierde en el momento en que se va, lo expulsan o el clan se disuelve. El clan conserva sus niveles.

### Cuánto se tarda {#how-long-it-takes}

Un clan que termina todas las líneas gana 100 puntos al día. Si los oficiales compran por igual en las tres mejoras, tiene **4 niveles tras la primera línea, 10 tras la tercera, 16 tras la quinta y los 30 el día 12 de la temporada**. Catorce líneas han pasado cuando empieza el día 15, así que un clan así tiene dos líneas de margen. Un día que no se termina paga igualmente los pasos hechos. Tras el último nivel la línea sigue corriendo y sigue pagando tu recompensa; los puntos siguen sumando a lo que el clan ganó esta temporada, que muestra el texto emergente de los puntos de clan en la tarjeta Mejoras de la flota.

### Puntos y reinicio {#clan-points-and-the-wipe}

En cada reinicio, los **puntos, los niveles de mejora y las líneas del clan empiezan de nuevo**, así que cada temporada es una nueva carrera hacia las mejoras al máximo. El clan en sí, sus miembros, su banco y su impuesto se quedan como están.

---

## Diplomacia {#diplomacy}

Los clanes pueden establecer relaciones diplomáticas formales con otras organizaciones introduciendo la etiqueta del clan objetivo:

- **Alianza**: clanes aliados formalmente. El estado amistoso se muestra en el mapa.
- **Pacto de no agresión (NAP)**: acuerdo de no iniciar hostilidades.
- **Guerra**: declaración formal de guerra. Los objetivos de guerra se pueden atacar en cualquier lugar sin penalización.

---

## Trae a un amigo {#bringing-a-friend}

Un amigo que sea nuevo en el juego puede unirse con tu código de invitación personal y recibe un paquete inicial; consulta [Invitar amigos](/wiki/03-Mechanics/Invite-Friends.md). Una vez dentro del juego, puede solicitar el ingreso en tu clan como cualquier piloto.
