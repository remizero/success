# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessException import SuccessException


# Preconditions / Precondiciones


class ValidJsonRequestException ( SuccessException ) :

  def __init__ ( self ) :
    self.message = "Error en los datos suministrados en el objeto JSON de la solicitud"
