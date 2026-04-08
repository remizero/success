# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessException import SuccessException


# Preconditions / Precondiciones


class RequestMethodException ( SuccessException ) :

  def __init__ ( self, message : str ) :
    self.message = "Error en el metodo de la solicitud, el metodo debe ser de tipo $s"%message
