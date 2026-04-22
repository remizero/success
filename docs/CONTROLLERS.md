# Controllers in Success. 🎮

In Success, the controller orchestrates the business logic of an action.

It receives a `payload` already validated by `Input`, executes the main operation, and returns a `dict` compatible with `Output`.

---

## Get started now.

[Template](#template)

---

## Table of contents. 📑

* [What is a controller](#what-is-a-controller)
* [Base contract](#base-contract)
* [Real example](#real-example)
* [Recommended return format](#recommended-return-format)
* [Best practices](#best-practices)
* [Manual](#manual)
* [Template](#template)
* [CLI](#cli)
* [Next step](#next-step)

---

## What is a controller.

A controller in Success:

* Does not parse HTTP requests directly.
* Does not serialize the final response.
* Does not know transport details (`view`, `restful`).
* Focuses on business rules.

---

## Base contract.

All controllers must inherit from `SuccessController`.

```python
from success.engine.infrastructure.SuccessController import SuccessController

class MyController ( SuccessController ) :

  def fetch ( self, payload : dict ) -> dict :
    return {
      "status" : 200,
      "body"   : { "ok" : True }
    }
```

Notes:

- The method name (`fetch`) must match `self._controllerMethod` in the `Action`.
- In `view`, `body` will be the context used by the template.

In RESTFUL, `SuccessOutput` automatically applies `DefaultIntent`.

---

## Real example.

`apps/example/modules/chromadb/v1/admin/controllers/PublicApi.py`:

```python
class PublicApi ( SuccessController ) :

  def fetch ( self, payload : dict ) -> dict :
    # external query
    return {
      "status" : 200,
      "body"   : {
        "source" : "https://jsonplaceholder.typicode.com/todos/1",
        "data"   : {}
      }
    }
```

---

## Recommended return format.

### Success

```python
{
  "status"  : 200,
  "message" : "OK",
  "body"    : {...}
}
```

### Business/controller error

```python
{
  "status" : 500,
  "error"  : "Error description",
  "type"   : "controller",
  "code"   : "CONTROLLER_ERROR"
}
```

---

## Best practices.

* Use explicit methods (`load`, `fetch`, `create`, `update`, `delete`).
* Maintain homogeneous returns (`status`, `message`, `body` / `error`).
* Avoid parsing or validation logic here.
* Extract complex external integrations to `infrastructure/` when applicable.

---

## Manual. (optional) 🛠️

To better understand how a Success controller works, its structure, or to customize it from scratch, these are the steps to build a Success action controller from the ground up.

```python
from success.engine.infrastructure.SuccessController import SuccessController

class <ControllerName> ( SuccessController ) :

  def <method> ( self, payload : dict ) -> dict :
    # business logic
    return {
      "status"  : 200,
      "message" : "Operation successful",
      "body"    : {}
    }
```

---

## Template.

The fastest way to get started is by copying the `controller` template included in the Success examples directory:

  ```bash
    cp -r examples/controller.py path/<my_project>/apps/<my_app>/modules/<service>/v1/<my_module>/controllers/<my_controller.py>
  ```

---

## CLI. 🖥️

> Available in upcoming versions.

  ```bash
    success create-controller path/my_controller
  ```

---

## Advanced configuration. 🛠️

[CONTROLLERS_AVANZADOS.md](CONTROLLERS_AVANZADOS.md) – advanced controller patterns, fallback, pre-hooks, and scalable design.

---

## Next step. 🔗

[OUTPUT.md](OUTPUT.md)
