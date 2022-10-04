# Python Libraries / Librerías Python
import os


# Application Libraries / Librerías de la Aplicación
from config import (
  Development,
  Production,
  Testing,
  Staging
)
from kernel import Config, Debug
from exceptions import (
  DevelopmentModeException,
  ProductionModeException,
  StagingModeException
)


# Preconditions / Precondiciones


class Application () :

  @staticmethod
  def __isMode ( mode : str ) -> bool :
    return os.environ.get ( 'APP_ENV' ) == mode

  @staticmethod
  def getConfigClass ( default : Config ) -> Config :

    config = None
    if ( Application.isDevelopmentMode () ) :

      if ( Application.isDebugMode () ) :

        config = Development ()

      else :

        # TODO AQUI MOSTRAR UN ERROR EN CONSOLA
        Debug.log ( 'TIENE QUE ESTAR HABILITADO EL MODO DEBUG' )
        raise DevelopmentModeException ()

    elif ( Application.isTestingMode () ) :

      config = Testing ()

    elif ( Application.isStagingMode () ) :

      if ( Application.isProductionMode () ) :

        config = Staging ()

      else :

        # TODO AQUI MOSTRAR UN ERROR EN CONSOLA
        Debug.log ( 'TIENE QUE ESTAR HABILITADO EL MODO PRODUCCION' )
        raise StagingModeException ()

    elif ( Application.isProductionMode () ) :

      if ( not Application.isDebugMode () ) :

        config = Production ()

      else :

        # TODO AQUI MOSTRAR UN ERROR EN CONSOLA
        Debug.log ( 'TIENE QUE ESTAR DESHABILITADO EL MODO DEBUG' )
        raise ProductionModeException ()

    else :

      config = default

    return config

  @staticmethod
  def getConfigFile () -> str :
    configFile = ''
    if ( Application.isDefaultMode () ) :

      configFile = 'Default.py'

    elif ( Application.isDevelopmentMode () ) :

      configFile = 'Development.py'

    elif ( Application.isLocalMode () ) :

      configFile = 'Local.py'

    elif ( Application.isProductionMode () ) :

      configFile = 'Production.py'

    elif ( Application.isStagingMode () ) :

      configFile = 'Staging.py'

    elif ( Application.isTestingMode () ) :

      configFile = 'Testing.py'

    return configFile

  @staticmethod
  def isDebugMode () -> bool :
    return bool ( os.environ.get ( 'FLASK_DEBUG' ) ) or bool ( os.environ.get ( 'DEBUG' ) )

  @staticmethod
  def isDefaultMode () -> bool :
    return Application.__isMode ( 'default' )

  @staticmethod
  def isDevelopmentMode () -> bool :
    return Application.__isMode ( 'development' )

  @staticmethod
  def isLocalMode () -> bool :
    return Application.__isMode ( 'local' )

  @staticmethod
  def isProductionMode () -> bool :
    return Application.__isMode ( 'production' )

  @staticmethod
  def isTestingMode () -> bool :
    return bool ( os.environ.get ( 'TESTING' ) )

  @staticmethod
  def isStagingMode () -> bool :
    return bool ( os.environ.get ( 'STAGING' ) )
