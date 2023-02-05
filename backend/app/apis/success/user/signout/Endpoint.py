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
  Response,
  Encryption,
  Http,
  Resultset,
  Structs
)
from exceptions import (
  JsonRequestException,
  OutputException
)
from kernel import (
  Debug,
  Logger
)
from app.models import User
#from utils.Structs import Structs
# from utils import (
#   Encryption,
#   Http,
#   Resultset,
#   Structs
# )


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
      userObj = user.findByFilters ( False, **inputData )
      result = Resultset.toJson ( userObj )
      self.responseData = output.data ( result [ 0 ] )
      self.statusResponse = HTTPStatus.OK
      '''
        HASTA AQUI TODO BIEN
        1-. AJUSTAR EL OUTPUT A LA DATA QUE DEBE RETORNAR
            EL OUTPUT DEBE SER UNA ESTRUCTURA COMO LA QUE UTILIZO EN CORE
            COMO ESTABLECER LOS ARCHIVOS INPUT/OUTPUT COMO ME GUSTARIA DEFINIR
        2-. CARGAR LA DATA RESPECTIVA A LA SESSION
        3-. CREAR EL JWT
      '''

    except ( 
      JsonRequestException,
      OutputException,
      ValidationError,
      SchemaError
    ) as exception :

      self.logger.log ( exception )
      self.responseData = output.exception ( self.logger.toShow (), 'CRITICAL', HTTPStatus.BAD_REQUEST )

    except :

      self.logger.uncatchErrorException ()
      self.responseData = output.exception ( self.logger.toShow (), 'CRITICAL', HTTPStatus.BAD_REQUEST )

    response = Http.returnResponse ( self.responseData, self.statusResponse )
    # if self.statusResponse == HTTPStatus.OK :
    #   JsonWebToken.create ( response )
    return response
