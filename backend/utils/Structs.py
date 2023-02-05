# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación


# Preconditions / Precondiciones


class Structs () :
  
  @staticmethod
  def session () :
    struct = {
      'id' : '',
      'username' : '',
      'group_id' : '',
      'role_id' : '',
      'token' : ''
    }
    return struct.copy ()
  
  @staticmethod
  def signin () :
    struct = {
      'username' : '',
      'fullname' : '',
      'token' : '',
      'loggedin' : '',
      'type' : '',
      'status' : ''
    }
    return struct.copy ()
  
  @staticmethod
  def signout () :
    struct = {
      'msg' : '',
      'loggedin' : '',
      'type' : '',
      'status' : ''
    }
    return struct.copy ()

  @staticmethod
  def booleanOptions () :
    return [
      {
        'True' : True
      },
      {
        'False' : False
      }
    ]

  @staticmethod
  def successOutputEmptySchema () :
    emptySchema = {
      'action' : '',
      'data' : list (),
      'model' : list ()
    }
    return emptySchema.copy ()

  @staticmethod
  def successBaseOutput () :
    schemaList = list ()
    schemaList.append ( Structs.jsonInputSchema ( 'id', 'ID', '', 'input', '', 'False', 1 ) )
    schemaList.append ( Structs.jsonSelectBooleanSchema ( 'enabled', 'Habilitado', '', 'False', 2 ) )
    schemaList.append ( Structs.jsonInputSchema ( 'created_at', 'Creado en', '', 'input', 'True', 'datetime-local', 3 ) )
    schemaList.append ( Structs.jsonInputSchema ( 'updated_at', 'Actualizado en', '', 'input', 'False', 'datetime-local', 4 ) )
    schemaList.append ( Structs.jsonSelectBooleanSchema ( 'deleted', 'Eliminado', '', 'False', 5 ) )
    fullSchema = {
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
              'True' : 'True'
            },
            {
              'False' : 'False'
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
              'True' : 'True'
            },
            {
              'False' : 'False'
            }
          ]
        }
      ]
    }
    return schemaList.copy ()
  
  @staticmethod
  def getJsonKeys ( jsonData ) :
    return jsonData.keys ()
  
  @staticmethod
  def getJsonValues ( jsonData ) :
    return jsonData.values ()
  
  @staticmethod
  def jsonModelMsgResponse ( msg : str, type : str, status : int ) :
    return {
      'msg' : msg,
      'type' : type, # warning, fatal, error, normal
      'status' : status #200, 401, ...
    }

  @staticmethod
  def jsonInputSchema ( name, label, action, maxLength, required, type, order ) :
    return {
      'name' : name,
      'label' : label,
      'action' : action,
      'htmlType' : 'input',
      'maxLength' : maxLength,
      'required' : required,
      'type' : type,
      'order' : order
    }

  @staticmethod
  def jsonInputRangeSchema ( name, label, action, maxLength, required, type, min, max, step, order ) :
    return {
      'name' : name,
      'label' : label,
      'action' : action,
      'htmlType' : 'input',
      'maxLength' : maxLength,
      'required' : required,
      'type' : type,
      'order' : order,
      'min' : min,
      'max' : max,
      'step' : step
    }

  @staticmethod
  def jsonSelectSchema ( name, label, action, maxLength, required, type, order ) :
    return {
      'name' : name,
      'label' : label,
      'action' : action,
      'htmlType' : 'select',
      'maxLength' : maxLength,
      'required' : required,
      'type' : type,
      'order' : order,
      'options' : []
    }

  @staticmethod
  def jsonSelectBooleanSchema ( name, label, action, required, order ) :
    return {
      'name' : name,
      'label' : label,
      'action' : action,
      'htmlType' : 'select',
      'maxLength' : '',
      'required' : required,
      'type' : 'boolean',
      'order' : order,
      'options' : [
        {
          'True' : 'True'
        },
        {
          'False' : 'False'
        }
      ]
    }

  @staticmethod
  def jsonTextareaSchema ( name, label, maxLength, required, order ) :
    return {
      'name' : name,
      'label' : label,
      'action' : '',
      'htmlType' : 'textarea',
      'maxLength' : maxLength,
      'required' : required,
      'type' : 'text',
      'order' : order
    }
