# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts import ExceptionAbs

# Preconditions / Precondiciones


class LoginException ( ExceptionAbs ) :

  def __init__ ( self ) :
    self.message = "Debe estar autenticado en el sistema."
    