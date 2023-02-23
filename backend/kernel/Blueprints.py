# Python Libraries / Librerías Python
from flask import Flask


# Application Libraries / Librerías de la Aplicación
from app.apis.success.user.auth   import signinBp
from app.apis.success.user.create import userCreateBp


# Preconditions / Precondiciones


class Blueprints () :

  @staticmethod
  def register ( _app : Flask ) -> None :
    _app.register_blueprint ( signinBp )
    _app.register_blueprint ( userCreateBp )

