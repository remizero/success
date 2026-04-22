# Output in Success. 📤

`Output.py` transforms the result from `Input` or `Controller` into a canonical format and defines the final response intent (`default`, `render`, `redirect`).

---

## Getting started.

[Template](#template)

---

## Table of contents. 📑

* [Output responsibility](#output-responsibility)
* [Canonical normalization](#canonical-normalization)
* [Real examples](#real-examples)
* [Intent and OutputSpec](#intent-and-outputspec)
* [Best practices](#best-practices)
* [Manual](#manual)
* [Template](#template)
* [CLI](#cli)
* [Next step](#next-step)

---

## Output responsibility.

`Output` is responsible for:

* normalizing the payload,
* selecting the output model,
* resolving the output intent,
* leaving the result ready for `Response`.

---

## Canonical normalization.

Based on the payload origin (`INPUT` or `CONTROLLER`), Success generates a standard structure with fields such as:

* `success`
* `status`
* `message`
* `data`
* `error`
* `kind`

---

## Real examples.

### RESTful

```python
class Output(SuccessOutput):
  def __init__(self):
    super().__init__()
    self._intent = DefaultIntent()
```

### View

```python
from success.engine.io.RenderIntent import RenderIntent

class Output(SuccessOutput):
  def __init__(self):
    super().__init__()
    self._intent = RenderIntent("hello.html")
```

---

## Intent and OutputSpec.

In `view` actions, you can also define the intent via `Action._outputSpec`:

* `template`
* `redirect_to`
* `fallback_redirect`

Success automatically resolves `render` or `redirect` based on success/error and configuration.

---

### How the intent is resolved.

`SuccessOutput._resolve_intent(outputSpec)` applies:

- If `protocol == RESTFUL` -> `DefaultIntent`.
- If `protocol == VIEW`:
  - if there is an error and a redirect is configured -> `RedirectIntent`.
  - if there is no error and a `template` exists -> `RenderIntent(template)`.
  - if there is no template and a redirect exists -> `RedirectIntent`.
  - fallback -> `DefaultIntent`.

---

### Available attributes in `SuccessActionOutputSpec`.

- `protocol` -> Defined by the parent class SuccessViewAction or SuccessRestfulAction.
- `template`
- `redirect`
- `redirect_to`
- `fallback_redirect`

Important:

- `redirect_to` and `fallback_redirect` must be endpoint names compatible with `url_for`.
- Do not use Python modules or file paths for redirect.

---

## Best practices.

* Keep controller output consistent.
* Use `DefaultIntent` for APIs.
* Use `RenderIntent` or `OutputSpec.template` for views.
* Avoid mixing domain transformation with response formatting.

---

## Manual. (optional) 🛠️

To better understand how a Success controller works, its structure, or how to customize it from scratch, these are the steps to build a Success action controller from the ground up.

```python
from success.engine.io.SuccessOutput import SuccessOutput
from success.engine.io.DefaultIntent import DefaultIntent

class Output ( SuccessOutput ) :

  def __init__ ( self ) :
    super ().__init__ ()
    self._intent = DefaultIntent ()
```

---

## Template.

The fastest way to get started is by copying the `output` template included in the Success examples directory:

  ```bash
    cp -r examples/Output.py path/my_project/apps/my_app/services/view/simple_view/v1/hello/render/<Output.py>
  ```

---

## CLI. 🖥️

> Available in upcoming versions.

  ```bash
    success create-output path
  ```

---

## Next step. 🔗

[SCHEMAS.md](SCHEMAS.md)
