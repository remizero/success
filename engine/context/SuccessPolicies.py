# Python Libraries / Librerías Python

# Success Libraries / Librerías Success
from success.common.base.SuccessClass                 import SuccessClass
from success.engine.context.SuccessPostOutputPolicy   import SuccessPostOutputPolicy
from success.engine.context.SuccessPreInputPolicy     import SuccessPreInputPolicy
from success.engine.context.SuccessResponsePolicy     import SuccessResponsePolicy

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessPolicies ( SuccessClass ) :
  """
  Policy manager for input and output processing.

  Coordinates pre-input and post-output policy evaluation
  for the Success framework.

  Attributes:
    _preInputPolicy (SuccessPreInputPolicy): Pre-input policy handler.
    _postOutputPolicy (SuccessPostOutputPolicy): Post-output policy handler.
  """

  _preInputPolicy   : SuccessPreInputPolicy   = None
  _postOutputPolicy : SuccessPostOutputPolicy = None


  def __init__ ( self, preInputPolicy : SuccessPreInputPolicy = None, postOutputPolicy : SuccessPostOutputPolicy = None ) -> None :
    """
    Initialize the policy manager.

    Args:
      preInputPolicy: Pre-input policy instance. Uses default if None.
      postOutputPolicy: Post-output policy instance. Uses default if None.
    """
    super ().__init__ ()
    self._preInputPolicy   = preInputPolicy or SuccessPreInputPolicy ()
    self._postOutputPolicy = postOutputPolicy or SuccessPostOutputPolicy ()


  def preInput ( self, action, method : str ) -> dict :
    """
    Evaluate pre-input policies for an action.

    Args:
      action: The action to evaluate.
      method: HTTP method name.

    Returns:
      dict: Policy evaluation result.
    """
    return self._preInputPolicy.evaluate ( action, method )


  def postOutput ( self, builtOutput : dict, responsePolicy : SuccessResponsePolicy ) -> dict :
    """
    Apply post-output policies to the built output.

    Args:
      builtOutput: The built output dictionary.
      responsePolicy: Response policy to apply.

    Returns:
      dict: Modified output after applying policies.
    """
    return self._postOutputPolicy.apply ( builtOutput, responsePolicy )
