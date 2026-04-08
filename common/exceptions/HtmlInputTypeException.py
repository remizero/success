# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessException import SuccessException

# Preconditions / Precondiciones


class HtmlInputTypeException ( SuccessException ) :

  def __init__ ( self ) :
    self.message = "Modo Desarrollo activado, por lo que debe habilitar el \
      modo SuccessDebug = True, y debe deshabilitar el \
      modo Testing = False y \
      modo Staging = False"
    