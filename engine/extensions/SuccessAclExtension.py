# Python Libraries / Librerías Python
from flask           import Flask
from flask_principal import Principal

# Success Libraries / Librerías Success
from success.common.base.SuccessExtension import SuccessExtension
from success.common.tools.SuccessEnv      import SuccessEnv

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessAclExtension ( SuccessExtension ) :


  def __init__ ( self, app : Flask ) -> None :
    super ().__init__ ( app )
    self._extension = Principal ()
