# Python Libraries / Librerías Python
from threading     import Lock
# from werkzeug.wsgi import get_path_info
# from werkzeug.wsgi import pop_path_info
from wsgiref.util import shift_path_info

# Success Libraries / Librerías Success
from success.common.base.SuccessClass import SuccessClass

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessPathDispatcher ( SuccessClass ) :


  def __init__ ( self, default_app, create_apps ) :
    super ().__init__ ()
    self.default_app = default_app
    self.create_apps = create_apps  # Diccionario mount_path => app
    self.lock = Lock ()
    self.instances = {}
    self._logger.log ( "Cargando el sub-sistema SuccessPathDispatcher.", "INFO" )


  def get_application ( self, prefix ) :
    with self.lock :
      app = self.instances.get ( prefix )
      if app is None :
        app = self.create_apps.get ( f"/{prefix}" )
        if app is not None :
          self.instances [ prefix ] = app
      return app


  def __call__ ( self, environ, start_response ) :
    # path = get_path_info ( environ ).lstrip ( "/" ).split ( "/", 1 ) [ 0 ]
    # app = self.get_application ( path )
    app = self._get_application ( self._peek_path_info ( environ ) )

    if app is not None :
      shift_path_info ( environ )
      # pop_path_info ( environ )

    else :
      app = self.default_app

    return app ( environ, start_response )


  def _peek_path_info ( environ : dict [ str, str ] | dict ) -> str | None :
    """
    Devuelve el primer segmento del PATH_INFO sin modificar el entorno.
    """
    path = environ.get ( "PATH_INFO", "" ).lstrip ( "/" )
    return path.split ( "/", 1 ) [ 0 ] if path else None

