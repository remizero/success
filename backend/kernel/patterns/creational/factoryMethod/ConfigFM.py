# Python Libraries / Librerías Python


# Application Libraries / Librerías de la Aplicación
from kernel           import Application
from kernel           import Debug
from kernel.abstracts import Config
from config           import Default
from config           import Development
from config           import Local
from config           import Production
from config           import Staging
from config           import Testing
from exceptions       import DevelopmentModeException
from exceptions       import ProductionModeException
from exceptions       import StagingModeException
from utils            import EnvVar


# Preconditions / Precondiciones


class ConfigFM () :

  @staticmethod
  def create () -> Config :

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

      config = Default ()

    return config
