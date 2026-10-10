<!-- wiki-i18n source: 7a131032ce9f07fb -->
<!-- wiki-i18n title: Escudos -->
# Escudos y defensa {#shields-defense}

Los módulos defensivos aportan capacidad de escudo, absorben daño y recargan tus defensas.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Árbol de objetos {#item-tree}

Lo que fabrica Ensamblaje necesita antes su tecnología; pasa el cursor por un objeto para ver cuánto tarda en investigarse. El árbol de tecnologías, el combustible y el impulso: [Investigación](/wiki/03-Mechanics/Research.md).

```tree
Light Shield Core | shield, shoddy | buy 20000 Credits | /wiki/06-Items/Shields.md#shield-cores
Basic Shield Core | shield, common | buy 2000 Thulium | /wiki/06-Items/Shields.md#shield-cores
Heavy Shield Core | shield, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Basic Shield Core, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cores
Adaptive Core I | hybrid-generator, shoddy | buy 100000 Credits | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core II | hybrid-generator, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Adaptive Core I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Adaptive Core III | hybrid-generator, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Adaptive Core II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#hybrid-generators-adaptive-cores-
Absorption Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell I | shield-cell, shoddy | buy 30000 Credits | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Absorption Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell II | shield-cell, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Capacity Shield Cell I, 4 Reinforced Hull Plate, 10 Cataclysite, 2 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Absorption Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell III | shield-cell, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Capacity Shield Cell II, 6 Reinforced Hull Plate, 15 Cataclysite, 4 Velkonite Reinforced Plate | /wiki/06-Items/Shields.md#shield-cells
Absorption Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Absorption Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells
Capacity Shield Cell IV | shield-cell, epic | craft 2500 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Capacity Shield Cell III, 8 Reinforced Hull Plate, 20 Cataclysite, 3 Dark Matter Plate | /wiki/06-Items/Shields.md#shield-cells

Light Shield Core -> Basic Shield Core => Heavy Shield Core
Adaptive Core I => Adaptive Core II => Adaptive Core III
Absorption Shield Cell I => Absorption Shield Cell II => Absorption Shield Cell III => Absorption Shield Cell IV
Capacity Shield Cell I => Capacity Shield Cell II => Capacity Shield Cell III => Capacity Shield Cell IV
```
<!-- item-tree:end -->

## Núcleos de escudo {#shield-cores}

Equipa núcleos de escudo para generar barreras defensivas activas, en las ranuras de generador de tu nave o en tus [drones](/wiki/03-Mechanics/Drones.md) (la ranura de un dron cuenta como una ranura principal). Ten en cuenta que los escudos pesados reducen tu velocidad. Un núcleo de escudo en una **ranura de habilidad** te da en cambio el **Shield Surge** de la columna Efecto especial, una reparación del escudo durante diez segundos, y no aporta escudo propio (consulta [Habilidades](/wiki/03-Mechanics/Abilities.md)).

| Nombre | Rareza | Capacidad | Vel. de recarga | Absorción | Escudo % | Velocidad % | Ranuras de célula | Efecto especial | Costo |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Light Shield Core** | Deficiente | 10.000 | 333/s | 45 % | +5 % | -1 % | 1 | Shield Surge I | 20.000 créditos |
| **Basic Shield Core** | Común | 15.000 | 500/s | 48 % | +10 % | -3 % | 2 | Shield Surge II | 2.000 Thulium |
| **Heavy Shield Core** | Raro | 25.000 | 833/s | 50 % | +20 % | -5 % | 3 | Shield Surge III | Solo fabricable |

El **Heavy Shield Core** se fabrica en [Ensamblaje](/wiki/06-Items/Overview.md#upgrading-modules) a partir de un Basic Shield Core, con 2.000 Thulium, 20 Cataclysite, 8 Reinforced Hull Plates y 3 Dark Matter Plates ([Dark Matter y Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)). Conserva el grado de encantamiento del núcleo que consume, y sus bonificaciones se sortean de nuevo ([Mejoras de módulos](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Quita primero el Basic Shield Core de tu nave (y saca de él sus células): un núcleo que está instalado o que lleva células no se consume.

La **absorción** es la parte de cada impacto que se llevan tus escudos; el casco recibe el resto. Un escudo solo tiene del **45 al 50 %**, y sus células suman el resto: el mejor escudo con las mejores células (un Heavy Shield Core con tres Absorption Shield Cell IV) llega al **80 %**, lo máximo que tiene una nave de serie. A eso se suman dos mejoras: la mejora Shield Absorbance Boost de la Tienda de temporada (+0,1 puntos por nivel, 100 niveles, 25 puntos de reinicio cada uno) y las bonificaciones de absorción de la Forja. Las fuentes actuales de puntos de reinicio (855 en total en sus límites, que se conservan entre reinicios; hay previstas más fuentes) compran 34 de esos 100 niveles (+3,4 puntos), lo que con un juego de grado Eterno totalmente forjado da en torno al **95 %**. Aun así, la estadística no tiene tope en el 100 %: la *penetración de escudo* de un atacante se resta de ella, así que lo que una nave tiene por encima del 100 % es su margen frente a la penetración. Consulta [Mecánicas de los escudos](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-).

---

## Generadores híbridos (núcleos adaptativos) {#hybrid-generators-adaptive-cores-}

Los núcleos adaptativos funcionan como generadores híbridos, combinando capacidades de escudo y de velocidad. Admiten tanto propulsores como células de escudo en sus ranuras (un módulo por ranura, de cualquiera de los dos tipos). Su bono de escudo y de velocidad cuenta como el de un escudo o el de un motor (los cuatro mejores, por el rendimiento de la ranura). No tienen absorción: no cambian la absorción de tu nave, y las células que llevan solo suman capacidad y recarga. Solo los escudos se llevan una parte de un impacto, así que las células de un núcleo adaptativo necesitan también un escudo en la nave.

| Nombre | Rareza | Bono de escudo % | Bono de velocidad % | Ranuras | Efecto especial | Costo |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **Adaptive Core I** | Deficiente | +4 % | +2,4 % | 1 | — | 100.000 créditos |
| **Adaptive Core II** | Común | +6,4 % | +3,2 % | 2 | — | Solo fabricable |
| **Adaptive Core III** | Raro | +8 % | +4 % | 3 | — | Solo fabricable |

El **Adaptive Core II** se fabrica en [Ensamblaje](/wiki/06-Items/Overview.md#upgrading-modules) a partir de un Adaptive Core I, con 1.000 Thulium, 10 Ship Fragments, 1 Power Core y 2 Velkonite Reinforced Plates. El **Adaptive Core III** se fabrica allí a partir de un Adaptive Core II, con 2.000 Thulium, 60 Ship Fragments, 3 Power Cores y 3 Dark Matter Plates ([Dark Matter y Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)). Cada uno conserva el grado de encantamiento del núcleo que consume, y sus bonificaciones se sortean de nuevo ([Mejoras de módulos](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Quita primero de tu nave el núcleo que vas a consumir (y saca de él sus propulsores y células): un núcleo que está instalado o que lleva módulos no se consume.

---

## Células de escudo {#shield-cells}

Las células de escudo se instalan dentro de núcleos de escudo o de núcleos adaptativos (tantas como ranuras tiene el núcleo) para potenciar ese núcleo. En un núcleo de escudo suben también su absorción, en puntos, y con ella la parte de cada impacto que se llevan tus escudos. Hay dos familias de cuatro niveles cada una: las **Capacity Shield Cell** aportan más escudo y recarga, las **Absorption Shield Cell** más absorción (en cada nivel, el doble de absorción y la mitad de escudo y recarga que la Capacity de ese nivel). Capacity ayuda a una nave en la que el escudo decide el combate; Absorption, a una en la que lo decide el casco. Un núcleo con todas sus ranuras llenas de una misma célula: un Light Shield Core (1 ranura) da del 47 al 55 %, un Basic Shield Core (2 ranuras) del 52 al 68 % y un Heavy Shield Core (3 ranuras) del 56 al 80 %, de las células Capacity de nivel I a las Absorption de nivel IV. Desequipar el núcleo, o consumirlo como donante de una combinación de la [Forja](/wiki/06-Items/Forge.md), devuelve sus células al inventario.

| Nombre | Rareza | Aumento de capacidad | Aumento de recarga | Aumento de absorción | Costo |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Capacity Shield Cell I** | Deficiente | +3.000 | +250/s | +2 % | 30.000 créditos |
| **Capacity Shield Cell II** | Común | +6.000 | +500/s | +3 % | Solo fabricable |
| **Capacity Shield Cell III** | Raro | +9.000 | +750/s | +4 % | Solo fabricable |
| **Capacity Shield Cell IV** | Épico | +12.000 | +1.000/s | +5 % | Solo fabricable |
| **Absorption Shield Cell I** | Deficiente | +1.500 | +125/s | +4 % | 30.000 créditos |
| **Absorption Shield Cell II** | Común | +3.000 | +250/s | +6 % | Solo fabricable |
| **Absorption Shield Cell III** | Raro | +4.500 | +375/s | +8 % | Solo fabricable |
| **Absorption Shield Cell IV** | Épico | +6.000 | +500/s | +10 % | Solo fabricable |

El nivel I de cada familia se vende por 30.000 créditos. Los niveles II a IV se fabrican en [Ensamblaje](/wiki/06-Items/Overview.md#upgrading-modules), cada uno a partir de la célula de la misma familia un nivel por debajo (una Capacity Shield Cell II a partir de una Capacity Shield Cell I, una III a partir de una II, una IV a partir de una III), con Thulium, botín y placas: 2 o 4 Velkonite Reinforced Plates de tu Skylab para el nivel II o III, y 3 Dark Matter Plates para el nivel IV. Una célula nunca cambia de familia: eliges Capacity o Absorption al comprar el nivel I. La célula nueva conserva el grado de encantamiento de la célula que consume, y sus bonificaciones se sortean de nuevo ([Mejoras de módulos](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Las células no caben en una [ranura de habilidad](/wiki/03-Mechanics/Abilities.md); van dentro de escudos y de núcleos adaptativos.
