# Python Libraries / Librerías Python

# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessException import SuccessException

# Preconditions / Precondiciones


class RequestMethodException ( SuccessException ) :
  """
  Exception raised when there is an error in the request method.

  Indicates that the request method must be of a specific type.
  """

  def __init__ ( self, message : str ) :
    """
    Initialize the RequestMethodException with a custom message.

    Args:
      message (str): The expected request method type to include in the error message.
    """
    self.message = "Error en el metodo de la solicitud, el metodo debe ser de tipo $s."%message
