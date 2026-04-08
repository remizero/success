# Python Libraries / Librerías Python
from flask import Flask

# Success Libraries / Librerías Success
from success.common.base.SuccessClass                 import SuccessClass
from success.core.SuccessContext                      import SuccessContext
from success.common.tools.SuccessEnv                  import SuccessEnv
from success.common.infra.config.SuccessConfig        import SuccessConfig
from success.engine.infrastructure.SuccessHookManager import SuccessHookManager
from success.core.routers.SuccessCLIRoutesLoader      import SuccessCLIRoutesLoader
from success.core.routers.SuccessGQRoutesLoader       import SuccessGQRoutesLoader
from success.core.routers.SuccessRestfulRoutesLoader  import SuccessRestfulRoutesLoader
from success.core.routers.SuccessRPCRoutesLoader      import SuccessRPCRoutesLoader
from success.core.routers.SuccessSSERoutesLoader      import SuccessSSERoutesLoader
from success.core.routers.SuccessViewRoutesLoader     import SuccessViewRoutesLoader
from success.core.routers.SuccessWSRoutesLoader       import SuccessWSRoutesLoader

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessBlueprintsLoader ( SuccessClass ) :

  __cliLoader  : SuccessCLIRoutesLoader     = None
  __gqLoader   : SuccessGQRoutesLoader      = None
  __restLoader : SuccessRestfulRoutesLoader = None
  __rpcLoader  : SuccessRPCRoutesLoader     = None
  __sseLoader  : SuccessSSERoutesLoader     = None
  __viewLoader : SuccessViewRoutesLoader    = None
  __wsLoader   : SuccessWSRoutesLoader      = None


  def __init__ ( self, apps : Flask, config : SuccessConfig = None, hooks : SuccessHookManager = None ) -> None :
    super ().__init__ ()
    if ( SuccessEnv.isTrue ( config.get ( "SUCCESS_ENABLE_CLI" ) ) ) :
      self.__cliLoader = SuccessCLIRoutesLoader ( apps, config, hooks )
    
    if ( SuccessEnv.isTrue ( config.get ( "SUCCESS_ENABLE_GRAPHQL" ) ) ) :
      self.__gqLoader = SuccessGQRoutesLoader ( apps, config, hooks )
    
    if ( SuccessEnv.isTrue ( config.get ( "SUCCESS_ENABLE_REST" ) ) ) :
      self.__restLoader = SuccessRestfulRoutesLoader ( apps, config, hooks )
    
    if ( SuccessEnv.isTrue ( config.get ( "SUCCESS_ENABLE_RPC" ) ) ) :
      self.__rpcLoader = SuccessRPCRoutesLoader ( apps, config, hooks )
    
    if ( SuccessEnv.isTrue ( config.get ( "SUCCESS_ENABLE_SSE" ) ) ) :
      self.__sseLoader = SuccessSSERoutesLoader ( apps, config, hooks )
    
    if ( SuccessEnv.isTrue ( config.get ( "SUCCESS_ENABLE_VIEW" ) ) ) :
      self.__viewLoader = SuccessViewRoutesLoader ( apps, config, hooks )
    
    if ( SuccessEnv.isTrue ( config.get ( "SUCCESS_ENABLE_WEB_SOCKET" ) ) ) :
      self.__wsLoader = SuccessWSRoutesLoader ( apps, config, hooks )


  def load ( self, package : str, config : SuccessConfig = None ) :
    """
    Orquesta el flujo completo: descubrimiento + registro.
    """
    self._logger.log ( "Iniciando carga de blueprints...", "INFO" )
    self._logger.log ( f"Iniciando carga de blueprints config.get ( SUCCESS_ENABLE_REST )... {config.get ( 'SUCCESS_ENABLE_REST' )}", "INFO" )

    if ( SuccessEnv.isTrue ( config.get ( "SUCCESS_ENABLE_CLI" ) ) ) :
      self.__cliLoader.load ( package )
    
    if ( SuccessEnv.isTrue ( config.get ( "SUCCESS_ENABLE_GRAPHQL" ) ) ) :
      self.__gqLoader.load ( package )
    
    if ( SuccessEnv.isTrue ( config.get ( "SUCCESS_ENABLE_REST" ) ) ) :
      self.__restLoader.load ( package )
    
    if ( SuccessEnv.isTrue ( config.get ( "SUCCESS_ENABLE_RPC" ) ) ) :
      self.__rpcLoader.load ( package )
    
    if ( SuccessEnv.isTrue ( config.get ( "SUCCESS_ENABLE_SSE" ) ) ) :
      self.__sseLoader.load ( package )
    
    if ( SuccessEnv.isTrue ( config.get ( "SUCCESS_ENABLE_VIEW" ) ) ) :
      self.__viewLoader.load ( package )
    
    if ( SuccessEnv.isTrue ( config.get ( "SUCCESS_ENABLE_WEB_SOCKET" ) ) ) :
      self.__wsLoader.load ( package )
      
    self._logger.log ( "Carga de blueprints finalizada.", "INFO" )
