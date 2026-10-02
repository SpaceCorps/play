<!-- wiki-i18n source: 46436d9c65bc6c7e -->
<!-- wiki-i18n title: Extras -->
# Extras {#extras}

Los extras son los dispositivos que van en las **ranuras de extra** de una nave (tres en cada nave, por configuración). Los activas desde el selector de Extras de la barra rápida o desde una ranura de la barra que les hayas asignado. Solo funcionan desde la configuración que pilotas: si instalas uno en la otra configuración, espera hasta que cambies de configuración.

| Extra | Qué hace | Usos | Precio |
| :---- | :----------- | :--- | :---- |
| **Repair Drone I a IV** | Repara tu casco: 1,5 %, 2,25 %, 3,5 % y 5 % del máximo por segundo | ilimitados | 5000 / 15.000 / 35.000 créditos, 2000 Thulium |
| **Cloaking CPU S** | Oculta tu nave | 10 | 5000 Thulium |
| **Cloaking CPU M** | Oculta tu nave | 25 | 11.250 Thulium |
| **Cloaking CPU L** | Oculta tu nave | 50 | 20.000 Thulium |
| **EMP Charge** | Durante 3 segundos nadie puede fijarte, todas las fijaciones sobre ti se rompen y todos los camuflajes cercanos terminan | 1 | 500 Thulium |

Las Cloaking CPU y la EMP Charge se venden solo en la tienda. No se pueden fusionar y nada las regala.

## Repair Drones {#repair-drones}

Activa un Repair Drone (REP) y repara el casco hasta que esté completo. Solo empieza tras 10 segundos sin recibir impactos, y cualquier impacto lo apaga. Con varios instalados, trabaja el mejor. Las tasas están en [Combate](/wiki/03-Mechanics/Combat.md).

## Cloaking CPU {#cloaking-cpu}

Pulsa la ranura CLK para camuflarte. **Una pulsación es un uso**, sea cual sea el paquete, y los usos que quedan se ven en la ranura y en el hangar. Un camuflaje **no tiene límite de tiempo**: sigue activo hasta que lo apagas o algo lo rompe.

- **Quién no puede verte.** Los pilotos de otras corporaciones y los alienígenas no ven tu nave en absoluto: no aparece en su pantalla ni en su lista de objetivos, y nadie puede fijarla. Los pilotos de corporación de otras corporaciones también la ignoran.
- **El punto de radar.** Todos los demás pilotos del mapa, salvo los de tu propia corporación, ven un simple **punto rojo** en el minimapa donde estás, así que saben que hay alguien camuflado cerca. El punto no tiene nombre, nave, corporación ni id, y no admite clics ni fijación; al pasar el cursor por encima solo dice «Hay algo camuflado aquí». Es redondo, dentro de un anillo (las naves en el minimapa son cuadrados), y el anillo «respira» despacio, o se queda quieto si tienes activado Reducir movimiento. El servidor lo actualiza unas dos veces por segundo y tu juego lo mueve con suavidad entre una actualización y otra. Dice que hay alguien y dónde, no quién: un piloto que te vio camuflarte puede seguir el punto, y la **explosión de un cohete** dirigida a él aun así te alcanza.
- **Quién sí te ve.** Tú ves tu propia nave, tenue y con un contorno. Los pilotos de tu corporación te ven como un fantasma pálido; los compañeros de clan de otras corporaciones no, porque un clan admite a cualquiera que lo solicite. Nadie puede fijar al fantasma, ni siquiera tu corporación.
- **No puedes camuflarte** dentro de una zona segura, mientras la CPU se recarga, ni en los **10 segundos** posteriores a recibir un impacto o disparar.
- **Qué lo termina.** Volver a pulsar la ranura, tu primera andanada o cohete (llega a su destino y te ven), entrar en una zona segura, que la CPU salga de la configuración que pilotas, un **EMP que se active a menos de 1500 unidades** de ti, lo haya lanzado quien lo haya lanzado (también el de tu corporación, pero no el de un compañero de grupo), y la explosión en área de un cohete que te alcanza. El tiempo no lo termina, recoger carga tampoco (una caja que recoges desaparece para todos, así que se enteran de que algo estuvo al alcance de ese punto, no de quién), las habilidades tampoco, y la radiación del agujero negro daña a una nave camuflada pero no termina su camuflaje. Cerrar sesión o morir lo termina, porque una nave que nadie pilota no está camuflada.
- **Recarga.** Cuando un camuflaje termina, sea como sea, la CPU se recarga durante **60 segundos**. La recarga es tuya, no de la nave: continúa si saltas por un portal, cierras sesión o mueres. Cada pulsación sigue costando un uso.
- **Los alienígenas** que iban tras de ti te pierden. Tus reclamaciones de derribo se liberan cuando te camuflas.
- **Cohetes.** Nadie puede fijar un cohete guiado sobre ti, y un cohete recto de un objetivo te atraviesa. Una **explosión en área** sigue dañando a una nave que cubre y termina su camuflaje, y a los pilotos que pueden ver el lugar de la nave se les muestra antes de que aparezca el número de daño. Lanzar un cohete es un disparo: termina tu propio camuflaje igual que una andanada (la CPU se recarga entonces los 60 segundos indicados arriba) y, camuflado o no, te impide camuflarte durante los 10 segundos siguientes.
- **El agujero negro** se traga una nave camuflada como cualquier otra, y todo el mapa lo oye.
- **Lo que ves.** Tu nave se vuelve translúcida, con un contorno violeta discontinuo, y un indicador en la parte superior de la pantalla dice «Camuflado» con los usos que quedan (sin segundos: no hay temporizador). La ranura CLK muestra los usos restantes; mientras estás camuflado brilla en violeta y dice ON, y cuando el camuflaje termina, sea como sea, se oscurece y cuenta los 60 segundos de recarga. Una pulsación que el servidor rechaza (recarga, zona segura, un impacto o un disparo en los últimos 10 segundos) hace parpadear la ranura en rojo, y un mensaje te dice por qué. Un aliado se muestra como un fantasma pálido con una marca de fantasma antes de su nombre, y un piloto que se camufla cerca de ti se desvanece con una onda. Arrastra CLK desde los Extras de la barra rápida a una ranura para usarlo, como REP.
- **Los usos** se guardan con la CPU. Cerrar sesión, morir o reiniciar el juego no devuelve ninguno, y una activación que cancelas se gasta igualmente. Cuando se acaba el último uso de un paquete, este se consume y su ranura se rellena con una CPU igual de repuesto que tengas en el inventario, si tienes alguna.
- **Varias CPU** en una misma configuración no se suman. Se usa primero la que menos usos tiene.

