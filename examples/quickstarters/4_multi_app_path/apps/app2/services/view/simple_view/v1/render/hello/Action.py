# Python Libraries / Librerías Python
from flask import Response as FlaskResponse

# Success Libraries / Librerías Success
from success.engine.io.SuccessViewAction import SuccessViewAction
from success.engine.io.SuccessOutput     import SuccessOutput

# Application Libraries / Librerías de la Aplicación
from apps.app2.services.view.simple_view.v1.render.hello.Input    import Input
from apps.app2.services.view.simple_view.v1.render.hello.Response import Response as ActionResponse
from apps.app2.modules.app2.v1.view.controllers.Hello            import Hello

# Preconditions / Precondiciones


class Action ( SuccessViewAction ) :


  def __init__ ( self ) -> None :
    super ().__init__ ( Input (), SuccessOutput (), ActionResponse (), Hello () )
    self._controllerMethod    = "load"
    self._outputSpec.template = "hello.html"


  def get ( self ) -> FlaskResponse :
    return self.execute ( self._controllerMethod )
