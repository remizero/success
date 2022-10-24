# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel.Schema import (
  fields,
  pre_load,
  Schema as SuccessSchema,
  ValidationError
)
from app.models import User


# Preconditions / Precondiciones


class Schema ( SuccessSchema ) :

  class Meta :
    model = User

  username = fields.String ( required = True )
  password = fields.String ( required = True )
  email = fields.Email ( required = True )
