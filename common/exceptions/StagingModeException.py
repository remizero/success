# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessException import SuccessException

# Preconditions / Precondiciones


class StagingModeException ( SuccessException ) :

  def __init__ ( self ) :
    self.message = "Modo Staging activado, por lo que debe habilitar el \
      modo Produccion FLASK_ENV = 'production'."
    