# Python Libraries / Librerías Python
from abc import abstractmethod

# Success Libraries / Librerías Success
from success.common.base.SuccessClass    import SuccessClass

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessOutputModelContract ( SuccessClass ) :
  """
  Abstract contract for output models.

  Defines the interface that all output models must implement
  for building output from canonical format.

  Attributes:
    _outputModel (dict): Output model data.
  """

  _outputModel : dict = None


  def __init__ ( self ) :
    """
    Initialize the output model contract.
    """
    super ().__init__ ()


  @abstractmethod
  def build ( self, canonicalOutput : dict ) -> dict :
    """
    Build output from canonical format.

    Args:
      canonicalOutput: Canonical output dictionary.

    Returns:
      dict: Built output.

    Raises:
      NotImplementedError: Must be implemented by subclasses.
    """
    raise NotImplementedError
