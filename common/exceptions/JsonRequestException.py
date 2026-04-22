# Python Libraries / Librerías Python

# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessException import SuccessException

# Preconditions / Precondiciones


class JsonRequestException ( SuccessException ) :
  """
  Exception raised when a JSON object is required in the request.

  Indicates that the request body must contain a valid JSON object.
  """

  def __init__ ( self ) :
    """
    Initialize the JsonRequestException with a default message.

    Sets the message indicating that a JSON object is required in the request.
    """
    self.message = "Se requiere un objeto de tipo JSON en la solicitud."
