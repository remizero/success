# Python Libraries / Librerías Python
from flask_restful import Resource

# Success Libraries / Librerías Success
from success.common.types.SuccessProtocol            import SuccessProtocol
from success.engine.io.SuccessAction                 import SuccessAction
from success.engine.infrastructure.SuccessController import SuccessController
from success.engine.io.SuccessInput                  import SuccessInput
from success.engine.io.SuccessOutput                 import SuccessOutput
from success.engine.context.SuccessResponse          import SuccessResponse

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessRestfulAction ( SuccessAction, Resource ) :
  """
  RESTful action handler for REST API endpoints.

  Combines SuccessAction with Flask-RESTful Resource for
  handling REST API requests.
  """


  def __init__( self, _input : SuccessInput, _output : SuccessOutput, _response : SuccessResponse, _controller : SuccessController ) -> None :
    """
    Initialize the RESTful action.

    Args:
      _input: Input handler instance.
      _output: Output handler instance.
      _response: Response handler instance.
      _controller: Controller instance.
    """
    super ().__init__ ( _input, _output, _response, _controller )
    self._outputSpec.protocol = SuccessProtocol.RESTFUL
