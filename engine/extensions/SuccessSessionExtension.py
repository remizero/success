# Python Libraries / Librerías Python
from flask         import Flask
from flask         import session
from flask_redis   import FlaskRedis
from flask_session import Session

# Application Libraries / Librerías de la Aplicación
from success.common.base.SuccessExtension import SuccessExtension
from success.common.tools.SuccessEnv      import SuccessEnv
from success.core.SuccessContext          import SuccessContext

# Preconditions / Precondiciones


class SuccessSessionExtension ( SuccessExtension ) :


  def __init__ ( self, app : Flask ) -> None :
    super ().__init__ ( app )
    self._extension = Session ()


  def config ( self ) -> None :
    redis = SuccessContext ().getExtension ( "SUCCESS_EXTENSION_REDIS" )
    if redis :
      self._app.config [ 'SESSION_REDIS' ] = redis


  # def set_user_session () :
  #   # self._extensions.
  #   sesion = FlaskSession ()
  #   print ( "Se está ejecutando la función def set_user_session () :..." )
  #   if 'user_token' not in session :
  #     print ( "Inicializando sesión de usuario..." )
  #     session [ 'user_token' ] = "test-token-supercow"
  #     session [ 'user_name' ] = "Superuser"
  #     session [ 'user_role' ] = "supercow"
  #     session [ 'tenant_list' ] = [ "default_tenant" ]

  #   g.user_token = session [ 'user_token' ]
  #   g.user_name = session [ 'user_name' ]


  def get_chroma_info () :
    try :
      headers = { "Authorization" : f"Bearer {session [ 'user_token' ]}" }

      # Versión e identidad son strings planos
      version_response = requests.get ( f"{CHROMA_API}/version", headers = headers )
      version = version_response.text if version_response.ok else "Desconocido"

      identity_response = requests.get ( f"{CHROMA_API}/auth/identity", headers = headers )
      identity = identity_response.json ().get ( "user_id" )

      # Heartbeat es JSON con clave
      heartbeat_response = requests.get ( f"{CHROMA_API}/heartbeat", headers = headers )
      if heartbeat_response.ok :
        heartbeat_data = heartbeat_response.json ()
        heartbeat_ns_raw = heartbeat_data.get ( "nanosecond heartbeat", None )
        heartbeat = format_heartbeat_ns ( heartbeat_ns_raw )
      else :
        heartbeat = "N/A"
    except Exception as e :
      version, identity, heartbeat = "Error", "Error", "Error"
    return headers, version, identity, heartbeat
