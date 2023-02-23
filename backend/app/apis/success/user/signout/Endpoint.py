# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from app.apis.success.user.signout import Input
from app.apis.success.user.signout import Output
from kernel.abstracts              import Endpoint as SuccessEndpoint
from kernel.abstracts.Endpoint     import Debug
from kernel.abstracts.Endpoint     import Encryption
from kernel.abstracts.Endpoint     import Http
from kernel.abstracts.Endpoint     import HTTPStatus
from kernel.abstracts.Endpoint     import JsonRequestException
from kernel.abstracts.Endpoint     import jwt
from kernel.abstracts.Endpoint     import LoginException
from kernel.abstracts.Endpoint     import OutputException
from kernel.abstracts.Endpoint     import Permissions
from kernel.abstracts.Endpoint     import request
from kernel.abstracts.Endpoint     import Response
from kernel.abstracts.Endpoint     import Resultset
from kernel.abstracts.Endpoint     import Session
from kernel.abstracts.Endpoint     import SchemaError
from kernel.abstracts.Endpoint     import Structs
from kernel.abstracts.Endpoint     import ValidationError
from app.models                    import User
from app.models                    import UserGroup
from app.models                    import Group


# Preconditions / Precondiciones
input  = Input ( only = ( 'username', 'password' ) )
output = Output ()


class Endpoint ( SuccessEndpoint ) :

  def post ( self ) -> Response :
    
    try :

      Http.requestIsJson () # TODO donde colocar esta clase para evitar dependencia circular al agregar el lanzamiento de la excepcion correspondiente
      inputData                = input.load ( request.get_json () )
      user                     = User ()
      inputData [ 'password' ] = Encryption.password ( inputData [ 'password' ] )
      userObj                  = user.findByFilters ( False, **inputData )
      result                   = Resultset.toJson ( userObj )
      self.responseData        = output.data ( result [ 0 ] )
      self.statusResponse      = HTTPStatus.OK
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
