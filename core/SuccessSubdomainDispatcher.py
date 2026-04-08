# Python Libraries / Librerías Python
from flask               import Flask
from threading           import Lock
from werkzeug.exceptions import NotFound
from flask import url_for

# Success Libraries / Librerías Success
from success.common.base.SuccessClass import SuccessClass

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessSubdomainDispatcher ( SuccessClass ) :


  def __init__ ( self, domain : str, create_app : dict [ str, Flask ] ) :
    super ().__init__ ()
    self.domain     = domain
    self.create_app = create_app
    self.lock       = Lock ()
    self.instances  = {}


  def get_application ( self, host : str ) :
    host = host.split ( ':' ) [ 0 ]
    self._logger.log ( f"self.domain {self.domain}", "ERROR" )
    self._logger.log ( f"host {host}", "ERROR" )
    assert host.endswith ( self.domain ), 'Configuration error'
    subdomain = host [ : -len ( self.domain ) ].rstrip ( '.' )
    self._logger.log ( f"subdomain = {subdomain}", "ERROR" )
    with self.lock :
      app = self.instances.get ( subdomain )
      if app is None :
        self._logger.log ( f"type(self.create_app) = {type ( self.create_app )}", "ERROR" )
        self._logger.log ( f"self.create_app = {self.create_app}", "ERROR" )
        # print(f"type(self.app_map) = {type(self.app_map)}")
        # app = self.create_app ( subdomain )
        app = self.create_app.get(subdomain) or self.create_app.get(f"/{subdomain}")
        self.instances [ subdomain ] = app
        with app.app_context () :
          self._logger.log ( f"url_for('static', filename='js/chromadb/base.js') = {url_for('static', filename='js/chromadb/base.js')}", "ERROR" )
          self._logger.log ( f"app.config['SERVER_NAME'] = {app.config['SERVER_NAME']}", "ERROR" )
          for rule in app.url_map.iter_rules():
            self._logger.log ( f"rule, rule.subdomain, rule.Endpoint = {rule}, {rule.subdomain}, {rule.endpoint}", "ERROR" )
      return app


  def __call__ ( self, environ, start_response ) :
    app = self.get_application ( environ [ 'HTTP_HOST' ] )
    self._logger.log ( f"app {app}", "ERROR" )
    self._logger.log ( f"environ [ 'HTTP_HOST' ] {environ [ 'HTTP_HOST' ]}", "ERROR" )
    return app ( environ, start_response )

# antiguo sistema de subdominios que parece mas bien una versión path
# class SuccessSubdomainDispatcher ( SuccessClass ) :

#   def __init__ ( self, mainApp : Flask, mounts : dict [ str, Flask ], domain : str = "localhost" ) :
#     super ().__init__ ()
#     self.domain   = domain
#     self.main_app = mainApp
#     self.mounts   = mounts or {}


#   def __call__ ( self, environ, start_response ) :
#       host = environ.get ( "HTTP_HOST", "" )
#       host_no_port = host.split ( ":" ) [ 0 ]

#       if not host_no_port.endswith ( self.domain ) :
#         return NotFound () ( environ, start_response )

#       subdomain_part = host_no_port.removesuffix ( "." + self.domain )

#       if not subdomain_part or subdomain_part == host_no_port :
#         # No subdominio -> app principal
#         app = self.main_app

#       else :
#         app = self.mounts.get ( subdomain_part, None )
#         if app is None :
#           return NotFound () ( environ, start_response )

#       return app ( environ, start_response )

  # def __init__ ( self, domain : str, apps : dict [ str, Flask ] ) :
  #   super ().__init__ ()
  #   self.domain = domain
  #   self.apps   = {}  # Mapa: subdominio -> app
  #   self.lock   = Lock ()

  #   # Transformamos keys del estilo "/admin" en subdominios: "admin"
  #   for path_key, app in apps.items () :
  #     subdomain = path_key.strip ( "/" ).lower ()
  #     self.apps [ subdomain ] = app

  #   self._logger.log ( "Cargando el sub-sistema SuccessSubdomainDispatcher.", "INFO" )


  # def __init__ ( self, domain : str, mainApp : str, apps : dict [ str, Flask ] ) :
  #   super ().__init__ ()
  #   self.domain         = domain
  #   self.lock           = Lock ()
  #   self.apps           = {}
  #   self.main_app       = None
  #   self.main_subdomain = None

  #   for path_key, app in apps.items () :
  #     subdomain               = path_key.strip ( "/" ).lower ()
  #     print ( f"subdomain {subdomain}" )
  #     self.apps [ subdomain ] = app

  #     if subdomain == mainApp :
  #       self.main_app       = app
  #       self.main_subdomain = subdomain
  #       print ( f"self.main_app {self.main_app}" )
  #       print ( f"self.main_subdomain {self.main_subdomain}" )

  #   print ( f"self.apps {self.apps}" )

  #   self._logger.log ( "Cargando el sub-sistema SuccessSubdomainDispatcher.", "INFO" )

  # def get_application ( self, host : str ) :
  #   host = host.split ( ":" ) [ 0 ]
  #   if not host.endswith ( self.domain ) :
  #     return NotFound () ( None, None )

  #   subdomain = host [ : -len ( self.domain ) ].rstrip ( "." ).lower ()

  #   with self.lock :
  #     app = self.apps.get ( subdomain )
  #     if app :
  #       return app

  #   self._logger.log ( f"Subdominio desconocido: {subdomain}.{self.domain}", "WARNING" )
  #   return NotFound () ( None, None )
  # def get_application ( self, host : str ) :
  #   self.domain = host.split ( ":" ) [ 0 ]
  #   # self.domain = host
  #   print ( f"self.domain {self.domain}" )
  #   if not host.endswith ( self.domain ) :
  #     return NotFound () ( None, None )

  #   subdomain = host [ : -len ( self.domain ) ].rstrip ( "." ).lower ()
  #   print ( f"subdomain {subdomain}" )

  #   with self.lock :
  #     app = self.apps.get ( subdomain )
  #     if app :
  #       return app

  #   self._logger.log ( f"Subdominio desconocido: {subdomain}.{self.domain}", "WARNING" )
  #   return NotFound () ( None, None )
  # def get_application(self, host: str):
  #   # ⚙️ Normaliza quitando el puerto
  #   host_no_port = host.split(":")[0]  # Ej: 'prueba_view.localhost'

  #   self.domain = "localhost"  # Tu dominio base real sin subdominios
  #   print(f"host {host} → host_no_port {host_no_port}")
  #   print(f"self.domain {self.domain}")

  #   # ✅ Si es la app principal (sin subdominio)
  #   if host_no_port == self.domain:
  #       print("[DISPATCHER] Accediendo a app principal")
  #       return self.main_app

  #   # 🧠 Extrae subdominio
  #   if host_no_port.endswith(f".{self.domain}"):
  #       subdomain = host_no_port[: -len(self.domain) - 1].lower()
  #       print(f"[DISPATCHER] subdomain '{subdomain}'")

  #       with self.lock:
  #           app = self.apps.get(subdomain)
  #           if app:
  #               return app

  #       self._logger.log(f"Subdominio desconocido: {subdomain}.{self.domain}", "WARNING")
  #       return NotFound()
    
  #   # 🧨 Si no coincide con el dominio base
  #   print(f"[DISPATCHER] Dominio inválido: {host_no_port}")
  #   return NotFound()


  # def __call__ ( self, environ, start_response ) :
  #   host = environ.get ( "HTTP_HOST", "" )
  #   print ( f"host {host}" )
  #   app = self.get_application ( host )
  #   return app ( environ, start_response )
