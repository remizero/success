# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts import ExceptionAbs


# Preconditions / Precondiciones


class ValidJsonRequestException ( ExceptionAbs ) :

  def __init__ ( self ) :
    self.message = "Error en los datos suministrados en el objeto JSON de la solicitud"
