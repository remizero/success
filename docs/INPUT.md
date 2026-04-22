# Input in Success. 📥

`Input.py` is responsible for parsing and validating request data before executing the controller.

It is the entry point of the action pipeline.

---

## Get started now.

[Template](#template)

---

## Table of contents. 📑

* [Input responsibility](#input-responsibility)
* [Internal flow](#internal-flow)
* [Best practices](#best-practices)
* [Manual](#manual)
* [Template](#template)
* [CLI](#cli)
* [Next step](#next-step)

---

## Input responsibility.

`Input` must:

* parse request (`args`, JSON, form),
* validate with `Schema`,
* expose `_validatedData`,
* register errors in `_errors`.

---

## Internal flow.

1. `parse()` encapsulates and calls `_parseInput()`.
2. `validate()` executes `self._schema.load(self._rawData)` using `marshmallow`.
3. If there is an error, it accumulates messages in `_errors`.


### Best practices.

* Return `self` in `parse()` and `validate()` to be used in chain of responsibility.
* Keep validation declarative in Schema.
* Do not execute business logic in `Input`.
* Log parsing/validation errors for diagnosis.

---

## Manual. (optional) 🛠️

To better understand how a Success action Input works, its structure, or to customize it from scratch, these are the steps to build a Success action Input from the ground up.

```python
from marshmallow.exceptions         import ValidationError
from success.engine.io.SuccessInput import SuccessInput
from .Schema                        import Schema

class Input ( SuccessInput ) :

  def __init__ ( self ) :
    super ().__init__ ()
    self._schema = Schema ()

  def parse ( self ) :
    self._parseInput ()
    return self

  def validate ( self ) :
    try :
      self._validatedData = self._schema.load ( self._rawData )

    except ValidationError as e :
      self._errors.extend ( [f"{k}: {', '.join ( v )}" for k, v in e.messages.items ()] )

    return self
```

---

## Template.

If you're coming from ACTIONS.md, you've already done this step by copying the complete action template.

---

## CLI. 🖥️

> Available in upcoming versions.

---

## Next step. 🔗

[CONTROLLERS.md](CONTROLLERS.md)
