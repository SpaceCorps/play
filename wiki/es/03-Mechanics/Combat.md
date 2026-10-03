<!-- wiki-i18n source: c5ebaa2ae1a96278 -->
<!-- wiki-i18n title: Combate -->
# Mecánicas de combate {#combat-mechanics}

Esta sección explica cómo se calcula, se aplica y se repara el daño durante los enfrentamientos en SpaceCorps.

## Cálculo del daño {#damage-calculation}

Cuando una nave dispara sus láseres, el servidor calcula el daño resultante con la siguiente secuencia:

### 1. Daño base y variación aleatoria {#1-base-damage-random-variance}

Se suma el daño base de todos los láseres equipados (incluidos los láseres de los drones) y de los amplificadores láser instalados en ellos.
- **Tirada aleatoria**: el daño real de una andanada varía al azar entre el **80 %** y el **100 %** del daño base total.
  - Fórmula: `Roll = (0.8 + (Random * 0.2)) * BaseDamage`

### 2. Golpes críticos {#2-critical-hits}

Cada andanada tiene una probabilidad de ser un golpe crítico.
- **Probabilidad de crítico**: la probabilidad de crítico media de los láseres equipados más la suma de las probabilidades de crítico de todos los amplificadores láser equipados.
- **Multiplicador crítico**: si un disparo es crítico, la tirada de daño se multiplica por **1,5x**. El número de daño de una andanada crítica se muestra en azul hielo, más grande y con un «!».
- Los Quantum Laser 1 y 2 no tienen probabilidad de crítico propia: se la dan sus amplificadores.
- **Daño crítico fijo**: el daño crítico plano de los amplificadores láser se suma después del multiplicador.
  - Fórmula: `CritDamage = (Roll * 1.5) + FixedCritDamage`

### 3. Multiplicadores globales {#3-global-multipliers}

Por último, se aplican los multiplicadores globales (como los potenciadores activos o los multiplicadores de la munición láser, como x2, x3 o x4) para obtener el daño final:
- Fórmula: `FinalDamage = Damage * AmmoMultiplier * (1.0 + BoosterDamagePercent)`
- La munición **Siphon Battery** tiene el multiplicador x1, pero otro destino: su daño sale solo del escudo del objetivo (nunca del casco, sea cual sea la absorción) y pasa a tu propio escudo, hasta tu máximo. Consulta [Láseres y munición](/wiki/06-Items/Lasers.md).

### 3b. Cohetes {#3b-rockets}

Un [cohete](/wiki/06-Items/Rockets.md) tiene su propio daño (un Lancet I hace de 1.600 a 2.000, un Lancet III de 4.800 a 6.000, una N.U.K.E. de 45.000 a 50.000), que se sortea una vez al dispararlo y es el mismo para cualquier nave: tus láseres, amplificadores, potenciadores y munición no lo cambian, y no tiene golpe crítico. Todos los cohetes comparten una misma recarga de **5 segundos**. Un cohete de un solo objetivo tiene **penetración de escudo**: se resta de la absorción de tu objetivo (consulta Recibir daño, más abajo); una explosión daña a todas las naves dentro de su radio, menos cuanto más cerca del borde. Nada limita lo que un cohete le quita a la nave de un piloto: primero el escudo, luego el casco. Los cohetes nunca dañan a tu propia corporación ni a tu propio [grupo](/wiki/03-Mechanics/Groups.md), sean cuales sean las corporaciones que lo formen.

### 4. Encarar al objetivo {#4-facing-the-target}

Una nave o un alienígena que tiene fijado un objetivo y le dispara se gira hacia él, vuele como vuele (en círculos, retrocediendo o quieto), y vuelve a su rumbo cuando deja de disparar.

### 5. Alcance {#5-range}

