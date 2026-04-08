# @app.before_first_request
# def validate_route_sanitization():
#     if SuccessSystemEnv.isProd():
#         for rule in app.url_map.iter_rules():
#             if "apps" in rule.rule or "services" in rule.rule:
#                 raise RuntimeError(
#                     f"🚫 Ruta insegura detectada en producción: {rule.rule}. "
#                     "Debe enmascararse para ocultar estructura interna."
#                 )
