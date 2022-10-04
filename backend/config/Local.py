# Python Libraries / Librerías Python
import os


# Application Libraries / Librerías de la Aplicación
from . import Default


# Preconditions / Precondiciones

# TODO Ajustar las configuraciones adecuadas para el modo local
class Local ( Default ) :

  APP_HOST = os.environ.get ( 'APP_HOST' )
