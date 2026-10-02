<!-- wiki-i18n source: ac17fd77713a030e -->
<!-- wiki-i18n title: Inventario -->
# Inventario y equipamiento {#inventory-equipment}

El hangar te permite gestionar tus naves y tu equipo. Equipar bien los objetos es clave para sobrevivir y dominar. Puedes hacerlo en la estación y en vuelo desde dentro de una zona segura: consulta [El hangar en vuelo](/wiki/03-Mechanics/Hangar.md).

## Ranuras de equipo y eficiencia de estadísticas {#equipment-slots-stat-efficiencies}

A diferencia de los juegos espaciales tradicionales, SpaceCorps tiene ranuras de equipo escalonadas de forma dinámica que modulan la eficacia de los módulos instalados.

- **Ranuras de láser**: para las armas ofensivas (láseres). Siempre rinden al **100 % de daño y alcance**.
- **Ranuras de generadores**: ranuras compartidas para escudos, motores y núcleos adaptativos. Se dividen en tres bandas de eficiencia, y la banda decide cuánto de las estadísticas base de un objeto cuenta. En el hangar cada banda tiene una (i) junto a su nombre que la explica:
  - **Ranuras principales**: los objetos colocados aquí reciben el **100 %** de sus estadísticas base. Todas las naves las tienen: pon aquí tus escudos y motores más fuertes.
  - **Ranuras de apoyo**: los objetos colocados aquí reciben el **75 %** de sus estadísticas base (p. ej., el 75 % de la velocidad o de la capacidad de escudo). Todas las naves las tienen.
  - **Ranuras auxiliares**: los objetos colocados aquí reciben el **50 %** de sus estadísticas base. Solo algunas naves las tienen (la Paragon tiene 2, la Ironclad 3 y la Wraith 4; la Protos, la Kitefin y la Ostirion no tienen ninguna). Son ideales para escudos y motores adicionales más débiles, mientras que los más fuertes van en las ranuras principales.
  - **Ranuras de dron**: un escudo en uno de tus drones cuenta como uno en una ranura principal, el **100 %** de sus estadísticas (consulta [Mecánicas de los drones](/wiki/03-Mechanics/Drones.md)).
  - **Ranuras sin asignar o heredadas**: los objetos colocados aquí no aportan nada a las estadísticas.
  - **La acumulación también pierde fuerza**: los escudos y los motores se ordenan del más fuerte al más débil, y la parte de la banda se multiplica por la de su puesto: del 1.º al 4.º cuentan por completo, el 5.º, el 6.º y el 7.º un 85 %, un 70 % y un 55 %, y del 8.º en adelante un 25 %. Consulta [Escudos](/wiki/03-Mechanics/Shields.md) y [Velocidad](/wiki/03-Mechanics/Speed.md).
- **Ranuras de extra**: para objetos de utilidad especializados, como los Repair Drones.

## Orden del inventario {#inventory-order}

El inventario enumera tus objetos en el mismo orden que la tienda, sea cual sea el orden en que los compraste, fabricaste o encontraste. Los tipos que van juntos están juntos: láseres, amplificadores láser y munición láser; escudos y células de escudo; motores y propulsores; núcleos adaptativos; extras (Repair Drones); drones; y después los recursos. Dentro de un tipo va primero lo más barato (los créditos antes que el Thulium) y luego lo que no tiene precio: el equipo solo fabricable y los botines, de la rareza más débil a la más fuerte (los láseres de una misma rareza, del menor daño al mayor). La munición láser va de x1 a x4 y después la Siphon Battery. Los cohetes se ordenan por clase (un objetivo antes que explosión en área, guiados antes que rectos) y luego por grado, así que el cohete épico, que cuesta Thulium, queda el último de su clase. Las copias de un mismo objeto se ordenan por su grado de encantamiento. Encima de la cuadrícula, un chip por tipo sigue el mismo orden, cada uno con el número de objetos que encuentra en él la búsqueda. Cada chip se activa o se desactiva por separado, así que puedes ocultar la munición y los Repair Drones mientras trabajas con láseres, escudos y motores: haz clic en un chip para mostrar u ocultar su tipo, haz clic con Shift (o doble clic) para dejar activado solo ese tipo y vuelve a hacer clic en él para recuperar los demás. **Todas** muestra todos los tipos y **Ninguna** los oculta todos, para activar solo los que quieras. Un chip tachado está desactivado y un chip con una marca de verificación está activado. La búsqueda actúa sobre los tipos que están activados, y tu elección se guarda con tu piloto. Si todo está oculto, la cuadrícula lo indica y ofrece **Mostrar todas las categorías**.

## Instalar objetos en objetos (subranuras) {#item-to-item-equipping-sub-sockets-}

Algunos objetos principales pueden «equipar» objetos secundarios de apoyo (lo que se llama instalar en subranuras) para amplificar sus parámetros. Para instalar en una subranura, arrastra el objeto de apoyo directamente sobre el objeto principal en el inventario de tu hangar.

### Tabla de compatibilidad {#compatibility-table}

| Objeto principal | Objetos admitidos en subranuras | Efecto resultante |
| :--- | :--- | :--- |
| **Láser** | Amplificador láser (amp.) | Aumenta el daño base y las estadísticas de golpe crítico |
| **Escudo** | Célula de escudo | Aumenta la capacidad de escudo y la velocidad de recarga |
| **Motor** | Propulsor | Aumenta la velocidad del motor y sus multiplicadores |
| **Generador híbrido** | Célula de escudo O propulsor | Aumenta la capacidad de escudo, la velocidad de recarga o la velocidad |
| **Dron** | Un láser o un escudo, en cada una de sus ranuras (un Master Drone tiene dos) | Un láser suma su daño a tu andanada; un escudo cuenta como uno en una ranura principal (el 100 % de sus estadísticas) |

---

## Gestión de la munición {#ammo-management}

La munición láser es un recurso consumible.
- La munición se apila en tu inventario.
- Puedes cambiar la munición láser activa desde la barra rápida de tu HUD.
- La munición de mayor calidad aporta multiplicadores de daño (p. ej., Standard Battery x1, Advanced Plasma x2, Ultra Core x3, Experimental Fusion Core x4). La Siphon Battery inflige un daño x1 solo a los escudos y se lo da al tuyo.
