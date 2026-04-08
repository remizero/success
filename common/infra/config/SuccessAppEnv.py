# Python Libraries / Librerías Python
from dotenv import dotenv_values
from dotenv import load_dotenv
from flask  import json
from typing import Optional, Dict
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


class SuccessAppEnv ( SuccessEnvProvider ) :

  _data : dict [ str, Optional [ str ] ] = None


  def __init__ ( self, envFilePath : str = None ) -> None :

    self._data = SuccessEnv.loadAppEnv ( envFilePath )


  def get ( self, key : str, default = None ) -> str :

    return self._data.get ( key, default )
    

  def getJson ( self, key : str ) -> Any : 

    return json.loads ( self.get ( key ) )


  def isEmpty ( self, key : str ) -> bool :

    return ( self.get ( key ) == '' )


  def isTrue ( self, key : str ) -> bool :
    
    return ( self.get ( key ).lower () == 'true' )


  def toInt ( self, key : str ) -> int :

    return int ( self.get ( key ) )
  