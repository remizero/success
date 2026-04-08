# Python Libraries / Librerías Python
import argparse

# Application Libraries / Librerías de la Aplicación
from success.cli.Command import Command
from success.cli         import VERSION

# Preconditions / Precondiciones


def main () :
  parser     = argparse.ArgumentParser ( description = "Success CLI 🛠" )
  parser.add_argument ( '--version', action = 'version',    version = f'Success CLI {VERSION}', help = "Muestra la versión del sistema Success" )
  subparsers = parser.add_subparsers ( dest = "command" )

  # Subcomando: create-app
  Command.createApp ( subparsers )

  # Subcomando: add-service
  Command.addService ( subparsers )

  # Subcomando: create-Action
  Command.createEndpoint ( subparsers )

  # Subcomando: fix-package
  Command.fixPackage ( subparsers )

  # Subcomando: inspect-package
  Command.inspectPackage ( subparsers )

  # Subcomando: status
  Command.status ( subparsers )

  args = parser.parse_args ()

  if hasattr ( args, "func" ) :
    args.func ( args )

  else :
    parser.print_help ()
