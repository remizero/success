# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.Model import (
  Fields,
  Model,
  Relations
)


# Preconditions / Precondiciones
relator = Relations ( 'UserRole' )


class UserRole ( Model ) :

  # Model Specific Attributes / Atributos específicos del modelo
  user_id = Fields.foreignKey ( 'User', primaryKey = True )
  role_id = Fields.foreignKey ( 'Role', primaryKey = True )

  # Related tables / Tablas relacionadas
  user = relator.relationalTable ( 'User' )
  role = relator.relationalTable ( 'Role' )
