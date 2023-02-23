# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts        import Output as SuccessOutput
from kernel.abstracts.Output import Structs
from kernel.abstracts.Output import Http


# Preconditions / Precondiciones


class Output ( SuccessOutput ) :

  def __init__ ( self, isLogin : bool = False ) -> None :
    super ().__init__ ( isLogin )
    if ( self.__successOutput and Http.isMethod ( 'GET' ) ) :
      self.__schemaOutput [ 'model' ].append ( Structs.jsonInputSchema ( 'username', 'Usuario', '', '50', 'True', 'text', 1 ) )
      self.__schemaOutput [ 'model' ].append ( Structs.jsonInputSchema ( 'password', 'Contrase;a', '', '255', 'True', 'text', 2 ) )
      self.__schemaOutput [ 'model' ].append ( Structs.jsonInputSchema ( 'email', 'Correo', '', '50', 'True', 'text', 3 ) )

  def data ( self, data : dict ) -> dict :
    super ().data ( data )
    pass
