1.1	Introducción del Plan de Pruebas:

El presente plan de pruebas tiene como objetivo validar el correcto funcionamiento del sistema de gestión de torneos de fútbol universitario.
A través de este documento se definen la estrategia de pruebas, los casos de prueba y los resultados esperados, con el fin de garantizar que el sistema cumpla con los requisitos establecidos y funcione de manera adecuada para los usuarios finales.

1.2	Estrategia de Pruebas:

La estrategia de pruebas utilizada en el proyecto es de tipo funcional, enfocada en verificar que cada una de las funcionalidades del sistema cumpla con los requisitos definidos.

Las pruebas se realizarán de manera manual, simulando el uso real del sistema por parte de los usuarios, validando procesos como el registro de equipos, la programación de partidos, el ingreso de resultados y la visualización de la tabla de posiciones.

1.3	Tipos de pruebas:

-  Pruebas funcionales
-  Pruebas de validación de datos
-  Pruebas de aceptación del usuario

Se realizaron pruebas funcionales para verificar el correcto comportamiento de cada módulo del sistema, así como pruebas de validación de datos para asegurar que la información ingresada sea correcta. Finalmente, se consideraron pruebas de aceptación, simulando el uso del sistema por parte de los organizadores del torneo.

1.4	Casos de Prueba:

ID	Funcionalidad	Caso de prueba	Resultado esperado
CP-01	Registro de equipos	Registrar un equipo con datos válidos	El sistema guarda el equipo correctamente
CP-02	Registro de equipos	Registrar equipo con campos vacíos	El sistema muestra mensaje de error
CP-03	Programación de partidos	Generar calendario automáticamente	Se genera calendario sin cruces incorrectos
CP-04	Registro de resultados	Ingresar resultado de un partido	Se actualiza la tabla de posiciones


1.5	Evidencias simuladas:

Las evidencias de las pruebas realizadas fueron simuladas mediante la descripción de los resultados esperados, debido a que el sistema se encuentra en etapa académica de desarrollo. Estas evidencias permiten validar de forma conceptual el correcto funcionamiento de cada módulo del sistema.
