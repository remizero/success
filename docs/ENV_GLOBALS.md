# Global environment variables 🌍

The project `.env` configuration file defines the behavior of Success.

---

## Get started now.

[Template](#template)

---

## Table of contents. 📑

* [Location and scope](#location-and-scope)
* [Recommended blocks](#recommended-blocks)
* [Global environment variables](#global-environment-variables)
* [Per-application environment variables](#per-application-environment-variables)
* [Template](#template)

---

# Global environment variables 🌍

> NOTE: All `SUCCESS_*` variables are processed by the Success core during system initialization. Invalid values may affect the global behavior of the application.

| Variable                  | Description                               | Type     | Allowed values                      | Default        |
|---------------------------|-------------------------------------------|----------|-------------------------------------|----------------|
| SUCCESS_APP_PREFIX        | Global prefix for application routes      | string   | any string                          | ""             |
| SUCCESS_DEBUG_CONSOLE     | Enables detailed console logs             | boolean  | True / False                        | True           |
| SUCCESS_STAGING           | Enables staging mode                      | boolean  | True / False                        | False          |
| SUCCESS_TESTING           | Enables testing mode                      | boolean  | True / False                        | False          |
| SUCCESS_STRICT_SLASHES    | Controls trailing slashes in routes       | boolean  | True / False                        | False          |
| SUCCESS_MAIN_APP          | Main application                          | string   | app name                            | -              |
| SUCCESS_SECONDARY_APPS    | List of secondary applications            | list     | list of strings                     | []             |
| SUCCESS_APPS_PATH         | Base path for applications                | string   | valid path                          | "apps"         |
| SUCCESS_ALLOW_NO_MAIN_APP | Allows running without a main app         | boolean  | True / False                        | False          |
| SUCCESS_SAVE_MODE         | Enables persistence/configuration mode    | boolean  | True / False                        | False          |
| SUCCESS_SHOW_SUMMARY      | Shows execution summary                   | boolean  | True / False                        | True           |
| SUCCESS_SUMMARY_LEVEL     | Summary detail level                      | string   | NONE / BASIC / FULL                 | FULL           |
| SUCCESS_MOOD_LANG         | System language                           | string   | "es", "en", etc.                    | "es"           |
| SUCCESS_APP_MAIN          | Marks if current app is the main one      | boolean  | True / False                        | False          |
| SUCCESS_APP_TYPE          | App architecture type                     | string   | singleApp / multiApp                | singleApp      |
| SUCCESS_APP_MODE          | Routing strategy                          | string   | flask / standard / path / subdomain | flask          |

---

### SUCCESS_APP_PREFIX

Type: string
Default: ""

Defines a global prefix for all application routes.

Example:

```bash
  SUCCESS_APP_PREFIX=/api
```

👉 Result:
```bash
  /api/dashboard
  /api/users
```

---

### SUCCESS_DEBUG_CONSOLE

Type: boolean
Default: True

Enables detailed console log output during execution.

Recommended usage:

True → development
False → production

---

### SUCCESS_STAGING

Type: boolean
Default: False

---

### SUCCESS_TESTING

Type: boolean
Default: False

---

### SUCCESS_STRICT_SLASHES

Type: boolean
Default: False

---

### SUCCESS_MAIN_APP

Type: string
Default: -

Defines the name of the main application.

---

### SUCCESS_SECONDARY_APPS

Type: list
Default: []

Defines a list of secondary application names.

---

### SUCCESS_APPS_PATH

Type: string
Default: "apps"

Defines the base path for applications.

---

### SUCCESS_ALLOW_NO_MAIN_APP

Type: boolean
Default: False

Allows running without a main application.

---

### SUCCESS_SAVE_MODE

Type: boolean
Default: False

---

### SUCCESS_SHOW_SUMMARY

Type: boolean
Default: True

---

### SUCCESS_SUMMARY_LEVEL

Type: string
Default: FULL

Defines the detail level of the summary displayed by Success on startup.

Values:

NONE → no output
BASIC → minimal information
FULL → complete information

---

### SUCCESS_MOOD_LANG

Type: string
Default: "es"

Defines the system language.

Values:

es → Spanish
en → English

---

### SUCCESS_APP_MAIN

Type: boolean
Default: False

Marks if the current app is the main one.

---

### SUCCESS_APP_TYPE

Type: string
Default: singleApp

Defines the application architecture type.

Values:

singleApp → single application
multiApp → multiple applications

---

### SUCCESS_APP_MODE

Type: string
Default: flask

Defines how Success resolves application routes.

Values:

flask → standard Flask behavior
standard → simplified internal routing
path → separation by path (/app1/...)
subdomain → separation by subdomains

👉 This variable is critical in multi-app architectures.
