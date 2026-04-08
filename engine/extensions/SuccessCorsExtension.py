# Python Libraries / Librerías Python
from flask      import Flask
from flask_cors import CORS

# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessExtension import SuccessExtension
from success.common.tools.SuccessEnv      import SuccessEnv

# Preconditions / Precondiciones


class SuccessCorsExtension ( SuccessExtension ) :

  _corsConfigDefault   : dict = {}
  _resources           : dict = None
  _supportsCredentials : bool = False


  def __init__ ( self, app : Flask ) -> None :
    super ().__init__ ( app )
    self._extension = CORS ()
    self._corsConfigDefault = {
      r"*" : {
        "origins"        : [ "/*" ],
        "methods"        : [ "DELETE", "GET", "POST", "PUT" ],
        "allow_headers"  : [ "Authorization", "Content-Type", "X-Requested-With", "Accept", "Set-Cookie" ],
        "expose_headers" : [ "Content-Type", "X-CSRFToken" ]
      }
    }
    self.config ()


  def config ( self ) -> None :
    # DO NOT MODIFY (BEGIN) / NO MODIFICAR (INICIO)
    if ( not SuccessEnv.isEmpty ( self._app.config [ 'CORS_RESOURCES_APP_RESOURCES' ] ) ) :
      self._resources = self._corsConfigDefault
      #self._resources = SuccessSystemEnv.getCorsResources ()

    elif ( not SuccessSystemEnv.isEmpty ( 'CORS_RESOURCES' ) ) :
      # TODO Que hacer aqui
      self._resources = self._corsConfigDefault

    else :
      self._resources = self._corsConfigDefault
    # DO NOT MODIFY (END) / NO MODIFICAR (FIN)


  def register ( self ) -> None :
    # super ().register ( self._app )
    if ( self._app.config [ 'CORS_SUPPORTS_CREDENTIALS' ] != '' ) :
      self._supportsCredentials = SuccessEnv.isTrue ( self._app.config [ 'CORS_SUPPORTS_CREDENTIALS' ] )
    self._extension.init_app (
      app                  = self._app,
      resources            = self._resources,
      supports_credentials = self._supportsCredentials
    )
