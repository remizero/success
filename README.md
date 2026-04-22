# Success

## What is Success?

Success is not just a framework. It's a **way of thinking, organizing, and executing systems** with semantics, traceability, and elegance.

It is an application orchestrator built on Flask, designed to establish order, coherence, and scalability without sacrificing the freedom to develop a Flask application.

Unlike other approaches, Success does not replace Flask, but rather structures it, automates it, and empowers it, eliminating the need to reinvent the architecture in every project with the ability to adapt to multiple interfaces without changing the base architecture. It prevents a Flask project from becoming a nightmare as it grows.

Its purpose is simple but powerful:

> Allow building complex applications with the same clarity as a small project.

---

## Get started now.

[QUICKSTARTER.md](docs/QUICKSTARTER.md)

---

## Table of contents

- [What is Success?](#what-is-success)
- [Why Success?](#why-success)
- [Problems that Success solves](#problems-that-success-solves)
- [Fundamental principles of Success](#fundamental-principles-of-success)
- [Philosophy of Success](#philosophy-of-success)
- [Features of Success](#features-of-success)
- [Quick Start](#quick-start)
- [Roadmap](#roadmap)
- [Key concepts](#key-concepts)
- [Versioning strategy](#versioning-strategy)
- [Naming convention](#naming-convention)
- [Next step](#next-step)

---

## Why Success?

Success was born from a recurring problem when working with Flask:

> Every project starts clean... but as it grows, the architecture becomes inconsistent, repetitive, and difficult to maintain.

In Flask:

* There is no defined structure.
* Each developer organizes differently.
* Best practices are not integrated.
* Infrastructure is constantly rewritten.

Success arises to turn those best practices into something automatic, reusable, and consistent. It comes from the need to build **robust systems**, **modular** and **maintainable**, without sacrificing clarity or development speed. Not to limit the developer, but to prevent them from having to reinvent the same thing in every project.

It is the bridge between:

* The declarative and the procedural.
* The structured and the dynamic.
* What you need today and what will grow tomorrow.

Success doesn't try to change how you develop. It makes developing well, the natural path.

---

## Problems that Success solves

🔹 Constant infrastructure repetition
Every new Flask project involves redoing configurations, structures, and patterns.

👉 Success eliminates that repetition.

🔹 Inconsistent architectures
Without clear guidelines, every module, endpoint, or blueprint can end up organized differently.

👉 Success imposes order without removing flexibility.

🔹 Coupling between logic and transport
In many projects, business logic ends up mixed with HTTP, requests, and responses.

👉 Success clearly separates: Input → Action → Output

🔹 Painful scalability
What starts simple becomes difficult to maintain as it grows.

👉 Success allows scaling without restructuring everything.

🔹 Lack of structural automation
Blueprints, endpoints, and connections are defined manually over and over again.

👉 Success automates the complete application build process.

---

## Fundamental principles of Success

Success is built on five fundamental pillars:

🔹 Order over freedom
    Flask gives you freedom. Success gives you direction.

🔹 Conventions over repetition
    Don't write the same thing 20 times. Define once, reuse always.

🔹 Real extensibility (not marketing)
    Everything can be extended or replaced without breaking the system.

🔹 Explicit architecture
    Nothing is hidden behind black magic. Every flow is traceable.

🔹 Progressive scalability
    You start simple, grow without restructuring.

---

## Philosophy of Success

Success doesn't tell you what to build. It tells you how not to break yourself while building it.

It is based on:
🔹 Code must be explicit, not implicit
🔹 Every action is a deterministic pipeline
🔹 Structure is more important than freedom
🔹 The framework guides, doesn't allow chaos
🔹 Clear separation of intent, execution, and response.
🔹 Treat architecture as part of the system, not a detail.
🔹 Automate the repetitive without hiding behavior.
🔹 Prioritize clarity over "magic".
🔹 Design thinking about evolution, not just the present.

---

## Features of Success

You only need to focus on what matters, the **business logic**.

🔹 Centralized declarative configuration as the system core and single source of truth.
🔹 Macro system based on Success's own macros without colliding with Flask macros.
🔹 Modular architecture.
🔹 Native integration with Flask extensions.
🔹 Automatic application build.
🔹 Separation of responsibilities.
🔹 Action-oriented flow (not traditional endpoints).
🔹 Capable of adapting to multiple interfaces without changing the base architecture.
🔹 Multi-interface support: HTTP, CLI, WebSockets, etc.
🔹 Extension through clear contracts (hooks).

---

## Quick Start

1. Quickstarters. Start faster with pre-built examples.
2. Download/install Success.
3. Create project.
4. Create application.
5. Configure .env.
6. Define first action.
7. Run application.


### 1. Download/Install Success.

#### Download Success.

  You can download Success from GitHub:

    git clone <download url>

#### Install Success. (This hasn't been tested yet and has not been implemented)

  pip install success

### 2. Create project.

  - Create a directory with the name of the project to develop.
  - Copy the success directory inside the newly created project.
  - Enter the directory.
  - Create a directory called apps.
  - Enter the apps directory.
  - Create a directory with the name of the application to develop, it can be the same name as the global project.
  - Enter the application directory.
  - Create a file called __init__.py.
  - Create a directory called services.
  - Create a directory called static.
  - Create a directory called templates.
  - Create a file called blueprints.json.
  - Create a file called endpoints.json.
  - Create a file called hooks.json.
  - Create a file called extensions.json.
  - Create a file called .env.

### 3. Configure .env.

### 4. Define first action.

### 5. Run application.

---

## Quick Start

[QUICKSTARTER.md](docs/QUICKSTARTER.md)

---

## Roadmap

See [ROADMAP.md](docs/ROADMAP.md) for upcoming features and plans.

---

## Key concepts

## Versioning strategy

Success adopts a namespace-based versioning approach (v1, v2, ...),
allowing progressive evolution of actions.

### Recommendations

- Keep previous versions while there are active consumers
- Avoid modifying behaviors in already published versions
- Introduce breaking changes only in new versions (v2, v3, ...)

Success does not impose a lifecycle strategy, but promotes these practices to guarantee stability and scalability.


## Naming convention

In Success, the semantics of an action are not defined by the class name,
but by its location within the filesystem.

services/<protocol>/<service>/<version>/<resource>/<action>/

This allows reducing code complexity, avoiding redundancies and
favoring a predictable and self-documented structure.

"Every action is an intent, every folder is a decision."
"In Success, the code doesn't explain the intent... the location does."
"An Action is not a function... it's an orchestrated pipeline."
You don't execute actions... you convert them into executable code.
First run it... then understand it.

---

## Next step. 🔗

[PROJECTS.md](docs/PROJECTS.md)
