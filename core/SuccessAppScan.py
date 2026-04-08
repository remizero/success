# Python Libraries / Librerías Python
from flask import Flask
import os
import importlib.util

# Success Libraries / Librerías Success
from success.common.base.SuccessClass                  import SuccessClass
from success.common.infra.logger.SuccessLogger         import SuccessLogger
from success.core.SuccessAppValidator                  import SuccessAppValidator
from success.core.SuccessAppLoader                     import SuccessAppLoader
from success.core.SuccessSystemState                   import SuccessSystemState
from success.common.tools.BootCommentator              import BootCommentator
from success.common.tools.SuccessEnv                   import SuccessEnv
from success.common.infra.config.SuccessSystemEnv      import SuccessSystemEnv
from success.core.SuccessContext                       import SuccessContext
from success.common.tools.SuccessStructs               import SuccessStructs
from success.common.tools.SuccessAppPlaceholderFactory import SuccessAppPlaceholderFactory

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessAppScan ( SuccessClass ) :

  _rootApp       : str  = None
  _secondaryApps : list = []


  def __init__ ( self ) :
    super ().__init__ ()
    self._rootApp       = SuccessSystemEnv.get ( "SUCCESS_MAIN_APP" )
    self._secondaryApps = SuccessEnv.toList ( SuccessSystemEnv.get ( "SUCCESS_SECONDARY_APPS" ) )


  def getSecondaryApps ( self ) -> dict [ str, Flask ] :
    self._logger.log ( "Iniciando carga de aplicaciones del sistema.", "INFO" )
    
    apps = {}

    try :
      for appName in self._secondaryApps :
        path = os.path.join ( "apps", appName )
        if os.path.isdir ( path ) :
          app = SuccessAppLoader.getApp ( path )
          if app :
            mount_path = f"/{appName}"
            apps [ mount_path ] = app
            SuccessSystemState.addAppCargada ( app )
            self._logger.log ( "Carga de aplicaciones del sistema realizada exitosamente.", "INFO" )

          else :
            SuccessSystemState.addAppOmitida ( path, "No define 'apps' ni 'createApp ()'" )

        else :
          SuccessSystemState.addAppOmitida ( path, "Directorio no encontrado" )

    except Exception as e :
      self._logger.log ( e, "ERROR" )
      raise  # Relanzamos la excepción para que no quede oculta

    return apps


  def getRootApp ( self ) -> Flask | None :
    self._logger.log ( "Iniciando carga de aplicación base del sistema.", "INFO" )

    try :
      path = os.path.join ( "apps", self._rootApp )
      if not os.path.isdir ( path ) :
        raise FileNotFoundError

      app = SuccessAppLoader.getApp ( path )
      if app :
        self._logger.log ( "Carga de aplicación base del sistema realizada exitosamente." )
        return app

    except Exception as e :
      if SuccessSystemEnv.isTrue ( "SUCCESS_ALLOW_NO_MAIN_APP" ) :
        if SuccessSystemEnv.get ( "APP_ENV" ) != "development" :
          self._logger.log ( "🚫 'SUCCESS_ALLOW_NO_MAIN_APP' solo permitido en modo desarrollo.", "ERROR" )
          exit ( 1 )

        self._logger.log ( "⚠️ Usando SuccessAppPlaceholder como raíz.", "WARNING" )
        return SuccessAppPlaceholderFactory.build ()

      self._logger.log ( "🚫 No se pudo cargar la aplicación base y no se permite continuar sin ella.", "ERROR" )
      exit ( 1 )


  def getAllApps ( self ) -> dict [ str, Flask ] :
    """Carga todas las apps disponibles sin duplicar, y las clasifica según el .env"""
    self._logger.log ( "Iniciando carga total de aplicaciones del sistema.", "INFO" )

    allApps = set ()
    if self._rootApp :
      allApps.add ( self._rootApp )

    allApps.update ( self._secondaryApps )

    apps = {}
    for appName in allApps :
      path = os.path.join ( "apps", appName )
      if not os.path.isdir ( path ) :
        SuccessSystemState.addAppOmitida ( path, "Directorio no encontrado" )
        continue

      app = SuccessAppLoader.getApp ( path )
      if app :
        apps [ appName ] = app
        SuccessSystemState.addAppCargada ( app )

      else :
        SuccessSystemState.addAppOmitida ( path, "No define 'apps' ni 'createApp()'" )

    return apps


  @staticmethod
  def report ( base_dir = 'apps' ) -> list [ dict ] :
    results = []
    for item in os.listdir ( base_dir ) :
      full_path = os.path.join ( base_dir, item )
      if not os.path.isdir ( full_path ) :
        continue

      result = {
        'name' : item,
        'path' : full_path,
        'valid_dir' : SuccessAppValidator.isValidAppDir ( full_path ),
        'has_factory' : SuccessAppValidator.hasFactoryOrInstance ( full_path ),
      }
      results.append ( result )

    return results
