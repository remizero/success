# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts import ExceptionAbs


# Preconditions / Precondiciones


class RevokeJwtException ( ExceptionAbs ) :

  def __init__ ( self ) :
    self.message = "JWToken no ha podido ser revocado con éxito"
