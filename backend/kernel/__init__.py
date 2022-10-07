# Python Libraries / Librerías Python
import imp
from flask import Flask


# Application Libraries / Librerías de la Aplicación
from .Importer import Importer
from .Debug import Debug
from .Config import Config
from .LoggerMailer import LoggerMailer
from .Logger import Logger
# from .App import App
from .Exception import Exception
from .Extension import Extension
from .Model import Model
#from .Response import Response
from .Validator import Validator
from extensions import (
  # Blueprint,
  Cors,
  Database,
  Email,
  Jwt,
  Restful,
  Routes,
  Session
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

"""
  DEFINITION OF CORS POLICIES TO WORK WITH THE FLASK APPLICATION /
  DEFINICION DE POLITICAS CORS PARA TRABAJAR CON LA APLICACION FLASK
"""
cors = Cors ()

"""
  DEFINITION OF MODULE POLICIES TO WORK WITH THE FLASK APPLICATION /
  DEFINICION DE POLITICAS DE MODULOS PARA TRABAJAR CON LA APLICACION FLASK
"""
#blueprint = Blueprint ()

"""
  CREATION OF JSON WEB TOKEN MANAGER /
  CREACION DEL JSON WEB TOKEN MANAGER
"""
jwt = Jwt ()

"""
  MAIL MODULE CREATION /
  CREACION DEL MODULO DE CORREO
"""
email = Email ()

"""
  DEFINITION OF THE RESTFUL SYSTEM TO WORK WITH THE FLASK APPLICATION /
  DEFINICION DEL SISTEMA RESTFUL PARA TRABAJAR CON LA APLICACION FLASK
"""
restful = Restful ()

"""
  CONFIGURATION FOR HANDLING CORE SYSTEM ROUTES /
  CONFIGURACIÓN PARA EL MANEJO DE LAS RUTAS DEL SISTEMA CORE
"""
routes = Routes ()

"""
  SESSION CONFIGURATION TO WORK WITH THE FLASK APPLICATION /
  CONFIGURACIÓN DE SESIÓN PARA TRABAJAR CON LA APLICACION FLASK
"""
session = Session ()

"""
  CONFIGURATION FOR HANDLING SQLALCHEMY /
  CONFIGURACIÓN PARA EL MANEJO DE SQLALCHEMY
"""
database = Database ()


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
     # Al parecer esto no iria aqui, sino en los modulos donde se encuentran los endpoints
    # blueprint.register ( app )
    jwt.register ( app )
    session.register ( app )
    database.register ( app )
    routes.register ( app, restful.extension )
    restful.register ( app )
    return app