Una nave dispara una andanada por segundo mientras su objetivo está dentro de su **alcance**, y deja de disparar mientras el objetivo está más lejos: el fuego deja de gastar munición hasta que el objetivo vuelve a estar lo bastante cerca, y el panel del objetivo indica «Fuera de alcance». El alcance es **la media de los alcances de todos tus láseres** (también de los láseres de tus drones), redondeada a la unidad más cercana, y es un único número para toda la nave: dentro de él disparan todos los láseres; fuera, ninguno. Por eso un láser de largo alcance junto a otros cortos no amplía tu alcance: un Starfire-3 (850) y dos Quantum Laser 2 (700) dan 750. Una bonificación de alcance de la Forja cuenta en su propio láser antes de calcular la media. Una nave sin láser no puede disparar sus láseres, y el hangar no muestra alcance para ella (un guion); sus cohetes siguen disparando, cada uno con su propio alcance (consulta [Cohetes](/wiki/06-Items/Rockets.md)). Consulta [Láseres y munición](/wiki/06-Items/Lasers.md) para ver el alcance propio de cada láser.

---

## Recompensas por derribo: reclama quien impacta primero {#kill-rewards-first-hit-claims}

Las recompensas de un alienígena son para el piloto que le disparó primero, no para quien da el último golpe.

