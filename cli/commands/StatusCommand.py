# Python Libraries / Librerías Python

# Success Libraries / Librerías Success
from success.cli.core.Status import Status

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class StatusCommand () :


  @staticmethod
  def run ( args : list = None ) -> None :
    status = Status ( args )
    status.run ()
    exit ( 0 )
