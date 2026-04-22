# Hooks advanced en Success. 🧬

Esta guía cubre capacidades advanceds del sistema de hooks: matching jerárquico, prioridades y diseño de callbacks robustos.

---

## Get started now.

[Matching jerárquico](#matching-jerárquico)

---

## Table of contents. 📑

* [Matching jerárquico](#matching-jerárquico)
* [Prioridad y orden de ejecución](#prioridad-y-orden-de-ejecución)
* [Firma del callback](#firma-del-callback)
* [Contexto de ejecución](#contexto-de-ejecución)
* [Ejemplo avanzado](#ejemplo-avanzado)
* [Checklist de seguridad](#checklist-de-seguridad)
* [Next step](#paso-siguiente)

---

## Matching jerárquico.

Si se emite:

```txt
build:endpoint:adapter:register
```

También hacen match declaraciones más generales:

* `build:endpoint:adapter:register`
* `build:endpoint:adapter`
* `build:endpoint`
* `build`

Esto permite hooks transversales por nivel de granularidad.

---

## Prioridad y orden de ejecución.

`priority` define orden ascendente:

* menor número = se ejecuta primero,
* mayor número = se ejecuta después.

---

## Firma del callback.

Success soporta callbacks con:

* 0 parámetros,
* 1 parámetro (`context`),
* o más (`context`, `**kwargs`).

Recomendado:

```python
def beforeEndpointCreate(self, context: dict, **kwargs):
  ...
```

---

## Contexto de ejecución.

`context` incluye:

* `hook`
* `declaration`
* `payload`
* `when`
* `action`
* `action_hierarchy`
* `kwargs`

---

## Ejemplo avanzado.

```json
[
  {
    "name": "endpoint_adapter_before",
    "when": "before",
    "action": "build:endpoint:adapter:register",
    "callback": "apps.synthetos.infrastructure.hooks.EndpointHooks.beforeEndpointAdapterRegister",
    "priority": 50,
    "payload": {
      "validate_protocol": true
    }
  }
]
```

---

## Checklist de seguridad.

* ¿El callback pertenece a una clase que hereda de `SuccessHook`?
* ¿La acción está definida en `SuccessHookCatalog`?
* ¿El hook tolera errores y no rompe el build completo?
* ¿El `payload` no incluye secretos sensibles?

---

## Next step. 🔗

[EXTENSIONS_AVANZADOS.md](EXTENSIONS_AVANZADOS.md)
