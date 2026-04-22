# Create an Action in Success.

This guide describes how to create an action in Success, the fundamental unit of execution for endpoints in Flask applications.

---

## Get started now.

Prefer to get straight to the point?

👉 [Create my first action in one minute](#create-my-first-action-in-one-minute)

---

## Table of contents.

* [What is a Success action?](#what-is-a-success-action)
* [Structure of a Success action](#structure-of-a-success-action)
* [Files that make up a Success action](#files-that-make-up-a-success-action)
* [Execution flow](#execution-flow)
* [Manual](#manual)
* [Template](#template)
* [CLI](#cli)
* [Next step](#next-step)

---

## What is a Success action?.

A Success action is a unit of execution that encapsulates the business logic associated with an endpoint.

Its goal is to decouple responsibilities, allowing each component of the system to have a clear role within the request processing flow.

An action is not a single function, but an execution pipeline composed of decoupled phases that allow extending behavior without modifying the main logic.

---

## Structure of a Success action.

All actions are defined within the `services` directory, following a semantic convention:

```
apps/<app_name>/services/<protocol>/<service>/<version>/<module>/[<submodule>]/<action>/
```

### Understanding the Success directory system for an action.

- apps: the root directory for applications.
- app_name: the name of the application.
- services: allows organizing the different services provided by the application by access protocol.
- protocol: access protocol to the action or service (view, restful, rpc, etc.).
- service: name of the service to serve or consume by the application, which can be external or internal.
- version: the service version.
- module: groups actions according to their nature (users, products, orders, etc.).
- submodule: optional directory to separate/group actions according to criteria (CRUD, etc.).
- action: name of the action (encloses the files that make up a Success action).

This structure allows organizing actions in a scalable way, aligned with the domain and application context. It also uses a versioning approach based on directory structure or URL Path Versioning.

Each version of an action is defined within its own namespace:

services/<protocol>/<service>/v1/...
services/<protocol>/<service>/v2/...

This approach allows evolving the behavior of an action without affecting previous versions, guaranteeing backward compatibility.

- Actions must use infinitive verbs: create, update, delete.
- Resources must be in singular: user, order, product.
- Do not use synonyms for the same action.

---

## Files that make up a Success action

An action may consist of the following files:

* `Action.py`
* `Input.py`
* `Response.py`
* `Output.py` *(optional, for special cases)*
* `Schema.py` *(optional)*

Each one fulfills a specific responsibility (SRP - Single Responsibility Principle) within the execution flow:

* **Action** → Orchestrates business logic
* **Input** → Parses and validates input data
* **Response** → Builds the base response
* **Output** → Formats the output *(optional)*
* **Schema** → Defines the data structure *(optional)*

This design allows clear decoupling and facilitates system maintainability.

---

## Execution flow

The lifecycle of an action follows this flow:

```
Request → PreInput → Input → Controller → Output → PostOutput → Response
```

1. The request enters the system
2. `PreInput` (permissions, context, etc.).
3. `Input` validates and transforms input data.
4. `Controller` executes business logic and returns a resultset (data).
5. `Output` formats and normalizes the resultset to build the final output.
6. `PostOutput` (cookies, headers, etc.).
7. `Response` builds the final response.

---

## Manual. (optional) 🛠️

To better understand how a Success action works, its structure, or to customize it from scratch, these are the steps to follow to build a Success action from zero.
These steps create the action structure and prepare the environment for its subsequent use.

### 1. Create the structure

Based on the "structure of a Success action" section, you must follow this pattern:

```bash
apps/<app_name>/services/<protocol>/<service>/<version>/<module>/[<submodule>]/<action>/
```

At this point, we should be inside the `apps/hello_world/` application, so our path will look like this:

```bash
  mkdir services/view/simple_view/v1/hello/render
  cd services/view/simple_view/v1/hello/render
  touch Action.py
  touch Input.py
  touch Response.py
```

---

### 2. Action.py

#### View-type action.

```bash
  cat <<EOF >> Action.py
  # Python Libraries / Librerías Python
  from flask import Response as FlaskResponse

  # Success Libraries / Librerías Success
  from success.engine.io.SuccessViewAction import SuccessViewAction
  from success.engine.io.SuccessOutput     import SuccessOutput

  # Application Libraries / Librerías de la Aplicación
  from apps.hello_world.services.view.simple_view.v1.hello.render.Input    import Input
  from apps.hello_world.services.view.simple_view.v1.hello.render.Response import Response as ActionResponse
  from apps.hello_world.modules.simple_view.v1.hello.controllers.Hello    import Hello

  # Preconditions / Precondiciones


  class Action ( SuccessViewAction ) :


    def __init__ ( self ) -> None :
      super ().__init__ ( Input (), SuccessOutput (), ActionResponse (), Hello () )
      self._controllerMethod    = "load"
      self._outputSpec.template = "hello.html"

      # Optional redirect parameters (endpoint name, not URL):
      # self._outputSpec.redirect_to = "auth.login"
      # self._outputSpec.fallback_redirect = "core.home"


    def get ( self ) -> FlaskResponse :
      return self.execute ( self._controllerMethod )
  EOF
```

---

#### Restful-type action.

```bash
  cat <<EOF >> Action.py
  # Python Libraries / Librerías Python
  from flask import Response as FlaskResponse

  # Success Libraries / Librerías Success
  from success.engine.io.SuccessRestfulAction import SuccessRestfulAction
  from success.engine.io.SuccessOutput        import SuccessOutput

  # Application Libraries / Librerías de la Aplicación
  from apps.hello_world.services.restful.simple_api.v1.hello.api.Input    import Input
  from apps.hello_world.services.restful.simple_api.v1.hello.api.Response import Response as ActionResponse
  from apps.hello_world.modules.simple_api.v1.hello.controllers.PublicApi import PublicApi

  # Preconditions / Precondiciones


  class Action ( SuccessRestfulAction ) :


    def __init__ ( self ) -> None :
      super ().__init__ ( Input (), SuccessOutput (), ActionResponse (), PublicApi () )
      self._controllerMethod    = "get"

      # Optional redirect parameters (endpoint name, not URL):
      # self._outputSpec.redirect_to = "auth.login"
      # self._outputSpec.fallback_redirect = "core.home"


    def get ( self ) -> FlaskResponse :
      return self.execute ( self._controllerMethod )
  EOF
```

---

### Notes

* It is recommended to use templates to ensure consistency.
* CLI support for automatic action generation is under development.
* This structure allows scaling from simple actions to complex flows without modifying the system base.

---

## Template. (recommended) ⚡

The fastest way to get started is by copying the action template included in the Success examples directory:

  ```bash
    cp -r examples/action <path/my_project/apps/my_app/services/view/simple_view/v1/hello/render>
  ```

---

## CLI. 🖥️

> Available in upcoming versions.

  ```bash
    success create-action path/my_action
  ```

---

## Next step. 🔗

[INPUT.md](INPUT.md)
