# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from extensions.Cors        import Cors
from extensions.Database    import Database
from extensions.Email       import Email
from extensions.Jwt         import Jwt
from extensions.Marshmallow import Marshmallow
from extensions.Redis       import Redis
from extensions.Session     import Session
from utils                  import EnvVar


# Preconditions / Precondiciones
"""
  DEFINITION OF CORS POLICIES TO WORK WITH THE FLASK APPLICATION /
  DEFINICION DE POLITICAS CORS PARA TRABAJAR CON LA APLICACION FLASK
"""
cors = None
if ( EnvVar.isTrue ( 'SUCCESS_EXTENSION_CORS' ) ) :
  cors = Cors ()


"""
  CONFIGURATION FOR HANDLING SQLALCHEMY /
  CONFIGURACIÓN PARA EL MANEJO DE SQLALCHEMY
"""
database = None
if ( EnvVar.isTrue ( 'SUCCESS_EXTENSION_SQLALCHEMY' ) ) :
  database = Database ()


"""
  MAIL MODULE CREATION /
  CREACION DEL MODULO DE CORREO
"""
email = None
if ( EnvVar.isTrue ( 'SUCCESS_EXTENSION_EMAIL' ) ) :
  email = Email ()


"""
  CREATION OF JSON WEB TOKEN MANAGER /
  CREACION DEL JSON WEB TOKEN MANAGER
"""
jwt = None
if ( EnvVar.isTrue ( 'SUCCESS_EXTENSION_JWT' ) ) :
  jwt = Jwt ()


"""
  MAIL MODULE CREATION /
  CREACION DEL MODULO DE CORREO
"""
marshmallow = None
if ( EnvVar.isTrue ( 'SUCCESS_EXTENSION_MARSHMALLOW' ) ) :
  marshmallow = Marshmallow ()


"""
  REDIS CONFIGURATION TO WORK WITH THE FLASK APPLICATION /
  CONFIGURACIÓN DE REDIS PARA TRABAJAR CON LA APLICACION FLASK
"""
redis = None
if ( EnvVar.isTrue ( 'SUCCESS_EXTENSION_REDIS' ) ) :
  redis = Redis ()


"""
  SESSION CONFIGURATION TO WORK WITH THE FLASK APPLICATION /
  CONFIGURACIÓN DE SESIÓN PARA TRABAJAR CON LA APLICACION FLASK
"""
session = None
if ( EnvVar.isTrue ( 'SUCCESS_EXTENSION_SESSION' ) ) :
  session = Session ()
