# Python Libraries / Librerías Python
from dotenv import dotenv_values
from dotenv import load_dotenv
from flask  import json
from typing import Any, Dict, Optional
import ast
import os

# Success Libraries / Librerías Success
from success.common.infra.config.SuccessEnvProvider import SuccessEnvProvider
from success.common.tools.SuccessEnv                import SuccessEnv

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


class SuccessSystemEnv ( SuccessEnvProvider ) :


  @classmethod
  def __init__ ( cls, envFilePath : str = None ) -> None :

    SuccessEnv.loadEnv ( envFilePath )


  @classmethod
  def get ( cls, key : str, default = None ) -> str :

    return os.environ.get ( key, default )


  @classmethod
  def getJson ( cls, key : str ) -> Any : 

    return json.loads ( cls.get ( key ) )


  @classmethod
  def isEmpty ( cls, key : str ) -> bool :

    return ( cls.get ( key ) == '' )


  @classmethod
  def isTrue ( cls, key : str ) -> bool :
    
    return ( cls.get ( key ).lower () == 'true' )


  @classmethod
  def toInt ( cls, key : str ) -> int :

    return int ( cls.get ( key ) )
