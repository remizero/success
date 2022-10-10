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
#from extensions import Logger
from kernel import (
  Debug,
  Logger
)
from app.models import User
#from utils.Structs import Structs
from utils import (
  Encryption,
  Http,
  Structs
)
from . import Input
from . import Output


# Preconditions / Precondiciones


class Signin ( Resource ) :

  #logger = Logger ( __name__ )

  def post ( self ) -> Response :
    logger = Logger ( __name__ )
    responseData = ''
    statusResponse = HTTPStatus.BAD_REQUEST
    try :
      Http.isPost ()
      Http.requestIsJson ()
      input = Input ()
      input.validate ( request.get_json () )
      user = User ()
      # request.json [ 'password' ] = Encryption.passToHash ( request.json [ 'password' ] )
      '''
        HASTA AQUI TODO BIEN
        AJUSTAR EL OUTPUT A LA DATA QUE DEBE RETORNAR
        CARGAR LA DATA RESPECTIVA A LA SESSION
        CREAR EL JWT
      '''
      jsonResult = Structs.modelResultToJson ( user.findByFilters ( **request.get_json () ) )
      responseData = Structs.jsonModelSessionLogin ( jsonResult )
      statusResponse = HTTPStatus.OK
    except ( 
      RequestMethodException, 
      JsonRequestException,
      ValidationError,
      SchemaError
    ) as exception :
      #responseData = { "msg" : exception.getMessage () }
      logger.log ( exception )
    except :
      responseData = Structs.jsonModelMsgResponse ( 'Error no identificado, comunicarse inmediatamente con el administrador del sistema.', 'Fatal', statusResponse )
      logger.uncatchErrorException ()
    response = Http.returnResponse ( responseData, statusResponse )
    # if statusResponse == HTTPStatus.OK :
    #   JsonWebToken.create ( response )
    return response
