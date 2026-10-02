<!-- wiki-i18n source: 21f10d185095b346 -->
<!-- wiki-i18n title: Clanes -->
# Clanes {#clans}

Fundar un clan o unirte a uno te permite reunir recursos, subir de nivel la banca compartida, fijar tasas de impuesto, coordinarte con los miembros de la facción y gestionar la diplomacia.

## Progreso del clan {#clan-progression}

Los clanes empiezan en el nivel 1 y pueden mejorar hasta el nivel 5. Mejorar el clan requiere créditos, que se pagan del **Banco del clan**. Las mejoras aumentan la capacidad de miembros y los límites diarios de pago.

| Nivel del clan | Límite de miembros | Límite diario de pago (por miembro) | Costo de mejora (créditos) |
| :---: | :---: | :---: | :--- |
| **Nivel 1** | 10 | 1.000.000 Cr | — |
| **Nivel 2** | 25 | 2.000.000 Cr | 10.000.000 Cr |
| **Nivel 3** | 50 | 3.000.000 Cr | 100.000.000 Cr |
| **Nivel 4** | 75 | 4.000.000 Cr | 1.000.000.000 Cr |
| **Nivel 5** | 100 | 5.000.000 Cr | 10.000.000.000 Cr |

---

## Economía e impuestos del clan {#clan-economy-taxation}

Los clanes funcionan con un sistema financiero basado en impuestos:

### 1. Impuesto diario {#1-daily-taxation}

- **Tasa de impuesto**: el líder o los colíderes pueden fijar una tasa de impuesto diaria de entre el **0 % y el 5 %**.
- **Cobro automático**: una vez al día (UTC), el servidor cobra automáticamente los impuestos a todos los miembros del clan.
- **Fórmula**: el impuesto se calcula como `ClanTaxRate` del saldo actual de créditos de cada miembro.
  - *Ejemplo*: si tienes 10.000.000 de créditos y el impuesto del clan es del 2 %, se descontarán 200.000 créditos de tu cuenta y se ingresarán en el Banco del clan.
  - También se pueden hacer donaciones voluntarias de créditos, hasta el límite de la sección siguiente.

### 2. Donaciones {#2-donations}

- **Donar**: cualquier miembro puede enviar créditos al Banco del clan desde la página Clan. La ventana muestra lo que aún puedes enviar.
- **Límite de donaciones**: un piloto puede enviar como máximo **1.000.000 de créditos a clanes en cualquier periodo de 24 horas**, contando todos los clanes en los que haya estado. Salir de un clan y unirse a otro no da una asignación nueva.
- **Sin reinicio diario**: las 24 horas se desplazan. Cada donación deja de contar exactamente 24 horas después de hacerse, y la ventana te dice cuándo ocurre con la más antigua y cuánto se recupera. Una donación que supere lo que queda se rechaza entera.
- El impuesto diario no es una donación y no gasta tu asignación.

### 3. Pagos del banco {#3-bank-payouts}

- **Límites de pago**: los líderes y oficiales del clan pueden repartir créditos del Banco del clan a miembros concretos.
- **Límite diario**: un miembro no puede recibir más de `1,000,000 * ClanLevel` créditos en pagos en un mismo día natural (UTC).

---

## Jerarquía y rangos {#hierarchy-roles}

Los clanes usan una estructura de rangos basada en roles para gestionar los permisos:

- **Líder (rol 3)**: tiene acceso administrativo completo, incluido mejorar, fijar impuestos, la diplomacia, los ascensos, las expulsiones y la disolución del clan.
- **Colíder (rol 2)**: puede fijar tasas de impuesto, pagar créditos, gestionar la diplomacia y ascender o degradar a rangos inferiores.
- **Veterano (rol 1)**: miembro de confianza que puede aceptar solicitudes nuevas de ingreso al clan.
- **Miembro (rol 0)**: jugador normal sin permisos administrativos.

### Tabla de permisos {#permissions-table}

| Acción | Líder | Colíder | Veterano | Miembro |
| :--- | :---: | :---: | :---: | :---: |
| **Disolver el clan** | ✅ | ❌ | ❌ | ❌ |
| **Mejorar el clan** | ✅ | ❌ | ❌ | ❌ |
| **Fijar la tasa de impuesto** | ✅ | ✅ | ❌ | ❌ |
| **Pagar créditos** | ✅ | ✅ | ❌ | ❌ |
| **Gestionar la diplomacia** | ✅ | ✅ | ❌ | ❌ |
| **Ascender / expulsar** | ✅ | ✅* | ❌ | ❌ |
| **Aceptar solicitudes** | ✅ | ✅ | ✅ | ❌ |

*\*Los colíderes solo pueden ascender, degradar o expulsar a miembros de un rango inferior al suyo.*

### Cuando el líder se va {#when-the-leader-leaves}

Un líder no puede salir de un clan que aún tiene otros miembros: antes debe ascender a un colíder a líder (el líder pasa a colíder) o salir el último, lo que disuelve el clan. Si el líder elimina su cuenta (Configuración › Cuenta), el liderazgo pasa al miembro de mayor rango y, en caso de empate, al que lleve más tiempo; un líder que esté solo en el clan lo disuelve, banco incluido.

---

## Diplomacia {#diplomacy}

Los clanes pueden establecer relaciones diplomáticas formales con otras organizaciones introduciendo la etiqueta del clan objetivo:

- **Alianza**: clanes aliados formalmente. El estado amistoso se muestra en el mapa.
- **Pacto de no agresión (NAP)**: acuerdo de no iniciar hostilidades.
- **Guerra**: declaración formal de guerra. Los objetivos de guerra se pueden atacar en cualquier lugar sin penalización.

---

## Trae a un amigo {#bringing-a-friend}

Un amigo que sea nuevo en el juego puede unirse con tu código de invitación personal y recibe un paquete inicial; consulta [Invitar amigos](/wiki/03-Mechanics/Invite-Friends.md). Una vez dentro del juego, puede solicitar el ingreso en tu clan como cualquier piloto.
