# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from . import Logger


# Preconditions / Precondiciones


class Schema () :

  @staticmethod
  def input ( name, label, action, maxLength, required, type, order ) :
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
  def inputRange ( name, label, action, maxLength, required, type, min, max, step, order ) :
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
  def select ( name, label, action, maxLength, required, type, order ) :
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
  def selectBoolean ( name, label, action, required, order ) :
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
          "True": "True"
        },
        {
          "False": "False"
        }
      ]
    }

  @staticmethod
  def textarea ( name, label, maxLength, required, order ) :
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
