# Python Libraries / Librerías Python
from pathlib import Path
from typing  import Any
from typing  import Dict
from typing  import Optional
import json

# Success Libraries / Librerías Success
from success.common.infra.config.SuccessSystemEnv import SuccessSystemEnv

# Preconditions / Precondiciones


class SuccessFile () :
    """
    Utilitario para operaciones con archivos.
    
    Proporciona métodos estáticos para operaciones comunes con archivos
    como carga de JSON, lectura/escritura de texto, y operaciones de path.
    
    Usage:
        # Cargar JSON desde archivo
        data = SuccessFile.loadAppJson('/apps/myapp/endpoints.json')
        
        # Obtener última línea de archivo
        line_num = SuccessFile.getLastNumberLine()
    """


    @staticmethod
    def getLastNumberLine () -> int :
        """
        Get the number of lines in a file.

        Warning:
            This method depends on LOGGER_FILE which must be configured.

        Returns:
            int: Number of lines in the file.

        Raises:
            FileNotFoundError: If the file does not exist.

        Example:
            count = SuccessFile.getLastNumberLine()  # → 150
        """
        file  = open ( SuccessSystemEnv.get ( 'LOGGER_DIR' ), 'r' )
        lines = file.readlines ()
        count = len ( lines )
        file.close ()

        return count


    @staticmethod
    def loadAppJson ( filename : str ) -> Optional [ Dict [ str, Any ] ] :
        """
        Load a JSON file and return its content as a dictionary.

        Args:
            filename: Path to the JSON file to load.

        Returns:
            Optional[Dict[str, Any]]: Dictionary with JSON content, or None if the file does not exist.

        Example:
            endpoints = SuccessFile.loadAppJson('/apps/myapp/endpoints.json')
            blueprints = SuccessFile.loadAppJson('blueprints.json')
        """
        _data    = ""
        jsonPath = Path ( filename )
        if jsonPath.exists () :
          with open ( jsonPath, 'r' ) as file :
            _data = json.load ( file )

        return _data
