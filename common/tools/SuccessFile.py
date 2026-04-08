# Python Libraries / Librerías Python
from pathlib import Path
import json

# Success Libraries / Librerías Success
from success.core.SuccessContext              import SuccessContext
from success.common.tools.SuccessEnv          import SuccessEnv
from success.common.tools.SuccessPathResolver import SuccessPathResolver

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessFile () :


  @staticmethod
  def getLastNumberLine () -> int :
    file  = open ( SuccessSystemEnv.get ( 'LOGGER_DIR' ), 'r' )
    lines = file.readlines ()
    count = len ( lines )
    file.close ()

    return count


  @staticmethod
  def loadAppJson ( filename : str ) :
    _data = ""
    jsonPath = Path ( SuccessPathResolver.getPath ( SuccessContext ().getAppModule ().__file__ ) ) / filename
    if jsonPath.exists () :
      with open ( jsonPath, 'r' ) as file :
        _data = json.load ( file )

    return _data
