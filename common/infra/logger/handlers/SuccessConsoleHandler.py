# Python Libraries / Librerías Python
from logging import StreamHandler

# Success Libraries / Librerías Success
from success.common.base.SuccessLoggerHandler import Formatter
from success.common.base.SuccessLoggerHandler import SuccessLoggerHandler

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessConsoleHandler ( SuccessLoggerHandler ) :


  def __init__ ( self ) :
    super ().__init__ ()
    self._handler = StreamHandler ()
    self._getFormatter ()


  def _getFormatter ( self ) :
    self._format = super ()._getFormatter ()
    self._handler.setFormatter ( Formatter ( self._format ) )
