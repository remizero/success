# Python Libraries / Librerías Python

# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessException import SuccessException

# Preconditions / Precondiciones


class OutputException ( SuccessException ) :
  """
  Exception raised when no valid output type is defined.

  Indicates that a valid output type must be defined for the response to be sent.
  """

  def __init__ ( self ) :
    """
    Initialize the OutputException with a default message.

    Sets the message indicating that no valid output type has been defined for the response.
    """
    self.message = "No se ha definido un tipo de salida valida para la respuesta a ser enviada."
