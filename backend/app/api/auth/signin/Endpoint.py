# Python Libraries / Librerías Python
from flask import (
  json,
  request,
  session
)
from jsonschema.exceptions import (
  ValidationError,
  SchemaError
)


# Application Libraries / Librerías de la Aplicación
from .Schema import Schema
from kernel.Endpoint import (
  Endpoint as SuccessEndpoint,
  HTTPStatus,
  Response
)
from exceptions import JsonRequestException
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


# Preconditions / Precondiciones
input = Schema ( only = ( 'username', 'password' ) )
#output = Schema ()


class Endpoint ( SuccessEndpoint ) :

  def post ( self ) -> Response :
    
    try :

      Http.requestIsJson ()
      inputData = input.load ( request.get_json () )
      user = User ()
      inputData [ 'password' ] = Encryption.password ( inputData [ 'password' ] )
      userObj = user.findByFilters ( False, **inputData )
      Debug.log ( inputData [ 'password' ] )
      '''
        HASTA AQUI TODO BIEN
        AJUSTAR EL OUTPUT A LA DATA QUE DEBE RETORNAR
        CARGAR LA DATA RESPECTIVA A LA SESSION
        CREAR EL JWT
      '''
      Debug.log ( userObj.username )
      jsonResult = Structs.modelResultToJson ( user.findByFilters ( **inputData ) )
      self.responseData = Structs.jsonModelSessionLogin ( jsonResult )
      self.statusResponse = HTTPStatus.OK

    except ( 
      JsonRequestException,
      ValidationError,
      SchemaError
    ) as exception :

      #self.responseData = { "msg" : exception.getMessage () }
      self.logger.log ( exception )

    except :

      self.responseData = Structs.jsonModelMsgResponse ( 'Error no identificado, comunicarse inmediatamente con el administrador del sistema.', 'Fatal', self.statusResponse )
      self.logger.uncatchErrorException ()
    response = Http.returnResponse ( self.responseData, self.statusResponse )
    # if self.statusResponse == HTTPStatus.OK :
    #   JsonWebToken.create ( response )
    return response
