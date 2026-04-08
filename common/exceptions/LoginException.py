# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessException import SuccessException

# Preconditions / Precondiciones


class LoginException ( SuccessException ) :

  def __init__ ( self ) :
    self.message = "Debe estar autenticado en el sistema."
    