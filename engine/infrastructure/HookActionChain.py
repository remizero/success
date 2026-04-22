# Python Libraries / Librerías Python

# Application Libraries / Librerías de la Aplicación
from success.engine.infrastructure.HookAction import HookAction

# Preconditions / Precondiciones


class HookActionChain () :
  """
  Fluent builder for creating hierarchical hook actions.

  Example:
    HookActionChain.start("build", "endpoint").component("adapter").stage("register")
  """

  def __init__ ( self, baseAction : HookAction ) -> None :
    """
    Initialize the chain with a base action.

    Args:
      baseAction: Base HookAction to start the chain.
    """
    self._action = baseAction


  @staticmethod
  def start ( verb : str, domain : str ) -> "HookActionChain" :
    """
    Start a new chain with verb and domain.

    Args:
      verb: Action verb.
      domain: Action domain.

    Returns:
      HookActionChain: New chain instance.
    """
    return HookActionChain ( HookAction ( verb, domain ) )


  @staticmethod
  def fromAction ( action : HookAction | str ) -> "HookActionChain" :
    """
    Start a chain from an existing action.

    Args:
      action: HookAction or string to start from.

    Returns:
      HookActionChain: New chain instance.
    """
    parsed = action if isinstance ( action, HookAction ) else HookAction.fromString ( action )
    return HookActionChain ( parsed )


  def component ( self, name : str ) -> "HookActionChain" :
    """
    Add a component segment to the chain.

    Args:
      name: Component name.

    Returns:
      HookActionChain: Self for chaining.
    """
    self._action = self._action.child ( name )
    return self


  def stage ( self, name : str ) -> "HookActionChain" :
    """
    Add a stage segment to the chain.

    Args:
      name: Stage name.

    Returns:
      HookActionChain: Self for chaining.
    """
    self._action = self._action.child ( name )
    return self


  def detail ( self, name : str ) -> "HookActionChain" :
    """
    Add a detail segment to the chain.

    Args:
      name: Detail name.

    Returns:
      HookActionChain: Self for chaining.
    """
    self._action = self._action.child ( name )
    return self


  def then ( self, name : str ) -> "HookActionChain" :
    """
    Add an additional segment to the chain.

    Args:
      name: Segment name.

    Returns:
      HookActionChain: Self for chaining.
    """
    self._action = self._action.child ( name )
    return self


  def build ( self ) -> HookAction :
    """
    Build and return the final HookAction.

    Returns:
      HookAction: The built action.
    """
    return self._action


  def asString ( self ) -> str :
    """
    Get the action as a colon-separated string.

    Returns:
      str: Colon-separated action string.
    """
    return self._action.asString ()


  def __str__ ( self ) -> str :
    """
    Return string representation of the chain.

    Returns:
      str: Colon-separated action string.
    """
    return self.asString ()

