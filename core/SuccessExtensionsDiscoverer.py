# Python Libraries / Librerías Python
from flask   import Flask
from pathlib import Path
import importlib
import inspect
import json
import os

# Success Libraries / Librerías Success
from success.common.base.SuccessClass                 import SuccessClass
from success.common.base.SuccessExtension             import SuccessExtension
from success.common.tools.SuccessClasses              import SuccessClasses
from success.core.SuccessContext                      import SuccessContext
from success.common.infra.config.SuccessConfig        import SuccessConfig
from success.engine.infrastructure.SuccessHookManager import SuccessHookManager
from success.common.tools.SuccessFile                 import SuccessFile
from success.common.tools.SuccessPathResolver         import SuccessPathResolver

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessExtensionsDiscoverer ( SuccessClass ) :
  """
  Descubre extensiones personalizadas dentro de los directorios de infraestructura
  siguiendo la estructura: apps/infrastructure/{service}/{version}/{module}/extensions/
  """

  __app    : Flask              = None
  __config : SuccessConfig      = None
  _data    : dict               = None
  __hooks  : SuccessHookManager = None


  def __init__ ( self, apps : Flask, config : SuccessConfig = None, hooks : SuccessHookManager = None, base_path = "apps/infrastructure" ) :
    super ().__init__ ()
    self.__app     = apps
    self.__config  = config
    self.__hooks   = hooks
    self.base_path = base_path
    self._data     = SuccessFile.loadAppJson ( "extensions.json" )


  def discover ( self ) :
    """Descubre clases válidas que extienden SuccessExtension en la ruta indicada"""
    if not self._data :
      self._logger.log ( f"No se registraron extensiones personalizadas para la aplicación {SuccessContext ().getCurrentAppName ()}.", "WARNING" )
      return

    extensions = []

    for idx, estension in enumerate ( self._data ) :
      _class  = estension.get ( "class", f"unnamed_extension_{idx}" )
      enabled = estension.get ( "enabled" )
      config  = estension.get ( "config", {} )

      if not isinstance ( _class, str ) :
        self._logger.log ( f"[{_class}] La 'extensión' debe ser una cadena tipo 'paquete.Clase'.", "ERROR" )
        continue

      if not config :
        self._logger.log ( f"[{config}] El valor de 'config' debe contener al menos un registro de tipo 'key' : 'value'.", "ERROR" )
        continue

      try :

        instance = self.resolveCallback ( _class )
        instance.userConfig ( **config )
        instance.register ()
        SuccessContext ().setExtension ( instance.__class__.__name__, instance )
        self._logger.log ( f"Se ha registrado la extensiones personalizadas {instance.__class__.__name__, instance} para la aplicación {SuccessContext ().getCurrentAppName ()}.", "INFO" )

      except Exception as e :
        self._logger.log ( f"Error al resolver la clase de extensión '{_class}': {e}", "ERROR" )
        continue

      _tuple = ( instance.__class__.__name__, instance )

      extensions.append ( _tuple )

    return extensions


  def resolveCallback ( self, callback : str ) -> callable :
    try :
      parts = callback.split ( "." )
      if len ( parts ) < 3 :
        raise ValueError ( f"Callback '{callback}' debe tener formato completo: paquete.Clase" )

      *moduleParts, className = parts

      module = SuccessClasses.getModule ( "infrastructure", moduleParts, className )
      klass  = SuccessClasses.getClassFromModule ( module, className )

      if not issubclass ( klass, SuccessExtension ) :
        raise TypeError ( f"La clase '{className}' no hereda de SuccessExtension." )

      instance = klass ( self.__app )

      return instance

    except Exception as e :
      raise RuntimeError ( f"Error resolviendo callback '{callback}': {e}" )
