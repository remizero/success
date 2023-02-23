# Python Libraries / Librerías Python
from flask import Flask


# Application Libraries / Librerías de la Aplicación
from kernel.patterns.creational.factoryMethod import ConfigFM
from extensions                               import cors
from extensions                               import database
from extensions                               import email
from extensions                               import jwt
from extensions                               import marshmallow
from extensions                               import redis
from extensions                               import session
from kernel                                   import Blueprints
from managers                                 import EnvVar
from utils                                    import Application


# Preconditions / Precondiciones
"""
  DEFINITION OF CONFIGURATION POLICIES TO WORK WITH THE SUCCESS APPLICATION /
  DEFINICION DE POLITICAS DE CONFIGURACION PARA TRABAJAR CON LA APLICACION SUCCESS
"""
# config = Config ()


class Success () :

  __success : Flask = None

  def create ( self ) :
    """
      CREATION OF THE FLASK APPLICATION /
      CREACION DE LAS APLICACION FLASK
    """
    #self.__success = App ( __name__, instance_relative_config = True )
    self.__success = Flask ( __name__, instance_relative_config = True )
    # self.__success.config.from_object ( Application.getConfigClass ( config ) )
    self.__success.config.from_object ( ConfigFM.create () )
    self.__success.config.from_pyfile ( Application.getConfigFile (), silent = True )
    if ( EnvVar.isTrue ( 'SUCCESS_EXTENSION_EMAIL' ) ) :
      email.register ( self.__success )
    # ---------------------------------------
    # AQUI DEBERIA IR LA CLASE LOGGER
    # ---------------------------------------
    if ( EnvVar.isTrue ( 'SUCCESS_EXTENSION_CORS' ) ) :
      cors.register ( self.__success )
    if ( EnvVar.isTrue ( 'SUCCESS_EXTENSION_JWT' ) ) :
      jwt.register ( self.__success )
    if ( EnvVar.isTrue ( 'SUCCESS_EXTENSION_REDIS' ) ) :
      redis.register ( self.__success )
    if ( EnvVar.isTrue ( 'SUCCESS_EXTENSION_SESSION' ) ) :
      session.register ( self.__success )
    if ( EnvVar.isTrue ( 'SUCCESS_EXTENSION_SQLALCHEMY' ) ) :
      database.register ( self.__success )
    if ( EnvVar.isTrue ( 'SUCCESS_EXTENSION_MARSHMALLOW' ) ) :
      marshmallow.register ( self.__success )
    """
      CONFIGURATION FOR HANDLING SUCCESS SYSTEM ROUTES /
      CONFIGURACIÓN PARA EL MANEJO DE LAS RUTAS DEL SISTEMA SUCCESS
    """
    Blueprints.register ( self.__success )

  def addExtension ( extension ) -> None :
    pass

  def getApp ( self ) -> Flask :
    return self.__success
