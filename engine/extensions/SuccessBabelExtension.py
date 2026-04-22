# Python Libraries / Librerías Python
from flask       import Flask
from flask_babel import Babel

# Success Libraries / Librerías Success
from success.common.base.SuccessExtension import SuccessExtension

# Preconditions / Precondiciones


class SuccessBabelExtension ( SuccessExtension ) :
  """
  Babel extension for the Success framework.

  Integrates Flask-Babel for internationalization (i18n)
  and localization (l10n) support.
  """


  def __init__ ( self, app : Flask ) -> None :
    """
    Initialize the Babel extension.

    Args:
      app: Flask application instance.
    """
    super ().__init__ ( app )
    self._extension = Babel ()
