# Python Libraries / Librerías Python
from flask import Flask
import time
from werkzeug.routing.rules import Rule

# Success Libraries / Librerías Success
from success.common.tools.SuccessColor import SuccessColor
from success.core.SuccessContext       import SuccessContext

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessSystemState () :

  _start_time    = None
  _env           = "unknown"
  _logger_file   = False
  _apps_cargadas = []
  _apps_omitidas = {}


  @staticmethod
  def startTimer () :
    SuccessSystemState._start_time = time.perf_counter ()


  @staticmethod
  def stopTimer () :
    if SuccessSystemState._start_time is None :
      return 0
    return int ( ( time.perf_counter () - SuccessSystemState._start_time ) * 1000 )


  @staticmethod
  def setEnv ( env ) :
    SuccessSystemState._env = env


  @staticmethod
  def setLoggerFile ( enabled ) :
    SuccessSystemState._logger_file = enabled


  @staticmethod
  def addAppCargada ( app ) :
    SuccessSystemState._apps_cargadas.append ( app )


  @staticmethod
  def addAppOmitida ( path, reason = "Desconocido" ) :
    SuccessSystemState._apps_omitidas [ path ] = reason


  @staticmethod
  def getAppStats () :
    total = len ( SuccessSystemState._apps_cargadas ) + len ( SuccessSystemState._apps_omitidas )
    activas = len ( SuccessSystemState._apps_cargadas )
    omitidas = len ( SuccessSystemState._apps_omitidas )

    return total, activas, omitidas


  @staticmethod
  def report ( logger = None ) :
    ms = SuccessSystemState.stopTimer ()
    logger_type = "Sí (archivo/log externo)" if SuccessSystemState._logger_file else "No (solo consola)"
    total, activas, omitidas = SuccessSystemState.getAppStats ()
    session_id = SuccessContext ().getSuccessValue ( "SESSION_ID" )

    lines = [
      f"\n"
      f"🔥 Success System Summary ({SuccessSystemState._env.upper ()}):",
      f"{SuccessColor.level ( '├──' )} {SuccessColor.tag ( 'Entorno' )}:            {SuccessSystemState._env}",
      f"{SuccessColor.level ( '├──' )} {SuccessColor.tag ( 'Tiempo de arranque' )}: {ms}ms",
      f"{SuccessColor.level ( '├──' )} {SuccessColor.tag ( 'SuccessLogger' )}:      {logger_type}",
      f"{SuccessColor.level ( '├──' )} {SuccessColor.tag ( 'SuccessSession ID' )}:  {session_id}",
      f"{SuccessColor.level ( '├──' )} {SuccessColor.tag ( 'Aplicaciones' )}:"
    ]

    for i, app in enumerate ( SuccessSystemState._apps_cargadas ) :
      lines.append ( f"{SuccessColor.level ( '│   │' )}" )
      is_last_app = i == len ( SuccessSystemState._apps_cargadas ) - 1
      app_prefix = '│   └── ' if is_last_app else '│   ├──'

      app_name = getattr ( app, "import_name", "unknown_app" )
      lines.append ( f"{SuccessColor.level ( app_prefix )} {SuccessColor.tag ( 'AppName' )}: {app_name}" )

      # Blueprints
      blueprints = list ( app.blueprints.keys () )
      lines.append ( f"{SuccessColor.level ( app_prefix.replace ( '├', '│   ├' ) )} {SuccessColor.tag ( 'Blueprints' )}:  {', '.join ( blueprints ) or '—'}" )

      # Extensiones
      ext_names = list ( app.extensions.keys () )
      lines.append ( f"{SuccessColor.level ( app_prefix.replace ( '├', '│   ├' ) )} {SuccessColor.tag ( 'Extensiones' )}: {', '.join ( ext_names ) or '—'}" )
 
      # Hooks
      hooks = getattr ( app, "success_hooks", {} )
      lines.append ( f"{SuccessColor.level ( app_prefix.replace ( '├', '│   ├' ) )} {SuccessColor.tag ( 'Hooks' )}:       {len ( hooks )} ({', '.join ( hooks ) or '—'})" )

      # Rutas
      rules = list ( app.url_map.iter_rules () )

      # Pre-cálculo de longitudes máximas por campo
      max_method = max ( ( len ( list ( rule.methods - {'HEAD', 'OPTIONS'} ) [ 0 ] ) for rule in rules), default = 0 )
      max_rule   = max ( ( len ( rule.rule ) for rule in rules), default = 0 )
      max_host   = max ( ( len ( rule.host or "" ) for rule in rules), default = 0 )
      max_subdom = max ( ( len ( rule.subdomain or "" ) for rule in rules), default = 0 )
      max_ep     = max ( ( len ( rule.endpoint or "" ) for rule in rules), default = 0 )

      # Formateo bonito con los anchos calculados
      lines.append ( f"{SuccessColor.level ( app_prefix.replace ( '├', '│   └' ) )} {SuccessColor.tag ( 'Rutas' )}:" )
      for j, rule in enumerate ( rules ) :
        method       = list ( rule.methods - {'HEAD', 'OPTIONS'} ) [ 0 ]
        route_prefix = '│   │       └──' if j == len ( rules ) - 1 else '│   │       ├──'
        
        lines.append (
          f"{SuccessColor.level ( route_prefix )} "
          f"{method:<{max_method}}  "
          f"{rule.rule:<{max_rule}} "
          f"{SuccessColor.tag ( 'host' )}={rule.host or '':<{max_host}}   "
          f"{SuccessColor.tag ( 'subdomain' )}={rule.subdomain or '':<{max_subdom}}   "
          f"{SuccessColor.tag ( 'Action' )}={rule.endpoint or '':<{max_ep}}"
        )

    lines.append ( f"{SuccessColor.level ( '├──' )} Total apps detectadas:      {total}" )
    lines.append ( f"{SuccessColor.level ( '├──' )} Total apps omitidas:    {omitidas} / {total}" )
    lines.append ( f"{SuccessColor.level ( '└──' )} Total apps activas:     {activas} / {total}" )

    for app in SuccessSystemState._apps_cargadas :
      lines.append ( f"app.import_name {app.import_name}" )
      lines.append ( f"app.config [ SERVER_NAME] {app.config [ 'SERVER_NAME' ]}" )
      lines.append ( f"app.config [ SUCCESS_APP_MAIN] {app.config [ 'SUCCESS_APP_MAIN' ]}" )

    summary = "\n".join ( lines ) + "\n" + f"{SuccessColor.level ( '─' )}" * 150 + "\n🔧 Generated by Success Engine ⛓️"

    if logger:
      logger.log(summary, "INFO")
      for path, reason in SuccessSystemState._apps_omitidas.items():
        logger.log(f"[SKIP] {path} → {reason}", "INFO")

    else:
      print(summary)
      for path, reason in SuccessSystemState._apps_omitidas.items():
        print(f"[SKIP] {path} → {reason}")

  #   # 🔸 Guardar si se solicita
  #   if save_to_file:
  #       import os, json, datetime
  #       output_dir = output_dir or os.getcwd()
  #       now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
  #       file_ext = "json" if as_json else "log"
  #       filename = f"success_report_{now}.{file_ext}"
  #       full_path = os.path.join(output_dir, filename)

  #       try:
  #           with open(full_path, "w", encoding="utf-8") as f:
  #               if as_json:
  #                   json.dump(summary_data, f, indent=2, ensure_ascii=False)
  #               else:
  #                   f.write(output + "\n")
  #           print(f"✅ Reporte exportado a {full_path}")
  #       except Exception as e:
  #           print(f"❌ Error exportando el reporte: {e}")

