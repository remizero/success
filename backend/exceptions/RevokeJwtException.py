# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.Exception import Exception


# Preconditions / Precondiciones


class RevokeJwtException ( Exception ) :

  def __init__ ( self ) :
    self.message = "JWToken no ha podido ser revocado con éxito"
