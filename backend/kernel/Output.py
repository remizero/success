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
from exceptions import OutputException
from kernel import (
  Logger
)
from . import Schema


# Preconditions / Precondiciones
@unique
class OutputType ( Enum ) :
  ERROR = 1
  EXCEPTION = 2
  LOGIN = 3
  STANDARD = 4
  SUCCESSFUL = 5
  SUCCESS = 6

# TODO reconstruir esta clase
class Output ( ABC ) :

  __output       : dict       = None
  __outputType   : OutputType = None
  __schemaOutput : Schema     = None

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
      self.__schemaOutput = Schema ()
    self.schema = ''
    if ( emptySchema ) :
      self.schema = self.__emptySchema.copy ()
    else :
      self.schema = self.__fullSchema.copy ()
    #raise NotImplementedError ()

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
    if ( ( self.__outputType is not None ) and ( self.__outputType is not OutputType.SUCCESS ) ) :
      self.schema [ 'action' ] = action
    else :
      raise OutputException ()

  def setData ( self, data : list ) -> None :
    if ( ( self.__outputType is not None ) and ( self.__outputType is not OutputType.SUCCESS ) ) :
      self.schema [ 'data' ] = data
    else :
      raise OutputException ()

  def setOptions ( self, attribute : str, options : list ) -> None :
    if ( ( self.__outputType is not None ) and ( self.__outputType is not OutputType.SUCCESS ) ) :
      for model in self.schema [ 'model' ] :
        if model [ 'name' ] == attribute :
          model [ 'options' ] = options
          break
    else :
      raise OutputException ()

  def error ( self, _msg : str, _type : str, _status : int ) -> dict :
    return {
      'error' : _msg,
      'type' : _type, # warning, fatal, error, normal
      'status' : _status #200, 401, ...
    }

  def exception ( self, _msg : str, _type : str, _status : int ) -> dict :
    return self.error ( _msg, _type, _status )

  def standard () -> dict :
    return ''

  def success () -> dict :
    return ''
