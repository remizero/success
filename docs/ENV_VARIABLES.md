# Variables de entorno de aplicación en Success. 🌱

El archivo `.env` define la configuración operativa de cada aplicación Success.

Esta guía explica cómo estructurarlo correctamente para que el cargador de apps, blueprints, endpoints y extensiones funcione sin sorpresas.

> NOTA: en esta guía solo se tratarán las variables de entorno propias de Success.

---

## Get started now.

[Template](#plantilla)

---

## Table of contents. 📑

* [Ubicación y alcance](#ubicación-y-alcance)
* [Bloques recomendados](#bloques-recomendados)
* [Variables de entorno globales](#variables-de-entorno-globales)
* [Variables de entorno por aplicación](#variables-de-entorno-por-aplicación)
* [Template](#plantilla)
* [Variables mínimas recommendeds](#variables-mínimas-recommendeds)
* [Errores frecuentes](#errores-frecuentes)
* [Best practices](#buenas-prácticas)
* [Configuración advanced](#configuración-advanced)
* [Next step](#paso-siguiente)

---

## Ubicación y alcance.

Cada aplicación define su propio `.env` en:

  ```bash
    apps/<my_app>/.env
  ```

Este archivo controla:

* parámetros Flask (`APP_HOST`, `APP_PORT`, `SERVER_NAME`, etc.).
* flags de Success (`SUCCESS_*`).
* configuración de extensiones habilitadas.

> NOTAS:
> - Cada archivo .env maneja todas las variables de entorno básicas de una aplicación Flask, por lo que pueden ser configuradas de la manera habitual como siempre lo has hecho.
> - Las variables de Success (`SUCCESS_*`) son variables especiales utilizadas por el core de Success para orquestar el comportamiento de aplicaciones, blueprints, endpoints y extensiones.
> - Aunque Success utiliza el mismo sistema de variables de entorno que Flask, algunas variables pueden influir en el comportamiento interno del framework, por lo que se recomienda entender su interacción en escenarios advanced.

---

## Bloques recomendados.

Orden sugerido:

1. **Configuración general** (`APP_*`, `DEBUG`, `SECRET_KEY`).
2. **Flags Success** (`SUCCESS_*`).
3. **Extensiones** (`CORS_*`, `JWT_*`, `LOGGER_*`, etc.).

> NOTAS: 
> - Success incluye archivos `.env` preconfigurados con variables listas para cada extensión, reduciendo la configuración manual y evitando errores comunes.
> - Success también incluye archivos `.env` pre-configurados para entorno de desarrollo, pruebas y producción, así como también una modalidad `staging` para pruebas de integración como si de trabajar en modo producción se tratara.

---

## Variables de entorno globales.

Para una mejor comprensión de las variables de entorno globales de Success ir a:

[ENV_GLOBALS.md](ENV_GLOBALS.md)

---

## Variables de entorno por aplicación.

Para una mejor comprensión de las variables de entorno por aplicación de Success ir a:

[ENV_APPS.md](ENV_APPS.md)

---

## Template. (recommended) ⚡

La forma más rápida de empezar es copiando la plantilla env.globals o env.app según corresponda, incluidas en el directorio examples:

Para el proyecto `my_project`:

  ```bash
    cp examples/env.globals <path/my_project/.env>
  ```

Para la aplicación `my_app`:

  ```bash
    cp examples/env.app <path/my_project/apps/my_app/.env>
  ```

Resultado: estructura base preconfigurada para empezar a trabajar en un proyecto o aplicación.
Ideal para: iniciar rápidamente un proyecto o aplicación sin configuración manual.

---

## Variables mínimas recommendeds.

Para un arranque estable:

* `APP_ENV`
* `APP_HOST`
* `APP_PORT`
* `SERVER_NAME`
* `DEBUG`
* `SECRET_KEY`
* `SUCCESS_ENABLE_VIEW` y/o `SUCCESS_ENABLE_REST` *(define el tipo de endpoints habilitados)*
* flags de extensiones necesarias (`CORS_*`, `JWT_*`, etc.)

---

## Errores frecuentes.

* Usar comillas y formatos inconsistentes en listas (puede romper el parsing del `.env`).
* Habilitar extensiones sin definir su configuración base.
* Reutilizar secretos de ejemplo en producción.
* Dejar valores inválidos de host/puerto en modo subdomain.

---

## Best practices.

* Mantener un `.env` por aplicación.
* Usar valores explícitos y seguros para secretos.
* Separar configuración por bloques comentados.
* Versionar una plantilla (`.env.example`) sin secretos.

---

## Configuración advanced. 🛠️

[ENV_VARIABLES_AVANZADAS.md](ENV_VARIABLES_AVANZADAS.md) – escenarios multi-app, subdominios y estrategias de endurecimiento.

---

## Next step. 🔗

[BLUEPRINTS.md](BLUEPRINTS.md)
