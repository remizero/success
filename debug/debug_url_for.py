
from flask import url_for as flask_url_for

def debug_url_for(Action, **values):
    url = flask_url_for(Action, **values)
    print(f"[url_for] {Action} -> {url}")
    return url

# Monkey patch global
import builtins
builtins.url_for = debug_url_for
