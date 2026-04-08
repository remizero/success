# Python Libraries / Librerías Python
from typing import Any
import json
import importlib

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessEndpointBuilder () :

  _json_path      : str = None
  _endpoints_data : Any = None


  def __init__ ( self, json_path : str ) -> None :
    self._json_path = json_path
    self._endpoints_data = self._load_json ()


  def _load_json ( self ) -> Any :
    with open ( self._json_path, "r", encoding = "utf-8" ) as f :
      return json.load ( f )


  def build ( self ) :
    """Registra todos los endpoints en sus blueprints correspondientes"""
    for ep_data in self._endpoints_data :
      # Importar blueprint dinámicamente
      bp_module = importlib.import_module ( ep_data [ "blueprint_import" ].rsplit ( '.', 1 ) [ 0 ] )
      bp = getattr ( bp_module, ep_data [ "blueprint_var" ] )

      # Importar clase Endpoint dinámica
      endpoint_module = importlib.import_module ( ep_data [ "endpoint_class" ].rsplit ( '.', 1 ) [ 0 ] )
      endpoint_cls = getattr ( endpoint_module, ep_data [ "endpoint_class" ].rsplit ( '.' ) [ -1 ] )

      # Construir view_func
      view_func = endpoint_cls.as_view ( ep_data [ "endpoint_name" ] )

      # Registrar en Flask
      kwargs = ep_data.get ( "additional_options", {} )
      if ep_data.get ( "host" ) :
        kwargs [ "host" ] = ep_data [ "host" ]

      bp.add_url_rule (
        rule = ep_data [ "rule" ],
        view_func = view_func,
        methods = ep_data.get ( "methods" ),
        **kwargs
      )
