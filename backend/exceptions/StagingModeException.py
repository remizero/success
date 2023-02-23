# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts import ExceptionAbs

# Preconditions / Precondiciones


class StagingModeException ( ExceptionAbs ) :

  def __init__ ( self ) :
    self.message = "Modo Staging activado, por lo que debe habilitar el \
      modo Produccion FLASK_ENV = 'production'."
    