# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.abstracts        import Schema
from kernel.abstracts.Schema import fields
from kernel.abstracts.Schema import pre_load
from kernel.abstracts.Schema import ValidationError
from app.models              import User


# Preconditions / Precondiciones


class Input ( Schema ) :

  class Meta :
    model = User

  username = fields.String ( required = True )
  password = fields.String ( required = True )
  email    = fields.Email  ( required = True )
