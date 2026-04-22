# Python Libraries / Librerías Python
from abc import ABC
from abc import abstractmethod

# Success Libraries / Librerías Success
from success.common.infra.logger.SuccessLogger       import SuccessLogger
from success.common.reflection.SuccessModuleMetadata import SuccessModuleMetadata
from success.core.SuccessContext                     import SuccessContext

# Preconditions / Precondiciones


class SuccessClass ( ABC ) :
  """
  Abstract base class for all classes in the Success framework.

  Provides common functionality such as logging and reflection to identify
  the module and scope of each derived class.

  Attributes:
    _logger (SuccessLogger): Instance of SuccessLogger for event logging.
    _module (str): Name of the module where the class is defined.
    _scope (str): Application scope of the class.
  """

  _logger : SuccessLogger = None
  _module : str           = None
  _scope  : str           = None


  def __init__ ( self ) -> None :
    """
    Initialize the SuccessClass configuring logger and reflection.

    Obtains the application name and scope from the module where the class
    is defined, and initializes the corresponding logger.

    Note:
      Logs an informational message about the class initialization.
    """
    module  = SuccessModuleMetadata.getAppName ( self.__class__.__module__ )
    scope   = SuccessModuleMetadata.getScope ( self.__class__.__module__ )
    ctx_app = SuccessContext ().getCurrentAppName ()
    if ctx_app:
      module = ctx_app

    self._module = module
    self._scope  = scope
    self._logger = SuccessLogger ( module = self._module, scope = self._scope )
    self._logger.log ( f"Inicializando clase {self.__class__.__name__}...", "INFO" )
