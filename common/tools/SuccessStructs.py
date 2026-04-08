# Python Libraries / Librerías Python
from copy import deepcopy

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessStructs () :
  
  @staticmethod
  def session () -> dict :
    struct = {
      'id'       : '',
      'username' : '',
      'group_id' : '',
      'role_id'  : '',
      'token'    : ''
    }
    return struct.copy ()
  
  @staticmethod
  def signin () -> dict :
    struct = {
      'username' : '',
      'fullname' : '',
      'token'    : '',
      'loggedin' : '',
      'type'     : '',
      'status'   : ''
    }
    return struct.copy ()
  
  @staticmethod
  def signout () -> dict :
    struct = {
      'msg'      : '',
      'loggedin' : '',
      'type'     : '',
      'status'   : ''
    }
    return struct.copy ()

  @staticmethod
  def booleanOptions () :
    return [
      {
        'True'  : True
      },
      {
        'False' : False
      }
    ]

  @staticmethod
  def successOutputEmptySchema () -> dict :
    emptySchema = {
      'action' : '',
      'data'   : list (),
      'model'  : list ()
    }
    return emptySchema.copy ()

  @staticmethod
  def successBaseOutput () -> dict :
    schemaList = list ()
    schemaList.append ( SuccessStructs.jsonInputSchema ( 'id', 'ID', '', 'input', '', 'False', 1 ) )
    schemaList.append ( SuccessStructs.jsonSelectBooleanSchema ( 'enabled', 'Habilitado', '', 'False', 2 ) )
    schemaList.append ( SuccessStructs.jsonInputSchema ( 'created_at', 'Creado en', '', 'input', 'True', 'datetime-local', 3 ) )
    schemaList.append ( SuccessStructs.jsonInputSchema ( 'updated_at', 'Actualizado en', '', 'input', 'False', 'datetime-local', 4 ) )
    schemaList.append ( SuccessStructs.jsonSelectBooleanSchema ( 'deleted', 'Eliminado', '', 'False', 5 ) )
    fullSchema = {
      'action' : '',
      'data'   : [],
      'model'  : [
        {
          'name'      : 'id',
          'label'     : 'ID',
          'action'    : '',
          'htmlType'  : 'input',
          'maxLength' : '0',
          'required'  : 'False',
          'type'      : 'number'
        },
        {
          'name'      : 'enabled',
          'label'     : 'Habilitado',
          'action'    : '',
          'htmlType'  : 'select',
          'maxLength' : 'None',
          'required'  : 'False',
          'type'      : 'boolean',
          'options'   : [
            {
              'True'  : 'True'
            },
            {
              'False' : 'False'
            }
          ]
        },
        {
          'name'      : 'created_at',
          'label'     : 'Creado en',
          'action'    : '',
          'htmlType'  : 'input',
          'maxLength' : 'None',
          'required'  : 'True',
          'type'      : 'datetime-local'
        },
        {
          'name'      : 'updated_at',
          'label'     : 'Actualizado en',
          'action'    : '',
          'htmlType'  : 'input',
          'maxLength' : 'None',
          'required'  : 'True',
          'type'      : 'datetime-local'
        },
        {
          'name'      : 'deleted',
          'label'     : 'Eliminado',
          'action'    : '',
          'htmlType'  : 'select',
          'maxLength' : 'None',
          'required'  : 'False',
          'type'      : 'boolean',
          'options'   : [
            {
              'True'  : 'True'
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
  def jsonModelMsgResponse ( msg : str, type : str, status : int ) -> dict :
    return {
      'msg'    : msg,
      'type'   : type, # warning, fatal, error, normal
      'status' : status #200, 401, ...
    }

  @staticmethod
  def jsonInputSchema ( name, label, action, maxLength, required, type, order ) -> dict :
    return {
      'name'      : name,
      'label'     : label,
      'action'    : action,
      'htmlType'  : 'input',
      'maxLength' : maxLength,
      'required'  : required,
      'type'      : type,
      'order'     : order
    }

  @staticmethod
  def jsonInputRangeSchema ( name, label, action, maxLength, required, type, min, max, step, order ) -> dict :
    return {
      'name'      : name,
      'label'     : label,
      'action'    : action,
      'htmlType'  : 'input',
      'maxLength' : maxLength,
      'required'  : required,
      'type'      : type,
      'order'     : order,
      'min'       : min,
      'max'       : max,
      'step'      : step
    }

  @staticmethod
  def jsonSelectSchema ( name, label, action, maxLength, required, type, order ) -> dict :
    return {
      'name'      : name,
      'label'     : label,
      'action'    : action,
      'htmlType'  : 'select',
      'maxLength' : maxLength,
      'required'  : required,
      'type'      : type,
      'order'     : order,
      'options'   : []
    }

  @staticmethod
  def jsonSelectBooleanSchema ( name, label, action, required, order ) -> dict :
    return {
      'name'      : name,
      'label'     : label,
      'action'    : action,
      'htmlType'  : 'select',
      'maxLength' : '',
      'required'  : required,
      'type'      : 'boolean',
      'order'     : order,
      'options'   : [
        {
          'True'  : 'True'
        },
        {
          'False' : 'False'
        }
      ]
    }

  @staticmethod
  def jsonTextareaSchema ( name, label, maxLength, required, order ) -> dict :
    return {
      'name'      : name,
      'label'     : label,
      'action'    : '',
      'htmlType'  : 'textarea',
      'maxLength' : maxLength,
      'required'  : required,
      'type'      : 'text',
      'order'     : order
    }


  @staticmethod
  def redirect ( enabled : bool, target : str, context : dict ) -> dict :
    redirect = { "enabled" : enabled, "target" : target, "context" : context or {} }
    return deepcopy ( redirect )


  @staticmethod
  def render ( enabled : bool, template : str, context : dict ) -> dict :
    render = { "enabled" : enabled, "template" : template, "context" : { "context": context or {} } }
    return deepcopy ( render )


  @staticmethod
  def successContextApp ( appName : str ) -> dict :
    context = {
      appName : {
        "config"     : None,
        "instance"   : None,
        "module"     : None,
        "logger"     : None,
        "extensions" : {},
        "breadcrumb" : {
          "current" : "",
          "scope"   : ""
        }
      }
    }
    return deepcopy ( context )


  @staticmethod
  def successContextFramework () -> dict :
    context = {
      "config"  : None,
      "success" : {
        "apps" : {},
      }
    }
    return context.copy ()
