# Python Libraries / Librerías Python
import ast
import importlib
import json
import os
from pathlib import Path

# Success Libraries / Librerías Success
from success.core.SuccessContext               import SuccessContext
from success.common.tools.SuccessPathResolver  import SuccessPathResolver
from success.common.infra.logger.SuccessLogger import SuccessLogger

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessHookSecurityAuditor () :

  __logger : SuccessLogger = None

  DANGEROUS_NODES = {
      "Exec", "Eval", "Call",
      "Import", "ImportFrom", "Delete"
  }

  DANGEROUS_NAMES = {
      "open", "exec", "eval", "compile", "os", "subprocess", "socket", "requests"
  }


  def __init__ ( self, strict: bool = False ) :
    self.__strict = strict
    self.__logger = SuccessContext ().getSuccessValue ( "LOGGER" )


  def audit_hooks ( self ) :
    hooks_path = Path ( SuccessPathResolver.getPath ( SuccessContext ().getAppModule ().__file__ ) ) / "hooks.json"
    if not hooks_path.exists () :
      self.__logger.log ( "No se encontró archivo hooks.json", "WARNING" )
      return

    with open ( hooks_path, "r" ) as f :
      hooks = json.load ( f )

    if not isinstance ( hooks, list ) :
      self.__logger.log ( "El archivo hooks.json debe contener una lista de hooks.", "ERROR" )
      return

    for hook in hooks :
      name = hook.get ( "name" )
      callback = hook.get ( "callback" )
      if not callback :
        self.__logger.log ( f"[{name}] Callback no definido.", "ERROR" )
        continue

      try :
        class_path, method_name = callback.rsplit ( ".", 1 )
        module_path = self.resolve_module_path ( class_path )
        if not module_path or not os.path.exists ( module_path ) :
          self.__logger.log ( f"[{name}] No se encontró archivo para {class_path}", "ERROR" )
          continue

        self.analyze_source ( name, module_path )

      except Exception as e :
          self.__logger.log ( f"[{name}] Error auditando hook: {str ( e )}", "ERROR" )


  def resolve_module_path ( self, dotted_path ) :
    base_module = SuccessContext ().getAppModule ().__name__
    base_parts = base_module.split ( "." ) [ : -1 ]  # Quitar Bootstrap
    full_path = ".".join ( base_parts + [ "infrastructure" ] + dotted_path.split ( "." ) )
    try :
      module = importlib.import_module ( full_path )
      return module.__file__

    except Exception :
      return None


  def analyze_source ( self, hook_name, file_path ) :
    with open ( file_path, "r" ) as f :
      source = f.read ()

    tree = ast.parse ( source )
    issues = []

    for node in ast.walk ( tree ) :
      if isinstance ( node, ast.Call ) :
        func = node.func
        if isinstance ( func, ast.Name ) and func.id in self.DANGEROUS_NAMES :
          issues.append ( f"Uso de función peligrosa: {func.id}" )

        elif isinstance ( func, ast.Attribute ) and func.attr in self.DANGEROUS_NAMES :
          issues.append ( f"Acceso sospechoso a método: {func.attr}" )

      elif isinstance ( node, ast.Import ) or isinstance ( node, ast.ImportFrom ) :
        for alias in node.names :
          if alias.name.split ( "." ) [ 0 ] in self.DANGEROUS_NAMES :
            issues.append ( f"Importación peligrosa: {alias.name}" )

    if issues :
      for issue in issues :
        self.__logger.log ( f"[{hook_name}] ⚠️ {issue}", "WARNING" if not self.__strict else "ERROR" )

    else :
      self.__logger.log ( f"[{hook_name}] ✅ Hook auditado sin problemas.", "INFO" )
