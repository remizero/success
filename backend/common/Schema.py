# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel import Logger


# Preconditions / Precondiciones


class Schema () :

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

  def __init__ ( self, emptySchema : bool = True ) -> None :
    self.schema = ''
    if ( emptySchema ) :
      self.schema = self.__emptySchema.copy ()
    else :
      self.schema = self.__fullSchema.copy ()

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
