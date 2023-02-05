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
    self.input = Input ( only = ( 'username', 'password' ) )
    self.model = User ()
    self.output = Output ( True )
    super ().__init__ ()

  def get ( self ) -> Response :

    if ( Session.exist ( 'loggedin' ) ) :

      self.status = HTTPStatus.ACCEPTED
      self.response = Http.response ( self.output.output (), self.status )

    else :
      self.status = HTTPStatus.CONTINUE
      self.output.exception ( 'Ya existe una sesión.', 'WARNING', self.status )
      self.response = Http.response ( self.output.output (), self.status )

    return self.response

  def post ( self ) -> Response :

    try :

      Http.requestIsJson ()
      self.inputData [ 'password' ] = Encryption.password ( self.inputData [ 'password' ] )
      modelObj = self.model.findByFilters ( False, **self.inputData )
      result = Resultset.toJson ( modelObj )
      profile = modelObj.profiles.filter_by ().all ()
      result [ 0 ] [ 'fullname' ] = profile [ 0 ].name_first + ' ' + profile [ 0 ].lastname_first
      self.status = HTTPStatus.ACCEPTED
      result [ 0 ] [ 'status' ] = self.status
      result [ 0 ] [ 'type' ] = 'ACCEPTED'
      self.output.data ( result [ 0 ] )

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
      if self.status == HTTPStatus.ACCEPTED :
        try :
          Session.create ( modelObj )
          ( self.response, token ) = jwt.create ( self.response )
          Session.set ( 'token', token )
        except :
          self.logger.uncatchErrorException ()
          self.output.exception ( self.logger.toShow (), 'FATAL', self.status )
          self.status = HTTPStatus.BAD_REQUEST
          self.response = Http.response ( self.output.output (), self.status )

    return self.response
