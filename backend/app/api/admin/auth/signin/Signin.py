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
from kernel import session
from models import User
from utils.Structs import Structs

from signin import Validator
from utils import (
  Encryption,
  Http
)


# Preconditions / Precondiciones


class Signin ( Resource ) :

  def __init__ ( self ) :
    pass

  def post ( self ) :
    logger = Logger ( __name__ )
    responseData = ''
    statusResponse = HTTPStatus.BAD_REQUEST
    try :
      Http.isPost ()
      Http.requestIsJson ()
      validator = Validator ()
      validator.validate ( request.get_json () )

      user = User ()
      request.json [ 'password' ] = Encryption.passToHash ( request.json [ 'password' ] )
      jsonResult = Structs.modelResultToJson ( user.findByFilters ( **request.get_json () ) )
      applicationUser = ApplicationUser ()
      applicationUserList = applicationUser.findByFilters ( user_id = int ( jsonResult [ 0 ] [ 'id' ] ) )
      jsonList = []
      for applicationUserObj in applicationUserList :
        jsonAux = {
          'app' : '',
          'action' : '',
          'target' : ''
        }
        application = Application ( id = int ( applicationUserObj.app_id ) )
        applicationyObj = application.findById ()
        jsonAux [ 'app' ] = applicationyObj.name
        jsonAux [ 'action' ] = applicationyObj.link
        jsonAux [ 'target' ] = applicationyObj.is_blank
        jsonList.append ( jsonAux )
      responseData = Structs.jsonModelSessionLogin ( jsonResult )
      responseData [ 'apps' ] = jsonList
      statusResponse = HTTPStatus.OK
    except ( 
      RequestMethodException, 
      JsonRequestException,
      ValidationError,
      SchemaError
    ) as exception :
      responseData = { "msg" : exception.getMessage () }
      logger.log ( exception )
    except :
      responseData = Structs.jsonModelMsgResponse ( 'Error no identificado, comunicarse inmediatamente con el administrador del sistema.', 'Fatal', statusResponse )
      logger.uncatchErrorException ()
    response = Http.returnResponse ( responseData, statusResponse )
    if statusResponse == HTTPStatus.OK :
      JsonWebToken.create ( response )
    return response
