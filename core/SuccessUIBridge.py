import inspect
from typing import Callable

__UI_REGISTRY__ = {}


def success_ui(name: str = None, icon: str = None, order: int = 100):
    """
    Decorador para marcar una función como expuesta al sistema UI (menús, dashboards, etc).
    Guarda metadatos opcionales como nombre, ícono o prioridad.
    """
    def wrapper(func: Callable):
        Action = func.__name__
        mod = inspect.getmodule(func)
        app_name = mod.__name__.split(".")[1] if "apps." in mod.__name__ else "unknown"

        __UI_REGISTRY__[f"{app_name}:{Action}"] = {
            "app": app_name,
            "Action": Action,
            "name": name or Action.replace("_", " ").title(),
            "icon": icon,
            "order": order,
            "func": func,
        }
        return func
    return wrapper


class SuccessUIBridge:
    """
    Servicio que permite consultar los endpoints registrados para UI.
    """

    @staticmethod
    def get_registry():
        """
        Devuelve todos los endpoints registrados por apps con @success_ui.
        """
        return list(__UI_REGISTRY__.values())

    @staticmethod
    def get_for_app(app_name: str):
        """
        Devuelve todos los endpoints registrados para una app específica.
        """
        return [v for k, v in __UI_REGISTRY__.items() if v['app'] == app_name]

    @staticmethod
    def as_menu_tree():
        """
        Devuelve un árbol simple agrupado por app, ordenado por prioridad.
        """
        tree = {}
        for item in SuccessUIBridge.get_registry():
            tree.setdefault(item['app'], []).append(item)

        for items in tree.values():
            items.sort(key=lambda x: x['order'])

        return tree
