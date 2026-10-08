<!-- wiki-i18n source: 9288511cf701ce85 -->
<!-- wiki-i18n title: Láseres -->
# Láseres y munición {#lasers-ammo}

<!-- wiki-search: arc amp; focus amp; pulse amp; prism amp; nova amp; apex amp; damage amp 1; crit amp 1; amps; penetration amp; shield penetration -->

Las armas son el medio principal de causar daño en SpaceCorps.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Árbol de objetos {#item-tree}

Lo que fabrica Ensamblaje necesita antes su tecnología; pasa el cursor por un objeto para ver cuánto tarda en investigarse. El árbol de tecnologías, el combustible y el impulso: [Investigación](/wiki/03-Mechanics/Research.md).

```tree
Quantum Laser I | laser, shoddy | buy 8000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser II | laser, common | buy 80000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser III | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-III | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser III, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-III, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp I | laser-amp, shoddy | buy 10000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp I | laser-amp, shoddy | buy 15000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp I | laser-amp, shoddy | buy 15000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Damage Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Crit Amp I, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp II | laser-amp, uncommon | craft 250 Thulium, 60 s | research 1800 s, 1800 science | 1 Penetration Amp I, 20 Daraxium, 10 Cataclysite, 1 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Damage Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Crit Amp II, 1 Power Core, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp III | laser-amp, rare | craft 1000 Thulium, 60 s | research 10800 s, 10800 science | 1 Penetration Amp II, 1 Power Core, 30 Nyxite, 20 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Damage Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Damage Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp IV | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Crit Amp III, 1 Power Core, 30 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Penetration Amp IV | laser-amp, epic | craft 1200 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Penetration Amp III, 1 Power Core, 30 Cataclysite, 40 Quorvium, 3 Dark Matter Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Standard Battery | ammo, common | buy 5 Credits | /wiki/06-Items/Lasers.md#laser-ammunition
Siphon Battery | ammo, rare | buy 0.25 Thulium | /wiki/06-Items/Lasers.md#siphon-battery
Advanced Plasma | ammo, rare | buy 0.5 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Ultra Core | ammo, rare | buy 1 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Experimental Fusion Core | ammo, epic | buy 2.2 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition

Quantum Laser I -> Quantum Laser II -> Quantum Laser III => Starfire-III => Helios Beam
Damage Amp I => Damage Amp II => Damage Amp III => Damage Amp IV
Crit Amp I => Crit Amp II => Crit Amp III => Crit Amp IV
Penetration Amp I => Penetration Amp II => Penetration Amp III => Penetration Amp IV
Standard Battery -> Advanced Plasma -> Ultra Core -> Experimental Fusion Core
```
<!-- item-tree:end -->

## Láseres {#lasers}

Equipa láseres directamente en las ranuras de láser de la nave o dentro de drones para aumentar tu capacidad ofensiva.

| Nombre | Rareza | Daño base | Prob. crítico | Alcance | Ranuras de amp. | Costo |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Quantum Laser I** | Deficiente | 55 | – | 600 | 1 | 8.000 créditos |
| **Quantum Laser II** | Común | 65 | – | 700 | 2 | 80.000 créditos |
| **Quantum Laser III** | Raro | 80 | 10 % | 800 | 3 | Solo fabricable |
| **Starfire-III** | Mítico | 135 | 15 % | 850 | 3 | Solo fabricable |
| **Helios Beam** | Mítico | 185 | 25 % | 900 | 3 | Solo fabricable |

La columna Alcance es la de cada láser por separado. **Tu nave dispara al alcance medio de sus láseres** (cuentan también los láseres de tus drones), redondeado a la unidad más cercana, y todos los láseres disparan en cuanto el objetivo está dentro de esa distancia. Un Starfire-III junto a dos Quantum Laser II da a la nave un alcance de 750, no de 850; tres Starfire-III mantienen 850, y los láseres que son todos iguales no cambian nada. Una bonificación de alcance de la Forja cuenta en su propio láser antes de calcular la media. Sin ningún láser, el hangar no muestra alcance (un guion) y los láseres no pueden disparar, pero tus cohetes sí, cada uno con su propio alcance (consulta [Cohetes](/wiki/06-Items/Rockets.md)). En el hangar, la casilla dice «Alcance medio» cuando tus láseres difieren, y al pasar el cursor por encima se lista el alcance de cada láser.

El Quantum Laser I y el II no tienen probabilidad de crítico propia («–»): se la da un Damage Amp o un Crit Amp en sus ranuras (un Penetration Amp no). Los golpes críticos se muestran con otro color en los números de daño flotantes (azul hielo, más grandes y con un «!»; consulta [Números de daño y de curación](/wiki/03-Mechanics/Combat.md#damage-and-heal-numbers)).

Los láseres también dañan los [asteroides](/wiki/03-Mechanics/Asteroid-Mining.md#breaking-one), pero solo con el 5 % de lo que una andanada hace a una nave (cuentan tus amplificadores, potenciadores, munición y golpes críticos, y después se resta el blindaje del asteroide; la Siphon Battery no puede dañar ninguno). Para romperlos, la herramienta son los cohetes.

### Cómo se fabrican los tres mejores láseres {#making-the-top-three-lasers}

El **Quantum Laser III**, el **Starfire-III** y el **Helios Beam** se fabrican solo en **Ensamblaje**. El Quantum Laser III ya no se vende en la tienda; el piloto que ya tiene uno se lo queda. Cada receta pide placas de la Forja del [Skylab](/wiki/03-Mechanics/Skylab.md), y el Helios Beam además 3 Dark Matter Plates:

| Láser | Tiempo de fabricación | Qué necesita |
| :--- | :---: | :--- |
| Quantum Laser III | 1 min | 10 Ship Fragments, 2 Velkonite Reinforced Plates, 1.500 Thulium |
| Starfire-III | 1 min | 1 Quantum Laser III, 15 Ship Fragments, 8 Velkonite Reinforced Plates, 1 Reinforced Hull Plate, 1.500 Thulium, 100.000 créditos |
| Helios Beam | 3 min | 1 Starfire-III, 50 Cataclysite, 2 Power Cores, 18 Orvium Reinforced Plates, 3 Dark Matter Plates, 4 Reinforced Hull Plates, 2.000 Thulium |

La página de Ensamblaje muestra lo que tienes frente a lo que pide una receta, y el botón Ensamblar dice lo que te falta. Si apuntas a la imagen o al nombre de una receta, o a uno de sus materiales, aparecen la descripción completa y las estadísticas del objeto.

**El Starfire-III se fabrica a partir de un Quantum Laser III.** Primero fabricas el Quantum Laser III y el Starfire-III lo consume. Nada de lo que ya costó el Quantum Laser III se pide otra vez, así que los dos juntos cuestan exactamente lo que costaba un Starfire-III por sí solo: 3.000 Thulium, 100.000 créditos, 25 Ship Fragments, 10 Velkonite Reinforced Plates, 1 Reinforced Hull Plate y 2 minutos. Si ya tienes un Quantum Laser III, solo pagas la parte propia del Starfire-III. Las reglas son las del Helios Beam, más abajo: el Starfire-III conserva el grado de encantamiento del Quantum Laser III que consume (un Quantum Laser III Divino da un Starfire-III Divino) y sus bonificaciones se sortean de nuevo; tú eliges qué Quantum Laser III se va, la tarjeta pregunta antes de usar uno por encima de Estándar, y el Quantum Laser III debe estar suelto: **quítalo primero de tu nave** (sus amplificadores vuelven a tu inventario) y sácalo del Alijo de Transporte. El botón Ensamblar dice «Desequipa Quantum Laser III» cuando está en una nave.

**El Helios Beam se fabrica a partir de un Starfire-III.** Primero fabricas el Starfire-III (3.000 Thulium y 100.000 créditos con su Quantum Laser III) y el Helios Beam lo consume, igual que el [Master Drone](/wiki/06-Items/Drones.md) consume un Slave Drone. Nada de lo que ya costó el Starfire-III se pide otra vez, así que los dos juntos cuestan lo que el Helios Beam pedía por sí solo (5.000 Thulium, Cataclysite, Power Cores y Reinforced Hull Plates) y 18 placas de Orvium en lugar de 20 (las diez placas de Velkonite del Starfire-III sustituyen a las dos que faltan), más, como el Helios Beam es el último nivel de su cadena, 3 Dark Matter Plates; lo que pagas además son los 100.000 créditos y los 25 Ship Fragments del Starfire-III. La regla es la de las [mejoras de módulos](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly): el Helios Beam conserva el grado de encantamiento del Starfire-III que consume (un Starfire-III Divino da un Helios Beam Divino) y sus bonificaciones se sortean de nuevo; tú eliges qué Starfire-III se va cuando tienes varios, y la tarjeta pregunta antes de usar uno por encima de Estándar. El Starfire-III debe estar suelto: **quítalo primero de tu nave** (los amplificadores instalados en él vuelven a tu inventario) y sácalo del Alijo de Transporte. El botón Ensamblar dice «Desequipa Starfire-III» cuando está en una nave.

De dónde salen las placas:

- Las **Velkonite Reinforced Plates** (Quantum Laser III y Starfire-III) se forjan a partir de Velkonite, 40 de mineral por placa con la Forja del Skylab en nivel 1. Las **Orvium Reinforced Plates** (Helios Beam) se forjan a partir de Orvium, 80 de mineral por placa.
- Las **Dark Matter Plates** (3 para el Helios Beam) se prensan en el Ensamblaje a partir de 5 Dark Matter, una Velkonite y una Orvium Reinforced Plate y 250 Thulium, una vez que has investigado su receta. Las tres necesitan 15 Dark Matter, 7,5 cohetes N.I.K.E. de media del [agujero negro](/wiki/03-Mechanics/Black-Hole.md): [Dark Matter y Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md) recoge todo el camino.
- El mineral solo sale de los colectores de tu Skylab. Un Colector de Velkonite de nivel 5 extrae 18 de Velkonite por hora, así que las placas de un Quantum Laser III requieren unas 4 horas de minería y las diez de un Starfire-III (dos en su Quantum Laser III, ocho en su propio paso) unas 22. El Helios Beam es el largo: sus 18 placas necesitan 1.440 de Orvium, unos 4 días con un Colector de Orvium de nivel 5, y las 3 placas de Orvium más que van dentro de sus 3 Dark Matter Plates suman 240 de Orvium, unas 17 horas.
- El Almacén de recursos guarda 240 de cada mineral en el nivel 1: 6 placas de Velkonite o 3 de Orvium con la Forja en el nivel 1. Así que forja sobre la marcha (un lote de la Forja son hasta 10 placas en el nivel 1) o mejora el almacén.
- Las placas forjadas esperan en la Forja hasta que las recoges con la nave en la base, y llegan a tu inventario como objetos normales.

Ship Fragments, Cataclysite, Power Cores y Reinforced Hull Plates caen de los alienígenas; todas las fuentes y usos de cada material están en la página [Recursos](/wiki/06-Items/Resources.md); las listas de botín de las páginas del [Bulwark](/wiki/04-Aliens/Bulwark.md) y del [Goombah](/wiki/04-Aliens/Goombah.md) indican cuánto.

---

## Amplificadores láser (amps) {#laser-amplifiers-amps-}

Equípalos directamente en la ranura de un láser para mejorar sus características. Hay **tres líneas de cuatro niveles**, nombradas como las células de escudo: el **Damage Amp** suma una cantidad fija de daño, el **Crit Amp** suma probabilidad de crítico y daño crítico fijo, y el **Penetration Amp** resta puntos a la absorción de tu objetivo ([más abajo](#shield-penetration-of-a-laser-hit)). No son los [potenciadores](/wiki/06-Items/Boosters.md): el **Laser Damage Booster I** y el **Laser Damage Booster II** son potenciadores con temporizador (+10 % de daño láser durante 10 horas), sin nada que equipar.

| Nombre | Rareza | Aumento de daño base | Aum. prob. crítico | Daño crítico fijo | Costo |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Damage Amp I** | Deficiente | +10 | +5 % | +5 | 10.000 créditos |
| **Damage Amp II** | Poco común | +16 | +5 % | +8 | Solo fabricable |
| **Damage Amp III** | Raro | +26 | +6 % | +13 | Solo fabricable |
| **Damage Amp IV** | Épico | +38 | +7 % | +20 | Solo fabricable |
| **Crit Amp I** | Deficiente | +0 | +15 % | +0 | 15.000 créditos |
| **Crit Amp II** | Poco común | +0 | +20 % | +14 | Solo fabricable |
| **Crit Amp III** | Raro | +0 | +25 % | +24 | Solo fabricable |
| **Crit Amp IV** | Épico | +0 | +25 % | +44 | Solo fabricable |

| Nombre | Rareza | Penetración de escudo | Costo |
| :--- | :--- | :---: | :--- |
| **Penetration Amp I** | Deficiente | +2 % | 15.000 créditos |
| **Penetration Amp II** | Poco común | +4 % | Solo fabricable |
| **Penetration Amp III** | Raro | +6 % | Solo fabricable |
| **Penetration Amp IV** | Épico | +8 % | Solo fabricable |

**Solo se vende el primer nivel de cada línea**, en la tienda. Los otros tres se fabrican en [Ensamblaje](/wiki/06-Items/Overview.md#upgrading-modules) a partir del amp del nivel inferior, una vez que has investigado su tecnología en el Skylab ([Investigación](/wiki/03-Mechanics/Research.md)). Cada paso pide Thulium, botín de alienígenas y placas (Velkonite Reinforced Plates de tu Skylab para los niveles II y III, 3 Dark Matter Plates para el nivel IV), y el nuevo amp conserva el grado de encantamiento del amp que consume mientras sus bonificaciones se sortean de nuevo ([Mejoras de módulos en el Ensamblaje](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Los pasos de Penetration añaden una lente de cristal. Cada amp del nivel IV pide 3 [Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md), como el último nivel de cada cadena de mejora, así que la tecnología de un amp del nivel IV pide antes la de la plate.

| Paso | Thulium | Tiempo | Además del amp del nivel inferior |
| :--- | ---: | ---: | :--- |
| Damage Amp II / Crit Amp II | 250 | 60 s | 10 Cataclysite, 1 Velkonite Reinforced Plate |
| Damage Amp III / Crit Amp III | 1.000 | 60 s | 20 Cataclysite, 1 Power Core, 2 Velkonite Reinforced Plate |
| Damage Amp IV / Crit Amp IV | 1.200 | 60 s | 30 Cataclysite, 1 Power Core, 3 Dark Matter Plate |
| Penetration Amp II | 250 | 60 s | 20 Daraxium, 10 Cataclysite, 1 Velkonite Reinforced Plate |
| Penetration Amp III | 1.000 | 60 s | 30 Nyxite, 20 Cataclysite, 1 Power Core, 2 Velkonite Reinforced Plate |
| Penetration Amp IV | 1.200 | 90 s | 40 Quorvium, 30 Cataclysite, 1 Power Core, 3 Dark Matter Plate |

Un Helios Beam con sus 3 amps del nivel IV contiene 4 piezas del último nivel: 12 Dark Matter Plates, 60 Dark Matter, 30 cohetes N.I.K.E. de media. Un Wraith con el último nivel en cada ranura contiene 900 Dark Matter ([Dark Matter y Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md#what-the-last-tier-asks-for)).

### Qué amplificador va dónde {#which-amp-goes-where}

Un amplificador de daño suma el mismo daño a cualquier láser, así que vale más en los **láseres Quantum**. Un amplificador de crítico multiplica lo que el láser ya hace, así que vale más cuanto más fuerte pega el láser: iguala a la línea de daño en el **Starfire-III** y sale un 3,5 % por delante en el **Helios Beam**. La probabilidad de crítico de un láser se detiene en el 100 %: tres Crit Amp III o Crit Amp IV llevan un Helios Beam exactamente a eso. Un Penetration Amp no da daño ni probabilidad de crítico: es para naves cuyos escudos, de otro modo, se llevarían la mayor parte de tu impacto ([más abajo](#when-is-a-penetration-amp-worth-a-slot)).

Con el mismo amplificador en todas las ranuras, un láser siempre es más fuerte que el del escalón inferior, así que un amplificador mejor nunca sustituye a un láser mejor: un Quantum Laser III con tres Damage Amp IV hace menos daño que un Helios Beam con tres Damage Amp I (con piezas del mismo grado de encantamiento: un Quantum Laser III y Damage Amp IV forjados a Divino o superior, con las mejores tiradas, pueden superar a un Helios Beam de grado Estándar con Damage Amp I, por un pelo con grado Divino).


---

## Munición láser {#laser-ammunition}

Baterías consumibles que multiplican el daño de tus andanadas láser:

| Nombre | Rareza | Multiplicador de daño | Penetración de escudo | Precio por unidad |
| :--- | :--- | :---: | :---: | :--- |
| **Standard Battery** | Común | x1,0 | – | 5 créditos |
| **Advanced Plasma** | Raro | x2,0 | – | 0,5 Thulium |
| **Ultra Core** | Raro | x3,0 | 5 % | 1,0 Thulium |
| **Experimental Fusion Core** | Épico | x4,0 | 10 % | 2,2 Thulium |
| **Siphon Battery** | Raro | x1,0, solo escudos | – | 0,25 Thulium |

La **penetración de escudo** se resta de la absorción de tu objetivo en cada impacto de tus andanadas: los escudos reciben la absorción del objetivo menos la penetración (consulta [Mecánicas de los escudos](/wiki/03-Mechanics/Shields.md#shield-penetration)). Tus Penetration Amps y una formación de drones se suman a la de la munición, y la suma entera está [más abajo en esta página](#shield-penetration-of-a-laser-hit). Contra una nave con 80 % (el mejor escudo con las mejores células), el 10 % de la munición x4 deja a los escudos el 70 % del impacto y al casco el 30 %. Importa sobre todo contra naves cuyo casco es pequeño frente a su escudo; una nave muy grande con 80 % aguanta lo mismo de cualquiera de las dos formas. Los alienígenas no tienen una estadística de absorción propiamente dicha (sus escudos reciben el 80 % de un impacto), y la penetración también se resta de eso.

### Siphon Battery

La Siphon Battery es una munición para robar escudos en lugar de romper cascos. Causa **daño x1 directamente al escudo del objetivo** y suma la misma cantidad a **tu propio escudo**, hasta tu máximo. Elígela en el selector de munición de la barra rápida como cualquier otra munición (es la casilla con el vórtice turquesa). No dispara un rayo: una sonda fina y tenue de color turquesa sale hacia el objetivo, el escudo del objetivo destella en turquesa donde llega, y el escudo que drenaste vuelve visiblemente a tu nave en forma de paquetes brillantes turquesa (de tres a diez, más cuanto mayor es el drenaje), uno tras otro durante aproximadamente medio segundo. Cada paquete que llega hace pulsar tu escudo. Ves lo mismo con la Siphon Battery de cualquier piloto que esté a la vista, sea a quien sea al que drene: alienígenas, otros pilotos y naves de pilotos de corporación.

- **Solo escudo**: el casco nunca se toca, la absorción del objetivo no reparte el daño, y una Siphon Battery nunca puede destruir nada. Su daño está limitado por lo que aún tiene el escudo del objetivo.
- **Nada que robar**: contra un objetivo sin escudo no drena nada y no da nada. La andanada se gasta igualmente, una batería por láser, como con toda munición. Solo ves la sonda y un parpadeo apagado en el casco, y ningún paquete.
- **Ganancia**: tu escudo nunca supera su máximo, y absorber escudo no retrasa la regeneración de tu propio escudo.
- **Los alienígenas y los pilotos** por igual tienen escudos que drenar. Un drenaje que quita escudo a un alienígena cuenta como impacto para la [reclamación del primer impacto](/wiki/03-Mechanics/Combat.md); uno que no encuentra escudo, no. También despierta a un Seeker o a un Goombah, que solo contraatacan, como cualquier otro impacto.
- **Los golpes críticos** cuentan: una andanada crítica drena 1,5 veces más, y su número se dibuja como un golpe crítico. Sus paquetes son más grandes y brillantes, y el escudo del objetivo destella con más fuerza.
- Los [pilotos de corporación](/wiki/03-Mechanics/Company-Pilots.md) disparan munición estándar x1.

---

## Penetración de escudo de un impacto láser {#shield-penetration-of-a-laser-hit}

Cada impacto láser resta puntos a la absorción de tu objetivo, de hasta tres fuentes que se suman: tu **munición** (Ultra Core 5 %, Experimental Fusion Core 10 %), tus **Penetration Amps** y una **formación de drones** (Gemini +9 %, Stiletto +16 %; [Formaciones de drones](/wiki/03-Mechanics/Formations.md)). El total **se detiene en el 50 %** para un láser; el de un cohete directo se detiene en el 40 % ([Cohetes](/wiki/06-Items/Rockets.md)). Los escudos reciben entonces la absorción del objetivo menos la penetración del impacto, y el casco el resto ([Mecánicas de los escudos](/wiki/03-Mechanics/Shields.md#shield-penetration)).

- **Tus amps cuentan como la media de tus láseres.** Una andanada es un solo impacto, así que el juego suma la penetración de los amps de cada láser (los láseres de tus drones cuentan también) y toma la media de tus láseres, cada uno ponderado por su daño, como hace con la probabilidad de crítico. Tres Penetration Amp IV en cada láser dan 24 %; un Penetration Amp IV en uno de doce láseres da 0,67 %. Un Wraith tiene 12 láseres y 36 ranuras de amp, y hay que llenar las 36 para llegar al 24 %.
- **El Hangar lo muestra.** Las estadísticas de combate del Hangar tienen un recuadro **Penetración** en cada nave, con la cifra de tus amps (0,0 % sin ningún Penetration Amp); la munición y la formación no entran en ella. Apunta al recuadro para leer los topes: el total de un impacto láser se detiene en el 50 %, el de un cohete en el 40 %.
- **El mejor láser llega justo al tope.** Un Experimental Fusion Core (10 %), un Stiletto (16 %) y tres Penetration Amp IV en cada láser (24 %) suman 50 %.
- **Una bonificación de la Forja en un Penetration Amp IV se desperdicia en ese montaje.** Un Penetration Amp se puede forjar como los demás amps, y su única bonificación multiplica la penetración: una bonificación Eterna (+9 % a +15 %) deja un Penetration Amp IV en 8,7 a 9,2 puntos en lugar de 8. Pero 10 + 16 + 24 ya dan el tope del 50 %, y cada punto de más se recorta (tres Eternos sumarían 53,6 %, recortado a 50 %).

| Andanada láser | Munición | Amps (3 ranuras) | Formación | Total |
|---|---|---|---|---|
| Experimental Fusion Core solo | 10 % | – | – | **10 %** |
| Fusion Core + Gemini | 10 % | – | 9 % | **19 %** |
| Fusion Core + Stiletto (lo mejor antes de los Penetration Amps) | 10 % | – | 16 % | **26 %** |
| Fusion Core + 3 Penetration Amp I | 10 % | 6 % | – | **16 %** |
| Fusion Core + 3 Penetration Amp II | 10 % | 12 % | – | **22 %** |
| Fusion Core + 3 Penetration Amp III | 10 % | 18 % | – | **28 %** |
| Fusion Core + 3 Penetration Amp IV | 10 % | 24 % | – | **34 %** |
| Fusion Core + 3 Penetration Amp IV + Gemini | 10 % | 24 % | 9 % | **43 %** |
| Ultra Core + 3 Penetration Amp IV + Stiletto (lo mejor para el día a día) | 5 % | 24 % | 16 % | **45 %** |
| Fusion Core + 3 Penetration Amp IV + Stiletto (el mejor láser) | 10 % | 24 % | 16 % | **50 %** |

Lo que eso hace con los escudos del objetivo: cada celda es la parte de un impacto que **se llevan los escudos / se lleva el casco**.

| Defensor (absorción) | Sin amps | Fusion Core solo (10 %) | Antes: Fusion Core + Stiletto (26 %) | Fusion Core + 3 Penetration Amp IV (34 %) | El mejor láser (50 %) |
|---|---|---|---|---|---|
| Light Shield Core, sin célula (45 %) | 45 / 55 | 35 / 65 | 19 / 81 | 11 / 89 | 0 / 100 |
| Heavy Shield Core, sin célula (50 %) | 50 / 50 | 40 / 60 | 24 / 76 | 16 / 84 | 0 / 100 |
| Light Shield Core + Absorption Shield Cell IV (55 %) | 55 / 45 | 45 / 55 | 29 / 71 | 21 / 79 | 5 / 95 |
| Heavy Shield Core + 3 Capacity Shield Cell IV (65 %) | 65 / 35 | 55 / 45 | 39 / 61 | 31 / 69 | 15 / 85 |
| El mejor escudo de fábrica (80 %) | 80 / 20 | 70 / 30 | 54 / 46 | 46 / 54 | 30 / 70 |
| El mejor escudo, con Eterno de la Forja (mejor tirada) y 34 niveles de la Tienda de temporada (95,4 %) | 95 / 5 | 85 / 15 | 69 / 31 | 61 / 39 | 45 / 55 |
| El mejor escudo, con Eterno de la Forja (mejor tirada) y la Tienda de temporada en su límite (102 %) | 100 / 0 | 92 / 8 | 76 / 24 | 68 / 32 | 52 / 48 |
| Cualquier alienígena (80 %) | 80 / 20 | 70 / 30 | 54 / 46 | 46 / 54 | 30 / 70 |

El mejor láser vacía un núcleo de escudo sin célula (el casco recibe todo el impacto); un núcleo con una célula conserva una parte de cada impacto, y el mejor escudo conserva el 30 % (45 % con las mejoras). Un cohete nunca vacía un escudo: su tope es el 40 %.

### ¿Cuándo compensa un Penetration Amp una ranura? {#when-is-a-penetration-amp-worth-a-slot}

**Un Penetration Amp contrarresta una absorción por encima de aprox. el 95 % (montajes con Tienda de temporada, Forja y Rampart). Contra el mejor escudo de fábrica (80 %), un Crit Amp del mismo nivel sigue siendo un 10 % más rápido, y un Penetration Amp no mata alienígenas más rápido que un Damage Amp o un Crit Amp de su nivel.**

- **No da daño.** En un Helios Beam, tres Penetration Amp IV dan 187 de daño por andanada (munición x1, la media de la tirada y de los críticos), donde tres Damage Amp IV dan 356 y tres Crit Amp IV 369: aproximadamente la mitad. Lo que recupera es la parte del escudo, así que solo compensa donde el casco es pequeño frente al escudo y la absorción es alta; contra un Wraith o un Ironclad, cuyo gran casco aguanta igualmente, un conjunto simple de Damage o Crit es más rápido.
- **Alienígenas.** Sus escudos reciben el 80 % de un impacto menos tu penetración, así que también funciona con ellos, pero un Damage Amp o un Crit Amp del nivel los mata igualmente más rápido.
- **Lo que cuesta.** Cada Penetration Amp IV pide 3 Dark Matter Plates (15 Dark Matter), como todo amp del nivel IV, así que un Wraith que llene sus 36 ranuras necesita 108 plates, 540 Dark Matter.
