# Python Libraries / Librerías Python
from abc  import abstractmethod
from copy import deepcopy

# Success Libraries / Librerías Success
from success.engine.io.SuccessOutputModelContract import SuccessOutputModelContract
from success.common.tools.SuccessStructs          import SuccessStructs

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessRichOutputModel ( SuccessOutputModelContract ) :
  """
  Rich output model with action and UI model support.

  Extends canonical output with action URL, data, and
  UI model schema for rich client interactions.
  """


  def __init__ ( self ) :
    """
    Initialize the rich output model.
    """
    super ().__init__ ()


  def build ( self, canonicalOutput : dict ) -> dict :
    """
    Build rich output from canonical format.

    Args:
      canonicalOutput: Canonical output dictionary.

    Returns:
      dict: Built output with action, data, and UI model.
    """
    output = deepcopy ( canonicalOutput )

    rich = SuccessStructs.successRichSchema ()
    rich [ "action" ]  = self.action ()
    rich [ "data" ]    = deepcopy ( output.get ( "data" ) )
    rich [ "uimodel" ] = deepcopy ( self.uiModel () )

    output [ "data" ]  = rich
    return output


  @abstractmethod
  def action ( self ) -> str :
    """
    Get the action URL.

    Returns:
      str: Action URL.

    Raises:
      NotImplementedError: Must be implemented by subclasses.
    """
    raise NotImplementedError ()


  @abstractmethod
  def uiModel ( self ) -> list :
    """
    Generate the UI model schema.

    Returns:
      list: List of UI model field schemas.

    Raises:
      NotImplementedError: Must be implemented by subclasses.
    """
    raise NotImplementedError ()
