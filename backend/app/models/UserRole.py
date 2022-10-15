# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel import Model
from utils import (
  Fields,
  Relations
)


# Preconditions / Precondiciones
relator = Relations ( 'UserRole' )


class UserRole ( Model ) :

  # Model Specific Attributes / Atributos específicos del modelo
  user_id = Fields.db_foreign_key ( 'User' )
  role_id = Fields.db_foreign_key ( 'Role' )

  # Related tables / Tablas relacionadas
  user = relator.relationalTable ( 'User' )
  role = relator.relationalTable ( 'Role' )
