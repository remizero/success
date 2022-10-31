# Python Libraries / Librerías Python
from flask import Flask


# Application Libraries / Librerías de la Aplicación
from . import Config
from extensions import (
  cors,
  database,
  email,
  jwt,
  marshmallow,
  redis,
  session
)
from . import Blueprints
from utils import Application


# Preconditions / Precondiciones
"""
  DEFINITION OF CONFIGURATION POLICIES TO WORK WITH THE SUCCESS APPLICATION /
  DEFINICION DE POLITICAS DE CONFIGURACION PARA TRABAJAR CON LA APLICACION SUCCESS
"""
config = Config ()


class Success () :

  __success : Flask = None

  def create ( self ) :
    """
      CREATION OF THE FLASK APPLICATION /
      CREACION DE LAS APLICACION FLASK
    """
    #self.__success = App ( __name__, instance_relative_config = True )
    self.__success = Flask ( __name__, instance_relative_config = True )
    self.__success.config.from_object ( Application.getConfigClass ( config ) )
    self.__success.config.from_pyfile ( Application.getConfigFile (), silent = True )
    email.register ( self.__success )
    # ---------------------------------------
    # AQUI DEBERIA IR LA CLASE LOGGER
    # ---------------------------------------
    cors.register ( self.__success )
    jwt.register ( self.__success )
    redis.register ( self.__success )
    session.register ( self.__success )
    database.register ( self.__success )
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
