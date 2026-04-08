# Python Libraries / Librerías Python
from flask  import json
from flask  import request
from flask  import Response
from typing import Any

# Success Libraries / Librerías Success
from success.common.exceptions.JsonRequestException   import JsonRequestException
from success.common.exceptions.RequestMethodException import RequestMethodException

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessHttp () :


  @staticmethod
  def contentTypeHtml () -> dict :
    return { "Content-Type": "text/html" }


  @staticmethod
  def isDelete () -> bool :
    return SuccessHttp.__isMethod ( 'DELETE' )


  @staticmethod
  def isGet () -> bool :
    return SuccessHttp.__isMethod ( 'GET' )


  @staticmethod
  def isPatch () -> bool :
    return SuccessHttp.__isMethod ( 'PATCH' )


  @staticmethod
  def isPost () -> bool :
    return SuccessHttp.__isMethod ( 'POST' )


  @staticmethod
  def isPut () -> bool :
    return SuccessHttp.__isMethod ( 'PUT' )


  @staticmethod
  def isMethod ( method : str ) -> bool :
    return request.method == method


  @staticmethod
  def __isMethod ( method : str ) -> bool :
    return request.method == method


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
