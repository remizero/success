# Blueprints in Success 📌

In Success, blueprints define how each module is organized and exposed within an application. Each blueprint connects a module with a URL prefix and defines its internal path based on the protocol, service, and available actions.

> Note: The values shown are test data from the quickstarter_1 example.

---

## Get started now.

[Template](#template)

---

## Table of contents. 📑

* [General structure of a blueprint](#general-structure-of-a-blueprint)
* [Detailed fields](#detailed-fields)
* [Blueprint examples](#blueprint-examples)
* [Best practices](#best-practices)
* [Next step](#next-step)

---

## General structure of a blueprint. 🏗️

Each blueprint is defined as a JSON object with the following structure:

  ```json
    {
      "id": "<blueprint identifier>",
      "module": {
        "name": "<module name>",
        "path": {
          "protocol": "<transport type: view | restful | rpc | etc.>",
          "service": "<associated service>",
          "version": "<service version>",
          "submodule": "<optional submodule>",
          "actions": "<main module action>"
        }
      },
      "url_prefix": "<blueprint URL prefix>"
    }
  ```

---

## Detailed fields 📝
| Field                   | Description                                                                        | Optional |
| ----------------------- | ---------------------------------------------------------------------------------- | -------- |
| `id`                    | Unique identifier of the blueprint within the application.                         | No       |
| `module.name`           | Name of the module associated with the blueprint.                                  | No       |
| `module.path.protocol`  | Defines the transport type used by the module: `view`, `restful`, `rpc`, etc.      | No       |
| `module.path.service`   | Main service the module connects to.                                               | No       |
| `module.path.version`   | Version of the service being used.                                                 | No       |
| `module.path.submodule` | Internal submodule within the main module.                                         | Yes      |
| `module.path.actions`   | Action or set of actions exposed by the module.                                    | No       |
| `url_prefix`            | URL prefix that serves as the entry point to the blueprint.                        | No       |

---

## Blueprint examples.

  ```json
    [
      {
        "id": "hello_view",
        "module": {
          "name": "render",
          "path": {
            "protocol": "view",
            "service": "simple_view",
            "version": "v1",
            "actions": "hello"
          }
        },
        "url_prefix": "/hello"
      },
      {
        "id": "public_rest",
        "module": {
          "name": "public",
          "path": {
            "protocol": "restful",
            "service": "simple_restful",
            "version": "v1",
            "actions": "get"
          }
        },
        "url_prefix": "/public"
      }
    ]
  ```

> In this example, hello_view is exposed as a view (view) while public_rest is exposed as a REST API (restful), each using its corresponding service.

---

## Best practices.

* Keep the id unique for each blueprint within the application.
* Use submodule only when you need to organize internal hierarchies.
* URL prefixes (url_prefix) must be consistent with the app's architecture and avoid overlaps.
* Define the protocol based on the nature of the blueprint: view for web interfaces, restful for APIs, rpc for remote procedures.

---

## Advanced configuration. 🛠️

[BLUEPRINTS_AVANZADOS.md](BLUEPRINTS_AVANZADOS.md) – advanced documentation and real-world configuration cases.

---

## Next step. 🔗

[ENDPOINTS.md](ENDPOINTS.md)
