# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts import ExceptionAbs


# Preconditions / Precondiciones


class StringException ( ExceptionAbs ) :

  def __init__ ( self ) :
    self.message = "Se requiere un valor de tipo cadena"
