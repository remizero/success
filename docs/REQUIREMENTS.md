# Create the project dependencies file (requirements.txt).

Defines the project dependencies required for Success to function correctly.

This list includes all dependencies used internally by Success
and ensures the project works correctly from the start.

> Note: Some dependencies may not be directly used in all projects.
> They can be removed later based on the specific needs of the application to avoid dependency overload within Success projects.

---

## Get started now.

[Template](#template)

---

## Table of contents. 📑

* [Create requirements.txt file](#create-requirementstxt-file)
* [Content of the requirements.txt file](#content-of-the-requirementstxt-file)
* [Template](#template)
* [Next step](#next-step)

---

## Create requirements.txt file

If you have not yet created the `requirements.txt` file, a quick way to do it is:

  ```bash
    touch requirements.txt
  ```

---

## Content of the requirements.txt file

After creating the `requirements.txt` file, copy the dependencies required by Success:

  ```bash
    cat <<EOF >> requirements.txt
    aniso8601
    async-timeout
    attrs
    blinker
    cachelib
    click
    colorama
    Deprecated
    Flask
    Flask-Admin
    Flask-APScheduler
    Flask-Babel
    Flask-Caching
    Flask-Cors
    Flask-JWT-Extended
    Flask-Limiter
    Flask-Login
    Flask-Mail
    flask-marshmallow
    Flask-Migrate
    flask-redis
    Flask-RESTful
    Flask-Security
    Flask-Security-Too
    Flask-Session
    Flask-SQLAlchemy
    Flask-Uploads
    greenlet
    gunicorn
    importlib-metadata
    itsdangerous
    Jinja2
    jsonschema
    MarkupSafe
    marshmallow
    marshmallow-sqlalchemy
    packaging
    psycopg2
    psycopg2-binary
    pycryptodomex
    PyJWT
    pyparsing
    pyrsistent
    PyPDF2
    python-docx
    python-dotenv
    python-json-logger
    pytz
    redis
    requests
    six
    SQLAlchemy
    Werkzeug
    wrapt
    zipp
    EOF
  ```
---

## Template. (recommended) ⚡

The fastest way to get started is by copying the `requirements.txt` template included in the examples directory of Success:

  ```bash
    cp examples/requirements.txt <path/my_project/requirements.txt>
  ```

---

## Next step. 🔗

[WSGI.md](WSGI.md)
