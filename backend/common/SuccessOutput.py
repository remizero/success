# Python Libraries / Librerías Python
from abc import (
  ABC,
  abstractmethod
)
from enum import (
  Enum,
  unique
)


# Application Libraries / Librerías de la Aplicación
from kernel import (
  Logger
)
from . import Schema


# Preconditions / Precondiciones
@unique
class OutputType ( Enum ) :
  ERROR = 1
  EXCEPTION = 2
  STANDARD = 3
  SUCCESS = 4


class SuccessOutput ( ABC ) :

  __output : dict = None
  __schemaOutput : Schema = None

  @abstractmethod
  def __init__ ( self, outputType : OutputType = OutputType.SUCCESS, emptySchema : bool = True ) -> None :
    self.logger = Logger ( __name__ )
    if ( outputType == OutputType.SUCCESS ) :
      self.__schemaOutput = Schema ( emptySchema )
    raise NotImplementedError ()

  def getOutput ( self ) -> dict :
    return self.__output

  # passasdf = {
  #   "username": resultData [ 0 ] [ 'username' ],
  #   "email": resultData [ 0 ] [ 'email' ],
  #   "name": resultData [ 0 ] [ 'name' ],
  #   "lastname": resultData [ 0 ] [ 'lastname' ],
  #   "group_id": resultData [ 0 ] [ 'group_id' ],
  #   "loggedin": True
  # }
