# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from .Cors import Cors
from .Database import Database
from .Email import Email
from .Jwt import Jwt
from .Session import Session


# Preconditions / Precondiciones

"""
  DEFINITION OF CORS POLICIES TO WORK WITH THE FLASK APPLICATION /
  DEFINICION DE POLITICAS CORS PARA TRABAJAR CON LA APLICACION FLASK
"""
cors = Cors ()

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
  SESSION CONFIGURATION TO WORK WITH THE FLASK APPLICATION /
  CONFIGURACIÓN DE SESIÓN PARA TRABAJAR CON LA APLICACION FLASK
"""
session = Session ()

"""
  CONFIGURATION FOR HANDLING SQLALCHEMY /
  CONFIGURACIÓN PARA EL MANEJO DE SQLALCHEMY
"""
database = Database ()
