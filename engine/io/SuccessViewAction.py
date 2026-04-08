# Python Libraries / Librerías Python
from flask       import render_template
from flask       import request
from flask       import Response
from flask.views import View

# Success Libraries / Librerías Success
from success.engine.io.SuccessAction               import SuccessAction
from success.engine.infrastructure.SuccessController import SuccessController
from success.engine.io.SuccessInput                  import SuccessInput
from success.engine.io.SuccessOutput                 import SuccessOutput

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessViewAction ( SuccessAction, View ) :


  def __init__( self, _input : SuccessInput, _output : SuccessOutput, _controller : SuccessController ) -> None :
    super ().__init__ ( _input, _output, _controller )
    
  
  def dispatch_request ( self ) -> Response :
    if request.method == "GET" :
      return self.get ()

    return "Método no soportado", 405


  def get ( self ) -> Response :
    raise NotImplementedError ( "Debes implementar el método GET en tu Action de vista." )
