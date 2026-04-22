# Variables de entorno SUCCESS

Este documento lista las variables `SUCCESS_*` activas en:

- Framework: `success/.env`
- App: `apps/<app_name>/.env`

## Ambito framework (`success/.env`)

| Variable                   | Descripcion breve                                       | Valor por defecto | Valores que puede recibir         |
|----------------------------|---------------------------------------------------------|-------------------|-----------------------------------|
| `SUCCESS_APP_PREFIX`       | Prefijo global para rutas/nombres de la app en Success. | vacio             | texto (incluyendo vacio)          |
| `SUCCESS_DEBUG_CONSOLE`    | Activa mensajes de depuracion en consola del framework. | `True`            | `True` o `False`                  |
| `SUCCESS_STAGING`          | Marca ejecucion en entorno staging.                     | `False`           | `True` o `False`                  |
| `SUCCESS_TESTING`          | Marca ejecucion en entorno de pruebas.                  | `False`           | `True` o `False`                  |
| `SUCCESS_STRICT_SLASHES`   | Controla el comportamiento de barras finales en rutas.  | `False`           | `True` o `False`                  |
| `SUCCESS_MAIN_APP`         | Nombre de la app principal del ecosistema Success.      | `"app_name"`      | nombre de app existente           |
| `SUCCESS_SECONDARY_APPS`   | Lista de apps secundarias registradas.                  | Python List       | lista de nombres de app           |
| `SUCCESS_APPS_PATH`        | Directorio donde se ubican las apps.                    | `"apps"`          | ruta/directorio valido            |
| `SUCCESS_ALLOW_NO_MAIN_APP`| Permite iniciar sin app principal definida.             | `False`           | `True` o `False`                  |
| `SUCCESS_SAVE_MODE`        | Activa modo de guardado/control especial del framework. | `False`           | `True` o `False`                  |
| `SUCCESS_SHOW_SUMMARY`     | Muestra resumen de ejecucion/configuracion.             | `True`            | `True` o `False`                  |
| `SUCCESS_SUMMARY_LEVEL`    | Nivel de detalle del resumen mostrado.                  | `FULL`            | `NONE`, `BASIC`, `FULL`           |
| `SUCCESS_HUMOR_ENABLED`    | Activa respuestas/mensajes de humor en la capa Success. | `False`           | `True` o `False`                  |
| `SUCCESS_MOOD_LANG`        | Idioma usado para el modo humor/tono.                   | `'es'`            | codigo de idioma (ej. `es`, `en`) |
| `SUCCESS_APP_MAIN`         | Marca esta config como app principal.                   | `False`           | `True` o `False`                  |
| `SUCCESS_APP_TYPE`         | Tipo de despliegue de aplicaciones en Success.          | `"singleApp"`     | `singleApp`, `multiApp`           |
| `SUCCESS_APP_MODE`         | Modo de enrutado/ejecucion de apps.                     | `"subdomain"`     | `standard`, `path`, `subdomain`   |

## Ambito app (`apps/<app_name>/.env`)

