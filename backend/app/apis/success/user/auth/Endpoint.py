# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from .Input import Input
from .Output import Output
from kernel.Endpoint import (
  Debug,
  Encryption,
  Endpoint as SuccessEndpoint,
  Http,
  HTTPStatus,
  JsonRequestException,
  jwt,
  OutputException,
  Permissions,
  request,
  Response,
  Result,
  Session,
  SchemaError,
  Structs,
  ValidationError
)
from app.models import User


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
      result = Result.toJson ( userObj )
      self.data = output.data ( result [ 0 ] )
      self.status = HTTPStatus.ACCEPTED
      '''
        HASTA AQUI TODO BIEN
        1-. AJUSTAR EL OUTPUT AL FORMATO SUCCESS PARA RETORNAR DE CONSULTA SOLICITADA
        2-. AJUSTAR EL OUTPUT AL FORMATO STANDARD PARA RETORNAR DE CONSULTA SOLICITADA
        3-. CARGAR LA DATA RESPECTIVA A LA SESSION
        4-. CREAR EL JWT
        5-. Manejo de permisos
        6-. Agregar el nombre del usuario en el output
      '''

    except ( 
      JsonRequestException,
      OutputException,
      ValidationError,
      SchemaError
    ) as exception :

      self.logger.log ( exception )
      self.data = output.exception ( self.logger.toShow (), 'CRITICAL', HTTPStatus.BAD_REQUEST )

    except :

      self.logger.uncatchErrorException ()
      self.data = output.exception ( self.logger.toShow (), 'CRITICAL', HTTPStatus.BAD_REQUEST )

    finally :

      self.response = Http.response ( self.data, self.status )
      if self.status == HTTPStatus.ACCEPTED :
        ( self.response, token ) = jwt.create ( self.response )
        Session.create ( userObj, token )
    return self.response
