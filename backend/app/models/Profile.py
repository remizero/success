# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts       import Model
from kernel.abstracts.Model import Fields
from kernel.abstracts.Model import Relations


# Preconditions / Precondiciones
relator = Relations ( 'Profile' )


class Profile ( Model ) :

  # Model Specific Attributes / Atributos específicos del modelo
  name_first      = Fields.string ( 15 )
  name_second     = Fields.string ( 15 )
  lastname_first  = Fields.string ( 15 )
  lastname_second = Fields.string ( 15 )

  # Related tables / Tablas relacionadas
  users = relator.manyToMany ( 'User', 'UserProfile' )
