# Python Libraries / Librerías Python
from pathlib import Path
import sys

# Success Libraries / Librerías Success
from success.cli.utils.Package import Package

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class Service () :

  def __init__ ( self, args : list = None ) -> None :
    self.app_name     = args.to_app
    self.protocol     = args.protocol
    self.service = args.service
    self.version      = args.version

    self.root_path    = Path ( "apps" ) / self.app_name / "services"
    self.base_path    = self.root_path / self.protocol / self.service / self.version

  def create ( self ) -> None :
    if self.base_path.exists () :
      print ( f"[ERROR] El servicio '{self.service}' ya existe para '{self.app_name}' bajo protocolo '{self.protocol}'." )
      sys.exit ( 1 )

    current_path = self.root_path
    for segment in [ self.protocol, self.service, self.version ] :
      current_path = current_path / segment
      current_path.mkdir ( parents = True, exist_ok = True )
      print ( f"[OK] Directorio creado: {current_path.relative_to ( Path ( 'apps' ) / self.app_name )}" )
      Package.copyInitTemplate ( current_path )

    print ( f"\n✅ Servicio creado exitosamente en '{self.base_path}'." )
