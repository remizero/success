# Python Libraries / Librerías Python
from sqlalchemy.ext.declarative import declared_attr

# Success Libraries / Librerías Success
from success.engine.models.SuccessBaseModel import SuccessBaseModel
from success.core.SuccessContext            import SuccessContext
from success.engine.models.SuccessFields           import SuccessFields
from success.engine.models.SuccessRelations        import SuccessRelations
from success.common.tools.SuccessDatetime          import SuccessDatetime

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessModel ( SuccessBaseModel ) :

  enabled    = SuccessFields.boolean    ()
  created_at = SuccessFields.datetime   ( default = SuccessDatetime.getNow () )
  updated_at = SuccessFields.datetime   ( nullable = True, default = None )
  deleted    = SuccessFields.boolean    ()
