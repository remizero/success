# Python Libraries / Librerías Python
from logging import (
  CRITICAL,
  currentframe,
  DEBUG,
  ERROR,
  FATAL,
  Formatter,
  getLogger,
  INFO,
  Logger as LoggerPython,
  raiseExceptions,
  StreamHandler,
  WARNING,
  LogRecord
)
from logging.handlers import (
  RotatingFileHandler,
  SMTPHandler
)
from pythonjsonlogger.jsonlogger import JsonFormatter
from types import TracebackType
import os
import sys
import traceback


# Application Libraries / Librerías de la Aplicación
from kernel import (
  Debug,
  Exception,
  LoggerMailer
)
from utils import (
  Application,
  EnvVar
)


# Preconditions / Precondiciones
# https://docs.python.org/es/3/howto/logging-cookbook.html
# https://docs.python.org/es/3/howto/logging.html
# https://docs.python.org/es/3.9/library/logging.handlers.html
# https://docs.python.org/es/3/library/logging.config.html
# https://stackify.dev/231524-custom-logger-class-and-correct-line-number-function-name-in-log
# https://www.machinelearningplus.com/python/python-logging-guide/
# https://dock2learn.com/tech/create-a-reusable-logger-factory-for-python-projects/
# https://www.peterspython.com/es/blog/cree-sus-propias-clases-de-excepcion-python-personalizadas-y-adaptadas-a-su-aplicacion
# https://desktop.arcgis.com/es/arcmap/10.3/analyze/python/error-handling-with-python.htm
# https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/logging-de-python/
# https://docs.python.org/3/library/logging.html

# TODO PARA EL MANEJO DEL TAMANO DEL ARCHIVO
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling

# TODO PARA UTILIZAR DOCKER EN EL MANEJO DE ARCHIVOS LOG CENTRALIZADOS
# https://www.loggly.com/ultimate-guide/centralizing-python-logs/

# TODO PARA FORMATEAR EL ARCHIVO LOG EN FORMATO JSON
# https://everythingtech.dev/2021/03/python-logging-with-json-formatter/
# https://www.datadoghq.com/blog/python-logging-best-practices/
# https://docs.python.org/3/howto/logging-cookbook.html#a-qt-gui-for-logging
if hasattr ( sys, 'frozen' ) : #support for py2exe

  _srcfile = "logging%s__init__%s" % ( os.sep, __file__ [ -4 : ] )

elif __file__ [ -4 : ].lower () in [ '.pyc', '.pyo' ] :

  _srcfile = __file__ [ : -4 ] + '.py'

else :

  _srcfile = __file__
_srcfile = os.path.normcase ( _srcfile )


