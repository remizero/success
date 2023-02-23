# Python Libraries / Librerías Python
from flask         import Blueprint
from flask_restful import Api


# Application Libraries / Librerías de la Aplicación
from app.apis.success.user.signout.Endpoint import Endpoint
from app.apis.success.user.signout.Input    import Input
from app.apis.success.user.signout.Output   import Output


# Preconditions / Precondiciones
signoutBp = Blueprint ( 'signout', __name__ )
restful = Api ( signoutBp )
restful.add_resource ( Endpoint, '/signout' )
