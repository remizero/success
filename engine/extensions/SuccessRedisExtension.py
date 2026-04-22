# Python Libraries / Librerías Python
from flask       import Flask
from flask_redis import FlaskRedis

# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessExtension import SuccessExtension

# Preconditions / Precondiciones


class SuccessRedisExtension ( SuccessExtension ) :
  """
  Redis extension for the Success framework.

  Integrates Flask-Redis for Redis connection management
  and caching operations.
  """


  def __init__ ( self, app : Flask ) -> None :
    """
    Initialize the Redis extension.

    Args:
      app: Flask application instance.
    """
    super ().__init__ ( app )
    self._extension = FlaskRedis ()
