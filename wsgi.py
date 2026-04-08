# Python Libraries / Librerías Python
from werkzeug.serving import run_simple

# Application Libraries / Librerías de la Aplicación
from success.Success import Success
from success.debug.WSGIFullTrace import WSGIFullTrace

# Preconditions / Precondiciones
success = Success ()
success.create ()


if __name__ == "__main__" :
  # app = success.getApp ()
  # app = WSGIFullTrace ( app, "WSGI ENTRY", deep = False )
  run_simple ( '0.0.0.0', 5000, success.getApp (), use_reloader = True, use_debugger = True, use_evalex = True )
  # run_simple('0.0.0.0', 5000, app,
  #          use_reloader=True,
  #          use_debugger=True,
  #          use_evalex=True)
