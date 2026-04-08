# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessException import SuccessException


# Preconditions / Precondiciones


class StringException ( SuccessException ) :

  def __init__ ( self ) :
    self.message = "Se requiere un valor de tipo cadena"
