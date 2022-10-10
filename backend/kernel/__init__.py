# Python Libraries / Librerías Python
from flask import Flask


# Application Libraries / Librerías de la Aplicación
#from .Importer import Importer
from .Debug import Debug
from .Config import Config
from .LoggerMailer import LoggerMailer
from .Logger import Logger
# from .App import App
from .Exception import Exception
from .Extension import Extension
from .Blueprints import Blueprints
#from .Response import Response
from extensions import (
  cors,
  database,
  email,
  jwt,
  session
)
from utils import (
  Application,
  File
)


# Preconditions / Precondiciones
"""
  DEFINITION OF CONFIGURATION POLICIES TO WORK WITH THE SUCCESS APPLICATION /
  DEFINICION DE POLITICAS DE CONFIGURACION PARA TRABAJAR CON LA APLICACION SUCCESS
"""
config = Config ()


class Success () :

  @staticmethod
  def create () :
    """
      CREATION OF THE FLASK APPLICATION /
      CREACION DE LAS APLICACION FLASK
    """
    #app = App ( __name__, instance_relative_config = True )
    app = Flask ( __name__, instance_relative_config = True )
    app.config.from_object ( Application.getConfigClass ( config ) )
    app.config.from_pyfile ( Application.getConfigFile (), silent = True )
    email.register ( app )
    # ---------------------------------------
    # AQUI DEBERIA IR LA CLASE LOGGER
    # ---------------------------------------
    cors.register ( app )
    jwt.register ( app )
    session.register ( app )
    database.register ( app )
    """
      CONFIGURATION FOR HANDLING CORE SYSTEM ROUTES /
      CONFIGURACIÓN PARA EL MANEJO DE LAS RUTAS DEL SISTEMA CORE
    """
    Blueprints.register ( app )
    return app
