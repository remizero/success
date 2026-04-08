from flask import Flask, request, g
from success.env import SuccessEnv
from success.helpers.url import success_url_for, success_redirect


class SuccessAutoContext:

    @staticmethod
    def inject(app: Flask):
        """
        Inyecta variables globales y helpers automáticos en Jinja2 para todas las apps Success.
        """

        # Variables de entorno
        app.jinja_env.globals['env']        = SuccessSystemEnv.get("APP_ENV", "development")
        app.jinja_env.globals['app_name']   = app.name

        # Helpers URL
        app.jinja_env.globals['successUrlFor']   = success_url_for
        app.jinja_env.globals['successRedirect'] = success_redirect

        # Acceso al usuario (si estás usando Flask-Login u otro sistema similar)
        @app.context_processor
        def inject_user():
            user = getattr(g, 'user', None) or getattr(request, 'user', None) or None
            return dict(current_user=user)

        # Cualquier otro futuro helper...
        # app.jinja_env.globals['customHelper'] = ...

        return app
