# Python Libraries / Librerías Python
import os
import sys
# from .jinja_utils import render_template_file  # Separalo si querés
from pathlib import Path

# Success Libraries / Librerías Success
from success.cli.core.App import App

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class AppCommand () :


  @staticmethod
  def create ( args : list = None ) -> None :
    app = App ( args )

    # Crear directorio base de la aplicación
    app.createAppDir ()
    
    # Crear estructura base
    app.createBaseStructure ()

    # Crear carpeta para tipo de servicio
    app.createServiceType ()

    # Renderizar y copiar archivos base
    app.renderBaseFiles ()

    print ( f"\n✅ Aplicación '{app.app_name}' creada exitosamente en '{app.base_path}'." )
