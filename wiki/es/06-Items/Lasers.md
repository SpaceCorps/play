<!-- wiki-i18n source: d64d048fd518e14c -->
<!-- wiki-i18n title: Láseres -->
# Láseres y munición {#lasers-ammo}

Las armas son el medio principal de causar daño en SpaceCorps.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Árbol de objetos {#item-tree}

Lo que fabrica Ensamblaje necesita antes su tecnología; pasa el cursor por un objeto para ver cuánto tarda en investigarse. El árbol de tecnologías, el combustible y el impulso: [Investigación](/wiki/03-Mechanics/Research.md).

```tree
Quantum Laser 1 | laser, shoddy | buy 8000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser 2 | laser, common | buy 80000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser 3 | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-3 | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser 3, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-3, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp 1 | laser-amp, shoddy | buy 10000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp 1 | laser-amp, shoddy | buy 15000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Arc Amp | laser-amp, uncommon | buy 60000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Focus Amp | laser-amp, uncommon | buy 60000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Pulse Amp | laser-amp, rare | buy 1500 Thulium | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Prism Amp | laser-amp, rare | buy 1500 Thulium | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Nova Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Pulse Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Apex Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Prism Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Standard Battery | ammo, common | buy 10 Credits | /wiki/06-Items/Lasers.md#laser-ammunition
Siphon Battery | ammo, rare | buy 0.25 Thulium | /wiki/06-Items/Lasers.md#siphon-battery
Advanced Plasma | ammo, rare | buy 0.5 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Ultra Core | ammo, rare | buy 1 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Experimental Fusion Core | ammo, epic | buy 2.2 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition

Quantum Laser 1 -> Quantum Laser 2 -> Quantum Laser 3 => Starfire-3 => Helios Beam
Damage Amp 1 -> Arc Amp -> Pulse Amp => Nova Amp
Crit Amp 1 -> Focus Amp -> Prism Amp => Apex Amp
Standard Battery -> Advanced Plasma -> Ultra Core -> Experimental Fusion Core
```
<!-- item-tree:end -->

## Láseres {#lasers}

Equipa láseres directamente en las ranuras de láser de la nave o dentro de drones para aumentar tu capacidad ofensiva.

| Nombre | Rareza | Daño base | Prob. crítico | Alcance | Ranuras de amp. | Costo |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Quantum Laser 1** | Deficiente | 55 | – | 600 | 1 | 8.000 créditos |
| **Quantum Laser 2** | Común | 65 | – | 700 | 2 | 80.000 créditos |
| **Quantum Laser 3** | Raro | 80 | 10 % | 800 | 3 | Solo fabricable |
| **Starfire-3** | Mítico | 135 | 15 % | 850 | 3 | Solo fabricable |
| **Helios Beam** | Mítico | 185 | 25 % | 900 | 3 | Solo fabricable |

La columna Alcance es la de cada láser por separado. **Tu nave dispara al alcance medio de sus láseres** (cuentan también los láseres de tus drones), redondeado a la unidad más cercana, y todos los láseres disparan en cuanto el objetivo está dentro de esa distancia. Un Starfire-3 junto a dos Quantum Laser 2 da a la nave un alcance de 750, no de 850; tres Starfire-3 mantienen 850, y los láseres que son todos iguales no cambian nada. Una bonificación de alcance de la Forja cuenta en su propio láser antes de calcular la media. Sin ningún láser, el hangar no muestra alcance (un guion) y los láseres no pueden disparar, pero tus cohetes sí, cada uno con su propio alcance (consulta [Cohetes](/wiki/06-Items/Rockets.md)). En el hangar, la casilla dice «Alcance medio» cuando tus láseres difieren, y al pasar el cursor por encima se lista el alcance de cada láser.

El Quantum Laser 1 y el 2 no tienen probabilidad de crítico propia («–»): se la da un Damage Amp o un Crit Amp en sus ranuras. Los golpes críticos se muestran con otro color en los números de daño flotantes (azul hielo, más grandes y con un «!»).

### Cómo se fabrican los tres mejores láseres {#making-the-top-three-lasers}

El **Quantum Laser 3**, el **Starfire-3** y el **Helios Beam** se fabrican solo en **Ensamblaje**. El Quantum Laser 3 ya no se vende en la tienda; el piloto que ya tiene uno se lo queda. Cada receta pide placas de la Forja del [Skylab](/wiki/03-Mechanics/Skylab.md):

| Láser | Tiempo de fabricación | Qué necesita |
| :--- | :---: | :--- |
| Quantum Laser 3 | 1 min | 10 Ship Fragments, 2 Velkonite Reinforced Plates, 1.500 Thulium |
| Starfire-3 | 1 min | 1 Quantum Laser 3, 15 Ship Fragments, 8 Velkonite Reinforced Plates, 1 Reinforced Hull Plate, 1.500 Thulium, 100.000 créditos |
| Helios Beam | 3 min | 1 Starfire-3, 50 Cataclysite, 2 Power Cores, 18 Orvium Reinforced Plates, 4 Reinforced Hull Plates, 2.000 Thulium |

La página de Ensamblaje muestra lo que tienes frente a lo que pide una receta, y el botón Ensamblar dice lo que te falta. Si apuntas a la imagen o al nombre de una receta, o a uno de sus materiales, aparecen la descripción completa y las estadísticas del objeto.

**El Starfire-3 se fabrica a partir de un Quantum Laser 3.** Primero fabricas el Quantum Laser 3 y el Starfire-3 lo consume. Nada de lo que ya costó el Quantum Laser 3 se pide otra vez, así que los dos juntos cuestan exactamente lo que costaba un Starfire-3 por sí solo: 3.000 Thulium, 100.000 créditos, 25 Ship Fragments, 10 Velkonite Reinforced Plates, 1 Reinforced Hull Plate y 2 minutos. Si ya tienes un Quantum Laser 3, solo pagas la parte propia del Starfire-3. Las reglas son las del Helios Beam, más abajo: el Starfire-3 conserva el grado de encantamiento del Quantum Laser 3 que consume (un Quantum Laser 3 Divino da un Starfire-3 Divino) y sus bonificaciones se sortean de nuevo; tú eliges qué Quantum Laser 3 se va, la tarjeta pregunta antes de usar uno por encima de Estándar, y el Quantum Laser 3 debe estar suelto: **quítalo primero de tu nave** (sus amplificadores vuelven a tu inventario) y sácalo del Alijo de Transporte. El botón Ensamblar dice «Desequipa Quantum Laser 3» cuando está en una nave.

**El Helios Beam se fabrica a partir de un Starfire-3.** Primero fabricas el Starfire-3 (3.000 Thulium y 100.000 créditos con su Quantum Laser 3) y el Helios Beam lo consume, igual que el [Master Drone](/wiki/06-Items/Drones.md) consume un Slave Drone. Nada de lo que ya costó el Starfire-3 se pide otra vez, así que los dos juntos cuestan lo que el Helios Beam pedía por sí solo (5.000 Thulium, Cataclysite, Power Cores y Reinforced Hull Plates) y 18 placas de Orvium en lugar de 20 (las diez placas de Velkonite del Starfire-3 sustituyen a las dos que faltan); lo que pagas además son los 100.000 créditos y los 25 Ship Fragments del Starfire-3. La regla es la de las [mejoras de módulos](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly): el Helios Beam conserva el grado de encantamiento del Starfire-3 que consume (un Starfire-3 Divino da un Helios Beam Divino) y sus bonificaciones se sortean de nuevo; tú eliges qué Starfire-3 se va cuando tienes varios, y la tarjeta pregunta antes de usar uno por encima de Estándar. El Starfire-3 debe estar suelto: **quítalo primero de tu nave** (los amplificadores instalados en él vuelven a tu inventario) y sácalo del Alijo de Transporte. El botón Ensamblar dice «Desequipa Starfire-3» cuando está en una nave.

De dónde salen las placas:

- Las **Velkonite Reinforced Plates** (Quantum Laser 3 y Starfire-3) se forjan a partir de Velkonite, 40 de mineral por placa con la Forja del Skylab en nivel 1. Las **Orvium Reinforced Plates** (Helios Beam) se forjan a partir de Orvium, 80 de mineral por placa.
- El mineral solo sale de los colectores de tu Skylab. Un Colector de Velkonite de nivel 5 extrae unos 29 de Velkonite por hora, así que las placas de un Quantum Laser 3 requieren unas 3 horas de minería y las diez de un Starfire-3 (dos en su Quantum Laser 3, ocho en su propio paso) unas 14. El Helios Beam es el largo: sus 18 placas necesitan 1.440 de Orvium, unos 4 días con un Colector de Orvium de nivel 5.
- El Almacén de recursos guarda 900 de cada mineral en el nivel 1, así que forja sobre la marcha (un lote de la Forja son 10 placas en el nivel 1) o mejora el almacén.
- Las placas forjadas esperan en la Forja hasta que las recoges con la nave en la base, y llegan a tu inventario como objetos normales.

Ship Fragments, Cataclysite, Power Cores y Reinforced Hull Plates caen de los alienígenas; todas las fuentes y usos de cada material están en la página [Recursos](/wiki/06-Items/Resources.md); las listas de botín de las páginas del [Bulwark](/wiki/04-Aliens/Bulwark.md) y del [Goombah](/wiki/04-Aliens/Goombah.md) indican cuánto.

---

## Amplificadores láser (amps) {#laser-amplifiers-amps-}

Equípalos directamente en la ranura de un láser para mejorar sus características. Hay dos líneas, de cuatro escalones cada una: la **línea de daño** suma una cantidad fija de daño, y la **línea de crítico** suma probabilidad de crítico y daño crítico fijo.

| Nombre | Rareza | Aumento de daño base | Aum. prob. crítico | Daño crítico fijo | Costo |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Damage Amp 1** | Deficiente | +10 | +5 % | +5 | 10.000 créditos |
| **Arc Amp** | Poco común | +16 | +5 % | +8 | 60.000 créditos |
| **Pulse Amp** | Raro | +26 | +6 % | +13 | 1.500 Thulium |
| **Nova Amp** | Épico | +38 | +7 % | +20 | Solo fabricable |
| **Crit Amp 1** | Deficiente | +0 | +15 % | +0 | 15.000 créditos |
| **Focus Amp** | Poco común | +0 | +20 % | +14 | 60.000 créditos |
| **Prism Amp** | Raro | +0 | +25 % | +24 | 1.500 Thulium |
| **Apex Amp** | Épico | +0 | +25 % | +44 | Solo fabricable |

El Nova Amp y el Apex Amp se fabrican en [Ensamblaje](/wiki/06-Items/Overview.md#upgrading-modules) a partir de un Pulse Amp y de un Prism Amp, con Thulium, botín y 3 Velkonite Reinforced Plates de tu Skylab cada uno. Conservan el grado de encantamiento del amplificador que consumen, y sus bonificaciones se sortean de nuevo ([Mejoras de módulos](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)).

### Qué amplificador va dónde {#which-amp-goes-where}

Un amplificador de daño suma el mismo daño a cualquier láser, así que vale más en los **láseres Quantum**. Un amplificador de crítico multiplica lo que el láser ya hace, así que vale más cuanto más fuerte pega el láser: iguala a la línea de daño en el **Starfire-3** y sale un 3,5 % por delante en el **Helios Beam**. La probabilidad de crítico de un láser se detiene en el 100 %: tres Prism Amps o Apex Amps llevan un Helios Beam exactamente a eso.

Con el mismo amplificador en todas las ranuras, un láser siempre es más fuerte que el del escalón inferior, así que un amplificador mejor nunca sustituye a un láser mejor: un Quantum Laser 3 con tres Nova Amps hace menos daño que un Helios Beam con tres Damage Amp 1 (con piezas del mismo grado de encantamiento: un Quantum Laser 3 y Nova Amps forjados a Divino o superior, con las mejores tiradas, pueden superar a un Helios Beam de grado Estándar con Damage Amp 1, por un pelo con grado Divino).

---

## Munición láser {#laser-ammunition}

Baterías consumibles que multiplican el daño de tus andanadas láser:

| Nombre | Rareza | Multiplicador de daño | Penetración de escudo | Precio por unidad |
| :--- | :--- | :---: | :---: | :--- |
| **Standard Battery** | Común | x1,0 | – | 10 créditos |
| **Advanced Plasma** | Raro | x2,0 | – | 0,5 Thulium |
| **Ultra Core** | Raro | x3,0 | 5 % | 1,0 Thulium |
| **Experimental Fusion Core** | Épico | x4,0 | 10 % | 2,2 Thulium |
| **Siphon Battery** | Raro | x1,0, solo escudos | – | 0,25 Thulium |

La **penetración de escudo** se resta de la absorción de tu objetivo en cada impacto de tus andanadas: los escudos reciben la absorción del objetivo menos la penetración (consulta [Mecánicas de los escudos](/wiki/03-Mechanics/Shields.md#shield-penetration)). Contra una nave con 80 % (el mejor escudo con las mejores células), el 10 % de la munición x4 deja a los escudos el 70 % del impacto y al casco el 30 %. Importa sobre todo contra naves cuyo casco es pequeño frente a su escudo; una nave muy grande con 80 % aguanta lo mismo de cualquiera de las dos formas. Los alienígenas no tienen una estadística de absorción propiamente dicha (sus escudos reciben el 80 % de un impacto), y la penetración también se resta de eso.

### Siphon Battery {#siphon-battery}

La Siphon Battery es una munición para robar escudos en lugar de romper cascos. Causa **daño x1 directamente al escudo del objetivo** y suma la misma cantidad a **tu propio escudo**, hasta tu máximo. Elígela en el selector de munición de la barra rápida como cualquier otra munición (es la casilla con el vórtice turquesa). No dispara un rayo: una sonda fina y tenue de color turquesa sale hacia el objetivo, el escudo del objetivo destella en turquesa donde llega, y el escudo que drenaste vuelve visiblemente a tu nave en forma de paquetes brillantes turquesa (de tres a diez, más cuanto mayor es el drenaje), uno tras otro durante aproximadamente medio segundo. Cada paquete que llega hace pulsar tu escudo. Ves lo mismo con la Siphon Battery de cualquier piloto que esté a la vista, sea a quien sea al que drene: alienígenas, otros pilotos y naves de pilotos de corporación.

- **Solo escudo**: el casco nunca se toca, la absorción del objetivo no reparte el daño, y una Siphon Battery nunca puede destruir nada. Su daño está limitado por lo que aún tiene el escudo del objetivo.
- **Nada que robar**: contra un objetivo sin escudo no drena nada y no da nada. La andanada se gasta igualmente, una batería por láser, como con toda munición. Solo ves la sonda y un parpadeo apagado en el casco, y ningún paquete.
- **Ganancia**: tu escudo nunca supera su máximo, y absorber escudo no retrasa la regeneración de tu propio escudo.
- **Los alienígenas y los pilotos** por igual tienen escudos que drenar. Un drenaje que quita escudo a un alienígena cuenta como impacto para la [reclamación del primer impacto](/wiki/03-Mechanics/Combat.md); uno que no encuentra escudo, no. También despierta a un Seeker o a un Goombah, que solo contraatacan, como cualquier otro impacto.
- **Los golpes críticos** cuentan: una andanada crítica drena 1,5 veces más, y su número se dibuja como un golpe crítico. Sus paquetes son más grandes y brillantes, y el escudo del objetivo destella con más fuerza.
- Los [pilotos de corporación](/wiki/03-Mechanics/Company-Pilots.md) disparan munición estándar x1.
