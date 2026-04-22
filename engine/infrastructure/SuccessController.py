# Python Libraries / Librerías Python
from typing import Any, Dict, List, Type

# Success Libraries / Librerías Success
from success.engine.models.SuccessModel import SuccessModel

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessController () :
  """
  Base contract for all controllers in the Success ecosystem.

  - All methods receive a `payload: dict` that has been
    normalized by the Input layer.
  - Each method must return a `dict` compatible with Output.
  - Execution can be dynamic via `execute(...)`.
  - Pre-hook allowed per method (`before_method`).
  """


  # Hook: allows modifying payload before executing any method
  def before_method ( self, method : str, payload : Dict [ str, Any ] ) -> Dict [ str, Any ] :
    """
    Hook that executes before the requested method.
    Can modify or validate the payload before execution.

    Args:
      method: Method name being executed.
      payload: Payload dictionary.

    Returns:
      Dict[str, Any]: Modified payload.
    """
    return payload


  # Dynamic method execution
  def execute ( self, method : str, payload : Dict [ str, Any ] ) -> Dict [ str, Any ] :
    """
    Execute the specified method passing the payload as parameter.
    Uses introspection to validate method existence.

    Args:
      method: Method name to execute.
      payload: Payload dictionary.

    Returns:
      Dict[str, Any]: Method execution result.

    Raises:
      NotImplementedError: If method is not executable.
    """
    if method not in self.methods :
      raise NotImplementedError ( f"Method '{method}' is not executable by controller {self.__class__.__name__}" )

    return getattr ( self, method ) ( payload )


  def get_model ( self ) -> Type [ SuccessModel ] :
    """
    Get the associated model, if any.

    Returns:
      Type[SuccessModel]: Associated model or None.
    """
    return getattr ( self, "_model", None )


  @property
  def has_model ( self ) -> bool :
    """
    Check if the controller has an associated model.

    Returns:
      bool: True if controller has a model.
    """
    return hasattr ( self, "_model" ) and self._model is not None


  @property
  def methods ( self ) -> List [ str ] :
    """
    Get the list of public methods available in the controller.
    Excludes methods inherited from SuccessController.

    Returns:
      List[str]: List of method names.
    """
    base_methods = set ( dir ( SuccessController ) )
    methods : List [ str ] = []

    for methodName in dir ( self.__class__ ) :
      if methodName.startswith ( "_" ) :
        continue

      if methodName in base_methods :
        continue

      methodRef = getattr ( self.__class__, methodName, None )
      if callable ( methodRef ) :
        methods.append ( methodName )

    return methods
