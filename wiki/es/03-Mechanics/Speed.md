<!-- wiki-i18n source: 431a488ba7a0842e -->
<!-- wiki-i18n title: Velocidad -->
# Cálculo de la velocidad {#speed-calculation}

La velocidad determina lo rápido que se mueve tu nave por el mapa espacial, y te permite perseguir objetivos, escapar del combate o cruzar zonas.

## La fórmula de la velocidad {#the-speed-formula}

La velocidad final de tu nave se calcula en el servidor con la siguiente fórmula:

\[\text{Velocidad final} = (\text{Velocidad base de la nave} + \text{Velocidad total de los motores}) \times (1,0 + \text{Porcentaje total de bono de velocidad})\]

### 1. Velocidad efectiva del motor {#1-effective-engine-speed}

Cada motor equipado genera velocidad. Si hay propulsores instalados en el motor, su velocidad se modifica:

\[\text{Velocidad del motor} = (\text{Velocidad base del motor} \times \text{Multiplicador de propulsores}) + \text{Bono fijo de propulsores}\]

- **Multiplicador de propulsores**: el producto de los multiplicadores de velocidad de todos los propulsores instalados en ese motor (p. ej., Thruster III es `1.1` o `+10%`).
- **Bono fijo de propulsores**: la suma de todos los aumentos fijos de velocidad de los propulsores (p. ej., Thruster III da `+15` de velocidad).

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
