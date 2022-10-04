# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.Exception import Exception

# Preconditions / Precondiciones


class InputParamsException ( Exception ) :

  def __init__ ( self, message : int ) :
    self.message = "La cantidad de parametros no son los esperados, debe recibir %d parametros"%message
    