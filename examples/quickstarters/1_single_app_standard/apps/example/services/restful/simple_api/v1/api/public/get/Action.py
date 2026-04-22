# Python Libraries / Librerías Python
from flask import Response as FlaskResponse

# Success Libraries / Librerías Success
from success.engine.io.SuccessRestfulAction import SuccessRestfulAction

# Application Libraries / Librerías de la Aplicación
from apps.example.services.restful.simple_api.v1.api.public.get.Input    import Input
from apps.example.services.restful.simple_api.v1.api.public.get.Output   import Output
from apps.example.services.restful.simple_api.v1.api.public.get.Response import Response
from apps.example.modules.example.v1.view.controllers.PublicApi          import PublicApi

# Preconditions / Precondiciones


class Action ( SuccessRestfulAction ) :


  def __init__ ( self ) -> None :
    super ().__init__ ( Input (), Output (), Response (), PublicApi () )
    self._controllerMethod = "fetch"


  def get ( self ) -> FlaskResponse :
    return self.execute ( self._controllerMethod )
