# Python Libraries / Librerías Python
from flask              import Flask
from flask_limiter      import Limiter
from flask_limiter.util import get_remote_address

# Success Libraries / Librerías Success
from success.common.base.SuccessExtension import SuccessExtension

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class RateLimiterExtension ( SuccessExtension ) :

  def __init__ ( self, app : Flask ) -> None :
    super ().__init__ ( app )
    self._extension = Limiter (
      key_func = get_remote_address
    )
