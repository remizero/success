# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
#from kernel import Logger
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

  # para radio, checkbox colocar 'options' : []
  # min y max pueden ser usados en los formType date, number, 
  # TODO acer uso de estos enlaces
  # https://medium.com/swlh/3-alternatives-to-if-statements-to-make-your-python-code-more-readable-91a9991fb353
  # https://skonik.me/python-alternatives-to-if-elif-statements-before-python-3-10/
  # https://www.w3schools.com/html/html_form_input_types.asp
  # utilizar hidden para los id y como encriptarlos aunque sea con base64
  # pattern = "[0-9]{4}-[0-9]{3}.[0-9]{2}.[0-9]{2}" para telefonos

  @staticmethod
  def __baseElement ( name : str,
                     label : str,
                     order : int,
                  formType : FormType = FormType.input.name,
                      type : str = 'string',
                  required : bool = True,
                  readonly : bool = False,
                    action : str = None,
                 inputType : InputType = InputType.text.name,
                 maxLength : int = 255,
                       min : int = 0,
                       max : int = 100,
                      step : int = 1,
                   pattern : str = None ) :
    element = {
      'name' : name,
      'label' : label,
      'action' : action,
      'formType' : formType,
      'required' : required,
      'type' : type,
      'order' : order
    }
    if ( ( formType.name == 'input' ) and ( inputType is not None ) ) :
      element [ 'inputType' ] = inputType.name
      if ( ( inputType.name == 'text' ) and ( maxLength is not None ) ) :
        element [ 'maxLength' ] = maxLength
    else :
      element [ 'inputType' ] = 'text'
    return element.copy ()

  @staticmethod
  def input ( name : str, label : str, action : str, maxLength : int, required : bool, type : str, order : int ) :
    return Schemas.__baseElement ( name, label, action, FormType.input, maxLength, required, type, order )

  @staticmethod
  def inputRange ( name : str, label : str, action : str, maxLength : int, required : bool, type : str, min, max, step, order : int ) :
    return {
      'name' : name,
      'label' : label,
      'action' : action,
      'formType' : 'input',
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
      'formType' : 'select',
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
      'formType' : 'select',
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
      'formType' : 'textarea',
      'maxLength' : maxLength,
      'required' : required,
      'type' : 'text',
      'order' : order
    }
