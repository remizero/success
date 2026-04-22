# Convenciones, Patrones y Contratos en Success

Esta guía documenta las convenciones que ya se usan en el código de `success/` y `apps/example`.

> NOTA: Desde Success reconocemos que todas estas convenciones, nomenclaturas, patrones y contratos contrastan con las convenciones Python, pero estamos convencidos que permiten una mayor claridad en el código.

¿Por qué NO seguimos PEP8?

- Porque priorizamos alineación visual para lectura estructural.
- Porque el código representa contratos, no scripts.
- Porque favorecemos consistencia interna sobre estándar externo.

---

## Empezar ahora.

¿Quieres una versión rápida?

👉 [Checklist operativo](#checklist-operativo)

---

## Tabla de contenido.

* [Objetivo y alcance](#objetivo-y-alcance)
* [Arquitectura base (patrón Action Pipeline)](#arquitectura-base-patrón-action-pipeline)
* [Convención de estructura de directorios](#convención-de-estructura-de-directorios)
* [Contrato de una Action](#contrato-de-una-action)
* [Contrato de Input / Schema](#contrato-de-input--schema)
* [Contrato de Controller](#contrato-de-controller)
* [Contrato de Output / Response](#contrato-de-output--response)
* [Contratos declarativos JSON](#contratos-declarativos-json)
* [Contrato de Hooks](#contrato-de-hooks)
* [Contrato de Extensions](#contrato-de-extensions)
* [Convenciones transversales de código](#convenciones-transversales-de-código)
* [Diferencias observadas entre apps/example y apps/synthetos](#diferencias-observadas-entre-appsexample-y-appssynthetos)
* [Checklist operativo](#checklist-operativo)

---

## Objetivo y alcance.

Este documento describe convenciones definidas en Success:

* `success/` (núcleo del framework)
* `apps/example` (app de referencia)

---

## Arquitectura base (patrón Action Pipeline).

El patrón central en Success es un pipeline por acción:

`Request -> preInput (policies) -> Input.parse -> Input.validate -> Controller.execute -> Output.presenter -> Response.response`

Contratos del pipeline:

* `SuccessAction.execute()` orquesta todo y decide si la fuente del payload es `INPUT` o `CONTROLLER`.
* `SuccessPreInputPolicy` puede bloquear antes de parsear input.
* `SuccessOutput.normalize()` transforma a un formato canónico homogéneo.
* `SuccessResponse.response()` exige que haya `outputModel` e `intent` definidos.

---

## Convención de estructura de directorios.

### Patrón general por servicio/acción

```text
apps/<app>/services/<protocol>/<service>/<version>/<module>/[<submodule>]/<action>/
```

Ejemplos reales:

* `apps/example/services/view/chromadb/v1/admin/hello/`
* `apps/example/services/restful/chromadb/v1/admin/public/get/`
* `apps/synthetos/services/restful/chromadb/v1/admin/tenant/create/`

### Controladores

```text
apps/<app>/modules/<service>/<version>/<module>/controllers/<Controller>.py
```

Ejemplos:

* `apps/example/modules/chromadb/v1/admin/controllers/Hello.py`
* `apps/synthetos/modules/chromadb/v1/controllers/Tenant.py`

---

## Contrato de una Action.

Una acción concreta hereda según protocolo:

* `SuccessViewAction` para `view`
* `SuccessRestfulAction` para `restful`

Convenciones observadas:

* Clase se llama siempre `Action`.
* Constructor inyecta explícitamente: `Input`, `Output`/`SuccessOutput`, `Response`, `Controller`.
* Método HTTP (`get`, `post`, etc.) llama `self.execute("<controller_method>")`.

Ejemplos:

* View: `hello.Action.get -> execute("load")`
* Restful: `public/get.Action.get -> execute("fetch")`
* Restful: `tenant/create.Action.post -> execute("create")`

Convención de seguridad en acciones:

* Se puede declarar `policySpec()` por acción (ej. `tenant/create/Action.py`).
* En modo `SUCCESS_POLICY_MODE=strict`, una acción no pública sin `policySpec` explícito puede ser denegada.

---

## Contrato de Input / Schema.

`Input` hereda de `SuccessInput` e implementa:

* `parse()`: normalmente llama `self._parseInput()`, puede ser sobre escrito para extender el flujo de análisis por uno más profundo y personalizado.
* Se guarda esquema en `self._schema = Schema()`.
* `validate()`: normalmente ejecuta `self._schema.load(self._rawData)`
* Los errores se agregan en `self._errors`.
* Retorna `self` para chain of responsibility (`parse().validate()`).

`SuccessInput._parseInput()` define contrato HTTP:

* `GET` -> `request.args`
* `POST/PUT/PATCH` -> JSON o `form`
* `DELETE` -> query + JSON si existe

Schema:

* Implementado con Marshmallow.
* En ejemplos básicos se usa `unknown = INCLUDE`.
* En `synthetos` hay validación explícita de campos (`name` requerido en create tenant).

---

## Contrato de Controller.

Todo controller hereda de `SuccessController`.

Contrato:

* Métodos públicos (no privados) son invocables por `execute(method, payload)`.
* Cada método recibe `payload: dict`.
* Debe devolver `dict` compatible con Output.

Formato de retorno recomendado (observado):

* Éxito: `{"status": <int>, "message": <str opcional>, "body": <data>}`
* Error: `{"status": <int>, "error": <str>, ...}`

Convención práctica:

* Método del controller debe existir y coincidir con string usado en `Action.execute(...)`.

---

## Contrato de Output / Response.

`SuccessOutput` normaliza a formato canónico:

* `kind`: `success | input_error | controller_error`
* `success`: bool
* `status`, `message`, `data`, `error`

Resolución de intent:

* `RESTFUL` -> `DefaultIntent`
* `VIEW` -> `RenderIntent` (si hay template) o `RedirectIntent` (si aplica)

`Action._outputSpec` controla:

* `protocol`
* `template`
* `redirect_to`
* `fallback_redirect`

`Response`:

* Suele heredar de `SuccessResponse`.
* En views puede incluir policy específica (`SuccessResponsePolicy`) para `content_type` HTML.

---

## Contratos declarativos JSON.

### `blueprints.json`

Contrato base por entrada:

* `id`
* `module.name`
* `module.path.protocol`
* `module.path.service`
* `module.path.version`
* `url_prefix` (habitual)
* `module.path.actions` (opcional en algunos casos restful)

Patrón observado:

* `id` de blueprint es referenciado por endpoints mediante `blueprint_id`.

### `endpoints.json`

Contrato varía por protocolo:

Para `view`:

* `endpoint_id`
* `protocol: "view"`
* `blueprint_id`
* `rule`
* `action`
* `action_name`
* `methods` (default GET si no se define)
* `host` (opcional/útil en modo subdomain)

Para `restful`:

* `endpoint_id`
* `protocol: "restful"`
* `blueprint_id`
* `resource`
* `urls`
* `endpoint`
* `host` (opcional)

Convención de referencia:

* `action` / `resource` suelen declararse como path tipo `apps/<app>/services/...`.

### Naming semántico generado

Los blueprints se nombran automáticamente con patrón:

`apps_<app>_services_<protocol>_<service>_<version>_<module>_<id>`

Esto impacta en `url_for(...)` (ejemplo real en templates de `synthetos`).

---

## Contrato de Hooks.

Declaración en `hooks.json` por entrada:

* `name`
* `when`: `before | after`
* `action`: acción del catálogo (`SuccessHookCatalog`)
* `callback`: `module.Class.method`
* `enabled` (default `true`)
* `priority` (default `100`; menor valor = mayor prioridad)
* `payload` (dict opcional)

Contrato de implementación:

* Clase del callback debe heredar de `SuccessHook`.
* Método callback debe ser callable.
* Matching de acciones soporta jerarquía (una acción padre puede capturar eventos hijos).

Patrón en código:

* `SuccessHookManager.register()` valida, ordena por prioridad y registra.
* `execute()` arma `context` estándar para callback.

---

## Contrato de Extensions.

### Extensiones core

Se cargan por flags de entorno `SUCCESS_EXTENSION_*` vía `SuccessExtensionsLoader`.

### Extensiones custom (`extensions.json`)

Contrato observado:

* `class`: path completo a clase
* `enabled`: bool
* `config`: dict

Implementación:

* Clase debe heredar de `SuccessExtension`.
* Flujo: `userConfig(**config)` -> `register()`.

Nota importante:

* En el discoverer actual, `config` vacío se considera inválido (se loguea error y se omite extensión).

---

## Convenciones transversales de código.

Convenciones recurrentes en `success/` y apps:

* Bloques de imports comentados en orden:
  * `# Python Libraries`
  * `# Success Libraries`
  * `# Application Libraries`
  * `# Preconditions`
* Clases con Type Hints explícitos.
* Nombres de clases en `PascalCase`.
* Métodos y atributos en `snake_case`.
* Acciones y métodos de controlador con verbos claros (`load`, `fetch`, `create`).
* Organización por protocolo (`view` / `restful`) y versión (`v1`, etc.).

---

## Diferencias observadas entre apps/example y apps/synthetos.

`apps/example`:

* Referencia mínima de patrón Action/Input/Output/Response/Schema.
* `hooks.json` vacío.
* `extensions.json` con una extensión custom declarada.

`apps/synthetos`:

* Usa `policySpec()` en endpoint sensible (`tenant/create`).
* Tiene hooks declarados con acciones del build pipeline.
* Usa templates más completos y endpoint naming generado en `url_for`.
* Controllers con integración externa (Chroma API) y persistencia local (`storage/tenants.json`).

---

## Checklist operativo.

Si quieres mantener consistencia con Success:

1. Crea acciones bajo `services/<protocol>/<service>/<version>/<module>/<action>/`.
2. Mantén set mínimo de archivos de acción: `Action.py`, `Input.py`, `Response.py` (+ `Output.py`, `Schema.py` según necesidad).
3. Asegura que `Action.execute("<method>")` coincida con método público existente del controller.
4. Retorna desde controller estructuras con `status` + `body` (éxito) o `error` (fallo).
5. Declara correctamente `blueprints.json` y `endpoints.json` según protocolo.
6. Si usas hooks, respeta `when/action/callback` y hereda de `SuccessHook`.
7. Si usas extensiones custom, hereda de `SuccessExtension` y provee `config` no vacío.
8. En endpoints sensibles, define `policySpec()` explícito para compatibilidad con modo estricto.

---

## Otras convenciones.

### Imports.
Para la definición de imports dentro de una clase se aplica la siguiente convención.

```python
# Python Libraries / Librerías Python
from flask                 import json
from flask                 import request
from flask                 import Response
from flask_restful         import Resource
from http                  import HTTPStatus
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

# Success Libraries / Librerías Success
from success.common.base.SuccessClass                 import SuccessClass
from success.engine.context.SuccessPolicies           import SuccessPolicies
from success.engine.io.SuccessOutput                  import SuccessOutput
from success.engine.infrastructure.SuccessController  import SuccessController
from success.engine.io.SuccessInput                   import SuccessInput
from success.common.types.SuccessPayloadSource        import SuccessPayloadSource
from success.common.types.SuccessProtocol             import SuccessProtocol
from success.engine.context.SuccessResponse           import SuccessResponse
from success.engine.io.SuccessActionOutputSpec        import SuccessActionOutputSpec

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones
```

---

### Definición de clase.

Para la definición de clases se utiliza la siguiente nomencatura y convención.

```python
class SuccessAction ( SuccessAction ) :
```

---

### Definición de atributos de clase.

Para la definición de atributos de clases se utiliza la siguiente nomencatura y convención.

```python
class SuccessAction ( SuccessAction ) :

  _controller        : SuccessController       = None
  _input             : SuccessInput            = None
  _output            : SuccessOutput           = None
  _policies          : SuccessPolicies         = None
  _response          : SuccessResponse         = None
  _controllerMethod  : str                     = None
  _outputSpec        : SuccessActionOutputSpec = None
```

---

### Definición de métodos de clase.

```python
def execute ( self, method : str ) -> Response :
```

---

### Definición de atributos de instancia.

```python
class SuccessAction ( SuccessAction ) :

  def __init__ ( self ) -> None :
    super ().__init__ ()
    self._controller        = None
    self._input             = None
    self._output            = None
    self._policies          = None
    self._response          = None
    self._controllerMethod  = None
    self._outputSpec        = None
```

---

### Asignación de valores a atributos de instancia.

```python
  self._input      = _input
  self._output     = _output
  self._controller = _controller
  self._response   = _response
  self._policies   = _policies or SuccessPolicies ()
  self._outputSpec = SuccessActionOutputSpec ()
```

---

### Otras definiciones.

#### Dicts

Para definir estructuras tipo dict se utiliza una identación y alineación especial.

```json
{
  "atribute_1"       : "value_1",
  "atribute_2"       : "value_2",
  "longest_atribute" : "value"
}
```
