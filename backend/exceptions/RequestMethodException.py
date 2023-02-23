# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts import ExceptionAbs


# Preconditions / Precondiciones


class RequestMethodException ( ExceptionAbs ) :

  def __init__ ( self, message : str ) :
    self.message = "Error en el metodo de la solicitud, el metodo debe ser de tipo $s"%message
