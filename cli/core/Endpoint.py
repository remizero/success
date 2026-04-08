# Python Libraries / Librerías Python
from pathlib import Path
import os
import sys

# Success Libraries / Librerías Success
from success.cli.utils.Package        import Package
from success.cli.utils.RenderTemplate import RenderTemplate

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class Action () :


  def __init__ ( self, args : list = None ) -> None :
    self.appName  = args.to_app
    self.protocol = args.protocol
    self.service  = args.service
    self.version  = args.version
    self.module   = args.module
    self.action   = args.action

    self.context = {
      "app"      : self.appName,
      "protocol" : self.protocol,
      "service"  : self.service,
      "version"  : self.version,
      "module"   : self.module,
      "action"   : self.action
    }

    self.rootPath    = Path ( "apps" ) / self.appName / "services"
    self.basePath    = self.rootPath / self.protocol / self.service / self.version
    self.templateDir = Path ( __file__ ).parent.parent / "resources" / "Action" / self.protocol
    self.fullPath    = self.basePath / self.module / self.action
    self.modulePath  = self.basePath / self.module
    self.actionPath  = self.modulePath / self.action


  def create ( self ) -> None :

    if not self.basePath.exists () :
      print ( f"[ERROR] El servicio '{self.service_name}' no existe para '{self.appName}' bajo protocolo '{self.protocol}' para la versión '{self.version}'." )
      sys.exit ( 1 )

    self.createModule ()
    self.createAction ()

    if self.protocol == "view":
      self.createTemplateView ()

    print ( f"\n✅ Action creado exitosamente en '{self.fullPath}'." )


  def createAction ( self ) -> None :
    actionTemplateDir = Path ( __file__ ).parent.parent / "resources" / "Action" / self.protocol
    if not actionTemplateDir.exists () :
      print ( f"[ERROR] No existen plantillas para el protocolo '{self.protocol}'." )
      sys.exit ( 1 )

    self.actionPath.mkdir ( parents = True, exist_ok = True )
    print ( f"[OK] Directorio creado: {self.actionPath.relative_to ( Path ( 'apps' ) / self.appName )}" )

    for tpl in actionTemplateDir.glob ( "*.j2" ) :
      targetFile = self.actionPath / tpl.name.replace ( ".j2", "" )
      RenderTemplate.toFile ( actionTemplateDir, tpl.name, targetFile, self.context )
      print ( f"[OK] Archivo creado: {targetFile}" )


  def createModule ( self ) -> None :
    moduleTemplateDir = Path ( __file__ ).parent.parent / "resources" / "module"
    if not moduleTemplateDir.exists () :
      print ( f"[ERROR] No existen plantillas para el módulo '{self.module}'." )
      sys.exit ( 1 )

    self.modulePath.mkdir ( parents = True, exist_ok = True )
    print ( f"[OK] Directorio creado: {self.modulePath.relative_to ( Path ( 'apps' ) / self.appName )}" )
    
    initFile = self.modulePath / "__init__.py"

    if not initFile.exists () :
      RenderTemplate.toFile (
        template_dir = moduleTemplateDir,
        template_name = "__init__.py.j2",
        output_path = initFile,
        context = self.context
      )
      print ( f"[OK] __init__.py creado en {initFile}" )


  def createTemplateView ( self ) -> None :
    templateBase = Path ( "apps" ) / self.app_name / "templates"
    targetPath   = templateBase / self.protocol / self.service / self.version / self.module

    targetPath.mkdir ( parents = True, exist_ok = True )

    targetFile = targetPath / f"{self.action}.html"

    if targetFile.exists () :
      print ( f"[WARN] Plantilla ya existe: {targetFile}" )
      return

    # Puedes tener un template base o mínimo para vistas
    baseTemplate = Path ( __file__ ).parent.parent / "resources" / "Action" / "view" / "template.html.j2"

    RenderTemplate.toFile (
      source_dir    = baseTemplate.parent,
      template_name = baseTemplate.name,
      target_file   = targetFile,
      context       = self.context
    )

    print ( f"[OK] Plantilla HTML creada: {targetFile}" )


  def setMethod ( self ) -> None :
    pass


  def setController ( self ) -> None :
    pass
