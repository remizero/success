# Hooks in Success. 🪝

Hooks allow intercepting internal events of the Success build cycle to execute additional logic before or after key actions.

They are declared in `hooks.json` per application.

---

## Get started now.

[Template](#template)

---

## Table of contents. 📑

* [What is a hook](#what-is-a-hook)
* [The hooks.json contract](#the-hooksjson-contract)
* [Template](#template)
* [Detailed fields](#detailed-fields)
* [Catalog actions](#catalog-actions)
* [Real example](#real-example)
* [Best practices](#best-practices)
* [Next step](#next-step)

---

## What is a hook.

A hook is a behavior extension for internal events such as:

* config loading,
* extension loading,
* blueprint construction,
* endpoint registration.

---

## The hooks.json contract.

Expected root: JSON list.

Each hook defines:

* when it executes (`before` or `after`),
* which action it observes (`build:...`),
* which callback it runs (`package.Class.method`).

---

## Template.

```json
[
  {
    "name": "endpoint_any_before",
    "when": "before",
    "action": "build:endpoint",
    "callback": "apps.my_app.infrastructure.hooks.EndpointHooks.beforeAny",
    "enabled": true,
    "priority": 100,
    "payload": {
      "trace": true
    }
  }
]
```

---

## Detailed fields.

| Field      | Description                                          | Optional |
| ---------- | ---------------------------------------------------- | -------- |
| `name`     | Hook name.                                           | Yes      |
| `when`     | Execution timing: `before` or `after`.               | No       |
| `action`   | Semantic action from the hook catalog.               | No       |
| `callback` | `package.Class.method` path.                         | No       |
| `enabled`  | Activates or deactivates the hook.                   | Yes      |
| `priority` | Execution order (lower value = higher priority).     | Yes      |
| `payload`  | Extra immutable data for the hook.                   | Yes      |

---

## Catalog actions.

Frequent actions:

* `build:app:config:load`
* `build:app:extensions:core_load`
* `build:app:blueprints:load`
* `build:blueprint:builder:create`
* `build:endpoint:builder:create`
* `build:endpoint:adapter:register`

---

## Real example.

`apps/synthetos/hooks.json`:

```json
[
  {
    "name": "app_config_before",
    "when": "before",
    "action": "build:app:config:load",
    "callback": "apps.synthetos.infrastructure.hooks.CoreHooks.beforeAppConfigLoad",
    "enabled": true,
    "priority": 100,
    "payload": {
      "trace": true
    }
  }
]
```

---

## Best practices.

* Use a semantic and stable `name`.
* Keep `payload` small and explicit.
* Use clear priorities to avoid ambiguous ordering.
* Avoid irreversible side effects in `before` hooks.

---

## Advanced configuration. 🛠️

[HOOKS_AVANZADOS.md](HOOKS_AVANZADOS.md) – hierarchical matching, callback signatures, and audit strategies.

---

## Next step. 🔗

[CONVENTIONS.md](CONVENTIONS.md)
