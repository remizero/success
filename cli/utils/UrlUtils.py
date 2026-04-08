


class UrlUtils () :


  def build_endpoint_name ( app : str, protocol : str, service : str, version : str, module : str, action : str ) -> str :
    """
    Genera el nombre completo del Action para usar en `as_view(...)` y `url_for(...)`.
    Ejemplo: "prueba_view.view.chromadb.v1.admin.dashboard"
    """
    return f"{app}.{protocol}.{service}.{version}.{module}.{action}"


  def build_url_prefix(protocol: str, service: str, version: str, module: str) -> str:
    """
    Genera el prefix semántico del blueprint.
    Ejemplo: "/view/chromadb/v1/admin"
    """
    return f"/{protocol}/{service}/{version}/{module}"


# Crear blueprint
bp = Blueprint(
    name=f"{module}_{protocol}",
    import_name=__name__,
    url_prefix=build_url_prefix(protocol, service, version, module)
)

# Registrar acción
bp.add_url_rule(
    f"/{action}",
    view_func=Action.as_view(build_endpoint_name(app, protocol, service, version, module, action)),
    methods=["GET", "POST"]
)