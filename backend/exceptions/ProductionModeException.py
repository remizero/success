# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts import ExceptionAbs

# Preconditions / Precondiciones


class ProductionModeException ( ExceptionAbs ) :

  def __init__ ( self ) :
    self.message = "Modo Produccion activado, por lo que debe deshabilitar el \
      modo Debug = False, \
      modo Testing = False y \
      modo Staging = False"
    