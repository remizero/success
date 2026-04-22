# Python Libraries / Librerías Python
from flask         import Flask
from flask_caching import Cache

# Success Libraries / Librerías Success
from success.common.base.SuccessExtension import SuccessExtension

# Preconditions / Precondiciones


class SuccessCacheExtension ( SuccessExtension ) :
  """
  Cache extension for the Success framework.

  Integrates Flask-Caching for caching operations
  and performance optimization.
  """


  def __init__ ( self, app : Flask ) -> None :
    """
    Initialize the Cache extension.

    Args:
      app: Flask application instance.
    """
    super ().__init__ ( app )
    self._extension = Cache ()
