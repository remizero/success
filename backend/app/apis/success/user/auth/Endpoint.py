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
  OutputException,
  request,
  Response,
  Result,
  session,
  SchemaError,
  Structs,
  ValidationError
)
from app.models import User


# Preconditions / Precondiciones
#session = sessionFlask
input = Input ( only = ( 'username', 'password' ) )
output = Output ()


class Endpoint ( SuccessEndpoint ) :

  def post ( self ) -> Response :

    #from flask import session
    
    try :

      Http.requestIsJson ()
      inputData = input.load ( request.get_json () )
      user = User ()
      inputData [ 'password' ] = Encryption.password ( inputData [ 'password' ] )
      userObj = user.findByFilters ( False, **inputData )
      result = Result.toJson ( userObj )
      #self.session.
      #session [ 'id' ] = userObj.id
      Debug.log ( type ( session ) )
      Debug.log ( session )
      # session = Structs.session ()
      # Debug.log ( type ( session ) )
      # Debug.log ( session )
      # session [ 'id' ] = userObj.id
      # session [ 'group_id' ] = userObj.id
      # session [ 'role_id' ] = userObj.id
      # 'id' : '',
      # 'username' : '',
      # 'group_id' : '',
      # 'role_id' : '',
      # 'token' : ''
      self.responseData = output.data ( result [ 0 ] )
      self.responseStatus = HTTPStatus.ACCEPTED
      '''
        HASTA AQUI TODO BIEN
        1-. AJUSTAR EL OUTPUT AL FORMATO SUCCESS PARA RETORNAR DE CONSULTA SOLICITADA
        2-. AJUSTAR EL OUTPUT AL FORMATO STANDARD PARA RETORNAR DE CONSULTA SOLICITADA
        3-. CARGAR LA DATA RESPECTIVA A LA SESSION
        4-. CREAR EL JWT
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

    finally :

      self.response = Http.returnResponse ( self.responseData, self.responseStatus )
    # if self.responseStatus == HTTPStatus.OK :
    #   JsonWebToken.create ( response )
    return self.response
