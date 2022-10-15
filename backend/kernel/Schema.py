# Python Libraries / Librerías Python
from marshmallow import (
  fields,
  pre_load,
  ValidationError
)


# Application Libraries / Librerías de la Aplicación
from extensions import marshmallow
from . import Model


# Preconditions / Precondiciones


class Schema ( marshmallow.extension.SQLAlchemySchema ) :

  class Meta :
    model = Model

  id = fields.Integer ( dump_only = True )
  enabled = fields.Boolean ( required = True )
  created_at = fields.DateTime ( required = True )
  updated_at = fields.DateTime ()
  deleted = fields.Boolean ( required = True )
