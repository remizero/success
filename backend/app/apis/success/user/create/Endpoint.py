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
  Resultset,
  Session,
  SchemaError,
  Structs,
  ValidationError
)
from app.models import (
  User,
  UserGroup,
  Group
)


# Preconditions / Precondiciones


class Endpoint ( SuccessEndpoint ) :

  def __init__ ( self ) -> None :
    self.input = Input ()
    self.model = User ()
    self.output = Output ()
    super ().__init__ ()

  def get ( self ) -> Response :

    if ( Session.exist ( 'loggedin' ) ) :
      # TODO Verificar permisos para acceder a esta seccion

      self.status = HTTPStatus.ACCEPTED
      self.response = Http.response ( self.output.output (), self.status )

    else :

      self.status = HTTPStatus.UNAUTHORIZED
      self.output.exception ( 'Debe estar autenticado en el sistema.', 'WARNING', self.status )
      self.response = Http.response ( self.output.output (), self.status )

    return self.response

  def post ( self ) -> Response :

    # TODO Verificar permisos para acceder a esta seccion
    try :

      Http.requestIsJson ()
      self.inputData [ 'password' ] = Encryption.password ( self.inputData [ 'password' ] )
      self.model.inputData ( **self.inputData )
      self.model.insert ()
      self.status = HTTPStatus.OK
      # self.output.data ( result [ 0 ] )

    except ( 
      JsonRequestException,
      OutputException,
      ValidationError,
      SchemaError
    ) as exception :

      self.logger.log ( exception )
      self.output.exception ( self.logger.toShow (), 'CRITICAL', self.status )

    except :

      self.logger.uncatchErrorException ()
      self.output.exception ( self.logger.toShow (), 'FATAL', self.status )

    finally :

      self.response = Http.response ( self.output.output (), self.status )

    return self.response
