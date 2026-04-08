# Python Libraries / Librerías Python
import os
import sys

# Success Libraries / Librerías Success
from success.cli.core.Action import Action

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class EndpointCommand () :


  @staticmethod
  def create ( args : list = None ) -> None :
    Action = Action ( args )
    Action.create ()

    print ( f"\n✅ Action '{args.action}' creado en app '{args.to_app}' bajo protocolo '{args.protocol}' en su versión '{args.version}'." )
