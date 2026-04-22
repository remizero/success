# Quickstarter

If you want to quickly see what Success has to offer, below are five basic examples to try the different functionalities and/or capabilities of Success.

---

## First.

```bash
git clone https://github.com/remizero/success.git
```

---

## Table of contents.

1. [Domain setup](#domain-setup)
2. [Single App Mode (Standard)](#single-app-standard)
3. [Single App Mode (Subdomain)](#single-app-subdomain).
4. [Multi App Mode (WSGI Dispatcher)](#multi-app-dispatcher)
5. [Multi App Mode (Path)](#multi-app-path).
6. [Multi App Mode (Subdomain)](#multi-app-subdomain).
7. [Multi-App Modes Comparison](#multi-app-modes-comparison)

---

## 1. Domain setup (`success.local`)

Some quickstarters use `success.local` in `env.example`.

Recommended (Linux/macOS):

```bash
sudo sh -c 'echo "127.0.0.1 success.local" >> /etc/hosts'
```

Alternative:

If you prefer not to edit your `hosts` file, replace `success.local` with `localhost` (or your own domain) in the corresponding `env.example` files before running the quickstarter.

---

## 2. Single App Mode (Standard).

Standard Flask application using Success.

Use this mode when you want a single, self-contained application following Success conventions, without any multi-app complexity. Ideal for simple services, APIs, or monolithic applications.

```bash
git clone https://github.com/remizero/success.git
./success/examples/quickstarters/1_single_app_standard/setup.sh quickstarter_1
cd quickstarter_1
source venv/bin/activate
python3 wsgi.py
```

### How to access.

```
http://localhost:5000/hello/
```

After running the application, check the console output to see the available URLs for each app.

---

## 3. Single App Mode (Subdomain).

Flask application with subdomain support using Success.

Use this mode when your application needs to respond to different subdomains (e.g., api.example.com, admin.example.com) while still being a single logical application. Useful for separating concerns without splitting into multiple apps.

```bash
git clone https://github.com/remizero/success.git
./success/examples/quickstarters/2_single_app_subdomain/setup.sh quickstarter_2
cd quickstarter_2
source venv/bin/activate
python3 wsgi.py
```

### How to access.

```
http://example.success.local:5000/hello/
```

After running the application, check the console output to see the available URLs for each app.

---

## 4. Multi App Mode (WSGI Dispatcher).

Runs multiple completely isolated Flask applications, dispatched at the WSGI level.

Use this mode when you need strong isolation between applications (e.g., microservices in a single process), where each app has its own configuration, routes, and lifecycle. This is the most robust and decoupled multi-app setup.

Success uses Flask's dispatching mechanism to execute multiple applications in isolation. ([see Flask documentation](https://flask.palletsprojects.com/en/stable/patterns/appdispatch/#combining-applications))

```bash
git clone https://github.com/remizero/success.git
./success/examples/quickstarters/3_multi_app_dispatcher/setup.sh quickstarter_3
cd quickstarter_3
source venv/bin/activate
python3 wsgi.py
```

### How to access.

```
http://success.local:5000/hello/       (app1)
http://success.local:5000/app2/hello/  (app2)
```

After running the application, check the console output to see the available URLs for each app.


---

## 5. Multi App Mode (Path).

Runs multiple isolated Flask applications, accessed via URL paths.

Use this mode when you want to group multiple applications under a single domain using path-based routing (e.g., /app1, /app2). Simpler to configure than subdomains, but with less separation at the domain level.

Success uses Flask's dispatching mechanism to execute multiple applications in isolation. ([see Flask documentation](https://flask.palletsprojects.com/en/stable/patterns/appdispatch/#dispatch-by-path))

```bash
git clone https://github.com/remizero/success.git
./success/examples/quickstarters/4_multi_app_path/setup.sh quickstarter_4
cd quickstarter_4
source venv/bin/activate
python3 wsgi.py
```

### How to access.

```
http://success.local:5000/hello/       (app1)
http://success.local:5000/app2/hello/  (app2)
```

After running the application, check the console output to see the available URLs for each app.

---

## 6. Multi App Mode (Subdomain).

Runs multiple isolated Flask applications using subdomain-based routing.

Use this mode when each application should be exposed under its own subdomain (e.g., app1.example.com, app2.example.com). Ideal for multi-tenant systems, SaaS platforms, or when clear domain-level separation is required.

Success uses Flask's dispatching mechanism to execute multiple applications in isolation. ([see Flask documentation](https://flask.palletsprojects.com/en/stable/patterns/appdispatch/#dispatch-by-subdomain))

```bash
git clone https://github.com/remizero/success.git
./success/examples/quickstarters/5_multi_app_subdomain/setup.sh quickstarter_5
cd quickstarter_5
source venv/bin/activate
python3 wsgi.py
```

### How to access.

```
http://app1.success.local:5000/hello/ (app1)
http://app2.success.local:5000/hello/ (app2)
```

After running the application, check the console output to see the available URLs for each app.

---

## 7. Multi-App Modes Comparison.

| Mode       | Isolation | Routing Type | Use Case            |
|------------|-----------|--------------|---------------------|
| Dispatcher | High      | WSGI mount   | Strong isolation    |
| Path       | Medium    | URL path     | Simple multi-app    |
| Subdomain  | Medium    | Subdomain    | SaaS / multi-tenant |
