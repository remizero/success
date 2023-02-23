# Python Libraries / Librerías Python
from flask         import Blueprint
from flask_restful import Api


# Application Libraries / Librerías de la Aplicación
from app.apis.success.user.update.Endpoint import Endpoint
from app.apis.success.user.update.Input    import Input
from app.apis.success.user.update.Output   import Output


# Preconditions / Precondiciones
userUpdateBp = Blueprint ( 'userUpdateBp', __name__ )
restful      = Api ( userUpdateBp )
restful.add_resource ( Endpoint, '/user/update' )
