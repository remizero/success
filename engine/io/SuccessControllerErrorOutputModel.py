# Python Libraries / Librerías Python

# Success Libraries / Librerías Success
from success.engine.io.SuccessOutputModelContract import SuccessOutputModelContract

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessControllerErrorOutputModel ( SuccessOutputModelContract ) :
  """
  Output model for controller error responses.

  Formats controller errors with appropriate structure
  including success flag, message, type, and status.
  """


  def __init__ ( self ) :
    """
    Initialize the controller error output model.
    """
    super ().__init__ ()


  def build ( self, canonicalOutput : dict ) -> dict :
    """
    Build the output from canonical format for controller errors.

    Args:
      canonicalOutput: Canonical output dictionary.

    Returns:
      dict: Built output with controller error information.
    """
    error = canonicalOutput.get ( "error", {} ) or {}
    return {
      'success' : False,
      'msg'     : error.get ( "detail", canonicalOutput.get ( "message" ) ),
      'type'    : error.get ( "type", "controller" ),
      'status'  : canonicalOutput.get ( "status", 500 )
    }
