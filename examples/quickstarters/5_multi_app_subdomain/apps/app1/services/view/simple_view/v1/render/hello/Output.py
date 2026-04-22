# Python Libraries / Librerías Python

# Success Libraries / Librerías Success
from success.engine.io.SuccessOutput import SuccessOutput
from success.engine.io.RenderIntent  import RenderIntent

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class Output ( SuccessOutput ) :


  def __init__ ( self ) -> None :
    super ().__init__ ()
    self._intent = RenderIntent ( "hello.html" )
