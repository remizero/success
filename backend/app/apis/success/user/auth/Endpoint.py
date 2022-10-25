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
from .Input import Input
from .Output import Output
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
input = Input ( only = ( 'username', 'password' ) )
output = Output ()


class Endpoint ( SuccessEndpoint ) :

  def post ( self ) -> Response :
    
    try :

      Http.requestIsJson ()
      inputData = input.load ( request.get_json () )
      user = User ()
      inputData [ 'password' ] = Encryption.password ( inputData [ 'password' ] )
      Debug.log ( inputData [ 'password' ] )
      userObj = user.findByFilters ( False, **inputData )
      Debug.log ( userObj.username )
      '''
        HASTA AQUI TODO BIEN
        1-. AJUSTAR EL OUTPUT A LA DATA QUE DEBE RETORNAR
            EL OUTPUT DEBE SER UNA ESTRUCTURA COMO LA QUE UTILIZO EN CORE
            COMO ESTABLECER LOS ARCHIVOS INPUT/OUTPUT COMO ME GUSTARIA DEFINIR
        2-. CARGAR LA DATA RESPECTIVA A LA SESSION
        3-. CREAR EL JWT
      '''
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