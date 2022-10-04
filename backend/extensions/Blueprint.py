# Python Libraries / Librerías Python
from flask import (
  Blueprint as FlaskBlueprint,
  Flask
)


# Application Libraries / Librerías de la Aplicación
from kernel import Extension


# Preconditions / Precondiciones


class Blueprint ( Extension ) :

  def __init__ ( self, name : str, importName : str, urlPrefix : str ) -> None :
    super ().__init__ ()
    self.extension = FlaskBlueprint ( name = name, import_name = importName, url_prefix = urlPrefix )

  def config ( self ) -> None :
    pass

  def register ( self, _app : Flask ) -> None :
    super ().register ( _app )
    self.extension.init_app ( _app )

  def userConfig ( self, **kwargs ) -> None :
    pass
