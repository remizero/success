# Python Libraries / Librerías Python
from dotenv import load_dotenv
from flask import Flask
import importlib
import os

# Success Libraries / Librerías Success
from success.common.SuccessDebug               import SuccessDebug
from success.common.tools.SuccessEnv           import SuccessEnv
from success.common.infra.config.SuccessConfig import SuccessConfig

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessConfigLoader () :


  @classmethod
  def load ( cls, app : Flask ) -> None :
    # 1. Cargar .env primero
    # env_path = os.getenv ( "SUCCESS_ENV_PATH", ".env" )
    # load_dotenv ( env_path )
    SuccessSystemEnv.loadEnv ( __file__, True )

    # 2. Cargar SuccessConfig base del framework
    app.config.from_object ( SuccessConfig )

    # 3. ¿Clase de configuración personalizada?
    custom_config_path = os.getenv ( "SUCCESS_CUSTOM_CONFIG_CLASS" )
    if custom_config_path :
      try :
        module_path, class_name = custom_config_path.rsplit ( ".", 1 )
        module = importlib.import_module ( module_path )
        custom_config_class = getattr ( module, class_name )

        if not isinstance ( custom_config_class, type ) : # TODO Aquí debería ser type, object o SuccessConfig?
          raise TypeError ( "SUCCESS_CUSTOM_CONFIG_CLASS debe ser una clase válida." )

        # Aplicar override selectivo
        app.config.from_object ( custom_config_class )
        app.logger.info ( f"✅ Configuración personalizada cargada desde '{custom_config_path}'." )

      except ( ImportError, AttributeError, TypeError ) as e :
        app.logger.error ( f"❌ Error cargando configuración personalizada: {e}" )

    else :
      app.logger.info ( "✅ Configuración estándar del framework cargada." )
