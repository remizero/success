# Python Libraries / Librerías Python
from flask import request

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class Context () :


  def resolve ( self, request : request ) -> str :

    if 'text/html' in request.accept_mimetypes :
      return 'html'

    elif request.is_json :
      return 'json'

    return 'unknown'
