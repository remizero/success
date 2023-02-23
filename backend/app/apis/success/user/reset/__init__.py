# Python Libraries / Librerías Python
from flask         import Blueprint
from flask_restful import Api


# Application Libraries / Librerías de la Aplicación
from app.apis.success.user.reset.Endpoint import Endpoint
from app.apis.success.user.reset.Input    import Input
from app.apis.success.user.reset.Output   import Output


# Preconditions / Precondiciones
userResetBp = Blueprint ( 'userReset', __name__ )
restful        = Api ( userResetBp )
restful.add_resource ( Endpoint, '/user/reset' )
