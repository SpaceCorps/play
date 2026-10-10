<!-- wiki-i18n source: 74226336693d1ae9 -->
<!-- wiki-i18n title: Velocidad -->
# Cálculo de la velocidad {#speed-calculation}

La velocidad determina lo rápido que se mueve tu nave por el mapa espacial, y te permite perseguir objetivos, escapar del combate o cruzar zonas.

## La fórmula de la velocidad {#the-speed-formula}

La velocidad final de tu nave se calcula en el servidor con la siguiente fórmula:

\[\text{Velocidad final} = (\text{Velocidad base de la nave} + \text{Velocidad total de los motores}) \times (1,0 + \text{Porcentaje total de bono de velocidad})\]

Un [diseño de nave](/wiki/03-Mechanics/Ship-Designs.md) cambia el primer término (THUNDER tiene 40 de velocidad base más, DUMA 20 menos), y NOTSUM y RECON multiplican la velocidad final por un factor más, +2 % y +5 %.

### 1. Velocidad efectiva del motor {#1-effective-engine-speed}

Cada motor equipado genera velocidad, y también cada núcleo adaptativo que lleva propulsores. Si hay propulsores instalados en el motor, su velocidad se modifica:

\[\text{Velocidad del motor} = (\text{Velocidad base del motor} + \text{Bono fijo de propulsores}) \times \text{Multiplicador de propulsores}\]

- **Bono fijo de propulsores**: la suma de todos los aumentos fijos de velocidad de los propulsores (p. ej., Impulse Thruster III da `+12.75` de velocidad).
- **Multiplicador de propulsores**: el producto de los multiplicadores de velocidad de todos los propulsores instalados en ese motor (p. ej., Momentum Thruster III es `1.0765` o `+7.65%`; Impulse Thruster III, `1.0255` o `+2.55%`). Multiplica todo lo que produce el motor: su propia velocidad base y los bonos fijos de los propulsores. Un núcleo adaptativo no tiene velocidad base propia, y los bonos fijos de sus propulsores se multiplican igualmente.

Un Engine III (velocidad base 6) con tres Momentum Thruster IV (`+11.135`, `1.0935`) produce (6 + 3 x 11,135) x 1,0935 x 1,0935 x 1,0935 = 51,5, y con tres Impulse Thruster IV (`+14.025`, `1.02975`) (6 + 3 x 14,025) x 1,02975 x 1,02975 x 1,02975 = 52,5. Una bonificación de la Forja en el multiplicador de un propulsor hace crecer la parte por encima de 1: +15 % sobre `1.0935` da `1.1075`.

### 2. Rendimientos decrecientes (eficiencia marginal) {#2-diminishing-returns-marginal-efficiency-}

Para evitar que los jugadores acumulen motores sin fin y consigan una velocidad infinita, se aplica una curva de **rendimientos decrecientes (eficiencia marginal)**. Todos los motores se ordenan por su aportación de velocidad y se procesan en ese orden. Los núcleos adaptativos (híbridos) y los núcleos de escudo se clasifican igual, cada tipo en su propio grupo, así que una nave con motores y núcleos adaptativos tiene unos primeros cuatro de cada tipo:

| Puesto del motor | Multiplicador de eficiencia |
| :---: | :--- |
| **1.º a 4.º** | **100 %** (1,0) |
| **5.º** | **85 %** (0,85) |
| **6.º** | **70 %** (0,70) |
| **7.º** | **55 %** (0,55) |
| **8.º y siguientes** | **25 %** (0,25) |

Además, la velocidad del motor se multiplica por la eficiencia de su ranura (principal: 100 %, apoyo: 75 %, auxiliar: 50 %).

### 3. Porcentaje de bono de velocidad y penalizaciones de los escudos {#3-speed-bonus-percent-shield-penalties}

El porcentaje total de bono de velocidad es la suma de todos los bonos de velocidad de los motores equipados (y de los híbridos) menos las penalizaciones de los escudos equipados:

- **Bono de velocidad de los motores**: los motores suman porcentajes de velocidad positivos (p. ej., Engine III suma `+5%`).
- **Penalización de velocidad de los escudos**: los escudos pesados lastran tu nave y suman porcentajes de velocidad negativos (p. ej., Heavy Shield Core suma `-5%` de velocidad).
- **Escalado por ranura**: estos bonos y penalizaciones porcentuales también se escalan según la eficiencia de la ranura donde está equipado el objeto. Un escudo en uno de tus drones te ralentiza igual que uno en una ranura principal.
- **Nunca por debajo de cero**: por muchos escudos que lleves, tu velocidad no baja de 0.
- **Formaciones de drones**: una [formación de drones](/wiki/03-Mechanics/Formations.md) puesta cambia la velocidad final una vez más, como un factor propio: Gyre +10 %, Cordon −3 %, Auger −9 %, Culler −10 %, Redoubt −11 %, Rampart −17 %. Después el Afterburner multiplica el resultado.
