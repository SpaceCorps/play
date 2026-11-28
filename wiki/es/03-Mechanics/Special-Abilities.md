<!-- wiki-i18n source: 0a2447734a603004 -->
<!-- wiki-i18n title: Habilidades especiales -->
# Habilidades especiales {#special-abilities}

<!-- wiki-search: special ability; special abilities; ability; abilities; mob; mobs; regenerate; mending; shield burst; hardened plating; plating; enrage; call reinforcements; reinforcements; clones; decoy; flee and return; flee; life drain; nova pulse; nova; rocket barrage; barrage; veil; sow mines; mines; split; fragments; boss steps; ladder; three steps; warning; tell; surprise; warlord; warden; leader; habilidades especiales; regeneración; ráfaga de escudo; blindaje reforzado; furia; pedir refuerzos; clones; huir y volver; drenaje de vida; pulso nova; andanada de cohetes; velo; sembrar minas -->

Algunos alienígenas llevan una **habilidad especial**: algo que hacen una sola vez en su vida, cuando han perdido la mitad del casco. Regenerarse, una ráfaga de escudo, una huida, una petición de ayuda. Nada se nota antes de que empiece, así que cada caza puede acabar en sorpresa. Esta página dice qué hace cada habilidad y cómo responder a ella. Los jefes funcionan de otro modo: cambian su forma de combatir en tres pasos a medida que cae su casco, y los alienígenas pequeños del último nivel pueden partirse en fragmentos si se los destruye demasiado rápido.

## Cómo funciona {#how-it-works}

<!-- mob-rules:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **Una vez.** Un alienígena que lleva una habilidad la usa una sola vez en su vida: cuando, en un combate, su casco (no su escudo) cae por debajo de 50 % de su máximo. Un golpe que lo destruye desde por encima de esa línea nunca le deja disparar, y un alienígena que no está en combate espera a que empiece uno.
- **Primero un aviso.** La habilidad empieza con un aviso: un anillo que se cierra sobre la nave y una palabra encima. Una habilidad cuyo apartado de abajo dice que empieza de inmediato no tiene aviso. El alienígena aún puede ser destruido durante el aviso; entonces no pasa nada y paga como siempre. Las clases ligeras (Seeker y Phantasm) son más rápidas: sus avisos y sus efectos duran 50 % de lo normal.
- **Nada se nota antes.** Un alienígena que lleva una habilidad es igual que cualquier otro, en cada detalle, hasta que empieza su aviso. Nada en el juego dice cuál es, ni siquiera la [Guía del Viajero](/wiki/03-Mechanics/Travelers-Guide.md).
- **Quién la lleva.** Una pequeña parte de los alienígenas de los sectores de las compañías y de los Danger Sectors: cuanto más fuerte el nivel, mayor la parte, y los líderes de los enjambres (Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah y Boss Crystalys) tienen más probabilidad de llevarla que el resto. Los alienígenas de la Deep Void, de las mazmorras de clan y de las puertas en solitario nunca la llevan, ni los seguidores de un enjambre, las oleadas de un Guardián, la Dormant Force o el Tesseract.
- **Paga lo que paga cualquier alienígena.** Un alienígena que usa una habilidad paga, suelta botín y cuenta exactamente igual que uno que no la usa: la habilidad no añade nada al derribo y le quita tiempo. El derribo sigue siendo del piloto que lo tenía: mientras el alienígena huye, se regenera o se oculta, la reclamación no caduca.
- **Las naves llamadas y las copias no son derribos.** Las naves que llama un alienígena y las copias que hace no pagan nada, no sueltan nada y no cuentan para ninguna misión, estadística ni clasificación. Viven como máximo 6 por quien llama y 24 en un mapa, y los alienígenas propios del mapa siguen volviendo a tiempo.
- **Todos en el mapa lo ven.** Los pilotos del mapa saben cuándo empieza una habilidad: el juego dibuja el anillo, la palabra y el efecto, y reproduce un sonido.

