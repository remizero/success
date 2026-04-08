# Python Libraries / Librerías Python
from logging import config
from logging import Formatter
from logging import Handler

# Success Libraries / Librerías Success
# from success.common.tools.SuccessEnv import SuccessEnv
from success.common.infra.config.SuccessSystemEnv import SuccessSystemEnv

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessLoggerHandler () :

  _format  : str = None
  _handler : Handler = None


  def __init__ ( self ) :
    self._format = SuccessSystemEnv.get ( "LOGGER_FORMAT", f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s - %(threadName)s" )


  def _getFormatter ( self ) :
    return SuccessSystemEnv.get ( "LOGGER_FORMAT", f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s - %(threadName)s" )


  def getDescriptor ( self ) -> Handler :
    return self._handler
