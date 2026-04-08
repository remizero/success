# Python Libraries / Librerías Python
from flask            import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy       import MetaData
from sqlalchemy.orm   import relationship

# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessExtension import SuccessExtension
from success.common.tools.SuccessEnv      import SuccessEnv

# Preconditions / Precondiciones


class SuccessDatabaseExtension ( SuccessExtension ) :


  def __init__ ( self, app : Flask ) -> None :
    super ().__init__ ( app )
    self._extension = SQLAlchemy ()


  def metadata ( self ) -> MetaData :
    metadata = MetaData ()
    metadata.reflect ( self._extension.engine )
    return metadata
