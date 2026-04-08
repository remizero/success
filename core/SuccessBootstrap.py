# Python Libraries / Librerías Python
from flask import Flask
from flask import request
from flask import session
from typing import Optional
import importlib
import os
import sys

# Success Libraries / Librerías Success
from success.common.base.SuccessClass                 import SuccessClass
from success.common.tools.SuccessEnv                  import SuccessEnv
from success.common.infra.config.SuccessSystemEnv     import SuccessSystemEnv
from success.common.infra.logger.SuccessLogger        import SuccessLogger
from success.common.infra.config.SuccessConfig        import SuccessConfig
from success.engine.infrastructure.SuccessHookManager import SuccessHookManager
from success.common.tools.SuccessClasses              import SuccessClasses
from success.core.SuccessExtensionsDiscoverer         import SuccessExtensionsDiscoverer
from success.core.SuccessExtensionsLoader             import SuccessExtensionsLoader
from success.core.SuccessBlueprintsLoader             import SuccessBlueprintsLoader
from success.common.tools.SuccessPathResolver         import SuccessPathResolver
from success.core.SuccessContext                      import SuccessContext
from success.core.SuccessContext                      import CURRENT_APP
from success.common.helpers.SuccessBreadcrumbs        import SuccessBreadcrumbs

# Application Libraries / Librerías de la Aplicación
from apps.synthetos.infrastructure.Helpers            import Helpers

# Preconditions / Precondiciones


