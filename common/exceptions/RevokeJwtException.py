# Python Libraries / Librerías Python

# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessException import SuccessException

# Preconditions / Precondiciones


class RevokeJwtException ( SuccessException ) :
  """
  Exception raised when JWT revocation fails.

  Indicates that the JWT token could not be successfully revoked.
  """

  def __init__ ( self ) :
    """
    Initialize the RevokeJwtException with a default message.

    Sets the message indicating that the JWT token could not be revoked successfully.
    """
    self.message = "JWToken no ha podido ser revocado con éxito."
