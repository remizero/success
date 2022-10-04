# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from extensions import Blueprint
from kernel import restful


# Preconditions / Precondiciones
adminBp = Blueprint ( 'admin', __name__, '/admin' )
#restful.extension.