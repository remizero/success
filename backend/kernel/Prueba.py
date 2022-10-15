# Python Libraries / Librerías Python
from flask_marshmallow import Schema


# Application Libraries / Librerías de la Aplicación
from kernel import Logger


# Preconditions / Precondiciones


class Validator ( Schema ) :

  logger : Logger = None
  schema = {
    'type' : 'object',
    'properties' : {},
    'required' : [],
    'additionalProperties' : False
  }

  @abstractmethod
  def __init__ ( self, withId : bool = False, additionalProperties : bool = False ) -> None :
    self.logger = Logger ( __name__ )
    #self.schema = ''
    if ( withId ) :
      self.schema [ 'required' ].append ( 'id' )
    if ( additionalProperties ) :
      self.schema [ 'additionalProperties' ] = additionalProperties

  def validate ( self, data ) -> bool :
    validate ( data, self.schema )
    return True
