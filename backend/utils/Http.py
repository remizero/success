# Python Libraries / Librerías Python
from flask  import json
from flask  import request
from flask  import Response
from typing import Any


# Application Libraries / Librerías de la Aplicación
from exceptions import JsonRequestException
from exceptions import RequestMethodException


# Preconditions / Precondiciones


class Http () :

  @staticmethod
  def isDelete () -> bool :
    return Http.__isMethod ( 'DELETE' )

  @staticmethod
  def isGet () -> bool :
    return Http.__isMethod ( 'GET' )

  @staticmethod
  def isPost () -> bool :
    return Http.__isMethod ( 'POST' )

  @staticmethod
  def isPut () -> bool :
    return Http.__isMethod ( 'PUT' )

  @staticmethod
  def isMethod ( method : str ) -> bool :
    return request.method == method

  @staticmethod
  def __isMethod ( method : str ) -> bool :
    if request.method == method :

      return True

    raise RequestMethodException ( method )

  @staticmethod
  def requestIsJson () -> bool :
    if request.is_json :

      return True

    raise JsonRequestException ()

  @staticmethod
  def response ( data : Any, status : int ) -> Response :
    return Response (
      response = json.dumps ( data ),
      status   = status,
      mimetype = 'application/json'
    )
