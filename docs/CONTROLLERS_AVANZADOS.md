# Advanced Controllers in Success. 🚀

This guide covers advanced patterns for controllers in real-world scenarios: composition between controllers, controlled error handling, and consistent responses for `Output`.

---

## Get started now.

[Patterns](#advanced-patterns)

---

## Table of contents. 📑

* [Advanced patterns](#advanced-patterns)
* [Controller composition](#controller-composition)
* [Error handling and degradation](#error-handling-and-degradation)
* [Robust return contracts](#robust-return-contracts)
* [Production checklist](#production-checklist)
* [Next step](#next-step)

---

## Advanced patterns.

Recommended patterns:

* Aggregator Controller: combines multiple sources.
* Facade Controller: simplifies access to external layers.
* Resilient Controller: responds partially even if a dependency fails.

---

## Controller composition.

Real example: `Dashboard.load` consumes data from `Tenant.load` to calculate metrics.

```python
class Dashboard(SuccessController):

  def load(self, payload: dict) -> dict:
    tenant_response = Tenant().load()
    # compose response
    return {"status": 200, "body": {...}}
```

Benefit:

* Logic reuse without duplication.

---

## Error handling and degradation.

An advanced controller should not break the entire flow due to a single dependency:

* Catch the exception.
* Log context.
* Return valid output with `status` and `error`.

```python
return {
  "status": 200,
  "body": {...},
  "message": "Partial response"
}
```

---

## Robust return contracts.

To maintain stability in `Output`:

* Always include `status`.
* Use `body` for the main payload.
* Use `error` for business failures.
* Use `code` and `type` when you need traceability.

---

## Production checklist.

* Does the method exist and match `self._controllerMethod` from the action?
* Does the return fulfill the contract (`status`, `body` or `error`)?
* Are external errors translated into controlled messages?
* Is the logic testable without HTTP?

---

## Next step. 🔗

[INPUT.md](INPUT.md)
