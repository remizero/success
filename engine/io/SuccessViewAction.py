# Python Libraries / Librerías Python
from flask       import render_template
from flask       import request
from flask       import Response
from flask.views import View

# Success Libraries / Librerías Success
from success.common.types.SuccessProtocol            import SuccessProtocol
from success.engine.io.SuccessAction                 import SuccessAction
from success.engine.context.SuccessResponse          import SuccessResponse
from success.engine.infrastructure.SuccessController import SuccessController
from success.engine.io.SuccessInput                  import SuccessInput
from success.engine.io.SuccessOutput                 import SuccessOutput

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessViewAction ( SuccessAction, View ) :
  """
  View action handler for HTML view endpoints.

  Combines SuccessAction with Flask View for handling
  HTML view requests with GET method support.
  """


  def __init__( self, _input : SuccessInput, _output : SuccessOutput, _response : SuccessResponse, _controller : SuccessController ) -> None :
    """
    Initialize the view action.

    Args:
      _input: Input handler instance.
      _output: Output handler instance.
      _response: Response handler instance.
      _controller: Controller instance.
    """
    super ().__init__ ( _input, _output, _response, _controller )
    self._outputSpec.protocol = SuccessProtocol.VIEW


  def dispatch_request ( self ) -> Response :
    """
    Dispatch the request based on HTTP method.

    Returns:
      Response: Flask response object.
    """
    if request.method == "GET" :
      return self.get ()

    return "Method not supported", 405


  def get ( self ) -> Response :
    """
    Handle GET requests.

    Returns:
      Response: Flask response object.

    Raises:
      NotImplementedError: Must be implemented by subclasses.
    """
    raise NotImplementedError ( "You must implement the GET method in your View Action." )
