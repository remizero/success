# Python Libraries / Librerías Python
from flask import Flask
from logging import (
  currentframe,
  CRITICAL,
  DEBUG,
  ERROR,
  FATAL,
  Formatter,
  getLogger,
  INFO,
  raiseExceptions,
  StreamHandler,
  WARNING
)
from logging.handlers import RotatingFileHandler
from pythonjsonlogger import jsonlogger
import os
import sys
import traceback


# Application Libraries / Librerías de la Aplicación
from extensions import Email
from kernel import (
  Debug,
  Exception,
  Extension
)


# Preconditions / Precondiciones
if hasattr ( sys, 'frozen' ) : #support for py2exe

  _srcfile = "logging%s__init__%s" % ( os.sep, __file__ [ -4 : ] )

elif __file__ [ -4 : ].lower () in [ '.pyc', '.pyo' ] :

  _srcfile = __file__ [ : -4 ] + '.py'

else :

  _srcfile = __file__
_srcfile = os.path.normcase ( _srcfile )


class Logger ( Extension ) :

  # Cantidad de archivos log de errores a mantener
  __backupCount = 5
  # Nombre del archivo log de errores
  __fileName = os.environ.get ( 'LOGGER_DIR' )
  # Formato del mensaje que se guardara en el archivo log
  __format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s - %(threadName)s"
  # Instancia del logger
  __logger = None
  # Tamaño maximo del archivo log de errores
  __maxBytes = 500000

  def __init__ ( self ) -> None :
    super ().__init__ ()

  def __consoleHandled ( self ) -> StreamHandler :
    console_handler = StreamHandler ()
    console_handler.setFormatter ( Formatter ( self.__format ) )
    return console_handler

  def __emailHandled ( self, errorMessage ) -> None :
    Debug.log ( errorMessage )
    email.message ( _subject = 'Alerta critica en el sistema', _template = 'SuccessExceptionAlert.html' )
    email.send ( os.environ.get ( 'MAIL_DEFAULT_SENDER' ) )

  def __fileHandled ( self ) -> RotatingFileHandler :
    rotatingFileHandler = RotatingFileHandler ( self.__fileName, maxBytes = self.__maxBytes, backupCount = self.__backupCount, encoding = "utf-8" )
    rotatingFileHandler.setFormatter ( Formatter ( self.__format ) )
    # El registro log es almacenado en formato json
    # rotatingFileHandler.setFormatter ( jsonlogger.JsonFormatter ( self.__format ) )
    return rotatingFileHandler

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

  def config ( self ) -> None :
    pass

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

    if isinstance ( errorMessage, BaseException ) :

      if hasattr ( errorMessage, 'getMessage' ) :

        self.__logger.exception ( errorMessage.getMessage () )

      else :

        self.__logger.error ( errorMessage, exc_info = True )

    elif isinstance ( errorMessage, Exception ) :

      if hasattr ( errorMessage, 'getMessage' ) :

        self.__logger.exception ( errorMessage.getMessage () )

      else :

        self.__logger.error ( errorMessage, exc_info = True )

    elif self.__logger.isEnabledFor ( DEBUG ) :

      self.__logger.debug ( errorMessage, exc_info = True )

    elif self.__logger.isEnabledFor ( INFO ) :

      self.__logger.info ( errorMessage, exc_info = True )

    elif self.__logger.isEnabledFor ( WARNING ) :

      self.__logger.warning ( errorMessage, exc_info = True )

    elif self.__logger.isEnabledFor ( ERROR ) :

      self.__logger.error ( errorMessage, exc_info = True )

    elif self.__logger.isEnabledFor ( CRITICAL ) :

      self.__emailHandled ( errorMessage )
      self.__logger.critical ( errorMessage, exc_info = True )

    elif self.__logger.isEnabledFor ( FATAL ) :

      self.__emailHandled ( errorMessage )
      self.__logger.fatal ( errorMessage, exc_info = True )

  def register ( self, _app : Flask, module : str, level : int = DEBUG ) -> None :
    super ().register ( _app )
    del _app.logger.handlers [ : ]
    self.__logger = getLogger ( module )
    self.__logger.setLevel ( level )
    self.__logger.addHandler ( self.__fileHandled () )
    self.__logger.addHandler ( self.__consoleHandled () )
    if ( bool ( os.environ.get ( 'STAGING' ) ) or ( os.environ.get ( 'APP_ENV' ) == 'production' ) ) :
      raiseExceptions = False
    # TODO Entender el rollo de root y la jerarquia de loggers.
    #self.extension = SuccessLogger ()

  def uncatchErrorException ( self ) -> None :
    self.__emailHandled ( traceback.format_exc () )
    self.__logger.error ( "uncaught exception: %s", traceback.format_exc () )

  def userConfig ( self, **kwargs ) -> None :
    pass
