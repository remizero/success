
from werkzeug.routing import MapAdapter

class DebugRequestContext:
    def __init__(self, app):
        self.app = app
        self.original = app.request_context

    def __call__(self, environ):
        ctx = self.original(environ)

        adapter: MapAdapter = ctx.url_adapter
        print("\n[Router] PATH_INFO:", environ.get("PATH_INFO"))
        print("[Router] SCRIPT_NAME:", environ.get("SCRIPT_NAME"))
        print("[Router] SUBDOMAIN:", adapter.subdomain)

        try:
            Action, args = adapter.match()
            print("[Router] Action:", Action)
            print("[Router] Args:", args)
        except Exception as e:
            print("[Router] Match ERROR:", e)

        return ctx
