# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessException import SuccessException


# Preconditions / Precondiciones


class RevokeJwtException ( SuccessException ) :

  def __init__ ( self ) :
    self.message = "JWToken no ha podido ser revocado con éxito"
