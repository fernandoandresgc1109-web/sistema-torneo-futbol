# 📋 Plan de Pruebas del Sistema

> Sistema de Gestión de Torneo Interfacultades de Fútbol · Universidad Catolica del Norte · 2026

---

## 1.1 Introducción

Este plan de pruebas define la estrategia, el alcance, los recursos y el cronograma de las actividades de prueba para el Sistema de Gestión de Torneo Interfacultades de Fútbol. El objetivo principal es garantizar que el sistema cumple con los requisitos funcionales definidos en la fase de análisis y que opera correctamente bajo las condiciones de uso esperadas.

---

## 1.2 Alcance de las Pruebas

Las pruebas cubrirán los siguientes módulos del sistema:

| Módulo | Funcionalidades cubiertas |
|--------|--------------------------|
| **Gestión de Equipos** | Registro, listado y visualización de detalles |
| **Gestión de Jugadores** | Registro y visualización por equipo |
| **Calendario** | Generación automática de partidos (todos contra todos) |
| **Resultados** | Registro de resultados y marcación de goleadores |
| **Tabla de Posiciones** | Actualización automática de puntos y estadísticas |
| **Reportes** | Tabla de goleadores y estadísticas generales |

---

## 1.3 Estrategia de Pruebas

Se aplicarán los siguientes tipos de prueba en el orden del ciclo de vida del software:

### 🔬 1.3.1 Pruebas Unitarias
Verifican el correcto funcionamiento de funciones individuales de la lógica de negocio de forma aislada. Por ejemplo: la función que calcula puntos al registrar un resultado (victoria = 3 pts, empate = 1 pt, derrota = 0 pts).

### 🔗 1.3.2 Pruebas de Integración
Verifican que los módulos funcionen correctamente cuando interactúan entre sí. Por ejemplo, que al registrar el resultado de un partido la tabla de posiciones se actualice correctamente.

### ⬛ 1.3.3 Pruebas Funcionales (Caja Negra)
Se valida que cada funcionalidad del sistema cumpla los requisitos desde la perspectiva del usuario, sin conocer el código interno. Se basan en los casos de prueba definidos en la sección 1.4.

### 🖥️ 1.3.4 Pruebas de Interfaz de Usuario
Se verifica que la interfaz web sea intuitiva, que los formularios validen datos correctamente y que los mensajes de error y éxito se muestren adecuadamente al usuario.

---

## 1.4 Casos de Prueba

| CP-ID | Módulo | Descripción | Datos de Entrada | Resultado Esperado | Estado |
|-------|--------|-------------|------------------|--------------------|--------|
| CP-01 | Equipos | Registrar equipo con datos válidos | Nombre: `Los Tigres`, Facultad: `Ingeniería` | Equipo registrado, mensaje de éxito visible | ✅ Aprobado |
| CP-02 | Equipos | Registrar equipo con nombre duplicado | Nombre: `Los Tigres` (ya existe) | Mensaje de error: "Ya existe un equipo con ese nombre" | ✅ Aprobado |
| CP-03 | Equipos | Registrar equipo con campos vacíos | Nombre: vacío, Facultad: vacío | Formulario no se envía, campos requeridos resaltados | ✅ Aprobado |
| CP-04 | Jugadores | Registrar jugador con equipo válido | Nombre: `Juan Pérez`, #10, Equipo: `Los Tigres` | Jugador registrado y visible en la lista | ✅ Aprobado |
| CP-05 | Jugadores | Registrar jugador sin seleccionar equipo | Nombre: `Juan Pérez`, equipo: no seleccionado | Formulario no se envía, campo equipo requerido | ✅ Aprobado |
| CP-06 | Calendario | Generar calendario con 4 equipos | 4 equipos previamente registrados | Se generan 6 partidos (4×3/2), organizados en jornadas | ✅ Aprobado |
| CP-07 | Calendario | Generar calendario con menos de 2 equipos | 0 o 1 equipos registrados | Mensaje de error: "Se necesitan al menos 2 equipos" | ✅ Aprobado |
| CP-08 | Calendario | Intentar regenerar calendario existente | Calendario ya generado | Mensaje de advertencia: calendario ya fue generado | ✅ Aprobado |
| CP-09 | Resultados | Registrar victoria local 3-1 | Goles local: 3, Goles visitante: 1 | Equipo local recibe 3 puntos, tabla actualizada | ✅ Aprobado |
| CP-10 | Resultados | Registrar empate 1-1 | Goles local: 1, Goles visitante: 1 | Ambos equipos reciben 1 punto, estadísticas correctas | ✅ Aprobado |
| CP-11 | Resultados | Registrar goleadores del partido | Seleccionar 2 jugadores como goleadores | Goles de los jugadores seleccionados se incrementan en 1 | ✅ Aprobado |
| CP-12 | Resultados | Registrar resultado de partido ya jugado | Partido con estado `Jugado` | Mensaje de advertencia, no se permite el re-registro | ✅ Aprobado |
| CP-13 | Tabla | Verificar orden por puntos | 3 equipos con 6, 4 y 1 puntos | Tabla ordenada de mayor a menor puntos | ✅ Aprobado |
| CP-14 | Tabla | Verificar desempate por diferencia de goles | 2 equipos con mismos puntos, diferente dif. goles | El de mayor diferencia de goles aparece primero | ✅ Aprobado |
| CP-15 | Reportes | Verificar tabla de goleadores | Jugadores con goles registrados | Lista de top 10 goleadores en orden descendente | ✅ Aprobado |

---

## 1.5 Evidencias Simuladas de Resultados

| Métrica | Valor |
|---------|-------|
| Total de casos ejecutados | **15** |
| Casos aprobados | **15 (100%)** |
| Casos fallidos | **0 (0%)** |
| Defectos encontrados y corregidos | **3** |

**Defectos corregidos durante el desarrollo:**
- Campos no validados en formularios
- Calendario sin restricción de duplicados
- Diferencia de goles no contemplada como criterio de desempate

> 📁 Las capturas de pantalla de cada caso de prueba se encuentran en `/docs/` del repositorio.