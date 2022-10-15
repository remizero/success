# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel import Model
from utils import (
  Fields,
  Relations
)


# Preconditions / Precondiciones
relator = Relations ( 'Group' )


class Group ( Model ) :

  # Model Specific Attributes / Atributos específicos del modelo
  name = Fields.db_string ( 50 )

  # Related tables / Tablas relacionadas
  users = relator.manyToMany ( 'User', 'UserGroup' )
