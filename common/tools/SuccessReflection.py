# Python Libraries / Librerías Python
from pprint import pprint
from types  import ModuleType
from typing import Any
import importlib
import os

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessReflection () :


  @staticmethod
  def getScopeFromModule ( modulePath : str ) -> str :
    """
    Determina el ámbito base a partir del path del módulo.
    Ejemplo:
      - apps.synthetos.services...  => "application"
      - success.engine.io...        => "success"
    """
    parts = modulePath.split ( "." )

    if not parts :
      return "unknown"

    if parts [ 0 ] == "apps" :
      return "application"

    if parts [ 0 ] == "success" :
      return "framework"

    return "unknown"


  @staticmethod
  def getAppNameFromModule ( modulePath : str ) -> str :
    parts = modulePath.split ( "." )

    if not parts :
      return "unknown"

    if parts [ 0 ] == "apps" :
      idx = parts.index ( "apps" )
      return parts [ idx + 1 ]

    if parts [ 0 ] == "success" :
      return "success"

    return "unknown"
