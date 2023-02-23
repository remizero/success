# Python Libraries / Librerías Python
from flask         import Blueprint
from flask_restful import Api


# Application Libraries / Librerías de la Aplicación
from app.apis.success.user.create.Endpoint import Endpoint
from app.apis.success.user.create.Input    import Input
from app.apis.success.user.create.Output   import Output


# Preconditions / Precondiciones
userCreateBp = Blueprint ( 'userCreate', __name__ )
restful      = Api ( userCreateBp )
restful.add_resource ( Endpoint, '/user/create' )
