<!-- wiki-i18n source: d8bf989776a71cb4 -->
<!-- wiki-i18n title: Habilidades -->
# Habilidades activas de la nave {#active-ship-abilities}

Las habilidades son los botones que pulsas en pleno combate: un escudo que vuelve, una ráfaga de velocidad para salir de alcance, una reparación cuando casi no te queda casco. Provienen del **escudo, motor o Repair Drone** que instalas en las **ranuras de habilidad** de tu nave, y cuanto mejor es ese objeto, mejor es la habilidad. Están pensadas para el momento en que las necesitas, no para pulsarlas en cada recarga: cada una dura unos diez segundos y después descansa de un minuto y medio a dos minutos.

Un piloto nuevo empieza con una: el **Repair Drone I** del kit inicial ya está instalado en la ranura de habilidad de la Protos, así que el botón de Emergency Repair (`E`) está ahí desde el primer minuto.

## Ranuras de habilidad {#ability-slots}

Cada nave tiene un número fijo de ranuras de habilidad en el hangar:

- **Protos** (inicial): 1 ranura
- **Kitefin**: 1 ranura
- **Ostirion**: 2 ranuras
- **Paragon**: 3 ranuras
- **Ironclad**: 3 ranuras
- **Wraith**: 3 ranuras

Una ranura de habilidad admite un **escudo**, un **motor** o un **Repair Drone**, y cada uno da su propia habilidad. Arrastra el objeto a la ranura. La configuración 1 y la configuración 2 tienen sus propias ranuras.

- **Las células de escudo y los propulsores no caben en una ranura de habilidad.** Son módulos de escudos, motores y núcleos adaptativos.
- **Un objeto en una ranura de habilidad no aporta nada más.** No da capacidad de escudo, recarga, absorción ni velocidad, ni tampoco la ralentización que provoca un escudo. El mismo Heavy Shield Core o bien está en una ranura de generador, para dar su escudo en todo momento, o bien en una ranura de habilidad, para su Surge. Tú eliges.
- Un escudo o un motor que lleva células o propulsores los devuelve a tu inventario cuando lo arrastras a una ranura de habilidad.
- Un Repair Drone en una ranura de habilidad da Emergency Repair y no repara el casco por sí solo. El dron lento (**REP**) necesita un Repair Drone en una ranura de extra.

## Varios módulos del mismo tipo {#several-modules-of-one-kind}

Puedes instalar **varios escudos, motores o Repair Drones** en las ranuras de habilidad de una configuración. Siguen siendo una sola habilidad, un solo botón y una sola recarga, pero más potente:

- **El módulo de peor rango fija la base.** Su rango da la potencia y la recarga. Un Heavy Shield Core junto a un Light Shield Core se comporta como dos módulos de rango I: un segundo módulo mejor sirve para el bono, nunca para una potencia mayor ni una recarga más corta.
- **Cada uno de los demás módulos suma el 50 % de la base**, se suma, no se multiplica. Los motores hacen que el Afterburner **dure más**: 10 s, 15 s con dos motores y 20 s con tres (el bono de velocidad y la recarga no cambian). Los escudos hacen que el Shield Surge **restaure más** y los Repair Drones hacen que Emergency Repair **repare más**, en los mismos diez segundos: el 100 %, el 150 % y el 200 % del total con uno, dos y tres módulos.
- **Los módulos adicionales cuestan ranuras.** Una nave con tres ranuras de habilidad puede tener tres de un mismo tipo, uno de cada, o dos y uno. Una Protos o una Kitefin tiene una sola ranura y no puede acumular; una Ostirion puede tener dos de un mismo tipo.
- Los rangos iguales son simplemente ese rango. De dos módulos del mismo rango, el que tiene el encantamiento más débil fija la base.

## Las tres habilidades {#the-three-abilities}

### Shield Surge (escudos), tecla `Q` {#shield-surge-shields-key-q}

Durante diez segundos el escudo de tu nave se **repara**: el Surge restaura una parte de tu escudo máx. de manera uniforme, hasta el máximo y nunca por encima. No es una barrera y no cambia cómo se reparten los impactos; devuelve escudo, y lo que devolvió se queda. No se detiene cuando te impactan (la recarga normal espera 15 segundos tras un impacto; el Surge no). Una nave con el escudo lleno saca poco de él, así que púlsalo cuando el escudo se esté agotando. El total nunca es inferior a la capacidad del propio núcleo, así que una nave con poco escudo recibe igualmente una reparación real (hasta su máximo).

- Se rechaza dentro de la protección de una zona segura y en una nave sin ningún escudo, para que un clic equivocado no lo gaste.
- Los cohetes con penetración de escudo siguen atravesando parcialmente los escudos, como siempre.

### Afterburner (motores), tecla `W` {#afterburner-engines-key-w}

