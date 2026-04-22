# Response in Success. 📬

`Response.py` builds the final Flask response using the already normalized output and the response policies.

It is the last stage of an action's pipeline.

---

## Getting started.

[Template](#template)

---

## Table of contents. 📑

* [Response responsibility](#response-responsibility)
* [Base template](#base-template)
* [Custom policies](#custom-policies)
* [Real examples](#real-examples)
* [Best practices](#best-practices)
* [Next step](#next-step)

---

## Response responsibility.

`SuccessResponse`:

* takes `SuccessOutput`,
* executes `outputModel.build(...)`,
* applies `postOutput` policies,
* executes the `intent` to generate the Flask response.

---

## Base template.

```python
from success.engine.context.SuccessResponse import SuccessResponse

class Response(SuccessResponse):

  def __init__(self):
    super().__init__()
```

---

## Custom policies.

You can customize mime type, status, and content-type with `SuccessResponsePolicy`.

```python
from success.engine.context.SuccessResponse       import SuccessResponse
from success.engine.context.SuccessResponsePolicy import SuccessResponsePolicy

class HtmlPolicy ( SuccessResponsePolicy ) :
  def definitions ( self ) :
    self._default_mimetype = "text/html"
    self._default_status   = 200
    self._charset          = "utf-8"
    self._content_type     = "text/html; charset=utf-8"

class Response ( SuccessResponse ) :
  def __init__ ( self ) :
    super ().__init__ ( HtmlPolicy () )
```

---

## Real examples.

* REST APIs in `apps/example` use the base `Response`.
* HTML views (`hello`, `dashboard`) use a custom `SuccessResponsePolicy` for `text/html`.

---

## Best practices.

* Customize the policy only when necessary.
* Keep headers/cookies in the output/policy layer.
* Do not duplicate business logic in `Response`.

---

## Next step. 🔗

[EXTENSIONS.md](EXTENSIONS.md)
