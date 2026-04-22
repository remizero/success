# Create an application in Success.

Success allows creating an application in three ways: quick (template), manual, and via CLI. Each method generates the same application structure, but with different levels of control and speed.

A newly created application defines the base structure of Success, but it is not executable until at least one endpoint is created.

---

## Get started now.

[Template](#template)

---

## Table of contents. 📑

* [Manual](#manual)
* [Base files](#base-files)
* [Template](#template)
* [CLI](#cli)
* [Result](#result)
* [Next step](#next-step)

---

## Manual. (optional) 🛠️

To better understand how a Success application works, its structure, or to customize it from scratch, these are the steps to build a Success application from the ground up.
These steps create the application structure within an already created project.

  ```bash
    cd <my_project>
    cd apps
    mkdir <my_app>
    cd <my_app>
    mkdir models # optional
    mkdir modules # optional
    mkdir services
    mkdir static
    mkdir templates
    touch __init__.py
    touch blueprints.json
    touch endpoints.json
    touch hooks.json # optional
    touch extensions.json # optional
    touch .env
 ```

Result: complete and understandable structure, ideal for learning or customization.
Ideal for: developers who want full control over every folder and file.

---

## Base files. 📂

### .env

[ENV_VARIABLES.md](ENV_VARIABLES.md)

### blueprints.json

[BLUEPRINTS.md](BLUEPRINTS.md)

### endpoints.json

[ENDPOINTS.md](ENDPOINTS.md)

### hooks.json (optional)

[HOOKS.md](HOOKS.md)

### extensions.json (optional)

[EXTENSIONS.md](EXTENSIONS.md)

---

## Template. (recommended) ⚡

The quickest way to get started is by copying the `new_application` template included in the Success `examples` directory:

  ```bash
    cp -r examples/new_application <path/my_project/my_app>
  ```

Result: base structure ready to start working on an application.
Ideal for: quickly creating an application without complications.

---

## CLI. 🖥️

> Available in upcoming versions.

  ```bash
    success create-application path/my_project my_app
  ```

Result: everything set up automatically (structure, folders, files, .env).
Ideal for: developers who want to get started immediately without worrying about the details.

---

## Result. 🏗️

  ```bash
    apps/
    └── my_app/
        ├── models/ (optional)
        ├── modules/ (optional)
        ├── services/
        ├── static/
        ├── templates/
        ├── __init__.py
        ├── blueprints.json
        ├── endpoints.json
        ├── hooks.json (optional)
        ├── extensions.json (optional)
        └── .env
  ```

---

## Next step. 🔗

[BLUEPRINTS.md](BLUEPRINTS.md)
