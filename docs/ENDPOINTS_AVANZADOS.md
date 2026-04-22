# Advanced Endpoints in Success. 🧠

Advanced endpoints in Success allow precise control over how an action is exposed based on protocol, host, domain, and semantic convention.

This guide documents recommended patterns for real-world production scenarios.

---

## Get started now.

[Template](#template)

---

## Table of contents. 📑

* [Advanced view vs restful differences](#advanced-view-vs-restful-differences)
* [Template](#template)
* [Real view case](#real-view-case)
* [Real restful case](#real-restful-case)
* [Host and subdomain](#host-and-subdomain)
* [Validation checklist](#validation-checklist)
* [Best practices](#best-practices)
* [Next step](#next-step)

---

## Advanced view vs restful differences.

### `view` endpoint

Required:

* `rule`
* `action`
* `action_name`

Optional:

* `methods` (default `GET`)
* `host` (in subdomain mode)

### `restful` endpoint

Required:

* `resource`
* `urls`
* `endpoint`

Optional:

* `host` (in subdomain mode)

---

## Template.

```json
[
  {
    "endpoint_id": "<id_view>",
    "protocol": "view",
    "blueprint_id": "<blueprint_id>",
    "rule": "/",
    "action": "apps/<app>/services/view/<service>/<version>/<module>/<action>",
    "action_name": "<flask_endpoint_name>",
    "methods": ["GET"],
    "host": "<optional>"
  },
  {
    "endpoint_id": "<id_rest>",
    "protocol": "restful",
    "blueprint_id": "<blueprint_id>",
    "resource": "apps/<app>/services/restful/<service>/<version>/<module>/<action>",
    "urls": "/",
    "endpoint": "<resource_name>",
    "host": "<optional>"
  }
]
```

---

## Real view case.

```json
{
  "endpoint_id": "dashboard",
  "protocol": "view",
  "blueprint_id": "dashboard",
  "rule": "/",
  "action": "apps/synthetos/services/view/chromadb/v1/admin/dashboard",
  "action_name": "dashboard",
  "methods": ["GET"],
  "host": "synthetos.nexaiideon.ai:5000"
}
```

---

## Real restful case.

```json
{
  "endpoint_id": "tenant",
  "protocol": "restful",
  "blueprint_id": "tenant",
  "resource": "apps/synthetos/services/restful/chromadb/v1/admin/tenant/create",
  "urls": "/create",
  "endpoint": "tenant_create"
}
```

---

## Host and subdomain.

In `SUCCESS_APP_MODE=subdomain`:

* If you define `host` in the endpoint, that value takes priority.
* If you do not define `host`, Success automatically builds it using `SERVER_NAME` and `APP_PORT`.

---

## Validation checklist.

Before running:

* `blueprint_id` exists in `blueprints.json`.
* `action` or `resource` points to a valid action folder.
* `Action.py` exists in the target path.
* In `view`, `action_name` matches the expected endpoint.
* In `restful`, `endpoint` is unique within the blueprint.

---

## Best practices.

* Use unique and stable `endpoint_id`.
* Keep `urls` and `rule` short and semantic.
* Avoid mixing business responsibilities in a single action.
* Define explicit `host` when handling multiple domains.

---

## Next step. 🔗

[HOOKS.md](HOOKS.md)
