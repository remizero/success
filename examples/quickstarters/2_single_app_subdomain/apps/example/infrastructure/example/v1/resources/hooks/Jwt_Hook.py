# Python Libraries / Librerías Python

# Success Libraries / Librerías Success
from success.engine.infrastructure.SuccessHook import SuccessHook

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class Jwt_Hook () :


  def __init__ ( self ) :
    super ().__init__ ()


  def execute ( self, context : dict ) -> None :
    print ( f"{self.__class__} ha recibido el context {context}" )
