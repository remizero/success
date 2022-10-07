# Python Libraries / Librerías Python
from flask import Flask
from flask_cors import CORS
import ast
import os


# Application Libraries / Librerías de la Aplicación
from kernel import Extension
from utils import EnvVar


# Preconditions / Precondiciones


class Cors ( Extension ) :

  __corsConfigDefault = {}
  __resources = None
  __supports_credentials = False

  def __init__ ( self ) -> None :
    super ().__init__ ()
    self.extension = CORS ()
    self.__corsConfigDefault = {
      r"*" : {
        "origins" : [ "/*" ],
        "methods" : [ "DELETE", "GET", "POST", "PUT" ],
        "allow_headers" : [ "Authorization", "Content-Type", "X-Requested-With", "Accept", "Set-Cookie" ],
        "expose_headers" : [ "Content-Type", "X-CSRFToken" ]
      }
    }

  def config ( self ) -> None :

    # DO NOT MODIFY (BEGIN) / NO MODIFICAR (INICIO)
    if ( not EnvVar.isEmpty ( 'CORS_RESOURCES_APP_RESOURCES' ) ) :

      self.__resources = self.__corsConfigDefault
      #self.__resources = EnvVar.getCorsResources ()

    elif ( not EnvVar.isEmpty ( 'CORS_RESOURCES' ) ) :

      # TODO Que hacer aqui
      self.__resources = self.__corsConfigDefault
      #pass

    else :

      self.__resources = self.__corsConfigDefault
    # DO NOT MODIFY (END) / NO MODIFICAR (FIN)

  def register ( self, _app : Flask ) -> None :
    super ().register ( _app )
    if ( EnvVar.get ( 'CORS_SUPPORTS_CREDENTIALS' ) != '' ) :
      self.__supports_credentials = EnvVar.isTrue ( 'CORS_SUPPORTS_CREDENTIALS' )
    self.extension.init_app (
      app = _app,
      resources = self.__resources,
      supports_credentials = self.__supports_credentials
    )

  def userConfig ( self, **kwargs ) -> None :
    pass
