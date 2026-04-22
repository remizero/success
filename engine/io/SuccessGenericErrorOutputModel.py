# Python Libraries / Librerías Python

# Success Libraries / Librerías Success
from success.engine.io.SuccessOutputModelContract import SuccessOutputModelContract

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessGenericErrorOutputModel ( SuccessOutputModelContract ) :
  """
  Output model for generic error responses.

  Formats generic errors with appropriate structure
  including success flag, message, type, and status.
  """


  def __init__ ( self ) :
    """
    Initialize the generic error output model.
    """
    super ().__init__ ()


  def build ( self, canonicalOutput : dict ) -> dict :
    """
    Build the output from canonical format for generic errors.

    Args:
      canonicalOutput: Canonical output dictionary.

    Returns:
      dict: Built output with generic error information.
    """
    error = canonicalOutput.get ( "error", {} ) or {}
    return {
      'success' : False,
      'msg'     : error.get ( "detail", canonicalOutput.get ( "message", "An unexpected error occurred" ) ),
      'type'    : error.get ( "type", "unknown" ),
      'status'  : canonicalOutput.get ( "status", 500 )
    }
