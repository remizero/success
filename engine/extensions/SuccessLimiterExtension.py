# Python Libraries / Librerías Python
from flask              import Flask
from flask_limiter      import Limiter
from flask_limiter.util import get_remote_address

# Success Libraries / Librerías Success
from success.common.base.SuccessExtension import SuccessExtension

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessLimiterExtension ( SuccessExtension ) :
  """
  Rate Limiter extension for the Success framework.

  Integrates Flask-Limiter for rate limiting and
  request throttling based on remote address.
  """

  def __init__ ( self, app : Flask ) -> None :
    """
    Initialize the Rate Limiter extension.

    Args:
      app: Flask application instance.
    """
    super ().__init__ ( app )
    self._extension = Limiter (
      key_func = get_remote_address
    )
