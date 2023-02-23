# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from app.apis.success.user.auth import Input
from app.apis.success.user.auth import Output
from kernel.abstracts           import Endpoint as SuccessEndpoint
from kernel.abstracts.Endpoint  import Debug
from kernel.abstracts.Endpoint  import Encryption
from kernel.abstracts.Endpoint  import Http
from kernel.abstracts.Endpoint  import HTTPStatus
from kernel.abstracts.Endpoint  import JsonRequestException
from kernel.abstracts.Endpoint  import jwt
from kernel.abstracts.Endpoint  import LoginException
from kernel.abstracts.Endpoint  import OutputException
from kernel.abstracts.Endpoint  import Permissions
from kernel.abstracts.Endpoint  import request
from kernel.abstracts.Endpoint  import Response
from kernel.abstracts.Endpoint  import Resultset
from kernel.abstracts.Endpoint  import Session
from kernel.abstracts.Endpoint  import SchemaError
from kernel.abstracts.Endpoint  import Structs
from kernel.abstracts.Endpoint  import ValidationError
from app.models                 import User
from app.models                 import UserGroup
from app.models                 import Group


# Preconditions / Precondiciones


class Endpoint ( SuccessEndpoint ) :

  def __init__ ( self ) -> None :
    self.input  = Input ( only = ( 'username', 'password' ) )
    self.model  = User ()
    self.output = Output ( True )
    super ().__init__ ()

  def get ( self ) -> Response :

    if ( Session.exist ( 'loggedin' ) ) :

      self.status   = HTTPStatus.CONTINUE
      self.output.exception ( 'Ya existe una sesión.', 'WARNING', self.status )
      self.response = Http.response ( self.output.output (), self.status )

    else :

      self.status   = HTTPStatus.ACCEPTED
      self.response = Http.response ( self.output.output (), self.status )

    return self.response

  def post ( self ) -> Response :

    try :

      if ( Http.requestIsJson () ) : # TODO donde colocar esta clase para evitar dependencia circular al agregar el lanzamiento de la excepcion correspondiente

        self.inputData [ 'password' ]  = Encryption.password ( self.inputData [ 'password' ] )
        modelObj                       = self.model.findByFilters ( False, **self.inputData )
        resultSet                      = Resultset.toJson ( modelObj )
        profile                        = modelObj.profiles.filter_by ().all ()
        resultSet [ 0 ] [ 'fullname' ] = profile [ 0 ].name_first + ' ' + profile [ 0 ].lastname_first
        self.status                    = HTTPStatus.ACCEPTED
        resultSet [ 0 ] [ 'status' ]   = self.status
        resultSet [ 0 ] [ 'type' ]     = 'ACCEPTED'
        self.output.data ( resultSet [ 0 ] )

      else :

        raise JsonRequestException ()

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
          self.status   = HTTPStatus.BAD_REQUEST
          self.output.exception ( self.logger.toShow (), 'FATAL', self.status )
          self.response = Http.response ( self.output.output (), self.status )

    return self.response
