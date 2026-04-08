# Python Libraries / Librerías Python
from flask import Flask

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessAppPlaceholderFactory () :

  @classmethod
  def build ( cls ) -> Flask :
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