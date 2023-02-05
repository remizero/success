# Python Libraries / Librerías Python
from flask import (
  json,
  request,
  Response
)
from flask_restful import Resource
from http import HTTPStatus
from jsonschema.exceptions import (
  ValidationError,
  SchemaError
)


# Application Libraries / Librerías de la Aplicación
from exceptions import (
  JsonRequestException,
  OutputException,
  RequestMethodException
)
from . import (
  Logger,
  Model,
  Debug,
  Output,
  Schema
)
from extensions import jwt
from managers import (
  Permissions,
  Session
)
from utils import (
  Encryption,
  Http,
  Resultset,
  Structs
)


# Preconditions / Precondiciones


class Endpoint ( Resource ) :

  input    : Schema   = None
  inputData           = None
  logger              = Logger ( __name__ )
  model    : Model    = None
  output   : Output   = None
  response : Response = None
  data                = None
  status              = HTTPStatus.BAD_REQUEST

  def __init__( self ) -> None :
    super ().__init__ ()
    if ( Http.isMethod ( 'POST' ) ) :
      self.inputData = self.input.load ( request.get_json () )
