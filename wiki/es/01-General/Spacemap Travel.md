<!-- wiki-i18n source: 885da8b1fe8a0f3a -->
<!-- wiki-i18n title: Viajes por el mapa espacial -->
# Viajes por el mapa espacial {#spacemap-travel}

El mapa espacial es tu interfaz de navegación para recorrer el universo de SpaceCorps. Cada corporación controla un sector del espacio, dispuesto según una topología concreta que permite tanto la exploración segura como los peligrosos enfrentamientos PvP.

## La estructura del universo {#the-universe-structure}

El universo consta de tres grandes sectores de corporación (Mars, Terra, Galactic) y una zona PvP central.

- **x-1 (base de origen)**: El mapa inicial de cada corporación (M-1, T-1, G-1). La zona más segura.
- **x-2 -> x-3**: Zonas de expansión con alienígenas cada vez más duros.
- **x-4 (frontera)**: La puerta de entrada al sector PvP.
- **DS-x (sectores de peligro)**: La zona PvP central que conecta todas las corporaciones: de DS-1 a DS-4.

Solo las bases de origen tienen una estación. Es donde se abre **Mission Control**, y su zona segura se extiende 1.600 unidades a su alrededor. Los sectores de peligro no tienen estación, ni siquiera `DS-1`: las únicas zonas seguras allí son los anillos de 660 unidades alrededor de los portales de salto, y Mission Control no puede abrirse allí; vuela de vuelta a tu base para tus misiones.

Cada [mundo](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) (Alpha, Beta, Gamma) tiene su propia copia de todo este mapa, y dónde pueden combatir los pilotos entre sí depende de él: en Alpha, solo en `x-4` y `DS-x`; en Beta, en todas partes excepto en `x-1`; en Gamma, en todas partes. El mapa galáctico colorea los sectores según la regla de tu mundo.

## Visualización {#visualization}

El mapa galáctico de abajo muestra en tiempo real la disposición del universo conocido. En el juego, ese mismo mapa es la ventana **Sistema estelar**.

```spacemap

```

Con una [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) instalada, el mapa también sirve para elegir destino: pulsa la ranura de la CPU en la barra rápida (**JMP**) y la ventana Sistema estelar se abre en modo de selección. Los sectores a los que la CPU puede llevarte se iluminan; tu propio sector y los sectores de peligro, no. Apunta a un sector iluminado para leer el precio, haz clic en él y confirma el salto cuando el mapa te lo pida (500 Thulium).

## Cómo viajar {#how-to-travel}

Los viajes por el mapa espacial se hacen a través de **portales de salto**, o simplemente portales. La [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) es la otra vía: no necesita portal (consulta el final de esta página).

1. **Localiza un portal**: Los portales suelen estar en las esquinas o en los bordes de un mapa.
2. **Navegación**: Acerca tu nave a la estructura del portal.
3. **Activación**: Pulsa **'J'** a menos de 500 unidades del portal para iniciar el salto.
4. **Espera**: El salto **dura 3 segundos**. Mientras tanto se llena una barra sobre tu barra rápida («Saltando…»), y el portal brilla cada vez más a medida que se carga; los demás pilotos ven esa misma carga en el portal cuando saltas. Tu nave sigue volando, pero tienes que quedarte a menos de 500 unidades del portal hasta que se acabe el tiempo: si sales del alcance, el salto se cancela («El portal está demasiado lejos para saltar.», y la barra se vuelve roja). Volver a pulsar **'J'** mientras saltas no hace nada, salvo avisarte de ello.
5. **Destino**: Llegarás al portal correspondiente del mapa de destino.

### Saltar bajo fuego enemigo {#jumping-under-fire}

