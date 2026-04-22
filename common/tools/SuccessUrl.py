# Python Libraries / Librerías Python
from flask import redirect
from flask import request
from flask import url_for

# Success Libraries / Librerías Success
from success.common.tools.SuccessUrlBuilder       import SuccessUrlBuilder
from success.common.infra.config.SuccessSystemEnv import SuccessSystemEnv
from success.core.app.SuccessDispatchMode         import SuccessDispatchMode

# Preconditions / Precondiciones


class SuccessUrl () :
  """
  URL utilities for the Success framework.

  Provides static methods for generating URLs and redirects
  with support for different dispatch modes (subdomain, path, standard).
  """


  @staticmethod
  def urlFor ( Action, app = None, external = True, **values ) :
    """
    Generate a URL for a given action.

    Args:
      Action: Action name or endpoint.
      app: Optional application name for subdomain/path mode.
      external: Whether to generate an external URL.
      **values: Additional URL values.

    Returns:
      str: Generated URL based on the dispatch mode.
    """
    rawMode = SuccessSystemEnv.get (
      "SUCCESS_APP_MODE",
      SuccessSystemEnv.get ( "SUCCESS_APP_DOMAIN", "standard" )
    )
    try :
      modo = SuccessDispatchMode ( str ( rawMode ).strip ().lower () )
    except ValueError :
      modo = SuccessDispatchMode.STANDARD

    if modo == SuccessDispatchMode.SUBDOMAIN and app :
      host = request.host.split ( ":" ) [ 0 ]
      port = f":{request.host.split ( ':' ) [ 1 ]}" if ':' in request.host else ""
      base_domain = SuccessSystemEnv.get ( "SERVER_NAME", host )
      full_host = SuccessUrlBuilder ().subdomain ( app ).domain ( base_domain ).port ( port.lstrip ( ":" ) ).build ()
      if not full_host :
        return url_for ( Action, _external = external, **values )
      return url_for ( Action, _external = True, _scheme = request.scheme, **values ).replace ( request.host, full_host )

    if modo == SuccessDispatchMode.PATH and app :
      return f"/{app}{url_for ( Action, _external = False, **values )}"

    return url_for ( Action, _external = external, **values )


  @staticmethod
  def redirect ( Action, app = None, code = 302, **values ) :
    """
    Redirect to a given action.

    Args:
      Action: Action name or endpoint.
      app: Optional application name for subdomain/path mode.
      code: HTTP redirect status code (default: 302).
      **values: Additional URL values.

    Returns:
      Flask redirect response.
    """
    url = SuccessUrl.urlFor ( Action, app = app, **values )
    return redirect ( url, code = code )
