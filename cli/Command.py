# Python Libraries / Librerías Python
from argparse import _SubParsersAction

# Success Libraries / Librerías Success
from success.cli.commands.AppCommand       import AppCommand
from success.cli.commands.EndpointCommand  import EndpointCommand
from success.cli.commands.ServiceCommand   import ServiceCommand
from success.cli.commands.AboutCommand     import AboutCommand
from success.cli.commands.ManifestoCommand import ManifestoCommand
from success.cli.commands.StatusCommand    import StatusCommand

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class Command () :


  @staticmethod
  def createApp ( subparsers : _SubParsersAction ) :
    parser = subparsers.add_parser ( "create-app", help = "Crea una nueva aplicación Success." )

    parser.add_argument ( "--app_name", type = str, required = True,                      help = "Nombre de la nueva aplicación." )
    parser.add_argument ( "--app-type", type = str, required = True, default = "restful", help = "Tipo de aplicación: restful, view, websocket, cli, etc. (default: restful)." )

    parser.set_defaults ( func = AppCommand.create )


  @staticmethod
  def createEndpoint ( subparsers : _SubParsersAction ) :
    parser = subparsers.add_parser ( "create-Action", help = "Agregar un Action a un servicio de una app." )

    parser.add_argument ( "--to-app",           required = True,                                    help = "Nombre de la app." )
    parser.add_argument ( "--protocol",         required = True,                                    help = "Protocolo (view, rest, ws, etc.)." )
    parser.add_argument ( "--service",          required = True,                                    help = "Servicio de referencia." )
    parser.add_argument ( "--version",          required = True,                                    help = "Versión." )
    parser.add_argument ( "--module",           required = True,                                    help = "Módulo." )
    parser.add_argument ( "--action",           required = True,                                    help = "Acción lógica del Action." )
    parser.add_argument ( "--method",           required = False, default = [ 'GET' ], nargs = '+', help = 'Métodos HTTP permitidos para el Action (GET, POST, PUT, DELETE, etc.)' )
    parser.add_argument ( "--controller",       required = False,                                   help = "Nombre del archivo de controlador (sin .py)" )
    parser.add_argument ( "--controller-class", required = False,                                   help = "Nombre de la clase del controlador (por defecto se infiere)" )

    parser.set_defaults ( func = EndpointCommand.create )


  @staticmethod
  def addService ( subparsers : _SubParsersAction ) :
    parser = subparsers.add_parser ( "add-service", help = "Agregar servicio base a una app (protocolo + referencia)" )

    parser.add_argument ( "--to-app",   required = True, help = "Nombre de la aplicación" )
    parser.add_argument ( "--protocol", required = True, help = "Protocolo de comunicación (rest, view, ws, graphql, etc.)" )
    parser.add_argument ( "--service",  required = True, help = "Nombre del servicio de referencia (e.g., chromadb, usuario, etc.)" )
    parser.add_argument ( "--version",  required = True, help = "Versión de la implementación del servicio de referencia (e.g., chromadb, usuario, etc.)" )

    parser.set_defaults ( func = ServiceCommand.create )


  @staticmethod
  def fixPackage ( subparsers : _SubParsersAction ) :
    parser = subparsers.add_parser ( "fix-packages", help = "Agrega __init__.py faltantes a una app" )

    parser.add_argument ( "--app", required = True, help = "Nombre de la aplicación que se desea revisar" )

    def fix_packages(args):
        app_path = Path("apps") / args.app
        if not app_path.exists():
          print(f"[ERROR] La app '{args.app}' no existe en apps/")
          return

        from utils.package_helper import PackageHelper
        PackageHelper.fix_all_inits(app_path)
        print(f"\n✅ Paquetes reparados en '{args.app}'")

    parser.set_defaults ( func = fix_packages )


  @staticmethod
  def inspectPackage ( subparsers : _SubParsersAction ) :
    parser = subparsers.add_parser ( "inspect-packages", help = "Inspecciona paquetes y __init__.py faltantes" )

    parser.add_argument ( "--app",                            required = True, help = "Nombre de la app a inspeccionar" )
    parser.add_argument ( "--fix",     action = "store_true",                  help = "Repara los __init__.py faltantes" )
    parser.add_argument ( "--dry-run", action = "store_true",                  help = "Simula sin modificar archivos" )

    def inspect_packages(args):
      from utils.package_inspector import PackageInspector

      app_path = Path("apps") / args.app
      if not app_path.exists():
          print(f"[ERROR] La app '{args.app}' no existe en apps/")
          return

      template_path = Path(__file__).parent / "resources" / "app" / "__init__.py"
      if not template_path.exists():
          print(f"[ERROR] Plantilla __init__.py no encontrada en {template_path}")
          return

      if args.dry_run:
          print(f"[DRY RUN] Explorando sin escribir archivos...\n")
          PackageInspector.report_missing(app_path)
      elif args.fix:
          print(f"[FIX MODE] Corrigiendo __init__.py faltantes...\n")
          PackageInspector.fix_missing_inits(app_path, template_path)
          print(f"\n✅ Reparación completada.")
      else:
          print(f"[INSPECCIÓN] Mostrando __init__.py faltantes (sin cambios):\n")
          PackageInspector.report_missing(app_path)

    parser.set_defaults ( func = inspect_packages )


  @staticmethod
  def about ( subparsers : _SubParsersAction ) :
    parser = subparsers.add_parser ( "about", help = "Muestra información general de Success CLI" )
    parser.set_defaults ( func = AboutCommand.show )


  @staticmethod
  def manifesto ( subparsers : _SubParsersAction ) :
    parser = subparsers.add_parser ( "manifesto", help = "Manifiesto filosófico del proyecto" )
    parser.set_defaults ( func = ManifestoCommand.show )


  @staticmethod
  def status ( subparsers : _SubParsersAction ) :
    parser = subparsers.add_parser ( "status", help = "Mostrar estado del sistema Success" )
    parser.set_defaults ( func = StatusCommand.run )




# python3 success-cli.py create-app prueba_view --app-type view
# main_project/apps/application/services/protocol/service/version/module/action
# python3 success-cli.py add-service \
#   --to-app prueba_view \
#   --protocol view \
#   --service chromadb \
#   --version v1

# python3 success-cli.py create-Action \
#   --to-app prueba_view \
#   --protocol view \
#   --service chromadb \
#   --version v1 \
#   --module admin \
#   --action dashboard \
#   --method POST GET
  
  
# python3 success-cli.py fix-packages --app=prueba_view


# python3 success-cli.py inspect-packages --app=prueba_view
# python3 success-cli.py inspect-packages --app=prueba_view --dry-run
# python3 success-cli.py inspect-packages --app=prueba_view --fix

# python3 success-cli.py --version

# python3 success-cli.py about

# python3 success-cli.py manifesto
