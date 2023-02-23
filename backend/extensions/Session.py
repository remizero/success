# Python Libraries / Librerías Python
from flask         import Flask
from flask_session import Session as FlaskSession


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts import Extension


# Preconditions / Precondiciones


class Session ( Extension ) :

  def __init__ ( self ) -> None :
    super ().__init__ ()
    self.extension = FlaskSession ()

  def config ( self ) -> None :
    pass

  def register ( self, _app : Flask ) -> None :
    super ().register ( _app )
    self.extension.init_app ( _app )

  def userConfig ( self, **kwargs ) -> None :
    pass
