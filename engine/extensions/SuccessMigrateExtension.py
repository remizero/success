# Python Libraries / Librerías Python
from flask         import Flask
from flask_migrate import Migrate

# Success Libraries / Librerías Success
from success.common.base.SuccessExtension import SuccessExtension

# Preconditions / Precondiciones


class SuccessMigrateExtension ( SuccessExtension ) :
  """
  Database Migrate extension for the Success framework.

  Integrates Flask-Migrate for database migration management
  using Alembic.
  """


  def __init__ ( self, app : Flask ) -> None :
    """
    Initialize the Migrate extension.

    Args:
      app: Flask application instance.
    """
    super ().__init__ ( app )
    self._extension = Migrate ()
