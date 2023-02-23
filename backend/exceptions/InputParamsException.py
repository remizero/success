# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts import ExceptionAbs

# Preconditions / Precondiciones


class InputParamsException ( ExceptionAbs ) :

  def __init__ ( self, message : int ) :
    self.message = "La cantidad de parametros no son los esperados, debe recibir %d parametros"%message
    