# Python Libraries / Librerías Python
import requests

# Success Libraries / Librerías Success
from success.engine.infrastructure.SuccessController import SuccessController

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class PublicApi ( SuccessController ) :

  _sourceUrl : str = "https://jsonplaceholder.typicode.com/todos/1"


  def fetch ( self, payload : dict ) -> dict :
    try :
      resultset = requests.get ( self._sourceUrl, timeout = 10 )
      data      = resultset.json ()

      return {
        "status" : resultset.status_code,
        "body"   : {
          "source" : self._sourceUrl,
          "data"   : data
        }
      }

    except Exception as e :
      return {
        "status" : 500,
        "error"  : f"No fue posible consultar la API pública: {str ( e )}",
        "body"   : {
          "source" : self._sourceUrl
        }
      }
