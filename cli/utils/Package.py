# Python Libraries / Librerías Python
import shutil
from pathlib import Path

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class Package () :


  @staticmethod
  def copyInitTemplate ( path : str ) -> None :
    init_template = Path ( __file__ ).parent.parent / "resources" / "generics" / "__init__.py"

    if not init_template.exists () :
      print ( f"[ERROR] Template base __init__.py no encontrado en {init_template}" )
      return

    init_file = path / "__init__.py"
    if not init_file.exists () :
      shutil.copy ( init_template, init_file )
      print ( f"[OK] __init__.py creado en {init_file}" )


  @staticmethod
  def ensureStructure ( path : Path ) -> None :
    """
    Asegura que cada nivel desde 'path' hacia arriba contenga un __init__.py,
    copiando el archivo base desde resources/app/__init__.py
    """
    for parent in reversed ( path.parents ) :
      Package.copyInitTemplate ( parent )


  @staticmethod
  def fixAllInits ( app_path : Path ) -> None :
    init_template = Path ( __file__ ).parent.parent / "resources" / "generics" / "__init__.py"
    if not init_template.exists () :
      print ( f"[ERROR] No se encontró el archivo plantilla: {init_template}" )
      return

    for dirpath, dirnames, filenames in os.walk ( app_path ) :
      dir_path = Path ( dirpath )
      init_file = dir_path / "__init__.py"
      if not init_file.exists () :
        shutil.copy ( init_template, init_file )
        print ( f"[OK] __init__.py inyectado en {init_file}" )
