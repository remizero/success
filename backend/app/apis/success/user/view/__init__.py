# Python Libraries / Librerías Python
from flask         import Blueprint
from flask_restful import Api


# Application Libraries / Librerías de la Aplicación
from app.apis.success.user.view.Endpoint import Endpoint
from app.apis.success.user.view.Input    import Input
from app.apis.success.user.view.Output   import Output


# Preconditions / Precondiciones
userViewBp = Blueprint ( 'userViewBp', __name__ )
restful    = Api ( userViewBp )
restful.add_resource ( Endpoint, '/user/view' )
