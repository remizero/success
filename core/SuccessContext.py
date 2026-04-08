# Python Libraries / Librerías Python
from flask       import Flask
from threading   import Lock
from contextvars import ContextVar

# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessExtension      import SuccessExtension
from success.common.tools.SuccessEnv           import SuccessEnv
from success.common.tools.SuccessStructs       import SuccessStructs
from success.common.infra.logger.SuccessLogger import SuccessLogger

# Preconditions / Precondiciones
CURRENT_APP = ContextVar ( "CURRENT_APP" )


class SuccessContext () :

  __context    : dict = {}
  __apps       : dict = {}
  __extensions : dict = {}
  __states     : dict = {}
  _instance           = None
  _lock        : Lock = Lock ()

  breadcrumb_current = None
  breadcrumb_scope = "chromadb"


  def __new__ ( cls ) :
    if not cls._instance :
      with cls._lock :
        if not cls._instance :
          cls._instance = super ().__new__ ( cls )
          cls._instance.__apps       = {}
          cls._instance.__states     = {}
          cls._instance.__extensions = {}
          cls._instance.__context    = {}

    return cls._instance


  def setApp ( self, appInstance : Flask ) -> None :
    apps = self.getCurrentAppName ()
    if apps not in self.__context [ "success" ] [ "apps" ] :
      self.__context [ "success" ] [ "apps" ].update ( SuccessStructs.successContextApp ( apps.lower () ) )

    self.__context [ "success" ] [ "apps" ] [ apps.lower () ] [ "instance" ] = appInstance


  def getApp ( self ) -> Flask :
    apps = self.getCurrentAppName ()
    return self.__context [ "success" ] [ "apps" ] [ apps.lower () ] [ "instance" ]


  def setAppModule ( self, module ) -> None :
    apps = self.getCurrentAppName ()
    if apps not in self.__context [ "success" ] [ "apps" ] :
      return

    self.__context [ "success" ] [ "apps" ] [ apps.lower () ] [ "module" ] = module


  def getAppModule ( self ) :
    apps = self.getCurrentAppName ()
    if apps not in self.__context [ "success" ] [ "apps" ] :
      return
    return self.__context [ "success" ] [ "apps" ] [ apps.lower () ] [ "module" ]


  def getContext ( self ) -> dict :
    return self.__context


  def setContext ( self, context : dict ) -> None :
    if not self.__context :
      self.__context.update ( context )


  def getAppLogger ( self ) -> SuccessLogger | None :
    apps = self.getCurrentAppName ()
    if apps in self.__context [ "success" ] [ "apps" ] :
      return self.__context [ "success" ] [ "apps" ] [ apps.lower () ] [ "logger" ]


  def setAppLogger ( self, logger : SuccessLogger ) -> None :
    apps = self.getCurrentAppName ()
    if apps in self.__context [ "success" ] [ "apps" ] :
      self.__context [ "success" ] [ "apps" ] [ apps.lower () ] [ "logger" ] = logger


  def setExtension ( self, extensionName : str, extensionInstance : SuccessExtension ) :
    apps = self.getCurrentAppName ()
    if apps in self.__context [ "success" ] [ "apps" ] :
      self.__context [ "success" ] [ "apps" ] [ apps.lower () ] [ "extensions" ] [ extensionName.lower () ] = extensionInstance

    # else :
    #   self.__logger.log (
    #     f"No existe la apps '{apps}' en contexto. No se pudo registrar extensión '{extensionName}'.",
    #     "WARNING"
    #   )
    # Si no, que hacer?


  def getExtension ( self, extensionName : str ) -> SuccessExtension :
    apps = self.getCurrentAppName ()
    if not apps:
      raise RuntimeError (
        "No se pudo determinar la aplicación actual. "
        "Verifica que se esté ejecutando dentro de una petición o durante bootstrap."
      )
    return self.__context [ "success" ] [ "apps" ] [ apps.lower () ] [ "extensions" ].get ( extensionName.lower () )


  def setState ( self, name : str, state ) :
    self.__states [ name.lower () ] = state


  def getState ( self, name : str ) :
    return self.__states.get ( name.lower () )


  def _ensure_scope ( scope ) :
    if not hasattr ( g, '_success_context' ) :
      g._success_context = {}

    if scope not in g._success_context :
        g._success_context [ scope ] = {}

    return g._success_context [ scope ]


  def set ( scope, key, value, persist = False ) :
    if persist :
      SuccessSessionExtension.set ( f"{scope}:{key}", value )

    else :
      scope_data = SuccessContext ()._ensure_scope ( scope )
      scope_data [ key ] = value


  def get ( scope, key, default = None, persist = False ) :
    if persist :
      return SuccessSessionExtension.get ( f"{scope}:{key}", default )

    else :
      scope_data = SuccessContext ()._ensure_scope ( scope )
      return scope_data.get ( key, default )


  def clear ( scope = None, persist = False ) :
    if persist :
      SuccessSessionExtension.clear ( scope )  # define en SuccessSessionExtension cómo limpiar por prefijo

    else :
      if hasattr ( g, '_success_context' ) :
        if scope :
          g._success_context.pop ( scope, None )

        else :
          g._success_context = {}


  def getCurrentAppName ( self ) :
    return (
      CURRENT_APP.get ( None )
      or self.__context [ "success" ].get ( "current_app_bootstrapping" )
    )


  def setSuccessValue ( self, key : str, value ) -> None :
    self.__context [ "success" ] [ key ] = value


  def getSuccessValue ( self, key : str ) :
    return self.__context [ "success" ].get ( key )