<!-- mob-rules:end -->

## Las doce habilidades {#the-twelve-abilities}

Una habilidad empieza con un **aviso**, salvo que su apartado diga que empieza de inmediato: un anillo que se cierra sobre la nave y una palabra encima. Los tiempos y las cifras de abajo son los de las clases pesadas. Donde una cifra tiene varios valores, son los de los niveles que se nombran entre paréntesis, la letra griega que va delante del nombre de un alienígena.

<!-- mob-abilities:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

### Regeneración {#regenerate}

Se queda quieto y restaura 15 % / 20 % / 25 % / 30 % (α / β / γ / δ) de su casco y su escudo en 6 s, y no dispara mientras tanto. El daño que suma 10 % de su casco y su escudo juntos la interrumpe, y conserva lo que ya ha restaurado.

- **Aviso**: 1,5 s
- **La palabra sobre la nave**: REGENERANDO
- **La llevan**: cualquier alienígena
- **Respuesta**: Revienta su regeneración con cohetes o con una multitud de naves, o destrúyelo durante el aviso.

### Ráfaga de escudo {#shield-burst}

Una capa de escudo nueva de 15 % / 20 % / 30 % / 40 % (α / β / γ / δ) de su casco máximo se añade a su escudo. Mientras dura, absorbe cada punto de un impacto; desaparece cuando se agota o tras 10 s.

- **Aviso**: 1 s
- **La palabra sobre la nave**: ESCUDO ARRIBA
- **La llevan**: cualquier alienígena
- **Respuesta**: La munición y los cohetes que perforan escudos la atraviesan mejor. O dispara a otro alienígena hasta que desaparezca.

### Blindaje reforzado {#hardened-plating}

Durante 7 s / 8 s / 10 s (β / γ / δ) recibe solo 50 % de cada impacto, casco y escudo por igual: el doble de resistente. Sigue luchando, y los números de tus impactos se vuelven grises.

- **Aviso**: 1,5 s
- **La palabra sobre la nave**: BLINDÁNDOSE
- **La llevan**: las clases pesadas (Bulwark, Goombah y Crystalys) y los líderes de enjambre pesados (Pirate Boss y Boss Phantasm), desde β
- **Respuesta**: Espera a que acabe, golpea a otro alienígena entretanto y guarda tus ráfagas para después.

### Furia {#enrage}

Durante 10 s su daño se multiplica por ×1,3 / ×1,4 / ×1,5 / ×1,75 (α / β / γ / δ) y su velocidad por ×1,25.

- **Aviso**: 1 s
- **La palabra sobre la nave**: FURIOSO
- **La llevan**: cualquier alienígena
- **Respuesta**: Mantén el escudo arriba, sigue moviéndote y quédate fuera de su alcance.

### Pedir refuerzos {#call-reinforcements}

4 / 6 (γ / δ) alienígenas más pequeños entran desde el borde más cercano del mapa, en 2 oleadas separadas 3 s. La clase que llega: Phantasm (llamado por Bulwark y Goombah); Bulwark (llamado por Crystalys). Juntos tienen 45 % / 60 % (γ / δ) de su casco y su escudo y disparan 50 % de su andanada. No pagan nada, no sueltan nada y no cuentan para nada, y se van tras 45 s o cuando destruyen a quien los llamó.

- **Aviso**: 2 s
- **La palabra sobre la nave**: PIDE AYUDA
- **La llevan**: las clases pesadas (Bulwark, Goombah y Crystalys) y los líderes de enjambre pesados (Boss Phantasm y Boss Goombah), desde γ
- **Respuesta**: Destruye a quien llama: sus naves se van con él. Un arma de área las despeja.

### Clones

3 (γ / δ) copias suyas aparecen a su alrededor, con su nombre y su aspecto. Entre todas tienen 18 % (γ / δ) de su casco y su escudo; no disparan ni pagan nada, y duran 15 s o hasta que destruyen al auténtico. El auténtico lleva un anillo fino mientras las copias siguen ahí, y la ventana de objetivo llama a una copia Señuelo.

