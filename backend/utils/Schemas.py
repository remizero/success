# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from . import Logger
from enum import (
  Enum,
  unique
)


# Preconditions / Precondiciones
@unique
class InputType ( Enum ) :
  button = 1
  checkbox = 2
  color = 3
  date = 4
  datetime = 5
  email = 6
  file = 7
  hidden = 8
  image = 9
  month = 10
  number = 11
  password = 12
  radio = 13
  range = 14
  reset = 15
  search = 16
  submit = 17
  tel = 18
  text = 19
  time = 20
  url = 21
  week = 22

@unique
class FormType ( Enum ) :
  datalist = 1
  input = 2
  select = 3
  texarea = 4


class Schemas () :

  @staticmethod
  def __baseElement ( name : str, label : str, action : str, htmlType : str, maxLength : int, required : bool, type : str, order : int ) :
    element = {
      'name' : name,
      'label' : label,
      'action' : action,
      'htmlType' : htmlType,
      'maxLength' : maxLength,
      'required' : required,
      'type' : type,
      'order' : order
    }
    return element.copy ()

  @staticmethod
  def input ( name : str, label : str, action : str, maxLength : int, required : bool, type : str, order : int ) :
    return Schemas.__baseElement ( name, label, action, FormType.input.name, maxLength, required, type, order )

  @staticmethod
  def inputRange ( name : str, label : str, action : str, maxLength : int, required : bool, type : str, min, max, step, order : int ) :
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
  def select ( name : str, label : str, action : str, maxLength : int, required : bool, type : str, order : int ) :
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
  def selectBoolean ( name : str, label : str, action : str, required : bool, order : int ) :
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
  def textarea ( name : str, label : str, maxLength : int, required : bool, order : int ) :
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
