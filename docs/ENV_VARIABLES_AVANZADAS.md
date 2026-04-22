# Variables de entorno advanceds en Success. 🔐

Esta guía cubre estrategias advanceds para `.env` en entornos reales: multi-app, subdominios, seguridad y overrides por aplicación.

---

## Get started now.

[Estrategias](#estrategias-advanceds)

---

## Table of contents. 📑

* [Estrategias advanceds](#estrategias-advanceds)
* [Escenario multi-app](#escenario-multi-app)
* [Escenario subdomain](#escenario-subdomain)
* [Seguridad de secretos](#seguridad-de-secretos)
* [Checklist de despliegue](#checklist-de-despliegue)
* [Next step](#paso-siguiente)

---

## Estrategias advanceds.

* Homologar variables comunes entre apps.
* Sobrescribir solo lo que cambia por app.
* Forzar configuración explícita en producción.

---

## Escenario multi-app.

Cuando hay varias apps en `apps/`:

* Cada app mantiene su propio `.env`.
* Las variables de dominio (`SERVER_NAME`, `APP_PORT`) deben estar alineadas con el modo de dispatch.
* Evita copiar `.env` completo si solo cambian dos o tres valores.

---

## Escenario subdomain.

Para `SUCCESS_APP_MODE=subdomain`:

* Define `SERVER_NAME` válido.
* Mantén `SUCCESS_HOST_MATCHING=True`.
* Define `host` por endpoint solo cuando necesites override específico.

---

## Seguridad de secretos.

* No expongas `SECRET_KEY`, `API_KEY`, `JWT_SECRET_KEY` en repositorios.
* Usa inyección de secretos por entorno.
* Rota claves periódicamente.

---

## Checklist de despliegue.

* ¿Se removieron secretos de ejemplo?
* ¿Los puertos y dominios coinciden con infraestructura real?
* ¿Las extensiones habilitadas tienen configuración completa?
* ¿El modo de políticas está definido (`SUCCESS_POLICY_MODE` si aplica)?

---

## Next step. 🔗

[BLUEPRINTS_AVANZADOS.md](BLUEPRINTS_AVANZADOS.md)
