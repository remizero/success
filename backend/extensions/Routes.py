# Python Libraries / Librerías Python
from flask import Flask
from flask_restful import Api


# Application Libraries / Librerías de la Aplicación
from kernel import Extension
from app.api.auth.signin import Signin


# Preconditions / Precondiciones


class Routes ( Extension ) :

  def __init__ ( self ) -> None :
    super ().__init__ ()

  def config ( self ) -> None :
    pass

  def register ( self, _app : Flask, _api : Api ) -> None :
    super ().register ( _app )
    # Aqui se registran todas las rutas
    #signin = Signin ()
    #_app.add_url_rule ( '/signin', 'Signin', signin.post (), methods = [ 'POST' ] )
    #_api.add_resource ( Signin, '/admin/signin', endpoint = '/admin/signin' )
    _api.add_resource ( Signin, '/signin' )

  def userConfig ( self, **kwargs ) -> None :
    pass