- **Aviso**: 1 s
- **La palabra sobre la nave**: CLONANDO
- **La llevan**: cualquier alienígena, desde γ
- **Respuesta**: Sigue el anillo y la barra de casco que se mueve del auténtico, o usa un arma de área.

### Huir y volver {#flee-and-return}

Huye de sus atacantes a velocidad ×2 durante 5 s / 6 s / 7 s / 8 s (α / β / γ / δ) y luego se vuelve contra el primer piloto que lo golpeó. Nunca sale del mapa ni entra en una zona segura, puede ser golpeado todo el tiempo, y el piloto que tenía su derribo lo conserva.

- **Aviso**: 0,5 s
- **La palabra sobre la nave**: HUYENDO
- **La llevan**: cualquier alienígena
- **Respuesta**: Persíguelo, o golpéalo con cohetes mientras vuela.

### Drenaje de vida {#life-drain}

Durante 10 s no dispara otra cosa: una vez por segundo drena a cada nave a su alcance con una andanada completa que nada esquiva, y cura 75 % / 100 % / 100 % (β / γ / δ) del daño que hace, como máximo 20 % de su casco en total.

- **Aviso**: 1 s
- **La palabra sobre la nave**: DRENANDO
- **La llevan**: las clases pesadas (Bulwark, Goombah y Crystalys) y los líderes de enjambre pesados (Pirate Boss, Boss Phantasm, Boss Goombah y Boss Crystalys), desde β
- **Respuesta**: Pon una roca o un muro en la línea, actívate el camuflaje o sal de su alcance.

### Pulso nova {#nova-pulse}

Un anillo crece en el suelo a su alrededor durante el aviso. Cuando el anillo está lleno, golpea una vez a cada nave que hay dentro, con 4 / 5 (γ / δ) de sus andanadas. Su radio, en unidades, es 700 / 800 (γ / δ).

- **Aviso**: 2,5 s
- **La palabra sobre la nave**: NOVA
- **La llevan**: las clases pesadas (Bulwark, Goombah y Crystalys) y los líderes de enjambre pesados (Pirate Boss, Boss Phantasm y Boss Goombah), desde γ
- **Respuesta**: Sal del anillo antes de que se llene: es la única ráfaga que puedes esquivar.

### Andanada de cohetes {#rocket-barrage}

