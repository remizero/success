# Python Libraries / Librerías Python
import os
import sys
# from .jinja_utils import render_template_file  # Separalo si querés
from pathlib import Path

# Success Libraries / Librerías Success
from success.cli.utils.Package        import Package
from success.cli.utils.RenderTemplate import RenderTemplate

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones
APP_TEMPLATES = [ "__init__.py.j2", "Bootstrap.py.j2", ".env.j2" ]
DEFAULT_APP_TYPE = "restful"
FIXED_DIRS = [
  "infrastructure",
  "models",
  "modules",
  "services",
  "static",
  "templates",
]


class App () :


  def __init__ ( self, args : list = None ) -> None :
    self.app_name  = args.app_name
    self.app_type  = args.app_type or DEFAULT_APP_TYPE
    self.base_path = Path ( "apps" ) / self.app_name


  def createAppDir ( self ) :
    if self.base_path.exists () :
      print ( f"[ERROR] La aplicación '{self.app_name}' ya existe." )
      sys.exit ( 1 )

    print ( f"[INFO] Creando nueva app: {self.app_name}" )
    self.base_path.mkdir ( parents = True )


  def createBaseStructure ( self ) :
    for folder in FIXED_DIRS :
      ( self.base_path / folder ).mkdir ( parents = True, exist_ok = True )
      print ( f"[OK] Carpeta base creada: {folder}" )
      Package.copyInitTemplate ( self.base_path / folder )


  def createServiceType ( self ) :
    service_type_dir = self.base_path / "services" / self.app_type
    service_type_dir.mkdir ( parents = True, exist_ok = True )
    Package.copyInitTemplate ( service_type_dir )
    print ( f"[OK] Carpeta de tipo de servicio creada: services/{self.app_type}" )


  def renderBaseFiles ( self ) :
    app_template_dir = Path ( __file__ ).parent.parent / "resources" / "app"
    context = { "app_name" : self.app_name }

    for tpl_file in APP_TEMPLATES :
      output_file = self.base_path / tpl_file.replace ( ".j2", "" )
      RenderTemplate.toFile ( str ( app_template_dir ), tpl_file, output_file, context )
      print ( f"[OK] Archivo creado: {output_file}" )
