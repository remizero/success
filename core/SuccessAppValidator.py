# Python Libraries / Librerías Python
import importlib.util
import os

# Success Libraries / Librerías Success
from success.common.infra.logger.SuccessLogger import SuccessLogger

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessAppValidator () :


  @staticmethod
  def isValidAppDir ( path : str ) -> bool :
    logger = SuccessLogger ( module = "success", scope = "framework" )
    if not os.path.isdir ( path ) :
      logger.log ( f"Directorio de aplicación Success no válido: {path}", "ERROR" )
      return False

    hasEntrypoint = any (
      os.path.exists ( os.path.join ( path, fname ) )
      for fname in [ 'Bootstrap.py', '__init__.py' ]
    )
    logger.log ( f"has_entrypoint: {hasEntrypoint}", "INFO" )
    return hasEntrypoint


  @staticmethod
  def hasFactoryOrInstance ( path : str ) -> bool :
    logger = SuccessLogger ( module = "success", scope = "framework" )
    entryFile = None
    for fname in [ 'Bootstrap.py', '__init__.py' ] :
      if os.path.exists ( os.path.join ( path, fname ) ) :
        entryFile = fname
        break

    if not entryFile :
      logger.log ( f"Directorio de aplicación Success no válido: {path}", "ERROR" )
      return False

    try :
      modulePath = os.path.join ( path, entryFile )
      spec = importlib.util.spec_from_file_location ( "tmp_module", modulePath )
      if spec is None or spec.loader is None :
        raise ImportError ( f"No se pudo cargar el módulo desde {modulePath}" )

      module = importlib.util.module_from_spec ( spec )
      spec.loader.exec_module ( module )

      bootstrap_cls = getattr ( module, 'Bootstrap', None )
      if bootstrap_cls and callable ( getattr ( bootstrap_cls, 'createApp', None ) ) :
        return True

    except Exception as e :
      logger.log ( e, "EXCEPTION" )
      return False

    return False