Las S, M y L se comportan igual: los paquetes más grandes solo salen más baratos por uso (500, 450 y 400 Thulium).

## EMP Charge {#emp-charge}

Pulsa la ranura EMP en combate. Durante **3 segundos** nadie puede fijarte, y **todos los que te tenían fijado pierden la fijación** al instante, estén donde estén: pilotos, alienígenas y pilotos de corporación. A un piloto al que se le rompe la fijación se le avisa con «Fijación perdida: el objetivo usó un EMP». Quien intente fijarte en esos 3 segundos es rechazado.

- **No es invulnerabilidad.** Detiene lo que necesita fijación: los láseres, los cohetes guiados y el contacto de un cohete recto de un objetivo, que te atraviesa. Una **explosión en área** no necesita fijación, así que sigue dañándote si estás dentro, y el agujero negro no es un disparo en absoluto.
- **Sigues pudiendo actuar.** Disparar no lo termina. Puedes camuflarte (si las reglas propias del camuflaje lo permiten) y usar otros extras.
- **Termina los camuflajes cercanos.** Toda nave camuflada a menos de **1500 unidades** de ti cuando se activa el pulso se muestra al instante y su CPU empieza sus 60 segundos de recarga, sea de la corporación que sea, también la tuya; las naves de tu propio [grupo](/wiki/03-Mechanics/Groups.md) son la excepción: conservan su camuflaje. Al piloto se le avisa con «Camuflaje roto: se ha lanzado un EMP cerca.», ve reaparecer la nave con la misma onda que en cualquier descamuflaje, y la ranura empieza su recarga. No puedes usar un EMP estando tú mismo camuflado.
- **No oculta nada.** Todos te siguen viendo, con una envoltura eléctrica crepitante durante los 3 segundos.
- **No puedes usarlo** mientras te protege una zona segura, estando camuflado, ni en los **30 segundos** posteriores al último. Funciona en todos los demás sitios, incluidos los primeros días de una temporada (el Protocolo de paz): entonces los alienígenas siguen cazando.
- Un alienígena al que alcances durante los 3 segundos no se vuelve contra ti hasta que terminen. Tus reclamaciones de derribo y las reglas del primer impacto no cambian.
- **Lo que ves.** Un pulso de espacio deformado sale disparado desde el piloto hasta donde el pulso termina camuflajes (1500 unidades), todos los que están al alcance lo ven, y una envoltura eléctrica crepitante lo rodea durante los 3 segundos, con un anillo alrededor de tu propia nave y un indicador en la parte superior de la pantalla que cuentan el tiempo. El anillo de objetivo de todos los que te tenían seleccionado se rompe en pedazos, con un chispazo corto. La ranura EMP muestra las cargas que tienes, se ilumina en azul mientras la envoltura está activa y se oscurece mientras se recarga.
- **Una carga, un uso.** La ranura se rellena desde tu inventario cuando tienes más. Los **30 segundos** de recarga no se guardan: cerrar sesión o saltar por un portal los borra, y el siguiente pulso cuesta una carga.
