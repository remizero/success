# Python Libraries / Librerías Python
from flask import current_app


# Application Libraries / Librerías de la Aplicación
from .Schema import Schema
from .Signin import Signin
from .Validator import Validator
from extensions import Blueprint


# Preconditions / Precondiciones
signinBp = Blueprint ( 'signin', __name__, '/signin' )
#restful.extension.