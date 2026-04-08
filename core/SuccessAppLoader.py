# Python Libraries / Librerías Python
from flask import Flask
import os
import importlib.util

# Success Libraries / Librerías Success
from success.common.infra.logger.SuccessLogger                  import SuccessLogger
from success.core.SuccessAppValidator                           import SuccessAppValidator
from success.common.tools.SuccessClasses                        import SuccessClasses
from success.engine.context.middleware.RequestContextMiddleware import RequestContextMiddleware
from success.common.tools.SuccessJinja                          import SuccessJinja

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessAppLoader () :


  @staticmethod
  def getApp ( path : str, prefix : str = '', validate : bool = True ) -> Flask | None :
    logger = SuccessLogger ( module = "success", scope = "framework" )

    if validate and not SuccessAppValidator.isValidAppDir ( path ) :
      logger.log ( f"[SKIP] Directorio '{path}' no tiene estructura de aplicación válida." )
      return None

    if validate and not SuccessAppValidator.hasFactoryOrInstance ( path ) :
      logger.log ( f"Aplicación en '{path}' no define 'apps' ni 'create_app()'. Se omitirá.", "WARNING" )
      return None

    try :
      pkg          = SuccessClasses.normalizePackage ( path, prefix )
      logical_name = SuccessClasses.normalizeModule ( pkg, "Bootstrap" )
      module       = importlib.import_module ( logical_name )
      # bootstrap    = getattr ( module, "Bootstrap", None )
      # createApp    = getattr ( bootstrap, 'createApp', None )
      # if callable ( createApp ) :
      #   app = createApp ()
      bootstrap_class = getattr ( module, "Bootstrap", None )
      # createApp    = getattr ( bootstrap, 'createApp', None )
      if bootstrap_class :
        bootstrap = bootstrap_class ()
      if hasattr ( bootstrap, 'createApp' ) and callable ( bootstrap.createApp ) :
        app = bootstrap.createApp ()
        RequestContextMiddleware ( app )
        SuccessJinja.registerMethods ( app )

        return app

      else :
        raise AttributeError ( f"El módulo '{logical_name}' no define un método 'createApp()'." )

    except Exception :
      logger.uncatchErrorException ()

    return None
