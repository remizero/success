# Python Libraries / Librerías Python
from flask import Flask

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessAppPlaceholderFactory () :
  """
  Factory for creating placeholder Flask applications.

  Provides a default Flask application with a placeholder route
  when no main application is defined.
  """

  @classmethod
  def build ( cls ) -> Flask :
    """
    Build a placeholder Flask application.

    Returns:
      Flask: A Flask application instance with a default root route.
    """
    app = Flask ( "success_placeholder_root" )

    @app.route ( "/" )
    def root () :
      return (
        "<h1>🚧 App principal no definida</h1>"
        "<p>Estás viendo la app placeholder de Success.</p>"
        "<p>Define <code>SUCCESS_MAIN_APP</code> para cambiar esta vista.</p>",
        200,
      )

    return app