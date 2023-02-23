# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts import Exception

# Preconditions / Precondiciones


class LoginException ( Exception ) :

  def __init__ ( self ) :
    self.message = "Debe estar autenticado en el sistema."
    