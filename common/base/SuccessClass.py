# Python Libraries / Librerías Python
from abc    import ABC
from abc    import abstractmethod
from flask  import request
from flask  import session
from typing import Any

# Success Libraries / Librerías Success
from success.common.SuccessDebug               import SuccessDebug
from success.common.infra.logger.SuccessLogger import SuccessLogger
from success.common.tools.SuccessReflection    import SuccessReflection

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessClass ( ABC ) :

  _logger : SuccessLogger = None
  _module : str           = None
  _scope  : str           = None


  def __init__ ( self ) -> None :
    self._module = SuccessReflection.getAppNameFromModule ( self.__class__.__module__ )
    self._scope = SuccessReflection.getScopeFromModule ( self.__class__.__module__ )
    self._logger = SuccessLogger ( module = self._module, scope = self._scope )
    self._logger.log ( f"Inicializando clase {self.__class__.__name__}...", "INFO" )
