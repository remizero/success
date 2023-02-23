# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts import Exception


# Preconditions / Precondiciones


class StringException ( Exception ) :

  def __init__ ( self ) :
    self.message = "Se requiere un valor de tipo cadena"
