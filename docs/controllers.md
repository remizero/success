# 🎮 Controllers

Este directorio contiene los **orquestadores principales** de las acciones que puede realizar una aplicación. Los controladores reciben datos desde un Action, invocan lógica de negocio (si aplica), se comunican con fuentes externas o internas, y devuelven la respuesta apropiada.

## 🎯 Propósito

Los controladores **coordinan el flujo** entre los diferentes componentes del sistema:

- Reciben input validado (`Input.py`)
- Llaman servicios o modelos necesarios
- Adaptan la salida para el `Output.py`

## ✅ Ejemplos comunes

- `UserController`: gestión de usuarios.
- `FileUploaderController`: lógica de subida de archivos.
- `ChromaQueryController`: operaciones con vectores.

## 📐 Filosofía Success

> El controlador **no debe contener lógica de negocio pesada**, sino delegar dicha responsabilidad a los servicios o a `infrastructure/` si depende de recursos externos.

---

✍️ Convención de nombres esperada:
- Archivo: `nombre_controller.py`
- Clase: `NombreController`

Ejemplo:
```python
from apps.mi_app.controllers.users.v1.auth_controller import AuthController
