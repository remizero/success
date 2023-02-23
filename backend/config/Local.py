# Python Libraries / Librerías Python
import os


# Application Libraries / Librerías de la Aplicación
from config         import Default
from config.Default import EnvVar


# Preconditions / Precondiciones

# TODO Ajustar las configuraciones adecuadas para el modo local
class Local ( Default ) :

  APP_HOST = os.environ.get ( 'APP_HOST' )
