# Python Libraries / Librerías Python
from flask import Response
from flask import redirect
from flask import url_for

# Success Libraries / Librerías Success
from success.engine.context.SuccessResponsePolicy import SuccessResponsePolicy
from success.engine.io.SuccessIntent              import SuccessIntent

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class RedirectIntent ( SuccessIntent ) :
  """
  Redirect intent executor for HTTP redirects.

  Executes output by performing an HTTP redirect to the
  specified target with context data.

  Attributes:
    _target (str): Target endpoint for redirect.
  """

  _target : str  = None


  def __init__ ( self, target : str ) -> None :
    """
    Initialize the redirect intent.

    Args:
      target: Target endpoint name for redirect.
    """
    super ().__init__ ()
    self._target = target


  def execute ( self, builtOutput : dict, responsePolicy : SuccessResponsePolicy ) -> Response :
    """
    Execute the redirect intent.

    Args:
      builtOutput: Built output dictionary.
      responsePolicy: Response policy for configuration.

    Returns:
      Response: Flask redirect response.
    """
    context = responsePolicy.resolve_redirect_context ( builtOutput )
    response = redirect ( url_for ( self._target, **context ) )

    responseMeta = builtOutput.get ( "response", {} ) if isinstance ( builtOutput, dict ) else {}
    headers = responseMeta.get ( "headers", {} ) if isinstance ( responseMeta, dict ) else {}
    if isinstance ( headers, dict ) :
      for key, value in headers.items () :
        response.headers [ key ] = value

    cookies = responseMeta.get ( "cookies", [] ) if isinstance ( responseMeta, dict ) else []
    if isinstance ( cookies, list ) :
      for cookie in cookies :
        if not isinstance ( cookie, dict ) :
          continue
        cookieKey = cookie.get ( "key" )
        if not cookieKey :
          continue
        cookieValue = cookie.get ( "value", "" )
        cookieKwargs = cookie.get ( "kwargs", {} )
        if not isinstance ( cookieKwargs, dict ) :
          cookieKwargs = {}
        response.set_cookie ( cookieKey, cookieValue, **cookieKwargs )

    return response
