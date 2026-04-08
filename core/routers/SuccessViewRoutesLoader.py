# Python Libraries / Librerías Python
from flask import Flask

# Success Libraries / Librerías Success
from success.common.base.SuccessRoutesLoader          import SuccessRoutesLoader
from success.common.tools.SuccessEnv                  import SuccessEnv
from success.common.infra.logger.SuccessLogger        import SuccessLogger
from success.common.infra.config.SuccessConfig        import SuccessConfig
from success.engine.infrastructure.SuccessHookManager import SuccessHookManager
from success.common.tools.SuccessClasses              import SuccessClasses

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessViewRoutesLoader ( SuccessRoutesLoader ) :


  def __init__ ( self, apps : Flask, config : SuccessConfig = None, hooks : SuccessHookManager = None ) -> None :
    super ().__init__ ( apps, config, hooks )


  def getSubpackage ( self ) -> str :
    return "view"
