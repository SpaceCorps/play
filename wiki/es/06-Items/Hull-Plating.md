<!-- wiki-i18n source: 2bd1925e336e25b6 -->
<!-- wiki-i18n title: Blindaje de casco -->
# Blindaje de casco {#hull-plating}

<!-- wiki-search: hull plate; hull plate slot; hull plate slots; plate slot; plate; armour; armor; hpl; blindaje; ranura de blindaje; placa de casco -->

El estudio del enjambre Dormant mostró avances en la tecnología de blindaje. Con ella, las naves pueden mejorar su casco: el **blindaje de casco** es un blindaje que encaja en una ranura de placa de casco de una nave fabricada y le añade puntos de casco. No es el Hull Plating **Booster** de la página [Potenciadores](/wiki/06-Items/Boosters.md), que es una bonificación temporal.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Árbol de objetos {#item-tree}

Lo que fabrica Ensamblaje necesita antes su tecnología; pasa el cursor por un objeto para ver cuánto tarda en investigarse. El árbol de tecnologías, el combustible y el impulso: [Investigación](/wiki/03-Mechanics/Research.md).

```tree
Hull Plating I | hull-plating, uncommon | buy 5000 Thulium | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating II | hull-plating, rare | craft 2500 Thulium, 300 s | research 86400 s, 86400 science, 25 Dark Matter | 1 Hull Plating I, 150 Ship Fragment, 20 Reinforced Hull Plate, 6 Power Core, 5 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings
Hull Plating III | hull-plating, epic | craft 4000 Thulium, 600 s | research 172800 s, 172800 science, 40 Dark Matter | 1 Hull Plating II, 300 Ship Fragment, 40 Reinforced Hull Plate, 12 Power Core, 1 Ancient Control Unit, 8 Dark Matter Plate | /wiki/06-Items/Hull-Plating.md#the-three-platings

Hull Plating I => Hull Plating II => Hull Plating III
```
<!-- item-tree:end -->

## Los tres blindajes {#the-three-platings}

| Objeto | Casco que añade | De dónde sale |
| :--- | ---: | :--- |
| **Hull Plating I** | 5.000 | Tienda, 5.000 Thulium |
| **Hull Plating II** | 10.000 | Ensamblaje, a partir de un Hull Plating I |
| **Hull Plating III** | 15.000 | Ensamblaje, a partir de un Hull Plating II |

El Hull Plating I se compra. **El II y el III son mejoras**: Ensamblaje consume un blindaje del nivel inferior (suelto en tu inventario) y pide Thulium, materiales y **Dark Matter Plates**, 5 para el II y 8 para el III, cuando el último nivel de cualquier otra pieza de equipo pide 3. Cada uno necesita antes su tecnología, en el árbol del Hull Plating de la página [Investigación](/wiki/03-Mechanics/Research.md#tree-hull-plating): 1 día y 25 Dark Matter para el II, 2 días y 40 para el III, además de la tecnología de la propia Dark Matter Plate. El árbol de arriba tiene los precios, los materiales y los tiempos.

La [Forja](/wiki/06-Items/Forge.md) acepta todos los blindajes, y una mejora conserva el grado de forja del blindaje que consumió y vuelve a sortear su bonificación. Un blindaje tiene una sola estadística, su casco, así que lleva una sola bonificación, de +2 % a +15 % según el grado: un Hull Plating III en Eterno suma hasta 17.250. La [Subasta](/wiki/03-Mechanics/Auction.md) lista el Hull Plating II y el III, nunca el Hull Plating I, que vende la tienda.

## Ranuras de blindaje {#hull-plate-slots}

El blindaje de casco solo encaja en las **ranuras de blindaje**, una clase de ranura propia que tienen las cuatro naves que fabricas en Ensamblaje además de sus ranuras de láser, generador, extra, habilidad y dron:

| Nave | Ranuras de blindaje | Un juego completo de Hull Plating III suma |
| :--- | ---: | ---: |
| **Paragon** | 5 | 75.000 |
| **Storm** | 7 | 105.000 |
| **Ironclad** | 15 | 225.000 |
| **Wraith** | 9 | 135.000 |

- **Todas bloqueadas al principio.** Una ranura se abre cuando la investigas en el Skylab: una tecnología por cada ranura, 1 hora y 10 Dark Matter, en orden desde la primera. La vista de [Investigación](/wiki/03-Mechanics/Research.md#ship-technologies) muestra las ranuras de una nave como una sola tarjeta con un punto por ranura.
- **Una clase de nave, no una sola nave.** Las ranuras que abriste para la Paragon están abiertas también en todos los diseños de la Paragon ([Diseños de naves](/wiki/03-Mechanics/Ship-Designs.md)). Una tecnología es tuya para siempre: el reinicio la conserva.
- **Las dos configuraciones las comparten.** Los blindajes pertenecen a la nave: cambiar de configuración los deja puestos, y el hangar muestra los mismos en ambas.
- **Cualquier mezcla.** Una ranura admite cualquier blindaje de casco, y dos iguales no son problema.
- **Tu proporción de casco se mantiene.** Al poner o quitar un blindaje se conserva la proporción de casco que tienes, así que un blindaje nunca te cura ni te hiere.
- **Como todo el equipo**, los blindajes se ponen y se quitan en el hangar, o en su ventana desde una zona segura, nunca en el campo. Una ranura que no has investigado rechaza el blindaje.

En el hangar, la tarjeta **Blindaje de casco** muestra las ranuras. Una abierta admite un blindaje arrastrándolo, como cualquier ranura; una bloqueada muestra un candado y un clic abre la investigación del Skylab. Un icono junto a las demás estadísticas suma lo que dan los blindajes puestos.

## Cómo se suma el casco {#how-the-hull-adds-up}

Un blindaje suma su casco al propio de la nave, y el hangar y la ventana de la nave muestran la cifra mayor. El casco de la nave más sus blindajes pasa luego por los multiplicadores de siempre: un [Hull Plating Booster](/wiki/06-Items/Boosters.md) y la [formación de drones](/wiki/03-Mechanics/Formations.md) que llevas. Un diseño que cambia el casco (el BUCKY tiene un 25 % más) cambia el casco propio de la nave, y los blindajes se suman encima.

## ¿Hull Plating o Hull Plating Booster? {#hull-plating-or-booster}

Dos cosas comparten el nombre. El **blindaje de casco** (esta página) es una armadura: una placa que va en una ranura de blindaje de una nave fabricada y suma su casco mientras esté puesta. El **Hull Plating Booster** es una bonificación temporal de la página [Potenciadores](/wiki/06-Items/Boosters.md), +10 % de puntos de casco máximos durante 10 horas en la nave que pilotes, y no hay nada que equipar. Se suman: primero van los blindajes y el 10 % del Booster se toma sobre el total.
