# Python Libraries / Librerías Python

# Success Libraries / Librerías Success
from success.common.base.SuccessClass import SuccessClass

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessPostOutputPolicy ( SuccessClass ) :
  """
  Post-output policy handler.

  Applies policies to the output after it has been built,
  including normalization, metadata, headers, and cookies.
  """


  def __init__ ( self ) -> None :
    """
    Initialize the post-output policy handler.
    """
    super ().__init__ ()


  def apply ( self, builtOutput, responsePolicy ) -> dict :
    """
    Apply post-output policies to the built output.

    This is the central point for post-output policies:
    - Final payload normalization
    - Response metadata (mimetype/content_type/etc)
    - Headers/cookies (if defined in output model)

    Args:
      builtOutput: The built output dictionary.
      responsePolicy: Response policy to apply.

    Returns:
      dict: Modified output with applied policies.
    """
    if not isinstance ( builtOutput, dict ) :
      builtOutput = { "data" : builtOutput }

    responseMeta = builtOutput.get ( "response", {} ) or {}
    if not isinstance ( responseMeta, dict ) :
      responseMeta = {}

    kwargs = responseMeta.get ( "kwargs", {} ) or {}
    if not isinstance ( kwargs, dict ) :
      kwargs = {}

    defaults = responsePolicy.response_kwargs ()
    merged = defaults.copy ()
    merged.update ( kwargs )
    responseMeta [ "kwargs" ] = merged

    headers = responseMeta.get ( "headers", {} ) or {}
    if not isinstance ( headers, dict ) :
      headers = {}
    responseMeta [ "headers" ] = headers

    cookies = responseMeta.get ( "cookies", [] ) or []
    if not isinstance ( cookies, list ) :
      cookies = []
    responseMeta [ "cookies" ] = cookies

    builtOutput [ "response" ] = responseMeta
    return builtOutput
