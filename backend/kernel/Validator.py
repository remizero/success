# Python Libraries / Librerías Python
from jsonschema import validate

# Application Libraries / Librerías de la Aplicación
from . import Logger


# Preconditions / Precondiciones


class Validator () :

  schema = ""

  def __init__ ( self ) :
    self.schema = ""

  def validate ( self, data ) -> bool :
    validate ( data, self.schema )
    return True