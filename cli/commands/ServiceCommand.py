# Python Libraries / Librerías Python
import os
import sys
from pathlib import Path

# Success Libraries / Librerías Success
from success.cli.core.Service import Service

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class ServiceCommand :

    @staticmethod
    def create ( args : list = None ) -> None :
      service = Service ( args )
      service.create ()

      print ( f"\n✅ Servicio '{args.service}' creado en app '{args.to_app}' bajo protocolo '{args.protocol}' en su versión '{args.version}'." )