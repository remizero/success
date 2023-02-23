# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from app.apis.success.user.create import Input
from app.apis.success.user.create import Output
from kernel.abstracts             import Endpoint as SuccessEndpoint
from kernel.abstracts.Endpoint    import Debug
from kernel.abstracts.Endpoint    import Encryption
from kernel.abstracts.Endpoint    import Http
from kernel.abstracts.Endpoint    import HTTPStatus
from kernel.abstracts.Endpoint    import JsonRequestException
from kernel.abstracts.Endpoint    import jwt
from kernel.abstracts.Endpoint    import LoginException
from kernel.abstracts.Endpoint    import OutputException
from kernel.abstracts.Endpoint    import Permissions
from kernel.abstracts.Endpoint    import request
from kernel.abstracts.Endpoint    import Response
from kernel.abstracts.Endpoint    import Resultset
from kernel.abstracts.Endpoint    import Session
from kernel.abstracts.Endpoint    import SchemaError
from kernel.abstracts.Endpoint    import Structs
from kernel.abstracts.Endpoint    import ValidationError
from app.models                   import User
from app.models                   import UserGroup
from app.models                   import Group


# Preconditions / Precondiciones


class Endpoint ( SuccessEndpoint ) :

  def __init__ ( self ) -> None :
    self.input  = Input ()
    self.model  = User ()
    self.output = Output ()
    super ().__init__ ()

  def get ( self ) -> Response :

    try :
      if ( Session.isLogin () ) : # TODO donde colocar esta clase para evitar dependencia circular al agregar el lanzamiento de la excepcion correspondiente

        # TODO Verificar permisos para acceder a esta seccion
        self.status   = HTTPStatus.ACCEPTED
        self.response = Http.response ( self.output.output (), self.status )

      else :

        raise LoginException ()

    except ( LoginException ) as exception :

      self.logger.log ( exception )
      self.status = HTTPStatus.UNAUTHORIZED
      self.output.exception ( self.logger.toShow (), 'WARNING', self.status )

    finally :

      self.response = Http.response ( self.output.output (), self.status )

    return self.response

  def post ( self ) -> Response :

    # TODO Verificar permisos para acceder a esta seccion
    try :

      Http.requestIsJson ()
      self.inputData [ 'password' ] = Encryption.password ( self.inputData [ 'password' ] )
      self.model.inputData ( **self.inputData )
      # TODO verificar que no se duplique la data independientemente de si lo maneja la DB.
      # como controlar la excepcion de duplicacion de SqlAlchemy
      self.model.insert ()
      self.status = HTTPStatus.OK

    except ( 
      JsonRequestException,
      OutputException,
      ValidationError,
      SchemaError
    ) as exception :

      self.logger.log ( exception )
      self.output.exception ( self.logger.toShow (), 'CRITICAL', self.status )

    except ( LoginException ) as exception :

      self.logger.log ( exception )
      self.status = HTTPStatus.UNAUTHORIZED
      self.output.exception ( self.logger.toShow (), 'WARNING', self.status )

    except :

      self.logger.uncatchErrorException ()
      self.output.exception ( self.logger.toShow (), 'FATAL', self.status )

    finally :

      self.response = Http.response ( self.output.output (), self.status )

    return self.response
