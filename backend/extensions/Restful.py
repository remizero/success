# Python Libraries / Librerías Python
from flask import Flask
from flask_restful import Api


# Application Libraries / Librerías de la Aplicación
from kernel import Extension


# Preconditions / Precondiciones

# https://blog.apilayer.com/kick-starting-apis-using-flask-restful/
# https://stackoverflow.com/questions/53909695/2-get-routes-to-same-resource-in-flask-restful
# https://splunktool.com/how-do-i-access-a-resource-with-multiple-endpoints-with-flaskrestful
# https://flask-restful.readthedocs.io/en/latest/
# https://dev.to/paurakhsharma/flask-rest-api-part-0-setup-basic-crud-api-4650
# https://github.com/paurakhsharma/flask-rest-api-blog-series
class Restful ( Extension ) :

  def __init__ ( self ) -> None :
    super ().__init__ ()
    self.extension = Api ()

  def config ( self ) -> None :
    pass

  def register ( self, _app : Flask ) -> None :
    super ().register ( _app )
    self.extension.init_app ( _app )

  def userConfig ( self, **kwargs ) -> None :
    pass
