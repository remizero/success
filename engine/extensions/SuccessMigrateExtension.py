# Python Libraries / Librerías Python
from flask         import Flask
from flask_migrate import Migrate

# Success Libraries / Librerías Success
from success.common.base.SuccessExtension import SuccessExtension
from success.common.tools.SuccessEnv      import SuccessEnv

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessMigrateExtension ( SuccessExtension ) :


  def __init__ ( self, app : Flask ) -> None :
    super ().__init__ ( app )
    self._extension = Migrate ()
