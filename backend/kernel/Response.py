# Python Libraries / Librerías Python
from flask import (
  json,
  request,
  session,
  Response as FlaskResponse
)
from http import HTTPStatus


# Application Libraries / Librerías de la Aplicación


# Preconditions / Precondiciones
# https://blog.miguelgrinberg.com/post/customizing-the-flask-response-class
# https://www.youtube.com/watch?v=gh2HPmpFjn8
# https://github.com/pallets/flask/issues/3294
# https://tedboy.github.io/flask/generated/generated/flask.Response.html
# TODO AGREGAR UN METODO QUE GENERE UNA RESPUESTA ESTANDAR

class Response ( FlaskResponse ) :

  baseSchema = {
    'action' : '',
    'formModel' : [],
    'data' : []
  }

  baseSchemaAux = {
    'action' : '',
    'formModel' : [
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
    ],
    'data' : []
  }

  response = FlaskResponse ()

  def __init__ ( self ) :
    self.default_mimetype = 'application/json'
    self.default_status = HTTPStatus.OK
    self.charset = 'utf-8'

  def respuesta ( self ) :
    #self.response.
    return {
      'data' : [],
      'status' : '',
      'code' : '',

    }

  @staticmethod
  def response ( responseData, statusResponse ) :
    return Response (
      response = json.dumps ( responseData ),
      status = statusResponse,
      mimetype = 'application/json'
    )