Tu velocidad final se multiplica por el bono del rango mientras dura. No cambia el giro, la fijación de objetivo ni el daño recibido: convierte el tiempo en distancia. Úsalo para salir de un combate, para llegar al anillo de una estación o de un portal, o para acercarte a un objetivo que huye. Funciona en cualquier sitio, también en las zonas seguras. Más motores lo hacen durar más, no ir más rápido.

### Emergency Repair (Repair Drones), tecla `E` {#emergency-repair-repair-drones-key-e}

Repara una parte de tu **casco máx. de manera uniforme durante diez segundos**, sin pasar nunca del máximo. Los impactos no la interrumpen: es una habilidad de emergencia y funciona bajo fuego, en la radiación del agujero negro, con el camuflaje activado y dentro de una ventana de EMP. Termina cuando se acaba el tiempo o cuando tu nave es destruida. No toca tu escudo, no cuenta como un impacto y deja la reparación lenta REP como estaba. Se rechaza con el casco lleno.

## Rangos {#ranks}

La potencia de una habilidad es una **parte de la cifra de tu propia nave** (escudo máx., velocidad, casco máx.), así que crece con la nave. El rango viene del objeto: un modelo mejor da una habilidad mejor. Un objeto encantado suma su bono de encantamiento a la potencia, como máximo un 15 %. La tabla es para un módulo; la pila viene debajo de ella.

<!-- abilities:begin -->
<!-- Generated from server/Resources/AbilityConfig.json and the items' stats by scripts/abilities-wiki.sh: don't edit by hand. -->

| Habilidad | Rango | Objeto | Potencia (un módulo) | Duración | Recarga | Activa |
| :--- | :---: | :--- | :--- | --: | --: | --: |
| **Shield Surge** | I | Light Shield Core | restaura el 30 % de tu escudo máx. | 10 s | 120 s | 8,3 % |
| **Shield Surge** | II | Basic Shield Core | restaura el 60 % de tu escudo máx. | 10 s | 105 s | 9,5 % |
| **Shield Surge** | III | Heavy Shield Core | restaura el 100 % de tu escudo máx. | 10 s | 90 s | 11,1 % |
| **Afterburner** | I | Engine I | +30 % de velocidad | 10 s | 120 s | 8,3 % |
| **Afterburner** | II | Engine II | +45 % de velocidad | 10 s | 105 s | 9,5 % |
| **Afterburner** | III | Engine III | +60 % de velocidad | 10 s | 90 s | 11,1 % |
| **Emergency Repair** | I | Repair Drone I | repara el 20 % de tu casco máx. | 10 s | 120 s | 8,3 % |
| **Emergency Repair** | II | Repair Drone II | repara el 25 % de tu casco máx. | 10 s | 105 s | 9,5 % |
| **Emergency Repair** | III | Repair Drone III | repara el 32 % de tu casco máx. | 10 s | 90 s | 11,1 % |
| **Emergency Repair** | IV | Repair Drone IV | repara el 40 % de tu casco máx. | 10 s | 75 s | 13,3 % |

Varios módulos de un mismo tipo en una configuración: el de peor rango fija la potencia y la recarga de arriba, y cada uno de los demás suma el 50 % de esa base.

| Módulos de un mismo tipo | Afterburner dura | Shield Surge restaura | Emergency Repair repara |
| :---: | --: | --: | --: |
| 1 | 10 s | 100 % | 100 % |
| 2 | 15 s | 150 % | 150 % |
| 3 | 20 s | 200 % | 200 % |

<!-- abilities:end -->

