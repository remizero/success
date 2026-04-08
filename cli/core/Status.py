# Python Libraries / Librerías Python
import os
import sys
# from .jinja_utils import render_template_file  # Separalo si querés
from pathlib import Path

# Success Libraries / Librerías Success
from success.Success                  import Success
from success.core.SuccessSystemState         import SuccessSystemState
from success.cli.utils.Package        import Package
from success.cli.utils.RenderTemplate import RenderTemplate

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class Status () :


  def __init__ ( self, args : list = None ) -> None :
    self.args = args


  def run ( self ) :
    success = Success ()
    success.create ()
    print ( SuccessSystemState.report () )