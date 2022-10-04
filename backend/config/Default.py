# Python Libraries / Librerías Python
from datetime import timedelta
import os


# Application Libraries / Librerías de la Aplicación
from kernel import Config


# Preconditions / Precondiciones

# TODO Ajustar las configuraciones adecuadas para el modo default
class Default ( Config ) :
  # os.environ.get ( '' )
  # Application Configuration / Configuración Aplicacion
  APP_HOST = os.environ.get ( 'APP_HOST' )
  APP_PORT = os.environ.get ( 'APP_PORT' )
  BASE_URL = os.environ.get ( 'BASE_URL' )
  DEBUG = os.environ.get ( 'DEBUG' )
  SECRET_KEY = os.environ.get ( 'SECRET_KEY' )
  API_KEY = os.environ.get ( 'API_KEY' )


  # Blueprint Configuration / Configuración Blueprint


  # Cors Configuration / Configuración Cors
  CORS_ALLOW_HEADERS = os.environ.get ( 'CORS_ALLOW_HEADERS' )
  CORS_ALWAYS_SEND = os.environ.get ( 'CORS_ALWAYS_SEND' )
  CORS_AUTOMATIC_OPTIONS = os.environ.get ( 'CORS_AUTOMATIC_OPTIONS' )
  CORS_EXPOSE_HEADERS = os.environ.get ( 'CORS_EXPOSE_HEADERS' )
  CORS_INTERCEPT_EXCEPTIONS = os.environ.get ( 'CORS_INTERCEPT_EXCEPTIONS' )
  CORS_MAX_AGE = os.environ.get ( 'CORS_MAX_AGE' )
  CORS_METHODS = os.environ.get ( 'CORS_METHODS' )
  CORS_ORIGINS = os.environ.get ( 'CORS_ORIGINS' )
  CORS_RESOURCES = os.environ.get ( 'CORS_RESOURCES' )
  CORS_SEND_WILDCARD = os.environ.get ( 'CORS_SEND_WILDCARD' )
  CORS_SUPPORTS_CREDENTIALS = os.environ.get ( 'CORS_SUPPORTS_CREDENTIALS' )
  CORS_VARY_HEADER = os.environ.get ( 'CORS_VARY_HEADER' )


  # Flask Configuration / Configuración Flask


  # JWT Configuration / Configuración JWT

  JWT_BLOCKLIST_ENABLED = os.environ.get ( 'JWT_BLOCKLIST_ENABLED' )
  JWT_BLOCKLIST_TOKEN_CHECKS = os.environ.get ( 'JWT_BLOCKLIST_TOKEN_CHECKS' )
  # Set the secret key to sign the JWTs with
  JWT_SECRET_KEY = os.environ.get ( 'JWT_SECRET_KEY' )
  # Se define el índice que devolverá los errores generados para la sesión
  JWT_ERROR_MESSAGE_KEY = os.environ.get ( 'JWT_ERROR_MESSAGE_KEY' )
  # Se define el tiempo de duración del token de acceso
  JWT_ACCESS_TOKEN_EXPIRES = timedelta ( seconds = 86400 )
  # Se define el tiempo de duración del token de reingreso o relogin
  JWT_REFRESH_TOKEN_EXPIRES = timedelta ( seconds = 86400 )
  # Configure application to store JWTs in cookies
  JWT_TOKEN_LOCATION = os.environ.get ( 'JWT_TOKEN_LOCATION' )
  # Se define el dominio sobre el cual se crearan las cookies
  # HABILITAR SOLO PARA MODO DE DESARROLLO EN LOCAL
  JWT_COOKIE_DOMAIN = os.environ.get ( 'JWT_COOKIE_DOMAIN' )
  # HABILITAR PARA MODO STAGING Y/O PRODUCCION
  JWT_COOKIE_DOMAIN = os.environ.get ( 'JWT_COOKIE_DOMAIN' )
  # Set the cookie paths
  JWT_ACCESS_COOKIE_PATH = os.environ.get ( 'JWT_ACCESS_COOKIE_PATH' )
  JWT_REFRESH_COOKIE_PATH = os.environ.get ( 'JWT_REFRESH_COOKIE_PATH' )
  # Only allow JWT cookies to be sent over https. In production, this should likely be True
  JWT_COOKIE_SECURE = os.environ.get ( 'JWT_COOKIE_SECURE' )
  # Enable csrf double submit protection.
  JWT_COOKIE_CSRF_PROTECT = os.environ.get ( 'JWT_COOKIE_CSRF_PROTECT' )
  # Set allowed methods for csrf
  JWT_CSRF_METHODS = os.environ.get ( 'JWT_CSRF_METHODS' )
  # Set header access name for csrf
  JWT_ACCESS_CSRF_HEADER_NAME = os.environ.get ( 'JWT_ACCESS_CSRF_HEADER_NAME' )
  # Set header refresh name for csrf
  JWT_REFRESH_CSRF_HEADER_NAME = os.environ.get ( 'JWT_REFRESH_CSRF_HEADER_NAME' )
  # Set a new name to token cookies
  JWT_ACCESS_COOKIE_NAME = os.environ.get ( 'JWT_ACCESS_COOKIE_NAME' )
  JWT_REFRESH_COOKIE_NAME = os.environ.get ( 'JWT_REFRESH_COOKIE_NAME' )
  # Set csrf check form
  JWT_CSRF_CHECK_FORM = os.environ.get ( 'JWT_CSRF_CHECK_FORM' )


  # Mail Configuration / Configuración Mail
  MAIL_SERVER = os.environ.get ( 'MAIL_SERVER' )
  MAIL_PORT = os.environ.get ( 'MAIL_PORT' )
  MAIL_USERNAME = os.environ.get ( 'MAIL_USERNAME' )
  MAIL_PASSWORD = os.environ.get ( 'MAIL_PASSWORD' )
  MAIL_USE_TLS = os.environ.get ( 'MAIL_USE_TLS' )
  MAIL_USE_SSL = os.environ.get ( 'MAIL_USE_SSL' )
  MAIL_DONT_REPLY_FROM_EMAIL = os.environ.get ( 'DONT_REPLY_FROM_EMAIL' )
  MAIL_ADMINS = os.environ.get ( 'ADMINS' )


  # Restful Configuration / Configuración Restful


  # Session Configuration / Configuración de sesion
  SESSION_TYPE = os.environ.get ( 'SESSION_TYPE' )
  SESSION_PERMANENT = os.environ.get ( 'SESSION_PERMANENT' )
  PERMANENT_SESSION_LIFETIME = os.environ.get ( 'PERMANENT_SESSION_LIFETIME' )
  SESSION_COOKIE_NAME = os.environ.get ( 'SESSION_COOKIE_NAME' )
  SESSION_COOKIE_DOMAIN = os.environ.get ( 'SESSION_COOKIE_DOMAIN' )
  SESSION_COOKIE_PATH = os.environ.get ( 'SESSION_COOKIE_PATH' )
  SESSION_COOKIE_HTTPONLY = os.environ.get ( 'SESSION_COOKIE_HTTPONLY' )
  SESSION_COOKIE_SECURE = os.environ.get ( 'SESSION_COOKIE_SECURE' )
  SESSION_KEY_PREFIX = os.environ.get ( 'SESSION_KEY_PREFIX' )
  SESSION_REDIS = os.environ.get ( 'SESSION_REDIS' )
  SESSION_MEMCACHED = os.environ.get ( 'SESSION_MEMCACHED' )
  SESSION_FILE_DIR = os.environ.get ( 'SESSION_FILE_DIR' )
  SESSION_FILE_THRESHOLD = os.environ.get ( 'SESSION_FILE_THRESHOLD' )
  SESSION_FILE_MODE = os.environ.get ( 'SESSION_FILE_MODE' )
  SESSION_SQLALCHEMY = os.environ.get ( 'SESSION_SQLALCHEMY' )
  SESSION_SQLALCHEMY_TABLE = os.environ.get ( 'SESSION_SQLALCHEMY_TABLE' )


  # SqlAlchemy Configuration / Configuración SqlAlchemy
  SQLALCHEMY_DATABASE_URI = '{driver}://{user}:{pw}@{host}:{port}/{db}'.format (
    driver = os.environ.get ( 'DB_DRIVER' ),
    user = os.environ.get ( 'DB_USER' ),
    pw = os.environ.get ( 'DB_PASSWORD' ),
    host = os.environ.get ( 'DB_HOST' ),
    port = os.environ.get ( 'DB_PORT' ),
    db = os.environ.get ( 'DB_NAME' )
  )
  SQLALCHEMY_BINDS = os.environ.get ( 'SQLALCHEMY_BINDS' )
  SQLALCHEMY_ECHO = os.environ.get ( 'SQLALCHEMY_ECHO' )
  SQLALCHEMY_RECORD_QUERIES = os.environ.get ( 'SQLALCHEMY_RECORD_QUERIES' )
  SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get ( 'SQLALCHEMY_TRACK_MODIFICATIONS' )
  SQLALCHEMY_ENGINE_OPTIONS = os.environ.get ( 'SQLALCHEMY_ENGINE_OPTIONS' )
  DB_DRIVER = os.environ.get ( 'DB_DRIVER' )
  DB_HOST = os.environ.get ( 'DB_HOST' )
  DB_PORT = os.environ.get ( 'DB_PORT' )
  DB_NAME = os.environ.get ( 'DB_NAME' )
  DB_USER = os.environ.get ( 'DB_USER' )
  DB_PASSWORD = os.environ.get ( 'DB_PASSWORD' )


  #  Configuration / Configuración 


  #  Configuration / Configuración 
