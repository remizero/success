# Python Libraries / Librerías Python
from pprint import pprint
from types  import ModuleType
from typing import Any
import importlib
import os

# Success Libraries / Librerías Success
from success.core.SuccessContext import SuccessContext

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessClasses () :


  @staticmethod
  def instanceFromString ( className : str, params : set ) -> dict [ str, Any ] :
    # https://programmerclick.com/article/23561860026/
    # https://cosasdedevs.com/posts/crear-una-instancia-de-una-clase-mediante-un-string-con-python/
    pprint ( globals () )
    return globals () [ className ] ( params )


  @staticmethod
  def hasMethod ( instance : object, methodName : str ) -> bool :

    return hasattr ( instance, methodName )


  @staticmethod
  def normalizeModule ( normalizedPackage : str, moduleClass : str ) -> str :

    return ".".join ( [ normalizedPackage, moduleClass ] )


  @staticmethod
  def normalizePackage ( packagePath : str, prefix : str ) -> str :
    normalized_path = os.path.normpath ( packagePath )

    parts = normalized_path.split ( os.sep )

    if parts :
      last = parts [ -1 ]
      if prefix :
        last = f"{prefix.strip ( '_' )}_{last}"
      parts [ -1 ] = last

    return ".".join ( parts )


  @staticmethod
  def getAppName ( modulePath : str ) -> str :
    parts = modulePath.split ( '.' )
    try :
      idx = parts.index ( 'apps' )
      return parts [ idx + 1 ]

    except ( ValueError, IndexError ) :
      return "unknown"


  @staticmethod
  def createAppName ( modulePath : str ) -> str :
    parts = modulePath.split ( "." ) if "." in modulePath else modulePath.split ( os.sep )
    try :
      idx = parts.index ( "apps" )
      app_name = parts [ idx + 1 ]

    except ( ValueError, IndexError ) :
      raise ValueError ( f"No se pudo determinar el nombre de la apps a partir de '{modulePath}'" )
    
    env_prefix = os.getenv ( "SUCCESS_APP_PREFIX", "" )
    return f"{env_prefix}{app_name}" if env_prefix else app_name


  @staticmethod
  def getAppNameFromPath ( modulePath : str ) -> str :
    parts = modulePath.split ( "." ) if "." in modulePath else modulePath.split ( os.sep )
    try :
      idx = parts.index ( "apps" )
      app_name = parts [ idx + 1 ]

    except ( ValueError, IndexError ) :
      raise ValueError ( f"No se pudo determinar el nombre de la apps a partir de '{modulePath}'" )
    
    env_prefix = os.getenv ( "SUCCESS_APP_PREFIX", "" )
    return f"{env_prefix}{app_name}" if env_prefix else app_name


  @staticmethod
  def getScopeFromModule ( modulePath : str ) -> str :
    """
    Determina el ámbito base a partir del path del módulo.
    Ejemplo:
      - apps.synthetos.services...  => "application"
      - success.engine.io...        => "success"
    """
    parts = modulePath.split ( "." )

    if not parts :
      return "unknown"

    if parts [ 0 ] == "apps" :
      return "application"

    if parts [ 0 ] == "success" :
      return "framework"

    return "unknown"


  @staticmethod
  def getAppNameFromModule ( modulePath : str ) -> str :
    parts = modulePath.split ( "." ) if "." in modulePath else modulePath.split ( os.sep )
    try :
      idx = parts.index ( "apps" )
      app_name = parts [ idx + 1 ]

    except ( ValueError, IndexError ) :
      raise ValueError ( f"No se pudo determinar el nombre de la apps a partir de '{modulePath}'" )
    
    env_prefix = os.getenv ( "SUCCESS_APP_PREFIX", "" )
    return f"{env_prefix}{app_name}" if env_prefix else app_name


  @staticmethod
  def getModule ( package : str, moduleParts, className : str ) -> ModuleType :

    baseModule = ".".join ( SuccessContext ().getAppModule ().__name__.split ( "." ) [ : -1 ] )
    fullModulePath = f"{baseModule}.{package}." + ".".join ( moduleParts + [ className ] )
    module = importlib.import_module ( fullModulePath )

    return module


  @staticmethod
  def getClassFromModule ( module : ModuleType, className : str ) -> Any :
    if not hasattr ( module, className ) :
      raise ImportError ( f"No se encontró la clase '{className}' en el módulo '{module.__file__}'" )

    return getattr ( module, className )


  @staticmethod
  def getMethodFromClass ( instance : object, methodName : str ) -> Any :
    if not hasattr ( instance, methodName ) :
      raise AttributeError ( f"El método '{methodName}' no existe en la clase '{instance.__class__.__name__}'" )

    return getattr ( instance, methodName )
