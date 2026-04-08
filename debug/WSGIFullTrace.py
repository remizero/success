

class WSGIFullTrace:
    def __init__(self, app, name="WSGIFullTrace", deep=False):
        self.app = app
        self.name = name
        self.deep = deep

    def __call__(self, environ, start_response):
        print("\n\n==============================")
        print(f"[{self.name}] INCOMING REQUEST")
        print("==============================")

        print("\n--- RAW WSGI ENVIRON ---")
        for k, v in environ.items():
            print(f"{k}: {v}")

        # Monkey patch start_response
        def traced_start_response(status, headers, exc_info=None):
            print("\n--- START RESPONSE ---")
            print(f"Status: {status}")
            for header in headers:
                print(f"{header[0]}: {header[1]}")
            print("--- END HEADERS ---\n")
            return start_response(status, headers, exc_info)

        result = self.app(environ, traced_start_response)

        if self.deep:
            print("\n--- RESPONSE BODY (FIRST CHUNK) ---")
            try:
                preview = next(iter(result))
                print(preview[:3000])  # evitar explosiones
            except Exception as e:
                print(f"ERROR reading response: {e}")

        print(f"\n[{self.name}] END REQUEST")
        print("==============================\n\n")

        return result
