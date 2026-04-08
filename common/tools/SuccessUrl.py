# Python Libraries / Librerías Python
from flask import redirect
from flask import request
from flask import url_for

# Success Libraries / Librerías Success
from success.common.tools.SuccessEnv  import SuccessEnv
from success.core.SuccessDispatchMode import SuccessDispatchMode

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones



class SuccessUrl () :


  @staticmethod
  def urlFor ( Action, app = None, external = True, **values ) :
    modo = SuccessDispatchMode ( SuccessSystemEnv.get ( "SUCCESS_APP_DOMAIN", "standard" ).strip ().lower () )

    if modo == "subdomain" and app :
      host = request.host.split ( ":" ) [ 0 ]
      port = f":{request.host.split ( ':' ) [ 1 ]}" if ':' in request.host else ""
      base_domain = domain
      full_host = f"{app}.{base_domain}{port}"
      return url_for ( Action, _external = True, _scheme = request.scheme, **values ).replace ( request.host, full_host )

    if modo == "path" and app :
      return f"/{app}{url_for ( Action, _external = False, **values )}"

    return url_for ( Action, _external = external, **values )


  @staticmethod
  def redirect ( Action, app = None, code = 302, **values ) :
    url = success_url_for ( Action, app = app, **values )
    return redirect ( url, code = code )
