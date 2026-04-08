# Python Libraries / Librerías Python

# Success Libraries / Librerías Success
from success.common.base.SuccessLoggerHandler        import Formatter
from success.common.base.SuccessLoggerHandler        import SuccessLoggerHandler
from success.common.infra.logger.SuccessLoggerMailer import SuccessLoggerMailer

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessEmailHandler ( SuccessLoggerHandler ) :


  def __init__ ( self ) :
    super ().__init__ ()
    self._handler = SuccessLoggerMailer ()
    self._getFormatter ()


  def _getFormatter ( self ) :
    self._format = super ()._getFormatter ()
    self._handler.setFormatter ( Formatter ( self._format ) )
