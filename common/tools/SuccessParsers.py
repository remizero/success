# Python Libraries / Librerías Python
from datetime import datetime
from logging import LogRecord
import os
import traceback

# Success Libraries / Librerías Success

# Application Libraries / Librerías de la Aplicación

# Preconditions / Precondiciones


class SuccessParsers () :

  @staticmethod
  def exc_info ( exc_info ) -> tuple [ dict, str ] :
    """
    Procesa el contenido de record.exc_info para extraer info útil.
    Devuelve un dict con los datos para el template, y el nombre del template.
    """
    template = os.environ.get ( 'LOGGER_TEMPLATE_HTML_ERROR' )  # default
    context = {}

    if exc_info is None :
      return context, template

    if isinstance ( exc_info, tuple ) and len ( exc_info ) == 3 :
      exc_type, exc_value, exc_tb = exc_info
      context.update (
        {
          'exception_type': exc_type.__name__,
          'exception_message': str ( exc_value ),
          'traceback': ''.join ( traceback.format_exception ( exc_type, exc_value, exc_tb ) )
        }
      )
      template = os.environ.get ( 'LOGGER_TEMPLATE_HTML_EXCEPTION' )

    elif isinstance ( exc_info, BaseException ) :
      context.update (
        {
          'exception_type': type ( exc_info ).__name__,
          'exception_message': str ( exc_info ),
          'traceback': ''.join ( traceback.format_exception ( type ( exc_info ), exc_info, exc_info.__traceback__ ) )
        }
      )
      template = os.environ.get ( 'LOGGER_TEMPLATE_HTML_EXCEPTION' )

    else :
      context [ 'exception_raw' ] = str ( exc_info )

    return context, template

  @staticmethod
  def record ( record : LogRecord ) -> tuple [ dict, str ] :
    """
    Procesa el LogRecord completo para preparar el contexto de una plantilla HTML.
    """
    template = os.environ.get ( 'LOGGER_TEMPLATE_HTML_ERROR' )  # default

    context = {
      'levelname' : record.levelname,
      'message' : record.getMessage (),
      'pathname' : record.pathname,
      'lineno' : record.lineno,
      'module' : record.module,
      'funcName' : record.funcName,
      'asctime' : datetime.fromtimestamp ( record.created ).isoformat (),
      'logger_name' : record.name
    }

    if record.exc_info :
      exc_type, exc_value, exc_tb = record.exc_info
      context.update (
        {
          'exception_type' : exc_type.__name__,
          'exception_message' : str ( exc_value ),
          'traceback' : ''.join ( traceback.format_exception ( exc_type, exc_value, exc_tb ) )
        }
      )
      template = os.environ.get ( 'LOGGER_TEMPLATE_HTML_EXCEPTION' )

    return context, template

