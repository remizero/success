# Python Libraries / Librerías Python
from flask import Blueprint
from flask_restful import Api


# Application Libraries / Librerías de la Aplicación
from .Endpoint import Endpoint
from .Schema import Schema


# Preconditions / Precondiciones
signinBp = Blueprint ( 'signin', __name__ )
restful = Api ( signinBp )
restful.add_resource ( Endpoint, '/signin' )
