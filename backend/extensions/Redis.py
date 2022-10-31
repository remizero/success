# Python Libraries / Librerías Python
from flask import Flask
from flask_redis import Redis as FlaskRedis


# Application Libraries / Librerías de la Aplicación
from kernel import Extension


# Preconditions / Precondiciones


class Redis ( Extension ) :

  def __init__ ( self ) -> None :
    super ().__init__ ()
    self.extension = FlaskRedis ()

  def config ( self ) -> None :
    pass

  def register ( self, _app : Flask ) -> None :
    super ().register ( _app )
    self.extension.init_app ( _app )

  def userConfig ( self, **kwargs ) -> None :
    pass
