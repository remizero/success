# Python Libraries / Librerías Python
from flask         import Blueprint
from flask_restful import Api


# Application Libraries / Librerías de la Aplicación
from app.apis.success.user.delete.Endpoint import Endpoint
from app.apis.success.user.delete.Input    import Input
from app.apis.success.user.delete.Output   import Output


# Preconditions / Precondiciones
userDeleteBp = Blueprint ( 'userDelete', __name__ )
restful      = Api ( userDeleteBp )
restful.add_resource ( Endpoint, '/user/delete' )
