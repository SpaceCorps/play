<!-- wiki-i18n source: d888495e0809faa2 -->
<!-- wiki-i18n title: Hangar -->
# El hangar en vuelo {#the-hangar-in-flight}

No tienes que volver a la base para cambiar de nave. Desde dentro de una zona segura puedes abrir la ventana **Hangar** (el botón del almacén en la barra de herramientas de arriba a la izquierda) y cambiar lo que llevas equipado, pasar a la otra configuración o pilotar otra nave que tengas, sin salir del juego. La ventana es la página Hangar de la estación, con las mismas ranuras, estadísticas e inventario, en una ventana sobre el juego. Consulta [Inventario y equipamiento](/wiki/03-Mechanics/Inventory.md) para saber cómo se instalan los objetos.

## Cuándo está abierto {#when-it-is-open}

Solo se permite un cambio mientras se cumplan todas estas condiciones:

- **Te protege una zona segura.** Cada estación y cada portal tienen un anillo protector (consulta [Combate](/wiki/03-Mechanics/Combat.md)). Dentro de él te protege cuando han pasado 5 segundos desde que te impactaron y 15 desde que disparaste.
- **Llevas fuera de combate unos segundos más**: **10** por defecto. Importa cuando llegas protegido de inmediato, por un portal, con un combate a tus espaldas.
- No estás camuflado, ni dentro de la ventana de tu propio EMP, ni cerca del [agujero negro](/wiki/03-Mechanics/Black-Hole.md), y no tienes ningún cohete tuyo todavía en el aire.

Las reparaciones en curso no te lo impiden. En cualquier otro lugar la ventana Hangar se abre igualmente, pero es de solo lectura. Un cartel ámbar explica el motivo y cuenta los segundos hacia atrás cuando se trata de una espera («Estabas en combate hace un momento. Espera 6 s para cambiar tu nave.»). El servidor también lo hace cumplir, así que nada puede cambiar una nave fuera de una zona segura.

## Qué puedes cambiar {#what-you-can-change}

- **Equipar y desequipar cualquier cosa**, en todos los tipos de ranura: láseres, generadores (escudos, motores, núcleos adaptativos), extras, ranuras de habilidad y ranuras de dron, y los amplificadores, células y propulsores instalados en ellos. Arrastra los objetos a las ranuras o haz clic en ellos, igual que en la estación. Tu nave se actualiza al instante: estadísticas, láseres, habilidades y barra rápida.
- **Cualquiera de las dos configuraciones.** Puedes preparar la Config. 2 mientras vuelas con la Config. 1 y después cambiar con la tecla Cambiar config. Un botón **Volar con config.** del hangar hace el mismo cambio.
- **Cualquier nave.** Activa otra nave y la pilotas desde donde estás. El modelo de tu nave cambia delante de todos los que están cerca.
- **Un escudo, un motor o un núcleo adaptativo nuevo empieza vacío**, como en la estación: la carga de escudo de su configuración está vacía hasta que se recarga.

## Cambiar de nave {#changing-ship}

La nave a la que cambias tiene **el casco y los escudos que tenía** la última vez que la pilotaste, exactamente como si la hubieras lanzado. El anillo no repara, así que cambiar de nave nunca te cura: la nave que dejas conserva el daño que tiene y vuelve con él. Una nave destruida no se puede pilotar hasta que la repares, lo cual es gratis y la devuelve con un máximo de 10.000 de casco y sin escudo, como una reaparición.

Lo que es tuyo sigue siendo tuyo: tu munición, tus cohetes y su temporizador, las recargas de tus habilidades, tus potenciadores, tu XP y tus Slave Drones. Lo que pertenecía a la nave termina: un Shield Surge o un Afterburner en marcha, las reparaciones, tu fijación de objetivo, tu ataque y el rumbo que seguías. Lo instalado se queda en la nave en la que está instalado.

## Peticiones desde otras herramientas {#requests-from-other-tools}

El servidor también permite cambiar el hangar solo desde una zona segura: equipar, desequipar, eliminar un objeto, reparar una nave o activar otra mientras vuelas responde «Solo puedes cambiar tu nave dentro de una zona segura.» El cambio de configuración es la excepción y funciona en cualquier sitio (una vez cada 5 segundos).
