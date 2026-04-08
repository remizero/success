
from success.core.SuccessSubdomainDispatcher import SuccessSubdomainDispatcher


# class DebugSubdomainDispatcher(SuccessSubdomainDispatcher):

#     def __init__(self, real_dispatcher):
#         self.real = real_dispatcher

#     def __call__(self, environ, start_response):
#         host = environ.get("HTTP_HOST", "")
#         print("\n[Dispatcher] Host recibido:", host)

#         selected = self.get_application(host)
#         print("[Dispatcher] App seleccionada:", getattr(selected, "import_name", selected))

#         return selected(environ, start_response)

class DebugSubdomainDispatcher:
    def __init__(self, dispatcher : SuccessSubdomainDispatcher, logger=None):
        self._dispatcher = dispatcher
        self._logger = logger or print

    def __getattr__(self, name):
        """
        Delegate every attribute and method to the original dispatcher.
        Only intercept what we explicitly override.
        """
        return getattr(self._dispatcher, name)

    def __call__(self, environ, start_response):
        host = environ.get("HTTP_HOST", "<unknown>")
        self._logger(f"[DebugSubdomainDispatcher] Incoming HOST={host}")

        # call real dispatcher
        return self._dispatcher(environ, start_response)

    def get_application(self, host):
        self._logger(f"[DebugSubdomainDispatcher] Resolving host={host}")
        app = self._dispatcher.get_application(host)
        self._logger(f"[DebugSubdomainDispatcher] Selected app={app}")
        return app
