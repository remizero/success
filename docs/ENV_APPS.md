# Application environment variables in Success. 🌱

The `.env` configuration file defines the behavior of each Success application.

This guide explains how to structure it correctly so that the app loader, blueprints, endpoints, and extensions work without surprises.

---

## Get started now.

[Template](#template)

---

## Table of contents. 📑

* [Location and scope](#location-and-scope)
* [Environment variables table for Success applications](#environment-variables-table-for-success-applications)
* [Extensions (SUCCESS_EXTENSION_*)](#extensions-success-extension-)
* [Output and models](#output-and-models)
* [Protocols (SUCCESS_ENABLE_*)](#protocols-success-enable-)
* [Advanced routing](#advanced-routing)
* [Advanced CORS configuration](#advanced-cors-configuration)


* [Per-application environment variables](#per-application-environment-variables)
* [Template](#template)
* [Recommended minimum variables](#recommended-minimum-variables)
* [Common errors](#common-errors)
* [Best practices](#best-practices)
* [Advanced configuration](#advanced-configuration)
* [Next step](#next-step)

---

## Location and scope.

Each application defines its own `.env` at:

  ```bash
    <my_project>/apps/<my_app>/.env
  ```

---

## Environment variables table for Success applications.

| Variable                         | Description                                     | Type    | Allowed values                         | Default |
|----------------------------------|-------------------------------------------------|---------|----------------------------------------|---------|
| SUCCESS_EXTENSION_*              | Enables/disables extensions                     | boolean | True / False                           | True    |
| SUCCESS_OUTPUT_MODEL             | Enables custom output model                     | boolean | True / False                           | True    |
| SUCCESS_OUTPUT_MODEL_CLASS       | Custom class for output                         | string  | valid Python path                      | -       |
| SUCCESS_TABLENAME_MODEL          | Generates models based on table name            | boolean | True / False                           | True    |
| SUCCESS_ENABLE_*                 | Enables protocols (view, rest, rpc, etc.)       | boolean | True / False                           | depends |
| SUCCESS_ENABLE_CLI               | Enables internal CLI                            | boolean | True / False                           | False   |
| SUCCESS_HOST_MATCHING            | Enables host-based matching                     | boolean | True / False                           | True    |
| SUCCESS_SUBDOMAIN_MATCHING       | Enables subdomain-based matching                | boolean | True / False                           | True    |
| CORS_*                           | Advanced CORS configuration                     | list    | structured lists                       | -       |

> NOTE: These variables control the behavior of each application within Success, including extensions, enabled protocols, and advanced configuration.

---

## Extensions (SUCCESS_EXTENSION_*) 🔌

These variables allow enabling or disabling Flask extensions integrated in Success.

Example:

  ```env
    SUCCESS_EXTENSION_SQLALCHEMY=True
    SUCCESS_EXTENSION_REDIS=True
    SUCCESS_EXTENSION_SECURITY=False
  ```

👉 Each extension is automatically initialized only if enabled.

Available extensions

| Environment variable            | Flask extension           | Description                                                           | Data type    | Allowed values         | Default value     |
| ------------------------------- | ------------------------- | --------------------------------------------------------------------- | ------------ | ---------------------- | ----------------- |
| SUCCESS_EXTENSION_ACL           | `Flask-Principal`         | Enables advanced permission and role control for resources.           | bool         | True / False           | True              |
| SUCCESS_EXTENSION_ADMIN         | `Flask-Admin`             | Provides administrative interface for models and app management.      | bool         | True / False           | True              |
| SUCCESS_EXTENSION_APSCHEDULER   | `Flask-APScheduler`       | Allows scheduling recurring tasks within the app.                     | bool         | True / False           | True              |
| SUCCESS_EXTENSION_BABEL         | `Flask-Babel`             | Internationalization and locale handling in the app.                  | bool         | True / False           | True              |
| SUCCESS_EXTENSION_BLUEPRINT     | N/A (Core)                | Manages loading and registration of blueprints in the application.    | bool         | True / False           | True              |
| SUCCESS_EXTENSION_CACHE         | `Flask-Caching`           | Enables caching of views, data, and query results.                    | bool         | True / False           | True              |
| SUCCESS_EXTENSION_CORS          | `Flask-Cors`              | Allows handling custom CORS policies per domain and endpoint.         | bool         | True / False           | True              |
| SUCCESS_EXTENSION_SQLALCHEMY    | `Flask-SQLAlchemy`        | ORM for database management.                                          | bool         | True / False           | True              |
| SUCCESS_EXTENSION_EMAIL         | `Flask-Mail`              | Enables sending emails from the application.                          | bool         | True / False           | True              |
| SUCCESS_EXTENSION_JWT           | `Flask-JWT-Extended`      | JWT-based authentication.                                             | bool         | True / False           | True              |
| SUCCESS_EXTENSION_LIMITER       | `Flask-Limiter`           | Limits request rate per IP or endpoint.                               | bool         | True / False           | True              |
| SUCCESS_EXTENSION_LOGGER        | `logging` (core Python)   | Configuration and activation of global Success logging.               | bool         | True / False           | True              |
| SUCCESS_EXTENSION_LOGGIN        | N/A                       | Custom logging control, internal use.                                 | bool         | True / False           | False             |
| SUCCESS_EXTENSION_MARSHMALLOW   | `flask-marshmallow`       | Serialization and validation of models and payloads.                  | bool         | True / False           | True              |
| SUCCESS_EXTENSION_MIGRATE       | `Flask-Migrate`           | Database migration management.                                        | bool         | True / False           | True              |
| SUCCESS_EXTENSION_REDIS         | `flask-redis`             | Redis connection and caching, used by several internal extensions.    | bool         | True / False           | True              |
| SUCCESS_EXTENSION_RESTFUL       | `Flask-RESTful`           | Enables building RESTful APIs within the app.                         | bool         | True / False           | True              |
| SUCCESS_EXTENSION_SECURITY      | `Flask-Security-Too`      | Authentication, user registration, roles, and advanced security.      | bool         | True / False           | False             |
| SUCCESS_EXTENSION_SESSION       | `Flask-Session`           | Server-side session management.                                       | bool         | True / False           | True              |
| SUCCESS_EXTENSION_UPLOADS       | `Flask-Uploads`           | Management of files uploaded by the application.                      | bool         | True / False           | True              |


> NOTES:
> - For extensions to work correctly, each corresponding environment variable for each enabled extension must be properly configured.
> - Each `.env` file (env.app) contains the environment variables corresponding to each extension of each Flask application.

---

## Output and models 🧠

### SUCCESS_OUTPUT_MODEL

Type: boolean
Default: True

Enables a custom output system for responses.

---

### SUCCESS_OUTPUT_MODEL_CLASS

Type: string
Default: None

Defines a custom class to handle system output.

SUCCESS_OUTPUT_MODEL_CLASS=myapp.output.CustomOutput

---

### SUCCESS_TABLENAME_MODEL

Type: boolean
Default: True

Automatically generates models based on database table names.

---

### Protocols (SUCCESS_ENABLE_*) 🌐

Controls which types of endpoints are enabled in the application.

SUCCESS_ENABLE_VIEW=True
SUCCESS_ENABLE_REST=True
SUCCESS_ENABLE_RPC=False
SUCCESS_ENABLE_GRAPHQL=False
SUCCESS_ENABLE_SSE=False
SUCCESS_ENABLE_WEB_SOCKET=False
SUCCESS_ENABLE_SOAP=False
SUCCESS_ENABLE_CLI=False

👉 This literally defines what type of application you are building. A single application can support multiple protocols.

---

## Advanced routing 🧭

### SUCCESS_HOST_MATCHING

Type: boolean
Default: True

Enables host-based routing.

---

## SUCCESS_SUBDOMAIN_MATCHING

Type: boolean
Default: True

Enables subdomain-based routing.

👉 Requires proper SERVER_NAME configuration.

---

## Advanced CORS configuration 🌍

These variables allow defining CORS policies in a granular way.

CORS_RESOURCES_APP_RESOURCES = [ r'/synthetos/*' ]
CORS_RESOURCES_APP_ORIGINS = [ [ 'http://nexaiideon.ai:5000' ] ]
CORS_RESOURCES_APP_METHODS = [ [ 'GET', 'POST', 'PUT', 'DELETE' ] ]
CORS_RESOURCES_APP_ALLOW_HEADERS = [ [ 'Authorization', 'Content-Type', 'X-Requested-With', 'Accept', 'Set-Cookie' ] ]
CORS_RESOURCES_APP_EXPOSE_HEADERS = [ [ 'Content-Type', 'X-CSRFToken' ] ]

> NOTE: These variables are interpreted by the Success extension system to dynamically build CORS policies.