- **Fuera de los sectores de peligro**, que te ataquen, ya sean alienígenas u otros pilotos, **no** interrumpe tu salto: se completa.
- **En los sectores de peligro (`DS-1` a `DS-4`)** no puedes salir saltando mientras te atacan. Si un piloto o un alienígena ha alcanzado tu nave (sus escudos o su casco) en los últimos **10 segundos**, el salto no empieza («Estás bajo ataque: no puedes saltar fuera de un sector de peligro.»), y un impacto mientras saltas cancela el salto (la barra se vuelve roja y el juego te dice por qué). El daño que recibes de la radiación del agujero negro no es un ataque, y tampoco lo es un disparo que haya detenido una zona segura. Un impacto que recibiste en el mapa del que saltaste no te sigue a través del portal: llegas con el historial limpio.
- Haces una sola cosa a la vez: no puedes recoger una [caja de carga](/wiki/03-Mechanics/Cargo.md) mientras saltas, e iniciar un salto anula una recogida que hubieras empezado.
- Cerrar el juego o volver a la base en mitad de un salto lo cancela: no llegas.
- **El teletransporte de una CPU se carga como un salto por portal.** Una Jump CPU se carga durante 5 segundos y una Base CPU durante 10, con una barra sobre la barra rápida. Un disparo tuyo o un impacto que recibas, en cualquier sector, lo cancela (no se paga ni se gasta nada), y ninguna de las dos CPU arranca dentro de los 10 segundos posteriores a un disparo o un impacto. Vuelve a pulsar la ranura de la CPU para cancelarlo tú.

### Conexiones de salto {#jump-links}

- **El circuito de cada corporación**: Mars, Terra y Galactic tienen la misma disposición. Las conexiones son `1 <-> 2 <-> 3`, `2 <-> 4` y `3 <-> 4`. Así se forma un circuito entre los mapas secundarios (`x-2` y `x-3`) y el mapa fronterizo (`x-4`), con `x-1` como un ramal de entrada seguro conectado solo a `x-2`: tu mapa inicial tiene un único portal.
- **Portales de acceso a los sectores de peligro**: El mapa fronterizo de cada corporación (`x-4`) conecta directamente con su propio sector de peligro:
  - `M-4` conecta con `DS-1`
  - `T-4` conecta con `DS-2`
  - `G-4` conecta con `DS-3`
- **Rutas de invasión (viajes entre corporaciones)**: Para entrar por los portales en territorio de una corporación enemiga tienes que cruzar la zona PvP. Por ejemplo, un piloto de Mars que quiera invadir Terra debe volar de `M-4` al sector de peligro `DS-1`, cruzar el portal de salto hacia `DS-2` y luego entrar en el espacio de Terra por `T-4`; para llegar a Galactic, debe cruzar el portal de salto hacia `DS-3` y entrar por `G-4`.
- **El triángulo de los sectores de peligro**: `DS-1`, `DS-2` y `DS-3` están conectados entre sí. Cada uno tiene el portal de una corporación (Mars en `DS-1`, Terra en `DS-2`, Galactic en `DS-3`); `DS-4` no tiene ninguno.
- **El núcleo central**: Los tres sectores de peligro exteriores (`DS-1`, `DS-2` y `DS-3`) conectan directamente con el mapa central, **`DS-4`**, la zona PvP más peligrosa y lucrativa del universo. En su centro exacto flota un **agujero negro**: los portales y las rutas entre ellos quedan bien lejos de él, pero una nave que se adentra sufre primero su radiación, luego su atracción, y es destruida en su horizonte de sucesos. Consulta [El agujero negro](/wiki/03-Mechanics/Black-Hole.md).

### La Jump CPU {#the-jump-cpu}

La [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) lleva tu nave a cualquier sector de corporación de tu mundo sin usar un portal, por 500 Thulium cada salto, incluidos los sectores de origen de los enemigos. Nunca va a un sector de peligro, no se activa en combate y primero la investigas en el Centro de investigación del Skylab ([Investigación](/wiki/03-Mechanics/Research.md)). Las [Base CPU](/wiki/06-Items/Extras.md#base-cpus) te llevan a casa de la misma manera.
