# 🌟 Guía Oficial para Crear una Extensión Personalizada en Success

Esta guía te muestra paso a paso cómo crear y registrar una extensión personalizada para el framework **Success**, utilizando el contrato oficial `SuccessExtension` y su ciclo de vida controlado.

---

## ✅ Requisitos Previos

* Tener una aplicación creada usando Success Framework
* Estructura base de carpetas correctamente configurada
* Haber definido en `extensions.json` o `extensions.yaml` las extensiones personalizadas (como se explica más abajo)

---

## ⚙️ Contrato Oficial: `SuccessExtension`

```python
from flask import Flask
from success.common.base.SuccessClass import SuccessClass

class SuccessExtension(SuccessClass):

    _extension = None
    _app: Flask = None

    def __init__(self, app: Flask) -> None:
        super().__init__()
        self._app = app

    def userConfig(self, **kwargs) -> None:
        self._app.config.update(kwargs)

    def register(self) -> None:
        if self._extension and hasattr(self._extension, "init_app"):
            self._extension.init_app(self._app)
        else:
            raise RuntimeError(
                f"La extensión {self.__class__.__name__} no define correctamente 'self._extension' o no implementa 'init_app'"
            )
```

---

## 📚 Ejemplo: `RateLimiterExtension`

### ✂ Paso 1: Implementar la extensión personalizada

```python
from flask_limiter import Limiter
from success.engine.extensions.SuccessExtension import SuccessExtension

class RateLimiterExtension(SuccessExtension):

    def __init__(self, app):
        super().__init__(app)
        self._extension = Limiter()
```

> ✉️ *Puedes sobreescribir `userConfig()` o `register()` si necesitas una lógica personalizada.*

---

## 📂 Declaración en `extensions.json`

```json
{
  "extensions": [
    {
      "class": "apps.infrastructure.prueba.extensions.rate_limiter.RateLimiterExtension",
      "enabled": true,
      "config": {
        "RATELIMIT_DEFAULT": "100 per minute",
        "RATELIMIT_SCOPE": "ip"
      }
    }
  ]
}
```

> El archivo debe ubicarse en la ruta: `apps/infrastructure/<service>/<version>/<module>/extensions/extensions.json`

---

## ⚡️ Flujo de Carga Interno

El `SuccessExtensionsDiscoverer` detecta, importa y registra todas las extensiones personalizadas:

```python
instance = ExtensionClass(self.__app)
instance.userConfig(**config)
instance.register()
SuccessContext().setExtension(ExtensionClass.__name__, instance)
```

---

## 🔧 Tips para Desarrolladores

* El atributo `_extension` debe apuntar a una instancia de la librería deseada
* `init_app(app)` es la forma canónica de integrarla con Flask
* Las variables declaradas en `config` se inyectan automáticamente
* Las extensiones se pueden reutilizar, versionar y aislar por módulo

---

## ✨ Beneficios de esta arquitectura

* 🔄 Ciclo de vida controlado (instancia, config, registro)
* 🤝 Unificación de extensiones propias y nativas
* 🌟 Mínima fricción para el desarrollador
* 🌐 Configuración declarativa por archivo `json/yaml`

---

## 💪 Estándar recomendado de Success

**Si no sabes cómo implementar una extensión, usa este contrato. Success hará todo el trabajo pesado por ti.**