Los escudos y motores de rango III (el Heavy Shield Core, el Engine III) no se venden: se fabrican en [Ensamblaje](/wiki/06-Items/Overview.md#upgrading-modules) a partir de un Basic Shield Core y un Engine II, con Thulium, lo que sueltan los alienígenas y Velkonite Reinforced Plates de la Forja de tu [Skylab](/wiki/03-Mechanics/Skylab.md). Emergency Repair tiene un cuarto rango, el Repair Drone IV.

## Recargas y límites {#cooldowns-and-limits}

- **La recarga empieza cuando pulsas** la habilidad e incluye su duración. Así, un Surge de 10 segundos con una recarga de 90 segundos está activo como máximo el 11 % del tiempo y no está disponible durante 80 segundos tras terminar. Varios módulos no la acortan (es la del módulo de peor rango); ni siquiera tres Afterburners están activos más del 22 % del tiempo.
- **Las recargas son tuyas, no del objeto.** Cambiar de configuración, cambiar el objeto, saltar a otro sector y desconectarte no las reinician. Una nave que es destruida empieza el siguiente vuelo con todas las habilidades listas.
- **Cada habilidad tiene su propia recarga.** Usar una no bloquea las demás.
- **Un efecto en marcha conserva las cifras con las que empezó.** Desequipar el objeto o cambiar de configuración no lo cambia ni lo termina. Un salto o una reconexión tampoco lo terminan; desconectarte sí, y su recarga se mantiene.
- Otros pilotos ven los temporizadores de tus habilidades en el mapa, como siempre: un Surge gastado les señala que los próximos minutos son una oportunidad.

## Teclas y botones {#keys-and-buttons}

`Q` Shield Surge, `W` Afterburner, `E` Emergency Repair (todas se pueden cambiar en Configuración). Cada botón aparece junto a la barra rápida solo cuando tu configuración tiene esa habilidad, así que la `E` de un piloto nuevo está ahí desde el primer minuto. El anillo alrededor de su icono indica en qué estado está la habilidad: completo y del color de la habilidad cuando está lista, vaciándose con los segundos que quedan mientras está en marcha (también Emergency Repair, ahora que repara durante diez segundos), y volviéndose a llenar mientras se recarga, con los segundos que faltan en el centro. Una pila de varios módulos lleva su marca (`x2`, `x3`) en la esquina del botón. El botón de Emergency Repair se atenúa mientras tu casco está lleno, y el de Shield Surge en una nave sin ningún escudo. Pasa el cursor por un botón para ver las cifras en tu nave, con la pila contada (por ejemplo, *Afterburner II x2: +45 % de velocidad durante 15 s*) y, mientras un Surge o una reparación están en marcha, cuánto da por segundo y cuánto falta por llegar.

## En el hangar {#in-the-hangar}

Arrastra un escudo, un motor o un Repair Drone a una ranura de habilidad, o haz clic derecho en él en tu inventario para ponerlo en la primera libre. Un segundo y un tercero del mismo tipo van a las siguientes ranuras libres y se acumulan. El nombre y el rango de la habilidad figuran bajo cada ranura ocupada, con la marca de la pila y las cifras de todos sus módulos juntos (*Afterburner II x2*, *x2 · 15 s*; para un Repair Drone II en una Wraith, *+81.000 de casco*), y al pasar el cursor por una ranura se ve lo que vale en tu nave, con la pila contada, y qué módulo de la pila fija el rango. Todos los módulos de un tipo muestran la misma habilidad, porque son una sola. Al pasar el cursor por el objeto en cualquier otro lugar se ve la habilidad con las partes de tu propia nave y una frase sobre lo que suma un módulo más.

## Lo que ve todo el mundo {#what-everyone-sees}

Un Shield Surge es una burbuja alrededor de la nave mientras dura, que parpadea en sus dos últimos segundos y se cierra cuando termina. Las barras de escudo (la tuya en la ventana Nave y la de un objetivo en la ventana Objetivo) simplemente se llenan a medida que el Surge devuelve escudo, y la barra pulsa suavemente mientras hay espacio para ello. Un Afterburner hace arder los motores con más intensidad mientras dura, 10, 15 o 20 segundos, y lanza un anillo desde la nave al empezar, más ancho en una pila. Un Emergency Repair emite un pulso verde al empezar; después, durante sus diez segundos, envuelve el casco en un suave resplandor verde del que se elevan unos cuantos signos más, hace flotar sobre tu propia nave el casco que repara cada segundo y termina con un último destello. Mientras dura, unos pequeños drones de reparación rodean la nave y la arreglan: uno para un Repair Drone I, dos para un II, tres para un III o IV, y uno más por cada Repair Drone adicional de una pila (nunca más de tres). Salen del casco, apuntan suaves haces verdes a las placas de este, envían pulsos por los haces a partir del grado II y vuelven volando a atracar cuando pasan los diez segundos; un Shield Surge tiene hasta dos azules dentro de su burbuja. Todos los pilotos del mapa ven las tres habilidades, también los drones (más pequeños en la nave de otro piloto y menos en las calidades gráficas más bajas, donde Baja muestra haces y resplandores sin modelos de drones, y con un haz algo más ancho por cada rango del dron), así que un Surge gastado es una señal tanto para el enemigo como para ti. Los drones hacen tres sonidos suaves propios, muy por debajo de la campanilla de la reparación: un leve pitido al salir del casco, otro al atracar y un tono tenue bajo sus haces mientras trabajan (el de los drones de un Surge, algo más agudo); los oyes desde las naves que ves en pantalla, como mucho unos pocos a la vez, y el volumen de Efectos de sonido los baja. Con *Reducir movimiento* activado, el resplandor se mantiene estable, se omiten los signos más, el último destello es un desvanecimiento y los drones se quedan aparcados junto a la nave con un haz estable (los sonidos se mantienen).

## Qué ha cambiado {#what-changed}

Antes de la actualización 0.4.3, las ranuras de habilidad admitían células de escudo (Regen. de escudo) y propulsores (Impulso de velocidad). Las células de escudo y los propulsores que estaban en ranuras de habilidad volvieron a tu inventario al actualizarse el juego, y te los quedas: siguen siendo módulos de escudos, motores y núcleos adaptativos. Desde entonces el Shield Surge ya no da una barrera de sobreescudo, sino que repara tu escudo durante diez segundos, Emergency Repair repara durante diez segundos en lugar de al instante, y puedes instalar varios módulos de un mismo tipo para un Afterburner más largo, un Surge mayor o una reparación mayor.