class Logger () :

  # Number of error log files to keep. / Cantidad de archivos log de errores a mantener.
  __backupCount = 5
  # Error log file name and path. / Nombre y ruta del archivo log de errores.
  __fileName = EnvVar.get ( 'LOGGER_DIR' )
  # Format of the message to save in the log file. / Formato del mensaje a guardar en el archivo log.
  __format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s - %(threadName)s"
  # Logger object instance. / Instancia del objeto logger.
  __logger : LoggerPython = None
  # LoggerMailer instance for sending critical and fatal mail. / Instancia del LoggerMailer para envío de correo crítico y fatal.
  __loggerMailer : LoggerMailer = None
  # Maximum size of the error log file. / Tamaño máximo del archivo log de errores.
  __maxBytes = 500000
  # Error to display to the user at the frontend level. / Error a mostrar al usuario a nivel de frontend.
  __toShow = ''

  def __init__ ( self, module : str, level : int = DEBUG ) -> None :
    self.__logger = getLogger ( module )
    self.__logger.setLevel ( level )
    self.__logger.addHandler ( self.__fileHandled () )
    self.__logger.addHandler ( self.__consoleHandled () )
    self.__logger.addHandler ( self.__emailHandled () )
    if ( Application.isStagingMode () or Application.isProductionMode () ) :
      raiseExceptions = False

  def __consoleHandled ( self ) -> StreamHandler :
    consoleHandler = StreamHandler ()
    consoleHandler.setFormatter ( Formatter ( self.__format ) )
    return consoleHandler

  def __emailHandled ( self ) -> SMTPHandler :
    self.__loggerMailer = LoggerMailer ()
    self.__loggerMailer.setFormatter ( Formatter ( self.__format ) )
    return self.__loggerMailer

  def __fileHandled ( self ) -> RotatingFileHandler :
    fileHandler = RotatingFileHandler ( self.__fileName, maxBytes = self.__maxBytes, backupCount = self.__backupCount, encoding = "utf-8" )
    formater = None
    if ( EnvVar.get ( 'LOGGER_FORMATER' ) == 'json' ) :

      formater = JsonFormatter ()

    else :

      formater = Formatter ( self.__format )
    fileHandler.setFormatter ( formater )
    return fileHandler

  def _log ( self, level, msg, args, exc_info = None, extra = None ) -> None :
    """
      Low-level logging routine which creates a LogRecord and then calls
      all the handlers of this logger to handle the record.
    """
    # Add wrapping functionality here.
    if _srcfile :
      #IronPython doesn't track Python frames, so findCaller throws an
      #exception on some versions of IronPython. We trap it here so that
      #IronPython can use logging.
      try:
        fn, lno, func = self.findCaller ()
      except ValueError:
        fn, lno, func = "(unknown file)", 0, "(unknown function)"
    else:
      fn, lno, func = "(unknown file)", 0, "(unknown function)"
    if exc_info:
      if not isinstance ( exc_info, tuple ) :
        exc_info = sys.exc_info ()
    record = self.__logger.makeRecord ( self.__logger.name, level, fn, lno, msg, args, exc_info, func, extra )
    self.__logger.handle ( record )

  def findCaller ( self ) :
    """
      Find the stack frame of the caller so that we can note the source
      file name, line number and function name.
    """
    f = currentframe ()
    #On some versions of IronPython, currentframe() returns None if
    #IronPython isn't run with -X:Frames.
    if f is not None :
      f = f.f_back
    rv = "(unknown file)", 0, "(unknown function)"
    while hasattr ( f, "f_code" ) :
      co = f.f_code
      filename = os.path.normcase ( co.co_filename )
      if filename == _srcfile :
        f = f.f_back
        continue
      rv = ( co.co_filename, f.f_lineno, co.co_name )
      break
    return rv

  def log ( self, errorMessage ) -> None :
    try :

      getattr ( errorMessage, 'getMessage' )
      self.__toShow = str ( errorMessage.getMessage () )
      self.__logger.exception ( errorMessage.getMessage () )

    except :

      try :

        getattr ( errorMessage, 'orig' )
        self.__toShow = str ( errorMessage.orig )
        self.__logger.error ( errorMessage, exc_info = True )

      except :

        try :

          getattr ( errorMessage, 'message' )
          self.__toShow = str ( errorMessage.message )
          self.__logger.error ( errorMessage, exc_info = True )

        except :

          self.__toShow = str ( errorMessage.getMessage () )
          if self.__logger.isEnabledFor ( DEBUG ) :

            self.__logger.debug ( errorMessage, exc_info = True )

          elif self.__logger.isEnabledFor ( INFO ) :

            self.__logger.info ( errorMessage, exc_info = True )

          elif self.__logger.isEnabledFor ( WARNING ) :

            self.__logger.warning ( errorMessage, exc_info = True )

          elif self.__logger.isEnabledFor ( ERROR ) :

            self.__logger.error ( errorMessage, exc_info = True )

          elif self.__logger.isEnabledFor ( CRITICAL ) :

            self.sendException ( 'Critical exception', CRITICAL, errorMessage )
            self.__logger.critical ( errorMessage, exc_info = True )

          elif self.__logger.isEnabledFor ( FATAL ) :

            self.sendException ( 'Fatal exception', FATAL, errorMessage )
            self.__logger.fatal ( errorMessage, exc_info = True )

          else :

            self.sendException ( 'Critical exception', CRITICAL, errorMessage )
            self.__logger.error ( errorMessage, exc_info = True )

  def sendException ( self, _name : str, _level : int, _exc_info : BaseException or TracebackType ) :
    messageRecord = LogRecord ( name = _name, level = _level, exc_info = _exc_info )
    self.__loggerMailer.emit ( messageRecord )

  def toShow ( self ) -> str :
    return self.__toShow

  def uncatchErrorException ( self ) -> None :
    self.__toShow = 'Error no identificado, comunicarse inmediatamente con el administrador del sistema.'
    #self.sendException ( 'uncaught exception', CRITICAL, sys.exc_info () )
    self.__logger.error ( 'uncaught exception: %s', traceback.format_exc () )
