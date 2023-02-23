# Python Libraries / Librerías Python
from flask         import Blueprint
from flask_restful import Api


# Application Libraries / Librerías de la Aplicación
from app.apis.success.user.list.Endpoint import Endpoint
from app.apis.success.user.list.Input    import Input
from app.apis.success.user.list.Output   import Output


# Preconditions / Precondiciones
userListBp = Blueprint ( 'userList', __name__ )
restful    = Api ( userListBp )
restful.add_resource ( Endpoint, '/user/list' )
