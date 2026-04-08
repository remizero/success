# Python Libraries / Librerías Python
from marshmallow import fields
from marshmallow import pre_load
from marshmallow import ValidationError

# Application Libraries / Librerías de la Aplicación
from success.core.SuccessContext        import SuccessContext
from success.engine.models.SuccessModel import SuccessModel

# Preconditions / Precondiciones
marshmallow = SuccessContext ().getExtension ( "SuccessMarshmallowExtension" )
if marshmallow is None :
  raise RuntimeError ( "La extensión SuccessMarshmallowExtension no está cargada" )


class SuccessSchema ( marshmallow._extension.SQLAlchemySchema ) :

  class Meta :
    model = SuccessModel


  id         = fields.Integer ( dump_only = True )
  enabled    = fields.Boolean ( required = True )
  created_at = fields.DateTime ( required = True )
  updated_at = fields.DateTime ()
  deleted    = fields.Boolean ( required = True )
