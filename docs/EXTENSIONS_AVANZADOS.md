# Extensiones advanceds en Success. ⚙️

Esta guía cubre estrategias advanceds para extensiones personalizadas: encapsulación de librerías externas, defaults de políticas y configuración por entorno.

---

## Get started now.

[Patrones](#patrones-advanced)

---

## Table of contents. 📑

* [Patrones advanced](#patrones-advanced)
* [Configuración robusta](#configuración-robusta)
* [Policy defaults](#policy-defaults)
* [Errores frecuentes](#errores-frecuentes)
* [Checklist de calidad](#checklist-de-calidad)
* [Next step](#paso-siguiente)

---

## Patrones advanced.

* Wrapper de librería externa.
* Extension + policy defaults para integración con `SuccessPreInputPolicy`.
* Configuración jerárquica por `config` + `.env`.

---

## Configuración robusta.

Flujo recomendado:

1. Instanciar `_extension` en `__init__`.
2. Resolver configuración en `config()`.
3. Registrar en `register()`.

Esto mantiene el ciclo de vida predecible y desacoplado.

---

## Policy defaults.

Una extensión puede contribuir políticas por defecto:

```python
def policyDefaults(self) -> dict:
  return {
    "require_jwt": False,
    "jwt_token_locations": ["cookies"]
  }
```

Estas políticas se integran en evaluación pre-input.

---

## Errores frecuentes.

* No asignar `self._extension`.
* Definir `class` mal en `extensions.json`.
* Inyectar `config` no-dict.
* Acoplar extensión con controladores o rutas concretas.

---

## Checklist de calidad.

* ¿La clase hereda de `SuccessExtension`?
* ¿`register()` puede ejecutar `init_app` correctamente?
* ¿La configuración es segura y parametrizable?
* ¿El comportamiento es testeable de forma aislada?

---

## Next step. 🔗

[HOOKS.md](HOOKS.md)
