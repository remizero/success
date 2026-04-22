# Python Libraries / Librerías Python
from marshmallow import INCLUDE
from marshmallow import Schema as MarshmallowSchema

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class Schema ( MarshmallowSchema ) :

  class Meta :
    unknown = INCLUDE
