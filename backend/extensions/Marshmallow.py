# Python Libraries / Librerías Python
from flask import Flask
from flask_marshmallow import Marshmallow as FlaskMarshmallow


# Application Libraries / Librerías de la Aplicación
from kernel import Extension
from utils import EnvVar


# Preconditions / Precondiciones


class Marshmallow ( Extension ) :

  __corsConfigDefault = {}
  __resources = None
  __supports_credentials = False

  def __init__ ( self ) -> None :
    super ().__init__ ()
    self.extension = FlaskMarshmallow ()

  def config ( self ) -> None :
    pass

  def register ( self, _app : Flask ) -> None :
    super ().register ( _app )
    self.extension.init_app ( app = _app )

  def userConfig ( self, **kwargs ) -> None :
    pass
