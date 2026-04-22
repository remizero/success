# Python Libraries / Librerías Python

# Success Libraries / Librerías Success
from success.engine.io.SuccessOutputModelContract import SuccessOutputModelContract

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessDefaultOutputModel ( SuccessOutputModelContract ) :
  """
  Default output model for simple success/error responses.

  Provides minimal output structure with success flag,
  data, and error information.
  """


  def __init__ ( self ) :
    """
    Initialize the basic output model.
    """
    super ().__init__ ()


  def build ( self, canonicalOutput : dict ) -> dict :
    """
    Build the output from canonical format.

    Args:
      canonicalOutput: Canonical output dictionary.

    Returns:
      dict: Built output with success/data or error info.
    """
    if not canonicalOutput.get ( "success", False ) :
      error = canonicalOutput.get ( "error", {} ) or {}
      return {
        'success' : False,
        'msg'     : error.get ( "detail", canonicalOutput.get ( "message" ) ),
        'type'    : error.get ( "type", "unknown" ),
        'status'  : canonicalOutput.get ( "status", 500 )
      }

    return {
      'success' : True,
      'data'    : canonicalOutput.get ( "data" )
    }
