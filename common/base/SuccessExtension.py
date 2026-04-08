# Python Libraries / Librerías Python
from flask import Flask

# Success Libraries / Librerías Success
from success.common.base.SuccessClass import SuccessClass

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessExtension ( SuccessClass ) :

  _extension         = None
  _app       : Flask = None


  def __init__ ( self, app : Flask ) -> None :
    super ().__init__ ()
    self._app = app


  def config ( self ) -> None :
    pass


  def register ( self ) -> None :
    if self._extension and hasattr ( self._extension, "init_app" ) :
      self._extension.init_app ( self._app )

    else :
      raise RuntimeError ( f"La extensión {self.__class__.__name__} no define correctamente 'self._extension' o no implementa 'init_app'" )


  def userConfig ( self, **kwargs ) -> None :
    self._app.config.update ( kwargs )
