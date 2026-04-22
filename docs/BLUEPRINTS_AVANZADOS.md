# Advanced Blueprints in Success. 🧭

In Success, advanced blueprints allow segmenting domains, protocols, and versions explicitly without losing traceability.

This guide focuses on real configurations for projects with more than one module, more than one protocol, or subdomain deployments.

---

## Get started now.

[Template](#template)

---

## Table of contents. 📑

* [When to use advanced blueprints](#when-to-use-advanced-blueprints)
* [Recommended organization patterns](#recommended-organization-patterns)
* [Template](#template)
* [Real multi-protocol case](#real-multi-protocol-case)
* [Real subdomain case](#real-subdomain-case)
* [Common errors](#common-errors)
* [Best practices](#best-practices)
* [Next step](#next-step)

---

## When to use advanced blueprints.

Use advanced configuration when:

* You need to separate `view` and `restful` within the same app.
* You need to version by `v1`, `v2`, etc.
* You need to segment URLs by functional domain (`/dashboard`, `/tenant`, `/public`).
* You need to operate in `subdomain` mode.

---

## Recommended organization patterns.

### 1. One blueprint per functional domain

Example: `dashboard`, `tenant`, `public`.

### 2. One blueprint per protocol if the domain changes contract

Example: `hello_view` for HTML, `public_rest` for API.

### 3. Explicit versioning in `module.path.version`

Example: `v1`, `v2`.

---

## Template.

```json
[
  {
    "id": "<blueprint_id>",
    "module": {
      "name": "<module>",
      "path": {
        "protocol": "<view|restful|rpc>",
        "service": "<service>",
        "version": "<version>",
        "actions": "<optional_actions_group>"
      }
    },
    "url_prefix": "/<prefix>"
  }
]
```

---

## Real multi-protocol case.

`apps/example/blueprints.json` combines view and API:

```json
[
  {
    "id": "hello_view",
    "module": {
      "name": "admin",
      "path": {
        "protocol": "view",
        "service": "chromadb",
        "version": "v1"
      }
    },
    "url_prefix": "/hello"
  },
  {
    "id": "public_rest",
    "module": {
      "name": "admin",
      "path": {
        "protocol": "restful",
        "service": "chromadb",
        "version": "v1",
        "actions": "public"
      }
    },
    "url_prefix": "/public"
  }
]
```

Result:

* The first blueprint routes HTML views.
* The second blueprint routes REST resources.

---

## Real subdomain case.

If `SUCCESS_APP_MODE=subdomain`, Success can assign `subdomain` automatically per app (or explicitly via configuration).

```json
[
  {
    "id": "dashboard",
    "module": {
      "name": "admin",
      "path": {
        "protocol": "view",
        "service": "chromadb",
        "version": "v1"
      }
    },
    "url_prefix": "/dashboard",
    "subdomain": "synthetos"
  }
]
```

> Note: `subdomain` only applies in subdomain mode.

---

## Common errors.

* Repeating `id` across blueprints.
* Defining `blueprint_id` in endpoints that do not exist in `blueprints.json`.
* Mixing `view` and `restful` routes in the same endpoint inconsistently.
* Omitting `url_prefix` and ending up with ambiguous routes.

---

## Best practices.

* Keep `id` short, semantic, and unique.
* Use a stable `url_prefix` to avoid breaking consumers.
* Use `actions` only when it adds real clarity.
* Version from the start (`v1`) even if only one version exists.

---

## Next step. 🔗

[ENDPOINTS_AVANZADOS.md](ENDPOINTS_AVANZADOS.md)
