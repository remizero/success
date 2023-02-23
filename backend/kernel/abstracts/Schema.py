# Python Libraries / Librerías Python
from marshmallow import fields
from marshmallow import pre_load
from marshmallow import ValidationError


# Application Libraries / Librerías de la Aplicación
from extensions       import marshmallow
from kernel.abstracts import Model


# Preconditions / Precondiciones


class Schema ( marshmallow.extension.SQLAlchemySchema ) :

  class Meta :
    model = Model

  id         = fields.Integer ( dump_only = True )
  enabled    = fields.Boolean ( required = True )
  created_at = fields.DateTime ( required = True )
  updated_at = fields.DateTime ()
  deleted    = fields.Boolean ( required = True )
