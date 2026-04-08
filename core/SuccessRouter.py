from flask import redirect
from success.helpers.url import success_url_for, success_redirect


class SuccessRouter:
    """
    Router semántico que permite construir redirecciones y rutas entre apps de forma sencilla.
    """

    @staticmethod
    def to(app: str, Action: str, code: int = 302, **values):
        """
        Redirecciona a un Action específico en otra app.

        Ejemplo:
            return SuccessRouter.to("feeder", "dashboard.index")
        """
        return success_redirect(Action, app=app, code=code, **values)

    @staticmethod
    def url(app: str, Action: str, **values) -> str:
        """
        Devuelve la URL absoluta o relativa a un Action en otra app.

        Ejemplo:
            SuccessRouter.url("adminus", "users.view", id=5)
        """
        return success_url_for(Action, app=app, **values)
