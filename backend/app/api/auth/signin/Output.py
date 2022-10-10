# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from common import (
  OutputType,
  SuccessOutput
)


# Preconditions / Precondiciones


class Output ( SuccessOutput ) :

  def __init__ ( self, outputType : OutputType = OutputType.SUCCESS, emptySchema : bool = True ) -> None :
    super ().__init__ ( outputType, emptySchema )

  # passasdf = {
  #   "username": resultData [ 0 ] [ 'username' ],
  #   "email": resultData [ 0 ] [ 'email' ],
  #   "name": resultData [ 0 ] [ 'name' ],
  #   "lastname": resultData [ 0 ] [ 'lastname' ],
  #   "group_id": resultData [ 0 ] [ 'group_id' ],
  #   "loggedin": True
  # }
