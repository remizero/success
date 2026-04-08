# Python Libraries / Librerías Python
from flask       import Flask
from flask_redis import FlaskRedis

# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessExtension import SuccessExtension
from success.common.tools.SuccessEnv      import SuccessEnv

# Preconditions / Precondiciones


class SuccessRedisExtension ( SuccessExtension ) :


  def __init__ ( self, app : Flask ) -> None :
    super ().__init__ ( app )
    self._extension = FlaskRedis ()
