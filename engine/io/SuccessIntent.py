# Python Libraries / Librerías Python
from abc   import ABC
from abc   import abstractmethod
from flask import Response

# Success Libraries / Librerías Success
from success.engine.context.SuccessResponsePolicy import SuccessResponsePolicy

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessIntent ( ABC ) :
  """
  Abstract base class for output intent executors.

  Defines the interface for executing different types of output
  such as default JSON, redirect, or template render.
  """


  @abstractmethod
  def execute ( self, builtOutput : dict, responsePolicy : SuccessResponsePolicy ) -> Response :
    """
    Execute the intent and return a Flask response.

    Args:
      builtOutput: Built output dictionary.
      responsePolicy: Response policy for configuration.

    Returns:
      Response: Flask response object.

    Raises:
      NotImplementedError: Must be implemented by subclasses.
    """
    raise NotImplementedError ()
