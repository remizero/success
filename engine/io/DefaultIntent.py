# Python Libraries / Librerías Python
from flask import Response
from flask import make_response

# Success Libraries / Librerías Success
from success.engine.context.SuccessResponsePolicy import SuccessResponsePolicy
from success.engine.io.SuccessIntent              import SuccessIntent

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class DefaultIntent ( SuccessIntent ) :
  """
  Default intent executor for standard JSON responses.

  Executes output by creating a standard Flask response with
  appropriate status code, headers, and cookies.
  """


  def execute ( self, builtOutput : dict, responsePolicy : SuccessResponsePolicy ) -> Response :
    """
    Execute the default intent by creating a Flask response.

    Args:
      builtOutput: Built output dictionary.
      responsePolicy: Response policy for configuration.

    Returns:
      Response: Flask response object.
    """
    statusCode = responsePolicy.resolve_status ( builtOutput )
    response = make_response ( builtOutput, statusCode )
    kwargs = responsePolicy.response_kwargs ( builtOutput )
    if kwargs.get ( "mimetype" ) :
      response.mimetype = kwargs.get ( "mimetype" )
    if kwargs.get ( "content_type" ) :
      response.content_type = kwargs.get ( "content_type" )

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
