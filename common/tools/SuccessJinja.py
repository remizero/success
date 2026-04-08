# Python Libraries / Librerías Python
from flask import Flask

# Success Libraries / Librerías Success
from success.common.tools.SuccessEnv import SuccessEnv
from success.common.tools.SuccessUrl import SuccessUrl

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones



class SuccessJinja () :


  @staticmethod
  def registerMethods ( app : Flask ) :
    app.jinja_env.globals [ 'successUrlFor' ]   = SuccessUrl.urlFor
    app.jinja_env.globals [ 'successRedirect' ] = SuccessUrl.redirect
