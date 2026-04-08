# Python Libraries / Librerías Python
from dotenv import dotenv_values
from dotenv import load_dotenv
from flask  import json
from typing import Optional, Dict
import ast
import os

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones
RESERVED_VARS = {
  'SUCCESS_APP_PREFIX',
  'SUCCESS_MAIN_APP',
  'SUCCESS_SECONDARY_APPS',
  'SUCCESS_ALLOW_NO_MAIN_APP',
  'SUCCESS_SAVE_MODE',
  'SUCCESS_SHOW_SUMMARY',
  'SUCCESS_SUMMARY_LEVEL',
  'SUCCESS_HUMOR_ENABLED',
  'SUCCESS_MOOD_LANG',
  'SUCCESS_APP_DOMAIN',
}


class SuccessEnv () :


  @staticmethod
  def verify_required_env_vars(required_vars: list[str]) -> None:
    for var in required_vars:
      if not os.getenv(var):
        raise EnvironmentError(f"Variable de entorno obligatoria no definida: {var}")


  @staticmethod
  def load_env_filtered ( path : str ) :
    env_vars = dotenv_values ( path )
    for k, v in env_vars.items () :
      if k not in RESERVED_VARS :
        os.environ [ k ] = v


  # @staticmethod
  # def get ( envVar : str, default = None ) :

  #   return os.environ.get ( envVar, default )


  # @staticmethod
  # def getCorsResources () -> dict :
  #   resource = '{ '
  #   corsResources = SuccessEnv.toList ( 'CORS_RESOURCES_APP_RESOURCES' )
  #   corsOrigins   = SuccessEnv.toList ( 'CORS_RESOURCES_APP_ORIGINS' )
  #   corsMethods   = SuccessEnv.toList ( 'CORS_RESOURCES_APP_METHODS' )
  #   corsAllowed   = SuccessEnv.toList ( 'CORS_RESOURCES_APP_ALLOW_HEADERS' )
  #   corsExposes   = SuccessEnv.toList ( 'CORS_RESOURCES_APP_EXPOSE_HEADERS' )
  #   for i in range ( len ( corsResources ) ) :
  #     resource += corsResources [ i ] + ' : { '
  #     resource += '\'origins\' : ' + SuccessEnv.listToString ( corsOrigins, i ) + ', '
  #     resource += '\'methods\' : ' + SuccessEnv.listToString ( corsMethods, i ) + ', '
  #     resource += '\'allow_headers\' : ' + SuccessEnv.listToString ( corsAllowed, i ) + ', '
  #     resource += '\'expose_headers\' : ' + SuccessEnv.listToString ( corsExposes, i )
  #     resource += ' }, '

  #   resource = resource [ : -2 ]
  #   resource += ' }'

  #   return SuccessEnv.toResource ( resource )


  @staticmethod
  def getJson ( value : str ) :

    return json.loads ( value )


  @staticmethod
  def isEmpty ( value : str ) -> bool :

    return ( value == '' )


  @staticmethod
  def isTrue ( value : str ) -> bool :
    
    return (  str ( value ).lower () == 'true' )


  # Esto se queda aquí
  @staticmethod
  def listToString ( envVarList : list, index : int = 0 ) -> str :

    return envVarList [ index ].__repr__ ()


  # Esto se queda aquí
  @staticmethod
  def loadEnv ( envFilePath : str = None, override : bool = False ) -> None :
    if ( envFilePath ) :
      dotenv_path = os.path.join ( os.path.dirname ( envFilePath ), '.env' )

    else :
      dotenv_path = os.path.join ( os.path.dirname ( __file__ ), '../../.env' )

    load_dotenv ( dotenv_path, override = override )


  # Esto se queda aquí
  @staticmethod
  def loadAppEnv ( envFilePath : str = None ) -> dict [ str, Optional [ str ] ] :
    if ( envFilePath ) :
      dotenvPath = os.path.join ( os.path.dirname ( envFilePath ), '.env' )

    else :
      dotenvPath = os.path.join ( os.path.dirname ( __file__ ), '../../.env' )

    return dotenv_values ( dotenvPath )


  @staticmethod
  def toInt ( value : str ) -> int :

    return int ( value )


  # Esto se queda aquí
  @staticmethod
  def toList ( value : str ) -> list :
    toReturn = list ()
    if ( SuccessEnv.wellFormedList ( value ) ) :
      toReturn = value.strip ( ' ][ ' ).split ( ', ' )

    else :
      toReturn = ast.literal_eval ( value )

    return toReturn


  # Esto se queda aquí
  @staticmethod
  def toResource ( resource : str ) -> dict :

    return ast.literal_eval ( resource )


  # Esto se queda aquí
  @staticmethod
  def wellFormedList ( value : str ) -> bool :
    string = value
    
    return ( 'r\'' in string ) and ( '[' in string ) and ( ']' in string )
