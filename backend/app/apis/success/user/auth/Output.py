# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.Output import (
  Output as SuccessOutput,
  Structs
)
from utils import Http


# Preconditions / Precondiciones


class Output ( SuccessOutput ) :

  def __init__ ( self, isLogin : bool = False ) -> None :
    super ().__init__ ( isLogin )
    if ( self.__successOutput and Http.isMethod ( 'GET' ) ) :
      self.__schemaOutput [ 'model' ].append ( Structs.jsonInputSchema ( 'username', 'Usuario', '', '50', 'True', 'text', 1 ) )
      self.__schemaOutput [ 'model' ].append ( Structs.jsonInputSchema ( 'password', 'Contrase;a', '', '255', 'True', 'text', 2 ) )

  def data ( self, data : dict ) -> dict :
    self.__output = Structs.signin ()
    self.__output [ 'username' ] = data [ 'username' ]
    self.__output [ 'fullname' ] = data [ 'fullname' ]
    self.__output [ 'status' ] = data [ 'status' ]
    self.__output [ 'type' ] = data [ 'type' ]
