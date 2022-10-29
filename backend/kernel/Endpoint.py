# Python Libraries / Librerías Python
from flask import (
  json,
  request,
  session,
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
  RequestMethodException
)
from . import Logger
#from utils.Structs import Structs
from utils import (
  Encryption,
  Http,
  Result,
  Structs
)


# Preconditions / Precondiciones


class Endpoint ( Resource ) :

  logger = Logger ( __name__ )
  responseData = ''
  statusResponse = HTTPStatus.BAD_REQUEST
