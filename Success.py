# Python Libraries / Librerías Python
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import uuid

# Success Libraries / Librerías Success
from success.common.base.SuccessClass             import SuccessClass
from success.core.SuccessAppScan                  import SuccessAppScan
from success.common.tools.SuccessEnv              import SuccessEnv
from success.common.infra.config.SuccessSystemEnv import SuccessSystemEnv
from success.core.SuccessSystemState              import SuccessSystemState
from success.common.tools.SuccessStructs          import SuccessStructs
from success.core.SuccessContext                  import SuccessContext
from success.core.SuccessDispatcherFactory        import SuccessDispatcherFactory

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones
session_id = str ( uuid.uuid4 () )


class Success ( SuccessClass ) :

  __success : DispatcherMiddleware = None


  def __init__ ( self ) :
    # SuccessEnv.loadEnv ( __file__, False )
    SuccessSystemEnv ( __file__ )
    super ().__init__ ()
    SuccessContext ().setContext ( SuccessStructs.successContextFramework () )
    SuccessContext ().setSuccessValue ( "SESSION_ID", session_id )
    SuccessContext ().setSuccessValue ( "LOGGER", self._logger )


  def create ( self ) -> None :
    try :
      SuccessSystemState.startTimer ()
      # SuccessSystemState.setEnv ( SuccessEnv.get ( "FLASK_ENV", "development" ) )
      SuccessSystemState.setEnv ( SuccessSystemEnv.get ( "FLASK_ENV", "development" ) )
      # SuccessSystemState.setLoggerFile ( SuccessEnv.isTrue ( "LOGGER_FILE" ) )
      SuccessSystemState.setLoggerFile ( SuccessSystemEnv.isTrue ( "LOGGER_FILE" ) )

      self._logger.log ( "Iniciando la carga del sistema Success.", "INFO" )

      factory = SuccessDispatcherFactory ()
      self.__success = factory.build ()

      self._logger.log ( "Carga exitosa del sistema Success.", "INFO" )
      SuccessSystemState.report ( self._logger )
      # if SuccessEnv.isTrue ( "SUCCESS_SHOW_SUMMARY" ) and not isTestingEnv () :
      #   level = SuccessEnv.get ( "SUCCESS_SUMMARY_LEVEL", "FULL" ).upper ()
      # SuccessSummary ().show ( level = level )

      # if ( SuccessEnv.isTrue ( "SUCCESS_HUMOR_ENABLED" ) ) :
      #   BootCommentator.show ( apps )

    except :
      self._logger.uncatchErrorException ()


  def getApp ( self ) -> DispatcherMiddleware :

    return self.__success
