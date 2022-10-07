# Python Libraries / Librerías Python
from flask import (
  json,
  request,
  session,
  Response
)
from flask_restful import Resource
from http import HTTPStatus
from jsonschema.exceptions import (
  ValidationError,
  SchemaError
)


# Application Libraries / Librerías de la Aplicación
from exceptions import (
  JsonRequestException,
  RequestMethodException
)
from extensions import Logger
from kernel import Debug
from app.models import User
#from utils.Structs import Structs

from . import Validator
from utils import (
  Encryption,
  Http,
  Structs
)


# Preconditions / Precondiciones


class Signin ( Resource ) :

  def post ( self ) :
    Debug.log ( 'ESTA ENTRANDO' )
    #logger = Logger ( __name__ )
    responseData = ''
    statusResponse = HTTPStatus.BAD_REQUEST
    try :
      Http.isPost ()
      Http.requestIsJson ()
      validator = Validator ()
      validator.validate ( request.get_json () )

      user = User ()
      # request.json [ 'password' ] = Encryption.passToHash ( request.json [ 'password' ] )
      jsonResult = Structs.modelResultToJson ( user.findByFilters ( **request.get_json () ) )
      responseData = Structs.jsonModelSessionLogin ( jsonResult )
      statusResponse = HTTPStatus.OK
    except ( 
      RequestMethodException, 
      JsonRequestException,
      ValidationError,
      SchemaError
    ) as exception :
      responseData = { "msg" : exception.getMessage () }
      #logger.log ( exception )
    except :
      responseData = Structs.jsonModelMsgResponse ( 'Error no identificado, comunicarse inmediatamente con el administrador del sistema.', 'Fatal', statusResponse )
      #logger.uncatchErrorException ()
    response = Http.returnResponse ( responseData, statusResponse )
    # if statusResponse == HTTPStatus.OK :
    #   JsonWebToken.create ( response )
    return response
