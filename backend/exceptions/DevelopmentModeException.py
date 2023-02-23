# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts import ExceptionAbs


# Preconditions / Precondiciones


class DevelopmentModeException ( ExceptionAbs ) :

  def __init__ ( self ) :
    super ().__init__ ()
    self.message = "Modo Desarrollo activado, por lo que debe habilitar el \
      modo Debug = True, y debe deshabilitar el \
      modo Testing = False y \
      modo Staging = False"
    