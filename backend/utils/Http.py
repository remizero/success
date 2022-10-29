# Python Libraries / Librerías Python
from flask import (
  json,
  request,
  Response
)


# Application Libraries / Librerías de la Aplicación
from exceptions import (
  JsonRequestException,
  RequestMethodException
)


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
  def returnResponse ( responseData, statusResponse ) -> Response :
    return Response (
      response = json.dumps ( responseData ),
      status = statusResponse,
      mimetype = 'application/json'
    )
