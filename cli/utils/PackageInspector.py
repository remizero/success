# Python Libraries / Librerías Python
import os
import shutil
from pathlib import Path

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class PackageInspector () :

  @staticmethod
  def get_missing_init_paths ( app_path: Path ) :
    missing = []
    for dirpath, dirnames, filenames in os.walk ( app_path ) :
      dir_path = Path ( dirpath )
      if not ( dir_path / "__init__.py" ).exists () :
        missing.append ( dir_path )
    return missing

  @staticmethod
  def fix_missing_inits ( app_path : Path, template_path : Path ) :
    missing_paths = PackageInspector.get_missing_init_paths ( app_path )
    for dir_path in missing_paths :
      shutil.copy ( template_path, dir_path / "__init__.py" )
      print ( f"[FIXED] __init__.py creado en: {dir_path}" )
    return missing_paths

  @staticmethod
  def report_missing ( app_path : Path ) :
    missing = PackageInspector.get_missing_init_paths ( app_path )
    for dir_path in missing :
      print ( f"[MISSING] __init__.py faltante en: {dir_path}" )
    return missing
