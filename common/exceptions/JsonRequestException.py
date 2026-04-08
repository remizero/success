# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessException import SuccessException


# Preconditions / Precondiciones


class JsonRequestException ( SuccessException ) :

  def __init__ ( self ) :
    self.message = "Se requiere un objeto de tipo JSON en la solicitud."
