# Python Libraries / Librerías Python
from flask         import Blueprint
from flask_restful import Api


# Application Libraries / Librerías de la Aplicación
from app.apis.success.user.auth.Endpoint import Endpoint
from app.apis.success.user.auth.Input    import Input
from app.apis.success.user.auth.Output   import Output


# Preconditions / Precondiciones
signinBp = Blueprint ( 'signin', __name__ )
restful  = Api ( signinBp )
restful.add_resource ( Endpoint, '/signin' )
