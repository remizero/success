# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.Exception import Exception


# Preconditions / Precondiciones


class JsonRequestException ( Exception ) :

  def __init__ ( self ) :
    self.message = "Se requiere un objeto de tipo JSON en la solicitud"
