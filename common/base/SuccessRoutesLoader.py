# Python Libraries / Librerías Python
from flask import Blueprint
from flask import Flask
from abc   import ABC
from abc   import abstractmethod
import os
import importlib.util
import importlib
import pkgutil

# Success Libraries / Librerías Success
from success.core.SuccessContext                      import SuccessContext
from success.common.tools.SuccessEnv                  import SuccessEnv
from success.common.infra.config.SuccessConfig        import SuccessConfig
from success.engine.infrastructure.SuccessHookManager import SuccessHookManager
from success.common.tools.SuccessClasses              import SuccessClasses
from success.common.base.SuccessClass                 import SuccessClass

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessRoutesLoader ( SuccessClass ) :

  _app        : Flask              = None
  _config     : SuccessConfig      = None
  _hooks      : SuccessHookManager = None
  _blueprints : list               = []


  def __init__ ( self, apps : Flask, config : SuccessConfig = None, hooks : SuccessHookManager = None ) -> None :
    super ().__init__ ()
    self._config     = config
    self._app        = apps
    self._hooks      = hooks
    self._blueprints = []


  def discover ( self, package : str ) :
    try :
      package_module = importlib.import_module ( package )

    except ModuleNotFoundError as mnfe :
      self._logger.log ( f"[Blueprints] Cannot import package '{package}': {mnfe}", "ERROR" )
      return

    for finder, module_name, is_pkg in pkgutil.walk_packages ( package_module.__path__, prefix = package + "." ) :
      if not is_pkg :
        continue

      try :
        module = importlib.import_module ( module_name )
        bp = getattr ( module, 'bp', None )

        if isinstance ( bp, Blueprint ) :
          self._blueprints.append ( bp )
          self._logger.log ( f"[Blueprints] Registered blueprint: {module_name}", "INFO" )

        else :
          self._logger.log ( f"[Blueprints] No valid 'bp' found in {module_name}", "ERROR" )

      except Exception as e :
        self._logger.log ( f"[Blueprints] Failed to import/register blueprint from {module_name}: {e}", "ERROR" )


  @abstractmethod
  def getSubpackage ( self ) -> str :
    pass


  def load ( self, package : str ) :
    subPackage = self.getSubpackage ()
    self._logger.log ( f"Iniciando carga de blueprints para el paquete {subPackage}...", "INFO" )

    self.discover ( f"{package}.{subPackage}" )
    self.register ()
    
    self._logger.log ( f"Carga de blueprints para el paquete {subPackage} finalizada.", "INFO" )


  def register ( self ) :
    for bp in self._blueprints :
      self._hooks.execute ( when = "before", action = "blueprint_register", target = bp )
      self._app.register_blueprint ( bp )
      self._logger.log ( f"Blueprint '{bp.name}' registrado.", "INFO" )
      self._hooks.execute ( when = "after", action = "blueprint_register", target = bp )

    self._logger.log ( "Registro de blueprints completado.", "INFO" )
