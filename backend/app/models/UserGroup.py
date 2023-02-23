# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts       import Model
from kernel.abstracts.Model import Fields
from kernel.abstracts.Model import Relations


# Preconditions / Precondiciones
relator = Relations ( 'UserGroup' )


class UserGroup ( Model ) :

  # Model Specific Attributes / Atributos específicos del modelo
  user_id  = Fields.foreignKey ( 'User', primaryKey = True )
  group_id = Fields.foreignKey ( 'Group', primaryKey = True )

  # Related tables / Tablas relacionadas
  group = relator.relationalTable ( 'Group' )
  user  = relator.relationalTable ( 'User' )
