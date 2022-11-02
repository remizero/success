# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.Model import (
  Fields,
  Model,
  Relations
)


# Preconditions / Precondiciones
relator = Relations ( 'TokenBlacklist' )


class TokenBlacklist ( Model ) :

  # Model Specific Attributes / Atributos específicos del modelo
  jti = Fields.db_string ( 36 )
  type = Fields.db_string ( 10 )
  user_id = Fields.db_foreign_key ( 'User' )

  # Related tables / Tablas relacionadas
  #users = relator.hasOne ( 'User' )
