# Python Libraries / Librerías Python
from marshmallow.exceptions import ValidationError

# Success Libraries / Librerías Success
from success.engine.io.SuccessInput import SuccessInput

# Application Libraries / Librerías de la Aplicación
from apps.example.services.restful.simple_api.v1.api.public.get.Schema import Schema

# Preconditions / Precondiciones


class Input ( SuccessInput ) :


  def __init__ ( self ) -> None :
    super ().__init__ ()
    self._schema = Schema ()


  def parse ( self ) -> SuccessInput :
    try :
      self._parseInput ()

    except Exception as e :
      self._logger.log ( f"Error al procesar el request data: {e}", "EXCEPTION" )

    return self


  def validate ( self ) -> None :
    try :
      self._validatedData = self._schema.load ( self._rawData )

    except ValidationError as e :
      self._logger.log ( f"Error al procesar el request data: {e}", "EXCEPTION" )
      self._errors.extend ( [ f"{k}: {', '.join ( v )}" for k, v in e.messages.items () ] )

    return self
