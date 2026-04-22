# Python Libraries / Librerías Python
from flask import Flask

# Success Libraries / Librerías Success
from success.common.tools.SuccessUrl import SuccessUrl

# Preconditions / Precondiciones



class SuccessJinja () :
  """
  Jinja2 template utilities for the Success framework.

  Provides methods for registering custom Jinja2 globals and filters.
  """


  @staticmethod
  def registerMethods ( app : Flask ) :
    """
    Register custom Jinja2 methods in the Flask application.

    Registers SuccessUrl methods as global template functions.

    Args:
      app: Flask application instance.
    """
    app.jinja_env.globals [ 'successUrlFor' ]   = SuccessUrl.urlFor
    app.jinja_env.globals [ 'successRedirect' ] = SuccessUrl.redirect
