# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from common import Validator
from kernel import Debug


# Preconditions / Precondiciones


class Input ( Validator ) :

  def __init__ ( self, withId : bool = False, additionalProperties : bool = False ) -> None :
    super ().__init__ ( withId, additionalProperties )
    self.schema [ 'properties' ].setdefault ( 'username', { 'type' : 'string', 'maxLength' : 50 } )
    self.schema [ 'properties' ].setdefault ( 'password', { 'type' : 'string', 'maxLength' : 255 } )
    self.schema [ 'required' ].append ( 'username' )
    self.schema [ 'required' ].append ( 'password' )
    #Debug.log ( self.schema )
