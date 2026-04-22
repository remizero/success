# Endpoints in Success. 🎯

In Success, **endpoints** define how the actions of a module are exposed within a blueprint. Each endpoint is associated with a **protocol**, a **blueprint**, and a **specific action**, with URL rules and HTTP methods as applicable.

> Note: The values shown are test data from the `quickstarter_1` example.

---

## Getting started.

[Template](#template)

---

## Table of contents. 📑

* [General structure of an endpoint](#general-structure-of-an-endpoint)
* [Detailed fields](#detailed-fields)
* [Example of endpoints](#example-of-endpoints)
* [Best practices](#best-practices)
* [Advanced configuration](#advanced-configuration)
* [Next step](#next-step)

---

## General structure of an endpoint. 🏗️

Each endpoint is defined as a JSON object with the following structure:

```json
{
  "endpoint_id": "<endpoint identifier>",
  "protocol": "<transport type: view | restful | rpc | etc.>",
  "blueprint_id": "<id of the blueprint it belongs to>",
  "rule": "<URL rule (for view) or urls (for restful)>",
  "action": "<internal path to the action>",
  "action_name": "<name of the action>",
  "methods": ["<allowed HTTP methods>"],
  "host": "<optional host>"
}
```

> Note: For RESTful endpoints, instead of `rule`, `resource` and `urls` are used, and `endpoint` instead of `action_name`.

---

## Detailed fields. 📝

| Field          | Description                                                    | Optional |
| -------------- | -------------------------------------------------------------- | -------- |
| `endpoint_id`  | Unique identifier for the endpoint within the application.     | No       |
| `protocol`     | Defines the transport type: `view`, `restful`, `rpc`, etc.     | No       |
| `blueprint_id` | ID of the blueprint the endpoint belongs to.                   | No       |
| `rule`         | URL or rule for `view` type endpoints.                         | Yes      |
| `methods`      | List of allowed HTTP methods (`GET`, `POST`, etc.).            | Yes      |
| `host`         | Host where the endpoint is exposed (e.g., `example.domain.com`). | Yes    |
| `action`       | Full path to the executable action within the module.          | No       |
| `action_name`  | Name of the action within the module.                          | No       |
| `resource`     | Internal path for RESTful endpoints (`restful`).               | Yes      |
| `urls`         | Relative URL for RESTful endpoints.                            | Yes      |
| `endpoint`     | Name of the RESTful endpoint.                                  | Yes      |

---

## Example of endpoints.

```json
[
  {
    "endpoint_id": "hello",
    "protocol": "view",
    "blueprint_id": "hello_view",
    "rule": "/",
    "action": "apps/example/services/view/simple_view/v1/render/hello",
    "action_name": "hello",
    "methods": ["GET"],
    "host": "example.domain.com"
  },
  {
    "endpoint_id": "public_get",
    "protocol": "restful",
    "blueprint_id": "public_rest",
    "resource": "apps/example/services/restful/simple_restful/v1/public/get",
    "urls": "/",
    "endpoint": "public_get"
  }
]
```

> In this example, `hello` is exposed as a view (`view`) in the `hello_view` blueprint, while `public_get` is a RESTful endpoint (`restful`) within `public_rest`.
> Note: The `host` field is optional, but is used for the example.

---

## Best practices.

* Keep `endpoint_id` unique within the application.
* Associate each endpoint with its corresponding blueprint (`blueprint_id`).
* For views (`view`), define `rule` and HTTP methods (`methods`).
* For RESTful, define `resource`, `urls`, and `endpoint`.
* Use `host` only when it is necessary to expose the endpoint on a specific domain or port.
* Keep the internal path (`action` or `resource`) consistent with the app's service structure.

---

## Advanced configuration. 🛠️

[ENDPOINTS_AVANZADOS.md](ENDPOINTS_AVANZADOS.md) – advanced documentation and real-world configuration cases.

---

## Next step. 🔗

[HOOKS.md](HOOKS.md)
[ACTIONS.md](ACTIONS.md)
