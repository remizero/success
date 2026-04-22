# Schemas in Success. 📐

Schemas define the validation and transformation of input data for an action.

In Success, schemas are consumed from `Input.py` and typically rely on Marshmallow.

---

## Getting started.

[Template](#template)

---

## Table of contents. 📑

* [What is a schema](#what-is-a-schema)
* [Where to place it](#where-to-place-it)
* [Template](#template)
* [Real examples](#real-examples)
* [Best practices](#best-practices)
* [Next step](#next-step)

---

## What is a schema.

A schema validates and normalizes incoming data before it reaches the controller.

If validation fails:

* `Input` adds errors to `_errors`,
* `SuccessOutput` generates a validation response (`input_error`).

---

## Where to place it.

```bash
apps/<app>/services/<protocol>/<service>/<version>/<module>/[<submodule>]/<action>/Schema.py
```

---

## Template.

```python
from marshmallow import Schema as MarshmallowSchema, fields

class Schema(MarshmallowSchema):
  name = fields.Str(required=True)
```

---

## Real examples.

### Flexible schema (allows extra fields)

```python
from marshmallow import INCLUDE
from marshmallow import Schema as MarshmallowSchema

class Schema(MarshmallowSchema):
  class Meta:
    unknown = INCLUDE
```

### Strict schema (required field)

```python
from marshmallow import fields
from marshmallow import Schema as MarshmallowSchema

class Schema(MarshmallowSchema):
  name = fields.Str(required=True, error_messages={"required": "The tenant name is required."})
```

---

## Best practices.

* Declare only the fields needed for the action.
* Use clear error messages.
* Avoid business logic in the schema.
* Version the schema alongside the action (`v1`, `v2`).

---

## Next step. 🔗

[RESPONSE.md](RESPONSE.md)
