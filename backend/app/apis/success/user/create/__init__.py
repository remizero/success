# Python Libraries / Librerías Python
from flask import Blueprint
from flask_restful import Api


# Application Libraries / Librerías de la Aplicación
from .Endpoint import Endpoint
from .Input import Input
from .Output import Output


# Preconditions / Precondiciones
userCreateBp = Blueprint ( 'userCreate', __name__ )
restful = Api ( userCreateBp )
restful.add_resource ( Endpoint, '/user/create' )
