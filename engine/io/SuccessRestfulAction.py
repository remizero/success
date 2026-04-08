# Python Libraries / Librerías Python
from flask_restful import Resource

# Success Libraries / Librerías Success
from success.engine.io.SuccessAction               import SuccessAction
from success.engine.infrastructure.SuccessController import SuccessController
from success.engine.io.SuccessInput                  import SuccessInput
from success.engine.io.SuccessOutput                 import SuccessOutput

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessRestfulAction ( SuccessAction, Resource ) :


  def __init__( self, _input : SuccessInput, _output : SuccessOutput, _controller : SuccessController ) -> None :
    super ().__init__ ( _input, _output, _controller )
