# Python Libraries / Librerías Python
from marshmallow import fields
from marshmallow import pre_load
from marshmallow import ValidationError

# Application Libraries / Librerías de la Aplicación
# from success.core.SuccessContext        import SuccessContext
from success.engine.models.SuccessModel                        import SuccessModel
from success.engine.extensions.proxies.SuccessProxyMarshmallow import mm as marshmallow

# Preconditions / Precondiciones
# marshmallow = SuccessContext ().getExtension ( "SuccessMarshmallowExtension" )
# if marshmallow is None :
#   raise RuntimeError ( "La extensión SuccessMarshmallowExtension no está cargada" )


class SuccessSchema ( marshmallow.SQLAlchemySchema ) :
  """
  Base schema for model serialization and validation.

  Extends marshmallow SQLAlchemy schema with standard fields
  for all Success models.

  Meta:
    model: Associated SQLAlchemy model (SuccessModel).

  Attributes:
    id: Integer field (dump only).
    enabled: Boolean field (required).
    created_at: DateTime field (required).
    updated_at: DateTime field.
    deleted: Boolean field (required).
  """

  class Meta :
    model = SuccessModel


  id         = fields.Integer ( dump_only = True )
  enabled    = fields.Boolean ( required = True )
  created_at = fields.DateTime ( required = True )
  updated_at = fields.DateTime ()
  deleted    = fields.Boolean ( required = True )