class SuccessBootstrap ( SuccessClass ) :

  __app        : Flask                          = None
  __config     : SuccessConfig                  = None
  __hooks      : SuccessHookManager             = None
  __extensions : dict                           = {}
  _configDict  : dict [ str, Optional [ str ] ] = None
  

  def __init__ ( self ) :
    super ().__init__ ()


  def createApp ( self ) -> Flask :
    if self.__app is not None :
      self._logger.log ( "App ya fue creada. Se retornará la instancia existente.", "WARNING" )

      return self.__app

    module       = sys.modules.get ( self.__module__ )
    appName      = SuccessClasses.getAppName ( self.__module__ )
    self._logger = SuccessLogger ( module = appName, scope = "application" )
    self._logger.log ( "Iniciando proceso de creación de la aplicación.", "INFO" )

    pathResolver = SuccessPathResolver ( module.__file__ )

    self.__app   = Flask (
      appName,
      subdomain_matching = not SuccessSystemEnv.isTrue ( "SUCCESS_APP_MAIN" ),
      host_matching      = True,
      static_host        = f"{appName}.{self._configDict.get ( 'SERVER_NAME' )}:{int ( self._configDict.get ( 'APP_PORT' ) )}",
      # static_host        = f"{self._configDict.get ( 'SERVER_NAME' )}",
      template_folder    = pathResolver.templatesFolder (),
      static_folder      = pathResolver.staticFolder ()
      # ,
      # static_url_path    = "/static"
    )

    # from success.debug.DebugRequestContext import DebugRequestContext
    # self.__app.request_context = DebugRequestContext ( self.__app )


    # self._logger.log ( f"➡️  pathResolver.templatesFolder (): {pathResolver.templatesFolder ()}", "INFO" )
    self._logger.log ( f"➡️  pathResolver.staticFolder (): {pathResolver.staticFolder ()}", "INFO" )
    @self.__app.before_request
    def show_host_debug_info():
      print(f"➡️  request.host: {request.host}")
      print(f"➡️  request.url: {request.url}")
      print(f"➡️  request.blueprint: {request.blueprint}")
      print(f"➡️  request.endpoint: {request.endpoint}")
      print(f"➡️  request.subdomain: {request.host.split('.')[0] if '.' in request.host else None}")
      print(f"➡️  pathResolver.templatesFolder (): {pathResolver.templatesFolder ()}")
      print(f"➡️  pathResolver.staticFolder (): {pathResolver.staticFolder ()}")

    SuccessContext ().setSuccessValue ( "current_app_bootstrapping", appName )
    SuccessContext ().setApp ( self.__app )
    SuccessContext ().setAppModule ( module )
    SuccessContext ().setAppLogger ( self._logger )
    self.__hooks = SuccessHookManager ()
    self.__hooks.register ()

    self.loadConfig ()
    self.__app.config [ "PROPAGATE_EXCEPTIONS" ] = True

    self.__extensions = {}
    self.loadExtensions ()
    self.loadCustomExtensions ()

    self.loadBlueprints ()

    self.loadSimulators ()
    self.loadContext ()

    self._logger.log ( "Aplicación creada exitosamente.", "INFO" )
    self.whoami ()
    SuccessContext ().setSuccessValue ( "current_app_bootstrapping", None )

    return self.__app


  def _extendConfig ( self, extendConfig : dict ) -> None :
    self._logger.log ( "Cargando configuración extendida de la aplicación...", "INFO" )
    if ( self.__config ) :
      self.__config.extend ( extendConfig )

    else :
      self._logger.log ( "La clase SuccessConfig debe ser cargada previamente...", "ERROR" )
      return

    if ( self.__app ) :
      self.__app.config.update ( extendConfig )

    else :
      self._logger.log ( "La aplcación Flask ser cargada previamente...", "ERROR" )
      return

    self._logger.log ( "Carga de configuración extendida de la aplicación terminada exitosamente...", "INFO" )


  def getApp ( self ) -> Flask :
    if self.__app is None :
      self._logger.log ( "getApp llamado antes de createApp. Se creará la apps automáticamente.", "WARNING" )

      return self.createApp ()

    return self.__app


  def loadBlueprints ( self ) -> None :
    self._logger.log ( "Registrando Blueprints...", "INFO" )

    blueprints = SuccessBlueprintsLoader (
      apps   = self.__app,
      config = self.__config,
      hooks  = self.__hooks
    )
    self._logger.log ( f"apps.{SuccessClasses.getAppName ( self.__module__ )}.services", "INFO" )
    blueprints.load ( f"apps.{SuccessClasses.getAppName ( self.__module__ )}.services", self.__config )

    self._logger.log ( "Registro de Blueprints finalizado exitosamente...", "INFO" )


  def loadConfig ( self ) -> None :
    self._logger.log ( "Iniciando carga de configuración de la aplicación...", "INFO" )

    self.__hooks.execute ( when = "before", action = "config_extend" )

    if self._configDict.get ( "SUCCESS_CUSTOM_CONFIG_CLASS" ) :
      self._logger.log ( "Cargando configuración personalizada de la aplicación...", "INFO" )
      custom_config_class_path = self._configDict.get ( "SUCCESS_CUSTOM_CONFIG_CLASS" )
      module_name, class_name = custom_config_class_path.rsplit ( ".", 1 )
      module = importlib.import_module ( module_name )
      self.__config = getattr ( module, class_name )

    else :
      self._logger.log ( "Cargando configuración estandar de la aplicación...", "INFO" )

      self.__config = SuccessConfig ( self._configDict )

    self.__app.config.from_object ( self.__config )

    self.__hooks.execute ( when = "after", action = "config_extend" )

    self._logger.log ( "Carga de configuración de la aplicación terminada exitosamente...", "INFO" )


  def loadCustomExtensions ( self ) -> None :
    self._logger.log ( "Cargando extensiones personalizadas (si existen)...", "INFO" )
    loader = SuccessExtensionsDiscoverer (
      apps   = self.__app,
      config = self.__config,
      hooks  = self.__hooks
    )
    customExtensions = loader.discover ()
    if customExtensions :
      self.__extensions.extend ( customExtensions )

    self._logger.log ( "Carga de extensiones personalizadas de la aplicación terminada exitosamente...", "INFO" )


  def loadExtensions ( self ) -> None :
    self._logger.log ( "Cargando extensiones básicas de la aplicación...", "INFO" )

    loader = SuccessExtensionsLoader (
      apps   = self.__app,
      config = self.__config,
      hooks  = self.__hooks
    )
    self.__extensions = loader.load ()

    self._logger.log ( "Carga de extensiones básicas de la aplicación terminada exitosamente...", "INFO" )


  def loadSimulators ( self ) -> None :
    @self.__app.before_request
    def simulate_session () :
      if 'user_token' not in session :
        session [ 'user_token' ]  = "test-token-supercow"
        session [ 'user_name'  ]  = "Superuser"
        session [ 'user_role' ]   = "supercow"
        session [ 'tenant_list' ] = [ "default_tenant" ]


  def loadContext ( self ) -> None :
    @self.__app.context_processor
    def inject_context () :
      headers, version, identity, heartbeat = Helpers.get_chroma_info ()
      return {
        'breadcrumb': SuccessBreadcrumbs.build (),
        'version': version,
        'identity': identity,
        'heartbeat_ns': heartbeat
      }


  def whoami ( self ) -> None :
    @self.__app.before_request
    def set_current_app () :
      CURRENT_APP.set ( SuccessClasses.getAppName ( self.__module__ ) )
