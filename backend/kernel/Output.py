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
from ..common import Schema


# Preconditions / Precondiciones
@unique
class OutputType ( Enum ) :
  ERROR = 1
  EXCEPTION = 2
  STANDARD = 3
  SUCCESS = 4


class Output ( ABC ) :

  __output : dict = None
  __schemaOutput : Schema = None


  schema = dict ()
  
  __emptySchema = {
    'action' : '',
    'data' : [],
    'formModel' : []
  }

  __fullSchema = {
    'action' : '',
    'data' : [],
    'model' : [
      {
        'name' : 'id',
        'label' : 'ID',
        'action' : '',
        'htmlType' : 'input',
        'maxLength' : '0',
        'required' : 'False',
        'type' : 'number'
      },
      {
        'name' : 'enabled',
        'label' : 'Habilitado',
        'action' : '',
        'htmlType' : 'select',
        'maxLength' : 'None',
        'required' : 'False',
        'type' : 'boolean',
        'options' : [
          {
            "True": "True"
          },
          {
            "False": "False"
          }
        ]
      },
      {
        'name' : 'created_at',
        'label' : 'Creado en',
        'action' : '',
        'htmlType' : 'input',
        'maxLength' : 'None',
        'required' : 'True',
        'type' : 'datetime-local'
      },
      {
        'name' : 'updated_at',
        'label' : 'Actualizado en',
        'action' : '',
        'htmlType' : 'input',
        'maxLength' : 'None',
        'required' : 'True',
        'type' : 'datetime-local'
      },
      {
        'name' : 'deleted',
        'label' : 'Eliminado',
        'action' : '',
        'htmlType' : 'select',
        'maxLength' : 'None',
        'required' : 'False',
        'type' : 'boolean',
        'options' : [
          {
            "True": "True"
          },
          {
            "False": "False"
          }
        ]
      }
    ]
  }

  @abstractmethod
  def __init__ ( self, outputType : OutputType = OutputType.SUCCESS, emptySchema : bool = True ) -> None :
    self.logger = Logger ( __name__ )
    if ( outputType == OutputType.SUCCESS ) :
      self.__schemaOutput = Schema ( emptySchema )
    self.schema = ''
    if ( emptySchema ) :
      self.schema = self.__emptySchema.copy ()
    else :
      self.schema = self.__fullSchema.copy ()
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

  def getSchema ( self ) -> dict :
    return self.schema

  def getEmptySchema ( self ) -> dict :
    return self.__emptySchema

  def getFullSchema ( self ) -> dict :
    return self.__fullSchema

  def setAction ( self, action : str ) -> None :
    self.schema [ 'action' ] = action

  def setData ( self, data : list ) -> None :
    self.schema [ 'data' ] = data

  def setOptions ( self, attribute : str, options : list ) -> None :
    for model in self.schema [ 'model' ] :
      if model [ 'name' ] == attribute :
        model [ 'options' ] = options
        break