| Variable                        | Descripcion breve                                   | Valor por defecto | Valores que puede recibir |
|---------------------------------|-----------------------------------------------------|-------------------|---------------------------|
| `SUCCESS_APP_PREFIX`            | Prefijo propio de la app para rutas/nombres.        | vacio             | texto (incluyendo vacio)  |
| `SUCCESS_DEBUG_CONSOLE`         | Activa depuracion en consola para la app.           | `True`            | `True` o `False`          |
| `SUCCESS_STAGING`               | Marca la app en entorno staging.                    | `False`           | `True` o `False`          |
| `SUCCESS_TESTING`               | Marca la app en entorno de pruebas.                 | `False`           | `True` o `False`          |
| `SUCCESS_STRICT_SLASHES`        | Control de slash final en rutas de la app.          | `False`           | `True` o `False`          |
| `SUCCESS_EXTENSION_ACL`         | Habilita extension ACL/permisos.                    | `True`            | `True` o `False`          |
| `SUCCESS_EXTENSION_ADMIN`       | Habilita extension de panel/admin.                  | `True`            | `True` o `False`          |
| `SUCCESS_EXTENSION_APSCHEDULER` | Habilita tareas programadas (APScheduler).          | `True`            | `True` o `False`          |
| `SUCCESS_EXTENSION_BABEL`       | Habilita internacionalizacion/localizacion (Babel). | `True`            | `True` o `False`          |
| `SUCCESS_EXTENSION_BLUEPRINT`   | Habilita soporte Blueprint modular.                 | `True`            | `True` o `False`          |
| `SUCCESS_EXTENSION_CACHE`       | Habilita capa de cache.                             | `True`            | `True` o `False`          |
| `SUCCESS_EXTENSION_CORS`        | Habilita gestion CORS.                              | `True`            | `True` o `False`          |
| `SUCCESS_EXTENSION_SQLALCHEMY`  | Habilita ORM SQLAlchemy.                            | `True`            | `True` o `False`          |
| `SUCCESS_EXTENSION_EMAIL`       | Habilita servicios de correo.                       | `True`            | `True` o `False`          |
| `SUCCESS_EXTENSION_JWT`         | Habilita autenticacion JWT.                         | `True`            | `True` o `False`          |
| `SUCCESS_EXTENSION_LIMITER`     | Habilita rate limiting.                             | `True`            | `True` o `False`          |
| `SUCCESS_EXTENSION_LOGGER`      | Habilita sistema de logging.                        | `True`            | `True` o `False`          |
| `SUCCESS_EXTENSION_LOGGIN`      | Flag adicional de logging definido en la app.       | `False`           | `True` o `False`          |
| `SUCCESS_EXTENSION_MARSHMALLOW` | Habilita serializacion/validacion (Marshmallow).    | `True`            | `True` o `False`          |
| `SUCCESS_EXTENSION_MIGRATE`     | Habilita migraciones de base de datos.              | `True`            | `True` o `False`          |
| `SUCCESS_EXTENSION_REDIS`       | Habilita integracion Redis.                         | `True`            | `True` o `False`          |
| `SUCCESS_EXTENSION_RESTFUL`     | Habilita soporte RESTful.                           | `True`            | `True` o `False`          |
| `SUCCESS_EXTENSION_SECURITY`    | Habilita capa de seguridad adicional.               | `False`           | `True` o `False`          |
| `SUCCESS_EXTENSION_SESSION`     | Habilita gestion de sesiones.                       | `True`            | `True` o `False`          |
| `SUCCESS_EXTENSION_UPLOADS`     | Habilita gestion de uploads/archivos.               | `True`            | `True` o `False`          |
| `SUCCESS_OUTPUT_MODEL`          | Activa macro de salida/modelo personalizada.        | `True`            | `True` o `False`          |
| `SUCCESS_OUTPUT_MODEL_CLASS`    | Clase Python para output model personalizado.       | vacio | import path de clase (texto) o vacio |
| `SUCCESS_TABLENAME_MODEL`       | Activa macro para modelado por nombre de tabla DB.  | `True`            | `True` o `False`          |
| `SUCCESS_ENABLE_CLI`            | Habilita CLI interno de la app.                     | `False`           | `True` o `False`          |
| `SUCCESS_ENABLE_GRAPHQL`        | Habilita endpoints GraphQL.                         | `False`           | `True` o `False`          |
| `SUCCESS_ENABLE_REST`           | Habilita endpoints REST.                            | `True`            | `True` o `False`          |
| `SUCCESS_ENABLE_RPC`            | Habilita endpoints RPC.                             | `False`           | `True` o `False`          |
| `SUCCESS_ENABLE_SSE`            | Habilita Server-Sent Events.                        | `False`           | `True` o `False`          |
| `SUCCESS_ENABLE_SOAP`           | Habilita endpoints SOAP.                            | `False`           | `True` o `False`          |
| `SUCCESS_ENABLE_VIEW`           | Habilita vistas/plantillas.                         | `True`            | `True` o `False`          |
| `SUCCESS_ENABLE_WEB_SOCKET`     | Habilita WebSocket.                                 | `False`           | `True` o `False`          |
| `SUCCESS_CUSTOM_CONFIG_CLASS`   | Clase de configuracion personalizada para la app.   | vacio | import path de clase (texto) o vacio |
| `SUCCESS_SAVE_MODE`             | Activa modo de guardado/control especial de la app. | `False`           | `True` o `False`          |
| `SUCCESS_HOST_MATCHING`         | Activa host matching en el enrutador.               | `True`            | `True` o `False`          |
| `SUCCESS_SUBDOMAIN_MATCHING`    | Activa resolucion por subdominios.                  | `True`            | `True` o `False`          |
