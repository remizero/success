# Python Libraries / Librerías Python
from flask       import Flask
from flask_login import LoginManager

# Success Libraries / Librerías Success
from success.common.base.SuccessExtension import SuccessExtension

# Preconditions / Precondiciones


class SuccessLoginExtension ( SuccessExtension ) :
  """
  Login extension for the Success framework.

  Integrates Flask-Login for user session management
  and authentication handling.
  """


  def __init__ ( self, app : Flask ) -> None :
    """
    Initialize the Login extension.

    Args:
      app: Flask application instance.
    """
    super ().__init__ ( app )
    self._extension = LoginManager ()


  def policyDefaults ( self ) -> dict :
    """
    Get default policy settings for Login.

    Returns:
      dict: Dictionary with default Login policy settings.
    """
    return {
      "require_login" : False
    }
