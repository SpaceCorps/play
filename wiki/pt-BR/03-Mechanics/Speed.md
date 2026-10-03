<!-- wiki-i18n source: 897dab3210b8f84a -->
<!-- wiki-i18n title: Velocidade -->
# Cálculo da velocidade {#speed-calculation}

A velocidade determina a rapidez com que a sua nave se move no mapa espacial, permitindo que você persiga alvos, escape de combates ou atravesse zonas.

## A fórmula da velocidade {#the-speed-formula}

A velocidade final da sua nave é calculada no servidor com a seguinte fórmula:

\[\text{Velocidade final} = (\text{Velocidade base da nave} + \text{Velocidade total dos motores}) \times (1,0 + \text{Percentual total de bônus de velocidade})\]

### 1. Velocidade efetiva do motor {#1-effective-engine-speed}

Cada motor equipado gera velocidade, e o mesmo vale para cada núcleo adaptativo que tem propulsores. Se houver propulsores encaixados no motor, a velocidade dele é modificada:

\[\text{Velocidade do motor} = (\text{Velocidade base do motor} + \text{Bônus fixo dos propulsores}) \times \text{Multiplicador dos propulsores}\]

- **Bônus fixo dos propulsores**: a soma de todos os acréscimos fixos de velocidade dos propulsores (por exemplo, o Impulse Thruster III é `+15` de velocidade).
- **Multiplicador dos propulsores**: o produto de todos os multiplicadores de velocidade dos propulsores encaixados naquele motor (por exemplo, o Momentum Thruster III é `1.13` ou `+13%`, o Impulse Thruster III, `1.03` ou `+3%`). Ele multiplica tudo o que o motor produz: a velocidade base dele e os bônus fixos dos propulsores. Um núcleo adaptativo não tem velocidade base própria, e os bônus fixos dos propulsores dele são multiplicados do mesmo jeito.

Um Engine III (velocidade base 6) com três Momentum Thruster IV (`+12`, `1.14`) produz (6 + 3 x 12) x 1,14 x 1,14 x 1,14 = 62,2, e com três Impulse Thruster IV (`+17`, `1.02`), (6 + 3 x 17) x 1,02 x 1,02 x 1,02 = 60,5. Um bônus da Forja no multiplicador de um propulsor faz crescer a parte acima de 1: +15% sobre `1.14` dá `1.161`.

### 2. Retornos decrescentes (eficiência marginal) {#2-diminishing-returns-marginal-efficiency-}

Para impedir que os jogadores empilhem motores sem fim em troca de velocidade sem fim, aplica-se uma curva de **retornos decrescentes (eficiência marginal)**. Todos os motores são ordenados pela contribuição de velocidade e processados nessa ordem. Os núcleos adaptativos (híbridos) e os núcleos de escudo são classificados do mesmo jeito, cada tipo em um grupo próprio, de modo que uma nave com motores e núcleos adaptativos tem os quatro primeiros de cada tipo:

| Posição do motor | Multiplicador de eficiência |
| :---: | :--- |
| **1º ao 4º** | **100%** (1,0) |
| **5º** | **85%** (0,85) |
| **6º** | **70%** (0,70) |
| **7º** | **55%** (0,55) |
| **8º em diante** | **25%** (0,25) |

Além disso, a velocidade do motor é multiplicada pela eficiência do slot (núcleo: 100%, suporte: 75%, auxiliar: 50%).

### 3. Percentual de bônus de velocidade e penalidades dos escudos {#3-speed-bonus-percent-shield-penalties}

O percentual total de bônus de velocidade é a soma de todos os bônus de velocidade dos motores (e híbridos) equipados, menos as penalidades dos escudos equipados:

- **Bônus de velocidade dos motores**: os motores somam percentuais de velocidade positivos (por exemplo, o Engine III soma `+5%`).
- **Penalidade de velocidade dos escudos**: escudos pesados sobrecarregam a nave e somam percentuais de velocidade negativos (por exemplo, o Heavy Shield Core soma `-5%` de velocidade).
- **Escala por slot**: esses bônus e penalidades percentuais também são escalados pela eficiência do slot em que o item está equipado. Um escudo em um dos seus drones deixa você mais lento, assim como um escudo em um slot de núcleo.
- **Nunca abaixo de zero**: por mais escudos que você carregue, a sua velocidade não cai abaixo de 0.
