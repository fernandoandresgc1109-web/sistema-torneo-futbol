# 📖 Manual Básico de Usuario

> Sistema de Gestión de Torneo Interfacultades de Fútbol · Universidad Catolica del Norte · 2026

---

## 2.1 Introducción

Este manual tiene como objetivo guiar al usuario en el uso del Sistema de Gestión de Torneo Interfacultades de Fútbol. El sistema es una aplicación web accesible desde cualquier navegador moderno (Chrome, Firefox, Edge). No requiere instalación por parte del usuario final.

---

## 2.2 Acceso al Sistema

Abre tu navegador web e ingresa la siguiente dirección:

```
http://127.0.0.1:5000
```

Serás redirigido al panel principal donde encontrarás un resumen del estado del torneo y las acciones rápidas disponibles.

---

## 2.3 Navegación Principal

| Sección | Descripción |
|---------|-------------|
| 🛡️ **Equipos** | Listado, registro y detalle de equipos |
| 👤 **Jugadores** | Listado y registro de jugadores |
| 📅 **Calendario** | Visualización y generación del calendario de partidos |
| 📊 **Tabla** | Tabla de posiciones actualizada en tiempo real |
| 📈 **Reportes** | Estadísticas del torneo y tabla de goleadores |

---

## 2.4 Guía Paso a Paso

### Paso 1 — Registrar Equipos

1. Haz clic en **Equipos** en la barra de navegación.
2. Haz clic en el botón verde **Nuevo Equipo**.
3. Ingresa el nombre del equipo y la facultad a la que pertenece.
4. Haz clic en **Registrar Equipo**. Verás un mensaje de confirmación en verde.

> ⚠️ **Importante:** Debes registrar al menos 2 equipos antes de generar el calendario.

---

### Paso 2 — Registrar Jugadores

1. Haz clic en **Jugadores** en la barra de navegación.
2. Haz clic en **Nuevo Jugador**.
3. Ingresa el nombre, número de camiseta (opcional) y selecciona el equipo.
4. Haz clic en **Registrar Jugador**.

> 📝 **Nota:** Registrar jugadores es opcional, pero necesario para marcar goleadores en los partidos.

---

### Paso 3 — Generar el Calendario

1. Haz clic en **Calendario** en la barra de navegación.
2. Si no hay partidos generados, verás el botón **Generar Calendario**.
3. Haz clic en él. El sistema creará automáticamente todos los partidos en formato todos contra todos, organizados por jornadas.

> ⚠️ **Importante:** El calendario solo puede generarse una vez. Si necesitas regenerarlo, contacta al administrador del sistema.

---

### Paso 4 — Registrar Resultados

1. Ve a **Calendario**.
2. Identifica el partido a registrar (estado: **Pendiente**).
3. Haz clic en el botón **Registrar** en la fila del partido.
4. Ingresa los goles anotados por cada equipo.
5. Selecciona los jugadores que marcaron goles (puedes seleccionar varios).
6. Haz clic en **Guardar Resultado**.

> ℹ️ El sistema actualizará automáticamente la tabla de posiciones al guardar.

---

### Paso 5 — Ver la Tabla de Posiciones

1. Haz clic en **Tabla** en la barra de navegación.
2. Verás la tabla ordenada por puntos. En caso de empate, el criterio de desempate es la diferencia de goles.

> 🥇 Los equipos en las primeras 3 posiciones se destacan visualmente.

---

### Paso 6 — Consultar Reportes

1. Haz clic en **Reportes**.
2. Verás el total de partidos jugados, pendientes y goles del torneo.
3. La tabla de goleadores muestra los 10 jugadores con más goles.

---

## 2.5 Mensajes del Sistema

| Tipo | Ejemplo | Significado |
|------|---------|-------------|
| ✅ **Verde — Éxito** | "Equipo registrado exitosamente" | La operación se completó sin problemas |
| ⚠️ **Amarillo — Advertencia** | "El calendario ya fue generado" | La acción no se realizó para evitar duplicados |
| ❌ **Rojo — Error** | "Ya existe un equipo con ese nombre" | Se ingresaron datos inválidos o duplicados |