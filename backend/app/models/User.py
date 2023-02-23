# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts       import Model
from kernel.abstracts.Model import Fields
from kernel.abstracts.Model import Relations


# Preconditions / Precondiciones
relator = Relations ( 'User' )


class User ( Model ) :

  # Model Specific Attributes / Atributos específicos del modelo
  username = Fields.string ( 50 )
  password = Fields.string ( 255 )
  email    = Fields.string ( 50 )

  # Related tables / Tablas relacionadas
  groups   = relator.manyToMany ( 'Group', 'UserGroup' )
  profiles = relator.manyToMany ( 'Profile', 'UserProfile' )
  roles    = relator.manyToMany ( 'Role', 'UserRole' )
