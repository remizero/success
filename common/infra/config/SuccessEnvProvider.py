# Python Libraries / Librerías Python
from abc import ABC, abstractmethod
from flask  import json
from typing import Any

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessEnvProvider ( ABC ) :


  @abstractmethod
  def get ( key : str, default = None ) -> str :
    raise NotImplementedError ()


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


  @staticmethod
  def getCorsResources () -> dict :
    resource = '{ '
    corsResources = SuccessEnv.toList ( self.get ( 'CORS_RESOURCES_APP_RESOURCES' ) )
    corsOrigins   = SuccessEnv.toList ( self.get ( 'CORS_RESOURCES_APP_ORIGINS' ) )
    corsMethods   = SuccessEnv.toList ( self.get ( 'CORS_RESOURCES_APP_METHODS' ) )
    corsAllowed   = SuccessEnv.toList ( self.get ( 'CORS_RESOURCES_APP_ALLOW_HEADERS' ) )
    corsExposes   = SuccessEnv.toList ( self.get ( 'CORS_RESOURCES_APP_EXPOSE_HEADERS' ) )
    for i in range ( len ( corsResources ) ) :
      resource += corsResources [ i ] + ' : { '
      resource += '\'origins\' : ' + SuccessEnv.listToString ( corsOrigins, i ) + ', '
      resource += '\'methods\' : ' + SuccessEnv.listToString ( corsMethods, i ) + ', '
      resource += '\'allow_headers\' : ' + SuccessEnv.listToString ( corsAllowed, i ) + ', '
      resource += '\'expose_headers\' : ' + SuccessEnv.listToString ( corsExposes, i )
      resource += ' }, '

    resource = resource [ : -2 ]
    resource += ' }'

    return SuccessEnv.toResource ( resource )


  @abstractmethod
  def getJson ( key : str ) -> Any :
    raise NotImplementedError ()


  @abstractmethod
  def isEmpty ( key : str ) -> bool :
    raise NotImplementedError ()


  @abstractmethod
  def isTrue ( key : str ) -> bool :
    raise NotImplementedError ()


  @abstractmethod
  def toInt ( key : str ) -> int :
    raise NotImplementedError ()
