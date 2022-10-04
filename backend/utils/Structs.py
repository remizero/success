# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación


# Preconditions / Precondiciones


class Structs () :
  
  @staticmethod
  def dictToJson ( results ) :
    myJsonList = []
    if results is dict :
      for result in results :
        myJsonList.append ( result [ 0 ] )
    return myJsonList
  
  @staticmethod
  def getJsonKeys ( jsonData ) :
    return jsonData.keys ()
  
  @staticmethod
  def getJsonValues ( jsonData ) :
    return jsonData.values ()
  
  @staticmethod
  def jsonModelSessionLogin ( resultData ) :
    return {
      "username": resultData [ 0 ] [ 'username' ],
      "email": resultData [ 0 ] [ 'email' ],
      "name": resultData [ 0 ] [ 'name' ],
      "lastname": resultData [ 0 ] [ 'lastname' ],
      "group_id": resultData [ 0 ] [ 'group_id' ],
      "loggedin": True
    }
  
  @staticmethod
  def jsonModelSessionLogout ( resultData ) :
    resultData [ 'msg' ] = 'Usuario desconectado correctamente'
    resultData [ 'loggedin' ] = False
    resultData [ 'type' ] = 'normal'
    resultData [ 'status' ] = 200
    return resultData
  
  @staticmethod
  def jsonModelMsgResponse ( msg : str, type : str, status : int ) :
    return {
      'msg' : msg,
      'type' : type, # warning, fatal, error, normal
      'status' : status #200, 401, ...
    }

  @staticmethod
  def jsonInputSchema ( name, label, action, maxLength, required, type, order ) :
    return [
      {
        'name' : name,
        'label' : label,
        'action' : action,
        'htmlType' : 'input',
        'maxLength' : maxLength,
        'required' : required,
        'type' : type,
        'order' : order
      }
    ]

  @staticmethod
  def jsonInputRangeSchema ( name, label, action, maxLength, required, type, min, max, step, order ) :
    return [
      {
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
    ]

  @staticmethod
  def jsonSelectSchema ( name, label, action, maxLength, required, type, order ) :
    return [
      {
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
    ]

  @staticmethod
  def jsonSelectBooleanSchema ( name, label, action, required, order ) :
    return [
      {
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
            "True": "True"
          },
          {
            "False": "False"
          }
        ]
      }
    ]

  @staticmethod
  def jsonTextareaSchema ( name, label, maxLength, required, order ) :
    return [
      {
        'name' : name,
        'label' : label,
        'action' : '',
        'htmlType' : 'textarea',
        'maxLength' : maxLength,
        'required' : required,
        'type' : 'text',
        'order' : order
      }
    ]

  @staticmethod
  def modelResultToJson ( result ) :
    myJsonList = []
    if isinstance ( result, list ) :
      for unitResult in result :
        myJsonList.append ( unitResult.toJson () )
    else :
      myJsonList = result.toJson ()
    return myJsonList
  
  @staticmethod
  def toJson ( result ) :
    return result.fetchone () [ 0 ]
