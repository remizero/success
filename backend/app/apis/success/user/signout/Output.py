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
    struct = Structs.signout ()
    struct [ 'msg' ] = 'Usuario desconectado correctamente'
    struct [ 'loggedin' ] = False
    struct [ 'type' ] = 'normal'
    struct [ 'status' ] = 200
    return struct.copy ()
