# Python Libraries / Librerías Python

# Success Libraries / Librerías Success
from success.engine.infrastructure.SuccessController import SuccessController

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class Hello ( SuccessController ) :


  def load ( self, payload : dict ) -> dict :
    return {
      "status"        : 200,
      "hello_message" : "Hello World desde Success View",
      "api_endpoint"  : "/public/",
      "app"           : "app1"
    }
