# Python Libraries / Librerías Python
from flask          import Flask
from flask_security import Security
from flask_security import UserDatastore

# Success Libraries / Librerías Success
from success.common.base.SuccessExtension import SuccessExtension
from success.common.tools.SuccessEnv      import SuccessEnv

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessSecurityExtension ( SuccessExtension ) :


  def __init__ ( self, app : Flask ) -> None :
    super ().__init__ ( app )
    # self._extension = Security ()


  def register ( self ) -> None :
    # if self._extension and hasattr ( self._extension, "init_app" ) :
    #   self._extension.init_app ( self._app, UserDatastore () )
    pass
