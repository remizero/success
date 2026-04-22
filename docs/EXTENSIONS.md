# Custom Extensions in Success. 🧩

In addition to the framework's core extensions, Success allows registering custom application extensions via `extensions.json`.

This section covers developer-owned extensions.

---

## Get started now.

[Template](#template)

---

## Table of contents. 📑

* [What is a custom extension](#what-is-a-custom-extension)
* [Base contract](#base-contract)
* [Template](#template)
* [Real example](#real-example)
* [The extensions.json file](#the-extensionsjson-file)
* [Best practices](#best-practices)
* [Next step](#next-step)

---

## What is a custom extension.

A custom extension is your own class that inherits from `SuccessExtension` and is initialized during the app build.

---

## Base contract.

```python
from flask import Flask
from success.common.base.SuccessExtension import SuccessExtension

class MyExtension(SuccessExtension):

  def __init__(self, app: Flask) -> None:
    super().__init__(app)
    self._extension = ...

  def config(self) -> None:
    # optional configuration
    pass
```

---

## Template.

Suggested path:

```bash
apps/<app>/infrastructure/<service>/<version>/<module>/extensions/<MyExtension>.py
```

Minimum content:

```python
from success.common.base.SuccessExtension import SuccessExtension

class MyExtension ( SuccessExtension ) :

  def __init__ ( self, app ) :
    super ().__init__ ( app )
    self._extension = ...
```

---

## Real example.

`RateLimiterExtension`:

```python
from flask_limiter                        import Limiter
from flask_limiter.util                   import get_remote_address
from success.common.base.SuccessExtension import SuccessExtension

class RateLimiterExtension ( SuccessExtension ) :

  def __init__ ( self, app ) :
    super ().__init__ ( app )
    self._extension = Limiter ( key_func = get_remote_address )
```

> NOTE:
> Environment variables must be declared in the application's .env file.
> Variables declared in `config` are injected automatically.

---

## The extensions.json file.

`apps/<app>/extensions.json`:

```json
[
  {
    "class": "apps.example.infrastructure.chromadb.v1.admin.extensions.RateLimiterExtension",
    "enabled": true,
    "config": {
      "RATELIMIT_DEFAULT": "100 per minute"
    }
  }
]
```

Fields:

* `class`   : full `package.Class` path.
* `enabled` : declarative flag.
* `config`  : configuration dictionary injected with `userConfig(**config)`.

---

## Best practices.

* Keep one extension per responsibility.
* Avoid business logic inside the extension.
* Use `config` for parameterization without hardcoding.
* Register unique class names to facilitate traceability.

---

## Advanced configuration. 🛠️

[EXTENSIONS_AVANZADOS.md](EXTENSIONS_AVANZADOS.md) – conditional loading, strong validation, and encapsulation patterns.

---

## Next step. 🔗

[HOOKS.md](HOOKS.md)
