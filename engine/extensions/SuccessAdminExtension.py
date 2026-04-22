# Python Libraries / Librerías Python
from flask       import Flask
from flask_admin import Admin


# Success Libraries / Librerías Success
from success.common.base.SuccessExtension import SuccessExtension

# Preconditions / Precondiciones


class SuccessAdminExtension ( SuccessExtension ) :
  """
  Admin extension for the Success framework.

  Integrates Flask-Admin for administrative interface
  management.
  """


  def __init__ ( self, app : Flask ) -> None :
    """
    Initialize the Admin extension.

    Args:
      app: Flask application instance.
    """
    super ().__init__ ( app )
    self._extension = Admin ()
