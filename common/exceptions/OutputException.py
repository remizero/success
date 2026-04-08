# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessException import SuccessException

# Preconditions / Precondiciones


class OutputException ( SuccessException ) :

  def __init__ ( self ) :
    self.message = "No se ha definido un tipo de salida valida para la respuesta a ser enviada."
    