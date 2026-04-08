# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessException import SuccessException

# Preconditions / Precondiciones


class InputParamsException ( SuccessException ) :

  def __init__ ( self, message : int ) :
    self.message = "La cantidad de parametros no son los esperados, debe recibir %d parametros"%message
    