Durante 3 s dispara 4 / 6 / 8 (β / γ / δ) [cohetes Rivet](/wiki/06-Items/Rockets.md#the-twelve-rockets) a su objetivo: Rivet I / II / II (β / γ / δ). Vuelan rectos y no son guiados.

- **Aviso**: 1,5 s
- **La palabra sobre la nave**: ANDANADA
- **La llevan**: las clases pesadas (Bulwark, Goombah y Crystalys) y los líderes de enjambre pesados (Boss Phantasm y Boss Goombah), desde β
- **Respuesta**: Sigue moviéndote: los cohetes van rectos. Una roca en medio los detiene.

### Velo {#veil}

Durante 6 s / 8 s (γ / δ), una nave a más de 700 unidades de él no puede fijarlo, y pierde una fijación que tuviera. Más cerca, se le ve como siempre. Sigue luchando, y una explosión aún lo daña.

- **Aviso**: ninguno, empieza de inmediato.
- **La palabra sobre la nave**: OCULTÁNDOSE
- **La llevan**: las clases pesadas (Bulwark, Goombah y Crystalys) y los líderes de enjambre pesados (Pirate Boss, Boss Phantasm, Boss Goombah y Boss Crystalys), desde γ
- **Respuesta**: Acércate a menos de 700 unidades.

### Sembrar minas {#sow-mines}

Coloca 4 / 6 / 8 (β / γ / δ) minas en un anillo de 500 unidades alrededor del lugar donde estaba su objetivo. Una mina se arma 3 s después de caer, dura 30 s y estalla una vez, bajo la primera nave de piloto que pase por encima, con 2 / 3 / 3 (β / γ / δ) de las andanadas del alienígena. Una mina nunca daña a un alienígena.

- **Aviso**: 1,5 s
- **La palabra sobre la nave**: SIEMBRA MINAS
- **La llevan**: las clases pesadas (Bulwark, Goombah y Crystalys) y los líderes de enjambre pesados (Pirate Boss, Boss Phantasm, Boss Goombah y Boss Crystalys), desde β
- **Respuesta**: Rodéalas: están dibujadas en el suelo y tardan en armarse.


<!-- mob-abilities:end -->

## División {#splitting}

<!-- mob-split:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Los alienígenas pequeños del último nivel pueden partirse si se los destruye demasiado rápido. Es propio de Seeker, Phantasm, Bulwark, Goombah y Crystalys del nivel δ y de ningún otro alienígena, y no es una de las habilidades de arriba: un alienígena puede tener las dos.

- **Cuándo**: un piloto lo destruye en 5 s desde el primer daño que recibió. No todo alienígena que muere tan rápido se parte.
- **Lo que sale**: 3 alienígenas de la misma clase y nivel, de 70 % de su tamaño, cada uno con 25 % de su casco y su escudo y una andanada completa, alrededor del lugar donde fue destruido. Van a por el piloto que lo destruyó y se van tras 180 s.
- **Son alienígenas corrientes**: cada uno paga lo que paga su clase, suelta lo que ella suelta y cuenta para misiones y estadísticas. No llevan ninguna habilidad y nunca se parten.
- **Límites**: como máximo 60 fragmentos viven en un mapa, y no retrasan a los alienígenas propios del mapa.
- **Qué significa**: una tripulación que destruye a sus alienígenas lo bastante rápido puede sacar hasta 4 derribos de un solo alienígena. Una que no lo hace no saca nada de ello.

<!-- mob-split:end -->

## Los tres pasos de los jefes {#the-bosses-three-steps}

Cada jefe cambia su forma de combatir en tres pasos: cuando empieza el combate, cuando su casco baja de dos tercios y cuando baja de un tercio. Un paso ocurre una vez y nunca se deshace, salvo que el jefe vuelva a empezar, como se dice abajo.

<!-- mob-ladders:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **Una pausa en cada paso.** Cuando empieza, después del primero, un paso que tiene algo que hacer, el jefe no puede ser dañado durante 1,5 s (3 s para el Señor de la guerra de la mazmorra y los jefes de las puertas en solitario).
- **También una habilidad especial.** Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah y Boss Crystalys también pueden llevar una habilidad especial (Dormant Force y Tesseract nunca): llega entre el segundo y el tercer paso; si los dos fueran a empezar a la vez, el que viene después espera 3 s como máximo. Nunca es una habilidad que usen los propios pasos del líder.
- **Volver a empezar.** El Tesseract vuelve a empezar sus pasos cuando se ha reparado por completo.

### Los líderes de enjambre {#the-swarm-leaders}

| Líder | Al empezar | Por debajo de dos tercios | Por debajo de un tercio |
| :--- | :--- | :--- | :--- |
| **Pirate Boss** | Dispara un abanico de 3 cohetes, separados 12 grados, al primer piloto que lo golpeó. | Llama a 5 Pirate Scouts más de golpe, como máximo 10 vivos. No pagan nada y se van tras 45 s. | Vuela a velocidad ×1,8 hacia la puerta más cercana durante 10 s y luego se vuelve contra los pilotos. |
| **Boss Seeker** | Sus Seeker Slaves lo reparan ×2 más rápido durante 8 s. | 2 copias suyas aparecen, y la auténtica lleva un anillo. | Huye de los pilotos durante 4 s y luego se vuelve contra ellos. |
| **Boss Phantasm** | Cada uno de sus Phantasm Guards levanta una capa de escudo de 10 % de su propio casco. | 3 copias suyas aparecen, y la auténtica lleva un anillo. | Salta unas 2.500 unidades lejos de los pilotos, y sus Phantasm Guards vuelven enteros a su alrededor. |
| **Boss Goombah** | Recibe 50 % de cada impacto durante 6 s. | Su daño se multiplica por ×1,5 y su velocidad por ×1,25 durante 10 s. | Repara 25 % de su casco y su escudo (una ráfaga de daño la interrumpe), y sus Goombah Guards lo reparan ×2 más rápido entretanto. |
| **Boss Crystalys** | Recibe 50 % de cada impacto durante 8 s. | Un anillo de 700 unidades golpea a cada nave que hay dentro con 4 de sus andanadas, y dispara 4 cohetes. | Repara 20 % de su casco y su escudo (una ráfaga de daño la interrumpe), y llegan 3 Crystalys Guards más, como máximo 6 vivos. |
| **Dormant Force** | Recibe 70 % de cada impacto mientras viva uno de sus Dormant Pulses. | Sus Dormant Pulses disparan un cohete cada 2,5 s durante 15 s. | Mientras vivan todos sus Dormant Pulses, lo reparan 5 % de su casco por segundo durante 6 s. |
| **Tesseract** | – | Llegan 20 Facets más de golpe, por encima de su número habitual. | – |

### Los Guardianes del clan {#the-clan-wardens}

| Guardián | Al empezar | Por debajo de dos tercios | Por debajo de un tercio |
| :--- | :--- | :--- | :--- |
| **Brood Warden** (I, II, III) | Los 4 drones vienen a su lado de golpe. | Sus drones lo reparan ×1,5 más rápido durante 15 s. | Llegan 2 drones más, por encima de su número habitual, durante 30 s. No pagan nada. |
| **Siege Warden** (I, II, III) | – | Dispara su cohete ×2 más a menudo durante 20 s. | Repara 15 % de su casco y su escudo (una ráfaga de daño la interrumpe). |
| **Wrath Warden** (I, II, III) | – | Sus láseres golpean ×1,25 más fuerte. | Sus láseres golpean ×1,5 más fuerte en total, no sumado al paso anterior. |

### El Señor de la guerra de la mazmorra {#the-dungeon-warlord}

- **Por debajo de dos tercios**: La pausa entre sus habilidades baja a 4 s y sus esperas a ×0,75.
- **Por debajo de un tercio**: La pausa baja a 2 s, sus esperas a ×0,5 y su daño sube a ×1,25; lanza una andanada de Meteor gratis, y su Swarm nunca vuelve más rápido que cada 120 s.
- **Una pausa en cada paso.** Cuando empieza un paso, el Señor de la guerra no puede ser dañado durante 3 s.

### Los jefes de las puertas en solitario {#the-solo-gate-bosses}

Los seis jefes de las puertas en solitario también tienen tres pasos, sus fases: están en la tabla de [los jefes](/wiki/03-Mechanics/Solo-Gates.md#the-bosses) del artículo de las puertas en solitario.

<!-- mob-ladders:end -->

## Más información {#where-to-read-more}

- [Combate](/wiki/03-Mechanics/Combat.md#who-an-alien-fights): contra quién lucha un alienígena y quién se lleva su baja.
- [Enjambres](/wiki/05-Swarms/Swarms.md): los líderes y sus pasos, un artículo por cada enjambre.
- [Warden del clan](/wiki/03-Mechanics/Clans.md#fighting-a-warden), el [Warlord de la mazmorra](/wiki/03-Mechanics/Dungeons.md#the-warlord) y los [jefes de las puertas en solitario](/wiki/03-Mechanics/Solo-Gates.md#the-bosses).
- [Guía del Viajero](/wiki/03-Mechanics/Travelers-Guide.md): lo que has aprendido de un alienígena. Nunca dice cuál lleva una habilidad.
