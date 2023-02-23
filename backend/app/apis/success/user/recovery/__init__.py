# Python Libraries / Librerías Python
from flask         import Blueprint
from flask_restful import Api


# Application Libraries / Librerías de la Aplicación
from app.apis.success.user.recovery.Endpoint import Endpoint
from app.apis.success.user.recovery.Input    import Input
from app.apis.success.user.recovery.Output   import Output


# Preconditions / Precondiciones
userRecoveryBp = Blueprint ( 'userRecovery', __name__ )
restful        = Api ( userRecoveryBp )
restful.add_resource ( Endpoint, '/user/recovery' )
