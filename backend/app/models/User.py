# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel import Model
from utils import (
  Fields,
  Relations
)


# Preconditions / Precondiciones
relator = Relations ( 'User' )


class User ( Model ) :

  # Model Specific Attributes / Atributos específicos del modelo
  username = Fields.db_string ( 50 )
  password = Fields.db_string ( 255 )
  email = Fields.db_string ( 50 )

  # Related tables / Tablas relacionadas
  groups = relator.manyToMany ( 'Group', 'UserGroup' )
  roles = relator.manyToMany ( 'Role', 'UserRole' )
