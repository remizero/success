# Python Libraries / Librerías Python
from flask import Flask

# Success Libraries / Librerías Success
from success.common.base.SuccessClass                      import SuccessClass
from success.common.infra.logger.SuccessLogger             import SuccessLogger
from success.common.tools.SuccessEnv                       import SuccessEnv
from success.common.infra.config.SuccessConfig             import SuccessConfig
from success.core.SuccessContext                           import SuccessContext
from success.engine.extensions.SuccessAdminExtension       import SuccessAdminExtension
from success.engine.extensions.SuccessAPSchedulerExtension import SuccessAPSchedulerExtension
from success.engine.extensions.SuccessBabelExtension       import SuccessBabelExtension
from success.engine.extensions.SuccessCacheExtension       import SuccessCacheExtension
from success.engine.extensions.SuccessCorsExtension        import SuccessCorsExtension
from success.engine.extensions.SuccessDatabaseExtension    import SuccessDatabaseExtension
from success.engine.extensions.SuccessEmailExtension       import SuccessEmailExtension
from success.engine.extensions.SuccessJwtExtension         import SuccessJwtExtension
from success.engine.extensions.SuccessLimiterExtension     import SuccessLimiterExtension
from success.engine.extensions.SuccessLoginExtension       import SuccessLoginExtension
from success.engine.extensions.SuccessMarshmallowExtension import SuccessMarshmallowExtension
from success.engine.extensions.SuccessMigrateExtension     import SuccessMigrateExtension
from success.engine.extensions.SuccessRedisExtension       import SuccessRedisExtension
from success.engine.extensions.SuccessSecurityExtension    import SuccessSecurityExtension
from success.engine.extensions.SuccessSessionExtension     import SuccessSessionExtension
from success.engine.infrastructure.SuccessHookManager      import SuccessHookManager

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessExtensionsLoader ( SuccessClass ) :

  __app        : Flask              = None
  __config     : SuccessConfig      = None
  __hooks      : SuccessHookManager = None
  __extensions : list               = []
  __instances  : dict               = {}
  __context    : SuccessContext     = None


  def __init__ ( self, apps : Flask, config : SuccessConfig = None, hooks : SuccessHookManager = None ) :
    super ().__init__ ()
    self.__app        = apps
    self.__config     = config
    self.__hooks      = hooks
    self.__context    = SuccessContext ()
    self.__extensions = [
      ( "SUCCESS_EXTENSION_ADMIN",       SuccessAdminExtension ),
      ( "SUCCESS_EXTENSION_APSCHEDULER", SuccessAPSchedulerExtension ),
      ( "SUCCESS_EXTENSION_BABEL",       SuccessBabelExtension ),
      ( "SUCCESS_EXTENSION_CACHE",       SuccessCacheExtension ),
      ( "SUCCESS_EXTENSION_CORS",        SuccessCorsExtension ),
      ( "SUCCESS_EXTENSION_SQLALCHEMY",  SuccessDatabaseExtension ),
      ( "SUCCESS_EXTENSION_EMAIL",       SuccessEmailExtension ),
      ( "SUCCESS_EXTENSION_JWT",         SuccessJwtExtension ),
      ( "SUCCESS_EXTENSION_LIMITER",     SuccessLimiterExtension ),
      ( "SUCCESS_EXTENSION_LOGGIN",      SuccessLoginExtension ),
      ( "SUCCESS_EXTENSION_MARSHMALLOW", SuccessMarshmallowExtension ),
      ( "SUCCESS_EXTENSION_MIGRATE",     SuccessMigrateExtension ),
      ( "SUCCESS_EXTENSION_REDIS",       SuccessRedisExtension ),
      ( "SUCCESS_EXTENSION_SECURITY",    SuccessSecurityExtension ),
      ( "SUCCESS_EXTENSION_SESSION",     SuccessSessionExtension )
    ]


  def getExtension ( self, name : str ) :
    return self.__extensions.get ( name )


  def load ( self ) -> dict :
    if self._logger :
      self._logger.log ( "Iniciando carga de extensiones...", "INFO" )

      for env_var, ExtensionClass in self.__extensions :
        if  SuccessEnv.isTrue ( self.__config.get ( env_var ) ) :
          instance = ExtensionClass ( self.__app )

          if self.__hooks :
            self.__hooks.execute ( when = "before", action = "extension_register", payload = { "extension" : instance } )

          instance.register ()
          SuccessContext ().setExtension ( ExtensionClass.__name__, instance )

          if self.__hooks :
            self.__hooks.execute ( when = "after", action = "extension_register", payload = { "extension" : instance } )

          self.__instances [ env_var ] = instance

          if self._logger :
            self._logger.log ( f"Extensión [{ExtensionClass.__name__}] registrada.", "INFO" )

      if self._logger :
        self._logger.log ( "Carga de extensiones completada con éxito.", "INFO" )

      return self.__extensions
