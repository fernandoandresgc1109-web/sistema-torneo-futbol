# 🔄 Estrategia de Seguimiento y Soporte Post-Proyecto

> Sistema de Gestión de Torneo Interfacultades de Fútbol · Universidad Catolica del Norte · 2026

---

## 4.1 Introducción

Esta sección describe las acciones recomendadas para garantizar el correcto funcionamiento del sistema después de su entrega y despliegue inicial. El objetivo es mantener el sistema operativo, corregir posibles fallas y planear mejoras futuras.

---

## 4.2 Clasificación de Incidencias

| Prioridad | Tipo | Ejemplo | Tiempo de Respuesta |
|-----------|------|---------|---------------------|
| 🔴 **Alta** | Error crítico que impide el uso del sistema | El sistema no inicia, no se puede registrar ningún resultado | Menos de 24 horas |
| 🟡 **Media** | Error funcional en un módulo específico | Los goles del goleador no se están actualizando correctamente | 2 a 3 días hábiles |
| 🟢 **Baja** | Mejora estética o funcional menor | Agregar filtro de búsqueda en la lista de jugadores | 1 a 2 semanas |

---

## 4.3 Canal de Reporte de Errores

Se recomienda utilizar el sistema de **Issues de GitHub** para el reporte de errores y sugerencias.

**Proceso:**

1. El usuario o administrador detecta un error o tiene una sugerencia de mejora.
2. Crea un **Issue** en el repositorio describiendo el problema, los pasos para reproducirlo y el resultado esperado.
3. El equipo de desarrollo revisa el Issue, lo clasifica por prioridad y asigna un responsable.
4. El responsable desarrolla la corrección en una rama separada: `feature/fix-nombre-error`.
5. Se realizan pruebas y se hace **merge** a la rama principal.
6. Se notifica al reportante que el error fue corregido y el Issue se cierra.

---

## 4.4 Plan de Mantenimiento

| Frecuencia | Actividad | Responsable |
|------------|-----------|-------------|
| **Al finalizar cada torneo** | Respaldar `torneo.db` y resetear los datos para el nuevo torneo | Administrador del sistema |
| **Mensual** | Revisar Issues abiertos sin resolver en GitHub | Equipo de desarrollo |
| **Semestral** | Revisar y aplicar actualizaciones de dependencias (Flask, SQLAlchemy) | Equipo de desarrollo |
| **A demanda** | Implementar nuevas funcionalidades solicitadas por los usuarios | Equipo de desarrollo |

---

## 4.5 Mejoras Futuras Propuestas

Con base en el análisis del sistema actual, se proponen las siguientes mejoras para versiones futuras:

- 🔐 **Módulo de autenticación:** agregar login con usuario y contraseña para que solo personas autorizadas puedan registrar resultados.
- 🏆 **Fase eliminatoria:** agregar soporte para semifinales y final después de la fase de grupos.
- 📄 **Generación de reportes PDF:** permitir exportar la tabla de posiciones y goleadores en formato PDF.
- 📧 **Notificaciones:** enviar correos automáticos a los equipos con el resultado después de cada partido.
- 📱 **Aplicación móvil:** desarrollar una versión mobile-friendly con mejor experiencia en dispositivos pequeños.
- 📊 **Estadísticas avanzadas:** tarjetas amarillas y rojas, asistencias, porterías a cero.

---

## 4.6 Respaldo y Recuperación de Datos

La base de datos del sistema es el archivo `torneo.db` ubicado en la raíz del proyecto.

- Copiar `torneo.db` a una ubicación segura o Google Drive antes de cada jornada importante.
- En caso de pérdida, reemplazar `torneo.db` con la copia más reciente y reiniciar el servidor Flask.

> 📝 **Nota:** Para una solución más robusta en producción, se recomienda migrar a PostgreSQL y configurar backups automáticos diarios.

---

## 4.7 Contacto y Soporte

| Canal | Dirección                                                             |
|-------|-----------------------------------------------------------------------|
| 🐙 **Repositorio GitHub** | `https://github.com/ebuitra10/sistema-torneo-futbol` — sección Issues |
| 📧 **Correo del equipo** | `equipo.torneo@catolicadelnorte.edu.co`                               |

> ⏱️ El tiempo de respuesta estará sujeto a la disponibilidad del equipo de desarrollo y a la prioridad de la incidencia según la clasificación de la sección 4.2.