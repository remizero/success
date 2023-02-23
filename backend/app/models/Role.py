# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts       import Model
from kernel.abstracts.Model import Fields
from kernel.abstracts.Model import Relations


# Preconditions / Precondiciones
relator = Relations ( 'Role' )


class Role ( Model ) :

  # Model Specific Attributes / Atributos específicos del modelo
  name = Fields.string ( 50 )

  # Related tables / Tablas relacionadas
  users = relator.manyToMany ( 'User', 'UserRole' )
