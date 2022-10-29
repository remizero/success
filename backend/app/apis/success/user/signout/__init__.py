# Python Libraries / Librerías Python
from flask import Blueprint
from flask_restful import Api


# Application Libraries / Librerías de la Aplicación
from .Endpoint import Endpoint
from .Input import Input
from .Output import Output


# Preconditions / Precondiciones
signoutBp = Blueprint ( 'signout', __name__ )
restful = Api ( signoutBp )
restful.add_resource ( Endpoint, '/signout' )
