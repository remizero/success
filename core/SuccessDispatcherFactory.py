# Python Libraries / Librerías Python
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# Success Libraries / Librerías Success
from success.common.base.SuccessClass             import SuccessClass
# from success.common.tools.SuccessEnv              import SuccessEnv
from success.common.infra.config.SuccessSystemEnv import SuccessSystemEnv
from success.core.SuccessAppScan                  import SuccessAppScan
from success.core.SuccessPathDispatcher           import SuccessPathDispatcher
from success.core.SuccessSubdomainDispatcher      import SuccessSubdomainDispatcher

# Application Libraries / Librerías de la Aplicación
from success.debug.WSGIFullTrace            import WSGIFullTrace
from success.debug.DebugSubdomainDispatcher import DebugSubdomainDispatcher

# Preconditions / Precondiciones


class SuccessDispatcherFactory ( SuccessClass ) :

  _domainMode : str            = None
  _appScan    : SuccessAppScan = None


  def __init__ ( self ) -> None :
    super ().__init__ ()
    self._appScan    = SuccessAppScan ()
    self._domainMode = SuccessSystemEnv.get ( "SUCCESS_APP_DOMAIN", "standard" ).strip ().lower ()
    self._logger.log ( "Cargando sistema de dominio de Success, SUCCESS_APP_DOMAIN.", "INFO" )


  # def build(self):

  #   if self._domainMode == "path":
  #       self._logger.log("Cargando Success en mode=path.", "INFO")
  #       disp = SuccessPathDispatcher(
  #           self._appScan.getRootApp(),
  #           self._appScan.getSecondaryApps()
  #       )
  #       return WSGIFullTrace(disp, "BeforeFlask")

  #   if self._domainMode == "subdomain":
  #       self._logger.log("Cargando Success en mode=subdomain.", "INFO")

  #       raw = SuccessSubdomainDispatcher(
  #           SuccessSystemEnv.get("SUCCESS_DOMAIN", "success.local").strip().lower(),
  #           self._appScan.getSecondaryApps()
  #       )

  #       disp = DebugSubdomainDispatcher(raw)
  #       return WSGIFullTrace(disp, "BeforeFlask", deep=True)

  #   self._logger.log("Cargando Success en mode=standard.", "INFO")

  #   raw = DispatcherMiddleware(
  #       self._appScan.getRootApp(),
  #       self._appScan.getSecondaryApps()
  #   )
  #   return WSGIFullTrace(raw, "BeforeFlask")



  def build ( self ) :

    if self._domainMode == "path" :
      self._logger.log ( "Cargando sistema Success en mode=path.", "INFO" )
      return SuccessPathDispatcher ( self._appScan.getRootApp (), self._appScan.getSecondaryApps () )

    if self._domainMode == "subdomain" :
      self._logger.log ( "Cargando sistema Success en mode=subdomain.", "INFO" )
      self._logger.log ( f"SuccessSystemEnv.get ( SUCCESS_DOMAIN, success.local ).strip ().lower () {SuccessSystemEnv.get ( 'SUCCESS_DOMAIN', 'success.local' ).strip ().lower ()}.", "INFO" )
      return SuccessSubdomainDispatcher ( SuccessSystemEnv.get ( "SUCCESS_DOMAIN", "success.local" ).strip ().lower (), self._appScan.getSecondaryApps () )
      # return SuccessSubdomainDispatcher ( mainApp = self._appScan.getRootApp (), mounts = self._appScan.getSecondaryApps (), domain = "localhost" )

    self._logger.log ( "Cargando sistema Success en mode=standard.", "INFO" )
    return DispatcherMiddleware ( self._appScan.getRootApp (), self._appScan.getSecondaryApps () )
