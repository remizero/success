# Creating a project in Success.

Success allows creating a project in three ways: quick (template), manual, and via CLI. Each method generates the same project structure, but with different levels of control and speed.

A newly created project defines the base structure of Success, but is not executable until at least one application with an endpoint is created.

---

## Get started now.

[Template](#template)

---

## Table of contents. 📑

* [Prerequisites](#prerequisites)
* [Manual](#manual)
* [Base files](#base-files)
* [Template](#template)
* [CLI](#cli)
* [Result](#result)
* [Next step](#next-step)

---

## Prerequisites.

- Python 3.x
- Git
- Pip

---

## Manual. (optional) 🛠️

To better understand how a Success project works, its structure, or to customize it from scratch, these are the steps to follow for building a Success project from the ground up.
These steps create the project structure and prepare the project environment for subsequent use.

  ```bash
    mkdir <my_project>
    cp -r success <my_project>
    cd <my_project>
    mkdir apps
    touch requirements.txt
    touch wsgi.py
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
  ```

Result: complete and understandable project, ideal for learning or customization.
Ideal for: developers who want full control over every folder and file.

---

## Base files. 📂

### requirements.txt

[REQUIREMENTS.md](REQUIREMENTS.md)

---

### wsgi.py

[WSGI.md](WSGI.md)

---

## Template. (recommended) ⚡

The fastest way to get started is by copying the new_project template included in the Success examples directory:

  ```bash
    cp -r examples/new_project <my_project>
    cp -r success <my_project>
    cd <my_project>
    ./setup.sh
  ```
The `setup.sh` file automates environment preparation (as defined in the manual mode).

Result: project ready for immediate use.
Ideal for: testing Success, quickly creating a project without complications.

---

## CLI. 🖥️

> Available in upcoming versions.

  ```bash
    success create-project path/my_project
  ```

Result: everything set up automatically (structure, folders, files, virtualenv, dependencies).
Ideal for: devs who want to get started immediately without worrying about the details.

---

## Result. 🏗️

  ```bash
    my_new_project/
    ├── apps/
    ├── success/
    ├── venv/
    ├── requirements.txt
    └── wsgi.py
  ```

> Note: The `venv/` directory is created during environment preparation.

---

## Next step. 🔗

[APPLICATIONS.md](APPLICATIONS.md)
