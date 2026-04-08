# Python Libraries / Librerías Python
from datetime import timedelta

# Application Libraries / Librerías de la Aplicación
from success.common.SuccessDebug                    import SuccessDebug
from success.common.tools.SuccessEnv                import SuccessEnv
from success.common.infra.config.SuccessEnvProvider import SuccessEnvProvider

# Preconditions / Precondiciones


class SuccessConfigExtensions () :


  @staticmethod
  def loadAcl ( env : SuccessEnvProvider ) -> dict :
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_ACL' ) ) ) :
      return {
        
      }
    return {}


  @staticmethod
  def loadBlueprint ( env : SuccessEnvProvider ) -> dict :
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_BLUEPRINT' ) ) ) :
      return {
        
      }
    return {}


  @staticmethod
  def loadCors ( env : SuccessEnvProvider ) -> dict :
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_CORS' ) ) ) :
      return {
        "CORS_ALLOW_HEADERS"                : SuccessEnv.toList ( env.get ( 'CORS_ALLOW_HEADERS' ) ),
        "CORS_ALWAYS_SEND"                  : SuccessEnv.isTrue ( env.get ( 'CORS_ALWAYS_SEND' ) ),
        "CORS_AUTOMATIC_OPTIONS"            : SuccessEnv.isTrue ( env.get ( 'CORS_AUTOMATIC_OPTIONS' ) ),
        "CORS_EXPOSE_HEADERS"               : SuccessEnv.toList ( env.get ( 'CORS_EXPOSE_HEADERS' ) ),
        "CORS_INTERCEPT_EXCEPTIONS"         : SuccessEnv.isTrue ( env.get ( 'CORS_INTERCEPT_EXCEPTIONS' ) ),
        "CORS_MAX_AGE"                      : env.get ( 'CORS_MAX_AGE' ),
        "CORS_METHODS"                      : SuccessEnv.toList ( env.get ( 'CORS_METHODS' ) ),
        "CORS_ORIGINS"                      : env.get ( 'CORS_ORIGINS' ),
        "CORS_RESOURCES"                    : env.get ( 'CORS_RESOURCES' ),
        "CORS_SEND_WILDCARD"                : SuccessEnv.isTrue ( env.get ( 'CORS_SEND_WILDCARD' ) ),
        "CORS_SUPPORTS_CREDENTIALS"         : SuccessEnv.isTrue ( env.get ( 'CORS_SUPPORTS_CREDENTIALS' ) ),
        "CORS_VARY_HEADER"                  : SuccessEnv.isTrue ( env.get ( 'CORS_VARY_HEADER' ) ),
        # ---------------------------------------------------------
        # Cors Opcional Configuration / Configuración Opcional Cors
        # Estas macros son especiales y personalizadas para el correcto manejo de las políticas de Cors en flask para diferentes dominios de manera personalizada.
        # ---------------------------------------------------------
        "CORS_RESOURCES_APP_RESOURCES"      : SuccessEnv.toList ( env.get ( 'CORS_RESOURCES_APP_RESOURCES' ) ),
        "CORS_RESOURCES_APP_ORIGINS"        : SuccessEnv.toList ( env.get ( 'CORS_RESOURCES_APP_ORIGINS' ) ),
        "CORS_RESOURCES_APP_METHODS"        : SuccessEnv.toList ( env.get ( 'CORS_RESOURCES_APP_METHODS' ) ),
        "CORS_RESOURCES_APP_ALLOW_HEADERS"  : SuccessEnv.toList ( env.get ( 'CORS_RESOURCES_APP_ALLOW_HEADERS' ) ),
        "CORS_RESOURCES_APP_EXPOSE_HEADERS" : SuccessEnv.toList ( env.get ( 'CORS_RESOURCES_APP_EXPOSE_HEADERS' ) )
      }
    return {}


  @staticmethod
  def loadJwt ( env : SuccessEnvProvider ) -> dict :
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_JWT' ) ) ) :
      return {
        # Set a new name to token cookies
        "JWT_ACCESS_COOKIE_NAME"        : env.get ( 'JWT_ACCESS_COOKIE_NAME' ),
        # Set the cookie paths
        "JWT_ACCESS_COOKIE_PATH"        : env.get ( 'JWT_ACCESS_COOKIE_PATH' ),
        # "JWT_ACCESS_CSRF_COOKIE_NAME"   : env.get ( 'JWT_ACCESS_CSRF_COOKIE_NAME' ),
        # "JWT_ACCESS_CSRF_COOKIE_PATH"   : env.get ( 'JWT_ACCESS_CSRF_COOKIE_PATH' ),
        # "JWT_ACCESS_CSRF_FIELD_NAME"    : env.get ( 'JWT_ACCESS_CSRF_FIELD_NAME' ),
        # Set header access name for csrf
        "JWT_ACCESS_CSRF_HEADER_NAME"   : env.get ( 'JWT_ACCESS_CSRF_HEADER_NAME' ),
        # Se define el tiempo de duración del token de acceso
        "JWT_ACCESS_TOKEN_EXPIRES"      : SuccessEnv.toInt ( env.get ( 'JWT_ACCESS_TOKEN_EXPIRES' ) ),
        # "JWT_ALGORITHM"                 : env.get ( 'JWT_ALGORITHM' ),
        "JWT_BLOCKLIST_ENABLED"         : SuccessEnv.isTrue ( env.get ( 'JWT_BLOCKLIST_ENABLED' ) ),
        "JWT_BLOCKLIST_TOKEN_CHECKS"    : SuccessEnv.toList ( env.get ( 'JWT_BLOCKLIST_TOKEN_CHECKS' ) ),
        # Enable csrf double submit protection.
        "JWT_COOKIE_CSRF_PROTECT"       : SuccessEnv.isTrue ( env.get ( 'JWT_COOKIE_CSRF_PROTECT' ) ),
        # Se define el dominio sobre el cual se crearan las cookies
        # HABILITAR SOLO PARA MODO DE DESARROLLO EN LOCAL
        # HABILITAR PARA MODO SUCCESS_STAGING Y/O PRODUCCION
        # "JWT_COOKIE_DOMAIN"             : env.get ( 'JWT_COOKIE_DOMAIN' ),
        # "JWT_COOKIE_SAMESITE"           : env.get ( 'JWT_COOKIE_SAMESITE' ),
        # Only allow JWT cookies to be sent over https. In production, this should likely be True
        "JWT_COOKIE_SECURE"             : SuccessEnv.isTrue ( env.get ( 'JWT_COOKIE_SECURE' ) ),
        # Set csrf check form
        "JWT_CSRF_CHECK_FORM"           : SuccessEnv.isTrue ( env.get ( 'JWT_CSRF_CHECK_FORM' ) ),
        # "JWT_CSRF_IN_COOKIES"           : SuccessEnv.isTrue ( env.get ( 'JWT_CSRF_IN_COOKIES' ),
        # Set allowed methods for csrf
        "JWT_CSRF_METHODS"              : SuccessEnv.toList ( env.get ( 'JWT_CSRF_METHODS' ) ),
        # "JWT_DECODE_ALGORITHMS"         : env.get ( 'JWT_DECODE_ALGORITHMS' ),
        # "JWT_DECODE_AUDIENCE"           : env.get ( 'JWT_DECODE_AUDIENCE' ),
        # "JWT_DECODE_ISSUER"             : env.get ( 'JWT_DECODE_ISSUER' ),
        # "JWT_DECODE_LEEWAY"             : SuccessEnv.toInt ( env.get ( 'JWT_DECODE_LEEWAY' ) ),
        # "JWT_ENCODE_AUDIENCE"           : env.get ( 'JWT_ENCODE_AUDIENCE' ),
        # "JWT_ENCODE_ISSUER"             : env.get ( 'JWT_ENCODE_ISSUER' ),
        # Se define el índice que devolverá los errores generados para la sesión
        "JWT_ERROR_MESSAGE_KEY"         : env.get ( 'JWT_ERROR_MESSAGE_KEY' ),
        # "JWT_HEADER_NAME"               : env.get ( 'JWT_HEADER_NAME' ),
        # "JWT_HEADER_TYPE"               : env.get ( 'JWT_HEADER_TYPE' ),
        # "JWT_IDENTITY_CLAIM"            : env.get ( 'JWT_IDENTITY_CLAIM' ),
        # "JWT_JSON_KEY"                  : env.get ( 'JWT_JSON_KEY' ),
        # "JWT_PRIVATE_KEY"               : env.get ( 'JWT_PRIVATE_KEY' ),
        # "JWT_PUBLIC_KEY"                : env.get ( 'JWT_PUBLIC_KEY' ),
        # "JWT_QUERY_STRING_NAME"         : env.get ( 'JWT_QUERY_STRING_NAME' ),
        # "JWT_QUERY_STRING_VALUE_PREFIX" : env.get ( 'JWT_QUERY_STRING_VALUE_PREFIX' ),
        # Set a new name to token cookies
        "JWT_REFRESH_COOKIE_NAME"       : env.get ( 'JWT_REFRESH_COOKIE_NAME' ),
        # Set the cookie paths
        "JWT_REFRESH_COOKIE_PATH"       : env.get ( 'JWT_REFRESH_COOKIE_PATH' ),
        # "JWT_REFRESH_CSRF_COOKIE_NAME"  : env.get ( 'JWT_REFRESH_CSRF_COOKIE_NAME' ),
        # "JWT_REFRESH_CSRF_COOKIE_PATH"  : env.get ( 'JWT_REFRESH_CSRF_COOKIE_PATH' ),
        # "JWT_REFRESH_CSRF_FIELD_NAME"   : env.get ( 'JWT_REFRESH_CSRF_FIELD_NAME' ),
        # Set header refresh name for csrf
        "JWT_REFRESH_CSRF_HEADER_NAME"  : env.get ( 'JWT_REFRESH_CSRF_HEADER_NAME' ),
        # "JWT_REFRESH_JSON_KEY"          : env.get ( 'JWT_REFRESH_JSON_KEY' ),
        # Se define el tiempo de duración del token de reingreso o relogin
        "JWT_REFRESH_TOKEN_EXPIRES"     : SuccessEnv.toInt ( env.get ( 'JWT_REFRESH_TOKEN_EXPIRES' ) ),
        # Set the secret key to sign the JWTs with
        "JWT_SECRET_KEY"                : env.get ( 'JWT_SECRET_KEY' ),
        # JWT_SESSION_COOKIE            : SuccessEnv.isTrue ( env.get ( 'JWT_SESSION_COOKIE' ),
        # Configure application to store JWTs in cookies
        "JWT_TOKEN_LOCATION"            : env.get ( 'JWT_TOKEN_LOCATION' )
        # "JWT_ENCODE_NBF"                : SuccessEnv.isTrue ( env.get ( 'JWT_ENCODE_NBF' )
      }
    return {}


  @staticmethod
  def loadLogger ( env : SuccessEnvProvider ) -> dict :
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_LOGGER' ) ) ) :
      return {
        "LOGGER_ADMIN"                   : env.get    ( 'LOGGER_ADMIN' ),
        "LOGGER_BACKUP_COUNT"            : SuccessEnv.toInt  ( env.get ( 'LOGGER_BACKUP_COUNT' ) ),
        "LOGGER_CONSOLE"                 : SuccessEnv.isTrue ( env.get ( 'LOGGER_CONSOLE' ) ),
        "LOGGER_DIR"                     : env.get    ( 'LOGGER_DIR' ),
        "LOGGER_ENCODING"                : env.get    ( 'LOGGER_ENCODING' ),
        "LOGGER_FILE"                    : SuccessEnv.isTrue ( env.get ( 'LOGGER_FILE' ) ),
        "LOGGER_FORMAT"                  : env.get    ( 'LOGGER_FORMAT' ),
        "LOGGER_FORMATER"                : env.get    ( 'LOGGER_FORMATER' ),
        "LOGGER_LEVEL"                   : env.get    ( 'LOGGER_LEVEL' ),
        "LOGGER_MAIL_ENABLED"            : SuccessEnv.isTrue ( env.get ( 'LOGGER_MAIL_ENABLED' ) ),
        "LOGGER_MAIL_PASSWORD"           : env.get    ( 'LOGGER_MAIL_PASSWORD' ),
        "LOGGER_MAIL_PORT"               : SuccessEnv.toInt  ( env.get ( 'LOGGER_MAIL_PORT' ) ),
        "LOGGER_MAIL_SERVER"             : env.get    ( 'LOGGER_MAIL_SERVER' ),
        "LOGGER_MAIL_SSL"                : SuccessEnv.isTrue ( env.get ( 'LOGGER_MAIL_SSL' ) ),
        "LOGGER_MAIL_TLS"                : SuccessEnv.isTrue ( env.get ( 'LOGGER_MAIL_TLS' ) ),
        "LOGGER_MAIL_USERNAME"           : env.get    ( 'LOGGER_MAIL_USERNAME' ),
        "LOGGER_MAX_BYTES"               : SuccessEnv.toInt  ( env.get ( 'LOGGER_MAX_BYTES' ) ),
        "LOGGER_MAX_RETRIES"             : SuccessEnv.toInt  ( env.get ( 'LOGGER_MAX_RETRIES' ) ),
        "LOGGER_MESSAGE_SUBJECT"         : env.get    ( 'LOGGER_MESSAGE_SUBJECT' ),
        "LOGGER_ROTATE_INTERVAL"         : env.get    ( 'LOGGER_ROTATE_INTERVAL' ),
        "LOGGER_TEMPLATE_FORMAT_MESSAGE" : env.get    ( 'LOGGER_TEMPLATE_FORMAT_MESSAGE' ),
        "LOGGER_TEMPLATE_HTML_ERROR"     : env.get    ( 'LOGGER_TEMPLATE_HTML_ERROR' ),
        "LOGGER_TEMPLATE_HTML_EXCEPTION" : env.get    ( 'LOGGER_TEMPLATE_HTML_EXCEPTION' ),
        "LOGGER_ROTATE_WHEN"             : env.get    ( 'LOGGER_ROTATE_WHEN' )
      }
    return {}


  @staticmethod
  def loadEmail ( env : SuccessEnvProvider ) -> dict :
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_EMAIL' ) ) ) :
      return {
        "MAIL_SERVER"                : env.get    ( 'MAIL_SERVER' ),
        "MAIL_PORT"                  : SuccessEnv.toInt  ( env.get ( 'MAIL_PORT' ) ),
        "MAIL_USE_TLS"               : SuccessEnv.isTrue ( env.get ( 'MAIL_USE_TLS' ) ),
        "MAIL_USE_SSL"               : SuccessEnv.isTrue ( env.get ( 'MAIL_USE_SSL' ) ),
        "MAIL_DEBUG"                 : SuccessEnv.toInt  ( env.get ( 'MAIL_DEBUG' ) ),
        "MAIL_USERNAME"              : env.get    ( 'MAIL_USERNAME' ),
        "MAIL_PASSWORD"              : env.get    ( 'MAIL_PASSWORD' ),
        "MAIL_DEFAULT_SENDER"        : SuccessEnv.toList ( env.get ( 'MAIL_DEFAULT_SENDER' ) ),
        "MAIL_MAX_EMAILS"            : SuccessEnv.toInt  ( env.get ( 'MAIL_MAX_EMAILS' ) ),
        # "MAIL_SUPPRESS_SEND"         : env.get    ( 'MAIL_SUPPRESS_SEND' ),
        "MAIL_ASCII_ATTACHMENTS"     : SuccessEnv.isTrue ( env.get ( 'MAIL_ASCII_ATTACHMENTS' ) ),
        # ---------------------------------------------------------
        # Mail Opcional Configuration / Configuración Opcional Mail
        # ---------------------------------------------------------
        "MAIL_DONT_REPLY_FROM_EMAIL" : env.get    ( 'MAIL_DONT_REPLY_FROM_EMAIL' )
      }
    return {}


  @staticmethod
  def loadMarshmallow ( env : SuccessEnvProvider ) -> dict :
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_MARSHMALLOW' ) ) ) :
      return {
        
      }
    return {}


  @staticmethod
  def loadRedis ( env : SuccessEnvProvider ) -> dict :
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_REDIS' ) ) ) :
      return {
        "REDIS_CHARSET"          : env.get    ( 'REDIS_CHARSET' ),
        "REDIS_CONNECTION_POOL"  : env.get    ( 'REDIS_CONNECTION_POOL' ),
        "REDIS_DB"               : env.get    ( 'REDIS_DB' ),
        "REDIS_DECODE_RESPONSES" : SuccessEnv.isTrue ( env.get ( 'REDIS_DECODE_RESPONSES' ) ),
        "REDIS_ERRORS"           : env.get    ( 'REDIS_ERRORS' ),
        "REDIS_HOST"             : env.get    ( 'REDIS_HOST' ),
        "REDIS_PASSWORD"         : env.get    ( 'REDIS_PASSWORD' ),
        "REDIS_PORT"             : SuccessEnv.toInt  ( env.get ( 'REDIS_PORT' ) ),
        "REDIS_SOCKET_TIMEOUT"   : env.get    ( 'REDIS_SOCKET_TIMEOUT' ),
        "REDIS_UNIX_SOCKET_PATH" : env.get    ( 'REDIS_UNIX_SOCKET_PATH' )
      }
    return {}


  @staticmethod
  def loadRestful ( env : SuccessEnvProvider ) -> dict :
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_RESTFUL' ) ) ) :
      return {
        "RESTFUL_CATCH_ALL_404S" : SuccessEnv.isTrue ( env.get ( 'RESTFUL_CATCH_ALL_404S' ) )
      }
    return {}


  @staticmethod
  def loadSession ( env : SuccessEnvProvider ) -> dict :
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_SESSION' ) ) ) :
      return {
        "SESSION_COOKIE_NAME"        : env.get    ( 'SESSION_COOKIE_NAME' ),
        "SESSION_COOKIE_DOMAIN"      : env.get    ( 'SESSION_COOKIE_DOMAIN' ),
        "SESSION_COOKIE_PATH"        : env.get    ( 'SESSION_COOKIE_PATH' ),
        "SESSION_COOKIE_HTTPONLY"    : SuccessEnv.isTrue ( env.get ( 'SESSION_COOKIE_HTTPONLY' ) ),
        "SESSION_COOKIE_SECURE"      : SuccessEnv.isTrue ( env.get ( 'SESSION_COOKIE_SECURE' ) ),
        "PERMANENT_SESSION_LIFETIME" : timedelta     ( seconds = SuccessEnv.toInt  ( env.get ( 'PERMANENT_SESSION_LIFETIME' ) ) ),
        "SESSION_TYPE"               : env.get    ( 'SESSION_TYPE' ),
        "SESSION_PERMANENT"          : SuccessEnv.isTrue ( env.get ( 'SESSION_PERMANENT' ) ),
        "SESSION_USE_SIGNER"         : SuccessEnv.isTrue ( env.get ( 'SESSION_USE_SIGNER' ) ),
        "SESSION_KEY_PREFIX"         : env.get    ( 'SESSION_KEY_PREFIX' ),
        # "SESSION_REDIS"              : env.get    ( 'SESSION_REDIS' ),
        # "SESSION_MEMCACHED"          : env.get    ( 'SESSION_MEMCACHED' ),
        # "SESSION_FILE_DIR"           : env.get    ( 'SESSION_FILE_DIR' ),
        # "SESSION_FILE_THRESHOLD"     : env.get    ( 'SESSION_FILE_THRESHOLD' ),
        # "SESSION_FILE_MODE"          : env.get    ( 'SESSION_FILE_MODE' ),
        # "SESSION_MONGODB"            : env.get    ( 'SESSION_MONGODB' ),
        # "SESSION_MONGODB_DB"         : env.get    ( 'SESSION_MONGODB_DB' ),
        # "SESSION_MONGODB_COLLECT"    : env.get    ( 'SESSION_MONGODB_COLLECT' ),
        # "SESSION_SQLALCHEMY"         : env.get    ( 'SESSION_SQLALCHEMY' ),
        # "SESSION_SQLALCHEMY_TABLE"   : env.get    ( 'SESSION_SQLALCHEMY_TABLE' )
      }
    return {}


  @staticmethod
  def loadSqlalchemy ( env : SuccessEnvProvider ) -> dict :
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_SQLALCHEMY' ) ) ) :
      return {
        "SQLALCHEMY_DATABASE_URI" : '{driver}://{user}:{pw}@{host}:{port}/{db}'.format (
          driver = env.get ( 'SQLALCHEMY_DB_DRIVER' ),
          user   = env.get ( 'SQLALCHEMY_DB_USER' ),
          pw     = env.get ( 'SQLALCHEMY_DB_PASSWORD' ),
          host   = env.get ( 'SQLALCHEMY_DB_HOST' ),
          port   = env.get ( 'SQLALCHEMY_DB_PORT' ),
          db     = env.get ( 'SQLALCHEMY_DB_NAME' )
        ),
        "SQLALCHEMY_BINDS"                    : SuccessEnv.getJson  ( env.get ( 'SQLALCHEMY_BINDS' ) ),
        # "SQLALCHEMY_BINDS"                    : SuccessEnv.getJson  ( env.get ( 'SQLALCHEMY_BINDS' ) ) or env.toResource ( 'SQLALCHEMY_BINDS' ),
        "SQLALCHEMY_ECHO"                     : SuccessEnv.isTrue ( env.get ( 'SQLALCHEMY_ECHO' ) ),
        "SQLALCHEMY_RECORD_QUERIES"           : SuccessEnv.isTrue ( env.get ( 'SQLALCHEMY_RECORD_QUERIES' ) ),
        "SQLALCHEMY_COMMIT_ON_TEARDOWN"       : SuccessEnv.isTrue ( env.get ( 'SQLALCHEMY_COMMIT_ON_TEARDOWN' ) ),
        "SQLALCHEMY_TRACK_MODIFICATIONS"      : SuccessEnv.isTrue ( env.get ( 'SQLALCHEMY_TRACK_MODIFICATIONS' ) ),
        "SQLALCHEMY_ENGINE_OPTIONS"           : env.get     ( 'SQLALCHEMY_ENGINE_OPTIONS' ),
        # ------------------------------------------------------------------------------------------------------------------------------------
        # additional sqlalchemy configuration for database connection / configuración adicional sqlalchemy para la conexión a la base de datos
        # ------------------------------------------------------------------------------------------------------------------------------------
        "SQLALCHEMY_DB_DRIVER"                : env.get     ( 'SQLALCHEMY_DB_DRIVER' ),
        "SQLALCHEMY_DB_HOST"                  : env.get     ( 'SQLALCHEMY_DB_HOST' ),
        "SQLALCHEMY_DB_PORT"                  : env.get     ( 'SQLALCHEMY_DB_PORT' ),
        "SQLALCHEMY_DB_NAME"                  : env.get     ( 'SQLALCHEMY_DB_NAME' ),
        "SQLALCHEMY_DB_USER"                  : env.get     ( 'SQLALCHEMY_DB_USER' ),
        "SQLALCHEMY_DB_PASSWORD"              : env.get     ( 'SQLALCHEMY_DB_PASSWORD' ),
        "SQLALCHEMY_TABLENAME_SUCCESS_MODEL"  : env.get     ( 'SQLALCHEMY_TABLENAME_SUCCESS_MODEL' )
      }
    return {}
