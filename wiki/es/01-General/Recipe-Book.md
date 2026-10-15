<!-- wiki-i18n source: 6ff3251582e96a39 -->
<!-- wiki-i18n title: Libro de recetas -->
# Libro de recetas y builds {#recipe-book-and-builds}

<!-- wiki-search: recipe; recipes; recipe book; bill; steps; chart; craft tree; what do i need; build; builds; loadout; preset; presets; import; export; json; my builds; share a build; receta; recetas; coste; pasos; diagrama; fabricar; equipo; importar; exportar; mis builds; compartir un build -->

El **Libro de recetas** responde a «¿qué hace falta para esto?» con cualquier objeto del juego: un diagrama de lo que lo compone, los pasos en orden, el coste completo y de dónde sale cada materia prima. **Builds** hace lo mismo con una nave entera: importa el equipo de tu hangar o el build de un amigo, empieza con uno de los 15 presets o crea el tuyo, y mira sus estadísticas y su coste completo, paso a paso. Los dos están en la **Biblioteca** de la estación, debajo de la Wiki.

El Libro de recetas no guarda una lista de precios propia: calcula sus números en el momento en que miras, a partir de las recetas, los precios, las tecnologías y las tablas de botín que usan la Tienda, el [Ensamblaje](/wiki/06-Items/Overview.md#upgrading-modules) y la [Investigación](/wiki/03-Mechanics/Research.md), así que sigue al juego cuando cambia un precio o una receta. Por eso esta página no cita ningún precio ni ninguna estadística: abre el objeto o el build.

![The Builds page: the presets from early to late, and a build with its lasers, generators, extras and drones laid out in slots](../../img/wiki-img/shots/builds.jpg)
![The Bill tab: what the item takes in Credits, Thulium and raw items, with what you have and what is missing](../../img/wiki-img/shots/recipe-book-bill.jpg)
![An item in the Recipe Book: its ways to get it, the switches for the bill and the chart of what it takes down to the raw items](../../img/wiki-img/shots/recipe-book-chart.jpg)

## Abrirlo {#open-it}

Abre el menú de la estación y elige **Biblioteca › Libro de recetas** o **Biblioteca › Builds**. El Libro de recetas recuerda el último objeto que miraste, sus filtros y su zoom, solo en este ordenador; tus builds no forman parte de eso ([Guardados en tu cuenta](#saved-on-your-account)). Cuando el juego es más nuevo que el servidor con el que habla, la página lo dice y muestra menos: el Libro de recetas sigue calculando todo lo que se compra, se fabrica o se mejora, pero no puede decir dónde da el mundo un objeto (solo pone «Conseguir»), y Builds nombra las partes que necesitan el servidor más nuevo: los presets, Mis builds y las estadísticas.

## Encontrar un objeto {#find-an-item}

La lista grande de la izquierda contiene todos los objetos del juego, agrupados por tipo y, dentro de un tipo, en el orden propio del juego: primero el nivel más débil. La EMP Charge, el único consumible, también está.

- **Búsqueda.** Empieza a escribir en cualquier punto de la página y el texto va al campo de búsqueda. La lista pasa a ser una sola, ordenada según lo bien que encaja el nombre (el nombre entero, su inicio, el inicio de una palabra, cualquier parte, y luego el tipo). Las mayúsculas y los acentos no importan, y el nombre antiguo de un objeto renombrado encuentra el objeto. `Esc` borra la búsqueda.
- **Tipo.** El menú desplegable sobre la lista la reduce a un tipo y dice cuántos objetos tiene cada tipo. El interruptor de al lado ordena de la A a la Z dentro de cada tipo.
- **Filas.** Una fila muestra la imagen, el nombre, el tipo y la rareza del objeto, un pequeño símbolo de la vía por la que lo conseguirías normalmente (se fabrica en Ensamblaje, se vende en la Tienda, cae o se encuentra, se prensa o se produce en el agujero negro) y una marca si lo tienes.
- **Teclas.** Las flechas, Re Pág, Av Pág, Inicio y Fin recorren la lista, y `Enter` pasa al diagrama. `Alt+Left` y `Alt+Right` van hacia atrás y hacia delante por los objetos que abriste.

## El diagrama {#the-chart}

Haz clic en un objeto y el lado derecho lo muestra. Arriba están su imagen, su nombre, su rareza y su tipo, y un chip por cada **vía** para conseguirlo: **Fabricar** (en Ensamblaje, con su tiempo y su coste), **Comprar** (en la Tienda, con su precio), **Prensar** (a partir de mineral, en la Forja del Skylab), **Botín** (lo da el mundo: alienígenas, rocas, recompensas) y **Producir** ([Dark Matter](/wiki/03-Mechanics/Dark-Matter.md), a partir de N.I.K.E. disparados al agujero negro). El chip relleno es la vía que siguen el diagrama y el coste; haz clic en otro chip para seguir esa en su lugar. Si no has investigado lo que te permite fabricar el objeto, una línea dice qué tecnología hace falta y cuánto tarda, con un botón que abre la Investigación.

El **Diagrama** dibuja el objeto como un árbol de izquierda a derecha: el objeto a la izquierda, lo que lo compone a su derecha, hasta llegar a las materias primas.

- Cada caja muestra el objeto, cuántos necesitas y un símbolo de cómo se consigue (el del chip de esa vía, arriba; pasa el ratón por la caja para ver las palabras, así el color nunca es la única señal). Un candado dice que su tecnología aún no está investigada, y una marca verde con un número, cuántos tienes.
- Una caja con ramas tiene un pequeño tirador que las pliega; las ramas profundas de un árbol grande empiezan plegadas. **Expandir todo**, **Contraer todo**, **Ajustar** y los botones de zoom están sobre el diagrama.
- Haz clic en una caja para leer su ficha bajo el diagrama: el objeto, las vías para conseguirlo (haz clic en otro chip para seguir esa vía), lo que pide la vía (las tandas, el tiempo y el coste de una fabricación, o su precio en la Tienda), cuántos tienes y, en una caja bloqueada, la tecnología que necesita. Un doble clic, o `Enter`, abre ese objeto en el Libro de recetas. Las flechas pasan de una caja a otra, `Space` pliega o despliega una rama y `0` ajusta el diagrama. Desplázate para moverte; `Ctrl` y la rueda hacen zoom.
- Un objeto que solo se compra o se encuentra es una sola caja que dice «Nada que fabricar: se compra o se encuentra. Mira Fuentes.»

En una ventana ancha el diagrama ocupa la izquierda y los demás paneles van en una columna a su derecha; en una estrecha, las pestañas **Diagrama**, **Pasos**, **Coste**, **Fuentes** y **Se usa en** muestran un panel cada vez.

## Pasos y coste {#steps-and-the-bill}

Bajo la cabecera, tres controles deciden qué se cuenta: **Cantidad** de copias que quieres, **Contar lo que tengo** (activado: lo que ya tienes se descuenta) e **Incluir lo equipado** (desactivado: una pieza equipada en una nave no se cuenta, porque mejorar consume una pieza y una equipada dejaría su ranura).

- **Pasos** es el diagrama como lista numerada, en el orden en que hay que hacerlo, en grupos: Investigar, Conseguir, Comprar, Prensar y fabricar, y De tu inventario. La investigación va primero porque el Ensamblaje no fabrica nada antes de que su tecnología esté investigada. Cada paso dice qué y cuántos, cuánto cuesta y cuánto tarda, y un paso de Conseguir puede mostrar dónde conseguirlo. **Copiar pasos** copia la lista como texto.
- **Coste** lo suma todo: tus Credits y tu Thulium frente a lo que tienes, cada materia prima con lo **Necesario**, lo que **Tienes** y lo que **Falta**, el Dark Matter que gasta la investigación, el tiempo de fabricar y prensar, el tiempo de investigar (una tecnología cada vez) y un **Valor**. El Valor es una forma de comparar dos maneras de conseguir un objeto, con el Thulium y lo que hay que encontrar contados en Credits: no es un precio. **Copiar coste** copia el coste como una tabla que puedes pegar en un chat o en una nota.

## Fuentes y Se usa en {#sources-and-used-in}

- **Fuentes** dice dónde da el mundo el objeto y cada materia prima que necesita el plan, por tipo: alienígenas, asteroides y rocas, enjambres, el Dormant Swamp, guardianes del clan, [Davidski](/wiki/03-Mechanics/Davidski.md), expediciones del Skylab, la excavadora gigante, producción del Skylab, misiones, Invitar amigos y el paquete inicial. Una fila nombra quién lo da y dónde, la probabilidad y cuántos. «También en» enumera la [Subasta](/wiki/03-Mechanics/Auction.md), las existencias de Davidski y otros pilotos. Una probabilidad es una probabilidad, no un ritmo por hora: lo que tarde una baja depende de ti.
- **Se usa en** enumera los objetos que se fabrican con este. Haz clic en uno para abrirlo.

## Añadir al build {#add-to-build}

Un objeto que va en una ranura o que se lleva tiene un botón **Añadir al build**: naves, blindajes de casco, láseres, amplificadores, escudos, celdas, motores, propulsores, Adaptive Cores, extras, drones, formaciones, munición, cohetes y la EMP Charge. Pone el objeto en el build que editas en **Builds**, en el primer sitio donde cabe (si no hay ninguno, se crea un build nuevo llamado «Nuevo build»), y un mensaje dice adónde fue o por qué no cabía («Elige primero una nave.»). Si añades una nave a un build que ya tiene una, te pide que hagas clic otra vez para sustituirla. La EMP Charge se lleva, no se equipa: va a los cohetes del build.

## Builds

Un **build** es el equipo de una nave, escrito con nombres de objetos para que signifique lo mismo en todos los servidores: la nave, los láseres con sus amplificadores, los escudos, motores y Adaptive Cores con sus celdas y propulsores, los extras, las piezas de las ranuras de habilidad, los blindajes de casco, los drones con lo que llevan, una formación y la munición y los cohetes que se llevan. También tiene un nombre, una nota, una fase (Inicio, Medio o Final) y un tipo.

La lista de la izquierda tiene los **Presets** por fase, **Mis builds**, **Nuevo build** e **Importar**; en una ventana estrecha es una fila de pestañas. Elige un build y verás su tablero, sus estadísticas y su coste.

### Importar {#import}

**Importar** abre una hoja con tres puertas:

- **Pegar**: pega el texto de un build, o pulsa **Pegar del portapapeles**.
- **Desde un archivo**: los archivos de build de la carpeta `exports` de la carpeta de datos del juego (`.spacecorps2027` en tu carpeta personal), la misma carpeta en la que escribe **Guardar en archivo**.
- **Desde mi hangar**: elige una de tus naves y una configuración, y el juego lee lo que está equipado: láseres y amplificadores, generadores con sus celdas y propulsores, extras, piezas de habilidad, blindajes de casco, drones con lo que llevan y el nivel de tu Extra Slots CPU. También ofrece la formación, la munición y los cohetes de tu barra rápida; marca los que quieras.

Ves lo que entra antes de que se guarde nada, y el juego te dice exactamente lo que no pudo importar: un objeto que no existe en este juego, una pieza que no va en su sitio, más piezas de las ranuras que tiene la nave, un build hecho por un juego más nuevo. **Importado sin cambios** significa que entró todo. Después, **Guardar en Mis builds**, **Abrir en el editor** o cierra la hoja. Tus niveles de [Forja](/wiki/06-Items/Forge.md), las bonificaciones de forja, los niveles de los drones, los potenciadores, el P.E.T., el aspecto de tu nave y la otra configuración del [Hangar](/wiki/03-Mechanics/Hangar.md) no forman parte de un build (importa la otra configuración como un segundo build).

### Los 15 presets {#the-15-presets}

Quince builds están listos para usar: tres fases del juego, **Inicio**, **Medio** y **Final**, con cinco tipos en cada una. **Farmeo** consigue más bajas por lo que cuesta, **Defensa** tiene el escudo más grande y la regeneración más rápida, **Ataque** el mayor daño y la mayor penetración, **Situacional** elige sus combates con camuflaje, saltos y velocidad, y **Tanque** tiene el casco y el escudo más altos juntos. Un preset no se puede cambiar: **Editar una copia** lo abre como tu propio borrador, y **Añadir a Mis builds** lo guarda tal cual. Cada fila muestra su Valor en pocos caracteres, calculado a partir de las recetas mientras miras; abre un preset para ver sus estadísticas y su coste.

### Editar {#edit}

Un build se dibuja como un hangar: láseres, generadores, extras, habilidades, blindajes y drones, y después el nivel de la Extra Slots CPU, una formación y la munición y los cohetes que se llevan. Haz clic en una ranura vacía y una lista muestra solo lo que cabe en ella, con su precio o la vía para conseguirlo; haz clic en una pieza para **Reemplazar**la, **Añadir un módulo** o **Quitar**la. Un dron lleva un láser o un núcleo de escudo. Si cambias la nave, las piezas que aún caben se quedan, y el resto se enumera como quitado. Dale al build un nombre, una fase, un tipo y una nota, y luego **Guardar**, **Guardar como copia**, **Eliminar** o **Cerrar** (Cerrar pregunta antes si hay cambios sin guardar).

### Estadísticas {#stats}

Bajo el tablero está la ficha de estadísticas del hangar: puntos de vida, daño, alcance, prob. crítico, escudos y su recarga, absorción, velocidad, bono de escudo y de velocidad, penetración y, en una nave con ranuras de blindaje, el casco que suman sus blindajes. La ficha no tiene líneas para las habilidades: las piezas de las ranuras de habilidad están en el tablero. El servidor calcula los números con el mismo código que tu hangar, para un build que no está equipado en ninguna nave. Dos interruptores fijan el **Nivel de forja** y el **Nivel de los drones** que suponen los números. Una formación actúa en vuelo, así que se enumera como texto y no se cuenta en los números, y tampoco los potenciadores ni tus propios niveles de forja.

### Coste {#cost}

El coste tiene cuatro bloques:

- **Totales**: Credits, Thulium, Dark Matter, cada materia prima con Necesario, Tienes y Falta, los tiempos y el Valor. **Todavía necesitas** es lo que queda una vez descontado lo que tienes.
- **En qué se va el dinero**: cada pieza, la más cara primero.
- **Pasos**: investigar, conseguir, comprar, prensar y fabricar, en orden, para el build entero. Haz clic en un paso de Conseguir para ver dónde lo da el mundo, o abre el objeto en el Libro de recetas.
- **Antes de empezar**: lo que no es una pieza, como los niveles de la Extra Slots CPU, la investigación de las ranuras de blindaje, los drones que aún tienes que comprar y el nivel del Núcleo del Skylab que necesita la forja.

Tres interruptores: **Descontar lo que tengo** (activado), **Incluir lo equipado** (desactivado) e **Incluir munición y cohetes** (desactivado: se gastan una y otra vez, así que no son el precio del build).

## Guardados en tu cuenta {#saved-on-your-account}

**Mis builds se guardan en tu cuenta**, en el servidor y no en este ordenador, así que te siguen a cualquier ordenador. Puedes conservar hasta 50; la lista muestra cuántos tienes y, cuando está llena, la página te pide que borres uno para guardar otro. Un build está guardado cuando el servidor lo dice: la página muestra **Guardando...** mientras espera, y si el servidor lo rechaza o no se le puede alcanzar, dice por qué y el build queda sin guardar, con tus cambios todavía en el editor. Un build guardado son solo nombres de objetos, unas pocas etiquetas y el nombre y la nota que escribiste, y ningún otro piloto puede verlo. Para dárselo a un amigo, expórtalo.

## Compartir y exportar {#share-and-export}

**Exportar** en un build abre una hoja con el build como texto (JSON). **Cópialo** para pegarlo en un chat, o usa **Guardar en archivo**, que escribe `spacecorps-build-<name>.json` en la carpeta `exports` y nunca sobrescribe un archivo anterior. Un amigo pega el texto en **Importar › Pegar**, o pone el archivo en su propia carpeta `exports` y lo elige en **Desde un archivo**. El texto contiene los nombres de los objetos del equipo, la nave y el nombre y la nota del build, y nada de tu cuenta.

## Consejos {#tips}

1. **Mira antes de farmear.** Abre un objeto en el Libro de recetas y lee sus Fuentes y sus Pasos antes de pasar un día en un botín que no es el que necesitas.
2. **Cuenta desde cero.** Desactiva **Contar lo que tengo** (en Builds: **Descontar lo que tengo**) para ver lo que cuesta un objeto o un build desde cero; déjalo activado para ver lo que aún necesitas.
3. **Empieza con un preset.** **Editar una copia**, cambia una pieza, y las estadísticas y el coste te siguen.
4. **Lee también los árboles.** Los [Árboles de objetos](/wiki/06-Items/Item-Trees.md) muestran cada tipo de objeto uno al lado de otro, y el Libro de recetas calcula el precio de cualquiera de ellos por ti.
