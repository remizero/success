# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessException import SuccessException

# Preconditions / Precondiciones


class ProductionModeException ( SuccessException ) :

  def __init__ ( self ) :
    self.message = "Modo Produccion activado, por lo que debe deshabilitar el \
      modo SuccessDebug = False, \
      modo Testing = False y \
      modo Staging = False"
    