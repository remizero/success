# Python Libraries / Librerías Python
from flask  import Flask
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type


# Success Libraries / Librerías Success
from success.common.base.SuccessClass                      import SuccessClass
from success.common.infra.config.SuccessConfig             import SuccessConfig
from success.core.SuccessContext                           import SuccessContext
from success.core.extension.SuccessExtensionBuilder        import SuccessExtensionBuilder
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
from success.core.SuccessBuildContext                      import SuccessBuildContext

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessExtensionsLoader ( SuccessClass ) :
  """
  Standard extension loader for the Success framework.

  Loads and registers built-in framework extensions (Admin, CORS,
  Database, JWT, etc.) based on environment configuration.

  Purpose:
  ----------
  SuccessExtensionsLoader is responsible for:
  - Maintaining registry of available standard extensions
  - Iterating over extensions and loading enabled ones
  - Registering each extension in SuccessContext
  - Executing hooks during registration

  Supported extensions:
  -----------------------
  - SUCCESS_EXTENSION_ADMIN: Administration
  - SUCCESS_EXTENSION_APSCHEDULER: Scheduled tasks
  - SUCCESS_EXTENSION_BABEL: Internationalization
  - SUCCESS_EXTENSION_CACHE: Caching
  - SUCCESS_EXTENSION_CORS: Cross-Origin Resource Sharing
  - SUCCESS_EXTENSION_SQLALCHEMY: Database
  - SUCCESS_EXTENSION_EMAIL: Email sending
  - SUCCESS_EXTENSION_JWT: JWT authentication
  - SUCCESS_EXTENSION_LIMITER: Rate limiting
  - SUCCESS_EXTENSION_LOGGIN: Login/authentication
  - SUCCESS_EXTENSION_MARSHMALLOW: Serialization
  - SUCCESS_EXTENSION_MIGRATE: DB migrations
  - SUCCESS_EXTENSION_REDIS: Redis caching
  - SUCCESS_EXTENSION_SECURITY: Security
  - SUCCESS_EXTENSION_SESSION: Session management

  Usage:
  ------
  ctx = SuccessBuildContext.from_app('myapp', '/apps/myapp')
  loader = SuccessExtensionsLoader(ctx)
  extensions = loader.load()  # Load enabled extensions

  Attributes:
      __extensions (list): List of tuples (env_var, extension_class).
      __instances (dict): Dictionary of created instances.
      __context (SuccessContext): Application context.
      __builder (SuccessExtensionBuilder): Extension builder.
      __buildContext (SuccessBuildContext): Build context.

  Note:
    - Each extension loads only if its env variable is 'true'
    - Extensions registered with multiple aliases in context
  """

  # __app        : Flask              = None
  # __config     : SuccessConfig      = None
  # __hooks      : SuccessHookManager = None
  __extensions   : list                    = []
  __instances    : dict                    = {}
  __context      : SuccessContext          = None
  __builder      : SuccessExtensionBuilder = None
  __buildContext : SuccessBuildContext     = None


  def __init__ ( self, buildContext : SuccessBuildContext ) -> None :
    """
    Initialize the extension loader.

    Args:
        buildContext: Build context with application configuration.

    Note:
        The list of standard extensions is defined internally.
    """
    super ().__init__ ()
    self.__buildContext = buildContext
    self.__builder      = SuccessExtensionBuilder ( self.__buildContext )
    self.__extensions   = [
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


  def getExtension ( self, name : str ) -> Optional [ Type ] :
    """
    Get extension class by name or environment variable.

    Args:
        name: Extension name or environment variable
             (e.g., 'SUCCESS_EXTENSION_CORS' or 'SuccessCorsExtension').

    Returns:
        Optional[Type]: Extension class if exists, None otherwise.

    Example:
        loader.getExtension('SUCCESS_EXTENSION_CORS')  # → SuccessCorsExtension
        loader.getExtension('SuccessCorsExtension')    # → SuccessCorsExtension
    """
    for envVar, extensionClass in self.__extensions :
      if envVar == name or extensionClass.__name__ == name :
        return extensionClass

    return None


  def load ( self ) -> List [ Tuple [ str, Type ] ] :
    """
    Load and register all enabled extensions.

    Iterates over the list of standard extensions, checks if they are
    enabled via SuccessExtensionBuilder, and registers them in
    SuccessContext.

    Returns:
        List[Tuple[str, Type]]: List of tuples (env_var, extension_class)
            of all standard extensions (enabled or not).

    Note:
        - Only enabled extensions are instantiated and registered
        - 'before/after extension_register' hooks are executed
        - Each extension is registered with two aliases in the context
    """
    self._logger.log ( f"Iniciando carga de extensiones básicas de la aplicación {self.__buildContext._appName}.", "INFO" )

    for env_var, ExtensionClass in self.__extensions :
      instance = self.__builder.build ( env_var, ExtensionClass )
      if not instance :
        continue

      self.__buildContext.setExtension ( ExtensionClass.__name__, instance )
      self.__instances [ env_var ] = instance

      self._logger.log ( f"Extensión [{ExtensionClass.__name__}] registrada.", "INFO" )

    self._logger.log ( f"Finalizando la carga de extensiones básicas de la aplicación {self.__buildContext._appName}.", "INFO" )

    return self.__extensions
