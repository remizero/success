# Python Libraries / Librerías Python
from dotenv import load_dotenv
import os

# Application Libraries / Librerías de la Aplicación
from success.common.SuccessDebug                         import SuccessDebug
from success.common.tools.SuccessEnv                     import SuccessEnv
from success.common.infra.config.SuccessConfigExtensions import SuccessConfigExtensions
from success.common.infra.config.SuccessEnvProvider      import SuccessEnvProvider

# Preconditions / Precondiciones


class SuccessConfig ( object ) :


  def __init__ ( self, env : SuccessEnvProvider ) -> None :
    # ----------------------------------------------------------
    # Success Configuration / Configuración de Success
    # ----------------------------------------------------------  
    self.APP_ENV                       = env.get ( 'APP_ENV' )
    self.APP_HOST                      = env.get ( 'APP_HOST' )
    self.APP_PORT                      = SuccessEnv.toInt ( env.get ( 'APP_PORT' ) )
    self.BASE_URL                      = env.get ( 'BASE_URL' )
    self.DEBUG                         = SuccessEnv.isTrue ( env.get ( 'DEBUG' ) )
    self.SERVER_NAME                   = env.get ( 'SERVER_NAME' )
    self.SECRET_KEY                    = env.get ( 'SECRET_KEY' )
    self.API_KEY                       = env.get ( 'API_KEY' )
    self.SUCCESS_DEBUG_CONSOLE         = SuccessEnv.isTrue ( env.get ( 'SUCCESS_DEBUG_CONSOLE' ) )
    self.SUCCESS_STAGING               = SuccessEnv.isTrue ( env.get ( 'SUCCESS_STAGING' ) )
    self.SUCCESS_TESTING               = SuccessEnv.isTrue ( env.get ( 'SUCCESS_TESTING' ) )
    self.SUCCESS_STRICT_SLASHES        = SuccessEnv.isTrue ( env.get ( 'SUCCESS_STRICT_SLASHES' ) )
    self.SUCCESS_EXTENSION_ACL         = SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_ACL' ) )
    self.SUCCESS_EXTENSION_CORS        = SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_CORS' ) )
    self.SUCCESS_EXTENSION_SQLALCHEMY  = SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_SQLALCHEMY' ) )
    self.SUCCESS_EXTENSION_EMAIL       = SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_EMAIL' ) )
    self.SUCCESS_EXTENSION_JWT         = SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_JWT' ) )
    self.SUCCESS_EXTENSION_LOGGER      = SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_LOGGER' ) )
    self.SUCCESS_EXTENSION_MARSHMALLOW = SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_MARSHMALLOW' ) )
    self.SUCCESS_EXTENSION_REDIS       = SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_REDIS' ) )
    self.SUCCESS_EXTENSION_RESTFUL     = SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_RESTFUL' ) )
    self.SUCCESS_EXTENSION_SESSION     = SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_SESSION' ) )
    self.SUCCESS_OUTPUT_MODEL          = SuccessEnv.isTrue ( env.get ( 'SUCCESS_OUTPUT_MODEL' ) )
    self.SUCCESS_TABLENAME_MODEL       = SuccessEnv.isTrue ( env.get ( 'SUCCESS_TABLENAME_MODEL' ) )
    # # Control del CLI interno
    self.SUCCESS_ENABLE_CLI            = SuccessEnv.isTrue ( env.get ( 'SUCCESS_ENABLE_CLI' ) )
    self.SUCCESS_ENABLE_GRAPHQL        = SuccessEnv.isTrue ( env.get ( 'SUCCESS_ENABLE_GRAPHQL' ) )
    self.SUCCESS_ENABLE_REST           = SuccessEnv.isTrue ( env.get ( 'SUCCESS_ENABLE_REST' ) )
    self.SUCCESS_ENABLE_RPC            = SuccessEnv.isTrue ( env.get ( 'SUCCESS_ENABLE_RPC' ) )
    self.SUCCESS_ENABLE_SSE            = SuccessEnv.isTrue ( env.get ( 'SUCCESS_ENABLE_SSE' ) )
    self.SUCCESS_ENABLE_SOAP           = SuccessEnv.isTrue ( env.get ( 'SUCCESS_ENABLE_SOAP' ) )
    self.SUCCESS_ENABLE_VIEW           = SuccessEnv.isTrue ( env.get ( 'SUCCESS_ENABLE_VIEW' ) )
    self.SUCCESS_ENABLE_WEB_SOCKET     = SuccessEnv.isTrue ( env.get ( 'SUCCESS_SUCCESS_ENABLE_WEB_SOCKETENABLE_CLI' ) )

    self.SUCCESS_CUSTOM_CONFIG_CLASS   = env.get ( 'SUCCESS_CUSTOM_CONFIG_CLASS' )

    # Control del entrypoint visual
    # self.SUCCESS_ENABLE_DASHBOARD      = SuccessEnv.isTrue ( env.get ( 'SUCCESS_ENABLE_DASHBOARD' )
    # # Aplicación principal (enrutada en '/')
    # self.SUCCESS_DEFAULT_APP           = SuccessEnv.isTrue ( env.get ( 'SUCCESS_DEFAULT_APP' )
    self.SUCCESS_HUMOR_ENABLED         = SuccessEnv.isTrue ( env.get ( 'SUCCESS_HUMOR_ENABLED' ) )
    self.SUCCESS_MOOD_LANG             = env.get ( 'SUCCESS_MOOD_LANG' )
    self.SUCCESS_CUSTOM_CONFIG_CLASS   = env.get ( 'SUCCESS_CUSTOM_CONFIG_CLASS' )
    self.SUCCESS_APP_MAIN              = SuccessEnv.isTrue ( env.get ( 'SUCCESS_APP_MAIN' ) )
    # self.SUCCESS_EXTENSION_ = 
    # self.SUCCESS_EXTENSION_ = 


    # -----------------------------------------
    # Flask Configuration / Configuración Flask
    # -----------------------------------------
    # - Project name.
    self.FLASK_APP             = env.get ( 'FLASK_APP' )
    # - Controls the environment.
    self.FLASK_ENV             = env.get ( 'FLASK_ENV' )
    #  - Enables debug mode.
    self.FLASK_DEBUG           = SuccessEnv.isTrue ( env.get ( 'FLASK_DEBUG' ) )
    # - A list of files that will be watched by the reloader in addition to the Python modules.
    # self.FLASK_RUN_EXTRA_FILES = env.get ( 'FLASK_RUN_EXTRA_FILES' )
    # - The host you want to bind your apps to.
    # self.FLASK_RUN_HOST        = env.get ( 'FLASK_RUN_HOST' )
    # - The port you want to use.
    # self.FLASK_RUN_PORT        = env.toInt ( 'FLASK_RUN_PORT' )
    # - A certificate file for so your apps can be run with HTTPS.
    # self.FLASK_RUN_CERT        = env.get ( 'FLASK_RUN_CERT' )
    # - The key file for your cert.
    # self.FLASK_RUN_KEY         = env.get ( 'FLASK_RUN_KEY' )

    # -------------------------------------------------
    # ACL Configuration / Configuración ACL
    # -------------------------------------------------
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_ACL' ) ) ) :
      self.extend ( SuccessConfigExtensions.loadAcl ( env ) )


    # -------------------------------------------------
    # Blueprint Configuration / Configuración Blueprint
    # -------------------------------------------------
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_BLUEPRINT' ) ) ) :
      self.extend ( SuccessConfigExtensions.loadBlueprint ( env ) )


    # ---------------------------------------
    # Cors Configuration / Configuración Cors
    # ---------------------------------------
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_CORS' ) ) ) :
      self.extend ( SuccessConfigExtensions.loadCors ( env ) )


    # ---------------------------------------
    # JWT Configuration / Configuración JWT
    # ---------------------------------------
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_JWT' ) ) ) :
      self.extend ( SuccessConfigExtensions.loadJwt ( env ) )


    # ---------------------------------------
    # SuccessLogger Configuration / Configuración SuccessLogger
    # ---------------------------------------
    # ---------------------------------------
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_LOGGER' ) ) ) :
      self.extend ( SuccessConfigExtensions.loadLogger ( env ) )


    # ---------------------------------------
    # Mail Configuration / Configuración Mail
    # ---------------------------------------
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_EMAIL' ) ) ) :
      self.extend ( SuccessConfigExtensions.loadEmail ( env ) )


    # -------------------------------------------------
    # MARSHMALLOW Configuration / Configuración MARSHMALLOW
    # -------------------------------------------------
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_MARSHMALLOW' ) ) ) :
      self.extend ( SuccessConfigExtensions.loadMarshmallow ( env ) )


    # -----------------------------------------
    # Redis Configuration / Configuración Redis
    # -----------------------------------------
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_REDIS' ) ) ) :
      self.extend ( SuccessConfigExtensions.loadRedis ( env ) )


    # ---------------------------------------------
    # Restful Configuration / Configuración Restful
    # ---------------------------------------------
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_RESTFUL' ) ) ) :
      self.extend ( SuccessConfigExtensions.loadRestful ( env ) )


    # -----------------------------------------------
    # SuccessSessionExtension Configuration / Configuración de Sesión
    # -----------------------------------------------
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_SESSION' ) ) ) :
      self.extend ( SuccessConfigExtensions.loadSession ( env ) )


    # ---------------------------------------------------
    # SqlAlchemy Configuration / Configuración SqlAlchemy
    # ---------------------------------------------------
    if ( SuccessEnv.isTrue ( env.get ( 'SUCCESS_EXTENSION_SQLALCHEMY' ) ) ) :
      self.extend ( SuccessConfigExtensions.loadSqlalchemy ( env ) )


  def extend ( self, config_dict : dict ) -> None :
    """
    Recibe un diccionario con configuraciones adicionales
    y las asigna como atributos de la instancia.
    """
    for key, value in config_dict.items () :
      setattr ( self, key, value )

  
  def get ( self, key : str, default = None ) -> str :
    return getattr ( self, key, default )
