# Python Libraries / Librerías Python
from flask            import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy       import MetaData
from sqlalchemy.orm   import relationship

# Success Libraries / Librerías Success
from success.common.base.SuccessExtension                   import SuccessExtension
from success.engine.extensions.proxies.SuccessProxyDatabase import db

# Preconditions / Precondiciones


class SuccessDatabaseExtension ( SuccessExtension ) :
  """
  Database extension for the Success framework.

  Integrates Flask-SQLAlchemy for database operations
  and ORM functionality.
  """


  def __init__ ( self, app : Flask ) -> None :
    """
    Initialize the Database extension.

    Args:
      app: Flask application instance.
    """
    super ().__init__ ( app )
    self._extension = db


  def metadata ( self ) -> MetaData :
    """
    Get and reflect database metadata.

    Returns:
      MetaData: Reflected database metadata.
    """
    metadata = MetaData ()
    metadata.reflect ( self._extension.engine )
    return metadata
