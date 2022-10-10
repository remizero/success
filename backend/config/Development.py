# Python Libraries / Librerías Python
import os


# Application Libraries / Librerías de la Aplicación
from . import Default
from utils import EnvVar


# Preconditions / Precondiciones

# TODO Ajustar las configuraciones adecuadas para el modo development
class Development ( Default ) :

  # ----------------------------------------------------------
  # Application Configuration / Configuración de la Aplicación
  # ----------------------------------------------------------
  APP_ENV = EnvVar.get ( 'APP_ENV' )
  APP_HOST = EnvVar.get ( 'APP_HOST' )
  APP_PORT = EnvVar.get ( 'APP_PORT' )
  BASE_URL = EnvVar.get ( 'BASE_URL' )
  DEBUG = EnvVar.isTrue ( 'DEBUG' )
  SECRET_KEY = EnvVar.get ( 'SECRET_KEY' )
  API_KEY = EnvVar.get ( 'API_KEY' )
  STAGING = EnvVar.isTrue ( 'STAGING' )
  TESTING = EnvVar.isTrue ( 'TESTING' )

  # -------------------------------------------------
  # Blueprint Configuration / Configuración Blueprint
  # -------------------------------------------------


  # ---------------------------------------
  # Cors Configuration / Configuración Cors
  # ---------------------------------------
  CORS_ALLOW_HEADERS = EnvVar.get ( 'CORS_ALLOW_HEADERS' )
  CORS_ALWAYS_SEND = EnvVar.isTrue ( 'CORS_ALWAYS_SEND' )
  CORS_AUTOMATIC_OPTIONS = EnvVar.isTrue ( 'CORS_AUTOMATIC_OPTIONS' )
  CORS_EXPOSE_HEADERS = EnvVar.get ( 'CORS_EXPOSE_HEADERS' )
  CORS_INTERCEPT_EXCEPTIONS = EnvVar.isTrue ( 'CORS_INTERCEPT_EXCEPTIONS' )
  CORS_MAX_AGE = EnvVar.get ( 'CORS_MAX_AGE' )
  CORS_METHODS = EnvVar.get ( 'CORS_METHODS' )
  CORS_ORIGINS = EnvVar.get ( 'CORS_ORIGINS' )
  CORS_RESOURCES = EnvVar.get ( 'CORS_RESOURCES' )
  CORS_SEND_WILDCARD = EnvVar.isTrue ( 'CORS_SEND_WILDCARD' )
  CORS_SUPPORTS_CREDENTIALS = EnvVar.isTrue ( 'CORS_SUPPORTS_CREDENTIALS' )
  CORS_VARY_HEADER = EnvVar.isTrue ( 'CORS_VARY_HEADER' )
  # ---------------------------------------------------------
  # Cors Opcional Configuration / Configuración Opcional Cors
  # ---------------------------------------------------------
  CORS_RESOURCES_APP_RESOURCES = EnvVar.get ( 'CORS_RESOURCES_APP_RESOURCES' )
  CORS_RESOURCES_APP_ORIGINS = EnvVar.get ( 'CORS_RESOURCES_APP_ORIGINS' )
  CORS_RESOURCES_APP_METHODS = EnvVar.get ( 'CORS_RESOURCES_APP_METHODS' )
  CORS_RESOURCES_APP_ALLOW_HEADERS = EnvVar.get ( 'CORS_RESOURCES_APP_ALLOW_HEADERS' )
  CORS_RESOURCES_APP_EXPOSE_HEADERS = EnvVar.get ( 'CORS_RESOURCES_APP_EXPOSE_HEADERS' )


  # -----------------------------------------
  # Flask Configuration / Configuración Flask
  # -----------------------------------------
  # - Project name.
  # FLASK_APP = EnvVar.get ( 'FLASK_APP' )
  # - Controls the environment.
  FLASK_ENV = EnvVar.get ( 'FLASK_ENV' )
  #  - Enables debug mode.
  FLASK_DEBUG = EnvVar.isTrue ( 'FLASK_DEBUG' )
  # - A list of files that will be watched by the reloader in addition to the Python modules.
  # FLASK_RUN_EXTRA_FILES = EnvVar.get ( 'FLASK_RUN_EXTRA_FILES' )
  # - The host you want to bind your app to.
  # FLASK_RUN_HOST = EnvVar.get ( 'FLASK_RUN_HOST' )
  # - The port you want to use.
  # FLASK_RUN_PORT = EnvVar.get ( 'FLASK_RUN_PORT' )
  # - A certificate file for so your app can be run with HTTPS.
  # FLASK_RUN_CERT = EnvVar.get ( 'FLASK_RUN_CERT' )
  # - The key file for your cert.
  # FLASK_RUN_KEY = EnvVar.get ( 'FLASK_RUN_KEY' )



  # ---------------------------------------
  # JWT Configuration / Configuración JWT
  # ---------------------------------------
  JWT_ACCESS_COOKIE_NAME = EnvVar.get ( 'JWT_ACCESS_COOKIE_NAME' )
  JWT_ACCESS_COOKIE_PATH = EnvVar.get ( 'JWT_ACCESS_COOKIE_PATH' )
  # JWT_ACCESS_CSRF_COOKIE_NAME = EnvVar.get ( 'JWT_ACCESS_CSRF_COOKIE_NAME' )
  # JWT_ACCESS_CSRF_COOKIE_PATH = EnvVar.get ( 'JWT_ACCESS_CSRF_COOKIE_PATH' )
  # JWT_ACCESS_CSRF_FIELD_NAME = EnvVar.get ( 'JWT_ACCESS_CSRF_FIELD_NAME' )
  JWT_ACCESS_CSRF_HEADER_NAME = EnvVar.get ( 'JWT_ACCESS_CSRF_HEADER_NAME' )
  JWT_ACCESS_TOKEN_EXPIRES = EnvVar.get ( 'JWT_ACCESS_TOKEN_EXPIRES' )
  # JWT_ALGORITHM = EnvVar.get ( 'JWT_ALGORITHM' )
  JWT_BLOCKLIST_ENABLED = EnvVar.isTrue ( 'JWT_BLOCKLIST_ENABLED' )
  JWT_BLOCKLIST_TOKEN_CHECKS = EnvVar.get ( 'JWT_BLOCKLIST_TOKEN_CHECKS' )
  JWT_COOKIE_CSRF_PROTECT = EnvVar.isTrue ( 'JWT_COOKIE_CSRF_PROTECT' )
  JWT_COOKIE_DOMAIN = EnvVar.get ( 'JWT_COOKIE_DOMAIN' )
  # JWT_COOKIE_SAMESITE = EnvVar.get ( 'JWT_COOKIE_SAMESITE' )
  JWT_COOKIE_SECURE = EnvVar.isTrue ( 'JWT_COOKIE_SECURE' )
  JWT_CSRF_CHECK_FORM = EnvVar.isTrue ( 'JWT_CSRF_CHECK_FORM' )
  # JWT_CSRF_IN_COOKIES = EnvVar.isTrue ( 'JWT_CSRF_IN_COOKIES' )
  JWT_CSRF_METHODS = EnvVar.get ( 'JWT_CSRF_METHODS' )
  # JWT_DECODE_ALGORITHMS = EnvVar.get ( 'JWT_DECODE_ALGORITHMS' )
  # JWT_DECODE_AUDIENCE = EnvVar.get ( 'JWT_DECODE_AUDIENCE' )
  # JWT_DECODE_ISSUER = EnvVar.get ( 'JWT_DECODE_ISSUER' )
  # JWT_DECODE_LEEWAY = EnvVar.get ( 'JWT_DECODE_LEEWAY' )
  # JWT_ENCODE_AUDIENCE = EnvVar.get ( 'JWT_ENCODE_AUDIENCE' )
  # JWT_ENCODE_ISSUER = EnvVar.get ( 'JWT_ENCODE_ISSUER' )
  JWT_ERROR_MESSAGE_KEY = EnvVar.get ( 'JWT_ERROR_MESSAGE_KEY' )
  # JWT_HEADER_NAME = EnvVar.get ( 'JWT_HEADER_NAME' )
  # JWT_HEADER_TYPE = EnvVar.get ( 'JWT_HEADER_TYPE' )
  # JWT_IDENTITY_CLAIM = EnvVar.get ( 'JWT_IDENTITY_CLAIM' )
  # JWT_JSON_KEY = EnvVar.get ( 'JWT_JSON_KEY' )
  # JWT_PRIVATE_KEY = EnvVar.get ( 'JWT_PRIVATE_KEY' )
  # JWT_PUBLIC_KEY = EnvVar.get ( 'JWT_PUBLIC_KEY' )
  # JWT_QUERY_STRING_NAME = EnvVar.get ( 'JWT_QUERY_STRING_NAME' )
  # JWT_QUERY_STRING_VALUE_PREFIX = EnvVar.get ( 'JWT_QUERY_STRING_VALUE_PREFIX' )
  JWT_REFRESH_COOKIE_NAME = EnvVar.get ( 'JWT_REFRESH_COOKIE_NAME' )
  JWT_REFRESH_COOKIE_PATH = EnvVar.get ( 'JWT_REFRESH_COOKIE_PATH' )
  # JWT_REFRESH_CSRF_COOKIE_NAME = EnvVar.get ( 'JWT_REFRESH_CSRF_COOKIE_NAME' )
  # JWT_REFRESH_CSRF_COOKIE_PATH = EnvVar.get ( 'JWT_REFRESH_CSRF_COOKIE_PATH' )
  # JWT_REFRESH_CSRF_FIELD_NAME = EnvVar.get ( 'JWT_REFRESH_CSRF_FIELD_NAME' )
  JWT_REFRESH_CSRF_HEADER_NAME = EnvVar.get ( 'JWT_REFRESH_CSRF_HEADER_NAME' )
  # JWT_REFRESH_JSON_KEY = EnvVar.get ( 'JWT_REFRESH_JSON_KEY' )
  JWT_REFRESH_TOKEN_EXPIRES = EnvVar.get ( 'JWT_REFRESH_TOKEN_EXPIRES' )
  JWT_SECRET_KEY = EnvVar.get ( 'JWT_SECRET_KEY' )
  # JWT_SESSION_COOKIE = EnvVar.isTrue ( 'JWT_SESSION_COOKIE' )
  JWT_TOKEN_LOCATION = EnvVar.get ( 'JWT_TOKEN_LOCATION' )
  # JWT_ENCODE_NBF = EnvVar.isTrue ( 'JWT_ENCODE_NBF' )


  # ---------------------------------------
  # Logger Configuration / Configuración Logger
  # ---------------------------------------
  LOGGER_ADMIN = EnvVar.get ( 'LOGGER_ADMIN' )
  LOGGER_BACKUP_COUNT = EnvVar.get ( 'LOGGER_BACKUP_COUNT' )
  LOGGER_DIR = EnvVar.get ( 'LOGGER_DIR' )
  LOGGER_FORMAT = EnvVar.get ( 'LOGGER_FORMAT' )
  LOGGER_FORMATER = EnvVar.get ( 'LOGGER_FORMATER' )
  LOGGER_MAIL_PASSWORD = EnvVar.get ( 'LOGGER_MAIL_PASSWORD' )
  LOGGER_MAIL_PORT = int ( EnvVar.get ( 'LOGGER_MAIL_PORT' ) )
  LOGGER_MAIL_SERVER = EnvVar.get ( 'LOGGER_MAIL_SERVER' )
  LOGGER_MAIL_SSL = EnvVar.isTrue ( 'LOGGER_MAIL_SSL' )
  LOGGER_MAIL_TLS = EnvVar.isTrue ( 'LOGGER_MAIL_TLS' )
  LOGGER_MAIL_USERNAME = EnvVar.get ( 'LOGGER_MAIL_USERNAME' )
  LOGGER_MAX_BYTES = int ( EnvVar.get ( 'LOGGER_MAX_BYTES' ) )
  LOGGER_MESSAGE_SUBJECT = EnvVar.get ( 'LOGGER_MESSAGE_SUBJECT' )
  LOGGER_TEMPLATE_FORMAT_MESSAGE = EnvVar.get ( 'LOGGER_TEMPLATE_FORMAT_MESSAGE' )
  LOGGER_TEMPLATE_HTML_ERROR = EnvVar.get ( 'LOGGER_TEMPLATE_HTML_ERROR' )
  LOGGER_TEMPLATE_HTML_EXCEPTION = EnvVar.get ( 'LOGGER_TEMPLATE_HTML_EXCEPTION' )


  # ---------------------------------------
  # Mail Configuration / Configuración Mail
  # ---------------------------------------
  MAIL_SERVER = EnvVar.get ( 'MAIL_SERVER' )
  MAIL_PORT = int ( EnvVar.get ( 'MAIL_PORT' ) )
  MAIL_USE_TLS = EnvVar.isTrue ( 'MAIL_USE_TLS' )
  MAIL_USE_SSL = EnvVar.isTrue ( 'MAIL_USE_SSL' )
  MAIL_DEBUG = EnvVar.isTrue ( 'MAIL_DEBUG' )
  MAIL_USERNAME = EnvVar.get ( 'MAIL_USERNAME' )
  MAIL_PASSWORD = EnvVar.get ( 'MAIL_PASSWORD' )
  MAIL_DEFAULT_SENDER = EnvVar.get ( 'MAIL_DEFAULT_SENDER' )
  MAIL_MAX_EMAILS = int ( EnvVar.get ( 'MAIL_MAX_EMAILS' ) )
  #MAIL_SUPPRESS_SEND = EnvVar.get ( 'MAIL_SUPPRESS_SEND' )
  MAIL_ASCII_ATTACHMENTS = EnvVar.isTrue ( 'MAIL_ASCII_ATTACHMENTS' )
  # ---------------------------------------------------------
  # Mail Opcional Configuration / Configuración Opcional Mail
  # ---------------------------------------------------------
  MAIL_DONT_REPLY_FROM_EMAIL = EnvVar.get ( 'MAIL_DONT_REPLY_FROM_EMAIL' )


  #  Redis Configuration / Configuración Redis
  REDIS_HOST = EnvVar.get ( 'REDIS_HOST' )
  REDIS_PORT = int ( EnvVar.get ( 'REDIS_PORT' ) )
  REDIS_DB = int ( EnvVar.get ( 'REDIS_DB' ) )
  REDIS_DECODE_RESPONSES = EnvVar.isTrue ( 'REDIS_DECODE_RESPONSES' )

  # host="localhost",
  # port=6379,
  # db=0,
  # password=EnvVar.get ( 'asdf' ),
  # socket_timeout=EnvVar.get ( 'asdf' ),
  # socket_connect_timeout=EnvVar.get ( 'asdf' ),
  # socket_keepalive=EnvVar.isTrue ( 'asdf' ),
  # socket_keepalive_options=EnvVar.get ( 'asdf' ),
  # socket_type=0,
  # retry_on_timeout=EnvVar.isTrue ( 'asdf' ),
  # retry_on_error=SENTINEL,
  # encoding="utf-8",
  # encoding_errors="strict",
  # decode_responses=EnvVar.isTrue ( 'asdf' ),
  # parser_class=DefaultParser,
  # socket_read_size=65536,
  # health_check_interval=0,
  # client_name=EnvVar.get ( 'asdf' ),
  # username=EnvVar.get ( 'asdf' ),
  # retry=EnvVar.get ( 'asdf' ),
  # redis_connect_func=EnvVar.get ( 'asdf' )


  # ---------------------------------------------
  # Restful Configuration / Configuración Restful
  # ---------------------------------------------


  # -----------------------------------------------
  # Session Configuration / Configuración de Sesión
  # -----------------------------------------------
  SESSION_COOKIE_NAME = EnvVar.get ( 'SESSION_COOKIE_NAME' )
  SESSION_COOKIE_DOMAIN = EnvVar.get ( 'SESSION_COOKIE_DOMAIN' )
  SESSION_COOKIE_PATH = EnvVar.get ( 'SESSION_COOKIE_PATH' )
  SESSION_COOKIE_HTTPONLY = EnvVar.get ( 'SESSION_COOKIE_HTTPONLY' )
  SESSION_COOKIE_SECURE = EnvVar.get ( 'SESSION_COOKIE_SECURE' )
  PERMANENT_SESSION_LIFETIME = EnvVar.get ( 'PERMANENT_SESSION_LIFETIME' )
  SESSION_TYPE = EnvVar.get ( 'SESSION_TYPE' )
  SESSION_PERMANENT = EnvVar.get ( 'SESSION_PERMANENT' )
  SESSION_USE_SIGNER = EnvVar.get ( 'SESSION_USE_SIGNER' )
  SESSION_KEY_PREFIX = EnvVar.get ( 'SESSION_KEY_PREFIX' )
  SESSION_REDIS = EnvVar.get ( 'SESSION_REDIS' )
  SESSION_MEMCACHED = EnvVar.get ( 'SESSION_MEMCACHED' )
  SESSION_FILE_DIR = EnvVar.get ( 'SESSION_FILE_DIR' )
  SESSION_FILE_THRESHOLD = EnvVar.get ( 'SESSION_FILE_THRESHOLD' )
  SESSION_FILE_MODE = EnvVar.get ( 'SESSION_FILE_MODE' )
  SESSION_MONGODB = EnvVar.get ( 'SESSION_MONGODB' )
  SESSION_MONGODB_DB = EnvVar.get ( 'SESSION_MONGODB_DB' )
  SESSION_MONGODB_COLLECT = EnvVar.get ( 'SESSION_MONGODB_COLLECT' )
  SESSION_SQLALCHEMY = EnvVar.get ( 'SESSION_SQLALCHEMY' )
  SESSION_SQLALCHEMY_TABLE = EnvVar.get ( 'SESSION_SQLALCHEMY_TABLE' )


  # ---------------------------------------------------
  # SqlAlchemy Configuration / Configuración SqlAlchemy
  # ---------------------------------------------------
  SQLALCHEMY_DATABASE_URI = '{driver}://{user}:{pw}@{url}:{port}/{db}'.format (
      driver = EnvVar.get ( 'SQLALCHEMY_DB_DRIVER' ),
      user = EnvVar.get ( 'SQLALCHEMY_DB_USER' ),
      pw = EnvVar.get ( 'SQLALCHEMY_DB_PASSWORD' ),
      url = EnvVar.get ( 'SQLALCHEMY_DB_HOST' ),
      port = EnvVar.get ( 'SQLALCHEMY_DB_PORT' ),
      db = EnvVar.get ( 'SQLALCHEMY_DB_NAME' )
    )
  SQLALCHEMY_BINDS = EnvVar.get ( 'SQLALCHEMY_BINDS' )
  SQLALCHEMY_ECHO = EnvVar.isTrue ( 'SQLALCHEMY_ECHO' )
  SQLALCHEMY_RECORD_QUERIES = EnvVar.isTrue ( 'SQLALCHEMY_RECORD_QUERIES' )
  SQLALCHEMY_COMMIT_ON_TEARDOWN = EnvVar.isTrue ( 'SQLALCHEMY_COMMIT_ON_TEARDOWN' )
  SQLALCHEMY_TRACK_MODIFICATIONS = EnvVar.isTrue ( 'SQLALCHEMY_TRACK_MODIFICATIONS' )
  SQLALCHEMY_ENGINE_OPTIONS = EnvVar.get ( 'SQLALCHEMY_ENGINE_OPTIONS' )
  # ------------------------------------------------------------------------------------------------------------------------------------
  # additional sqlalchemy configuration for database connection / configuración adicional sqlalchemy para la conexión a la base de datos
  # ------------------------------------------------------------------------------------------------------------------------------------
  SQLALCHEMY_DB_DRIVER = EnvVar.get ( 'SQLALCHEMY_DB_DRIVER' )
  SQLALCHEMY_DB_HOST = EnvVar.get ( 'SQLALCHEMY_DB_HOST' )
  SQLALCHEMY_DB_PORT = int ( EnvVar.get ( 'SQLALCHEMY_DB_PORT' ) )
  SQLALCHEMY_DB_NAME = EnvVar.get ( 'SQLALCHEMY_DB_NAME' )
  SQLALCHEMY_DB_USER = EnvVar.get ( 'SQLALCHEMY_DB_USER' )
  SQLALCHEMY_DB_PASSWORD = EnvVar.get ( 'SQLALCHEMY_DB_PASSWORD' )
  SQLALCHEMY_TABLENAME_SUCCESS_MODEL = EnvVar.isTrue ( 'SQLALCHEMY_TABLENAME_SUCCESS_MODEL' )


  # ---------------------------------------
  #  Configuration / Configuración 
  # ---------------------------------------
