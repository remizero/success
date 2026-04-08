# Python Libraries / Librerías Python
from logging.handlers            import RotatingFileHandler
from logging.handlers            import TimedRotatingFileHandler
from pythonjsonlogger.jsonlogger import JsonFormatter

# Success Libraries / Librerías Success
# from success.common.tools.SuccessEnv          import SuccessEnv
from success.common.base.SuccessLoggerHandler import Formatter
from success.common.base.SuccessLoggerHandler import SuccessLoggerHandler
from success.common.infra.config.SuccessSystemEnv import SuccessSystemEnv

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessFileHandler ( SuccessLoggerHandler ) :

  # Number of error log files to keep. / Cantidad de archivos log de errores a mantener.
  __backupCount : int = 7
  # Error log file name and path. / Nombre y ruta del archivo log de errores.
  __fileName    : str = "./log"
  # Maximum size of the error log file. / Tamaño máximo del archivo log de errores.
  __maxBytes    : int = 500000
  # Time when the error log file rotation should be performed. / Momento cuando debe realizarse la rotación del archivo log de errores.
  __when        : str = None
  # Number of times to rotate the error log file. / Cantidad de veces que debe realizarse la rotación del archivo log de errores.
  __interval    : int = 1


  def __init__ ( self ) :
    super ().__init__ ()
    self.__backupCount = SuccessSystemEnv.toInt ( 'LOGGER_BACKUP_COUNT' )
    self.__fileName    = SuccessSystemEnv.get   ( 'LOGGER_DIR' )
    self.__maxBytes    = SuccessSystemEnv.toInt ( 'LOGGER_MAX_BYTES' )
    self.__when        = SuccessSystemEnv.get   ( 'LOGGER_ROTATE_WHEN', 'midnight' )
    self.__interval    = SuccessSystemEnv.toInt ( 'LOGGER_ROTATE_INTERVAL' )

    try :
      self._handler = TimedRotatingFileHandler (
        self.__fileName,
        when = self.__when,
        interval = self.__interval,
        backupCount = self.__backupCount,
        encoding = SuccessSystemEnv.get ( 'LOGGER_ENCODING', 'utf-8' )
      )

    except Exception as e :
      self._handler = RotatingFileHandler(
        self.__fileName,
        maxBytes = self.__maxBytes,
        backupCount = self.__backupCount,
        encoding = SuccessSystemEnv.get ( 'LOGGER_ENCODING', 'utf-8' )
      )

    self._getFormatter ()


  def _getFormatter ( self ) :
    formater = None
    if ( SuccessSystemEnv.get ( 'LOGGER_FORMATER' ) == 'json' ) :
      formater = JsonFormatter ( self._format )

    else :
      formater = Formatter ( self._format )

    self._handler.setFormatter ( formater )
