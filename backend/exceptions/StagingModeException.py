# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts import Exception

# Preconditions / Precondiciones


class StagingModeException ( Exception ) :

  def __init__ ( self ) :
    self.message = "Modo Staging activado, por lo que debe habilitar el \
      modo Produccion FLASK_ENV = 'production'."
    