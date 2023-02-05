# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.Model import (
  Fields,
  Model,
  Relations
)


# Preconditions / Precondiciones
relator = Relations ( 'UserProfile' )


class UserProfile ( Model ) :

  # Model Specific Attributes / Atributos específicos del modelo
  user_id = Fields.foreignKey ( 'User', primaryKey = True )
  profile_id = Fields.foreignKey ( 'Profile', primaryKey = True )

  # Related tables / Tablas relacionadas
  user = relator.relationalTable ( 'User' )
  profile = relator.relationalTable ( 'Profile' )
