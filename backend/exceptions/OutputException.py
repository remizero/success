# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts import ExceptionAbs

# Preconditions / Precondiciones


class OutputException ( ExceptionAbs ) :

  def __init__ ( self ) :
    self.message = "No se ha definido un tipo de salida valida para la respuesta a ser enviada."
    