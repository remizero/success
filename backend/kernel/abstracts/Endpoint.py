# Python Libraries / Librerías Python
from flask                 import json
from flask                 import request
from flask                 import Response
from flask_restful         import Resource
from http                  import HTTPStatus
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError


# Application Libraries / Librerías de la Aplicación
from exceptions       import JsonRequestException
from exceptions       import LoginException
from exceptions       import OutputException
from exceptions       import RequestMethodException
from extensions       import jwt
from kernel           import Logger
from kernel           import Debug
from kernel.abstracts import Model
from kernel.abstracts import Schema
from kernel.abstracts import Output
from managers         import Permissions
from managers         import Session
from utils            import Encryption
from utils            import Http
from utils            import Resultset
from utils            import Structs


# Preconditions / Precondiciones


class Endpoint ( Resource ) :

  input     : Schema     = None
  inputData : dict       = None
  logger    : Logger     = Logger ( __name__ )
  model     : Model      = None
  output    : Output     = None
  response  : Response   = None
  status    : HTTPStatus = HTTPStatus.BAD_REQUEST

  def __init__( self ) -> None :
    super ().__init__ ()
    if ( Http.isMethod ( 'POST' ) ) :
      self.inputData = self.input.load ( request.get_json () )
