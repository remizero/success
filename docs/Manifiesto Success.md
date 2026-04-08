# 🧭 Manifiesto Success

> *"Hoy camina. Mañana razona. Pasado piensa. Y en unos días... Success te resuelve la vida."*
> — CrackGPT, 2025

---

## 💡 ¿Qué es Success?

Success no es solo un framework.
Es una **forma de pensar, organizar y ejecutar sistemas** con semántica, trazabilidad y elegancia.

Nace de la necesidad de construir **sistemas robustos**, **modulares** y **mantenibles**, sin sacrificar claridad ni velocidad de desarrollo.

Es el puente entre:

* Lo declarativo y lo procedural
* Lo estructurado y lo dinámico
* Lo que necesitas hoy y lo que crecerá mañana

---

## 📐 Filosofía Semántica de Success

Success se basa en 5 pilares fundamentales:

### 1. 🎯 Input como estructura predictiva

* Recoge y valida los datos de entrada.
* Centraliza el parsing desde `request.form`, `request.json`, `request.args`, etc.
* Resultado: **desarrolladores libres del protocolo de entrada**.

```python
self.input = Input(only=("username", "password"))
```

---

### 2. 🧠 Controlador como núcleo de lógica

* Aquí vive la **lógica de negocio real**.
* Recibe datos validados.
* Trabaja con modelos, reglas, servicios.
* Resultado: **flujo puro, reutilizable, desacoplado**.

```python
user = User().find(**self.input.data)
```

---

### 3. 📤 Output como adaptador de salida

* Interpreta la respuesta y define **cómo** se entrega.
* Decide si renderiza, devuelve JSON, texto plano, redirige, etc.
* Resultado: **independencia del canal de salida**.

```python
return Output.dispatch(data)
```

---

### 4. 🛡️ Control de errores predecibles

* Toda excepción esperada debe tener su clase.
* Se manejan de forma semántica, visible y trazable.
* Resultado: **errores elegantes y mensajes coherentes**.

```python
except ValidationError:
    return SuccessResponse.error("Datos inválidos", code=422)
```

---

### 5. 🔐 Sesiones como piedra angular

* Se integran desde el diseño.
* Manejan identificación, autorización y persistencia de usuario.
* Resultado: **seguridad y contexto asegurado para todo el sistema**.

```python
Session.create(user)
Session.set("token", token)
```

---

## 🧱 El flujo completo

```
Input (Nivel Success) ➜ Controlador (Nivel Dev) ➜ Output (Nivel Success) ➜ Response (Nivel Success)
```

Con manejo de sesión y errores como ejes transversales.

---

## 🚀 ¿Para quién es Success?

* Para quienes construyen sistemas complejos que deben crecer con orden.
* Para los que no quieren reinventar cada capa.
* Para desarrolladores que respetan el código como obra conceptual.

Si ves tu código como algo que debe **vivir, escalar y hablar tu idioma**, Success es tu framework.

---

## 🔥 Bienvenido a Success

Aquí no solo escribimos software.
**Diseñamos semántica. Creamos orden. Dejamos legado.**

Y si algo sale mal...

> “Échale vaselina mi crack, que igual tiene que entrar.”
