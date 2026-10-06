<!-- wiki-i18n source: a6d1c3f189d0e637 -->
<!-- wiki-i18n title: Hangar -->
# El hangar en vuelo {#the-hangar-in-flight}

No tienes que volver a la base para cambiar de nave. Desde dentro de una zona segura puedes abrir la ventana **Hangar** (el botón del almacén en la barra de herramientas de arriba a la izquierda) y cambiar lo que llevas equipado, pasar a la otra configuración o pilotar otra nave que tengas, sin salir del juego. La ventana es la página Hangar de la estación, con las mismas ranuras, estadísticas e inventario, en una ventana sobre el juego. Consulta [Inventario y equipamiento](/wiki/03-Mechanics/Inventory.md) para saber cómo se instalan los objetos.

![The Hangar window in flight, opened at the station on its Drones view: the drones, the list of drone formations and the inventory](../../img/wiki-img/shots/hangar-window.jpg)

## Cuándo está abierto {#when-it-is-open}

Solo se permite un cambio mientras se cumplan todas estas condiciones:

- **Te protege una zona segura.** Cada estación y cada portal tienen un anillo protector (consulta [Combate](/wiki/03-Mechanics/Combat.md)). Dentro de él te protege cuando han pasado 5 segundos desde que te impactaron y 15 desde que disparaste.
- **Llevas fuera de combate unos segundos más**: **10** por defecto. Importa cuando llegas protegido de inmediato, por un portal, con un combate a tus espaldas.
- No estás camuflado, ni dentro de la ventana de tu propio EMP, ni cerca del [agujero negro](/wiki/03-Mechanics/Black-Hole.md), y no tienes ningún cohete tuyo todavía en el aire.

Las reparaciones en curso no te lo impiden. En cualquier otro lugar la ventana Hangar se abre igualmente, pero es de solo lectura. Un cartel ámbar explica el motivo y cuenta los segundos hacia atrás cuando se trata de una espera («Estabas en combate hace un momento. Espera 6 s para cambiar tu nave.»). El servidor también lo hace cumplir, así que nada puede cambiar una nave fuera de una zona segura.

## Qué puedes cambiar {#what-you-can-change}

- **Equipar y desequipar cualquier cosa**, en todos los tipos de ranura: láseres, generadores (escudos, motores, núcleos adaptativos), extras, ranuras de habilidad y ranuras de dron, y los amplificadores, células y propulsores instalados en ellos. Arrastra los objetos a las ranuras o haz clic en ellos, igual que en la estación. Tu nave se actualiza al instante: estadísticas, láseres, habilidades y barra rápida.
- **Desequipar todo.** El botón **Desequipar todo** de la barra de herramientas del Hangar vacía de una vez la configuración que muestra la vista **Nave**: los láseres, escudos, motores, núcleos adaptativos, extras y ranuras de habilidad **y los láseres y escudos en las ranuras de tus drones**, con los amplificadores, células y propulsores instalados en ellos. Todo vuelve a tu inventario, entero o nada. Tus **drones siguen siendo tuyos** (un dron nunca se instala en una nave, así que no hay nada que quitarle) y la **formación de drones** que llevas sigue puesta. La otra configuración no se toca. En vuelo rigen las reglas de cualquier cambio: desde una zona segura, fuera de combate. La vista **Drones** tiene un botón propio que vacía solo las ranuras de los drones.
- **Cualquiera de las dos configuraciones.** Puedes preparar la Config. 2 mientras vuelas con la Config. 1 y después cambiar con la tecla Cambiar config. Un botón **Volar con config.** del hangar hace el mismo cambio.
- **Cualquier nave.** Activa otra nave y la pilotas desde donde estás. El modelo de tu nave cambia delante de todos los que están cerca.
- **Un escudo, un motor o un núcleo adaptativo nuevo empieza vacío**, como en la estación: la carga de escudo de su configuración está vacía hasta que se recarga.
- **Formaciones de drones.** La vista Drones lista bajo tus drones las formaciones que tienes. No se equipan: en vuelo arrastras una desde la lista de Formaciones de la barra rápida a una ranura, y el clic o la tecla de esa ranura la lleva, sin espera dentro de una zona segura ([Formaciones de drones](/wiki/03-Mechanics/Formations.md)).
- **Extras.** Las cuatro naves normales, la Protos, la Kitefin, la Ostirion y la Nomad (con las que empiezas o que compras), tienen 2 ranuras de extra en cada configuración; las cuatro naves que fabricas en Ensamblaje, la Paragon, la Ironclad, la Wraith y la Storm, tienen 3. Las Extra Slots CPU de tu Skylab suman 3, 5 o 7 más: 5, 7 o 9 en las normales y 6, 8 o 10 en las fabricadas ([Extras](/wiki/06-Items/Extras.md#extra-slots-cpus)). Con la 0.4.10, un tercer extra en una nave normal se desequipó y pasó a tu inventario: no se borró nada y recibiste un mensaje en el chat.

## Cambiar de nave {#changing-ship}

La nave a la que cambias tiene **el casco y los escudos que tenía** la última vez que la pilotaste, exactamente como si la hubieras lanzado. El anillo no repara, así que cambiar de nave nunca te cura: la nave que dejas conserva el daño que tiene y vuelve con él. Una nave destruida no se puede pilotar hasta que la repares, lo cual es gratis y la devuelve con un máximo de 10.000 de casco y sin escudo, como una reaparición.

Lo que es tuyo sigue siendo tuyo: tu munición, tus cohetes y su temporizador, las recargas de tus habilidades, tus potenciadores, tu XP y tus Slave Drones. Lo que pertenecía a la nave termina: un Shield Surge o un Afterburner en marcha, las reparaciones, tu fijación de objetivo, tu ataque y el rumbo que seguías. Lo instalado se queda en la nave en la que está instalado.

## Peticiones desde otras herramientas {#requests-from-other-tools}

El servidor también permite cambiar el hangar solo desde una zona segura: equipar, desequipar, eliminar un objeto, reparar una nave o activar otra mientras vuelas responde «Solo puedes cambiar tu nave dentro de una zona segura.» El cambio de configuración es la excepción y funciona en cualquier sitio (una vez cada 5 segundos).
