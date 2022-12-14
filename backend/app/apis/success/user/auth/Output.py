# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.Output import (
  Output as SuccessOutput,
  OutputType
)
from utils import Structs


# Preconditions / Precondiciones


class Output ( SuccessOutput ) :

  def __init__ ( self, outputType : OutputType = OutputType.SUCCESS, emptySchema : bool = True ) -> None :
    super ().__init__ ( outputType, emptySchema )

  def data ( self, data : dict ) -> dict :
    struct = Structs.signin ()
    struct [ 'username' ] = data [ 'username' ]
    struct [ 'loggedin' ] = True
    return struct.copy ()