- **Reclamar**: el primer piloto cuyo disparo daña a un alienígena lo reclama. Cada impacto tuyo renueva tu reclamación.
- **Perderla**: si no impactas al alienígena durante **10 segundos**, tu reclamación caduca y el siguiente piloto que lo impacte lo reclama. Tu reclamación también termina cuando destruyen tu nave o sales del mapa (por un portal o al cerrar sesión), y volver dentro de esos 10 segundos no te la devuelve.
- **El derribo**: cuando el alienígena es destruido, el piloto que tiene su reclamación se lo lleva todo: créditos, Thulium, XP, honor, el derribo para las misiones y los puntos de reinicio, y la [caja de carga](/wiki/03-Mechanics/Cargo.md). Un piloto que remata un alienígena que otro ha reclamado no recibe nada, y el Registro de juego lo indica. Cuando tu reclamación te paga y otro piloto da el último golpe, el Registro de juego nombra a ese piloto y dice que tu reclamación te paga a ti.
- **Puntos de clasificación**: el derribo también suma puntos PvE a la clasificación del piloto que tiene la reclamación, más cuanto más duro es el alienígena: 1 por un Seeker, 2 por un Phantasm, 4 por un Bulwark, 7 por un Goombah y 16 por un Crystalys (el artículo de cada alienígena indica el suyo). Son solo del piloto que lo derriba: el reparto de recompensas de un grupo no los incluye.
- **Verla**: cuando seleccionas un alienígena que otro piloto ha reclamado, la ventana Objetivo muestra *Reclamado por* ese piloto y *Sin recompensa*.
- Los [pilotos de corporación](/wiki/03-Mechanics/Company-Pilots.md) nunca reclaman un alienígena, y un alienígena que rematan sigue pagando al piloto que tiene su reclamación.
- Un piloto de un [grupo](/wiki/03-Mechanics/Groups.md) reparte lo que paga su reclamación con los compañeros de grupo que están cerca y disparando; la reclamación en sí es solo de ese piloto.
- **Los líderes de los [enjambres](/wiki/05-Swarms/Swarms.md) y los Dormant Pulses son la excepción**: un jefe de enjambre y cada Dormant Pulse cobran según el daño que les causó cada piloto, no según el primer impacto, y su caja de carga es para el piloto que más daño causó ([cómo paga el derribo de un jefe](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Los demás seguidores, los Pirate Scouts y los Seeker Slaves, pagan según la reclamación, como cualquier alienígena. Los puntos PvE de una nave de enjambre están en la página Enjambres.

---

## Alienígenas que solo se defienden {#aliens-that-only-fight-back}

El Seeker y el Goombah nunca empiezan un combate. Cada uno se vuelve contra un piloto que lo impacta (un impacto que haga daño; el fuego de otro alienígena nunca lo provoca), lucha contra el piloto que se describe en [Contra quién lucha un alienígena](#who-an-alien-fights) y lo suelta **10 segundos** después del último impacto que haya recibido de cualquiera. Si lo dejan en paz **30 segundos**, su casco se repara un 2 % de su máximo por segundo. Los demás alienígenas (Phantasm, Bulwark, Crystalys) van a por cualquier piloto sin protección que entre en su radio de agresión (700, 700 y 900 unidades) y nunca reparan su casco; el escudo de todo alienígena se recarga a partir de 15 segundos después de su último impacto.

---

## Contra quién lucha un alienígena {#who-an-alien-fights}

Un alienígena sigue luchando contra **el primer piloto que le disparó** mientras todavía pueda perseguirlo: el piloto está en el mapa, no está en una zona segura, no está camuflado ni dentro de su ventana de EMP, está vivo y lo ha impactado en los últimos **10 segundos** (cada impacto vuelve a empezar esos 10 segundos: una andanada láser, un cohete o el borde de una explosión por igual). Mientras eso se cumpla, los disparos de otros pilotos nunca lo desvían, por cerca que estén o por muchas veces que impacten, de modo que un piloto puede retener a un alienígena mientras otros le disparan.

Cuando el primer piloto queda fuera de combate (sale del mapa, llega a una zona segura, se camufla o dispara un EMP, es destruido o deja de impactar al alienígena durante 10 segundos), el alienígena se vuelve contra el **siguiente** piloto que se sumó al combate, por el orden en que le dispararon por primera vez, y no contra el que lo impactó en último lugar. Un piloto que quedó fuera y vuelve a dispararle se coloca al final de la cola. Un alienígena lleva la cuenta de los primeros **32** pilotos que le dispararon; un 33.º piloto que le dispare no entra en la cola hasta que uno de ellos quede fuera, y en una multitud de cualquier tamaño el alienígena se queda con el primero.

Los [pilotos de corporación](/wiki/03-Mechanics/Company-Pilots.md) cuentan después de todos los jugadores: un alienígena lucha contra un piloto de corporación solo mientras ningún jugador al que aún pueda perseguir le haya disparado, un jugador que dispara a un alienígena con el que lucha un piloto de corporación se lo arrebata, y un piloto de corporación nunca aparta a un alienígena de un jugador. Nada de esto cambia quién se lleva las recompensas del alienígena: eso lo decide la reclamación ([Recompensas por derribo](#kill-rewards-first-hit-claims)).

---

## Los alienígenas pierden el interés {#aliens-lose-interest}

Ningún alienígena te sigue por todo el mapa. Pero un alienígena al que estás **impactando** no está perdiendo el interés, está luchando contigo: durante **10 segundos** después de tu último impacto (cada impacto vuelve a empezar esos 10 segundos, ya sea una andanada láser, un cohete o el borde de una explosión) vuela hacia ti, a su propia velocidad, siempre que estés más allá de su alcance de ataque (Seeker 600, Phantasm y Bulwark 700, Goombah 800, Crystalys 900), y sigue acercándose y disparando hasta tenerte a su alcance. No hay límite de lo lejos que te sigue mientras sigas impactándolo. Un láser que llega más lejos que el arma del alienígena (un Starfire-3 llega a 850 unidades, un Helios Beam a 900) no te permite impactarlo desde donde no puede responder, y una nave más rápida solo lo mantiene detrás de ti mientras sigas disparando. Aun así, te suelta al instante si llegas a una zona segura, te camuflas o sales del mapa.

Cuando varios pilotos impactan al mismo alienígena, este se queda con el primero que le disparó (consulta [Contra quién lucha un alienígena](#who-an-alien-fights)): se acerca a ese piloto y le dispara, así que un grupo que lo rodea justo fuera de su alcance no puede tenerlo yendo de uno a otro sin que llegue nunca a responder.

Un alienígena que te ha tomado como objetivo (un Phantasm, Bulwark o Crystalys al que te acercaste, o cualquier alienígena al que disparaste) y al que no has impactado durante 10 segundos te suelta en cuanto se cumple una de estas condiciones:

- **Nunca le disparaste:** estás a más de **1.200 unidades** de él, o ha volado **2.000 unidades** desde donde empezó la persecución.
- **Le disparaste en el último minuto:** estás a más de **2.500 unidades** de él, o ha volado **3.000 unidades** desde donde empezó la persecución. Un combate que empezaste tú sigue siendo justo.

Un alienígena que te suelta deambula desde donde está, sin ir nunca hacia donde te vio por última vez (ni siquiera cuando te camuflas o disparas un EMP), y no vuelve a elegirte como objetivo durante **8 segundos**, salvo que le dispares. Cada alienígena decide por sí mismo, así que una manada mixta se va dispersando a medida que te alejas. Los alienígenas nunca te siguen a una zona segura ni a través de un portal, y los que te pierden cerca de uno se alejan de él, cada uno por su lado, para no quedarse esperando amontonados. El interés de un alienígena nunca se queda por debajo de su alcance de ataque y su radio de agresión, más 100 unidades.

Los alienígenas no se amontonan: una manada que va tras un piloto deja cierto espacio entre sus naves mientras se acerca (150 unidades entre cascos, así que una manada de Phantasms vuela con las naves separadas 250 unidades, y no casco contra casco), y un alienígena que se pone en camino con otros cerca vuela alejándose de ellos, de modo que una manada que perdió a su piloto se dispersa en todas direcciones.

Volar más rápido solo te ayuda hasta cierto punto: una Protos (150) es más lenta que todos los alienígenas que cazan (Phantasm 160, Bulwark 175, Crystalys 230), así que lo que pone fin a la persecución son esos límites de distancia, no tu velocidad.

---

## Recibir daño y zonas seguras {#taking-damage-safe-zones}

Cuando un enemigo o un NPC impacta tu nave, el daño se procesa así:

### 1. Absorción del escudo {#1-shield-absorption}

El daño entrante se reparte entre los escudos y los puntos de vida según la **absorción media** de tu nave: la media de la absorción de tus escudos, cada uno con la de sus células de escudo, más la mejora Shield Absorbance Boost de la Tienda de temporada (consulta [Mecánicas de los escudos](/wiki/03-Mechanics/Shields.md)). **No tiene un tope del 100 %**: lo que los escudos se llevan de un impacto es tu absorción **menos la penetración de escudo del atacante**, entre el 0 % y el 100 %.
- Los escudos reciben la **absorción** de cada impacto (p. ej., 80 % con el mejor escudo y las mejores células, 56 % con un Basic Shield Core con dos Absorption Shield Cell I), menos la penetración del impacto: el 35 % de un Lancet III deja un 45 % en los escudos de una nave con 80 %, y el resto (allí, el 55 %) va directo a los HP.
- La **penetración de escudo** viene de los cohetes directos (del 10 al 35 %) y de la munición láser x3 y x4 (5 % y 10 %); los alienígenas no tienen. Una nave por encima del 100 % (digamos, 112 %) aguanta en los escudos un impacto entero contra una penetración de hasta la diferencia (allí, 12 %).
- Un escudo demasiado bajo para su parte pasa la diferencia a los HP; si los escudos están totalmente agotados, el **100 %** de todo el daño restante va a los HP.
- Los alienígenas no tienen estadística de absorción: sus escudos reciben el 80 % de cada impacto (menos la penetración del impacto) y su casco, el resto.

### 2. Inmunidad en zona segura {#2-safe-zone-immunity}

La base de cada facción (los mapas X-1) contiene zonas seguras.
- Entrar en una zona segura hace tu nave completamente inmune al daño.
- **Romper la inmunidad**: atacar a un enemigo elimina al instante tu inmunidad de zona segura, aunque estés físicamente dentro de una.
- Un anillo alrededor de cada estación y cada portal te protege cuando han pasado 5 segundos desde que te impactaron y 15 desde que disparaste. Mientras te protege y estás fuera de combate, la ventana del hangar te permite cambiar de nave sin salir del juego: consulta [El hangar en vuelo](/wiki/03-Mechanics/Hangar.md).
- Las estaciones solo están en las bases de origen (`x-1`). Los sectores de peligro (de `DS-1` a `DS-4`) no tienen ninguna: allí los anillos alrededor de los portales son las únicas zonas seguras.

### 3. Bajo ataque en un sector de peligro {#3-under-attack-in-a-danger-sector}

Un salto a través de un portal dura 3 segundos (consulta [Viajes por el mapa espacial](/wiki/01-General/Spacemap%20Travel.md)). En los sectores de peligro (`DS-1` a `DS-4`), un piloto cuya nave haya sido impactada por otro piloto o por un alienígena en los últimos **10 segundos** no puede iniciar uno, y un impacto cancela un salto en curso. En cualquier otro lugar, los ataques nunca interrumpen un salto, y nada interrumpe la recogida de una [caja de carga](/wiki/03-Mechanics/Cargo.md).

---

## Recuperación y reparación {#recovery-repair}

Para recuperarse del combate, los pilotos pueden contar con la regeneración pasiva y con bots de utilidad activos:

### 1. Regeneración pasiva del escudo {#1-shield-passive-regeneration}

- **Funcionamiento**: restaura cada segundo tantos puntos de escudo como la velocidad de recarga de tu escudo.
- **Retraso**: el combate la interrumpe; la regeneración pasiva solo se reanuda tras **15 segundos** sin recibir daño.

### 1b. Siphon Battery {#1b-siphon-battery}

La munición [Siphon Battery](/wiki/06-Items/Lasers.md) suma al instante a tu escudo el escudo que le drena a un objetivo, hasta tu máximo. Ganar escudo no es recibir daño, así que no retrasa tu regeneración pasiva.

### 2. Repair Drones (reparación del casco) {#2-repair-drones-hull-repair-}

- **Funcionamiento**: si equipas un Repair Drone (en los extras del hangar), lo activas desde la barra rápida (arrástralo desde el selector de Extras a una ranura) y repara tu casco (HP). Cualquier impacto lo apaga, y se detiene cuando el casco está lleno.
- **Velocidad de reparación**: restaura por segundo un porcentaje de tus puntos de vida máximos (solo cuenta el mejor dron equipado; no se suman):
  - **Repair Drone I**: 1,5 % de los HP máx. / s
  - **Repair Drone II**: 2,25 % de los HP máx. / s
  - **Repair Drone III**: 3,5 % de los HP máx. / s
  - **Repair Drone IV**: 5 % de los HP máx. / s
- **Retraso**: los Repair Drones solo empiezan a reparar el casco tras **10 segundos** sin recibir daño.
- **En una ranura de habilidad**, un Repair Drone no repara por sí solo: te da **Emergency Repair**, un botón que cura una parte de tus puntos de vida máximos durante diez segundos, incluso bajo fuego (consulta [Habilidades](/wiki/03-Mechanics/Abilities.md)).

---

## Camuflaje y EMP {#cloaking-and-the-emp}

Un disparo necesita una fijación. Dos [extras](/wiki/06-Items/Extras.md) te quitan la tuya:

- **Cloaking CPU**: mientras estás camuflado (no hay límite de tiempo), los pilotos de otras corporaciones, los alienígenas y los pilotos de corporación no ven tu nave y no pueden fijarla; ven un simple punto rojo en el minimapa donde estás. Tu primera andanada termina el camuflaje, y no puedes volver a camuflarte durante un minuto, ni en los 10 segundos siguientes a un impacto o a un disparo.
- **EMP Charge**: durante 3 segundos nadie puede fijarte, y todas las fijaciones que ya había sobre ti se rompen al instante. Termina todos los camuflajes a menos de 1.500 unidades del piloto que la dispara, salvo los del propio grupo de ese piloto. No te oculta y no es invulnerabilidad: detiene lo que necesita una fijación.

Un cohete también es un disparo: termina tu propio camuflaje, y la explosión en área del cohete de otro sigue dañando a una nave camuflada y termina su camuflaje, porque una explosión no necesita fijación (consulta [Cohetes](/wiki/06-Items/Rockets.md)). El EMP detiene los láseres con fijación y los cohetes guiados, no una explosión.

Ninguno de los dos cambia una reclamación de derribo: una reclamación es el historial de quién impactó a un alienígena, no una fijación, y al camuflarte sueltas la tuya.
