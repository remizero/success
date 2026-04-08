# 📦 Infrastructure

Este directorio contiene **adaptadores técnicos** y componentes que permiten que la aplicación interactúe con sistemas **externos** o **infraestructuras ajenas al dominio principal**.

## 🎯 Propósito

`infrastructure/` existe para alojar piezas que hacen posible la ejecución de ciertas tareas, pero **no deciden lógica de negocio**, ni **forman parte del core funcional** del sistema. Representan *el "cómo se hace"*, no *el "qué se hace"*.

## ✅ Ejemplos comunes

- Conexiones a bases de datos externas (legacy, no gestionadas por el ORM del sistema).
- Clientes de APIs REST, SOAP o GraphQL de terceros.
- Integraciones con sistemas de almacenamiento de archivos (local, FTP, S3...).
- Adaptadores para sistemas de vectores (ChromaDB, FAISS...).
- Clientes para colas (SuccessRedisExtension, RabbitMQ, Kafka...).
- Envío de correos o notificaciones.
- Enlaces con librerías externas (C++, Java, binarios...).

## 🔥 Filosofía Success

> El directorio `infrastructure/` no necesita preexistir ni tener estructura predeterminada. Se crea **solo cuando una necesidad real lo exige**.

Esto evita confusiones, reduce el ruido visual y favorece la autonomía técnica del desarrollador.

## ⚠️ Importante

- **No coloques aquí lógica de negocio.**
- **No pongas modelos de datos.**
- **No lo confundas con `services/` o `controllers/`.**

---

✍️ Si tu controlador necesita acceder a un recurso externo, importa desde aquí:

```python
from apps.mi_app.infrastructure.chomadb.client import ChromaClient
