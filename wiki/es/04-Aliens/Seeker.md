<!-- wiki-i18n source: d1f973df95aefca8 -->
<!-- wiki-i18n title: Seeker -->
# Seeker {#seeker}

Los Seekers son unidades básicas de exploración y reconocimiento. Son pasivos, es decir, nunca empiezan un combate: un Seeker se vuelve contra el piloto que le dispara, y solo contra ese piloto. Lo deja ir si nadie lo ha alcanzado en 10 segundos, y su casco se repara cuando lo han dejado en paz durante 30 segundos. El Boss Seeker y los Seeker Slaves del [Enjambre Seeker](/wiki/05-Swarms/Seeker-Swarm.md) se parecen a los Seekers, pero son tipos propios: sus derribos se cuentan con su propio nombre, no como derribos de Seeker.

## Estadísticas {#stats}

- **Puntos de vida (HP)**: 800
- **Escudo**: 800
- **Daño**: 180
- **Velocidad**: 120
- **Alcance de ataque**: 600
- **Comportamiento**: Pasivo

## Comportamiento {#behavior}

- Un Seeker nunca persigue a una nave que se acerca: deambula hasta que alguien le dispara, y entonces persigue y dispara al primer piloto que le disparó, mientras ese piloto siga alcanzándolo y el Seeker pueda llegar hasta él; los disparos de otros pilotos no lo desvían entretanto, y cuando el primero queda fuera de combate, pasa al siguiente piloto que se sumó al combate (consulta [Contra quién lucha un alienígena](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)). El fuego de otro alienígena y un impacto que no causa daño nunca lo provocan.
- Abandona la persecución **10 segundos** después de que alguien lo haya alcanzado por última vez, y vuelve a deambular. Mientras un piloto siga alcanzándolo, vuela hacia ese piloto siempre que esté fuera del alcance de sus armas (600 unidades) y dispara en cuanto lo tiene a tiro.
- Deja ir a un piloto cuando está a más de **2500 unidades** de él, o cuando ha recorrido **3000 unidades** desde donde empezó la persecución, y no vuelve a ir a por ese piloto durante 8 segundos, a menos que el piloto le dispare de nuevo (consulta [Combate](/wiki/03-Mechanics/Combat.md)).
- Si lo dejan en paz **30 segundos**, su casco se repara: un 2 % de su máximo por segundo (el casco completo en unos 50 segundos). Su escudo se recarga como el de cualquier alienígena, a partir de los 15 segundos del último impacto.
- No combate contra nadie que no lo haya alcanzado, y nunca llama a otro alienígena en su ayuda.
- Los [pilotos de corporación](/wiki/03-Mechanics/Company-Pilots.md) cazan Seekers. Un piloto que dispara a uno atrae su fuego, salvo que ya esté combatiendo contra otro.

## Recompensas {#rewards}

- **Créditos**: 800
- **Thulium**: 4
- **Experiencia (XP)**: 100
- **Honor**: 2
- **Puntos PvE por derribo**: 1
- **Recarga de escudo**: 10 por segundo (15 s de retraso)

## Botín {#loot-drops}

Cae en una [caja de carga](/wiki/03-Mechanics/Cargo.md) en el lugar donde explota, reservada durante 30 segundos para quien lo destruyó.

Para qué sirve cada botín y dónde más se encuentra: [Recursos](/wiki/06-Items/Resources.md).

- **Ship Fragment**: 20 % de probabilidad (mín.: 1, máx.: 1)
- **Daraxium**: 50 % de probabilidad (mín.: 1, máx.: 2)

## Historia {#lore}

Los Seekers son sondas ligeras de exploración que el Enjambre alienígena despliega para cartografiar los portales de salto de los sectores y rastrear las firmas electromagnéticas de las flotas humanas. Con un armamento mínimo y estructuras frágiles, son muy pasivos: se retiran o ignoran a las naves a menos que les disparen. Sin embargo, se coordinan con unidades de combate mayores y, si se les ataca, señalan sus posiciones.
