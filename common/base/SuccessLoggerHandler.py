# Python Libraries / Librerías Python
from logging import Handler

# Success Libraries / Librerías Success
from success.common.infra.config.SuccessSystemEnv import SuccessSystemEnv

# Preconditions / Precondiciones


class SuccessLoggerHandler () :
  """
  Base class for logging handlers in the Success framework.

  Provides a common structure for creating custom logging handlers
  with configurable formatting.

  Attributes:
    _format (str): The log message format.
    _handler (Handler): The logging handler instance.
  """

  _format  : str     = None
  _handler : Handler = None


  def __init__ ( self ) -> None :
    """
    Initialize the logging handler with the system format.

    Obtains the logging format from the system configuration
    or uses a default format.
    """
    self._format = SuccessSystemEnv.get ( "LOGGER_FORMAT", f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s - %(threadName)s" )


  def _getFormatter ( self ) -> str :
    """
    Get the configured logging format.

    Returns:
      str: The logging format string to use.
    """
    return SuccessSystemEnv.get ( "LOGGER_FORMAT", f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s - %(threadName)s" )


  def getDescriptor ( self ) -> Handler :
    """
    Get the logging handler.

    Returns:
      Handler: The logging handler instance.
    """
    return self._handler
