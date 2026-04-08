# Python Libraries / Librerías Python
from flask  import Blueprint
from typing import Any
import json
import os


# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones
BLUEPRINT_ALLOWED_ARGS = {
  "name",
  "import_name",
  "static_folder",
  "static_url_path",
  "template_folder",
  "url_prefix",
  "subdomain",
  "url_defaults",
  "root_path",
  "cli_group",
}

# Funciones auxiliares
def generate_blueprint_name(bp_path: str) -> str:
    parts = bp_path.replace(os.sep, ".").split(".")
    parts = [p for p in parts if p not in ("apps", "src", "view")]
    return "_".join(parts)

def get_subdomain(env_key="SUCCESS_SUBDOMAIN", default=None):
    return os.environ.get(env_key, default)


class SuccessBlueprintBuilder () :

  _json_path      : str = None
  _endpoints_data : Any = None

  
  def __init__ ( self, json_path : str ) -> None :
    self.json_path = json_path
    self.blueprints_data = self._load_json ()


  def _load_json ( self ) :
    with open ( self.json_path, "r", encoding = "utf-8" ) as f :
      return json.load ( f )


  def build ( self ) :
    blueprints = []

    for bp_data in self.blueprints_data :
      kwargs = {}

      # GENERACIÓN DINÁMICA DE CAMPOS CLAVE
      bp_data [ "name" ]        = bp_data.get ( "name" ) or generate_blueprint_name ( bp_data [ "path" ] )
      bp_data [ "import_name" ] = bp_data.get ( "import_name" ) or "__name__"
      bp_data [ "subdomain" ]   = bp_data.get ( "subdomain" ) or get_subdomain ()

      for key, value in bp_data.items () :
        if key not in BLUEPRINT_ALLOWED_ARGS :
          continue

        if value is None:
          continue

        kwargs [ key ] = value

      bp = Blueprint ( **kwargs )
      blueprints.append ( bp )

    return blueprints

  # def build ( self ) :
  #   """Devuelve una lista de objetos Flask Blueprint"""
  #   blueprints = []
  #   for bp_data in self.blueprints_data :
  #     # Convertir claves null -> None
  #     bp_data = { k: ( v if v is not None else None ) for k, v in bp_data.items () }

  #     bp = Blueprint (
  #       name = bp_data [ "name" ],
  #       import_name = bp_data [ "import_name" ],
  #       static_folder = bp_data.get ( "static_folder" ),
  #       static_url_path = bp_data.get ( "static_url_path" ),
  #       template_folder = bp_data.get ( "template_folder" ),
  #       url_prefix = bp_data.get ( "url_prefix" ),
  #       subdomain = bp_data.get ( "subdomain"),
  #       url_defaults = bp_data.get ( "url_defaults"),
  #       root_path = bp_data.get ( "root_path"),
  #       cli_group = bp_data.get ( "cli_group")
  #     )
  #     blueprints.append ( bp )
  #   return blueprints
