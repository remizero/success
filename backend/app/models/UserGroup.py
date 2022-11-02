# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.Model import (
  Fields,
  Model,
  Relations
)


# Preconditions / Precondiciones
relator = Relations ( 'UserGroup' )


class UserGroup ( Model ) :

  # Model Specific Attributes / Atributos específicos del modelo
  user_id = Fields.db_foreign_key ( 'User' )
  group_id = Fields.db_foreign_key ( 'Group' )

  # Related tables / Tablas relacionadas
  user = relator.relationalTable ( 'User' )
  group = relator.relationalTable ( 'Group' )
