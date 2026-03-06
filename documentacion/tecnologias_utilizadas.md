# 🛠️ Documentación Técnica

> Sistema de Gestión de Torneo Interfacultades de Fútbol · Universidad Catolica del Norte · 2026

---

## 3.1 Descripción General del Sistema

El sistema es una aplicación web desarrollada con arquitectura **MVC (Modelo-Vista-Controlador)**, implementada en Python utilizando el microframework Flask. La persistencia de datos se realiza mediante una base de datos SQLite gestionada a través del ORM Flask-SQLAlchemy.

---

## 3.2 Tecnologías Utilizadas y Justificación

| Tecnología | Versión | Rol en el Sistema | Justificación |
|------------|---------|-------------------|---------------|
| **Python** | 3.10+ | Lenguaje de programación base | Excelente para proyectos web, gran comunidad y sintaxis clara. Lenguaje definido para el proyecto. |
| **Flask** | 3.0.0 | Framework web — servidor, rutas, vistas | Microframework ligero, ideal para proyectos académicos. Permite entender el flujo HTTP sin abstracción excesiva. |
| **Flask-SQLAlchemy** | 3.1.1 | ORM para base de datos | Permite trabajar con la base de datos usando objetos Python sin escribir SQL directamente, reduciendo errores. |
| **SQLite** | Integrado | Base de datos relacional | No requiere servidor separado. El archivo `.db` se genera automáticamente al ejecutar la aplicación. |
| **Jinja2** | Incluido en Flask | Motor de plantillas HTML | Genera HTML dinámico desde Python con herencia de plantillas, evitando repetición de código. |
| **Bootstrap 5** | 5.3.0 (CDN) | Framework CSS para interfaz | Permite crear una interfaz responsive y profesional sin escribir CSS desde cero. |

---

## 3.3 Arquitectura del Sistema

El sistema sigue el patrón **MVC** de la siguiente manera:

| Capa | Archivo | Responsabilidad |
|------|---------|-----------------|
| **Modelo** | `models.py` | Define las clases `Equipo`, `Jugador`, `Partido` y `Resultado`, mapeadas a tablas en SQLite |
| **Vista** | `templates/` | Plantillas HTML con Jinja2 que heredan de `base.html` para mantener consistencia visual |
| **Controlador** | `app.py` | Rutas Flask que reciben peticiones HTTP, interactúan con los modelos y devuelven las vistas |

**Flujo de una petición:**

```
Usuario
  │  HTTP Request
  ▼
app.py ──── Controlador (@app.route)
  │               │
  │         models.py ──── SQLAlchemy ──── SQLite (torneo.db)
  │
  └──── templates/ ──── Jinja2 ──── HTML
                │
                ▼
            Navegador
```

---

## 3.4 Modelo de Datos

El sistema maneja cuatro entidades principales:

| Entidad | Atributos Principales | Relaciones | Descripción |
|---------|-----------------------|------------|-------------|
| **Equipo** | `id`, `nombre`, `facultad`, `puntos`, `PJ`, `PG`, `PE`, `PP`, `GF`, `GC` | 1 equipo → N jugadores · 1 equipo → N partidos | Representa a cada equipo participante del torneo |
| **Jugador** | `id`, `nombre`, `numero`, `goles`, `equipo_id` | N jugadores → 1 equipo | Cada jugador pertenece a un equipo y acumula goles |
| **Partido** | `id`, `jornada`, `equipo_local_id`, `equipo_visitante_id`, `goles_local`, `goles_visitante`, `jugado` | Referencia a 2 equipos | Representa cada encuentro del calendario |
| **Resultado** | `id`, `partido_id`, `descripcion` | Referencia a un partido | Entidad auxiliar para observaciones del partido |

---

## 3.5 Lógica de Negocio Principal

### Generación del Calendario

Se utiliza el módulo `itertools.combinations` de Python para generar todos los posibles enfrentamientos entre equipos (formato todos contra todos). Los pares se distribuyen en jornadas de `n/2` partidos cada una.

```python
from itertools import combinations

pares = list(combinations(equipos, 2))  # genera todos los enfrentamientos posibles
```

### Actualización de la Tabla de Posiciones

Al registrar el resultado de un partido, el sistema evalúa automáticamente:

```python
if goles_local > goles_visitante:
    equipo_local.puntos += 3      # victoria local
elif goles_visitante > goles_local:
    equipo_visitante.puntos += 3  # victoria visitante
else:
    equipo_local.puntos += 1      # empate
    equipo_visitante.puntos += 1
```

También se actualizan: `PJ`, `PG`, `PE`, `PP`, `GF`, `GC` por equipo y el contador de goles de cada jugador marcado como goleador.

---

## 3.6 Estructura de Archivos del Proyecto

```
sistema-torneo-futbol/
├── app.py                  ← Rutas y controladores Flask
├── models.py               ← Modelos de base de datos (SQLAlchemy)
├── requirements.txt        ← Dependencias del proyecto
├── torneo.db               ← Base de datos SQLite (generada al ejecutar)
├── templates/              ← Plantillas HTML (Jinja2)
│   ├── base.html           ← Plantilla base con navbar
│   ├── index.html          ← Panel de inicio
│   ├── equipos/
│   ├── jugadores/
│   ├── calendario/
│   ├── resultados/
│   ├── tabla/
│   └── reportes/
└── docs/                   ← Documentación del proyecto
    ├── plan_de_pruebas.md
    ├── manual_usuario.md
    ├── documentacion_tecnica.md
    └── estrategia_seguimiento.md
```