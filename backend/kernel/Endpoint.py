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
from . import Logger, Debug
from extensions import jwt
from managers import (
  Permissions,
  Session
)
from utils import (
  Encryption,
  Http,
  Result,
  Structs
)


# Preconditions / Precondiciones


class Endpoint ( Resource ) :

  logger = Logger ( __name__ )
  response : Response = ''
  data = ''
  status = HTTPStatus.BAD_REQUEST
