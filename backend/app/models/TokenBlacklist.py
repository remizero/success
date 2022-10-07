# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel import Model
from utils import (
  Fields,
  Relations
)


# Preconditions / Precondiciones
relator = Relations ( 'TokenBlacklist' )

class TokenBlacklist ( Model ) :

  # Atributos específicos del modelo
  jti = Fields.db_string ( 36 )
  type = Fields.db_string ( 10 )
  user_id = Fields.db_foreign_key ( 'User' )

  # Tablas relacionadas
  users = relator.hasOne ( 'User' )

  # Constructor
  def __init__ ( self, **kwargs ) :
    self.inputData ( **kwargs )
