# Python Libraries / Librerías Python
from flask import Flask, request
import uuid

# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessClass      import SuccessClass
from success.engine.context.RequestContext import RequestContext

# Preconditions / Precondiciones


class RequestContextMiddleware ( SuccessClass ) :

  __app : Flask = None


  def __init__( self, apps : Flask ) :
    super ().__init__ ()
    self.__app = apps
    self._registerHooks ()


  def _registerHooks ( self ) :
    @self.__app.before_request
    def _set_request_context () :
      # Generar un UUID único para cada request
      RequestContext.setRequestId ( str ( uuid.uuid4 () ) )
      # Asignar dinámicamente el app_id (por ruta actual)
      RequestContext.setAppId ()

    @self.__app.teardown_request
    def _clear_request_context ( exception = None ) :
      # Limpiar el contexto para evitar fugas entre threads
      RequestContext.clear ()
