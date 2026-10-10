<!-- wiki-i18n source: 1433a0058afe39fa -->
<!-- wiki-i18n title: Propulsión -->
# Propulsión y velocidad {#propulsion-speed}

Los sistemas de propulsión determinan la velocidad de movimiento y la maniobrabilidad de tu nave.

## En un minuto {#in-one-minute}

- **Los motores producen velocidad, los propulsores van dentro de ellos y la aumentan.** Un motor admite de uno a tres propulsores (un Engine I uno, un Engine II dos, un Engine III tres), y un núcleo adaptativo también (su nivel indica cuántos).
- **Dos familias de cuatro niveles cada una.** Los Impulse Thruster aportan la mayor velocidad fija. Los Momentum Thruster aportan menos velocidad fija y multiplican más la velocidad. En las dos familias cada nivel es mejor que el de abajo, en ambas cifras.
- **Cuál va dónde.** Como regla, pon Impulse Thrusters en todas partes: solo en un Engine III lleno (tres propulsores) van por delante los Momentum Thrusters de los niveles I y II. [La tabla de más abajo](#which-thruster-where) tiene las cifras. El Engine III más rápido lleva tres Impulse Thruster IV y da 52,5.
- **Cómo conseguirlos.** El nivel I de cada familia cuesta 20.000 créditos. Los niveles II a IV se fabrican en Ensamblaje, cada uno a partir del anterior, y un propulsor nunca cambia de familia.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Árbol de objetos {#item-tree}

Lo que fabrica Ensamblaje necesita antes su tecnología; pasa el cursor por un objeto para ver cuánto tarda en investigarse. El árbol de tecnologías, el combustible y el impulso: [Investigación](/wiki/03-Mechanics/Research.md).

```tree
Engine I | engine, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#engines
Engine II | engine, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Engine I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#engines
Engine III | engine, rare | craft 2000 Thulium, 90 s | research 10800 s, 10800 science | 1 Engine II, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#engines
Impulse Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster I | thruster, shoddy | buy 20000 Credits | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Impulse Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster II | thruster, common | craft 1000 Thulium, 60 s | research 1800 s, 1800 science | 1 Momentum Thruster I, 10 Ship Fragment, 1 Power Core, 2 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Impulse Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster III | thruster, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 1 Momentum Thruster II, 30 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Propulsion.md#thrusters
Impulse Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Impulse Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters
Momentum Thruster IV | thruster, epic | craft 2000 Thulium, 90 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Momentum Thruster III, 60 Ship Fragment, 3 Power Core, 3 Dark Matter Plate | /wiki/06-Items/Propulsion.md#thrusters

Engine I => Engine II => Engine III
Impulse Thruster I => Impulse Thruster II => Impulse Thruster III => Impulse Thruster IV
Momentum Thruster I => Momentum Thruster II => Momentum Thruster III => Momentum Thruster IV
```
<!-- item-tree:end -->

## Motores {#engines}

Los motores son la fuente principal de empuje de tu nave. Un motor en una **ranura de habilidad** te da en cambio el **Afterburner** de la columna Efecto especial, una ráfaga de velocidad durante diez segundos (más con más motores), y no aporta empuje propio (consulta [Habilidades](/wiki/03-Mechanics/Abilities.md)).

| Nombre | Rareza | Velocidad base | Bono de velocidad % | Bono de escudo % | Ranuras | Efecto especial | Costo |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Engine I** | Deficiente | +2 | +2 % | -2 % | 1 | Afterburner I | 20.000 créditos |
| **Engine II** | Común | +4 | +4 % | -8 % | 2 | Afterburner II | Solo fabricable |
| **Engine III** | Raro | +6 | +5 % | -15 % | 3 | Afterburner III | Solo fabricable |

El **Engine II** se fabrica en [Ensamblaje](/wiki/06-Items/Overview.md#upgrading-modules) a partir de un Engine I, con 1.000 Thulium, 10 Ship Fragments, 1 Power Core y 2 Velkonite Reinforced Plates. El **Engine III** se fabrica allí a partir de un Engine II, con 2.000 Thulium, 60 Ship Fragments, 3 Power Cores y 3 Dark Matter Plates ([Dark Matter y Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)). Cada uno conserva el grado de encantamiento del motor que consume, y sus bonificaciones se sortean de nuevo ([Mejoras de módulos](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Quita primero de tu nave el motor que vas a consumir (y saca de él sus propulsores): un motor que está instalado o que lleva propulsores no se consume.

El bono de escudo de los motores figura en los datos del objeto, pero el juego nunca lo ha aplicado: los motores no debilitan tus escudos, y las tarjetas de los objetos lo omiten.

---

## Propulsores {#thrusters}

Los propulsores se instalan dentro de motores o de núcleos adaptativos para aumentar su aporte de velocidad. Hay dos familias de cuatro niveles cada una: los **Impulse Thruster** aportan más velocidad fija y multiplican un poco la velocidad del motor en el que van, los **Momentum Thruster** menos velocidad fija, pero la multiplican más. En las dos familias cada nivel es mejor que el de abajo, tanto en velocidad fija como en multiplicador. Un motor (o núcleo adaptativo) con propulsores produce **su propia velocidad base más los aumentos fijos de velocidad de los propulsores, todo ello multiplicado por los multiplicadores de velocidad de los propulsores, multiplicados entre sí** ([cómo se calcula la velocidad](/wiki/03-Mechanics/Speed.md)): un Engine III con tres Momentum Thruster IV produce (6 + 3 x 11,135) x 1,0935 x 1,0935 x 1,0935 = 51,5, con tres Impulse Thruster IV (6 + 3 x 14,025) x 1,02975 x 1,02975 x 1,02975 = 52,5, y un Adaptive Core II con dos Impulse Thruster IV produce (0 + 2 x 14,025) x 1,02975 x 1,02975 = 29,7 (26,6 con dos Momentum Thruster IV).

| Nombre | Rareza | Aumento fijo de velocidad | Multiplicador de velocidad | Costo |
| :--- | :--- | :---: | :---: | :--- |
| **Impulse Thruster I** | Deficiente | +4,25 | x1,017 | 20.000 créditos |
| **Impulse Thruster II** | Común | +8,5 | x1,02125 | Solo fabricable |
| **Impulse Thruster III** | Raro | +12,75 | x1,0255 | Solo fabricable |
| **Impulse Thruster IV** | Épico | +14,025 | x1,02975 | Solo fabricable |
| **Momentum Thruster I** | Deficiente | +3,825 | x1,051 | 20.000 créditos |
| **Momentum Thruster II** | Común | +7,65 | x1,0595 | Solo fabricable |
| **Momentum Thruster III** | Raro | +10,625 | x1,0765 | Solo fabricable |
| **Momentum Thruster IV** | Épico | +11,135 | x1,0935 | Solo fabricable |

### Qué propulsor va dónde {#which-thruster-where}

El Impulse aporta más velocidad fija y el Momentum multiplica más, así que cuál es más rápido depende de lo que el motor ya produce. La velocidad fija cuenta más donde hay poca velocidad que multiplicar: en un núcleo adaptativo (no tiene velocidad propia) y en un motor con uno o dos propulsores. Un multiplicador cuenta más en un Engine III lleno, donde hay mucha velocidad que multiplicar, pero allí solo ganan los Momentum Thrusters de los niveles I y II. La velocidad que produce cada uno con propulsores de nivel IV en todas las ranuras:

| Dónde van los propulsores | Con Impulse Thruster IV | Con Momentum Thruster IV | Más rápido |
| :--- | :---: | :---: | :--- |
| Engine I, 1 propulsor | 16,5 | 14,4 | Impulse |
| Engine II, 2 propulsores | 34,0 | 31,4 | Impulse |
| Engine III, 1 propulsor | 20,6 | 18,7 | Impulse |
| Engine III, 2 propulsores | 36,1 | 33,8 | Impulse |
| Engine III, 3 propulsores | 52,5 | 51,5 | Impulse |
| Adaptive Core II, 2 propulsores | 29,7 | 26,6 | Impulse |

- **Niveles inferiores.** Los niveles inferiores van igual, con dos casos ajustados y una excepción: con dos propulsores en un Engine II las familias quedan igualadas en los niveles I y II (el Impulse va por delante por 0,06 y 0,24), y con dos en un Engine III también (a menos de 0,1). Desde el nivel III el Impulse gana en ambos, por 1,5 a 2,6. La excepción es el Engine III lleno: allí el Momentum gana en los niveles I y II, por 0,6 y 0,9, y el Impulse en los niveles III y IV, por 0,5 y 1,0.
- **El Engine III más rápido.** Lleva tres Impulse Thruster IV: 52,5, algo por encima de un Impulse y dos Momentum Thruster IV (52,1) o de tres Momentum (51,5).

La bonificación de multiplicador de velocidad de un propulsor, de la [Forja](/wiki/06-Items/Forge.md), hace crecer la parte por encima de 1 (una bonificación de +15 % sobre x1,0935 da x1,1075), y la Forja no sortea ninguna bonificación sobre un multiplicador de x1,05 o menos: en el x1,017 a x1,02975 de un Impulse Thruster añadiría menos de 0,005 (+15 % sobre x1,02975 da x1,034). Un Impulse Thruster lleva una bonificación (su velocidad fija), un Momentum Thruster dos.

El nivel I de cada familia se vende por 20.000 créditos. Los niveles II a IV se fabrican en [Ensamblaje](/wiki/06-Items/Overview.md#upgrading-modules), cada uno a partir del propulsor de la misma familia un nivel por debajo (un Impulse Thruster II a partir de un Impulse Thruster I, uno III a partir de uno II, uno IV a partir de uno III), con Thulium, botín y placas: 2 o 4 Velkonite Reinforced Plates de tu Skylab para el nivel II o III, y 3 Dark Matter Plates para el nivel IV. Un propulsor nunca cambia de familia: eliges Impulse o Momentum al comprar el nivel I. Cada uno conserva el grado de encantamiento del propulsor que consume, y sus bonificaciones se sortean de nuevo ([Mejoras de módulos](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)). Los propulsores no caben en una [ranura de habilidad](/wiki/03-Mechanics/Abilities.md); van dentro de motores y núcleos adaptativos.

### Cómo dejar atrás a los alienígenas {#outrunning-aliens}

Los alienígenas vuelan a 120 (Seeker), 160 (Phantasm), 175 (Bulwark), 180 (Goombah) y 230 (Crystalys). Una Ostirion con un Engine II y dos propulsores vuela a 221,4 con Impulse Thruster I: todavía por debajo del Crystalys, así que hace falta un propulsor fabricado en Ensamblaje para dejarlo atrás (230,8 con Impulse Thruster II, 240,3 con III, 243,3 con IV). Los Momentum Thruster vuelan igual o algo más bajo en esa nave (221,4 con un Momentum Thruster I; después 230,5, 238,4 y 240,7 con II a IV): el nivel I de las dos familias queda por debajo de un Crystalys, y todo nivel fabricado en Ensamblaje, por encima, el nivel II por solo 0,8 y 0,5.
