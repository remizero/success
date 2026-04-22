# Python Libraries / Librerías Python

# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessException import SuccessException

# Preconditions / Precondiciones


class LoginException ( SuccessException ) :
  """
  Exception raised when authentication is required.

  Indicates that the user must be authenticated in the system to proceed.
  """

  def __init__ ( self ) :
    """
    Initialize the LoginException with a default message.

    Sets the message indicating that authentication is required.
    """
    self.message = "Debe estar autenticado en el sistema."
