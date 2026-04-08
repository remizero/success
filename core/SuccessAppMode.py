# Python Libraries / Librerías Python
import sys
import inspect
import os

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessAppMode () :


  @staticmethod
  def __isMode ( mode : str ) -> bool :

    return os.environ.get ( 'APP_ENV' ) == mode


  @staticmethod
  def isDebugMode () -> bool :

    return bool ( os.environ.get ( 'FLASK_DEBUG' ) ) or bool ( os.environ.get ( 'DEBUG' ) )


  @staticmethod
  def isDefaultMode () -> bool :
    
    return SuccessAppMode.__isMode ( 'default' )


  @staticmethod
  def isDevelopmentMode () -> bool :

    return SuccessAppMode.__isMode ( 'development' )


  @staticmethod
  def isLocalMode () -> bool :

    return SuccessAppMode.__isMode ( 'local' )


  @staticmethod
  def isProductionMode () -> bool :

    return SuccessAppMode.__isMode ( 'production' )


  @staticmethod
  def isTestingMode () -> bool :

    return bool ( os.environ.get ( 'SUCCESS_TESTING' ) )


  @staticmethod
  def isStagingMode () -> bool :

    return bool ( os.environ.get ( 'SUCCESS_STAGING' ) )
